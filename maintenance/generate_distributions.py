#!/usr/bin/env python3
"""
Generate OSO distribution artifacts for a given version from its authoritative
OSO.ttl source.

The OSO release workflow (see maintenance/Release_Workflow.md) describes OSO.ttl
as the authoritative source from which distribution artifacts are derived with
RDFLib. This script automates that derivation for a version directory:

    versions/<version>/OSO.ttl            (authoritative source, untouched)
        |
        +-- OSO-ontology.ttl              (TBox: ontology model, no individuals)
        +-- OSO-instances.ttl             (ABox: individuals/instance data)
        +-- OSO.owl                       (RDF/XML serialization of the full graph)
        +-- OSO.nt                        (N-Triples serialization of the full graph)
        +-- OSO.n3                        (Notation3 serialization of the full graph)
        +-- OSO.trig                      (TriG serialization of the full graph)
        +-- OSO.jsonld                    (JSON-LD serialization of the full graph)

TBox/ABox partition
-------------------
A subject is considered an *individual* (ABox) when it has at least one rdf:type
and none of its types is an OWL/RDF schema meta-class (owl:Class, owl:ObjectProperty,
owl:DatatypeProperty, owl:AnnotationProperty, owl:Ontology, owl:Restriction, ...).
Everything else (the ontology IRI, classes, properties, restrictions, anonymous
unionOf/intersectionOf class expressions, rdf:List nodes, ...) is kept in the TBox.

This keeps the ontology header (versionIRI, versionInfo, priorVersion, ...) in the
TBox even when the ontology IRI is also typed owl:NamedIndividual (as happens in
some OSO versions exported from Protege).

Usage
-----
    python maintenance/generate_distributions.py --version 1.0.2
    python maintenance/generate_distributions.py --version 1.0.2 --dry-run
    python maintenance/generate_distributions.py --version 1.0.2 --source-dir versions

Requirements: rdflib (>= 6).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rdflib import BNode, Graph, RDF, URIRef
from rdflib.namespace import OWL

# OWL/RDF meta-classes: a subject typed with one of these is a TBox entity.
TBOX_METACLASSES = {
    OWL.Class,
    OWL.ObjectProperty,
    OWL.DatatypeProperty,
    OWL.AnnotationProperty,
    OWL.Ontology,
    OWL.Restriction,
    OWL.AsymmetricProperty,
    OWL.SymmetricProperty,
    OWL.TransitiveProperty,
    OWL.FunctionalProperty,
    OWL.InverseFunctionalProperty,
    OWL.IrreflexiveProperty,
    OWL.ReflexiveProperty,
    URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"),
    URIRef("http://www.w3.org/2000/01/rdf-schema#Datatype"),
}

# (output filename, rdflib serializer format)
SERIALIZATIONS = [
    ("OSO.owl", "xml"),
    ("OSO.nt", "nt"),
    ("OSO.n3", "n3"),
    ("OSO.trig", "trig"),
    ("OSO.jsonld", "json-ld"),
]


def partition_tbox_abox(graph: Graph):
    """Return (tbox_graph, abox_graph) partitioned from `graph`.

    Triples are grouped into blank-node-connected components first: a bnode
    must appear in exactly one partition, otherwise serialising TBox and
    ABox to separate files splits shared bnodes (adms:identifier, vcard
    contact points, shared owl:unionOf lists, ...) and the union is no
    longer isomorphic to the source. A component goes to the ABox only if
    all its URIRef members are individuals.
    """
    individuals = set()
    for subject in set(graph.subjects()):
        types = list(graph.objects(subject, RDF.type))
        # An individual has at least one type, none of which is a meta-class.
        if types and not any(t in TBOX_METACLASSES for t in types):
            individuals.add(subject)

    # Union-find over components linked by blank nodes.
    parent = {}

    def find(node):
        parent.setdefault(node, node)
        while parent[node] is not node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for s, p, o in graph:
        find(s)
        find(o)
        if isinstance(s, BNode) or isinstance(o, BNode):
            parent[find(o)] = find(s)

    component_members = {}
    for node in parent:
        component_members.setdefault(find(node), set()).add(node)

    abox_components = set()
    for root, members in component_members.items():
        urirefs = [m for m in members if isinstance(m, URIRef)]
        if urirefs and all(m in individuals for m in urirefs):
            abox_components.add(root)

    tbox = Graph()
    abox = Graph()
    for s, p, o in graph:
        (abox if find(s) in abox_components else tbox).add((s, p, o))

    # Carry over namespace bindings so serializations reuse the source prefixes.
    for prefix, ns in graph.namespaces():
        tbox.bind(prefix, ns)
        abox.bind(prefix, ns)
    return tbox, abox


def serialize(graph: Graph, destination: Path, fmt: str) -> None:
    graph.serialize(destination=str(destination), format=fmt)


def validate(source: Graph, tbox: Graph, abox: Graph, version_iri_expected: str) -> list[str]:
    """Return a list of validation error messages (empty == OK)."""
    errors = []
    oso = URIRef("https://w3id.org/earthsemantics/OSO")

    # Partition must be exact and disjoint.
    if set(source) != set(tbox) | set(abox):
        errors.append("TBox ∪ ABox != source graph (partition is not exact).")
    if set(tbox) & set(abox):
        errors.append("TBox and ABox overlap.")

    # TBox must carry the ontology version metadata.
    version_iris = list(tbox.objects(oso, OWL.versionIRI))
    if not version_iris:
        errors.append("TBox is missing owl:versionIRI on the ontology IRI.")
    elif str(version_iris[0]) != version_iri_expected:
        errors.append(
            f"TBox versionIRI is {version_iris[0]!r}, expected {version_iri_expected!r}."
        )

    # No ABox individual should leak into the TBox.
    leaked = [
        s
        for s in set(tbox.subjects())
        if isinstance(s, URIRef)
        and s != oso
        and any(t not in TBOX_METACLASSES for t in tbox.objects(s, RDF.type))
        and not any(t in TBOX_METACLASSES for t in tbox.objects(s, RDF.type))
    ]
    if leaked:
        errors.append(f"{len(leaked)} individual(s) leaked into the TBox (e.g. {leaked[0]}).")

    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--version", required=True, help="Version directory name, e.g. 1.0.2")
    parser.add_argument("--source-dir", default="versions", help="Root versions directory (default: versions)")
    parser.add_argument("--dry-run", action="store_true", help="Validate only; do not write files")
    args = parser.parse_args(argv)

    version_dir = Path(args.source_dir) / args.version
    source_path = version_dir / "OSO.ttl"
    if not source_path.exists():
        print(f"[generate] source not found: {source_path}", file=sys.stderr)
        return 2

    expected_version_iri = f"https://w3id.org/earthsemantics/OSO/{args.version}"

    print(f"[generate] loading {source_path}")
    source = Graph().parse(str(source_path), format="turtle")
    print(f"[generate] source triples: {len(source)}")

    tbox, abox = partition_tbox_abox(source)
    print(f"[generate] TBox triples: {len(tbox)} | ABox triples: {len(abox)}")

    errors = validate(source, tbox, abox, expected_version_iri)
    if errors:
        print("[generate] validation FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print("[generate] validation OK")

    if args.dry_run:
        print("[generate] dry-run: no files written")
        return 0

    # TBox / ABox distributions.
    serialize(tbox, version_dir / "OSO-ontology.ttl", "turtle")
    serialize(abox, version_dir / "OSO-instances.ttl", "turtle")
    print(f"[generate] wrote OSO-ontology.ttl ({len(tbox)} triples)")
    print(f"[generate] wrote OSO-instances.ttl ({len(abox)} triples)")

    # Full-graph serializations.
    for fname, fmt in SERIALIZATIONS:
        serialize(source, version_dir / fname, fmt)
        print(f"[generate] wrote {fname} ({fmt})")

    print("[generate] done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
