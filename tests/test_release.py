"""Unit tests for the release gate in maintenance/check_release.py."""
import sys
from pathlib import Path

from rdflib import Graph

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "maintenance"))
from check_release import check_versioning, previous_release  # noqa: E402
from validate_ontology import check_ontology_header  # noqa: E402

TAGS = ["v1.0.0", "1.0.2", "v1.1.0", "v1.2.0", "not-a-version"]


def header(version="1.2.1", info=None, prior="1.2.0", extra=""):
    info = info or f"{version} – test release"
    return Graph().parse(data=f"""
        @prefix owl: <http://www.w3.org/2002/07/owl#> .
        @prefix dcterms: <http://purl.org/dc/terms/> .
        <https://w3id.org/earthsemantics/OSO> a owl:Ontology ;
            owl:versionIRI <https://w3id.org/earthsemantics/OSO/{version}/> ;
            owl:versionInfo "{info}"@en ;
            owl:priorVersion <https://w3id.org/earthsemantics/OSO/{prior}/> ;
            dcterms:modified "2026-09-25" {extra} .
    """, format="turtle")


def test_previous_release_handles_mixed_tag_styles():
    assert previous_release("1.2.1", TAGS) == "1.2.0"
    assert previous_release("1.1.0", TAGS) == "1.0.2"
    assert previous_release("1.0.0", TAGS) is None


def test_valid_patch_release():
    assert check_versioning(header(), "1.2.1", TAGS) == []


def test_rejects_existing_or_older_version():
    errors = check_versioning(header(version="1.1.5", prior="1.1.0"), "1.1.5", TAGS)
    assert any("older than existing" in e for e in errors)
    errors = check_versioning(header(version="1.2.0", prior="1.1.0"), "1.2.0", TAGS)
    assert any("already tagged" in e for e in errors)


def test_rejects_inconsistent_version_metadata():
    assert any("versionIRI" in e for e in check_versioning(header(version="1.2.2"), "1.2.1", TAGS))
    assert any("versionInfo" in e for e in check_versioning(header(info="1.2.0 – stale"), "1.2.1", TAGS))
    assert any("priorVersion" in e for e in check_versioning(header(prior="1.1.0"), "1.2.1", TAGS))


def test_self_reference_is_rejected():
    g = header(extra='; <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <https://w3id.org/earthsemantics/OSO>')
    assert any("self-referencing" in e for e in check_ontology_header(g, "OSO.ttl", expect_version=True))
    assert check_ontology_header(header(), "OSO.ttl", expect_version=True) == []
