#!/usr/bin/env python3
"""
Run OSO Competency Question (CQ) tests.

Each CQ lives in tests/cq/ as a small manifest plus its SPARQL query and
expected result:

    tests/cq/CQ-OSO-001.yaml          (manifest)
    tests/cq/queries/CQ-OSO-001.rq    (SPARQL query)
    tests/cq/expected/CQ-OSO-001.json (expected result)

Manifest format:

    id: CQ-OSO-001
    question: "Do all core OSO entities have an English label?"
    query_file: queries/CQ-OSO-001.rq
    expected_result: expected/CQ-OSO-001.json
    owner_role: ontology_maintainer

Expected results use a simplified JSON form of SPARQL results:
- SELECT: a list of binding objects, {"var": "lexical-value"}, compared
  as a multiset (order-insensitive).
- ASK: {"boolean": true} or {"boolean": false}.

By default the queries run against the authoritative OSO.ttl; a fixture
graph can be substituted with --graph for development.

Usage
-----
    python maintenance/run_cq_tests.py
    python maintenance/run_cq_tests.py --graph tests/fixtures/mini.ttl

Requirements: rdflib (>= 6), PyYAML.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import yaml
from rdflib import Graph

REPO_ROOT = Path(__file__).resolve().parent.parent
CQ_DIR = REPO_ROOT / "tests" / "cq"


def normalize_results(result) -> dict:
    """Return a comparable form of a SPARQL result (ASK or SELECT)."""
    if result.type == "ASK":
        return {"boolean": bool(result.askAnswer)}
    rows = []
    for row in result:
        rows.append({str(v): str(row[v]) for v in result.vars if row[v] is not None})
    # order-insensitive multiset comparison
    return {"select": Counter(json.dumps(r, sort_keys=True) for r in rows)}


def normalize_expected(expected: dict) -> dict:
    if "boolean" in expected:
        return {"boolean": expected["boolean"]}
    return {"select": Counter(json.dumps(r, sort_keys=True) for r in expected.get("select", []))}


def run(graph: Graph, cq_dir: Path) -> list[str]:
    errors: list[str] = []
    manifests = sorted(cq_dir.glob("*.yaml"))
    if not manifests:
        return [f"no CQ manifests found in {cq_dir}"]

    for manifest_path in manifests:
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        cid = manifest.get("id", manifest_path.stem)
        query_path = cq_dir / manifest["query_file"]
        expected_path = cq_dir / manifest["expected_result"]

        try:
            query = query_path.read_text(encoding="utf-8")
            expected = normalize_expected(json.loads(expected_path.read_text(encoding="utf-8")))
            actual = normalize_results(graph.query(query))
        except Exception as e:  # noqa: BLE001
            errors.append(f"{cid}: error: {e}")
            continue

        if actual != expected:
            errors.append(f"{cid}: FAILED (expected {expected}, got {actual})")
        else:
            print(f"[cq] {cid}: PASS — {manifest.get('question', '')}")

    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--graph", default=str(REPO_ROOT / "OSO.ttl"), help="RDF graph to query (default: OSO.ttl)")
    parser.add_argument("--format", default=None, help="rdflib format of --graph (default: guessed from extension)")
    parser.add_argument("--cq-dir", default=str(CQ_DIR), help="CQ directory (default: tests/cq)")
    args = parser.parse_args(argv)

    graph_path = Path(args.graph)
    fmt = args.format or {".ttl": "turtle", ".nt": "nt", ".owl": "xml", ".n3": "n3",
                          ".trig": "trig", ".jsonld": "json-ld"}.get(graph_path.suffix, "turtle")
    print(f"[cq] loading {graph_path}")
    graph = Graph().parse(str(graph_path), format=fmt)
    print(f"[cq] {len(graph)} triples")

    errors = run(graph, Path(args.cq_dir))
    if errors:
        print("[cq] FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print("[cq] all competency questions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
