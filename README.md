<h1 align="center">
Observatories of the Seas Ontology (OSO)
</h1>

<p align="center">
<b>A FAIR, multilingual and interoperable ontology for marine observatories, ocean observing systems and marine research infrastructures.</b>
</p>

<p align="center">
  <img src="docs/share/oso-social-qrcode.png"
       alt="Observatories of the Seas Ontology (OSO)"
       width="100%">
</p>

<p align="center">
OSO enables semantic interoperability across marine observatories, ocean observing systems and research infrastructures by connecting organisations, observatories, platforms, projects, scientific campaigns and datasets using Linked Open Data principles.
</p>

---

<b>🌐 Persistent IRI</b>&nbsp;
<a href="https://w3id.org/earthsemantics/OSO">
https://w3id.org/earthsemantics/OSO
</a>

<b>📦 Publish &amp; Cite</b>&nbsp;
<a href="https://github.com/emso-eric/oso-ontology"><img src="https://img.shields.io/badge/GitHub-Repository-181717?logo=github"></a>
<a href="https://github.com/emso-eric/oso-ontology/releases"><img src="https://img.shields.io/badge/Release-v1.1.0-blue"></a>
<a href="https://doi.org/10.5281/zenodo.19497913"><img src="https://img.shields.io/badge/Zenodo-DOI-1682D4?logo=zenodo"></a>
<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://img.shields.io/badge/License-CC--BY--4.0-green"></a>
<br>

<b>🔎 Discover</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://earthportal.eu/ontologies/OSO"><img src="https://img.shields.io/badge/EarthPortal-Catalogue-8A2BE2"></a>
<a href="https://lov.linkeddata.es/dataset/lov/vocabs/oso"><img src="https://img.shields.io/badge/LOV-Catalogue-3366CC"></a>
<a href="https://doi.org/10.25504/FAIRsharing.654931"><img src="https://img.shields.io/badge/FAIRsharing-Registry-2E8B57"></a>
<br>

<b>📚 Explore</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://emso-eric.github.io/oso-ontology/"><img src="https://img.shields.io/badge/Widoco-Docs-228B22"></a>
<a href="https://service.tib.eu/webvowl/#iri=https://w3id.org/earthsemantics/OSO"><img src="https://img.shields.io/badge/WebVOWL-View-F28C28"></a>
<a href="https://virtuoso.ifremer.fr/oso/sparql"><img src="https://img.shields.io/badge/SPARQL-Query-1E90FF"></a>
<br>

<b>🌐 Standards</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://img.shields.io/badge/RDF-W3C-0B6FA4">
<img src="https://img.shields.io/badge/OWL-2-F28C28">
<img src="https://img.shields.io/badge/SKOS-W3C-7B68EE">
<img src="https://img.shields.io/badge/DCAT-3-2E8B57">
<img src="https://img.shields.io/badge/VoID-W3C-3CB371">
<img src="https://img.shields.io/badge/GeoSPARQL-OGC-228B22">

<b>🚀 Next Steps</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.w3.org/TR/vocab-ssn/"><img src="https://img.shields.io/badge/SSN%2FSOSA-Planned-1E88E5"></a>
<a href="https://i-adopt.github.io/"><img src="https://img.shields.io/badge/I-ADOPT | Planned-1E88E5"></a>
<a href="https://www.w3.org/TR/shacl/"><img src="https://img.shields.io/badge/SHACL-Planned-1E88E5"></a>

---

# Why OSO?

The **Observatories of the Seas Ontology (OSO)** is a FAIR, multilingual ontology that provides a common semantic model for marine observatories, ocean observing systems and marine research infrastructures.

It enables organisations to describe and interlink infrastructures, observing sites, platforms, scientific campaigns, datasets and people using persistent identifiers, Linked Open Data principles and internationally recognised standards.

Originally developed within the **EMSO Data Management Service Group (DMSG)**, OSO is designed as an open and reusable ontology for the global marine science community.

---

# FAIR by Design

OSO has been designed from the outset according to FAIR and Linked Open Data principles.

| FAIR Capability | Status |
|-----------------------------------|:------:|
| Persistent ontology IRI (w3id) | ✅ |
| Versioned DOI (Zenodo) | ✅ |
| FAIRsharing registry | ✅ |
| EarthPortal catalogue | ✅ |
| Linked Open Vocabularies (LOV) | ✅ |
| HTML documentation (GitHub Pages) | ✅ |
| Public SPARQL endpoint | ✅ |
| DCAT metadata | ✅ |
| VoID description | ✅ |
| JSON-LD distribution | ✅ |
| Multilingual annotations | ✅ |
| Provenance metadata | ✅ |
| ORCID author identification | ✅ |
| Open license (CC BY 4.0) | ✅ |

OSO has also been independently evaluated using the **[O'FAIRe](https://github.com/agroportal/fairness)** (Ontology FAIRness Evaluator) framework, which provides an objective assessment of ontology FAIRness. The evaluation details are publicly available from the **[OSO EarthPortal page](https://earthportal.eu/ontologies/OSO)**.

Together, these features make OSO a FAIR, interoperable and reusable ontology for marine observatories, ocean observing systems and marine research infrastructures.

---

# Ontology Overview

```mermaid
graph TD

RI[Research Infrastructure]
RF[Regional Facility]
Site[Site]
SubSite[SubSite<br/>optional]
Platform[Platform]
SubPlatform[SubPlatform<br/>optional]

Cruise[Cruise / CSR]
Project[Project]
Person[Person]
InstrumentType[Instrument type]

EDMO[EDMO organisation ID]
ROR[ROR organisation ID]
CERIF[CERIF]
ORCID[ORCID]
NERC_L06[NERC L06]

RI --> RF
RF --> Site
Site --> SubSite
Site --> Platform
SubSite --> Platform
Platform --> SubPlatform

RF --> Cruise
RF --> Project
RF --> Person
Site --> Person
Platform --> Person

RF -. organisation identifier .-> EDMO
RF -. organisation identifier .-> ROR
Project -. aligned with .-> CERIF
Person -. identifier .-> ORCID
InstrumentType -. controlled vocabulary .-> NERC_L06
Platform --> InstrumentType
```

---

# Essential Links

| Resource | Link |
|-----------|------|
| Persistent ontology IRI | https://w3id.org/earthsemantics/OSO |
| Documentation (Widoco) | https://emso-eric.github.io/oso-ontology/ |
| EarthPortal | https://earthportal.eu/ontologies/OSO |
| SPARQL Endpoint | https://virtuoso.ifremer.fr/oso/sparql |
| GitHub Repository | https://github.com/emso-eric/oso-ontology |
| Zenodo | https://doi.org/10.5281/zenodo.19497913 |
| FAIRsharing | https://doi.org/10.25504/FAIRsharing.654931 |
| LOV | https://lov.linkeddata.es/dataset/lov/vocabs/oso |

---

# Downloads

The latest release is available in several RDF serialisation formats.

| File | Description |
|------|-------------|
| `OSO.ttl` | Turtle (authoritative source) |
| `OSO.owl` | RDF/XML |
| `OSO.jsonld` | JSON-LD |
| `OSO.nt` | N-Triples |
| `OSO.n3` | Notation3 |
| `OSO.trig` | TriG |
| `dcat.ttl` | DCAT metadata |
| `void.ttl` | VoID description |

---

# Repository Structure

```text
.
├── docs/              # Widoco documentation
├── images/            # Ontology figures
├── maintenance/       # Maintenance documentation
├── versions/          # Archived releases
├── .github/           # CI/CD workflows
│
├── OSO.ttl            # Authoritative ontology source
├── dcat.ttl
├── void.ttl
│
├── README.md
├── CHANGELOG.md
└── LICENSE
```

---

# Documentation

| Resource | Description |
|----------|-------------|
| `/docs` | HTML documentation generated with Widoco |
| `/maintenance` | Maintenance and release workflow |
| `/versions` | Archived ontology releases |
| `/images` | Images and diagrams used throughout the ontology |
| `CHANGELOG.md` | Release history |

---

# Example

Example describing a regional facility and one of its sites.

```turtle
:EMSOFrance
    a oso:RegionalFacility ;
    oso:containsSite :AzoresSite .

:AzoresSite
    a oso:Site .
```

---

# Citation

If you use the **Observatories of the Seas Ontology (OSO)** in research, publications or software, please cite:

> Piel, S. & EMSO Data Management Service Group (DMSG). (2026). *Observatories of the Seas Ontology (OSO)* (Version 1.1.0). EMSO ERIC. https://doi.org/10.5281/zenodo.19497913

**Persistent ontology IRI**

https://w3id.org/earthsemantics/OSO

For citation metadata compatible with GitHub and reference managers, see the [`CITATION.cff`](CITATION.cff) file.

---

# Contributing

Contributions are welcome.

Please use:

- GitHub Issues
- Pull Requests

Development and release procedures are documented in:

```
maintenance/
```

---

# License

This project is distributed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

https://creativecommons.org/licenses/by/4.0/

---

# Acknowledgements

OSO is collaboratively developed by the **EMSO Data Management Service Group (DMSG)** with contributions from the EMSO ERIC community, Ifremer and partner organisations.
