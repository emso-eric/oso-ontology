# OSO Release Workflow

## Purpose

This document describes the complete workflow followed to prepare, validate and publish a new release of the Observatories of the Seas Ontology (OSO).

The workflow currently combines manual and automated tasks. One of its primary objectives is to progressively migrate towards a fully reproducible Continuous Integration and Continuous Deployment (CI/CD) pipeline.

Each phase describes:

- its objective;
- the required inputs;
- the expected outputs;
- the software tools involved;
- its current level of automation.

## Workflow overview

The OSO release workflow is organised into the following phases:

1. Ontology development
2. Release preparation
3. Documentation generation
4. Distribution package generation
5. GitHub release
6. External publication

# Phase 1 – Ontology Development

## Objective

Develop, modify and maintain the Observatories of the Seas Ontology (OSO) while ensuring semantic consistency, interoperability and compliance with ontology engineering best practices.

This phase is primarily based on human expertise and therefore cannot be fully automated. It constitutes the foundation of the entire release workflow.

## Inputs

- Previous released version of OSO
- New requirements or change requests
- Ontology engineering expertise
- Reference ontologies and controlled vocabularies

## Outputs

- Updated ontology source (`OSO.ttl`)
- Updated ontology metadata
- Valid Turtle syntax

## Software tools

| Tool | Role |
|------|------|
| **VSCodium** | Primary editor for developing and maintaining the Turtle source files. |
| **Protégé** | Validation of Turtle syntax, ontology browsing, hierarchy inspection and computation of ontology metrics. |
| **Git** | Version control and change tracking. |

> **Important**
>
> The authoritative source of OSO is the Turtle serialization (`OSO.ttl`).
> Ontology development is performed directly on this source file using VSCodium.
> Protégé is primarily used for validation, inspection and ontology analysis rather than as the main editing environment.

## Activities

The following activities are typically performed during this phase:

- add, modify or remove ontology classes;
- create or update object, data and annotation properties;
- create or update named individuals;
- improve multilingual labels, definitions and comments;
- align OSO with external ontologies and controlled vocabularies;
- maintain persistent URIs and ontology consistency;
- update ontology metadata when required.

## Validation

Before proceeding to the release preparation phase, the ontology should be reviewed to ensure that:

- the Turtle syntax is valid;
- no parsing errors are reported by Protégé;
- ontology entities are consistently modelled;
- labels, definitions and comments are complete;
- ontology metadata are consistent;
- external ontology references remain valid.

## Automation potential

| Activity | Automation |
|----------|------------|
| Ontology modelling | ❌ Manual |
| Turtle syntax validation | ✅ Possible |
| Ontology metadata verification | ✅ Possible |
| URI verification | ✅ Possible |
| External link checking | ✅ Possible |
