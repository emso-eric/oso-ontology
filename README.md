# 🌊 OSO - Observatories of Seas Ontology

## Overview

**OSO (Observatories of Seas Ontology)** provides a semantic framework to describe marine research infrastructures, with a focus on deep-sea observatories operated by EMSO-ERIC and national nodes like EMSO-France.

Version **0.15** (published on July 23, 2025) improves syntax compliance, FAIRness, and semantic alignment with existing vocabularies and data standards.

## 📂 Access

- **Ontology IRI**: [https://w3id.org/earthsemantics/OSO](https://w3id.org/earthsemantics/OSO)
- **Documentation (HTML)**: [https://emso-eric.github.io/oso-ontology/](https://emso-eric.github.io/oso-ontology/)
- **WebVOWL Visualisation of the OSO Ontology**: [https://service.tib.eu/webvowl/#iri=https://earthportal.eu/ontologies/OSO](https://service.tib.eu/webvowl/#iri=https://earthportal.eu/ontologies/OSO)

## 🧭 Objectives

- To provide a common vocabulary for describing marine observatories and their components.
- To enhance interoperability of data across European marine research infrastructures.
- To support data publication and discovery in FAIR-compliant data portals.
- To align with existing ontologies and standards (SOSA, DCAT, GeoSPARQL, PROV-O).

## ✨ Highlights of version 0.15

- Ontology IRI: `https://w3id.org/earthsemantics/OSO/0.15`
- Published on **July 23, 2025**
- Improved syntax compliance (spaces, punctuation, consistent `dcterms:` usage)
- Enriched multilingual metadata and annotation properties
- New and updated instances for sites and platforms
- FAIR score: **62%** (according to O'FAIRe) — with targeted improvements under way

## FAIRification Roadmap

This ontology is progressively being aligned with the [FAIR principles](https://www.go-fair.org/fair-principles/) using the [O'FAIRe evaluation framework](https://www.ofaire.eu/).  
The detailed improvement plan is available in the following file:

➡️ [FAIR-roadmap-OSO.md](./FAIR-roadmap-OSO.md)

We welcome feedback and contributions to improve its FAIRness over time.

## 📦 Download & Examples

You can explore these resources directly or import them into ontology editors such as [Protégé](https://protege.stanford.edu/) using their respective IRI.

- **Turtle (.ttl)**: [`https://w3id.org/earthsemantics/OSO/0.15`](https://w3id.org/earthsemantics/OSO/0.15)
- **RDF/XML (.rdf)**: [`https://earthportal.eu/ontologies/OSO.rdf`](https://earthportal.eu/ontologies/OSO.rdf)
- **OWL/XML (.owl)**: [`https://earthportal.eu/ontologies/OSO.owl`](https://earthportal.eu/ontologies/OSO.owl)
- **CSV export**: [`https://earthportal.eu/ontologies/OSO.csv`](https://earthportal.eu/ontologies/OSO.csv)
- **Version diff**: [`https://earthportal.eu/ontologies/OSO.diff`](https://earthportal.eu/ontologies/OSO.diff)


- 📊 **Download extracted tabular view (Excel)**:  
  [`OSO_RF_Site_Platform_Filtered_EMSO_20250715.xlsx`](https://github.com/emso-eric/oso-ontology/blob/main/extraction/OSO_RF_Site_Platform_Filtered_EMSO_20250715.xlsx)  
  *(Based on OSO version 0.14. An updated extraction for version 0.15 will be provided soon.)*

- 🌐 **View or explore on [EarthPortal](https://earthportal.org/ontologies/OSO)**  
  *(Supports interactive browsing of classes, properties, and individuals)*


## Structure & Key Concepts

- **Hierarchical model**:  
  `RegionalFacility → Site → SubSite → Platform → SubPlatform`

- **Key classes**:  
  `RegionalFacility`, `Site`, `SubSite`, `Platform`, `SubPlatform`, `ResearchInfrastructure`, `Organisation`, `Project`, `Cruise`, `Discipline`, `Person`, `Geometry`, `BoundingBox`

- **Ontology aligns with and reuses concepts from**:  
  - `dcterms:` (Dublin Core Terms)  
  - `foaf:` (Friend of a Friend)  
  - `schema:` (Schema.org)  
  - `geo:` and `wgs84_pos:` (Geospatial vocabularies)  
  - `sosa:` / `ssn:` (Sensors and observations)  
  - `prov:` (Provenance ontology)  
  - `cerif:` (Common European Research Information Format)

## 🤝 Contribute / Contact

For feedback, suggestions or to contribute, feel free to:

- Open a [GitHub issue](https://github.com/emso-eric/oso-ontology/issues)
- Contact the EMSO DMSG team: 📧 emso.dmsg@emso-eu.org


## 📝 License

This ontology is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).  
Please cite or attribute the EMSO ERIC team when reusing.
