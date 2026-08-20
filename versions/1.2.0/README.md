# Observatories of the Seas Ontology (OSO) — Version 1.2.0

## Release information

| Property | Value |
|---|---|
| Ontology | Observatories of the Seas Ontology (OSO) |
| Version | 1.2.0 |
| Release date | 2026-XX-XX |
| Persistent IRI | https://w3id.org/earthsemantics/OSO |
| Version IRI | https://w3id.org/earthsemantics/OSO/1.2.0/ |
| License | CC-BY 4.0 |
| Publisher | EMSO ERIC |
| Contributors | EMSO Data Management Service Group (DMSG), Ifremer |

---

## Overview

Version 1.2.0 introduces a clearer separation between the OSO ontology
schema (TBox) and its instance data (ABox).

This separation improves ontology reuse, publication and interoperability
while preserving a complete distribution combining both the ontology
model and the OSO Knowledge Graph.

---

## Main improvements in version 1.2.0

- Separation of the ontology model (TBox) from instance data (ABox).
- Introduction of dedicated ontology and instance distributions.
- Preservation of a complete combined OSO distribution.
- Updated DCAT metadata describing the different distributions.
- Updated VoID description of the OSO Knowledge Graph.
- Correction of the SmartBay typographical error.
- Improved publication architecture for ontology registries and FAIR
  assessment services.

---

## Distribution architecture

OSO 1.2.0 is published through three complementary RDF distributions:

| Distribution | Content |
|---|---|
| `OSO-ontology.ttl` | Ontology model (TBox), including ontology metadata, classes, properties and axioms |
| `OSO-instances.ttl` | OSO Knowledge Graph instance data (ABox) |
| `OSO.ttl` | Complete distribution combining the ontology model and instance data |

The complete distribution is generated from:

```text
OSO-ontology.ttl
        +
OSO-instances.ttl
        ↓
     OSO.ttl