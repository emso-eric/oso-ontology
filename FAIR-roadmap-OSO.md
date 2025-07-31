# FAIRification Roadmap for the OSO Ontology (based on O'FAIRe Criteria)

📊 **Live FAIRness score of OSO**:  
[https://earthportal.eu/ajax/fair_score/html/?ontologies=OSO](https://earthportal.eu/ajax/fair_score/html/?ontologies=OSO)

This document provides a structured checklist to improve the FAIRness of the OSO ontology according to the [O'FAIRe evaluation framework](https://www.ofaire.eu/). The goal is to progressively reach a score above **90%**, making OSO an exemplary FAIR ontology.

---

## ✅ Findable (F)

### F1Q1 – Globally unique & resolvable identifier (0/11)
- [ ] Register a **DOI** for the ontology (e.g., via Zenodo or Sextant)
- [ ] Ensure it points directly to the OWL/Turtle file, not just a landing page
- [ ] Use `dcterms:identifier`, `dcterms:isReferencedBy`, etc. in `owl:Ontology`

### F2Q2 – Informative metadata on entities (2/4)
- [ ] Add `rdfs:comment`, `dcterms:description`, or `skos:definition` to all key classes, properties, and individuals
- [ ] Ensure **multilingual support** (English, French at minimum)

---

## ✅ Accessible (A)

### A1Q3 – Rich ontology metadata (18/24)
- [ ] Add `omv:*`, `adms:*`, `dcat:*`, `void:*` properties in `owl:Ontology`
- [ ] Include multilingual `dcterms:title` and `dcterms:description`
- [ ] Clarify scope, audience, and intended use of the ontology

### A1Q4 – Machine-readable downloadable formats (0/6)
- [ ] Provide multiple RDF formats: Turtle, RDF/XML, OWL/XML, JSON-LD
- [ ] Configure content negotiation (via `.htaccess` or `w3id.org` redirect rules)
- [ ] Declare `dcat:distribution` and `dcterms:format` in `owl:Ontology`

---

## ✅ Interoperable (I)

### I1Q5 – Reuse of external properties (0/4)
- [ ] Align `oso:` properties using `rdfs:subPropertyOf`, `owl:equivalentProperty` to DC, SKOS, FOAF, etc.

### I2Q4 – Reuse of FAIR external individuals (0/5)
- [ ] Link individuals (e.g., `Ifremer`, `SmartBay`) to **external URIs** (ROR, Wikidata, EDMO, GeoNames) via `owl:sameAs`, `skos:exactMatch`

### I2Q7 – Use of controlled vocabularies for literals (0/5)
- [ ] Replace free-text values with URIs from FAIR vocabularies (e.g., NERC, EU Vocabularies, ADMS)
- [ ] Example: `hasCountry` → `<http://publications.europa.eu/resource/authority/country/FRA>`

---

## ✅ Reusable (R)

### R1Q2 – Rich description per entity (1/3)
- [ ] Add meaningful `rdfs:comment`, `skos:definition` or `dcterms:description` on key entities
- [ ] Support multiple languages

### R1.1Q2 – Rich ontology-level description (1/3)
- [ ] Enrich `owl:Ontology` with a detailed narrative: goals, scope, domain, users

### R1.2Q1 – Metadata about creators/publishers (5/8)
- [ ] Add `pav:createdBy`, `dcterms:publisher`, `adms:status`, `pav:version`, `dcterms:issued`, `dcterms:modified`
- [ ] Use **ORCID URIs** for contributors if possible

### R1.2Q2 – Provenance of entities (4/6)
- [ ] Add `pav:createdBy`, `pav:createdOn`, or `prov:wasAttributedTo` to selected classes, properties, and individuals

### R1.2Q6 – Version links (4/6)
- [ ] Add `owl:priorVersion`, `prov:wasRevisionOf`, `adms:versionNotes` for major releases

### R1.2Q7 – Update tracking per entity (2/4)
- [ ] Use `pav:lastUpdatedOn`, `pav:lastUpdatedBy` on selected key entities

### R1.2Q8 – License per distribution (0/2)
- [ ] Declare `dcterms:license` for each `dcat:distribution` and `dcat:Dataset`
- [ ] Example: `dcterms:license <https://creativecommons.org/licenses/by/4.0/>`

### R1.3Q1 – Fine-grained traceability (0/10)
- [ ] For several key entities (30+), include:
  - `pav:createdBy`, `pav:createdOn`
  - `pav:version`
  - `prov:wasRevisionOf`
  - `adms:versionNotes`

### R1.3Q2 – Wide traceability coverage (0/20)
- [ ] Extend detailed provenance to a larger set of entities (classes, properties, individuals)
- [ ] Consider creating a `provenance.ttl` or `changelog.ttl` file using `prov:Activity`

---

## 🎯 Final Goal
- ✅ Current FAIR score: ~62%
- 🚀 Target: ≥ 90%
- 🏅 OSO will become one of the best-practice examples of FAIR ontologies for research infrastructures

---

_This checklist is maintained as part of the EMSO-ERIC semantic strategy. It is aligned with O'FAIRe criteria and aims to support continuous improvement of the OSO ontology._
