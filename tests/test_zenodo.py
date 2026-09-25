"""Unit tests for the pure helpers of maintenance/zenodo.py (no network)."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "maintenance"))
from zenodo import (  # noqa: E402
    ZenodoError, compare_files, declared_doi, local_digests, read_checksums, record_id_from_doi,
)


def test_record_id_from_doi():
    assert record_id_from_doi("10.5281/zenodo.22030990") == "22030990"
    assert record_id_from_doi("https://doi.org/10.5281/zenodo.19497912") == "19497912"
    with pytest.raises(ZenodoError):
        record_id_from_doi("10.25504/FAIRsharing.654931")


def test_declared_doi_of_published_release():
    assert declared_doi("1.2.0") == "10.5281/zenodo.22030990"


@pytest.fixture
def release(tmp_path):
    (tmp_path / "OSO.ttl").write_bytes(b"ontology")
    (tmp_path / "README.md").write_bytes(b"notes")
    local = local_digests(tmp_path, ["OSO.ttl", "README.md"])
    (tmp_path / "SHA256SUMS").write_text(
        "".join(f"{d['sha256']}  {n}\n" for n, d in local.items()), encoding="utf-8")
    return tmp_path, local


def test_checksums_roundtrip(release):
    path, local = release
    assert read_checksums(path / "SHA256SUMS") == {n: d["sha256"] for n, d in local.items()}


def test_compare_files_accepts_identical_upload(release):
    path, local = release
    remote = {n: d["md5"] for n, d in local.items()}
    assert compare_files(read_checksums(path / "SHA256SUMS"), local, remote) == []


def test_compare_files_detects_every_mismatch(release):
    path, local = release
    expected = read_checksums(path / "SHA256SUMS")
    remote = {"OSO.ttl": "0" * 32, "extra.png": "1" * 32}
    errors = compare_files(expected, local, remote)
    assert any("OSO.ttl: Zenodo md5" in e for e in errors)
    assert any("README.md: missing on Zenodo" in e for e in errors)
    assert any("unexpected file" in e for e in errors)
    tampered = dict(local, **{"OSO.ttl": dict(local["OSO.ttl"], sha256="f" * 64)})
    assert any("local sha256 differs" in e for e in compare_files(expected, tampered, remote))
