# OSO Ontology – EMSO ERIC Hierarchical Extraction Tool

This script extracts a 5-level hierarchy from the OSO ontology and generates an Excel file (`.xlsx`) containing only the **Regional Facilities** that are part of **EMSO ERIC**, along with their associated Sites, Subsites, Platforms, and Subplatforms.

---

## ✅ Requirements

- Python **3.10** or higher
- Required Python libraries:

```bash
pip install rdflib pandas openpyxl
```

---

## 📂 Input File

- The input ontology file must be named: `oso.ttl`
- It should be placed in the same folder as the script.
- The ontology must include object properties with the following semantics:
  - `oso:containsSite`
  - `oso:containsPlatform`
  - `oso:Site_has_a_Subsite`
  - `oso:Platform_contains_Subplatforms`
  - `oso:Regional_Facility_is_part_of_EMSO_ERIC`

---

## ▶️ Usage

Once the required libraries are installed and the `oso.ttl` ontology file is placed in the working directory, run the script with:

```bash
python oso_extraction_hierarchy_EMSO_ERIC.py
```

If successful, this will generate the file:

```
OSO_RF_Site_Platform_Filtered_EMSO.xlsx
```

---

## 🧠 Ontology Reference

- OSO Ontology URI: [`https://w3id.org/earthsemantics/OSO`](https://w3id.org/earthsemantics/OSO)
- Source: [`https://github.com/emso-eric/oso-ontology`](https://github.com/emso-eric/oso-ontology)

---

## 🔗 Related Properties Used in the Extraction

| Property                                     | Description                                            |
| -------------------------------------------- | ------------------------------------------------------ |
| `oso:containsSite`                           | Links a Regional Facility to its Sites                 |
| `oso:containsPlatform`                       | Links a Site to one or more Platforms                  |
| `oso:Site_has_a_Subsite`                     | Links a Site to a Subsite                              |
| `oso:Platform_contains_Subplatforms`         | Links a Platform to one or more Subplatforms           |
| `oso:Regional_Facility_is_part_of_EMSO_ERIC` | Indicates EMSO ERIC membership for Regional Facilities |

---

## 📊 Extraction of EMSO ERIC Hierarchical View

A script is provided in the [`extraction/`](../extraction) folder to generate an Excel file containing only the Regional Facilities that are part of **EMSO ERIC**, along with their associated Sites, Subsites, Platforms, and Subplatforms.

- Script: [`extraction/oso_extraction_hierarchy_EMSO_ERIC.py`](../extraction/oso_extraction_hierarchy_EMSO_ERIC.py)
- Input file: `oso.ttl`
- Output file: `OSO_RF_Site_Platform_Filtered_EMSO.xlsx`

➡️ [See example output file (as of 2025-07-15)](../extraction/OSO_RF_Site_Platform_Filtered_EMSO_2025-07-15.xlsx)

Run with:
```bash
python oso_extraction_hierarchy_EMSO_ERIC.py

## 🤝 Feedback / Contribution

- Open an [issue on GitHub](https://github.com/emso-eric/oso-ontology/issues)
- Or contact: [emso.data@emso-eu.org](mailto:emso.data@emso-eu.org)

Pull requests and suggestions are warmly welcomed!

---

## 📜 License

This tool and its documentation are licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

You are free to:

- Share — copy and redistribute the material in any medium or format  
- Adapt — remix, transform, and build upon the material for any purpose, even commercially.

Attribution must be given appropriately (e.g., citing the EMSO ERIC Data Management Group).

---
