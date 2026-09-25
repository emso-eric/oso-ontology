"""Unit tests for the TBox/ABox partition in maintenance/generate_distributions.py."""
import sys
from pathlib import Path

import pytest
from rdflib import Graph
from rdflib.compare import isomorphic

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "maintenance"))
from generate_distributions import main, partition_tbox_abox  # noqa: E402

PREFIXES = """
@prefix OSO: <https://w3id.org/earthsemantics/OSO#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
"""

# Header and an individual both reference bnodes typed with the same class:
# the class IRI must not glue their bnode structures together.
SHARED_CLASS = PREFIXES + """
<https://w3id.org/earthsemantics/OSO> a owl:Ontology ;
    owl:versionIRI <https://w3id.org/earthsemantics/OSO/9.9.9/> ;
    owl:versionInfo "9.9.9" ;
    adms:identifier [ a adms:Identifier ; skos:notation "ONT-ID" ] .
OSO:Site a owl:Class ;
    rdfs:subClassOf [ a owl:Restriction ; owl:onProperty OSO:p ; owl:someValuesFrom OSO:Platform ] .
OSO:DYFAMED a owl:NamedIndividual, OSO:Site ;
    adms:identifier [ a adms:Identifier ; skos:notation "10.17882/43749" ] .
"""


def roundtrip(graph: Graph) -> Graph:
    """Serialise and re-parse, as happens when TBox/ABox are written to files."""
    return Graph().parse(data=graph.serialize(format="turtle"), format="turtle")


@pytest.fixture
def partition():
    g = Graph().parse(data=SHARED_CLASS, format="turtle")
    tbox, abox = partition_tbox_abox(g)
    return g, tbox, abox


def test_individual_stays_in_abox(partition):
    _, tbox, abox = partition
    dyfamed = "https://w3id.org/earthsemantics/OSO#DYFAMED"
    assert not any(str(s) == dyfamed for s in tbox.subjects())
    assert any(str(s) == dyfamed for s in abox.subjects())


def test_bnodes_follow_their_owner(partition):
    _, tbox, abox = partition
    notations = lambda g: {str(o) for o in g.objects(None, None) if str(o) in {"ONT-ID", "10.17882/43749"}}
    assert notations(tbox) == {"ONT-ID"}
    assert notations(abox) == {"10.17882/43749"}


def test_partition_is_exact_and_roundtrips(partition):
    g, tbox, abox = partition
    assert not set(tbox) & set(abox)
    assert isomorphic(roundtrip(tbox) + roundtrip(abox), g)


def test_real_source_partition_roundtrips():
    source = Path(__file__).resolve().parent.parent / "OSO.ttl"
    g = Graph().parse(str(source), format="turtle")
    tbox, abox = partition_tbox_abox(g)
    assert isomorphic(roundtrip(tbox) + roundtrip(abox), g)


def test_version_iri_trailing_slash(tmp_path):
    version_dir = tmp_path / "9.9.9"
    version_dir.mkdir()
    (version_dir / "OSO.ttl").write_text(SHARED_CLASS, encoding="utf-8")
    assert main(["--version", "9.9.9", "--source-dir", str(tmp_path), "--dry-run"]) == 0
