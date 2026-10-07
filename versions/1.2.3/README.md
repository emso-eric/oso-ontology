# Observatories of the Seas Ontology (OSO) — Version 1.2.3

## Release information

| Property | Value |
| :--- | :--- |
| **Ontology** | Observatories of the Seas Ontology (OSO) |
| **Version** | 1.2.3 |
| **Release date** | **2026-10-07** |
| **Persistent IRI** | https://w3id.org/earthsemantics/OSO |
| **Version IRI** | https://w3id.org/earthsemantics/OSO/1.2.3/ |
| **License** | CC-BY 4.0 |
| **Publisher** | EMSO ERIC |
| **Contributors** | EMSO Data Management Service Group (DMSG), Ifremer |

---

## Overview

Version 1.2.3 is a patch release of OSO 1.2.2. It aligns the preferred
namespace prefix declared in the ontology with the prefix registered in
LOV and prefix.cc (FOOPS! check FIND2).

No class, property or individual is added or removed, and the OSO
Knowledge Graph content (ABox) is unchanged.

---

## Main improvements in version 1.2.3

- `vann:preferredNamespacePrefix` changed from `"OSO"` to `"oso"`, the
  prefix registered in LOV and prefix.cc. The namespace IRI
  (`https://w3id.org/earthsemantics/OSO#`) is unchanged.
- `owl:backwardCompatibleWith` now lists 1.2.2.
- Zenodo DOI reserved ahead of publication and embedded in the metadata
  (`10.5281/zenodo.23207425`); the concept DOI remains
  `10.5281/zenodo.19497912`.
- Updated DCAT, VoID and SHACL release metadata.

---

## Distribution architecture

OSO 1.2.3 is published through four complementary RDF distributions:

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
| **Version IRI** | https://w3id.org/earthsemantics/OSO/1.2.3/ |
| **Documentation** | https://emso-eric.github.io/oso-ontology/ |
| **EarthPortal** | https://earthportal.eu/ontologies/OSO |
| **LOV** | https://lov.linkeddata.es/dataset/lov/vocabs/oso |
| **SPARQL endpoint** | https://virtuoso.ifremer.fr/oso/sparql |

---

## Metrics

### Ontology model

| Metric | Value |
| :--- | ---: |
| **RDF triples** | 3,490 |
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
| **RDF triples** | 15,140 |

---

## SHACL validation

OSO 1.2.3 includes a dedicated SHACL shapes graph for validating the
consistency of instance data with the ontology model.

Validation can be performed with [pySHACL](https://github.com/RDFLib/pySHACL):

```bash
pyshacl -s OSO-shacl.ttl -e OSO-ontology.ttl -i rdfs -f human OSO-instances.ttl
```

The OSO 1.2.3 release conforms to the SHACL validation shapes:

```text
Conforms: True
```

---

## Version history

| Version | Description |
| :--- | :--- |
| **1.2.3** | **Current release** |
| 1.2.2 | Previous release |
| 1.2.1 | Earlier release |

Previous version IRI:  
https://w3id.org/earthsemantics/OSO/1.2.2/

---

## Citation

Observatories of the Seas Ontology (OSO), version 1.2.3.  
EMSO ERIC / Ifremer.

FAIRsharing DOI: https://doi.org/10.25504/FAIRsharing.654931

Zenodo DOI: https://doi.org/10.5281/zenodo.23207425

---

## Related resources

- FAIRsharing: https://fairsharing.org/FAIRsharing.654931
- Zenodo (OSO): https://doi.org/10.5281/zenodo.19497912
- GitHub repository: https://github.com/emso-eric/oso-ontology

---

## License

Creative Commons Attribution 4.0 (CC-BY 4.0)

https://creativecommons.org/licenses/by/4.0/
