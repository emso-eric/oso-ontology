# OSO Maintenance Guide

This directory contains the documentation required to maintain, release and publish the Observatories of the Seas Ontology (OSO).

The objective is to ensure that every release follows a reproducible process while progressively automating the workflow through Continuous Integration and Continuous Deployment (CI/CD).

## Contents

- Ontology development
- Release workflow
- Documentation generation
- Distribution package generation
- Publication process
- CI/CD roadmap
- Release checklist

## Scripts

| Script | Purpose |
|---|---|
| `generate_distributions.py` | Derives TBox/ABox and RDF serialisations for a `versions/<version>/` directory from its `OSO.ttl` source. |
| `generate_metadata.py` | Generates DCAT, VoID and SHACL metadata files for a version. |
| `generate_docs.py` | Regenerates `docs/ontology.{ttl,nt,owl,jsonld}` (GitHub Pages) from the root `OSO.ttl`. `--check` verifies without writing. |
| `validate_ontology.py` | Blocking quality gate: RDF syntax, single `owl:Ontology` identity, partition and serialisation consistency. |
| `run_cq_tests.py` | Runs the competency question tests under `tests/cq/`. |

Install dependencies with `pip install -r maintenance/requirements.txt`.

## Continuous integration

Two GitHub Actions workflows enforce the pipeline:

- `.github/workflows/validate.yml` — on every push/PR to `main`: parses all
  RDF artefacts, verifies the ontology identity and artefact consistency,
  checks that `docs/ontology.*` mirror `OSO.ttl`, and runs the CQ tests.
  Non-blocking SHACL and ROBOT reports are produced as artefacts.
- `.github/workflows/publish-docs.yml` — on release or manual dispatch:
  regenerates `docs/ontology.*` and commits them if they drifted.

## Intended audience

- OSO maintainers
- Contributors
- Future developers
- DevOps engineers

## Objectives

- Document the complete release workflow.
- Ensure reproducibility.
- Facilitate knowledge transfer.
- Progressively replace manual release tasks by an automated CI/CD pipeline while preserving reproducibility and traceability.

## Documentation

- [OSO Release Workflow](Release_Workflow.md)
