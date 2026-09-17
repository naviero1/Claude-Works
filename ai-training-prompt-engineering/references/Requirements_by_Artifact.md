# Requirements by artifact: a practical prompt-writing menu

Role, context, tone, format, and acceptance checks describe what a response or artifact must contain, how it should behave, and how well it must serve its reader. Context also supplies background facts; turn the consequential facts into explicit instructions when their use matters.

Choose the requirements that resolve ambiguity in the task. A simple reply may need only a few. More requirements are useful only when they are relevant, mutually consistent, feasible, and checkable. Separate a required outcome from an optional preference, and make trade-offs explicit.

For each selected type, write: **requirement → example or boundary case → acceptance evidence**. A role title is a starting point; observable behavior makes it useful. Prompt instructions request compliance. Actual permissions and configured controls determine which actions a tool can take.

This is a teaching taxonomy organized around the course artifacts, not a formal requirements standard. It applies the writing principles summarized by the National Aeronautics and Space Administration and the International Council on Systems Engineering.

## Prompt elements are requirement types

A prompt specifies the content, behavior, and quality of a reply or artifact.

| Requirement type | Example instruction | How to check it |
|---|---|---|
| Functional behavior | What the artifact must do: filter, calculate, extract, compare, or explain. | Exercise each requested behavior. |
| Data and provenance | Allowed inputs, definitions, period, revision, and traceability. | Trace a result to the right source record. |
| Scope and exclusions | What is included, excluded, or explicitly outside the task. | Check boundary cases and excluded records. |
| Audience and use | Who will use the result and the decision or action it supports. | Have a representative reader use the output. |
| Role and working behavior | A perspective plus observable conduct; a title alone is weak guidance. | Check the requested conduct, such as stating assumptions. |
| Content and completeness | Required topics, facts, fields, decisions, and limitations. | Compare output against a coverage checklist. |
| Method and business rules | Formulas, grouping rules, denominators, precedence, and missing-data treatment. | Independently recompute or trace a worked example. |
| Structure and interface | Sections, tabs, slides, columns, controls, and navigation. | Inspect structure and exercise navigation. |
| Tone and presentation | Voice, reading level, units, number formats, and visual emphasis. | Use a concrete rubric and a representative example. |
| Accessibility and usability | Readable contrast, meaningful labels, keyboard access, and understandable language. | Try the relevant reading or interaction tasks. |
| Quality and acceptance | Observable correctness, completeness, reliability, and performance criteria. | Define the test input and expected result. |
| Constraints and authority | Allowed tools, dependencies, data access, edits, approvals, and stop conditions. | Inspect actions and configured permissions where applicable. |
| Delivery and compatibility | File type, editability, offline use, destination, and supported application. | Open the delivered file in the intended environment. |
| Maintenance and reuse | Refresh procedure, source version, change notes, and reusable parameters. | Repeat the task with changed input and compare behavior. |

## Spreadsheet analysis: requirements to choose

Data requirements define which records and calculations are valid.

| Requirement type | Example instruction | How to check it |
|---|---|---|
| Row grain | State that each detail row is a month–site–supplier observation. | Confirm grouping keys before aggregation. |
| Reporting period | Use an explicit inclusive month range from Month. | Check the first and last included months. |
| Field types and units | Treat Month as a month; identify counts, percentages, hours, and currency. | Check parsing and unit labels. |
| Duplicates and summary rows | Exclude the existing TOTAL row and investigate duplicate keys. | Compare row counts and a duplicate-key report. |
| Metric definition | Define return rate as sum of Units_Returned divided by sum of Units_Shipped. | Recompute the numerator, denominator, and displayed rate. |
| Weighting and denominators | Do not infer overall on-time delivery from monthly percentages without delivery counts. | Flag the missing denominator instead of claiming an overall rate. |
| Missing and invalid values | Retain the missing Inspection_Hours value; disclose any exclusion. | Inspect missing-value counts and affected calculations. |
| Segmentation and comparison | Compare suppliers on the same selected period and sites. | Confirm equal filter scope for each comparison. |
| Rounding and number formats | Display return rates to three decimal places while retaining calculation precision. | Check displayed 0.348% against the underlying ratio. |
| Formula traceability | Use inspectable formulas or an included calculation log. | Trace one output to its input rows. |
| Structure and usability | Provide a scorecard tab and a definitions tab with meaningful headers. | Open both tabs and identify the measure without outside explanation. |
| Verification and limitations | Reconcile counts and sums; distinguish association from a causal explanation. | Compare totals and challenge unsupported explanations. |
| Delivery and portability | Deliver an editable Excel workbook (.xlsx) with no broken external references. | Open the file in the intended spreadsheet application. |

## HTML dashboards: requirements to choose

An interactive dashboard needs behavior and state requirements as well as visual requirements.

| Requirement type | Example instruction | How to check it |
|---|---|---|
| Input contract | Embed the checked supplier detail data and identify the snapshot date. | Compare record count and source identifiers. |
| Date range | Use month selectors matching the source granularity; include both endpoints. | Test a single month and the full range. |
| Category controls | Offer Supplier and Site multi-select controls; Type or Class requires a real source field. | Compare each option with actual distinct values. |
| Grouping and granularity | Allow grouping by supplier, site, or month when relevant to the decision. | Check counts and totals after changing the grouping. |
| Metric selection | Offer named measures with definitions and units. | Verify that labels, scales, and calculations all change together. |
| Filter combination | Apply selected filters consistently, with an explicit AND/OR rule. | Use a known intersection and compare included records. |
| Coordinated views | Charts, totals, and tables must represent the same selected records. | Reconcile a chart total with its underlying table. |
| Sorting and drill-down | Sort numerically and allow inspection of supporting rows. | Compare sorted order and inspect a selected group. |
| Empty, missing, and zero states | Distinguish no matching records from a valid zero; avoid division by zero. | Exercise all three cases. |
| Reset and visible state | Show active selections and restore the default state with Reset. | Change multiple controls, reset, and compare the initial view. |
| Accessibility and layout | Use labeled controls, visible focus, readable contrast, and a usable narrow layout. | Navigate by keyboard and test a smaller window. |
| Portability and dependencies | Deliver one self-contained HyperText Markup Language (.html) file with embedded data and no required network calls. | Open offline and inspect for missing assets. |
| Performance | Choose a measurable response target on the training laptop for this dataset. | Time a representative filter change; do not invent a universal target. |
| Export and reconciliation | If export is needed, export the filtered data and retain the chosen scope. | Compare exported rows with the displayed selection. |

## Presentations: requirements to choose

A presentation needs audience, narrative, visual, and delivery requirements.

| Requirement type | Example instruction | How to check it |
|---|---|---|
| Purpose and audience | Name the decision, audience knowledge, and intended action. | A reviewer can identify the decision and next step. |
| Scope and slide count | For the mock presentation, request five slides with a defined coverage list. | Count slides and map each required topic. |
| Story structure | Move from business question to evidence, implications, and next action. | Read only the titles and check the narrative. |
| Message hierarchy | Use one main message per slide; make evidence support that message. | Ask a reader what to remember first. |
| Data fidelity | Use only checked findings and preserve period, units, and limitations. | Reconcile displayed values with the workbook. |
| Chart semantics | Choose an appropriate chart, truthful axes, and clearly labeled categories. | Check that the encoding supports the claimed comparison. |
| Typography and readability | Set readable projected text and avoid dense paragraphs on teaching slides. | Inspect at presentation size and the expected viewing distance. |
| Visual consistency | Use a restrained palette, aligned margins, and consistent emphasis. | Compare consecutive slides as a set. |
| Speaker notes | Provide purpose, talking points, transitions, and exercise instructions. | Inspect notes on every relevant slide. |
| Timing and mode | Classify TEACH, DO, REFERENCE, and DIVIDER; protect 30 practice minutes. | Sum notes and rehearse the live path. |
| Reference completeness | Make self-study slides understandable without the facilitator. | Have a reader explain the example from the slide and notes. |
| Accessibility | Use readable contrast and descriptive alternatives for meaningful visuals. | Review with the target presentation application’s accessibility tools. |
| Delivery and editability | Deliver an editable PowerPoint (.pptx), retaining notes and usable charts. | Open, edit, and present the exported file. |

## Email summaries: requirements to choose

A useful summary preserves evidence, chronology, ownership, and conditions.

| Requirement type | Example instruction | How to check it |
|---|---|---|
| Source scope | Name the selected thread, relevant date range, and available attachments. | List the messages and attachments actually used. |
| Current state | Separate the latest position from earlier proposals. | Trace each changed date to the message that superseded it. |
| Decision extraction | Distinguish approved, proposed, rejected, and unresolved items. | Compare decision status with the source wording. |
| Conditional approval | Keep the cost cap and quality sign-off attached to the approval. | Reject a summary that says simply approved. |
| Actions and ownership | Extract action, explicit owner, due date, and status. | Check each field; use Not stated for missing details. |
| Date meaning | Distinguish a trial date, change date, and action due date. | Check that September 25 and October 2 are not conflated. |
| Open questions and conflicts | List unresolved freight responsibility and contradictory statements. | Locate the source question and any subsequent resolution. |
| Evidence traceability | Use message dates, senders, and supporting excerpts or available links. | Open the referenced message and verify the claim. |
| Attachments and missing input | Flag a mentioned drawing that is not available to the assistant. | Do not summarize content of an unavailable attachment. |
| Format and tone | Provide a neutral current-state brief and a separate action table. | Check that opinions are labeled and actions are easy to scan. |
| Access and tool availability | Use only mail and attachments available in the actual Copilot and Outlook setup. | Confirm retrieval scope; use the supplied-text exercise when needed. |
| Authority and delivery | Prepare any reply as a draft for human review; do not send automatically. | Inspect the draft and action record. |

## Plain-language documents: requirements to choose

Accessible language must preserve meaning, conditions, and useful detail.

| Requirement type | Example instruction | How to check it |
|---|---|---|
| Reader and purpose | Write for a reader at a fifth-grade reading level who needs to understand or do a named task. | A representative reader can state the purpose. |
| Source and factual scope | Use the supplied source and identify unsupported or missing information. | Trace factual claims to the source. |
| Concept coverage | List the ideas the reader must understand before drafting. | Compare the document with the coverage list. |
| Vocabulary | Prefer familiar words and define necessary technical terms at first use. | Review unfamiliar terms and their definitions. |
| Sentence and paragraph structure | Use short direct sentences and one main idea per paragraph. | Read aloud and inspect complex sentences. |
| Organization | Use meaningful headings and ordered steps when order matters. | Ask a reader to locate the first action and a key explanation. |
| Examples and analogies | Include a concrete everyday example and state the limit of any analogy. | Check that the analogy does not change the underlying idea. |
| Tone and respect | Use a clear adult tone without condescension or childish phrasing. | Review wording with the intended audience. |
| Accuracy and caveats | Preserve important conditions, uncertainty, exceptions, and warnings from the source. | Compare the simplified version with the original meaning. |
| Readability evidence | Use reading-level estimates as one signal, plus human comprehension checks. | Do not claim exact grade-level comprehension from a score alone. |
| Visual support and accessibility | Use a labeled diagram or example only when it improves understanding. | Ask what the visual helps the reader explain. |
| Comprehension check | Provide three questions and a short answer key grounded in the document. | Confirm the answers can be found or inferred from the text. |
| Delivery and reuse | Specify an editable document, useful headings, and reusable topic placeholders. | Open the output and adapt one topic without losing the structure. |

## Reusable prompt skeleton

**Purpose and audience:** Help [reader] make [decision] or complete [task].

**Sources and scope:** Use [source/version/period]. Include [scope]; exclude [items].

**Selected artifact requirements:** [Content, behavior, structure, style, method, and delivery requirements that matter for this task.]

**Acceptance evidence:** Check [specific result] against [source, calculation, or observable test].

**Missing information and boundaries:** If [gap/conflict], [state it, ask, or stop]. Actions requiring review: [actions].

## Excel analysis and charts: requirements to choose

The assistant edits the uploaded workbook and returns it — charts must stay editable and every number traceable.

| Requirement type | Example instruction | How to check it |
|---|---|---|
| Input contract | Work on the single uploaded data-only workbook; use its detail rows and note the TOTAL row and any missing values. | Compare the file the assistant describes with the one uploaded. |
| Data preservation | Keep the original data sheet unchanged; add analysis on a new Summary sheet. | Diff the returned data sheet against the source. |
| Summary content | The Summary sheet holds a supplier comparison table: units shipped, units returned, return rate, defect rate. | Check every listed column exists with a value per supplier. |
| Metric definitions | State each metric's formula on the sheet; rates from sums, never averaged percentages; returns and defects separate. | Read the definitions and recompute one rate from the stated formula. |
| Traceable logic | Use formulas, PivotTables, or other inspectable Excel logic — no hard-coded results. | Click a summary cell and follow its formula to the data rows. |
| Native editable charts | Add a native Excel column chart (supplier comparison) and line chart (rate by month); no pasted images. | Click each chart and edit its source range or PivotTable. |
| Reporting period | State the inclusive period the analysis covers on the Summary sheet. | Compare the stated period with the data's first and last months. |
| Missing-value handling | Preserve missing values as missing; disclose them; never zero-fill. | Locate the known missing cell and its disclosure. |
| Reconciliation | Reconcile summary totals to the source before returning the file. | Compare the summary totals with the source TOTAL row. |
| Limitations note | Include one short note on what the analysis cannot claim (no causes; any absent denominators). | Read the note; challenge one unsupported claim. |
| Delivery and naming | Return an editable Excel file with the agreed name (e.g. Supplier_Data_Analyzed.xlsx). | Open the returned file in Excel and edit a cell. |
| Rounding and precision | Retain calculation precision; round only at display, stating the display precision. | Check a displayed rate against the underlying ratio. |

## Quotation extraction: requirements to choose

Step one is faithful extraction with provenance — no normalizing, ranking, or recommending yet.

| Requirement type | Example instruction | How to check it |
|---|---|---|
| Source scope | Use only the attached quotation files; name each file used. | Compare the named files with those supplied. |
| Row grain | One row per quotation on a Raw Extraction sheet. | Count rows against the number of quotations. |
| Field coverage | Capture supplier, scope, currency, quantity basis, unit price, tooling/one-time charges, freight, taxes, lead time, payment terms, validity, exclusions. | Check every field column exists for every row. |
| Verbatim fidelity | Copy values exactly as stated — original currencies, quantity bases, and units. | Compare three extracted values character-for-character with the source. |
| No early normalization | Do not convert, rank, or recommend in this step. | Scan the sheet for any converted value or judgment. |
| Gap honesty | Write "Not stated" where the quotation is silent — never infer. | Check known silent fields (e.g. a missing freight amount) read "Not stated". |
| Source citation | Cite source file and page for every extracted commercial value. | Open one citation and find the value on that page. |
| Exclusions captured | Record what each quote excludes (VAT, freight, duties) in its own field. | Compare exclusions with the source wording. |
| Missing-information column | List per quotation what a fair comparison still needs. | Check the column names the real gaps, not "none" by default. |
| Traceable structure | Keep one header row, filters on, and no merged data cells. | Sort and filter the sheet without breaking it. |
| Delivery | Deliver an editable Excel workbook with the Raw Extraction sheet named. | Open and edit the returned file. |

## Quotation comparison: requirements to choose

Step two normalizes only what has a stated basis — and refuses a winner while the basis is incomplete.

| Requirement type | Example instruction | How to check it |
|---|---|---|
| Basis continuity | Build the Normalized Comparison sheet from the Raw Extraction sheet, not from the PDFs again. | Trace one comparison cell to its extraction row. |
| Conversion discipline | Normalize quantities, units, or currencies only where the conversion rule or basis is supplied; otherwise keep the original and flag it. | Find the unconverted currency and its flag. |
| Visible originals | Keep every original extracted value visible alongside any normalized figure. | Toggle between sheets and match values. |
| Comparable-total formulas | Show the formula for each comparable total (e.g. unit price + tooling amortized over the stated quantity). | Click the total and read its formula. |
| Amortization basis | State the quantity over which one-time charges are spread. | Recompute one amortized total by hand. |
| Scope flags | Flag differences in scope, assumptions, exclusions, and commercial terms per supplier. | Check the flags against the extraction sheet's exclusions. |
| Commercial terms | Compare warranty, lead time, payment terms, and validity — not price alone. | Check the non-price terms appear for every supplier. |
| Recommendation gate | Identify no best quote until the comparison basis is complete. | Confirm no winner is named while gaps remain. |
| Blocking-gap list | List the missing information and unresolved questions that prevent a fair recommendation. | Check the list against the known gaps (conversion basis, freight, taxes). |
| Traceability | Every normalized number traces to an extracted value plus a stated rule. | Pick one number and reproduce it. |
| Delivery | Deliver the comparison in the same editable workbook as the extraction. | Open the workbook and find both sheets. |

## Research workbooks: requirements to choose

References in, one traceable spreadsheet out — provenance survives, conflicts stay visible.

| Requirement type | Example instruction | How to check it |
|---|---|---|
| Source restriction | Use only information traceable to the supplied reference files. | Spot-check three claims against their cited sources. |
| Evidence row grain | One claim, instruction, or finding per Evidence row. | Scan for rows that bundle multiple claims. |
| Evidence columns | ID, topic, claim, source file, author/organization, date, page or section, short excerpt, plain-language interpretation, caveat, relevance to the research question, confidence/status, open question. | Check every column exists and is used. |
| Excerpt fidelity | Keep supporting excerpts short and verbatim. | Compare one excerpt with the source text. |
| Interpretation separation | Keep the plain-language interpretation separate from the quoted claim. | Check the two columns are not merged or blended. |
| Caveat preservation | Carry each source's limits and conditions into the caveat column. | Compare a caveat with the source's own qualifier. |
| Conflict handling | Keep conflicting claims as separate rows and surface the conflict in the Synthesis — never silently merge. | Find the known conflict and its Synthesis entry. |
| Gap honesty | Write "Not stated" for missing dates, scales, or scopes; log open questions. | Check undated sources read "Not stated", not a guessed date. |
| No invented citations | Every source row corresponds to a supplied file; no external references appear. | Compare the Sources sheet with the supplied pack. |
| Synthesis ordering | Order findings from foundations to implications; identify agreements, conflicts, and gaps. | Read the Synthesis top to bottom against that order. |
| Sources index | Index every supplied file with type, author, date, and a one-line description. | Count index rows against the pack. |
| Usability | Add filters, freeze the header row, wrap long text. | Filter a column and scroll with the header visible. |
| Delivery | Deliver an editable Excel workbook; if the tool cannot, separate CSV tables per sheet. | Open the file (or CSVs) and edit a cell. |

## How this catalog is used (maintenance map)

This file is the shared source for every artifact that presents requirement
menus. Change it here, then rebuild; keep examples and acceptance checks
consistent everywhere it flows:

| Consumer | How it consumes this file |
|---|---|
| Prompt_Template_Creator.html | `src/build_builder.py` parses the five artifact tables into the task-family menus. |
| Prompt_Template_Configurator.xlsx | `src/build_configurator_xlsx.py` parses the same tables into the Tasks sheet. |
| Elements_of_Prompting_Field_Guide.pdf | `src/build_elements_guide.py` prints the five tables as Part 6. |
| Course deck (slides 91–96) | The reference pages carry the same menus; update them together with this file. |
| Course_Workbook tabs 1–5 | The requirement-type annotations in the WHY column name types from these tables. |

The five reusable course prompts live in `src/assets/course_prompts.json`
(builder + configurator + field guide) and, with commentary, in the workbook tabs.

## Writing principles and references

Use necessary, clear, sufficiently complete, singular, feasible, consistent, and verifiable requirements. Keep the business reason and source available. Verification asks whether the output meets the written criteria; validation asks whether it serves the actual need. These principles improve prompt clarity and evaluation without guaranteeing model compliance.

- [National Aeronautics and Space Administration: How to Write a Good Requirement](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/)
- [International Council on Systems Engineering: Guide to Writing Requirements, version 4 summary](https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf)
