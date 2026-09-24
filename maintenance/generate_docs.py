#!/usr/bin/env python3
"""
Regenerate the RDF serialisations published through GitHub Pages in docs/
from the authoritative OSO.ttl source.

The GitHub Pages site serves the /docs directory of the main branch
(https://emso-eric.github.io/oso-ontology/). Widoco generates the HTML
documentation, but its serialisation artefacts (ontology.ttl, ontology.nt,
ontology.owl, ontology.jsonld) are produced by loading the ontology *with its
owl:imports closure*, which inlines the imported vocabularies and merges the
owl:Ontology headers. In the 1.1.0 and 1.2.0 documentation runs this produced
a corrupted artefact: the owl:Ontology subject was taken from an imported
ontology (prov-o, then wgs84_pos) instead of https://w3id.org/earthsemantics/OSO.

This script replaces that step so the published artefacts are faithful
serialisations of OSO.ttl only:

    OSO.ttl   (authoritative source, untouched)
        |
        +-- docs/ontology.ttl      (exact copy of OSO.ttl)
        +-- docs/ontology.nt       (N-Triples)
        +-- docs/ontology.owl      (RDF/XML)
        +-- docs/ontology.jsonld   (JSON-LD)

RDFLib does not resolve owl:imports, so imported vocabularies can never leak
into the published artefacts, and the owl:Ontology header is preserved as-is.

Usage
-----
    python maintenance/generate_docs.py            # regenerate docs artefacts
    python maintenance/generate_docs.py --check    # verify only (CI mode)

Requirements: rdflib (>= 6).
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from rdflib import Graph, RDF, URIRef
from rdflib.compare import isomorphic
from rdflib.namespace import OWL

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE = REPO_ROOT / "OSO.ttl"
DOCS = REPO_ROOT / "docs"

OSO_IRI = URIRef("https://w3id.org/earthsemantics/OSO")

# (output filename, rdflib serializer format). ontology.ttl is handled
# separately: it is an exact copy of the authoritative source.
SERIALIZATIONS = [
    ("ontology.nt", "nt"),
    ("ontology.owl", "xml"),
    ("ontology.jsonld", "json-ld"),
]


def load_source() -> Graph:
    return Graph().parse(str(SOURCE), format="turtle")


def check_ontology_header(graph: Graph, label: str) -> list[str]:
    """The graph must declare exactly one owl:Ontology: the OSO IRI."""
    errors = []
    ont_subjects = {s for s in graph.subjects(RDF.type, OWL.Ontology) if isinstance(s, URIRef)}
    if ont_subjects != {OSO_IRI}:
        errors.append(
            f"{label}: expected a single owl:Ontology <{OSO_IRI}>, "
            f"found {sorted(str(s) for s in ont_subjects) or 'none'}"
        )
    if (OSO_IRI, OWL.versionIRI, None) not in graph:
        errors.append(f"{label}: missing owl:versionIRI on <{OSO_IRI}>")
    return errors


def check() -> list[str]:
    """Verify every docs artefact parses and is graph-equal to OSO.ttl."""
    errors = []
    source = load_source()
    errors += check_ontology_header(source, "OSO.ttl")

    published_ttl = DOCS / "ontology.ttl"
    if not published_ttl.exists():
        errors.append(f"{published_ttl}: file missing")
    else:
        g = Graph().parse(str(published_ttl), format="turtle")
        errors += check_ontology_header(g, "docs/ontology.ttl")
        if not isomorphic(source, g):
            errors.append("docs/ontology.ttl: graph differs from OSO.ttl (out of sync)")

    for fname, fmt in SERIALIZATIONS:
        path = DOCS / fname
        if not path.exists():
            errors.append(f"{path}: file missing")
            continue
        try:
            g = Graph().parse(str(path), format=fmt)
        except Exception as e:  # noqa: BLE001 - report parse failure, keep checking
            errors.append(f"{path}: parse error: {e}")
            continue
        errors += check_ontology_header(g, f"docs/{fname}")
        if not isomorphic(source, g):
            errors.append(f"docs/{fname}: graph differs from OSO.ttl (out of sync)")
    return errors


def generate() -> None:
    source = load_source()
    errors = check_ontology_header(source, "OSO.ttl")
    if errors:
        for e in errors:
            print(f"[docs] {e}", file=sys.stderr)
        sys.exit(1)

    shutil.copyfile(SOURCE, DOCS / "ontology.ttl")
    print(f"[docs] copied OSO.ttl -> docs/ontology.ttl ({len(source)} triples)")

    for fname, fmt in SERIALIZATIONS:
        source.serialize(destination=str(DOCS / fname), format=fmt, encoding="utf-8")
        print(f"[docs] wrote docs/{fname} ({fmt})")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="Verify artefacts without writing (CI mode)")
    args = parser.parse_args(argv)

    if args.check:
        errors = check()
        if errors:
            print("[docs] check FAILED:", file=sys.stderr)
            for e in errors:
                print(f"  - {e}", file=sys.stderr)
            return 1
        print("[docs] check OK: docs/ontology.* are faithful serialisations of OSO.ttl")
        return 0

    generate()
    print("[docs] done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
