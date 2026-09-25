#!/usr/bin/env python3
"""
Zenodo deposit of an OSO release (InvenioRDM REST API).

Each OSO release is a new version of the Zenodo concept record, carrying
exactly the files of the GitHub release. The version DOI is written into
the release files (OSO.ttl, OSO-dcat.ttl, CITATION.cff), so it is reserved
before the release is built:

    reserve   create the new-version draft of the concept, set its version
              and reserve its DOI. Run once while preparing versions/X.Y.Z/.
    publish   upload the release files to that draft, verify every checksum
              against SHA256SUMS and the local bytes, then publish. The draft
              is located from the DOI declared in versions/X.Y.Z/OSO-dcat.ttl
              (Zenodo DOIs are 10.5281/zenodo.<record id>), so no state is
              kept between the two steps.
    verify    check that a published Zenodo version carries exactly the
              release files (used after publication and by monitoring).

Environment
-----------
    ZENODO_TOKEN   personal access token (scopes deposit:write, deposit:actions)
    ZENODO_URL     https://zenodo.org (default) or https://sandbox.zenodo.org

Usage
-----
    python maintenance/zenodo.py reserve --version 1.2.1 --record 22030990
    python maintenance/zenodo.py publish --version 1.2.1 --files dist/ \\
        --checksums dist/SHA256SUMS --release-url https://github.com/.../v1.2.1
    python maintenance/zenodo.py verify --version 1.2.1 --files dist/ \\
        --checksums dist/SHA256SUMS

Requirements: requests, rdflib (>= 7).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
import re
import sys
from pathlib import Path

import requests
from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

REPO_ROOT = Path(__file__).resolve().parent.parent
OSO_IRI = URIRef("https://w3id.org/earthsemantics/OSO")
RDM_JSON = "application/vnd.inveniordm.v1+json"
DOI_RE = re.compile(r"^(?:https://doi\.org/)?10\.5281/zenodo\.(\d+)$")


class ZenodoError(Exception):
    pass


# --- pure helpers (unit tested) ---------------------------------------------

def record_id_from_doi(doi: str) -> str:
    m = DOI_RE.match(doi.strip())
    if not m:
        raise ZenodoError(f"not a Zenodo DOI: {doi!r}")
    return m.group(1)


def read_checksums(path: Path) -> dict[str, str]:
    """Parse a SHA256SUMS file into {filename: sha256}."""
    sums = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            digest, name = line.split(maxsplit=1)
            sums[name.strip()] = digest
    return sums


def local_digests(files_dir: Path, names) -> dict[str, dict[str, str]]:
    out = {}
    for name in names:
        data = (files_dir / name).read_bytes()
        out[name] = {"sha256": hashlib.sha256(data).hexdigest(), "md5": hashlib.md5(data).hexdigest()}
    return out


def compare_files(expected_sha256: dict[str, str], local: dict[str, dict[str, str]],
                  remote_md5: dict[str, str]) -> list[str]:
    """Errors if local bytes or remote Zenodo files differ from SHA256SUMS."""
    errors = []
    for name, sha in expected_sha256.items():
        if local[name]["sha256"] != sha:
            errors.append(f"{name}: local sha256 differs from SHA256SUMS")
        if name not in remote_md5:
            errors.append(f"{name}: missing on Zenodo")
        elif remote_md5[name] != local[name]["md5"]:
            errors.append(f"{name}: Zenodo md5 {remote_md5[name]} != local {local[name]['md5']}")
    extra = sorted(set(remote_md5) - set(expected_sha256))
    if extra:
        errors.append(f"unexpected file(s) on Zenodo: {extra}")
    return errors


def declared_doi(version: str) -> str:
    """Version DOI declared in versions/<version>/OSO-dcat.ttl."""
    dcat = Graph().parse(str(REPO_ROOT / "versions" / version / "OSO-dcat.ttl"), format="turtle")
    dois = [str(o) for o in dcat.objects(OSO_IRI, DCTERMS.identifier) if DOI_RE.match(str(o))]
    if len(dois) != 1:
        raise ZenodoError(f"expected one Zenodo DOI on <{OSO_IRI}> in OSO-dcat.ttl, found {dois}")
    return dois[0].removeprefix("https://doi.org/")


# --- API client ----------------------------------------------------------------

class Zenodo:
    def __init__(self, base_url: str, token: str | None):
        self.base = base_url.rstrip("/") + "/api"
        self.session = requests.Session()
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    def call(self, method: str, path: str, **kwargs):
        # Record/draft endpoints serve the InvenioRDM schema only with the RDM
        # media type (plain JSON returns Zenodo's legacy format); file
        # endpoints only accept application/json.
        headers = {"Accept": "application/json" if "/files" in path else RDM_JSON}
        headers.update(kwargs.pop("headers", {}))
        r = self.session.request(method, self.base + path, headers=headers, timeout=120, **kwargs)
        if r.status_code >= 400:
            raise ZenodoError(f"{method} {path} -> {r.status_code}: {r.text[:500]}")
        return r.json() if r.content and "json" in r.headers.get("Content-Type", "") else None

    def draft(self, rid: str) -> dict:
        return self.call("GET", f"/records/{rid}/draft")

    def record(self, rid: str) -> dict:
        return self.call("GET", f"/records/{rid}")

    def files(self, rid: str, draft: bool) -> dict[str, str]:
        path = f"/records/{rid}/draft/files" if draft else f"/records/{rid}/files"
        entries = self.call("GET", path).get("entries", [])
        return {e["key"]: e["checksum"].removeprefix("md5:") for e in entries if e.get("checksum")}

    def reserve(self, record_id: str, version: str) -> tuple[str, str]:
        latest = self.call("GET", f"/records/{record_id}/versions/latest")
        if latest["metadata"].get("version") == version:
            raise ZenodoError(f"version {version} is already published ({latest['id']})")
        draft = self.call("POST", f"/records/{latest['id']}/versions")
        rid = draft["id"]
        draft["metadata"]["version"] = version
        draft["metadata"].pop("publication_date", None)
        self.call("PUT", f"/records/{rid}/draft",
                  json={"metadata": draft["metadata"], "files": {"enabled": True}},
                  headers={"Content-Type": "application/json"})
        pids = self.call("POST", f"/records/{rid}/draft/pids/doi")["pids"]
        return rid, pids["doi"]["identifier"]

    def upload(self, rid: str, files_dir: Path, names) -> None:
        for key in self.files(rid, draft=True):
            self.call("DELETE", f"/records/{rid}/draft/files/{key}")
        self.call("POST", f"/records/{rid}/draft/files", json=[{"key": n} for n in names],
                  headers={"Content-Type": "application/json"})
        for name in names:
            with open(files_dir / name, "rb") as fh:
                self.call("PUT", f"/records/{rid}/draft/files/{name}/content", data=fh,
                          headers={"Content-Type": "application/octet-stream"})
            self.call("POST", f"/records/{rid}/draft/files/{name}/commit")

    def finalize_metadata(self, rid: str, version: str, release_url: str | None) -> None:
        draft = self.draft(rid)
        md = draft["metadata"]
        md["version"] = version
        md["publication_date"] = dt.date.today().isoformat()
        if release_url:
            related = [r for r in md.get("related_identifiers", []) if r.get("identifier") != release_url]
            related.append({"identifier": release_url, "scheme": "url",
                            "relation_type": {"id": "issupplementto"}})
            md["related_identifiers"] = related
        self.call("PUT", f"/records/{rid}/draft", json={"metadata": md, "files": {"enabled": True}},
                  headers={"Content-Type": "application/json"})

    def publish(self, rid: str) -> dict:
        return self.call("POST", f"/records/{rid}/draft/actions/publish")


# --- commands --------------------------------------------------------------------

def client(require_token: bool = True) -> Zenodo:
    token = os.environ.get("ZENODO_TOKEN")
    if require_token and not token:
        raise ZenodoError("ZENODO_TOKEN is not set")
    return Zenodo(os.environ.get("ZENODO_URL", "https://zenodo.org"), token)


def cmd_reserve(args) -> None:
    rid, doi = client().reserve(args.record, args.version)
    print(f"[zenodo] draft {rid} for {args.version}: reserved DOI {doi}")


def check(z: Zenodo, rid: str, args, draft: bool) -> list[str]:
    expected = read_checksums(args.checksums)
    return compare_files(expected, local_digests(args.files, expected), z.files(rid, draft=draft))


def cmd_publish(args) -> None:
    z = client()
    doi = declared_doi(args.version)
    rid = record_id_from_doi(doi)
    try:
        draft = z.draft(rid)
    except ZenodoError:
        # No draft left: the version may already be published (re-run).
        errors = check(z, rid, args, draft=False)
        if errors:
            raise ZenodoError(f"no draft {rid} and the published record does not match:\n  - "
                              + "\n  - ".join(errors)) from None
        print(f"[zenodo] {args.version} already published at https://doi.org/{doi}; files verified")
        return
    if draft["metadata"].get("version") != args.version:
        raise ZenodoError(f"draft {rid} has version {draft['metadata'].get('version')!r}, expected {args.version!r}")
    if draft.get("pids", {}).get("doi", {}).get("identifier") != doi:
        raise ZenodoError(f"draft {rid} DOI does not match the declared DOI {doi}")

    names = list(read_checksums(args.checksums))
    z.upload(rid, args.files, names)
    errors = check(z, rid, args, draft=True)
    if errors:
        raise ZenodoError("uploaded files do not match the release:\n  - " + "\n  - ".join(errors))
    z.finalize_metadata(rid, args.version, args.release_url)
    z.publish(rid)
    errors = check(z, rid, args, draft=False)
    if errors:
        raise ZenodoError("published record does not match the release:\n  - " + "\n  - ".join(errors))
    print(f"[zenodo] published {args.version}: https://doi.org/{doi} ({len(names)} files verified)")


def cmd_verify(args) -> None:
    z = client(require_token=False)
    doi = declared_doi(args.version)
    errors = check(z, record_id_from_doi(doi), args, draft=False)
    if errors:
        raise ZenodoError("Zenodo record does not match the release:\n  - " + "\n  - ".join(errors))
    print(f"[zenodo] {args.version}: https://doi.org/{doi} matches the release files")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("reserve", help="create the new-version draft and reserve its DOI")
    p.add_argument("--version", required=True)
    p.add_argument("--record", required=True, help="any published record id of the concept")
    p.set_defaults(func=cmd_reserve)

    for name, func in [("publish", cmd_publish), ("verify", cmd_verify)]:
        p = sub.add_parser(name)
        p.add_argument("--version", required=True)
        p.add_argument("--files", type=Path, required=True, help="directory holding the release files")
        p.add_argument("--checksums", type=Path, required=True, help="SHA256SUMS of the release")
        if name == "publish":
            p.add_argument("--release-url", help="GitHub release URL, linked as isSupplementTo")
        p.set_defaults(func=func)

    args = parser.parse_args(argv)
    try:
        args.func(args)
    except ZenodoError as e:
        print(f"[zenodo] ERROR: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
