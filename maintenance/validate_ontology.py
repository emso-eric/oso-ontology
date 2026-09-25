#!/usr/bin/env python3
"""
Validate the OSO ontology and its distribution artefacts.

This script is the blocking quality gate of the OSO CI pipeline. It enforces
three layers of checks on the repository artefacts:

1. Syntax layer
   Every RDF serialisation committed to the repository must parse cleanly:
   the authoritative source (OSO.ttl), the derived distributions at the
   repository root, the published docs/ artefacts, and every archived
   versions/<version>/ directory.

2. Identity layer
   The ontology must declare exactly one owl:Ontology resource:
   <https://w3id.org/earthsemantics/OSO>, carrying owl:versionIRI and
   owl:versionInfo. This guards against the corruption observed in the
   Widoco-generated docs/ontology.ttl artefacts (1.1.0/1.2.0), where an
   imported ontology IRI (prov-o, wgs84_pos) replaced the OSO IRI.

3. Consistency layer
   - OSO-ontology.ttl + OSO-instances.ttl must partition OSO.ttl exactly.
   - OSO.nt, OSO.owl, OSO.n3, OSO.trig, OSO.jsonld must be isomorphic to
     OSO.ttl.
   - docs/ontology.* must be isomorphic to OSO.ttl (same checks as
     generate_docs.py --check, duplicated here so this script can be used
     as a single entry point).

Usage
-----
    python maintenance/validate_ontology.py              # all checks
    python maintenance/validate_ontology.py --no-versions # skip versions/ dirs

Requirements: rdflib (>= 6).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rdflib import Dataset, Graph, RDF, URIRef
from rdflib.compare import isomorphic
from rdflib.namespace import OWL

REPO_ROOT = Path(__file__).resolve().parent.parent
OSO_IRI = URIRef("https://w3id.org/earthsemantics/OSO")

# (path relative to repo root, rdflib parser format)
ROOT_SERIALIZATIONS = [
    ("OSO.nt", "nt"),
    ("OSO.owl", "xml"),
    ("OSO.n3", "n3"),
    ("OSO.jsonld", "json-ld"),
]

DOCS_SERIALIZATIONS = [
    ("docs/ontology.nt", "nt"),
    ("docs/ontology.owl", "xml"),
    ("docs/ontology.jsonld", "json-ld"),
]

# Other Turtle sources parsed for syntax + ontology-header sanity only.
EXTRA_TURTLE = [
    "OSO-dcat.ttl",
    "OSO-shacl.ttl",
    "OSO-void.ttl",
    "OSO-voId.ttl",
]

VERSION_FORMATS = {
    ".ttl": "turtle",
    ".nt": "nt",
    ".owl": "xml",
    ".n3": "n3",
    ".trig": "trig",
    ".jsonld": "json-ld",
}


def parse(path: Path, fmt: str) -> Graph:
    """Parse an RDF file; TriG goes through ConjunctiveGraph then flattens."""
    if fmt == "trig":
        ds = Dataset().parse(str(path), format="trig")
        g = Graph()
        for s, p, o, _ in ds.quads():
            g.add((s, p, o))
        return g
    return Graph().parse(str(path), format=fmt)


def check_ontology_header(graph: Graph, label: str, expect_version: bool) -> list[str]:
    errors = []
    ont_subjects = {s for s in graph.subjects(RDF.type, OWL.Ontology) if isinstance(s, URIRef)}
    if expect_version:
        if ont_subjects != {OSO_IRI}:
            errors.append(
                f"{label}: expected a single owl:Ontology <{OSO_IRI}>, "
                f"found {sorted(str(s) for s in ont_subjects) or 'none'}"
            )
        for prop, name in [(OWL.versionIRI, "owl:versionIRI"), (OWL.versionInfo, "owl:versionInfo")]:
            if (OSO_IRI, prop, None) not in graph:
                errors.append(f"{label}: missing {name} on <{OSO_IRI}>")
        # OWL API discards candidate ontology IRIs used as annotation values
        # (owlcs/owlapi#1080): a self-reference makes Widoco/FOOPS report an
        # imported ontology IRI instead of OSO.
        self_refs = sorted(str(p) for p in graph.predicates(OSO_IRI, OSO_IRI))
        if self_refs:
            errors.append(f"{label}: self-referencing annotation(s) on <{OSO_IRI}>: {self_refs}")
    else:
        # Metadata files may declare their own ontology headers; they must
        # never redeclare the OSO ontology IRI under another subject.
        leaked = [s for s in ont_subjects if str(s).startswith("http://www.w3.org/2003/01/geo/")]
        if leaked:
            errors.append(f"{label}: foreign ontology IRI leaked: {leaked}")
    return errors


def check_bundle(base: Path) -> tuple[Graph | None, list[str]]:
    """Check a distribution bundle (repo root or versions/<v>/).

    Returns the parsed OSO.ttl (None if unparseable) and the list of errors:
    ontology identity, exact TBox/ABox partition, and isomorphism of every
    serialisation with OSO.ttl.
    """
    errors: list[str] = []
    prefix = "" if base == REPO_ROOT else f"{base.relative_to(REPO_ROOT)}/"

    try:
        source = Graph().parse(str(base / "OSO.ttl"), format="turtle")
    except Exception as e:  # noqa: BLE001
        return None, [f"{prefix}OSO.ttl: parse error: {e}"]
    errors += check_ontology_header(source, f"{prefix}OSO.ttl", expect_version=True)

    # --- TBox/ABox partition ---
    try:
        tbox = Graph().parse(str(base / "OSO-ontology.ttl"), format="turtle")
        abox = Graph().parse(str(base / "OSO-instances.ttl"), format="turtle")
    except Exception as e:  # noqa: BLE001
        errors.append(f"{prefix}partition: parse error: {e}")
        tbox = abox = None
    if tbox is not None:
        if set(tbox) & set(abox):
            errors.append(f"{prefix}OSO-ontology.ttl and OSO-instances.ttl overlap.")
        union = Graph()
        for t in tbox:
            union.add(t)
        for t in abox:
            union.add(t)
        if not isomorphic(union, source):
            errors.append(f"{prefix}OSO-ontology.ttl ∪ OSO-instances.ttl is not isomorphic to OSO.ttl.")
        # An individual (typed owl:NamedIndividual, no OWL meta-class type)
        # must live in the ABox; the ontology IRI itself is exempt.
        metaclasses = {OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty,
                       OWL.AnnotationProperty, OWL.Ontology}
        leaked = {
            s for s in tbox.subjects(RDF.type, OWL.NamedIndividual)
            if s != OSO_IRI and metaclasses.isdisjoint(tbox.objects(s, RDF.type))
        }
        if leaked:
            errors.append(
                f"{prefix}OSO-ontology.ttl: {len(leaked)} individual(s) leaked into the TBox "
                f"(e.g. {sorted(map(str, leaked))[0]})."
            )
        split = {s for s in tbox.subjects() if isinstance(s, URIRef)} & {
            s for s in abox.subjects() if isinstance(s, URIRef)
        }
        if split:
            errors.append(
                f"{prefix}OSO-ontology.ttl / OSO-instances.ttl: {len(split)} subject(s) "
                f"described in both files (e.g. {sorted(map(str, split))[0]})."
            )

    # --- Serialisations must mirror the source ---
    for rel, fmt in ROOT_SERIALIZATIONS + [("OSO.trig", "trig")]:
        path = base / rel
        if not path.exists():
            errors.append(f"{prefix}{rel}: file missing")
            continue
        try:
            g = parse(path, fmt)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{prefix}{rel}: parse error: {e}")
            continue
        if not isomorphic(g, source):
            errors.append(f"{prefix}{rel}: graph differs from OSO.ttl (out of sync)")

    return source, errors


def validate(include_versions: bool) -> tuple[list[str], list[str]]:
    warnings: list[str] = []
    source, errors = check_bundle(REPO_ROOT)
    if source is None:
        return errors, warnings

    # --- Published docs artefacts must mirror the source ---
    for rel, fmt in [("docs/ontology.ttl", "turtle")] + DOCS_SERIALIZATIONS:
        path = REPO_ROOT / rel
        if not path.exists():
            errors.append(f"{rel}: file missing")
            continue
        try:
            g = parse(path, fmt)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{rel}: parse error: {e}")
            continue
        errors += check_ontology_header(g, rel, expect_version=True)
        if not isomorphic(g, source):
            errors.append(f"{rel}: graph differs from OSO.ttl (out of sync)")

    # --- Metadata Turtle files: syntax only ---
    for rel in EXTRA_TURTLE:
        path = REPO_ROOT / rel
        if path.exists():
            try:
                Graph().parse(str(path), format="turtle")
            except Exception as e:  # noqa: BLE001
                errors.append(f"{rel}: parse error: {e}")

    # --- Archived versions: syntax check on every RDF file ---
    # Historical archives are reported as warnings, not errors: some were
    # exported by Protege and contain defects that cannot be repaired
    # without rewriting a published release (e.g. versions/1.0.0/OSO.ttl).
    if include_versions:
        versions_dir = REPO_ROOT / "versions"
        for path in sorted(versions_dir.rglob("*")):
            if not path.is_file() or path.suffix not in VERSION_FORMATS:
                continue
            rel = path.relative_to(REPO_ROOT)
            try:
                parse(path, VERSION_FORMATS[path.suffix])
            except Exception as e:  # noqa: BLE001
                warnings.append(f"{rel}: parse error: {e}")

    return errors, warnings


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--no-versions", action="store_true", help="Skip syntax checks on versions/")
    parser.add_argument("--strict-versions", action="store_true",
                        help="Treat versions/ parse errors as failures")
    args = parser.parse_args(argv)

    errors, warnings = validate(include_versions=not args.no_versions)
    for w in warnings:
        print(f"[validate] WARNING: {w}")
    if args.strict_versions:
        errors += warnings
    if errors:
        print("[validate] FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print("[validate] OK: OSO.ttl and all artefacts are consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
