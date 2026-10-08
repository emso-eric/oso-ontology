# FOOPS! Assessment — OSO

Raw results returned by the FOOPS! API (`POST https://foops.linkeddata.es/assessOntology`), request body `{"ontologyUri":"https://w3id.org/earthsemantics/OSO"}`.

| Field | Value |
|---|---|
| `ontology_URI` | https://w3id.org/earthsemantics/OSO |
| `ontology_title` | Οντολογία θαλάσσιων παρατηρητηρίων (OSO) |
| `ontology_license` | https://creativecommons.org/licenses/by/4.0/ |
| `resource_found` | ontology |
| `overall_score` | **1.0** |
| `checks` | 24 |
| Report generated | 2026-10-08 11:51 UTC |

---

## Results by check

## Findable

### `PURL1` — Ontology has a persistent URL

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/PURL1 |
| `principle_id` | F1 |
| `category_id` | Findable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> Ontology URI follows a follows a persistent URI scheme (URI: https://w3id.org/earthsemantics/OSO )

<details><summary>description</summary>

<p>This test verifies if the ontology has a persistent URL. We do so by checking if the ontology URI follows any of the following URI schemes:</p>
<ul>
<li>w3id.org</li>
<li>doi.org</li>
<li>purl.org (or purl.something.org)  </li>
<li>linked.data.gov.au</li>
<li>dbpedia.org</li>
<li>www.w3.org</li>
<li>perma.cc</li>
<li>data.europa.eu</li>
</ul>

</details>

### `URI1` — Ontology URI is resolvable

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/URI1 |
| `principle_id` | F1 |
| `category_id` | Findable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> Ontology URL is resolvable in application/rdf+xml

<details><summary>description</summary>

<p>This test verifies if the ontology URI that was found within the ontology document is resolvable. 
Note that the ontology URI found in the ontology may be different from the URI used in the assessment.
The test will pass if the vocabulary is resolvable in any of the following RDF serializations: RDF/XML, TTL, N-Triples, JSON-LD. The test will fail if no known RDF serialization is returned, or the serialization returned is not among one of the aforementioned. </p>

</details>

### `OM1` — Ontology minimum metadata is declared

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/OM1 |
| `principle_id` | F2 |
| `category_id` | Findable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 6 / 6 |

**explanation**

> All the minimum metadata were found!

<details><summary>description</summary>

<p>This check verifies if the following  minimum metadata are present in the ontology metadata:</p>
<ul>
<li>title: declared using <a href="http://purl.org/dc/elements/1.1/title">dc:title</a>, <a href="http://purl.org/dc/terms/title">dcterms:title</a> or <a href="http://schema.org/name">schema:name</a></li>
<li>description: declared using <a href="http://purl.org/dc/elements/1.1/abstract">dc:abstract</a>, <a href="http://purl.org/dc/terms/abstract">dcterms:abstract</a>, <a href="http://purl.org/dc/elements/1.1/description">dc:description</a>, <a href="http://purl.org/dc/terms/description">dcterms:description</a>, <a href="http://schema.org/description">schema:description</a>, <a href="http://www.w3.org/2000/01/rdf-schema#comment">rdfs:comment</a>, <a href="http://usefulinc.com/ns/doap#description">doap:description</a>, <a href="http://usefulinc.com/ns/doap#shortdesc">doap:shortdesc</a> or <a href="http://www.w3.org/2004/02/skos/core#note">skos:note</a></li>
<li>license: declared using <a href="http://purl.org/dc/terms/license">dcterms:license</a>, <a href="http://schema.org/licesne">schema:license</a>, <a href="http://usefulinc.com/ns/doap#license">doap:license</a> or <a href="http://creativecommons.org/ns#license">cc:license</a>.</li>
<li>version iri: declared using <a href="http://www.w3.org/2002/07/owl#versionIRI">owl:versionIRI</a></li>
<li>creator: declared using <a href="http://purl.org/dc/elements/1.1/creator">dc:creator</a>, <a href="http://purl.org/dc/terms/creator">dcterms:creator</a>, <a href="http://purl.org/pav/createdBy">pav:createdBy</a>, <a href="http://purl.org/pav/authoredBy">pav:authoredBy</a>, <a href="http://schema.org/creator">schema:creator</a>, <a href="http://www.w3.org/ns/prov#wasAttributedTo">prov:wasAttributedTo</a> or <a href="http://usefulinc.com/ns/doap#developer">doap:developer</a></li>
<li>namespace URI: declared using  <a href="http://purl.org/vocab/vann/">vann:preferredNamespaceUri</a></li>
</ul>
<p>The test will pass if all ontology metadata are present. The test will fail otherwise, indicating the properties that are missing.</p>

</details>

### `FIND1` — Ontology prefix is declared

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/FIND1 |
| `principle_id` | F3 |
| `category_id` | Findable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> Prefix declaration found in the ontology: oso

<details><summary>description</summary>

<p>This check verifies if an ontology prefix is declared in the ontology metadata. 
The test will pass if a <a href="http://purl.org/vocab/vann/">vann:preferredNamespacePrefix</a> is declared.
Otherwise, the test will fail. </p>

</details>

### `FIND2` — Ontology prefix is found in prefix.cc or LOV

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/FIND2 |
| `principle_id` | F4 |
| `category_id` | Findable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 2 / 2 |

**explanation**

> Prefix declaration found with correct namespace (in prefix.cc)

<details><summary>description</summary>

<p>This test verifies whether the ontology prefix is available in <a href="(https://prefix.cc/)">prefix.cc</a> or the <a href="(https://lov.linkeddata.es/)">Linked Open Vocabularies (LOV)</a> registries. 
The test will pass if: </p>
<ol>
<li>there is a prefix declared in the assessed ontology, </li>
<li>the prefix is found in <a href="https://lov.linkeddata.es/">LOV</a> or <a href="https://prefix.cc/">prefix.cc</a> </li>
<li>if found in <a href="https://lov.linkeddata.es/">LOV</a> or <a href="https://prefix.cc/">prefix.cc</a> , the namespace URI associated with the prefix is the same as the assessed ontology URI (or preferred namespace URI)</li>
</ol>
<p>Otherwise, the test will fail. </p>

</details>

### `FIND3` — Ontology found in community registry

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/FIND3 |
| `principle_id` | F4 |
| `category_id` | Findable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> Otology is included in a data catalog.

<details><summary>description</summary>

<p>This test verifies if the ontology can be found in a public registry like the Linked Open Vocabularies (LOV) public registry.
The test will pass if the assessed ontology URI is found in the list of vocabularies returned by LOV.
Alternatively, if there is a <a href="https://schema.org/includedInDataCatalog">schema:includedInDataCatalog</a> annotation, the test will pass.
The test will fail otherwise.   </p>

</details>

### `VER1` — A version IRI is declared in the ontology metadata

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/VER1 |
| `principle_id` | F1 |
| `category_id` | Findable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 2 / 2 |

**explanation**

> Version IRI defined, IRI is different from ontology URI. Version info found (1.2.3 – ευθυγράμμιση του προτιμώμενου προθέματος χώρου ονομάτων (vann:preferredNamespacePrefix) σε «oso», όπως είναι καταχωρισμένο στα LOV και prefix.cc).

<details><summary>description</summary>

<p>This test verifies whether there is an id for this ontology version, and whether the id is unique (i.e., different from the ontology URI). The test will pass if: </p>
<ol>
<li>The ontology has a versionIRI (<a href="http://www.w3.org/2002/07/owl#versionIRI">owl:versionIRI</a>) and </li>
<li>The versionIRI used is different from the ontology URI.</li>
</ol>
<p>Otherwise the test will fail. The test will also verify whether version information is present (through <a href="http://www.w3.org/2002/07/owl#versionInfo">owl:versionInfo</a>), but this is optional.</p>

</details>

### `VER2` — Ontology version IRI resolves

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/VER2 |
| `principle_id` | F1 |
| `category_id` | Findable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> Version IRI resolves

<details><summary>description</summary>

<p>This test verifies if the version IRI resolves. The test will pass if there is a version IRI for the ontology/vocabulary (detected using <a href="http://www.w3.org/2002/07/owl#versionIRI">owl:versionIRI</a> in the ontology metadata) and whether doing a request to said IRI returns a resource. 
The test will fail if the resource is not found (404 response) or returns an error.</p>

</details>

### `URI2` — Consistent ontology IDs are employed

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/URI2 |
| `principle_id` | F1 |
| `category_id` | Findable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> Ontology URI is equal to ontology id

<details><summary>description</summary>

<p>This check verifies if the ontology URI is equal to the ontology ID. The test passes if the ontology URI used to load the ontology document is the same as the ontology id found in the document itself. Otherwise the test will fail.</p>

</details>

## Accessible

### `CN1` — Ontology has content negotiation for RDF in RDF/XML, TTL, NTriples or JSON-LD serializations

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/CN1 |
| `principle_id` | A1 |
| `category_id` | Accessible |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 2 / 2 |

**explanation**

> Ontology available in: HTML, RDF

<details><summary>description</summary>

<p>This test verifies whether HTML and an RDF representation is available for the target vocabulary by doing content negotiation on the ontology URI. The test will pass if the vocabulary is available in HTML and in any of the following RDF serializations: </p>
<ul>
<li>RDF/XML (application/rdf+xml), </li>
<li>TTL (text/turtle), </li>
<li>N-Triples (text/n3), </li>
<li>JSON-LD (application/ld+json)</li>
</ul>
<p>The test will fail if no HTML is returned, if no known RDF serialization is returned, or the serialization returned is not among one of the aforementioned.</p>

</details>

### `FIND_3_BIS` — Ontology metadata are accessible, even when the ontology is not

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/FIND_3_BIS |
| `principle_id` | A2 |
| `category_id` | Accessible |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> Otology is included in a data catalog.

<details><summary>description</summary>

<p>Metadata are accessible even when the ontology is no longer available. Since the metadata is usually included in the ontology, this test verifies if the ontology can be found in the <a href="https://lov.linkeddata.es">Linked Open Vocabularies (LOV) public registry</a>.
The test will pass if the assessed ontology/vocabulary URI is found in the LOV list of vocabularies.
Alternatively, if there is a <a href="https://schema.org/includedInDataCatalog">schema:includedInDataCatalog</a> annotation, the test will pass.
The test will fail otherwise. </p>

</details>

### `HTTP1` — Ontology uses an open protocol

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/HTTP1 |
| `principle_id` | A1.1 |
| `category_id` | Accessible |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> The ontology uses an open protocol

<details><summary>description</summary>

<p>This check verifies if the ontology uses an open protocol (HTTP or HTTPS). The test will pass if the ontology URI starts with http or https. It will fail otherwise.</p>

</details>

## Reusable

### `DOC1` — Ontology has HTML documentation

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/DOC1 |
| `principle_id` | R1 |
| `category_id` | Reusable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> Ontology available in HTML

<details><summary>description</summary>

<p>This test verifies if the ontology has an HTML documentation. The test will attempt to download an HTML representation using the ontology URI, with content negotiation </p>

</details>

### `OM2` — Ontology declares recommended metadata

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/OM2 |
| `principle_id` | R1 |
| `category_id` | Reusable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 4 / 4 |

**explanation**

> All recommended metadata found!

<details><summary>description</summary>

<p>This test verifies if the following recommended metadata are present in the ontology metadata: </p>
<ul>
<li>Namespace prefix: declared using <a href="http://purl.org/vocab/vann/">vann:preferredNamespacePrefix</a></li>
<li>Version info: declared using <a href="http://www.w3.org/2002/07/owl#versionInfo">owl:versionInfo</a> or <a href="http://schema.org/schemaVersion">schema:schemaVersion</a></li>
<li>Creation date: declared using <a href="http://purl.org/dc/terms/created">dcterms:created</a>, <a href="http://schema.org/dateCreated">schema:dateCreated</a>, <a href="http://usefulinc.com/ns/doap#created">doap:created</a>, <a href="http://www.w3.org/ns/prov#generatedAtTime">prov:generatedAtTime</a> or <a href="http://purl.org/pav/">pav:createdOn</a></li>
<li>Citation: declared using <a href="http://purl.org/dc/terms/bibliographicCitation">dcterms:bibliographicCitation</a></li>
<li>Contributor (optional): declared using <a href="http://purl.org/dc/elements/1.1/contributor">dc:contributor</a>, <a href="http://purl.org/dc/terms/contributor">dcterms:contributor</a>, schema:contributor, <a href="http://usefulinc.com/ns/doap#documenter">doap:documenter</a>, <a href="http://usefulinc.com/ns/doap#maintainer">doap:maintainer</a>, <a href="http://usefulinc.com/ns/doap#helper">doap:helper</a>, <a href="http://usefulinc.com/ns/doap#translator">doap:translator</a> or <a href="http://purl.org/pav/">pav:contributedBy</a>.</li>
</ul>
<p>The test will pass if all the recommended metadata properties are available in the ontology metadata (using any of the vocabularies listed above). The test will also check if contributor is present, but with no penalty (as not all ontologies have a contributor).</p>

</details>

### `OM3` — Ontology declares detailed metadata

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/OM3 |
| `principle_id` | R1 |
| `category_id` | Reusable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 6 / 6 |

**explanation**

> All optional metadata found!

<details><summary>description</summary>

<p>This test verifies if the ontology includes the following detailed metadata:</p>
<ul>
<li>Digital Object Identifier (DOI): declared using  <a href="http://purl.org/ontology/bibo/doi">bibo:doi</a>, <a href="https://schema.org/identifier">schema:identifier</a> (if a doi is provided) or <a href="http://purl.org/dc/terms/identifier">dcterms:identifier</a> (if a doi is provided)</li>
<li>publisher: declared using <a href="http://purl.org/dc/elements/1.1/publisher">dc:publisher</a>, <a href="http://purl.org/dc/terms/publisher">dcterms:publisher</a> or <a href="https://schema.org/publisher">schema:publisher</a></li>
<li>logo: declared using <a href="http://xmlns.com/foaf/0.1/logo">foaf:logo</a> or <a href="https://schema.org/logo">schema:logo</a></li>
<li>status: declared using <a href="http://purl.org/ontology/bibo/status">bibo:status</a> or <a href="https://w3id.org/mod#status">mod:status</a></li>
<li>source: declared using <a href="http://purl.org/dc/terms/source">dcterms:source</a> or <a href="http://www.w3.org/ns/prov#hadOriginalSource">prov:hadOriginalSource</a></li>
<li>issued date: declared using <a href="http://purl.org/dc/terms/issued">dcterms:issued</a></li>
<li>previous version (optional): declared using  <a href="http://purl.org/dc/elements/1.1/replaces">dc:replaces</a>, <a href="http://purl.org/dc/terms/replaces">dcterms:replaces</a>, <a href="http://www.w3.org/ns/prov#wasRevisionOf">prov:wasRevisionOf</a>, <a href="http://www.w3.org/2002/07/owl#priorVersion">owl:priorVersion</a> or <a href="http://purl.org/pav/previousVersion">pav:previousVersion</a></li>
<li>backward compatibility (optional): declared using <a href="http://www.w3.org/2002/07/owl#backwardCompatibleWith">owl:backwardCompatibleWith</a></li>
<li>modified date (optional): declared using <a href="http://purl.org/dc/terms/modified">dcterms:modified</a> or <a href="https://schema.org/dateModified">schema:dateModified</a></li>
</ul>
<p>The test will pass if all the detailed metadata properties are available in the ontology metadata (using any of the vocabularies listed above). The test will also check if previosu version, backward compatibility and modified date are present, but with no penalty (as not all ontologies have a previous version). </p>

</details>

### `OM4_1` — Ontology has a license available

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/OM4.1 |
| `principle_id` | R1.1 |
| `category_id` | Reusable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> A license was found https://creativecommons.org/licenses/by/4.0/

<details><summary>description</summary>

<p>This test verifies if a license (or rights) are associated with the ontology.
The test will pass if a license is declared using any of the following properties: <a href="http://purl.org/dc/terms/license">dcterms:license</a>, <a href="https://schema.org/license">schema:license</a>, <a href="http://usefulinc.com/ns/doap#license">doap:license</a> or <a href="http://creativecommons.org/ns#license">cc:license</a>.</p>
<p>If a license is not found, but rights are declared (using <a href="http://purl.org/dc/elements/1.1/rights">dc:rights</a>, <a href="http://purl.org/dc/terms/rights">dcterms:rights</a> or <a href="http://purl.org/dc/terms/accessRights">dcterms:accessRights</a>), the test will pass as well.</p>
<p>Otherwise, the test will fail (i.e., no license or rights are declared).</p>

</details>

### `OM4_2` — Ontology license is resolvable

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/OM4.2 |
| `principle_id` | R1.1 |
| `category_id` | Reusable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> License could be resolved

<details><summary>description</summary>

<p>This test verifies if the ontology license is resolvable. The test will pass if the license available in the ontology metadata resolves to a resource. The test will fail if no license is declared (OM4.1), if the license is not a URI/URL, or if the response when requesting is 404 or an error. </p>

</details>

### `OM5_1` — Ontology declares basic provenance metadata

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/OM5.1 |
| `principle_id` | R1.2 |
| `category_id` | Reusable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 2 / 2 |

**explanation**

> All basic provenance metadata found!

<details><summary>description</summary>

<p>This check verifies if basic provenance metadata is available for the ontology:  </p>
<ul>
<li>creator: declared using <a href="http://purl.org/dc/elements/1.1/creator">dc:creator</a>, <a href="http://purl.org/dc/terms/creator">dcterms:creator</a>, <a href="http://purl.org/pav/createdBy">pav:createdBy</a>, <a href="http://purl.org/pav/authoredBy">pav:authoredBy</a>, <a href="https://schema.org/creator">schema:creator</a> or <a href="http://usefulinc.com/ns/doap#developer">doap:developer</a></li>
<li>creation date: declared using <a href="http://purl.org/dc/terms/created">dcterms:created</a>, <a href="https://schema.org/dateCreated">schema:dateCreated</a>, <a href="http://usefulinc.com/ns/doap#created">doap:created</a>, <a href="http://www.w3.org/ns/prov#generatedAtTime">prov:generatedAtTime</a> or <a href="http://purl.org/pav/createdOn">pav:createdOn</a></li>
<li>contributor (optional): declared using <a href="http://purl.org/dc/elements/1.1/contributor">dc:contributor</a>, <a href="http://purl.org/dc/terms/contributor">dcterms:contributor</a>, <a href="https://schema.org/contributor">schema:contributor</a>, <a href="http://usefulinc.com/ns/doap#documenter">doap:documenter</a>, <a href="http://usefulinc.com/ns/doap#maintainer">doap:maintainer</a>, <a href="http://usefulinc.com/ns/doap#helper">doap:helper</a>, <a href="http://usefulinc.com/ns/doap#translator">doap:translator</a> or <a href="http://purl.org/pav/contributedBy">pav:contributedBy</a>.</li>
<li>previous version (optional): declared using  <a href="http://purl.org/dc/elements/1.1/replaces">dc:replaces</a>, <a href="http://purl.org/dc/terms/replaces">dcterms:replaces</a>, <a href="http://www.w3.org/ns/prov#wasRevisionOf">prov:wasRevisionOf</a>, <a href="http://www.w3.org/2002/07/owl#previousVersion">owl:priorVersion</a>, <a href="http://purl.org/pav/previousVersion">pav:previousVersion</a></li>
</ul>
<p>The test will pass if creator and creation date are present. The test will fail otherwise, indicating the properties that are missing.</p>

</details>

### `OM5_2` — Ontology declares detailed provenance metadata

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/OM5.2 |
| `principle_id` | R1.2 |
| `category_id` | Reusable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 2 / 2 |

**explanation**

> All detailed provenance metadata found!

<details><summary>description</summary>

<p>This check verifies if detailed provenance information is available for the ontology: </p>
<ul>
<li>issued date: declared using <a href="http://purl.org/dc/terms/issued">dcterms:issued</a>, <a href="http://purl.org/dc/terms/submitted">dcterms:submitted</a> or <a href="https://schema.org/datePublished">schema:datePublished</a></li>
<li>publisher: declared using <a href="http://purl.org/dc/elements/1.1/publisher">dc:publisher</a>, <a href="http://purl.org/dc/terms/publisher">dcterms:publisher</a> or <a href="https://schema.org/publisher">schema:publisher</a></li>
</ul>
<p>The test will pass if both metadata fields are present. The test will fail otherwise, indicating the properties that are missing.</p>

</details>

### `VOC3` — Ontology documentation: all terms have labels

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/VOC3 |
| `principle_id` | R1 |
| `category_id` | Reusable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 100 / 100 |

**explanation**

> Labels found for all ontology terms (100 terms found)

<details><summary>description</summary>

<p>This test verifies the extent to which all ontology terms have labels.
The test will pass if all classes, properties and data properties have either an <a href="http://www.w3.org/2000/01/rdf-schema#label">rdfs:label</a> or <a href="http://www.w3.org/2004/02/skos/core#prefLabel">skos:prefLabel</a>.
For skos vocabularies, only the skos:Concepts are assessed.
Otherwise, the test will fail, indicating the level of completeness found (i.e., percentage of documented terms) </p>

</details>

### `VOC4` — Ontology documentation: all terms have definitions

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/VOC4 |
| `principle_id` | R1 |
| `category_id` | Reusable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 100 / 100 |

**explanation**

> Descriptions found for all ontology terms (100 terms found)

<details><summary>description</summary>

<p>This check verifies whether all ontology terms have descriptions. 
The test will pass if all classes, properties and data properties have at least one <a href="http://www.w3.org/2000/01/rdf-schema#comment">rdfs:comment</a>, <a href="http://www.w3.org/2004/02/skos/core#definition">skos:definition</a> or <a href="http://purl.obolibrary.org/obo/IAO_0000118">obo:IAO_0000118</a> annotation.
For skos vocabularies, only the skos:Concepts are assessed.</p>
<p>The test will fail otherwise, showing the level of completeness obtained (i.e. the percentage of documented terms).</p>

</details>

## Interoperable

### `RDF1` — Ontology is available in RDF (TTL, N3, RDF/XML or JSON-LD)

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/RDF1 |
| `principle_id` | I1 |
| `category_id` | Interoperable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> Ontology available in RDF

<details><summary>description</summary>

<p>This test verifies if the ontology has a valid RDF serialization (TTL, N3, RDF/XML or JSON-LD are supported).
The test will fail if no RDF serialization could be loaded for analysis (e.g., the ontology has typos that prevent its parsing).
The test uses the OWLAPI to load ontologies or vocabularies.</p>

</details>

### `VOC1` — Ontology reuses existing vocabularies for metadata annotations

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/VOC1 |
| `principle_id` | I2 |
| `category_id` | Interoperable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> Ontology reuses existing vocabularies for declaring metadata. 

**reference_resources**

- `http://purl.org/dc/terms/`
- `http://purl.org/pav/`
- `http://purl.org/vocab/vann/`
- `http://www.w3.org/2000/01/rdf-schema#`
- `http://www.w3.org/2002/07/owl#`
- `http://www.w3.org/ns/prov#`
- `http://xmlns.com/foaf/0.1/`
- `https://w3id.org/mod#`

<details><summary>description</summary>

<p>This test verifies if the ontology reuses other vocabularies for declaring metadata terms (see tests OM1... OM5).
The test will pass if metadata annotations using properties from any of the following vocabularies are used:</p>
<ul>
<li><a href="http://purl.org/dc/elements/1.1/">Dublin Core</a> (dc, dcterms)</li>
<li><a href="https://schema.org/">Schema.org</a> (schema)</li>
<li><a href="http://purl.org/vocab/vann/">Vocabulary for annotating vocabulary descriptions</a> (vann)</li>
<li><a href="http://www.w3.org/ns/prov#">W3C Provenance standard</a> (prov)</li>
<li><a href="http://purl.org/ontology/bibo/">Bibliographic Ontology</a> (bibo)</li>
<li><a href="http://purl.org/pav/">Provenance, Authoring and Versioning</a> (pav)</li>
<li><a href="http://xmlns.com/foaf/0.1/">Firend of a friend</a> (foaf)</li>
<li><a href="http://usefulinc.com/ns/doap#">Description of a project</a> (doap)</li>
<li><a href="https://w3id.org/mod#">Metadata vocabulary for ontology descriptions</a> (mod)</li>
<li><a href="http://www.w3.org/2002/07/owl#">Web Ontology Language</a> (owl)</li>
<li><a href="http://www.w3.org/2000/01/rdf-schema#">Resource description framework schema</a> (rdfs)</li>
</ul>
<p>The test will also return the vocabularies that were found. If none are found, the test will fail.</p>

</details>

### `VOC2` — Ontology imports or reuses well established vocabularies

| Field | Value |
|---|---|
| `id` | https://w3id.org/foops/test/VOC2 |
| `principle_id` | I2 |
| `category_id` | Interoperable |
| `status` | `ok` |
| `total_passed_tests` / `total_tests_run` | 1 / 1 |

**explanation**

> The ontology imports the following vocabularies: . Foundational ontologies extended. Nicely done!

**reference_resources**

- `http://www.w3.org/2003/01/geo/wgs84_pos`
- `http://www.w3.org/2004/02/skos/core`
- `http://www.w3.org/ns/prov-o`
- `http://xmlns.com/foaf/0.1/`

<details><summary>description</summary>

<p>This test verifies if the ontology imports/extends other vocabularies (besides RDF, OWL and RDFS).
The test will pass if other vocabularies are imported (<a href="http://www.w3.org/2002/07/owl#imports">owl:imports</a>), or if classes, properties or data properties 
outside the ontology URI or namespace URI are used.
The test wil fail if no terms are reused.</p>

</details>

---

## Raw API response (JSON, untruncated)

```json
{
  "ontology_URI": "https://w3id.org/earthsemantics/OSO",
  "ontology_title": "Οντολογία θαλάσσιων παρατηρητηρίων (OSO)",
  "ontology_license": "https://creativecommons.org/licenses/by/4.0/",
  "resource_found": "ontology",
  "overall_score": 1.0,
  "checks": [
    {
      "id": "https://w3id.org/foops/test/PURL1",
      "principle_id": "F1",
      "category_id": "Findable",
      "status": "ok",
      "title": "Ontology has a persistent URL",
      "explanation": "Ontology URI follows a follows a persistent URI scheme (URI: https://w3id.org/earthsemantics/OSO )",
      "abbreviation": "PURL1",
      "description": "<p>This test verifies if the ontology has a persistent URL. We do so by checking if the ontology URI follows any of the following URI schemes:</p>\n<ul>\n<li>w3id.org</li>\n<li>doi.org</li>\n<li>purl.org (or purl.something.org)  </li>\n<li>linked.data.gov.au</li>\n<li>dbpedia.org</li>\n<li>www.w3.org</li>\n<li>perma.cc</li>\n<li>data.europa.eu</li>\n</ul>",
      "total_passed_tests": 1,
      "total_tests_run": 1
    },
    {
      "id": "https://w3id.org/foops/test/URI1",
      "principle_id": "F1",
      "category_id": "Findable",
      "status": "ok",
      "title": "Ontology URI is resolvable",
      "explanation": "Ontology URL is resolvable in application/rdf+xml",
      "abbreviation": "URI1",
      "description": "<p>This test verifies if the ontology URI that was found within the ontology document is resolvable. \nNote that the ontology URI found in the ontology may be different from the URI used in the assessment.\nThe test will pass if the vocabulary is resolvable in any of the following RDF serializations: RDF/XML, TTL, N-Triples, JSON-LD. The test will fail if no known RDF serialization is returned, or the serialization returned is not among one of the aforementioned. </p>",
      "total_passed_tests": 1,
      "total_tests_run": 1
    },
    {
      "id": "https://w3id.org/foops/test/CN1",
      "principle_id": "A1",
      "category_id": "Accessible",
      "status": "ok",
      "title": "Ontology has content negotiation for RDF in RDF/XML, TTL, NTriples or JSON-LD serializations",
      "explanation": "Ontology available in: HTML, RDF",
      "abbreviation": "CN1",
      "description": "<p>This test verifies whether HTML and an RDF representation is available for the target vocabulary by doing content negotiation on the ontology URI. The test will pass if the vocabulary is available in HTML and in any of the following RDF serializations: </p>\n<ul>\n<li>RDF/XML (application/rdf+xml), </li>\n<li>TTL (text/turtle), </li>\n<li>N-Triples (text/n3), </li>\n<li>JSON-LD (application/ld+json)</li>\n</ul>\n<p>The test will fail if no HTML is returned, if no known RDF serialization is returned, or the serialization returned is not among one of the aforementioned.</p>",
      "total_passed_tests": 2,
      "total_tests_run": 2
    },
    {
      "id": "https://w3id.org/foops/test/DOC1",
      "principle_id": "R1",
      "category_id": "Reusable",
      "status": "ok",
      "title": "Ontology has HTML documentation",
      "explanation": "Ontology available in HTML",
      "abbreviation": "DOC1",
      "description": "<p>This test verifies if the ontology has an HTML documentation. The test will attempt to download an HTML representation using the ontology URI, with content negotiation </p>",
      "total_passed_tests": 1,
      "total_tests_run": 1
    },
    {
      "id": "https://w3id.org/foops/test/RDF1",
      "principle_id": "I1",
      "category_id": "Interoperable",
      "status": "ok",
      "title": "Ontology is available in RDF (TTL, N3, RDF/XML or JSON-LD)",
      "explanation": "Ontology available in RDF",
      "abbreviation": "RDF1",
      "description": "<p>This test verifies if the ontology has a valid RDF serialization (TTL, N3, RDF/XML or JSON-LD are supported).\nThe test will fail if no RDF serialization could be loaded for analysis (e.g., the ontology has typos that prevent its parsing).\nThe test uses the OWLAPI to load ontologies or vocabularies.</p>",
      "total_passed_tests": 1,
      "total_tests_run": 1
    },
    {
      "id": "https://w3id.org/foops/test/OM1",
      "principle_id": "F2",
      "category_id": "Findable",
      "status": "ok",
      "title": "Ontology minimum metadata is declared",
      "explanation": "All the minimum metadata were found!",
      "abbreviation": "OM1",
      "description": "<p>This check verifies if the following  minimum metadata are present in the ontology metadata:</p>\n<ul>\n<li>title: declared using <a href=\"http://purl.org/dc/elements/1.1/title\">dc:title</a>, <a href=\"http://purl.org/dc/terms/title\">dcterms:title</a> or <a href=\"http://schema.org/name\">schema:name</a></li>\n<li>description: declared using <a href=\"http://purl.org/dc/elements/1.1/abstract\">dc:abstract</a>, <a href=\"http://purl.org/dc/terms/abstract\">dcterms:abstract</a>, <a href=\"http://purl.org/dc/elements/1.1/description\">dc:description</a>, <a href=\"http://purl.org/dc/terms/description\">dcterms:description</a>, <a href=\"http://schema.org/description\">schema:description</a>, <a href=\"http://www.w3.org/2000/01/rdf-schema#comment\">rdfs:comment</a>, <a href=\"http://usefulinc.com/ns/doap#description\">doap:description</a>, <a href=\"http://usefulinc.com/ns/doap#shortdesc\">doap:shortdesc</a> or <a href=\"http://www.w3.org/2004/02/skos/core#note\">skos:note</a></li>\n<li>license: declared using <a href=\"http://purl.org/dc/terms/license\">dcterms:license</a>, <a href=\"http://schema.org/licesne\">schema:license</a>, <a href=\"http://usefulinc.com/ns/doap#license\">doap:license</a> or <a href=\"http://creativecommons.org/ns#license\">cc:license</a>.</li>\n<li>version iri: declared using <a href=\"http://www.w3.org/2002/07/owl#versionIRI\">owl:versionIRI</a></li>\n<li>creator: declared using <a href=\"http://purl.org/dc/elements/1.1/creator\">dc:creator</a>, <a href=\"http://purl.org/dc/terms/creator\">dcterms:creator</a>, <a href=\"http://purl.org/pav/createdBy\">pav:createdBy</a>, <a href=\"http://purl.org/pav/authoredBy\">pav:authoredBy</a>, <a href=\"http://schema.org/creator\">schema:creator</a>, <a href=\"http://www.w3.org/ns/prov#wasAttributedTo\">prov:wasAttributedTo</a> or <a href=\"http://usefulinc.com/ns/doap#developer\">doap:developer</a></li>\n<li>namespace URI: declared using  <a href=\"http://purl.org/vocab/vann/\">vann:preferredNamespaceUri</a></li>\n</ul>\n<p>The test will pass if all ontology metadata are present. The test will fail otherwise, indicating the properties that are missing.</p>",
      "total_passed_tests": 6,
      "total_tests_run": 6
    },
    {
      "id": "https://w3id.org/foops/test/OM2",
      "principle_id": "R1",
      "category_id": "Reusable",
      "status": "ok",
      "title": "Ontology declares recommended metadata",
      "explanation": "All recommended metadata found!",
      "abbreviation": "OM2",
      "description": "<p>This test verifies if the following recommended metadata are present in the ontology metadata: </p>\n<ul>\n<li>Namespace prefix: declared using <a href=\"http://purl.org/vocab/vann/\">vann:preferredNamespacePrefix</a></li>\n<li>Version info: declared using <a href=\"http://www.w3.org/2002/07/owl#versionInfo\">owl:versionInfo</a> or <a href=\"http://schema.org/schemaVersion\">schema:schemaVersion</a></li>\n<li>Creation date: declared using <a href=\"http://purl.org/dc/terms/created\">dcterms:created</a>, <a href=\"http://schema.org/dateCreated\">schema:dateCreated</a>, <a href=\"http://usefulinc.com/ns/doap#created\">doap:created</a>, <a href=\"http://www.w3.org/ns/prov#generatedAtTime\">prov:generatedAtTime</a> or <a href=\"http://purl.org/pav/\">pav:createdOn</a></li>\n<li>Citation: declared using <a href=\"http://purl.org/dc/terms/bibliographicCitation\">dcterms:bibliographicCitation</a></li>\n<li>Contributor (optional): declared using <a href=\"http://purl.org/dc/elements/1.1/contributor\">dc:contributor</a>, <a href=\"http://purl.org/dc/terms/contributor\">dcterms:contributor</a>, schema:contributor, <a href=\"http://usefulinc.com/ns/doap#documenter\">doap:documenter</a>, <a href=\"http://usefulinc.com/ns/doap#maintainer\">doap:maintainer</a>, <a href=\"http://usefulinc.com/ns/doap#helper\">doap:helper</a>, <a href=\"http://usefulinc.com/ns/doap#translator\">doap:translator</a> or <a href=\"http://purl.org/pav/\">pav:contributedBy</a>.</li>\n</ul>\n<p>The test will pass if all the recommended metadata properties are available in the ontology metadata (using any of the vocabularies listed above). The test will also check if contributor is present, but with no penalty (as not all ontologies have a contributor).</p>",
      "total_passed_tests": 4,
      "total_tests_run": 4
    },
    {
      "id": "https://w3id.org/foops/test/OM3",
      "principle_id": "R1",
      "category_id": "Reusable",
      "status": "ok",
      "title": "Ontology declares detailed metadata",
      "explanation": "All optional metadata found!",
      "abbreviation": "OM3",
      "description": "<p>This test verifies if the ontology includes the following detailed metadata:</p>\n<ul>\n<li>Digital Object Identifier (DOI): declared using  <a href=\"http://purl.org/ontology/bibo/doi\">bibo:doi</a>, <a href=\"https://schema.org/identifier\">schema:identifier</a> (if a doi is provided) or <a href=\"http://purl.org/dc/terms/identifier\">dcterms:identifier</a> (if a doi is provided)</li>\n<li>publisher: declared using <a href=\"http://purl.org/dc/elements/1.1/publisher\">dc:publisher</a>, <a href=\"http://purl.org/dc/terms/publisher\">dcterms:publisher</a> or <a href=\"https://schema.org/publisher\">schema:publisher</a></li>\n<li>logo: declared using <a href=\"http://xmlns.com/foaf/0.1/logo\">foaf:logo</a> or <a href=\"https://schema.org/logo\">schema:logo</a></li>\n<li>status: declared using <a href=\"http://purl.org/ontology/bibo/status\">bibo:status</a> or <a href=\"https://w3id.org/mod#status\">mod:status</a></li>\n<li>source: declared using <a href=\"http://purl.org/dc/terms/source\">dcterms:source</a> or <a href=\"http://www.w3.org/ns/prov#hadOriginalSource\">prov:hadOriginalSource</a></li>\n<li>issued date: declared using <a href=\"http://purl.org/dc/terms/issued\">dcterms:issued</a></li>\n<li>previous version (optional): declared using  <a href=\"http://purl.org/dc/elements/1.1/replaces\">dc:replaces</a>, <a href=\"http://purl.org/dc/terms/replaces\">dcterms:replaces</a>, <a href=\"http://www.w3.org/ns/prov#wasRevisionOf\">prov:wasRevisionOf</a>, <a href=\"http://www.w3.org/2002/07/owl#priorVersion\">owl:priorVersion</a> or <a href=\"http://purl.org/pav/previousVersion\">pav:previousVersion</a></li>\n<li>backward compatibility (optional): declared using <a href=\"http://www.w3.org/2002/07/owl#backwardCompatibleWith\">owl:backwardCompatibleWith</a></li>\n<li>modified date (optional): declared using <a href=\"http://purl.org/dc/terms/modified\">dcterms:modified</a> or <a href=\"https://schema.org/dateModified\">schema:dateModified</a></li>\n</ul>\n<p>The test will pass if all the detailed metadata properties are available in the ontology metadata (using any of the vocabularies listed above). The test will also check if previosu version, backward compatibility and modified date are present, but with no penalty (as not all ontologies have a previous version). </p>",
      "total_passed_tests": 6,
      "total_tests_run": 6
    },
    {
      "id": "https://w3id.org/foops/test/OM4.1",
      "principle_id": "R1.1",
      "category_id": "Reusable",
      "status": "ok",
      "title": "Ontology has a license available",
      "explanation": "A license was found https://creativecommons.org/licenses/by/4.0/",
      "abbreviation": "OM4_1",
      "description": "<p>This test verifies if a license (or rights) are associated with the ontology.\nThe test will pass if a license is declared using any of the following properties: <a href=\"http://purl.org/dc/terms/license\">dcterms:license</a>, <a href=\"https://schema.org/license\">schema:license</a>, <a href=\"http://usefulinc.com/ns/doap#license\">doap:license</a> or <a href=\"http://creativecommons.org/ns#license\">cc:license</a>.</p>\n<p>If a license is not found, but rights are declared (using <a href=\"http://purl.org/dc/elements/1.1/rights\">dc:rights</a>, <a href=\"http://purl.org/dc/terms/rights\">dcterms:rights</a> or <a href=\"http://purl.org/dc/terms/accessRights\">dcterms:accessRights</a>), the test will pass as well.</p>\n<p>Otherwise, the test will fail (i.e., no license or rights are declared).</p>",
      "total_passed_tests": 1,
      "total_tests_run": 1
    },
    {
      "id": "https://w3id.org/foops/test/OM4.2",
      "principle_id": "R1.1",
      "category_id": "Reusable",
      "status": "ok",
      "title": "Ontology license is resolvable",
      "explanation": "License could be resolved",
      "abbreviation": "OM4_2",
      "description": "<p>This test verifies if the ontology license is resolvable. The test will pass if the license available in the ontology metadata resolves to a resource. The test will fail if no license is declared (OM4.1), if the license is not a URI/URL, or if the response when requesting is 404 or an error. </p>",
      "total_passed_tests": 1,
      "total_tests_run": 1
    },
    {
      "id": "https://w3id.org/foops/test/OM5.1",
      "principle_id": "R1.2",
      "category_id": "Reusable",
      "status": "ok",
      "title": "Ontology declares basic provenance metadata",
      "explanation": "All basic provenance metadata found!",
      "abbreviation": "OM5_1",
      "description": "<p>This check verifies if basic provenance metadata is available for the ontology:  </p>\n<ul>\n<li>creator: declared using <a href=\"http://purl.org/dc/elements/1.1/creator\">dc:creator</a>, <a href=\"http://purl.org/dc/terms/creator\">dcterms:creator</a>, <a href=\"http://purl.org/pav/createdBy\">pav:createdBy</a>, <a href=\"http://purl.org/pav/authoredBy\">pav:authoredBy</a>, <a href=\"https://schema.org/creator\">schema:creator</a> or <a href=\"http://usefulinc.com/ns/doap#developer\">doap:developer</a></li>\n<li>creation date: declared using <a href=\"http://purl.org/dc/terms/created\">dcterms:created</a>, <a href=\"https://schema.org/dateCreated\">schema:dateCreated</a>, <a href=\"http://usefulinc.com/ns/doap#created\">doap:created</a>, <a href=\"http://www.w3.org/ns/prov#generatedAtTime\">prov:generatedAtTime</a> or <a href=\"http://purl.org/pav/createdOn\">pav:createdOn</a></li>\n<li>contributor (optional): declared using <a href=\"http://purl.org/dc/elements/1.1/contributor\">dc:contributor</a>, <a href=\"http://purl.org/dc/terms/contributor\">dcterms:contributor</a>, <a href=\"https://schema.org/contributor\">schema:contributor</a>, <a href=\"http://usefulinc.com/ns/doap#documenter\">doap:documenter</a>, <a href=\"http://usefulinc.com/ns/doap#maintainer\">doap:maintainer</a>, <a href=\"http://usefulinc.com/ns/doap#helper\">doap:helper</a>, <a href=\"http://usefulinc.com/ns/doap#translator\">doap:translator</a> or <a href=\"http://purl.org/pav/contributedBy\">pav:contributedBy</a>.</li>\n<li>previous version (optional): declared using  <a href=\"http://purl.org/dc/elements/1.1/replaces\">dc:replaces</a>, <a href=\"http://purl.org/dc/terms/replaces\">dcterms:replaces</a>, <a href=\"http://www.w3.org/ns/prov#wasRevisionOf\">prov:wasRevisionOf</a>, <a href=\"http://www.w3.org/2002/07/owl#previousVersion\">owl:priorVersion</a>, <a href=\"http://purl.org/pav/previousVersion\">pav:previousVersion</a></li>\n</ul>\n<p>The test will pass if creator and creation date are present. The test will fail otherwise, indicating the properties that are missing.</p>",
      "total_passed_tests": 2,
      "total_tests_run": 2
    },
    {
      "id": "https://w3id.org/foops/test/OM5.2",
      "principle_id": "R1.2",
      "category_id": "Reusable",
      "status": "ok",
      "title": "Ontology declares detailed provenance metadata",
      "explanation": "All detailed provenance metadata found!",
      "abbreviation": "OM5_2",
      "description": "<p>This check verifies if detailed provenance information is available for the ontology: </p>\n<ul>\n<li>issued date: declared using <a href=\"http://purl.org/dc/terms/issued\">dcterms:issued</a>, <a href=\"http://purl.org/dc/terms/submitted\">dcterms:submitted</a> or <a href=\"https://schema.org/datePublished\">schema:datePublished</a></li>\n<li>publisher: declared using <a href=\"http://purl.org/dc/elements/1.1/publisher\">dc:publisher</a>, <a href=\"http://purl.org/dc/terms/publisher\">dcterms:publisher</a> or <a href=\"https://schema.org/publisher\">schema:publisher</a></li>\n</ul>\n<p>The test will pass if both metadata fields are present. The test will fail otherwise, indicating the properties that are missing.</p>",
      "total_passed_tests": 2,
      "total_tests_run": 2
    },
    {
      "id": "https://w3id.org/foops/test/FIND1",
      "principle_id": "F3",
      "category_id": "Findable",
      "status": "ok",
      "title": "Ontology prefix is declared",
      "explanation": "Prefix declaration found in the ontology: oso",
      "abbreviation": "FIND1",
      "description": "<p>This check verifies if an ontology prefix is declared in the ontology metadata. \nThe test will pass if a <a href=\"http://purl.org/vocab/vann/\">vann:preferredNamespacePrefix</a> is declared.\nOtherwise, the test will fail. </p>",
      "total_passed_tests": 1,
      "total_tests_run": 1
    },
    {
      "id": "https://w3id.org/foops/test/FIND2",
      "principle_id": "F4",
      "category_id": "Findable",
      "status": "ok",
      "title": "Ontology prefix is found in prefix.cc or LOV",
      "explanation": "Prefix declaration found with correct namespace (in prefix.cc)",
      "abbreviation": "FIND2",
      "description": "<p>This test verifies whether the ontology prefix is available in <a href=\"(https://prefix.cc/)\">prefix.cc</a> or the <a href=\"(https://lov.linkeddata.es/)\">Linked Open Vocabularies (LOV)</a> registries. \nThe test will pass if: </p>\n<ol>\n<li>there is a prefix declared in the assessed ontology, </li>\n<li>the prefix is found in <a href=\"https://lov.linkeddata.es/\">LOV</a> or <a href=\"https://prefix.cc/\">prefix.cc</a> </li>\n<li>if found in <a href=\"https://lov.linkeddata.es/\">LOV</a> or <a href=\"https://prefix.cc/\">prefix.cc</a> , the namespace URI associated with the prefix is the same as the assessed ontology URI (or preferred namespace URI)</li>\n</ol>\n<p>Otherwise, the test will fail. </p>",
      "total_passed_tests": 2,
      "total_tests_run": 2
    },
    {
      "id": "https://w3id.org/foops/test/FIND3",
      "principle_id": "F4",
      "category_id": "Findable",
      "status": "ok",
      "title": "Ontology found in community registry",
      "explanation": "Otology is included in a data catalog.",
      "abbreviation": "FIND3",
      "description": "<p>This test verifies if the ontology can be found in a public registry like the Linked Open Vocabularies (LOV) public registry.\nThe test will pass if the assessed ontology URI is found in the list of vocabularies returned by LOV.\nAlternatively, if there is a <a href=\"https://schema.org/includedInDataCatalog\">schema:includedInDataCatalog</a> annotation, the test will pass.\nThe test will fail otherwise.   </p>",
      "total_passed_tests": 1,
      "total_tests_run": 1
    },
    {
      "id": "https://w3id.org/foops/test/FIND_3_BIS",
      "principle_id": "A2",
      "category_id": "Accessible",
      "status": "ok",
      "title": "Ontology metadata are accessible, even when the ontology is not",
      "explanation": "Otology is included in a data catalog.",
      "abbreviation": "FIND_3_BIS",
      "description": "<p>Metadata are accessible even when the ontology is no longer available. Since the metadata is usually included in the ontology, this test verifies if the ontology can be found in the <a href=\"https://lov.linkeddata.es\">Linked Open Vocabularies (LOV) public registry</a>.\nThe test will pass if the assessed ontology/vocabulary URI is found in the LOV list of vocabularies.\nAlternatively, if there is a <a href=\"https://schema.org/includedInDataCatalog\">schema:includedInDataCatalog</a> annotation, the test will pass.\nThe test will fail otherwise. </p>",
      "total_passed_tests": 1,
      "total_tests_run": 1
    },
    {
      "id": "https://w3id.org/foops/test/HTTP1",
      "principle_id": "A1.1",
      "category_id": "Accessible",
      "status": "ok",
      "title": "Ontology uses an open protocol",
      "explanation": "The ontology uses an open protocol",
      "abbreviation": "HTTP1",
      "description": "<p>This check verifies if the ontology uses an open protocol (HTTP or HTTPS). The test will pass if the ontology URI starts with http or https. It will fail otherwise.</p>",
      "total_passed_tests": 1,
      "total_tests_run": 1
    },
    {
      "id": "https://w3id.org/foops/test/VOC1",
      "principle_id": "I2",
      "category_id": "Interoperable",
      "status": "ok",
      "title": "Ontology reuses existing vocabularies for metadata annotations",
      "explanation": "Ontology reuses existing vocabularies for declaring metadata. ",
      "abbreviation": "VOC1",
      "description": "<p>This test verifies if the ontology reuses other vocabularies for declaring metadata terms (see tests OM1... OM5).\nThe test will pass if metadata annotations using properties from any of the following vocabularies are used:</p>\n<ul>\n<li><a href=\"http://purl.org/dc/elements/1.1/\">Dublin Core</a> (dc, dcterms)</li>\n<li><a href=\"https://schema.org/\">Schema.org</a> (schema)</li>\n<li><a href=\"http://purl.org/vocab/vann/\">Vocabulary for annotating vocabulary descriptions</a> (vann)</li>\n<li><a href=\"http://www.w3.org/ns/prov#\">W3C Provenance standard</a> (prov)</li>\n<li><a href=\"http://purl.org/ontology/bibo/\">Bibliographic Ontology</a> (bibo)</li>\n<li><a href=\"http://purl.org/pav/\">Provenance, Authoring and Versioning</a> (pav)</li>\n<li><a href=\"http://xmlns.com/foaf/0.1/\">Firend of a friend</a> (foaf)</li>\n<li><a href=\"http://usefulinc.com/ns/doap#\">Description of a project</a> (doap)</li>\n<li><a href=\"https://w3id.org/mod#\">Metadata vocabulary for ontology descriptions</a> (mod)</li>\n<li><a href=\"http://www.w3.org/2002/07/owl#\">Web Ontology Language</a> (owl)</li>\n<li><a href=\"http://www.w3.org/2000/01/rdf-schema#\">Resource description framework schema</a> (rdfs)</li>\n</ul>\n<p>The test will also return the vocabularies that were found. If none are found, the test will fail.</p>",
      "total_passed_tests": 1,
      "total_tests_run": 1,
      "reference_resources": [
        "http://purl.org/dc/terms/",
        "http://purl.org/pav/",
        "http://purl.org/vocab/vann/",
        "http://www.w3.org/2000/01/rdf-schema#",
        "http://www.w3.org/2002/07/owl#",
        "http://www.w3.org/ns/prov#",
        "http://xmlns.com/foaf/0.1/",
        "https://w3id.org/mod#"
      ]
    },
    {
      "id": "https://w3id.org/foops/test/VOC2",
      "principle_id": "I2",
      "category_id": "Interoperable",
      "status": "ok",
      "title": "Ontology imports or reuses well established vocabularies",
      "explanation": "The ontology imports the following vocabularies: . Foundational ontologies extended. Nicely done!",
      "abbreviation": "VOC2",
      "description": "<p>This test verifies if the ontology imports/extends other vocabularies (besides RDF, OWL and RDFS).\nThe test will pass if other vocabularies are imported (<a href=\"http://www.w3.org/2002/07/owl#imports\">owl:imports</a>), or if classes, properties or data properties \noutside the ontology URI or namespace URI are used.\nThe test wil fail if no terms are reused.</p>",
      "total_passed_tests": 1,
      "total_tests_run": 1,
      "reference_resources": [
        "http://www.w3.org/2003/01/geo/wgs84_pos",
        "http://www.w3.org/2004/02/skos/core",
        "http://www.w3.org/ns/prov-o",
        "http://xmlns.com/foaf/0.1/"
      ]
    },
    {
      "id": "https://w3id.org/foops/test/VOC3",
      "principle_id": "R1",
      "category_id": "Reusable",
      "status": "ok",
      "title": "Ontology documentation: all terms have labels",
      "explanation": "Labels found for all ontology terms (100 terms found)",
      "abbreviation": "VOC3",
      "description": "<p>This test verifies the extent to which all ontology terms have labels.\nThe test will pass if all classes, properties and data properties have either an <a href=\"http://www.w3.org/2000/01/rdf-schema#label\">rdfs:label</a> or <a href=\"http://www.w3.org/2004/02/skos/core#prefLabel\">skos:prefLabel</a>.\nFor skos vocabularies, only the skos:Concepts are assessed.\nOtherwise, the test will fail, indicating the level of completeness found (i.e., percentage of documented terms) </p>",
      "total_passed_tests": 100,
      "total_tests_run": 100
    },
    {
      "id": "https://w3id.org/foops/test/VOC4",
      "principle_id": "R1",
      "category_id": "Reusable",
      "status": "ok",
      "title": "Ontology documentation: all terms have definitions",
      "explanation": "Descriptions found for all ontology terms (100 terms found)",
      "abbreviation": "VOC4",
      "description": "<p>This check verifies whether all ontology terms have descriptions. \nThe test will pass if all classes, properties and data properties have at least one <a href=\"http://www.w3.org/2000/01/rdf-schema#comment\">rdfs:comment</a>, <a href=\"http://www.w3.org/2004/02/skos/core#definition\">skos:definition</a> or <a href=\"http://purl.obolibrary.org/obo/IAO_0000118\">obo:IAO_0000118</a> annotation.\nFor skos vocabularies, only the skos:Concepts are assessed.</p>\n<p>The test will fail otherwise, showing the level of completeness obtained (i.e. the percentage of documented terms).</p>",
      "total_passed_tests": 100,
      "total_tests_run": 100
    },
    {
      "id": "https://w3id.org/foops/test/VER1",
      "principle_id": "F1",
      "category_id": "Findable",
      "status": "ok",
      "title": "A version IRI is declared in the ontology metadata",
      "explanation": "Version IRI defined, IRI is different from ontology URI. Version info found (1.2.3 – ευθυγράμμιση του προτιμώμενου προθέματος χώρου ονομάτων (vann:preferredNamespacePrefix) σε «oso», όπως είναι καταχωρισμένο στα LOV και prefix.cc).",
      "abbreviation": "VER1",
      "description": "<p>This test verifies whether there is an id for this ontology version, and whether the id is unique (i.e., different from the ontology URI). The test will pass if: </p>\n<ol>\n<li>The ontology has a versionIRI (<a href=\"http://www.w3.org/2002/07/owl#versionIRI\">owl:versionIRI</a>) and </li>\n<li>The versionIRI used is different from the ontology URI.</li>\n</ol>\n<p>Otherwise the test will fail. The test will also verify whether version information is present (through <a href=\"http://www.w3.org/2002/07/owl#versionInfo\">owl:versionInfo</a>), but this is optional.</p>",
      "total_passed_tests": 2,
      "total_tests_run": 2
    },
    {
      "id": "https://w3id.org/foops/test/VER2",
      "principle_id": "F1",
      "category_id": "Findable",
      "status": "ok",
      "title": "Ontology version IRI resolves",
      "explanation": "Version IRI resolves",
      "abbreviation": "VER2",
      "description": "<p>This test verifies if the version IRI resolves. The test will pass if there is a version IRI for the ontology/vocabulary (detected using <a href=\"http://www.w3.org/2002/07/owl#versionIRI\">owl:versionIRI</a> in the ontology metadata) and whether doing a request to said IRI returns a resource. \nThe test will fail if the resource is not found (404 response) or returns an error.</p>",
      "total_passed_tests": 1,
      "total_tests_run": 1
    },
    {
      "id": "https://w3id.org/foops/test/URI2",
      "principle_id": "F1",
      "category_id": "Findable",
      "status": "ok",
      "title": "Consistent ontology IDs are employed",
      "explanation": "Ontology URI is equal to ontology id",
      "abbreviation": "URI2",
      "description": "<p>This check verifies if the ontology URI is equal to the ontology ID. The test passes if the ontology URI used to load the ontology document is the same as the ontology id found in the document itself. Otherwise the test will fail.</p>",
      "total_passed_tests": 1,
      "total_tests_run": 1
    }
  ]
}
```