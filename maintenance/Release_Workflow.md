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

# Phase 2 – Release Preparation

## Objective

Prepare the ontology for publication by updating its metadata, version information and embedded statistics, ensuring that all release artefacts are consistent before distribution.

## Inputs

- Validated ontology source (`OSO.ttl`)
- Release version number
- Release date
- Computed ontology statistics

## Outputs

- Release-ready ontology (`OSO.ttl`)
- Updated ontology metadata
- Updated ontology statistics

## Activities

The following activities are typically performed during this phase.

### 2.1 Update ontology metadata

Update all version-related metadata throughout the ontology, including:

- ontology version;
- `owl:versionIRI`;
- `owl:versionInfo`;
- release date;
- last modification date;
- copyright statement (if applicable);
- contributors (if applicable).

Ensure that all version identifiers remain consistent across the ontology.

### 2.2 Update embedded ontology statistics

Recompute and update the ontology statistics embedded directly in `OSO.ttl`.

The following metrics are currently maintained:

| Metric | Predicate | Computation method |
|---------|-----------|--------------------|
| Maximum class hierarchy depth | `mod:maxDepth` | Protégé Metrics |
| Number of classes | `omv:numberOfClasses` | Protégé Metrics |
| Number of properties | `omv:numberOfProperties` | Protégé Metrics |
| Number of individuals | `omv:numberOfIndividuals` | Protégé Metrics |
| Number of axioms | `omv:numberOfAxioms` | Protégé Metrics |
| Number of RDF triples | `void:triples` | RDFLib (`len(Graph)`) |
| Number of ontology entities | `void:entities` | Computed as Classes + Properties + Individuals |

These metrics are embedded directly in the ontology to improve interoperability, transparency and FAIRness, independently of ontology repository implementations.

## Validation

Before proceeding to the documentation generation phase, verify that:

- the ontology version is consistent throughout all metadata;
- version identifiers are synchronised;
- release dates are correct;
- ontology statistics have been recomputed;
- all embedded metrics correspond to the current ontology version.

## Automation potential

| Activity | Automation |
|----------|------------|
| Version number update | ✅ High |
| Metadata update | ✅ High |
| Statistics computation | ✅ High |
| Metadata consistency verification | ✅ High |
| Release validation | ✅ High |
