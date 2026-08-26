# Observatories of the Seas Ontology (OSO) — Version 1.2.0

## Release information

| Property | Value |
|---|---|
| Ontology | Observatories of the Seas Ontology (OSO) |
| Version | 1.2.0 |
| Release date | 2026-08-25 |
| Persistent IRI | https://w3id.org/earthsemantics/OSO |
| Version IRI | https://w3id.org/earthsemantics/OSO/1.2.0/ |
| License | CC-BY 4.0 |
| Publisher | EMSO ERIC |
| Contributors | EMSO Data Management Service Group (DMSG), Ifremer |

---

## Overview

Version 1.2.0 introduces a clearer separation between the OSO ontology
schema (TBox) and its instance data (ABox), together with dedicated
SHACL shapes for validation.

This architecture improves ontology reuse, validation, publication and
interoperability, while preserving a complete distribution combining
both the ontology model and the OSO Knowledge Graph.

---

## Main improvements in version 1.2.0

- Separation of the ontology model (TBox) from instance data (ABox).
- Introduction of dedicated ontology, instance data and SHACL distributions.
- Introduction of SHACL shapes for structural and semantic validation of OSO instance data.
- Improved consistency between the TBox, ABox and SHACL validation layer.
- Preservation of a complete combined OSO distribution.
- Enrichment of semantic ecosystem modelling, ontology metadata and multilingual annotations.
- Refinement of classes and properties.
- Updated DCAT metadata describing the ontology, Knowledge Graph and distributions.
- Updated VoID description of the OSO Knowledge Graph.
- Correction of the SmartBay typographical error.
- Improved publication architecture for ontology registries and FAIR assessment services.

---

## Distribution architecture

OSO 1.2.0 is published through four complementary RDF distributions:

| Distribution | Content |
|---|---|
| `OSO-ontology.ttl` | Ontology model (TBox), including ontology metadata, classes, properties and axioms |
| `OSO-instances.ttl` | OSO Knowledge Graph instance data (ABox) |
| `OSO-shacl.ttl` | SHACL shapes for structural and semantic validation of OSO instance data |
| `OSO.ttl` | Complete distribution combining the ontology model and instance data |

The complete distribution is generated from:

```text
OSO-ontology.ttl
        +
OSO-instances.ttl
        ↓
     OSO.ttl

This architecture allows ontology registries, semantic tools and other
applications to consume the ontology model independently from the OSO
Knowledge Graph, while SHACL-aware tools can use OSO-shacl.ttl to
validate instance data. Users requiring the complete graph can continue
to use OSO.ttl

---

## Metadata distributions

Two metadata files describe the OSO publication:

| File | Purpose |
|---|---|
| `OSO-dcat.ttl` | DCAT description of the OSO ontology, Knowledge Graph and distributions |
| `OSO-void.ttl` | VoID description and statistics of the OSO Knowledge Graph |

---

## Main resources

| Resource | URL |
|---|---|
| Ontology IRI | https://w3id.org/earthsemantics/OSO |
| Version IRI | https://w3id.org/earthsemantics/OSO/1.2.0/ |
| Documentation | https://emso-eric.github.io/oso-ontology/ |
| EarthPortal | https://earthportal.eu/ontologies/OSO |
| LOV | https://lov.linkeddata.es/dataset/lov/vocabs/oso |
| SPARQL endpoint | https://virtuoso.ifremer.fr/oso/sparql |

---

## Metrics

### Ontology model

| Metric | Value |
|---|---:|
| RDF triples | 3,423 |
| OWL classes | 44 |
| Object properties | 59 |
| Datatype properties | 11 |

### Instance data

| Metric | Value |
|---|---:|
| RDF triples | 11,654 |
| OWL named individuals | 354 |
| Classes used | 49 |
| Properties used | 113 |
| URI resources | 1,166 |

### SHACL validation shapes

| Metric | Value |
|---|---:|
| RDF triples | 421 |
| Validation status | Conforms |

### Complete distribution

| Metric | Value |
|---|---:|
| RDF triples | 15,077 |

---

## SHACL validation

OSO 1.2.0 includes a dedicated SHACL shapes graph for validating the
consistency of instance data with the ontology model.

Validation can be performed with [pySHACL](https://github.com/RDFLib/pySHACL):

```bash
pyshacl -s OSO-shacl.ttl -e OSO-ontology.ttl -i rdfs -f human OSO-instances.ttl
```

The OSO 1.2.0 release conforms to the SHACL validation shapes:

```text
Conforms: True
```

---

## Version history

| Version | Description |
|---|---|
| 1.2.0 | Current release |
| 1.1.0 | Previous release |

Previous version IRI:  
https://w3id.org/earthsemantics/OSO/1.1.0/

---

## Citation

Observatories of the Seas Ontology (OSO), version 1.2.0.  
EMSO ERIC / Ifremer.

FAIRsharing DOI: https://doi.org/10.25504/FAIRsharing.654931

Zenodo DOI: **to be added after publication of version 1.2.0**

---

## Related resources

- FAIRsharing: https://fairsharing.org/FAIRsharing.654931
- Zenodo (OSO): https://doi.org/10.5281/zenodo.19497913
- GitHub repository: https://github.com/emso-eric/oso-ontology

---

## License

Creative Commons Attribution 4.0 (CC-BY 4.0)

https://creativecommons.org/licenses/by/4.0/
