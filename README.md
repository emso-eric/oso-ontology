# 🌊 OSO - Observatories of Seas Ontology

## 📌 Overview

**OSO** (Observatories of Seas Ontology) provides a semantic framework for describing **subsea and deep-sea observatories**, with a particular focus on those operated within the **EMSO-ERIC** (European Multidisciplinary Seafloor and water column Observatory) which is an European Research Infrastructure Consortium.

The ontology structures observatories across **three main hierarchical levels**:

1. **Regional Facilities** – large-scale marine areas under long-term observation,
2. **Sites** – specific geographic locations within a Regional Facility where observations take place,
3. **Platforms** – physical structures (e.g., cabled observatories, moorings, landers) deployed at a site to carry scientific instruments.

Two additional levels are planned for future development:
- **Measured Parameters** – describing the observed phenomena (e.g., temperature, pressure, biogeochemical indicators),
- **Datasets and PIDs** – linking observations and parameters to their corresponding published datasets (with persistent identifiers such as DOI).

Developed in the context of the **EMSO-ERIC**, OSO supports the **FAIR principles** (Findable, Accessible, Interoperable, Reusable) by enabling semantic integration of marine observation data. It also facilitates:

- Links to **organisations** responsible for the facilities,
- Association with relevant **geographical areas**,
- Connection to **scientific projects** and **oceanographic cruises**.

OSO is aligned with existing standards and aims to contribute to the broader adoption of semantic technologies in marine science.

## 🧭 Objectives

- To provide a common vocabulary for describing marine observatories and their components.
- To enhance interoperability of data across European marine research infrastructures.
- To support data publication and discovery in FAIR-compliant data portals.
- To align with existing ontologies and standards (SOSA, DCAT, GeoSPARQL, PROV-O).

## 🧱 Ontology Structure

The OSO ontology currently defines the following key classes, organised to describe subsea observatories and their context within the EMSO-ERIC infrastructure:

| Class Name              | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `RegionalFacility`      | A large-scale marine area representing the highest level of observatory organisation in EMSO (e.g., Ligurian Sea, Azores). |
| `Site`                  | A defined observation site located within a Regional Facility, where monitoring activities take place. |
| `Platform`              | A physical infrastructure (e.g., mooring, cabled observatory) deployed at a site to support sensors and instruments. |
| `ERIC`                  | A European infrastructure infrastructure consortium linked to the observatories such as EMSO or EMBRC.|
| `ResearchInfrastructure`| A national-level infrastructure coordinating marine observation activities such as EMSO-France, NorEMSO or EMSO Portugal. |
| `Organisation`          | A legal entity (e.g., research institute, university, operator) involved in the operation, funding, or coordination of the observatories. |
| `Person`                | An individual participating in the infrastructure (regional team leader, site responsible, Principal Investigator). |
| `Project`               | A scientific or infrastructure project contributing to the observatory's activities or data. |
| `Cruise` / `SeriesOfCruises` | An oceanographic mission (or set of missions) carried out to deploy platforms or collect data. |
| `Location`              | A geographic concept used to model the spatial extent or coordinates of observatory elements (point or bounding box). |
| `Discipline`            | A scientific domain related to the data collected (e.g., physical oceanography, biogeochemistry, geophysics). |

## DCAT Metadata

This ontology is described using the [DCAT standard](https://www.w3.org/TR/vocab-dcat-3/) to ensure better interoperability and indexing.

- 📄 [View the DCAT metadata on EarthPortal](https://w3id.org/earthsemantics/OSO_DCAT)

## 🔗 OSO Visualisation

You can interactively visualise the OSO ontology using WebVOWL by following this link:

[WebVOWL Visualisation of the OSO Ontology](https://service.tib.eu/webvowl/#iri=https://earthportal.eu/ontologies/OSO)


## 🔗 Ontology Alignments

OSO is designed to promote interoperability and semantic consistency with existing standards. It currently aligns with the following well-established vocabularies and ontologies:

| Ontology / Vocabulary | Prefix        | Purpose in OSO                                                                 |
|------------------------|---------------|--------------------------------------------------------------------------------|
| **GeoSPARQL**          | `geo`         | To represent geospatial information such as points, bounding boxes, and geometries. |
| **FOAF (Friend of a Friend)** | `foaf` | To describe people (`foaf:Person`) and organisations (`foaf:Organization`) involved in the observatories. |
| **Dublin Core Terms**  | `dcterms`     | To provide metadata properties such as titles, identifiers, contributors, or temporal coverage. |
| **W3C standard vocabularies** | `rdf`, `rdfs`, `xsd`, `owl` | To structure the ontology using RDF/OWL principles, classes, datatypes, and relations. |

These alignments allow OSO to integrate with broader data ecosystems and enable semantic linking with external knowledge bases and datasets.

Further alignments with marine science ontologies (e.g., SOSA/SSN, ENVO, PROV-O) are planned in future versions.

## 📂 Access

- **Ontology IRI**: [https://w3id.org/earthsemantics/OSO](https://w3id.org/earthsemantics/OSO)
- **Documentation (HTML)**: [https://emso-eric.github.io/oso-ontology/](https://emso-eric.github.io/oso-ontology/)
