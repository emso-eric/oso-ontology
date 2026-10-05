# Observatories of the Seas Ontology (OSO) — Version 1.2.2

## Release information

| Property | Value |
| :--- | :--- |
| **Ontology** | Observatories of the Seas Ontology (OSO) |
| **Version** | 1.2.2 |
| **Release date** | **2026-09-30** |
| **Persistent IRI** | https://w3id.org/earthsemantics/OSO |
| **Version IRI** | https://w3id.org/earthsemantics/OSO/1.2.2/ |
| **License** | CC-BY 4.0 |
| **Publisher** | EMSO ERIC |
| **Contributors** | EMSO Data Management Service Group (DMSG), Ifremer |

---

## Overview

Version 1.2.2 is a patch release of OSO 1.2.1. It improves the FAIR and
provenance metadata of the ontology, documents previously undocumented
terms in the eight supported languages, and corrects the domain of the
`hasDepth` property.

No class, property or individual is added or removed, and the OSO
Knowledge Graph content (ABox) is unchanged.

---

## Main improvements in version 1.2.2

- Ontology publication date (`dcterms:issued`), logo (`foaf:logo`) and
  explicit revision link (`prov:wasRevisionOf` 1.2.1) added to the header.
- Documented vocabulary specialisation relationships (`voaf:specializes`
  PROV-O, FOAF, DCAT, schema.org and GeoSPARQL).
- Multilingual definitions (`rdfs:comment`, 8 languages) added for
  previously undocumented terms.
- Corrected the domain of `OSO:hasDepth` from `owl:Site` (non-existent
  term) to `OSO:Site`.
- Zenodo DOI reserved ahead of publication and embedded in the metadata
  (`10.5281/zenodo.23158930`); the concept DOI remains
  `10.5281/zenodo.19497912`.
- Updated DCAT, VoID and SHACL release metadata.

---

## Distribution architecture

OSO 1.2.2 is published through four complementary RDF distributions:

| Distribution | Content |
| :--- | :--- |
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
```
This architecture allows ontology registries, semantic tools and other
applications to consume the ontology model independently from the OSO
Knowledge Graph, while SHACL-aware tools can use OSO-shacl.ttl to
validate instance data. Users requiring the complete graph can continue
to use OSO.ttl

---

## Metadata distributions

Two metadata files describe the OSO publication:

| File | Purpose |
| :--- | :--- |
| `OSO-dcat.ttl` | DCAT description of the OSO ontology, Knowledge Graph and distributions |
| `OSO-void.ttl` | VoID description and statistics of the OSO Knowledge Graph |

---

## Main resources

| Resource | URL |
| :--- | :--- |
| **Ontology IRI** | https://w3id.org/earthsemantics/OSO |
| **Version IRI** | https://w3id.org/earthsemantics/OSO/1.2.2/ |
| **Documentation** | https://emso-eric.github.io/oso-ontology/ |
| **EarthPortal** | https://earthportal.eu/ontologies/OSO |
| **LOV** | https://lov.linkeddata.es/dataset/lov/vocabs/oso |
| **SPARQL endpoint** | https://virtuoso.ifremer.fr/oso/sparql |

---

## Metrics

### Ontology model

| Metric | Value |
| :--- | ---: |
| **RDF triples** | 3,489 |
| **OWL classes** | 44 |
| **Object properties** | 59 |
| **Datatype properties** | 11 |

### Instance data

| Metric | Value |
| :--- | ---: |
| **RDF triples** | 11,650 |
| **OWL named individuals** | 354 |
| **Classes used** | 48 |
| **Properties used** | 110 |
| **URI resources** | 1,161 |

### SHACL validation shapes

| Metric | Value |
| :--- | ---: |
| **RDF triples** | 421 |
| **Validation status** | Conforms |

### Complete distribution

| Metric | Value |
| :--- | ---: |
| **RDF triples** | 15,139 |

---

## SHACL validation

OSO 1.2.2 includes a dedicated SHACL shapes graph for validating the
consistency of instance data with the ontology model.

Validation can be performed with [pySHACL](https://github.com/RDFLib/pySHACL):

```bash
pyshacl -s OSO-shacl.ttl -e OSO-ontology.ttl -i rdfs -f human OSO-instances.ttl
```

The OSO 1.2.2 release conforms to the SHACL validation shapes:

```text
Conforms: True
```

---

## Version history

| Version | Description |
| :--- | :--- |
| **1.2.2** | **Current release** |
| 1.2.1 | Previous release |
| 1.2.0 | Earlier release |

Previous version IRI:  
https://w3id.org/earthsemantics/OSO/1.2.1/

---

## Citation

Observatories of the Seas Ontology (OSO), version 1.2.2.  
EMSO ERIC / Ifremer.

FAIRsharing DOI: https://doi.org/10.25504/FAIRsharing.654931

Zenodo DOI: https://doi.org/10.5281/zenodo.23158930

---

## Related resources

- FAIRsharing: https://fairsharing.org/FAIRsharing.654931
- Zenodo (OSO): https://doi.org/10.5281/zenodo.19497912
- GitHub repository: https://github.com/emso-eric/oso-ontology

---

## License

Creative Commons Attribution 4.0 (CC-BY 4.0)

https://creativecommons.org/licenses/by/4.0/
