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
| `check_release.py` | Release gate for `versions/<version>/`: required files, identity, partition, serialisations, version chain (`versionIRI`, `versionInfo`, `priorVersion`), DCAT/CITATION consistency, no self-referencing annotation. `--checksums` writes `SHA256SUMS`. |
| `verify_published.py` | Checks the artefacts actually served by GitHub Pages. |

Install dependencies with `pip install -r maintenance/requirements.txt`.
Unit tests for the tooling run with `python -m pytest tests/`.

## Continuous integration

GitHub Actions workflows enforce the pipeline:

- `.github/workflows/validate.yml` — on every push/PR to `main`: parses all
  RDF artefacts, verifies the ontology identity and artefact consistency,
  checks that `docs/ontology.*` mirror `OSO.ttl`, and runs the CQ tests.
  Non-blocking SHACL and ROBOT reports are produced as artefacts.
- `.github/workflows/publish-docs.yml` — on release or manual dispatch:
  regenerates `docs/ontology.*` and commits them if they drifted.
- `.github/workflows/release.yml` — on a `vX.Y.Z` tag: runs every gate
  above plus `check_release.py`, then creates a **draft** release whose
  assets are the files committed under `versions/X.Y.Z/` (never regenerated)
  and their `SHA256SUMS`, and verifies the uploaded assets. A maintainer
  reviews and publishes the draft. Manual dispatch runs the gates only.
- `.github/workflows/verify-published.yml` — after each Pages build: checks
  that the live `ontology.*` artefacts carry the OSO identity.

Releases are immutable: a published version is never modified. Any fix,
even to metadata or labels, ships as a new patch version.

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
