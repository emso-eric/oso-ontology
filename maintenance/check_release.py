#!/usr/bin/env python3
"""
Release gate for an OSO version, run before a GitHub release is created.

A release publishes the files committed under versions/<version>/ as-is:
nothing is regenerated at release time, so the assets are byte-identical to
the repository archive and to the checksums written here.

Checks
------
1. Bundle     every expected file is present; identity, TBox/ABox partition
              and serialisation isomorphism (validate_ontology.check_bundle).
2. Source     versions/<version>/OSO.ttl is byte-identical to the root
              OSO.ttl (the release is cut from the current source).
3. Versioning owl:versionIRI = .../OSO/<version>/, owl:versionInfo starts
              with <version>, owl:priorVersion = the previous release, and
              <version> is newer than every existing release tag.
4. Metadata   OSO-dcat.ttl declares dcat:version, dcterms:hasVersion and
              pav:previousVersion consistently; CITATION.cff has the same
              version; dcterms:modified is present on the ontology; the
              Zenodo version DOI is declared once, identically in OSO.ttl and
              OSO-dcat.ttl, and differs from the concept and previous DOIs.
5. Tag        (--tag) the git tag is v<version>.

Usage
-----
    python maintenance/check_release.py --version 1.2.1
    python maintenance/check_release.py --version 1.2.1 --tag v1.2.1 \\
        --checksums dist/SHA256SUMS

Requirements: rdflib (>= 7), PyYAML.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

import yaml
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL

from validate_ontology import OSO_IRI, REPO_ROOT, check_bundle
from zenodo import DOI_RE

CONCEPT_DOI = "10.5281/zenodo.19497912"
DCAT = Namespace("http://www.w3.org/ns/dcat#")
PAV = Namespace("http://purl.org/pav/")

RELEASE_FILES = [
    "OSO.ttl",
    "OSO-ontology.ttl",
    "OSO-instances.ttl",
    "OSO.owl",
    "OSO.nt",
    "OSO.n3",
    "OSO.trig",
    "OSO.jsonld",
    "OSO-shacl.ttl",
    "OSO-dcat.ttl",
    "OSO-void.ttl",
    "README.md",
]

SEMVER = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)$")


def version_iri(version: str) -> URIRef:
    return URIRef(f"https://w3id.org/earthsemantics/OSO/{version}/")


def parse_semver(text: str) -> tuple[int, int, int] | None:
    m = SEMVER.match(text)
    return tuple(int(x) for x in m.groups()) if m else None


def release_tags() -> list[str]:
    out = subprocess.run(["git", "tag", "--list"], cwd=REPO_ROOT, check=True,
                         capture_output=True, text=True).stdout
    return [t for t in out.split() if parse_semver(t)]


def previous_release(version: str, tags: list[str]) -> str | None:
    """Highest released version strictly lower than `version`."""
    current = parse_semver(version)
    older = [v for v in map(parse_semver, tags) if v is not None and v < current]
    return ".".join(map(str, max(older))) if older else None


def check_versioning(source: Graph, version: str, tags: list[str]) -> list[str]:
    errors = []
    current = parse_semver(version)
    if current is None:
        return [f"invalid version {version!r} (expected X.Y.Z)"]

    tag_versions = {v for v in map(parse_semver, tags) if v is not None}
    if current in tag_versions:
        errors.append(f"version {version} is already tagged; releases are immutable")
    newer = sorted(".".join(map(str, v)) for v in tag_versions if v > current)
    if newer:
        errors.append(f"version {version} is older than existing release(s) {newer}")

    iris = set(source.objects(OSO_IRI, OWL.versionIRI))
    if iris != {version_iri(version)}:
        errors.append(f"owl:versionIRI is {sorted(map(str, iris))}, expected <{version_iri(version)}>")

    infos = [str(v) for v in source.objects(OSO_IRI, OWL.versionInfo)]
    if not infos or not all(i.startswith(version) for i in infos):
        errors.append(f"every owl:versionInfo must start with {version!r} (found {len(infos)})")

    prev = previous_release(version, [t for t in tags if parse_semver(t) != current])
    priors = set(source.objects(OSO_IRI, OWL.priorVersion))
    if prev and priors != {version_iri(prev)}:
        errors.append(f"owl:priorVersion is {sorted(map(str, priors))}, expected <{version_iri(prev)}>")

    if (OSO_IRI, DCTERMS.modified, None) not in source:
        errors.append("dcterms:modified missing on the ontology")
    return errors


def zenodo_dois(graph: Graph) -> set[str]:
    return {str(o).removeprefix("https://doi.org/")
            for o in graph.objects(OSO_IRI, DCTERMS.identifier) if DOI_RE.match(str(o))}


def check_doi(source: Graph, dcat: Graph, prev: str | None) -> list[str]:
    """The version DOI (reserved on Zenodo) must be declared once, identically,
    in OSO.ttl and OSO-dcat.ttl, and be new: zenodo.py publishes to it."""
    errors = []
    src, dc = zenodo_dois(source), zenodo_dois(dcat)
    if len(dc) != 1:
        return [f"OSO-dcat.ttl: expected one Zenodo version DOI (dcterms:identifier), found {sorted(dc)}"]
    if src != dc:
        errors.append(f"OSO.ttl dcterms:identifier {sorted(src)} differs from OSO-dcat.ttl {sorted(dc)}")
    if dc == {CONCEPT_DOI}:
        errors.append("the version DOI must not be the concept DOI")
    prev_dcat = REPO_ROOT / "versions" / (prev or "") / "OSO-dcat.ttl"
    if prev and prev_dcat.is_file() and zenodo_dois(Graph().parse(str(prev_dcat), format="turtle")) == dc:
        errors.append(f"version DOI {sorted(dc)[0]} is the DOI of the previous release {prev}")
    return errors


def check_metadata(vdir: Path, version: str, prev: str | None) -> list[str]:
    errors = []
    dcat = Graph().parse(str(vdir / "OSO-dcat.ttl"), format="turtle")
    errors += check_doi(Graph().parse(str(vdir / "OSO.ttl"), format="turtle"), dcat, prev)
    if (OSO_IRI, DCAT.version, Literal(version)) not in dcat:
        errors.append(f"OSO-dcat.ttl: dcat:version {version!r} missing on <{OSO_IRI}>")
    if (OSO_IRI, DCTERMS.hasVersion, version_iri(version)) not in dcat:
        errors.append(f"OSO-dcat.ttl: dcterms:hasVersion <{version_iri(version)}> missing")
    if prev and (OSO_IRI, PAV.previousVersion, version_iri(prev)) not in dcat:
        errors.append(f"OSO-dcat.ttl: pav:previousVersion <{version_iri(prev)}> missing")
    Graph().parse(str(vdir / "OSO-void.ttl"), format="turtle")

    cff = yaml.safe_load((REPO_ROOT / "CITATION.cff").read_text(encoding="utf-8"))
    if str(cff.get("version")) != version:
        errors.append(f"CITATION.cff: version is {cff.get('version')!r}, expected {version!r}")
    return errors


def write_checksums(vdir: Path, destination: Path) -> None:
    lines = [f"{hashlib.sha256((vdir / f).read_bytes()).hexdigest()}  {f}" for f in RELEASE_FILES]
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def check_release(version: str, tag: str | None, tags: list[str]) -> list[str]:
    vdir = REPO_ROOT / "versions" / version
    missing = [f for f in RELEASE_FILES if not (vdir / f).is_file()]
    if missing:
        return [f"versions/{version}/: missing {missing}"]

    source, errors = check_bundle(vdir)
    if source is None:
        return errors

    if (vdir / "OSO.ttl").read_bytes() != (REPO_ROOT / "OSO.ttl").read_bytes():
        errors.append(f"versions/{version}/OSO.ttl differs from the root OSO.ttl")

    errors += check_versioning(source, version, tags)
    prev = previous_release(version, tags)
    errors += check_metadata(vdir, version, prev)

    if tag is not None and tag != f"v{version}":
        errors.append(f"tag {tag!r} does not match version (expected 'v{version}')")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--version", required=True, help="Version to release, e.g. 1.2.1")
    parser.add_argument("--tag", help="Git tag being released (checked against --version)")
    parser.add_argument("--checksums", type=Path, help="Write a SHA256SUMS file for the release assets")
    args = parser.parse_args(argv)

    # The tag being released is excluded from the "already tagged" check.
    tags = [t for t in release_tags() if t != args.tag]
    errors = check_release(args.version, args.tag, tags)
    if errors:
        print(f"[release] {args.version}: FAILED", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    if args.checksums:
        write_checksums(REPO_ROOT / "versions" / args.version, args.checksums)
        print(f"[release] wrote {args.checksums}")
    print(f"[release] {args.version}: OK ({len(RELEASE_FILES)} assets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
