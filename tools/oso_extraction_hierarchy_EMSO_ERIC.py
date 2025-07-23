# OSO Ontology Hierarchy Extractor (Filtered for EMSO ERIC)
# This script extracts the hierarchy from the OSO ontology and exports it to Excel.
# Only includes Regional Facilities that are part of EMSO ERIC (via oso:Regional_Facility_is_part_of_EMSO_ERIC).

from rdflib import Graph, Namespace, RDF, RDFS, URIRef
import pandas as pd

# Load the OSO ontology file (v0.15)
g = Graph()
g.parse("../oso.ttl", format="turtle")

# Define namespaces and URIs
OSO = Namespace("https://w3id.org/earthsemantics/OSO#")

# Object properties
contains_site = OSO.containsSite
contains_platform = OSO.containsPlatform
site_has_subsite = OSO.Site_has_a_Subsite
platform_has_subplatform = OSO.Platform_contains_Subplatforms
is_part_of_ERIC = OSO.Regional_Facility_is_part_of_EMSO_ERIC

# EMSO ERIC individual
EMSO = OSO.EMSO

# Helper: get label or fragment
def get_label_or_fragment(entity):
    label = next(g.objects(entity, RDFS.label), None)
    if not label:
        label = next(g.objects(entity, URIRef("http://www.w3.org/2004/02/skos/core#prefLabel")), None)
    return str(label) if label else entity.split("#")[-1]

# Filter Regional Facilities part of EMSO
rf_emso = {rf for rf in g.subjects(predicate=is_part_of_ERIC, object=EMSO)}

# Build the hierarchy
rows = []

for rf in rf_emso:
    rf_label = get_label_or_fragment(rf)

    for site in g.objects(rf, contains_site):
        site_label = get_label_or_fragment(site)

        subsites = list(g.objects(site, site_has_subsite))
        platforms = list(g.objects(site, contains_platform))

        if not subsites and not platforms:
            rows.append([rf_label, site_label, "", "", ""])

        for subsite in subsites:
            subsite_label = get_label_or_fragment(subsite)
            rows.append([rf_label, site_label, subsite_label, "", ""])

        for platform in platforms:
            platform_label = get_label_or_fragment(platform)
            subplatforms = list(g.objects(platform, platform_has_subplatform))

            if not subplatforms:
                rows.append([rf_label, site_label, "", platform_label, ""])
            else:
                for subplatform in subplatforms:
                    subplatform_label = get_label_or_fragment(subplatform)
                    rows.append([rf_label, site_label, "", platform_label, subplatform_label])

# Export to Excel
output_file = "OSO_RF_Site_Platform_Filtered_EMSO_20250723.xlsx"
df = pd.DataFrame(rows, columns=["Regional Facility", "Site", "SubSite", "Platform", "SubPlatform"])
df.to_excel(output_file, index=False)
print(f"\n✅ Exported to {output_file}")
