# OSO Ontology Hierarchy Extractor (Filtered for EMSO ERIC)
# This script extracts the hierarchy from the OSO ontology and exports it to Excel.
# Only includes Regional Facilities that are part of EMSO ERIC (via oso:Regional_Facility_is_part_of_EMSO_ERIC).

from rdflib import Graph, Namespace, RDF, RDFS, URIRef
import pandas as pd

# Load the OSO ontology file
g = Graph()
g.parse("oso.ttl", format="turtle")

# Define namespaces and relevant URIs
OSO = Namespace("https://w3id.org/earthsemantics/OSO#")

# Object properties
contains_site = OSO.containsSite
contains_platform = OSO.containsPlatform
site_has_subsite = OSO.Site_has_a_Subsite
platform_has_subplatform = OSO.Platform_contains_Subplatforms
is_part_of_ERIC = OSO.Regional_Facility_is_part_of_EMSO_ERIC

# Target ERIC individual
EMSO = OSO.EMSO

# Utility function to get label or fallback to fragment
def get_label_or_fragment(entity):
    label = next(g.objects(entity, RDFS.label), None)
    if not label:
        label = next(g.objects(entity, URIRef("http://www.w3.org/2004/02/skos/core#prefLabel")), None)
    return str(label) if label else entity.split("#")[-1]

# Extract only Regional Facilities that are part of EMSO
rf_emso = set()
for rf in g.subjects(predicate=is_part_of_ERIC, object=EMSO):
    rf_emso.add(rf)

# Build hierarchy only for these filtered Regional Facilities
data = []

for rf in rf_emso:
    rf_label = get_label_or_fragment(rf)

    for site in g.objects(rf, contains_site):
        site_label = get_label_or_fragment(site)
        subsites = list(g.objects(site, site_has_subsite))
        platforms = list(g.objects(site, contains_platform))

        if not subsites and not platforms:
            data.append([rf_label, site_label, "", "", ""])

        for platform in platforms:
            platform_label = get_label_or_fragment(platform)
            subplatforms = list(g.objects(platform, platform_has_subplatform))
            if not subplatforms:
                data.append([rf_label, site_label, "", platform_label, ""])
            else:
                for subplatform in subplatforms:
                    subplatform_label = get_label_or_fragment(subplatform)
                    data.append([rf_label, site_label, "", platform_label, subplatform_label])

        for subsite in subsites:
            subsite_label = get_label_or_fragment(subsite)
            data.append([rf_label, site_label, subsite_label, "", ""])

# Create the DataFrame and save to Excel
df = pd.DataFrame(data, columns=["Regional Facility", "Site", "SubSite", "Platform", "SubPlatform"])
df.to_excel("OSO_RF_Site_Platform_Filtered_EMSO.xlsx", index=False)

print("✅ Filtered export completed: OSO_RF_Site_Platform_Filtered_EMSO.xlsx")
