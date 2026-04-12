 <img src="oso.png" alt="OSO logo" height="40"/> 

# Observatories of the Seas Ontology (OSO)

**OSO is a FAIR ontology for marine observatories, ocean observation systems, and marine research infrastructures (EMSO, Argo).**

## 🧾 Ontology Reference

* **IRI**: https://w3id.org/earthsemantics/OSO
* **Version**: 1.0.2
* **License**: https://creativecommons.org/licenses/by/4.0/
* **Publisher**: EMSO ERIC
* **Creators**: EMSO Data Management Service Group (DMSG), Ifremer
* **FAIRsharing DOI**: https://doi.org/10.25504/FAIRsharing.654931
* **DOI (Zenodo)**: https://doi.org/10.5281/zenodo.19497913

---

## 📖 Overview

OSO is designed to describe **marine observatories and ocean observation systems** in a FAIR and interoperable way.

**OSO (Observatories of the Seas Ontology)** provides a semantic framework to describe **marine observatories**, including those operated by **EMSO ERIC** as well as observatories managed by national nodes such as **EMSO-France** or developed within research projects.

Version **1.0.2** represents the **first stable release** of the ontology, consolidating previous developments and improving FAIR metadata, semantic interoperability, and alignment with reference ontologies.

Not to be confused with [OpenScienceOntology (OSO)](https://gitlab.com/opensourcelab/scientificdata/ontologies/openscienceontology/data) or [Ontology for Scenario Orchestration (OSO)](https://scite.ai/reports/ontology-for-scenario-orchestration-oso-6kyllX).

The ontology supports the **FAIR management, discovery, and reuse of marine observation data**.

---

## 🌍 Scope

OSO covers:

* Marine observatories (coastal and deep-sea)
* Ocean observation systems (fixed and mobile platforms, including floats)
* Marine research infrastructures (EMSO, Argo, national observatories)
* Scientific campaigns via CSR (Cruise Summary Reports)
* Links between infrastructures, datasets, and publications (DOIs)

This makes OSO suitable for integration in European and international marine data ecosystems.

---

## 📂 Access

* **Ontology IRI (persistent)**: [https://w3id.org/earthsemantics/OSO](https://w3id.org/earthsemantics/OSO)
* **Documentation (HTML)**: [https://emso-eric.github.io/oso-ontology/](https://emso-eric.github.io/oso-ontology/)
* **WebVOWL visualisation**: [https://service.tib.eu/webvowl/#iri=https://earthportal.eu/ontologies/OSO](https://service.tib.eu/webvowl/#iri=https://earthportal.eu/ontologies/OSO)
* **EarthPortal entry**: [https://earthportal.eu/ontologies/OSO](https://earthportal.eu/ontologies/OSO)
* **SPARQL endpoint (Virtuoso)**: [https://virtuoso.ifremer.fr/oso/sparql](https://virtuoso.ifremer.fr/oso/sparql)

---

## 🤖 Machine-readable access

The ontology is available in machine-readable formats:

* RDF (Turtle, RDF/XML, OWL/XML)
* Persistent HTTP IRI (w3id)
* EarthPortal distribution endpoints
* GitHub raw access

---

## 📦 Download

### Main distribution (recommended)

* Turtle (.ttl): https://earthportal.eu/ontologies/OSO.ttl

### Alternative formats

* RDF/XML: https://earthportal.eu/ontologies/OSO.rdf
* OWL/XML: https://earthportal.eu/ontologies/OSO.owl
* CSV export: https://earthportal.eu/ontologies/OSO.csv
* Ontology diff: https://earthportal.eu/ontologies/OSO.diff

### Development version

* GitHub (raw): https://raw.githubusercontent.com/emso-eric/oso-ontology/main/OSO.ttl

---

## 🔎 Knowledge Graph Access

OSO will soon be available through a public **SPARQL endpoint** backed by a **Virtuoso triplestore**.

This service will allow users to:

* query the ontology and its instances using SPARQL
* explore relationships between observatories, sites, platforms and projects
* integrate OSO within semantic data infrastructures

The endpoint URL will be announced in a future release.

---

## 🧭 Objectives

* Provide a semantic model for **marine observatories and ocean observation systems**

OSO aims to:

* Provide a **common vocabulary** for describing marine observatories and their components
* Enhance **interoperability across European marine research infrastructures**
* Support **data publication and discovery in FAIR-compliant data portals**
* Enable **semantic interoperability between marine data infrastructures**
* Align with widely adopted ontologies and standards

---

## ✨ Highlights of version 1.0.2

* Add conceptual diagram
* Metadata improvement for EarthPortal
* FAIR metadata and resolvability

---

## 📋 FAIRisation Roadmap

This ontology is progressively aligned with the **FAIR principles** using the
[O'FAIRe evaluation framework](https://catalogue.fair-impact.eu/resources/ofaire).

🧪 **Current FAIR score**:
https://earthportal.eu/ajax/fair_score/html/?ontologies=OSO

Feedback and contributions are welcome to further improve FAIR compliance.

---

## 🧬 Structure & Key Concepts

### Hierarchical model

```
RegionalFacility
 └─ Site
     └─ SubSite
         └─ Platform
             └─ SubPlatform
```

### Key classes

`RegionalFacility`, `Site`, `SubSite`, `Platform`, `SubPlatform`,
`ResearchInfrastructure`, `Organisation`, `Project`, `Cruise`,
`Discipline`, `Person`, `Geometry`, `BoundingBox`

### Reused vocabularies

| Vocabulary            | Purpose                  |
| --------------------- | ------------------------ |
| `dcterms:`            | Metadata                 |
| `foaf:`               | Organisations & persons  |
| `schema:`             | Web interoperability     |
| `geo:` / `wgs84_pos:` | Geospatial               |
| `sosa:` / `ssn:`      | Sensors & observations   |
| `prov:`               | Provenance               |
| `cerif:`              | Research infrastructures |

---

## 🔧 Versioning

OSO follows **Semantic Versioning (SemVer)**:

| Type  | Meaning          |
| ----- | ---------------- |
| MAJOR | breaking changes |
| MINOR | extensions       |
| PATCH | fixes            |

Example: `0.17 → 1.0.0`

---

## 🛠 Development Workflow

The ontology is developed collaboratively within the **EMSO Data Management Service Group (DMSG)**.

Workflow:

* modelling with **Protégé**
* editing with **VSCodium**
* version control via **GitHub**
* alignment with reference ontologies
* FAIR evaluation using **O'FAIRe**

---

## 🧾 Commit Convention

This repository follows **Conventional Commits**:

```
feat: add Organisation alignment with CERIF  
fix: correct domain of oso:containsSite  
docs: update ontology metadata  
refactor: reorganise platform hierarchy  
```

---

## 🔑 Keywords

marine ontology, ocean observation ontology, marine observatories, research infrastructure ontology, EMSO, Argo, FAIR data, semantic interoperability, marine data infrastructure

---

## 📖 How to cite

OSO – Observatories of the Seas Ontology
Version 1.0.2
EMSO ERIC / Ifremer
FAIRsharing DOI: https://doi.org/10.25504/FAIRsharing.654931

---

## 🤝 Contribute / Contact

Contributions are welcome:

* GitHub issues: https://github.com/emso-eric/oso-ontology/issues
* Suggestions and improvements
* Ontology extensions

📧 Contact: [emso.dmsg@emso-eu.org](mailto:emso.dmsg@emso-eu.org)

---

## 📝 License

Creative Commons Attribution 4.0 (CC-BY 4.0)
https://creativecommons.org/licenses/by/4.0/

---

## 🙏 Acknowledgements

OSO is developed collaboratively within the **EMSO Data Management Service Group (DMSG)** and benefits from contributions and feedback from the **EMSO ERIC community**.
