# Observatories of the Seas Ontology (OSO) — Version 1.2.1

## Release information

| Property | Value |
| :--- | :--- |
| **Ontology** | Observatories of the Seas Ontology (OSO) |
| **Version** | 1.2.1 |
| **Release date** | **2026-09-25** |
| **Persistent IRI** | https://w3id.org/earthsemantics/OSO |
| **Version IRI** | https://w3id.org/earthsemantics/OSO/1.2.1/ |
| **License** | CC-BY 4.0 |
| **Publisher** | EMSO ERIC |
| **Contributors** | EMSO Data Management Service Group (DMSG), Ifremer |

---

## Overview

Version 1.2.1 is a patch release of OSO 1.2.0. It corrects the ontology
publication metadata so that semantic web tools (OWL API based toolchains
such as WIDOCO, FOOPS and ontology catalogues) resolve the OSO ontology
IRI unambiguously, and it ships multilingual label corrections that were
integrated after the 1.2.0 release assets were produced.

No class, property or instance semantics are modified: the ontology model
and the OSO Knowledge Graph content are unchanged.

---

## Main improvements in version 1.2.1

- Removal of self-referencing annotations on the ontology IRI
  (`omv:URI`, `omv:resourceLocator`, `rdfs:isDefinedBy`) that made OWL API
  select an imported ontology as the document ontology (owlcs/owlapi#1080).
- Corrected multilingual labels for `Western_Mediterranean_Sea`
  (7 language-tagged literals fixed after the 1.2.0 assets were cut).
- Deterministic serialisations regenerated from the authoritative
  `OSO.ttl` source with RDFLib; all formats verified isomorphic.
- Zenodo DOI reserved ahead of publication and embedded in the metadata
  (`10.5281/zenodo.22957027`); the concept DOI remains
  `10.5281/zenodo.19497912`.
- Updated DCAT, VoID and SHACL release metadata.

---

## Distribution architecture

OSO 1.2.1 is published through four complementary RDF distributions:

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
| **Version IRI** | https://w3id.org/earthsemantics/OSO/1.2.1/ |
| **Documentation** | https://emso-eric.github.io/oso-ontology/ |
| **EarthPortal** | https://earthportal.eu/ontologies/OSO |
| **LOV** | https://lov.linkeddata.es/dataset/lov/vocabs/oso |
| **SPARQL endpoint** | https://virtuoso.ifremer.fr/oso/sparql |

---

## Metrics

### Ontology model

| Metric | Value |
| :--- | ---: |
| **RDF triples** | 3,425 |
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
| **RDF triples** | 15,075 |

---

## SHACL validation

OSO 1.2.1 includes a dedicated SHACL shapes graph for validating the
consistency of instance data with the ontology model.

Validation can be performed with [pySHACL](https://github.com/RDFLib/pySHACL):

```bash
pyshacl -s OSO-shacl.ttl -e OSO-ontology.ttl -i rdfs -f human OSO-instances.ttl
```

The OSO 1.2.1 release conforms to the SHACL validation shapes:

```text
Conforms: True
```

---

## Version history

| Version | Description |
| :--- | :--- |
| **1.2.1** | **Current release** |
| 1.2.0 | Previous release |
| 1.1.0 | Earlier release |

Previous version IRI:  
https://w3id.org/earthsemantics/OSO/1.2.0/

---

## Citation

Observatories of the Seas Ontology (OSO), version 1.2.1.  
EMSO ERIC / Ifremer.

FAIRsharing DOI: https://doi.org/10.25504/FAIRsharing.654931

Zenodo DOI: https://doi.org/10.5281/zenodo.22957027

---

## Related resources

- FAIRsharing: https://fairsharing.org/FAIRsharing.654931
- Zenodo (OSO): https://doi.org/10.5281/zenodo.19497912
- GitHub repository: https://github.com/emso-eric/oso-ontology

---

## License

Creative Commons Attribution 4.0 (CC-BY 4.0)

https://creativecommons.org/licenses/by/4.0/
