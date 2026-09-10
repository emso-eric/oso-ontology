#!/usr/bin/env python3
"""
Generate OSO metadata artifacts (DCAT, VoID, SHACL) for a given version from
its already-generated distribution files.

Inputs (produced by maintenance/generate_distributions.py):
    versions/<version>/OSO-ontology.ttl   (TBox)
    versions/<version>/OSO-instances.ttl  (ABox)

Outputs:
    versions/<version>/OSO-dcat.ttl   (DCAT catalog + distributions)
    versions/<version>/OSO-voId.ttl   (VoID description of the ABox dataset)
    versions/<version>/OSO-shacl.ttl  (SHACL profile auto-derived from the TBox)

The SHACL profile is structural: one sh:NodeShape per named class, with
sh:property constraints derived from rdfs:domain / rdfs:range assertions
(sh:class for object properties, sh:datatype for datatype properties). It is
not a hand-curated semantic profile; it captures the cardinality-free structural
constraints expressible in the TBox.

Usage
-----
    python maintenance/generate_metadata.py --version 1.0.2 \\
        --doi 10.5281/zenodo.19497913 \\
        --fairsharing-doi 10.25504/FAIRsharing.654931 \\
        --issued 2026-04-12 --modified 2026-04-12 \\
        --previous-version 1.0.1

Requirements: rdflib (>= 6).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rdflib import Graph, RDF, RDFS, URIRef, BNode, Literal, Namespace
from rdflib.namespace import OWL, XSD, DCTERMS, FOAF

VOID = Namespace("http://rdfs.org/ns/void#")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
PAV = Namespace("http://purl.org/pav/")
PROV = Namespace("http://www.w3.org/ns/prov#")
SH = Namespace("http://www.w3.org/ns/shacl#")

OSO = URIRef("https://w3id.org/earthsemantics/OSO")
OSO_NS = "https://w3id.org/earthsemantics/OSO#"
CREATOR = URIRef("https://orcid.org/0000-0001-8502-9812")
PUBLISHER = URIRef("https://ror.org/044jxhp58")
LICENSE = URIRef("https://creativecommons.org/licenses/by/4.0/")
SPARQL = URIRef("https://virtuoso.ifremer.fr/oso/sparql")
SPARQL_UI = URIRef("https://virtuoso.ifremer.fr/oso/")
HOMEPAGE = URIRef("https://github.com/emso-eric/oso-ontology")
LANDING = URIRef("https://earthportal.eu/ontologies/OSO")

LANGS = ["en", "fr", "es", "it", "pt", "no", "ro", "el"]
ISO_LANG = {l: URIRef(f"http://id.loc.gov/vocabulary/iso639-1/{l}") for l in LANGS}

IANA = "https://www.iana.org/assignments/media-types/"


def version_iri(version: str, trailing_slash: bool = False) -> str:
    base = f"https://w3id.org/earthsemantics/OSO/{version}"
    return base + "/" if trailing_slash else base


def bind_common(g: Graph) -> None:
    g.bind("dcat", DCAT)
    g.bind("dcterms", DCTERMS)
    g.bind("foaf", FOAF)
    g.bind("owl", OWL)
    g.bind("pav", PAV)
    g.bind("void", VOID)
    g.bind("prov", PROV)
    g.bind("sh", SH)
    g.bind("xsd", XSD)
    g.bind("rdfs", RDFS)
    g.bind("OSO", URIRef(OSO_NS))
    g.bind("schema", URIRef("http://schema.org/"))
    g.bind("vcard", URIRef("http://www.w3.org/2006/vcard/ns#"))


def build_dcat(version, doi, fairsharing_doi, issued, modified, previous_version) -> Graph:
    g = Graph()
    bind_common(g)
    vi = URIRef(version_iri(version))
    prev = URIRef(version_iri(previous_version))
    doi_uri = URIRef(f"https://doi.org/{doi}") if doi else None

    # --- Ontology (TBox) dataset ---
    g.add((OSO, RDF.type, OWL.Ontology))
    g.add((OSO, RDF.type, DCAT.Dataset))
    g.add((OSO, DCTERMS.title, Literal("Observatories of the Seas Ontology", lang="en")))
    g.add((OSO, DCTERMS.alternative, Literal("OSO", lang="en")))
    g.add((OSO, DCTERMS.description, Literal(
        "OSO is an ontology designed to describe marine observatories, research infrastructures, "
        "observation platforms, associated organisations, scientific activities and related metadata "
        "in a FAIR and interoperable way.", lang="en")))
    g.add((OSO, DCTERMS.creator, CREATOR))
    g.add((OSO, PAV.curatedBy, CREATOR))
    g.add((OSO, DCTERMS.publisher, PUBLISHER))
    g.add((OSO, DCTERMS.license, LICENSE))
    g.add((OSO, DCTERMS.created, Literal("2025-03-01", datatype=XSD.date)))
    g.add((OSO, DCTERMS.modified, Literal(modified, datatype=XSD.date)))
    for l in LANGS:
        g.add((OSO, DCTERMS.language, ISO_LANG[l]))
    for kw in ["marine observatories", "research infrastructures", "semantic web",
               "ontology", "FAIR", "ocean observing systems"]:
        g.add((OSO, DCAT.keyword, Literal(kw, lang="en")))
    g.add((OSO, FOAF.homepage, HOMEPAGE))
    g.add((OSO, DCAT.landingPage, LANDING))
    g.add((OSO, DCTERMS.hasVersion, vi))
    g.add((OSO, PAV.previousVersion, prev))
    g.add((OSO, OWL.versionInfo, Literal(version, lang="en")))
    g.add((OSO, DCAT.version, Literal(version)))
    if doi_uri:
        g.add((OSO, DCTERMS.identifier, doi_uri))
    ont_dist = URIRef(f"https://w3id.org/earthsemantics/OSO/{version}/ontology")
    shacl_dist = URIRef(f"https://w3id.org/earthsemantics/OSO/{version}/shacl")
    g.add((OSO, DCAT.distribution, ont_dist))
    g.add((OSO, DCAT.distribution, shacl_dist))

    # --- Knowledge Graph (ABox) dataset ---
    ds = URIRef("https://w3id.org/earthsemantics/OSO/dataset")
    g.add((ds, RDF.type, DCAT.Dataset))
    g.add((ds, RDF.type, VOID.Dataset))
    g.add((ds, DCTERMS.title, Literal("OSO Knowledge Graph", lang="en")))
    g.add((ds, DCTERMS.description, Literal(
        "Instance data described using the Observatories of the Seas Ontology (OSO), including "
        "marine observatories, Regional Facilities, Sites, Platforms, organisations and related "
        "entities.", lang="en")))
    g.add((ds, DCTERMS.creator, CREATOR))
    g.add((ds, DCTERMS.publisher, PUBLISHER))
    g.add((ds, DCTERMS.license, LICENSE))
    g.add((ds, DCTERMS.modified, Literal(modified, datatype=XSD.date)))
    g.add((ds, DCTERMS.conformsTo, OSO))
    g.add((ds, DCAT.version, Literal(version)))
    inst_dist = URIRef(f"https://w3id.org/earthsemantics/OSO/{version}/instances")
    g.add((ds, DCAT.distribution, inst_dist))
    g.add((ds, DCAT.accessService, SPARQL))

    # --- Complete bundle ---
    comp = URIRef(f"https://w3id.org/earthsemantics/OSO/{version}/complete")
    g.add((comp, RDF.type, DCAT.Dataset))
    g.add((comp, DCTERMS.title, Literal("OSO complete distribution", lang="en")))
    g.add((comp, DCTERMS.description, Literal(
        "Combined distribution of OSO containing both the ontology model and the instance data.",
        lang="en")))
    g.add((comp, DCTERMS.creator, CREATOR))
    g.add((comp, DCTERMS.publisher, PUBLISHER))
    g.add((comp, DCTERMS.license, LICENSE))
    g.add((comp, DCTERMS.modified, Literal(modified, datatype=XSD.date)))
    g.add((comp, DCTERMS.conformsTo, OSO))
    g.add((comp, DCTERMS.hasPart, OSO))
    g.add((comp, DCTERMS.hasPart, ds))
    g.add((comp, DCAT.version, Literal(version)))
    for ext in ["ttl", "owl", "jsonld", "nt", "n3", "trig"]:
        g.add((comp, DCAT.distribution, URIRef(f"https://w3id.org/earthsemantics/OSO/{version}.{ext}")))

    # --- Distributions ---
    def add_dist(uri, title, fmt, media):
        g.add((uri, RDF.type, DCAT.Distribution))
        g.add((uri, DCTERMS.title, Literal(title, lang="en")))
        g.add((uri, DCTERMS.format, Literal(fmt)))
        g.add((uri, DCAT.mediaType, URIRef(IANA + media)))
        g.add((uri, DCAT.downloadURL, uri))

    add_dist(ont_dist, "OSO ontology – Turtle distribution", "text/turtle", "text/turtle")
    g.add((ont_dist, DCTERMS.description, Literal(
        "Ontology-only distribution of OSO containing the ontology model, axioms and ontology "
        "metadata, without domain instance data.", lang="en")))
    add_dist(inst_dist, "OSO instance data – Turtle distribution", "text/turtle", "text/turtle")
    g.add((inst_dist, DCTERMS.description, Literal(
        "Instance-data distribution of the OSO Knowledge Graph, without the ontology schema.",
        lang="en")))
    add_dist(shacl_dist, "OSO SHACL validation shapes", "text/turtle", "text/turtle")
    g.add((shacl_dist, DCTERMS.description, Literal(
        "SHACL shapes used to validate OSO instance data against structural constraints.",
        lang="en")))

    serials = [
        ("ttl", "OSO complete – Turtle distribution", "text/turtle", "text/turtle"),
        ("owl", "OSO complete – RDF/XML distribution", "application/rdf+xml", "application/rdf+xml"),
        ("jsonld", "OSO complete – JSON-LD distribution", "application/ld+json", "application/ld+json"),
        ("nt", "OSO complete – N-Triples distribution", "application/n-triples", "application/n-triples"),
        ("n3", "OSO complete – N3 distribution", "text/n3", "text/n3"),
        ("trig", "OSO complete – TriG distribution", "application/trig", "application/trig"),
    ]
    for ext, title, fmt, media in serials:
        add_dist(URIRef(f"https://w3id.org/earthsemantics/OSO/{version}.{ext}"), title, fmt, media)

    # --- SPARQL service ---
    g.add((SPARQL, RDF.type, DCAT.DataService))
    g.add((SPARQL, DCTERMS.title, Literal("OSO SPARQL endpoint", lang="en")))
    g.add((SPARQL, DCTERMS.description, Literal(
        "SPARQL endpoint providing query access to the OSO ontology and instance data.", lang="en")))
    g.add((SPARQL, DCAT.endpointURL, SPARQL))
    g.add((SPARQL, DCAT.landingPage, SPARQL_UI))
    g.add((SPARQL, DCAT.servesDataset, comp))

    return g


def build_void(version, doi, issued, modified, previous_version, abox: Graph) -> Graph:
    g = Graph()
    bind_common(g)
    g.bind("vcard", URIRef("http://www.w3.org/2006/vcard/ns#"))
    g.bind("schema", URIRef("http://schema.org/"))
    vi = URIRef(version_iri(version))
    prev = URIRef(version_iri(previous_version))
    doi_uri = URIRef(f"https://doi.org/{doi}") if doi else None

    ds = URIRef("https://w3id.org/earthsemantics/OSO/dataset")
    g.add((ds, RDF.type, DCAT.Dataset))
    g.add((ds, RDF.type, VOID.Dataset))
    g.add((ds, DCTERMS.title, Literal("OSO Knowledge Graph", lang="en")))
    g.add((ds, DCTERMS.title, Literal("Graphe de connaissances OSO", lang="fr")))
    g.add((ds, DCTERMS.description, Literal(
        "Instance data described using the Observatories of the Seas Ontology (OSO), including "
        "marine observatories, Regional Facilities, Sites, Platforms, organisations and related "
        "entities.", lang="en")))
    g.add((ds, DCTERMS.creator, URIRef("https://ror.org/044jxhp58")))
    g.add((ds, DCTERMS.creator, URIRef("https://ror.org/04xkqms46")))
    g.add((ds, FOAF.maker, URIRef("https://ror.org/044jxhp58")))
    g.add((ds, FOAF.maker, URIRef("https://ror.org/04xkqms46")))
    g.add((ds, DCTERMS.publisher, URIRef("https://ror.org/04xkqms46")))
    g.add((ds, DCTERMS.issued, Literal(issued, datatype=XSD.date)))
    g.add((ds, DCTERMS.modified, Literal(modified, datatype=XSD.date)))
    g.add((ds, DCTERMS.license, LICENSE))
    if doi_uri:
        g.add((ds, DCTERMS.identifier, doi_uri))
    g.add((ds, DCTERMS.conformsTo, OSO))
    for l in ["en", "fr", "es", "it", "pt", "ro", "el", "no"]:
        g.add((ds, DCTERMS.language, Literal(l, datatype=XSD.language)))
    g.add((ds, OWL.versionInfo, Literal(version)))
    g.add((ds, DCTERMS.hasVersion, vi))
    g.add((ds, PAV.version, Literal(version)))
    g.add((ds, PAV.previousVersion, prev))
    g.add((ds, PROV.wasDerivedFrom, prev))
    g.add((ds, PROV.generatedAtTime, Literal(modified, datatype=XSD.date)))
    g.add((ds, PROV.wasAttributedTo, URIRef("https://ror.org/04xkqms46")))
    g.add((ds, FOAF.page, OSO))
    g.add((ds, FOAF.homepage, HOMEPAGE))

    inst_dist = URIRef(f"https://w3id.org/earthsemantics/OSO/{version}/instances")
    g.add((ds, DCAT.distribution, inst_dist))
    g.add((ds, DCAT.accessURL, SPARQL))
    g.add((ds, VOID.dataDump, inst_dist))
    g.add((ds, VOID.sparqlEndpoint, SPARQL))

    # example resource: first URIRef individual in the ABox
    examples = sorted(s for s in abox.subjects() if isinstance(s, URIRef) and str(s).startswith(OSO_NS))
    if examples:
        g.add((ds, VOID.exampleResource, examples[0]))

    # statistics from the ABox
    triples = len(abox)
    classes = len(set(abox.objects(predicate=RDF.type)))
    properties = len(set(abox.predicates()))
    entities = len(set(s for s in abox.subjects() if isinstance(s, URIRef)))
    g.add((ds, VOID.triples, Literal(triples, datatype=XSD.integer)))
    g.add((ds, VOID.classes, Literal(classes, datatype=XSD.integer)))
    g.add((ds, VOID.properties, Literal(properties, datatype=XSD.integer)))
    g.add((ds, VOID.entities, Literal(entities, datatype=XSD.integer)))
    g.add((ds, VOID.uriSpace, Literal(OSO_NS)))

    for v in [OSO, URIRef("http://www.w3.org/2002/07/owl#"), URIRef("http://www.w3.org/2000/01/rdf-schema#"),
              URIRef("http://www.w3.org/2004/02/skos/core#"), URIRef("http://purl.org/dc/terms/"),
              URIRef("http://www.w3.org/ns/dcat#"), URIRef("http://xmlns.com/foaf/0.1/")]:
        g.add((ds, VOID.vocabulary, v))

    for theme in ["EARTH", "ENV", "CLIMATE"]:
        g.add((ds, DCAT.theme, URIRef(f"https://data.earthportal.eu/categories/{theme}")))

    cp = BNode()
    g.add((ds, DCAT.contactPoint, cp))
    g.add((cp, RDF.type, URIRef("http://www.w3.org/2006/vcard/ns#Kind")))
    g.add((cp, URIRef("http://www.w3.org/2006/vcard/ns#fn"), Literal("EMSO Data Management Service Group")))
    g.add((cp, URIRef("http://www.w3.org/2006/vcard/ns#hasEmail"), URIRef("mailto:emso.dmsg@emso-eu.org")))
    g.add((cp, URIRef("http://www.w3.org/2006/vcard/ns#hasOrganizationName"), Literal("EMSO ERIC")))
    g.add((ds, FOAF.primaryTopic, OSO))
    return g


def build_shacl(version, issued, tbox: Graph) -> Graph:
    g = Graph()
    bind_common(g)
    g.bind("sh", SH)
    vi = URIRef(version_iri(version))

    shacl_iri = URIRef("https://w3id.org/earthsemantics/OSO/shacl")
    g.add((shacl_iri, RDF.type, OWL.Ontology))
    g.add((shacl_iri, DCTERMS.title, Literal("OSO SHACL validation profile", lang="en")))
    g.add((shacl_iri, DCTERMS.description, Literal(
        "Structural SHACL validation profile auto-derived from the OSO TBox (rdfs:domain / "
        "rdfs:range assertions). One sh:NodeShape per named class, with sh:property constraints "
        "expressing sh:class (object properties) and sh:datatype (datatype properties).", lang="en")))
    g.add((shacl_iri, DCTERMS.creator, CREATOR))
    g.add((shacl_iri, DCTERMS.license, LICENSE))
    g.add((shacl_iri, DCTERMS.conformsTo, URIRef("http://www.w3.org/ns/shacl#")))
    g.add((shacl_iri, DCTERMS.relation, vi))
    g.add((shacl_iri, DCTERMS.source, vi))
    g.add((shacl_iri, DCTERMS.issued, Literal(issued, datatype=XSD.date)))
    g.add((shacl_iri, RDFS.seeAlso, OSO))
    g.add((shacl_iri, RDFS.seeAlso, HOMEPAGE))
    g.add((shacl_iri, OWL.versionIRI, URIRef(f"https://w3id.org/earthsemantics/OSO/shacl/{version}")))
    g.add((shacl_iri, OWL.versionInfo, Literal(version)))

    # index properties by domain
    props_by_domain = {}
    for p in set(tbox.subjects(RDF.type, OWL.ObjectProperty)) | set(tbox.subjects(RDF.type, OWL.DatatypeProperty)) | set(tbox.subjects(RDF.type, OWL.AnnotationProperty)):
        for dom in tbox.objects(p, RDFS.domain):
            props_by_domain.setdefault(dom, []).append(p)

    classes = sorted(
        (c for c in tbox.subjects(RDF.type, OWL.Class) if isinstance(c, URIRef) and str(c).startswith(OSO_NS)),
        key=lambda c: str(c),
    )
    for c in classes:
        local = str(c).replace(OSO_NS, "")
        shape = URIRef(f"{OSO_NS}{local}Shape")
        g.add((shape, RDF.type, SH.NodeShape))
        g.add((shape, SH.targetClass, c))
        for p in sorted(props_by_domain.get(c, []), key=lambda x: str(x)):
            ps = BNode()
            g.add((shape, SH.property, ps))
            g.add((ps, SH.path, p))
            ranges = list(tbox.objects(p, RDFS.range))
            is_obj = (p, RDF.type, OWL.ObjectProperty) in tbox
            if is_obj:
                g.add((ps, SH.nodeKind, SH.IRI))
                for r in ranges:
                    if isinstance(r, URIRef):
                        g.add((ps, SH.clazz, r))  # sh:class
                        break
            else:
                for r in ranges:
                    if isinstance(r, URIRef):
                        g.add((ps, SH.datatype, r))
                        break
            g.add((ps, SH.severity, SH.Violation))
    return g


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--version", required=True)
    ap.add_argument("--source-dir", default="versions")
    ap.add_argument("--doi", default=None, help="Zenodo DOI (without the https://doi.org/ prefix)")
    ap.add_argument("--fairsharing-doi", default=None)
    ap.add_argument("--issued", required=True, help="Issue date YYYY-MM-DD")
    ap.add_argument("--modified", required=True, help="Modification date YYYY-MM-DD")
    ap.add_argument("--previous-version", required=True, help="Previous version number, e.g. 1.0.1")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    vdir = Path(args.source_dir) / args.version
    tbox_path = vdir / "OSO-ontology.ttl"
    abox_path = vdir / "OSO-instances.ttl"
    if not tbox_path.exists() or not abox_path.exists():
        print(f"[meta] missing TBox/ABox in {vdir} (run generate_distributions.py first)", file=sys.stderr)
        return 2

    tbox = Graph().parse(str(tbox_path), format="turtle")
    abox = Graph().parse(str(abox_path), format="turtle")
    print(f"[meta] TBox={len(tbox)} triples, ABox={len(abox)} triples")

    dcat = build_dcat(args.version, args.doi, args.fairsharing_doi, args.issued, args.modified, args.previous_version)
    void = build_void(args.version, args.doi, args.issued, args.modified, args.previous_version, abox)
    shacl = build_shacl(args.version, args.issued, tbox)
    print(f"[meta] DCAT={len(dcat)} triples, VoID={len(void)} triples, SHACL={len(shacl)} triples")

    if args.dry_run:
        print("[meta] dry-run: no files written")
        return 0

    dcat.serialize(destination=str(vdir / "OSO-dcat.ttl"), format="turtle")
    void.serialize(destination=str(vdir / "OSO-voId.ttl"), format="turtle")
    shacl.serialize(destination=str(vdir / "OSO-shacl.ttl"), format="turtle")
    print(f"[meta] wrote OSO-dcat.ttl, OSO-voId.ttl, OSO-shacl.ttl in {vdir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
