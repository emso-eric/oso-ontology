#!/usr/bin/env python3
"""
Verify the artefacts actually published on GitHub Pages.

Runs after every GitHub Pages build (see .github/workflows/verify-published.yml)
and on demand. It downloads each published serialisation and checks, end to end,
what external consumers (LOV, FOOPS, catalogues) will actually read:

- the file parses as the advertised format;
- it declares exactly one owl:Ontology: <https://w3id.org/earthsemantics/OSO>;
- its graph is isomorphic to the authoritative OSO.ttl.

Usage
-----
    python maintenance/verify_published.py
    python maintenance/verify_published.py --base-url https://emso-eric.github.io/oso-ontology

Requirements: rdflib (>= 6).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.request import Request, urlopen

from rdflib import Graph, RDF, URIRef
from rdflib.compare import isomorphic
from rdflib.namespace import OWL

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BASE = "https://emso-eric.github.io/oso-ontology"
OSO_IRI = URIRef("https://w3id.org/earthsemantics/OSO")
USER_AGENT = "OSO-release-pipeline/1.0 (+https://github.com/emso-eric/oso-ontology)"

ARTEFACTS = [
    ("ontology.ttl", "turtle"),
    ("ontology.nt", "nt"),
    ("ontology.owl", "xml"),
    ("ontology.jsonld", "json-ld"),
]


def check_header(graph: Graph, label: str) -> list[str]:
    errors = []
    ont_subjects = {s for s in graph.subjects(RDF.type, OWL.Ontology) if isinstance(s, URIRef)}
    if ont_subjects != {OSO_IRI}:
        errors.append(
            f"{label}: expected a single owl:Ontology <{OSO_IRI}>, "
            f"found {sorted(str(s) for s in ont_subjects) or 'none'}"
        )
    return errors


def verify(base_url: str) -> list[str]:
    errors: list[str] = []
    source = Graph().parse(str(REPO_ROOT / "OSO.ttl"), format="turtle")

    for name, fmt in ARTEFACTS:
        url = f"{base_url.rstrip('/')}/{name}"
        label = f"{url}"
        try:
            with urlopen(Request(url, headers={"User-Agent": USER_AGENT}), timeout=60) as r:
                data = r.read()
        except Exception as e:  # noqa: BLE001
            errors.append(f"{label}: fetch error: {e}")
            continue
        try:
            g = Graph().parse(data=data, format=fmt)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{label}: parse error: {e}")
            continue
        errors += check_header(g, label)
        if not isomorphic(source, g):
            errors.append(f"{label}: published graph differs from OSO.ttl")
        else:
            print(f"[verify] {name}: OK ({len(g)} triples)")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base-url", default=DEFAULT_BASE, help="Published docs base URL")
    args = parser.parse_args(argv)

    errors = verify(args.base_url)
    if errors:
        print("[verify] FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print("[verify] OK: published artefacts match OSO.ttl")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
