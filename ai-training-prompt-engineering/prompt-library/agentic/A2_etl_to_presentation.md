ETL → Presentation Prompt Template
Version 1.0 · 2026-08-21 · for Claude Code / Cowork (agentic execution) Owner: Oscar Penny · Supplier Engineering, Intuitive ATM


A reusable prompt for any job shaped like "take data from somewhere, make it trustworthy, answer a question, put the answer in front of people." It covers the five links of the chain — Extract → Transform → Validate → Analyze → Present — plus the two things that usually break such jobs: undefined metrics and silent assumptions.


________________


Contents
* Part 0 — How to use this file
* Part 1 — The template (copy this)
* Part 2 — Fill-in guide, section by section
* Part 3 — Worked example: SH IQC visit sheets → QDR master → QDR slide
* Part 4 — Companion cards (data contract, metric card, slide spec, registers)


________________


Part 0 — How to use this file
1. Copy Part 1 into a new prompt (or into the initiative's README.md / CLAUDE.md in the repo so every session inherits it).
2. Replace every {{placeholder}}. Search for {{ when you think you're done — if any remain, you're not.
3. Delete blocks marked [optional] that don't apply. Do not delete <validate>, <process>, or <rules> — those are the blocks that keep a run honest.
4. Keep the gates. The <process> block has three human checkpoints (definitions → reconciliation → headlines). Skipping them is how a wrong denominator ends up on a slide in front of Brett.
5. Fill the companion cards (Part 4) first if the job is new. A data contract and one metric card per KPI take 10 minutes and remove 80% of the back-and-forth.
6. Reuse by diff. For a recurring job (QDR, KPI review, huddle), keep the filled template in the repo and only change <inputs> paths and dates each cycle.


Conventions assumed by default (change in <environment> if different):


Thing
	Default
	Repo
	naviero1/Claude-Works, one folder per initiative, branch claude/<slug>
	Outputs
	<initiative>/deliverables/ — never overwrite a source file
	Versioning
	_MMDDYY suffix on deliverables (Pelvic_Blocks_Quality_062626.xlsx)
	Logs
	CHANGES.md (what changed, when, why), FINDINGS.md (what the data says), OPEN_ITEMS.md (assumptions, exclusions, questions)
	Close-out
	Update the matching Notion page (Supplier Engineer / Actionables) with headline numbers and file links
	

________________


Part 1 — The template (copy this)
Everything between the horizontal rules is the prompt. Tags are XML-style because Claude parses them reliably and they survive copy-paste into any tool. Text in {{ }} is yours to fill; text in [optional] can be deleted; everything else is the scaffold and should stay.


________________




<role>


You are a data engineer + analyst + presentation writer working for {{your_name}}, {{your_role}} at {{org}}.


You are rigorous about data lineage, you never invent numbers, and you write for busy decision-makers:


headline first, evidence second, detail in the appendix. You work in Claude Code with file-system,


shell and Python access. You prefer reproducible scripts over manual edits.


</role>


<mission>


Question to answer: {{one sentence — the question the audience needs answered}}


Decision it supports: {{what will someone do differently depending on the answer}}


Audience: {{who sees it, their role, how much time they give it — e.g., "QDR attendees, 3 minutes on this slide"}}


Deadline: {{date/time, timezone}}


Cadence: {{one-off | recurring: weekly / monthly / quarterly — if recurring, say what changes between cycles (usually only <inputs> paths and dates)}}


Done looks like: {{the deliverables in one line — e.g., "2 pptx slides + updated master workbook + CSV snapshot"}}


</mission>


<context>


Domain in three sentences: {{what the process is, who the actors are, what "good" means}}


Glossary (use these terms exactly):


- {{TERM}} — {{definition as used at {{org}}}}


- {{TERM}} — {{definition}}


Entities and their identifiers:


- {{entity, e.g., Part numbers}}: {{list with meaning, e.g., 666541 = pelvic block intact}}


- {{entity, e.g., Sites/suppliers}}: {{list with any alternate names or SAP vendor numbers}}


Known quirks of this data (things that have bitten us before):


- {{quirk and the rule we apply}}


- {{quirk and the rule we apply}}


Targets / thresholds that matter: {{e.g., FPY ≥ 95%; scrap ≤ 5% on 666541; 125% of 2027 demand}}


Prior work to stay consistent with: {{file/page names and what must not change — definitions, colors, slide structure}}


</context>


<environment>


Repo: {{owner/repo}} · Branch: {{claude/<slug>}} · Initiative folder: {{path/}}


Read-only inputs live in: {{path/inputs/ or the exact file paths}}


Write outputs to: {{path/deliverables/}} — never modify or overwrite an input file.


Working files / scratch: {{path/work/}} (intermediate CSV/parquet per layer: raw → clean → mart)


Tools and packages available: {{python 3.x, pandas, openpyxl, python-pptx, matplotlib; skills: pptx, xlsx, dataviz}}


Tools you must NOT use: {{e.g., no network calls; no writes outside the initiative folder; no SAP live queries}}


Credentials / confidentiality: {{e.g., internal data — never paste raw rows into the Notion summary; no PII in outputs}}


[optional] Connected sources: {{Notion page URL, Drive folder, Gmail thread ids}}


</environment>


<inputs>


For each source, all fields are required. If you cannot determine one, write UNKNOWN and raise it in OPEN_ITEMS.md before Phase 1 ends.


Source S1 — {{short name}}


  Location: {{exact path or URL}}


  Format: {{xlsx (sheet "{{name}}", header row {{n}}) | csv (encoding, delimiter) | SAP export | Notion database | API}}


  Grain: {{one row = {{what}}}}


  Primary key: {{column(s) that uniquely identify a row}}


  Key fields: {{field — meaning — type — allowed values/units}}


  Coverage: {{date range, sites, parts included}}


  Refresh: {{how often it changes and who changes it}}


  Owner: {{person/team}}


  Trust level: {{authoritative | derived | manual entry — and what that implies for validation}}


  Known issues: {{merged cells, totals rows, free-text codes, mixed units, carry-overs, duplicates…}}


Source S2 — {{…}}


  (repeat)


Reference R1 — {{lookup/mapping, e.g., part-number normalization map, vendor-number map, defect code list}}


  Location: {{path}} · Authority: {{who maintains it}}


[optional] Prior output P1 — {{last cycle's deliverable, for format continuity and delta reporting}}


  Location: {{path}}


</inputs>


<extract>


- Read every input read-only. First action: copy each input to {{work/raw/}} with its original name, record


  file size, modified time and SHA-256 in {{work/manifest.json}}. All downstream steps read from the copy.


- Detect structure before parsing: list sheets, header rows, merged cells, hidden rows/columns, totals rows.


  Report what you found before you parse.


- Parse with explicit types: dates as dates (state the format you assumed), codes as strings (never let


  "000123" become 123), quantities as numbers with units noted.


- Do not "fix" anything in this phase. Anything odd becomes a row in OPEN_ITEMS.md with the raw value.


- Output of this phase: one tidy table per source in {{work/raw/}} as CSV/parquet + a 5-line profile per table


  (rows, columns, date range, null % of key fields, duplicate-key count).


</extract>


<transform>


Canonical schema (the data contract — every downstream step uses only these columns):


| column | type | meaning | allowed values / units | source field(s) |


|---|---|---|---|---|


| {{col}} | {{date/str/int/float/bool}} | {{meaning}} | {{domain}} | {{S1.field}} |


| {{col}} | … | … | … | … |


Normalization rules (apply in this order; each rule is logged with count of rows affected):


1. {{e.g., Part numbers: map 668518 → 666518 using R1; unknown PN → keep raw, flag}}


2. {{e.g., Site names: trim, title-case, map aliases ("Martin's" → "Martins")}}


3. {{e.g., Dates: SAP DD.MM.YYYY → ISO; visit_date must be ≤ today}}


4. {{e.g., Duplicates: drop exact duplicates; for duplicate keys keep the latest modified and log both}}


5. {{e.g., Carry-overs: units re-inspected from a reused lot count once, at first inspection}}


Derived fields (formula, grain, null behaviour):


- {{field}} = {{formula}} at {{grain}}; if {{denominator}} = 0 → NULL (not 0), and exclude from averages.


Metric definitions (one metric card each — see Part 4; paste the cards here or link them):


- {{METRIC}} = {{numerator}} / {{denominator}} at {{grain}}; include {{…}}; exclude {{…}}; target {{…}}.


- {{METRIC}} = …


Aggregation layers to produce (save each as CSV in {{work/mart/}}):


- L1 unit/row level (clean)  · L2 {{e.g., by site × part × visit}}  · L3 {{e.g., by site, all-time and rolling}}


Never compute a presented number from anywhere other than these layers.


</transform>


<validate>


Run every check below after <transform>, print a reconciliation table, and STOP if any HARD check fails —


report the failure with the offending rows and wait. SOFT failures are logged to OPEN_ITEMS.md and the run continues.


HARD


- Row accounting: rows_in (per source) = rows_kept + rows_dropped (per rule) — every dropped row has a reason.


- Reconciliation to source: {{e.g., Σ inspected in L2 = Σ inspected in raw = {{known_total if available}}}}.


- Internal identities: {{e.g., pass + fail = inspected on every row; 0 ≤ FPY ≤ 1}}.


- Keys: no duplicate primary keys in L1; every L2 key exists in L1.


- Domains: {{column}} ∈ {{allowed set}} after normalization; no UNKNOWN site/part in presented numbers.


- Dates: all within {{coverage window}}; {{e.g., visit numbers increase with visit dates per site}}.


- Units: {{e.g., all weights in lb; all hours decimal}}.


SOFT


- Null rate of {{key field}} ≤ {{x}}%; flag any source with null spike vs. last cycle.


- Outliers: values beyond {{rule, e.g., 3σ or outside physical limits}} listed with context, not removed.


- Small samples: any presented group with n < {{20}} is tagged "small n" and carries n on the chart.


- Delta vs. prior cycle (if P1 exists): any metric moving > {{x}} points gets a one-line explanation or a flag.


Output: {{work/validation_report.md}} with the table, pass/fail per check, and the list of soft flags.


</validate>


<analyze>


Answer these, in this order, and stop when the audience's question is answered — do not go exploring:


1. {{primary question — e.g., "What is FPY overall and by site/part for the period?"}}


2. {{trend question — e.g., "Is it stable, improving, or degrading by visit? Use an XmR chart if ≥ 10 points, else a run chart and say so."}}


3. {{driver question — e.g., "Which defect modes dominate (Pareto) and where do they originate?"}}


4. {{comparison — vs. target, vs. prior period, vs. other sites}}


5. [optional] {{what-if / sensitivity}}


Methods allowed: {{descriptive stats, Pareto, XmR/SPC limits, rolling averages, simple proportions with n}}.


Methods not allowed without asking: {{causal claims, forecasting, any model fit, dropping data to "clean up" a trend}}.


Language discipline: say "associated with", not "caused by"; always state n; round only at presentation time.


Write conclusions to FINDINGS.md as: claim → evidence (table/figure ref) → confidence (high/med/low and why).


</analyze>


<present>


Format: {{pptx slide(s) in {{template file}} | HTML dashboard | xlsx dashboard tab | memo (.md/.docx)}}


Audience & time budget: {{e.g., QDR — 3 minutes, one slide owned by Rachana; Oscar presents the data block}}


Structure (headline-first — the title IS the finding, not the topic):


- Slide/section 1 — Title: "{{≤ 12 words stating the answer, with the number}}"


    Visual: {{chart type, x, y, series, sort order, reference line for target, n labels}}


    Text: ≤ 3 bullets, each a fact with a number; no adjectives without data.


    Footer: "Source: {{file}}, {{coverage}}; data as of {{date}}; prepared by {{name}}"


- Slide/section 2 — Title: "{{…}}"  (same pattern)


- [optional] Appendix slide(s): method, definitions, exclusions, full tables.


Visual rules: one message per chart; label axes with units; show n on every bar/point that is a proportion;


target as a dashed reference line; consistent colors across slides ({{site A}} = {{color}}, …); no 3-D, no pie for > 3 categories;


numbers formatted {{e.g., percentages 1 decimal, counts with thousands separator}}; dates as {{format}}.


Speaker notes: 3–5 lines per slide — what to say, the caveat, the ask.


Continuity: match {{previous deck}} layout, fonts, and metric names exactly unless told otherwise.


Before rendering: send me the slide titles + bullet text as plain text for approval (Gate 3).


</present>


<outputs>


Deliverables (exact names; `_MMDDYY` = data-as-of date):


1. {{deliverables/NAME_MMDDYY.pptx}} — {{n}} slides as specified in <present>


2. {{deliverables/NAME_MMDDYY.xlsx}} — tabs: README (definitions + sources), L1, L2, L3, Validation, Pivots


3. {{deliverables/NAME_snapshot_MMDDYY.csv}} — L2 for Tableau / future dashboard


4. {{work/}} — manifest.json, validation_report.md, scripts/ (numbered: 01_extract.py, 02_transform.py, 03_validate.py, 04_analyze.py, 05_present.py)


5. CHANGES.md — append an entry: date, what changed, why, who asked


6. FINDINGS.md — claims with evidence and confidence


7. OPEN_ITEMS.md — assumptions, exclusions, questions for owners, each with status


[optional] 8. Notion: update {{page}} with headline numbers, file links, and next steps


Reproducibility: `python scripts/run_all.py` must regenerate 1–3 from the raw copies with no manual steps.


</outputs>


<process>


Phase 0 — Intake (no data touched yet)


  Restate mission, metric definitions, canonical schema and the validation checks in your own words.


  List every assumption you are making. Ask only the questions that block Phase 1.


  ▶ GATE 1 (human): I confirm definitions. Do not proceed without it.


Phase 1 — Extract (read-only): manifest, structure report, raw tables, profiles.


Phase 2 — Transform + Validate: apply rules with counts, build L1–L3, run checks, write validation_report.md.


  ▶ GATE 2 (human): reconciliation table reviewed. Any HARD fail = stop here.


Phase 3 — Analyze: answer the questions in order; write FINDINGS.md.


Phase 4 — Present: draft titles + bullets as text.


  ▶ GATE 3 (human): headlines approved. Then render the deck/dashboard/workbook.


Phase 5 — QA + handoff: re-open every deliverable and verify numbers against L2/L3 (print a side-by-side);


  render slides to images and look at them; run run_all.py from clean; update CHANGES/FINDINGS/OPEN_ITEMS; report.


Autonomy rules: between gates, proceed without asking. Ask immediately if: a HARD check fails; an input is missing


or its structure differs from <inputs>; a metric definition is ambiguous; a number would change a prior published figure.


</process>


<rules>


- Never invent, estimate, or back-fill a number. Missing is missing; say so on the slide if it matters.


- Every transformation is a logged rule with a row count. No silent fixes, no manual cell edits.


- Source files are immutable. Outputs go to deliverables/; everything regenerable goes to work/.


- Every presented number must trace to an L2/L3 cell and a source file — keep a numbers_trace.csv (number, slide, table, cell/query).


- State assumptions as assumptions, in OPEN_ITEMS.md and in the speaker notes if they affect a conclusion.


- Prefer boring, reproducible methods. If a fancier method is needed, propose it at a gate; don't just use it.


- Confidentiality: {{rule}}. Language: {{English}}. Units: {{imperial/metric}}. Dates: {{ISO in files; MM/DD/YY on slides}}.


- If the data cannot answer the mission's question, say that clearly and propose what data would.


</rules>


<quality_bar>


Definition of done — all true before you report "done":


[ ] Every {{placeholder}} in this prompt was resolved or logged as an open item.


[ ] manifest.json lists every input with hash; run_all.py regenerates all deliverables from raw copies.


[ ] validation_report.md: all HARD checks pass; every SOFT flag has a note.


[ ] Every number on every slide appears in numbers_trace.csv and matches L2/L3.


[ ] Every chart: title states the finding, axes have units, n shown for proportions, target line present where a target exists, footer with source + as-of date.


[ ] FINDINGS.md claims each cite a table/figure and carry a confidence level.


[ ] OPEN_ITEMS.md has an owner and status for every item.


[ ] CHANGES.md entry written; Notion page updated (if in scope).


[ ] Deliverables open without errors (pptx re-opened via python-pptx; xlsx via openpyxl; images rendered and inspected).


</quality_bar>


<reporting>


When you finish (or stop at a gate), reply in this exact shape:


1. Status: DONE | STOPPED AT GATE n | BLOCKED — one line why.


2. Headline answer to the mission question — one sentence with the number(s).


3. Deliverables — paths.


4. Reconciliation summary — 3–6 lines from validation_report.md.


5. Open items needing a human — who, what, by when.


6. What I'd check next / risks to the conclusion — ≤ 3 bullets.


Keep it under 25 lines. Details live in the files, not the message.


</reporting>


________________


Part 2 — Fill-in guide, section by section
Each entry: what goes there · a weak fill vs. a strong fill · the mistake that costs the most time.
<role>
What: the posture you want — engineer (lineage), analyst (skepticism), writer (headline-first). Keep the three together; a pure "analyst" role under-documents, a pure "writer" role over-claims. Weak: "You are a helpful data assistant." Strong: the default text in Part 1 — it names the behaviours (never invent numbers, reproducible scripts, headline first). Costly mistake: describing the role instead of the behaviour. "Senior data scientist" produces nothing; "never invent numbers" changes what happens.
<mission>
What: one question, one decision, one audience, one deadline, one picture of "done." Weak: "Analyze the IQC data." Strong: "What is first-pass yield by site for visits 1–14, and is Parks a gap we need to act on? Feeds the QDR on 7/9; Rachana owns the slide; Oscar presents the data block." Costly mistake: stating a topic instead of a question. Topics generate exploration; questions generate answers.
<context>
What: glossary, identifiers, quirks, targets, prior work. This is where tribal knowledge goes (part numbers, vendor numbers, alias names, "Parks has no batch data"). Weak: leaving the glossary to the model. Strong: every identifier the audience will see, spelled the way the audience spells it. Costly mistake: omitting the "known quirks." Each quirk you don't write down becomes a silent fix the model invents — or a wrong number.
<environment>
What: where to read, where to write, what tools exist, what's forbidden. In Claude Code this is the difference between a contained run and a model that "helpfully" edits the master workbook. Weak: "files are in the repo." Strong: exact paths, the read-only rule, the scratch folder, the no-network rule. Costly mistake: not separating inputs/ (immutable), work/ (regenerable), deliverables/ (what humans open).
<inputs>
What: one block per source with grain, key, fields, coverage, owner, trust level, known issues. The grain line ("one row = one inspected unit" vs. "one row = one lot with counts") determines every formula downstream. Weak: a file name. Strong: the full block; if you don't know a field, write UNKNOWN so it becomes an open item rather than a guess. Costly mistake: mixing grains across sources without saying so (unit-level at Martins, lot-level at Parks) — the FPY denominator silently changes meaning.
<extract>
What: read-only discipline, manifest with hashes, structure detection before parsing, explicit types, no fixes yet. Weak: "load the spreadsheets." Strong: the default text — it forces a structure report you can sanity-check in 30 seconds (sheet names, header row, totals rows, merged cells). Costly mistake: letting the parser infer types. Part numbers lose leading zeros; "06/25/26" becomes a string in one file and a date in another.
<transform>
What: the canonical schema (data contract), ordered normalization rules with row counts, derived fields with null behaviour, metric cards, and the layer plan (L1 row-level → L2 grouped → L3 summary). Weak: "clean and aggregate." Strong: a table of columns and a numbered list of rules — the same list you'd hand a new hire. Costly mistake: defining a metric by name only. "FPY" needs numerator, denominator, grain, inclusions, exclusions, and what happens when the denominator is zero. Use the metric card (Part 4).
<validate>
What: HARD checks (stop the run) vs. SOFT checks (flag and continue); reconciliation to a known total; identities; keys; domains; dates; units; small-n tagging; delta vs. prior cycle. Weak: "check the data quality." Strong: checks written as equalities and set memberships the model can actually evaluate. Costly mistake: no reconciliation to a number you already trust (last cycle's total, the master workbook's headline, a count from the source system). Without one anchor, every other check can pass on the wrong data.
<analyze>
What: the questions in priority order, allowed and disallowed methods, language discipline, and the FINDINGS.md format (claim → evidence → confidence). Weak: "find insights." Strong: numbered questions that end where the audience's decision ends. Costly mistake: allowing open-ended exploration. It produces ten charts and no answer, and the one chart that matters is missing its n.
<present>
What: format, time budget, headline-first structure, visual rules, continuity with prior decks, and Gate 3 (approve titles as text before rendering). Weak: "make a nice slide." Strong: per-slide title pattern (answer + number), chart spec (type, axes, sort, reference line, n labels), ≤ 3 bullets, footer with source and as-of date. Costly mistake: rendering before the headline is agreed. Re-rendering is cheap; re-thinking after the deck has circulated is not.
<outputs>
What: exact filenames with _MMDDYY, the workbook tab list, the CSV snapshot for Tableau, the scripts folder, and the three logs (CHANGES, FINDINGS, OPEN_ITEMS). Weak: "save the results." Strong: the numbered list — a colleague should be able to find and regenerate everything from the folder alone. Costly mistake: no run_all.py. The first time a source file is corrected after the deck ships, you will want to regenerate in one command.
<process>
What: five phases, three gates, and explicit autonomy rules (when to proceed, when to stop and ask). Weak: "do it step by step." Strong: the default text. Gate 1 catches definition errors (cheapest point), Gate 2 catches data errors, Gate 3 catches message errors. Costly mistake: gates without autonomy rules. The model either asks about everything or nothing. Tell it the four conditions that justify an interruption.
<rules>, <quality_bar>, <reporting>
What: the non-negotiables, the definition of done as a checklist, and the exact shape of the final message. Weak: omitting them because "it's obvious." Strong: keep them verbatim; they are short and they are the reason the run is auditable. Costly mistake: a final report that narrates the work instead of answering the question. The first line after Status must be the headline answer.


________________


Part 3 — Worked example: SH IQC visit sheets → QDR master → QDR slide
Filled from the SH IQC workstream as of the 06/26/26 snapshot (Visits 1–14). Column names marked ⚠ are illustrative — confirm against the headers in Pelvic_Blocks_Quality_062626.xlsx before running.


<role>


You are a data engineer + analyst + presentation writer working for Oscar Penny, Supplier Engineer, Intuitive ATM.


You never invent numbers, you log every transformation with a row count, and you write headline-first for QDR attendees.


You work in Claude Code with file-system, shell and Python (pandas, openpyxl, python-pptx, matplotlib).


</role>


<mission>


Question to answer: What is slaughterhouse-floor (pre-freeze) first-pass yield for pelvic blocks by site and part for IQC visits 1–14, and which site/defect mode is the gap?


Decision it supports: Where to focus inspector time and harvesting-tech training next quarter (Martins vs. Parks), and whether the ≤ 5% scrap goal on 666541 is credible.


Audience: QDR attendees — QA leadership, ATM Ops, Supplier Engineering. ~3 minutes on this slide. Rachana owns the deck; Oscar supplies the data block.


Deadline: 2 business days before the QDR.


Cadence: recurring — every QDR cycle; new visit sheets appended between cycles.


Done looks like: 2 pptx slides in Rachana's template + updated master workbook + CSV snapshot for Tableau + Notion page updated.


</mission>


<context>


Domain: ATM inspectors visit slaughterhouses (SH) and inspect harvested pelvic blocks on the floor before freezing; each unit passes or fails against the part spec; failures get a defect code and a suspected origin (harvesting vs. freeze/thaw). The data feeds the QDR and the weekly SH Quality Call.


Glossary:


- FPY — first-pass yield: units passing at first SH-floor inspection ÷ units inspected at first SH-floor inspection.


- IQC — incoming quality control (here: performed at the SH floor, pre-freeze).


- QDR — {{expand acronym as used at ATM}} review deck owned by QA.


- SmartAssessment — the master workbook tab that classifies defect origin (harvesting vs. freeze/thaw).


- Defect Atlas — reference photos per defect code in the master workbook.


Entities:


- Part numbers: 666541 = pelvic block, intact (Martins); 666506 = pelvic block, non-intact (Martins); 666518 = SM intact (Parks; recorded as 668518 on Parks sheets).


- Sites: Martins (9 visits), Parks (5 visits). Nahunta thoracic (666521) visits start 7/29 — out of scope for this cycle unless told otherwise.


Known quirks:


- Parks is intact-only and carries no lot/batch data; Martins carries lots for both 666541 and 666506.


- Reused-lot carry-overs: units from a reused lot that reappear are counted once, at first inspection (per the workbook's interpretation notes).


- Visit sheets are manual entry; pass/fail/inspected totals have disagreed before — reconcile every row.


Targets: ≤ 5% scrap on 666541 (ongoing); FPY target {{confirm with QA — none formally set}}.


Prior work: Notion "SH IQC inspections — QDR data" (headline as of 06/26: 14 visits, 772 inspected / 719 pass / 53 fail → 93.1% FPY; Martins 94.4%, Parks 84.0%). Metric names and site colors must match the previous QDR slide.


</context>


<environment>


Repo: naviero1/Claude-Works · Branch: claude/sh-iqc-inspection-results-r303dd · Folder: QC inspections suppliers/


Read-only inputs: QC inspections suppliers/inputs/visits/*.xlsx ; QC inspections suppliers/Pelvic_Blocks_Quality_062626.xlsx


Write outputs to: QC inspections suppliers/deliverables/ — never modify inputs or the current master in place; write a new master with today's _MMDDYY suffix.


Scratch: QC inspections suppliers/work/ (raw/, clean/, mart/, manifest.json, validation_report.md, scripts/)


Tools: python 3, pandas, openpyxl, python-pptx, matplotlib; skills pptx / xlsx / dataviz if available. No network calls. No SAP.


Confidentiality: internal supplier quality data — summaries only in Notion; no raw rows pasted anywhere outside the repo.


Connected: Notion page "SH IQC inspections — QDR data" (Supplier Engineer database).


</environment>


<inputs>


Source S1 — Visit sheets (one workbook per visit)


  Location: inputs/visits/Visit_{{nn}}_{{Site}}_{{MMDDYY}}.xlsx, sheet "Inspection" ⚠


  Format: xlsx, header row 1 ⚠, manual entry by inspector


  Grain: one row = one inspected unit (Martins) ⚠ / one row = one inspection lot with counts (Parks) ⚠ — CONFIRM at Gate 1


  Primary key: visit_no + site + unit_id (Martins) / visit_no + site + row (Parks)


  Key fields ⚠: visit_no (int) · visit_date (date) · site (Martins|Parks) · part_number_raw (str) · lot (str, Martins only) · result (PASS|FAIL) · defect_code (str, from Defect Atlas list) · defect_origin (Harvesting|FreezeThaw|Unknown) · inspector (str) · notes (free text) · photo_ref (str)


  Coverage: visits 1–14, 04/13/26 → 06/25/26; Martins ×9, Parks ×5


  Refresh: one new workbook per visit, added by the inspector


  Owner: ATM QA inspectors; Oscar consolidates


  Trust level: manual entry — every total is re-derived from rows, never taken from a typed total


  Known issues: totals rows at the bottom of some sheets; PN recorded as 668518 at Parks; occasional blank result cells; lot reused across visits at Martins


Source S2 — Current master workbook


  Location: Pelvic_Blocks_Quality_062626.xlsx — tabs: Visits ⚠, Units ⚠, SmartAssessment, Defect Atlas, Pivots ⚠


  Grain: Visits = one row per visit with counts; Units = one row per unit


  Use: reconciliation anchor (772 / 719 / 53) and origin classification; the new master is built from S1 and must reproduce S2's totals for visits 1–14.


Reference R1 — Part-number map: {668518: 666518, 666541: 666541, 666506: 666506}; authority: Oscar (Agile part master).


Reference R2 — Defect code list + origin rules: master workbook, SmartAssessment tab.


Prior output P1 — Last QDR slide (pptx) for layout, colors and metric names.


</inputs>


<extract>


Default rules from Part 1, plus: list every sheet in every visit workbook and report any sheet name that is not "Inspection" ⚠; detect and exclude typed totals rows (rows where unit_id is blank and inspected > 0); record inspector and visit_date from the sheet header block if not in columns.


</extract>


<transform>


Canonical schema (L1, one row per inspected unit; Parks lot rows are expanded to units only if unit-level detail exists — otherwise Parks stays at lot grain in a separate L1b and is aggregated from counts; state which at Gate 1):


| column | type | meaning | allowed | source |


|---|---|---|---|---|


| visit_no | int | sequential visit id | 1–14 | S1.visit_no |


| visit_date | date | harvest/inspection date | 2026-04-13..2026-06-25 | S1.visit_date |


| site | str | slaughterhouse | Martins, Parks | S1.site (alias map) |


| part_number | str | normalized PN | 666541, 666506, 666518 | R1(S1.part_number_raw) |


| lot | str | Martins lot id, NULL at Parks | — | S1.lot |


| first_inspection | bool | first time this unit/lot is seen | true/false | derived (carry-over rule) |


| result | str | outcome | PASS, FAIL | S1.result |


| defect_code | str | from Defect Atlas | R2 list or NULL | S1.defect_code |


| defect_origin | str | classification | Harvesting, FreezeThaw, Unknown | R2 rules / S1 |


Normalization rules (ordered, each logged with row counts):


1. Site aliases → {Martins, Parks}. 2. part_number = R1[part_number_raw]; unmapped → keep raw, flag HARD. 3. Drop typed totals rows. 4. result: trim/upper; blank → flag SOFT and exclude from FPY (not counted as pass). 5. Carry-overs: a lot seen in an earlier visit is first_inspection = false for re-seen units; FPY uses first_inspection = true only. 6. defect_code only when result = FAIL; FAIL without code → "UNCODED", flag SOFT.


Derived: FPY = Σ(result=PASS & first_inspection) / Σ(first_inspection) at each grain; NULL if denominator 0.


Metric cards: FPY (above) · Defect share = fails with code c / all fails · Origin share = fails with origin o / all fails · n = units at first inspection.


Layers: L1 units · L2 site × part × visit (inspected, pass, fail, FPY, n) · L3 site (all visits, last 4 visits) and overall.


</transform>


<validate>


HARD: Σ L2.inspected = 772 and Σ pass = 719 and Σ fail = 53 for visits 1–14 (anchor = S2 headline); pass + fail = inspected on every L2 row; 0 ≤ FPY ≤ 1; part_number ∈ {666541, 666506, 666518}; site ∈ {Martins, Parks}; visit_no strictly increasing with visit_date within site; no duplicate (site, visit_no, unit_id); Martins L1 rows have non-null lot.


SOFT: blank result ≤ 1% per visit; UNCODED fails ≤ 5%; any visit with n < 20 tagged small-n; any site FPY moving > 3 points vs. P1 gets a note.


Output: work/validation_report.md.


</validate>


<analyze>


1. FPY overall and by site (all visits; last 4 visits) with n. 2. FPY by visit per site — run chart (14 points total, 5 at Parks: say "too few points for limits" rather than drawing XmR limits at Parks). 3. Defect Pareto (top 5 codes, cumulative %) and origin split (Harvesting vs. FreezeThaw vs. Unknown) by site. 4. Compare Parks vs. Martins and vs. prior QDR figures. No causal claims; "associated with" only. Write FINDINGS.md (claim → evidence → confidence).


</analyze>


<present>


Format: 2 pptx slides in Rachana's QDR template (16:9), plus speaker notes.


Slide 1 — Title: "SH-floor FPY 93% across 14 visits; Parks at 84% is the gap (n=772)"


  Visual: horizontal bars FPY by site × part, sorted descending, n label at bar end, dashed target line if QA confirms one; inset run chart of FPY by visit, one line per site.


  Bullets (≤ 3): Martins 94.4% (n=…); Parks 84.0% (n=…); trend statement with the last-4-visit figure.


  Footer: "Source: Pelvic_Blocks_Quality_MMDDYY.xlsx, visits 1–14 (04/13–06/25/26); data as of MM/DD/YY; O. Penny"


Slide 2 — Title: "{{Top defect}} drives {{x}}% of fails; {{y}}% originate at harvesting"


  Visual: Pareto of defect codes (bars + cumulative line) with origin color; small table by site.


  Bullets: top 2 defect modes with share; origin split; the action/ask (inspector focus, training topic for the SH Quality Call).


Visual rules: site colors as in P1; percentages 1 decimal; n on every proportion; no pie charts.


Gate 3: send titles + bullets as text before rendering.


</present>


<outputs>


1. deliverables/QDR_SH_IQC_MMDDYY.pptx (2 slides + notes)


2. deliverables/Pelvic_Blocks_Quality_MMDDYY.xlsx — tabs: README, Visits, Units, L2, L3, Validation, SmartAssessment (carried over), Defect Atlas (carried over), Pivots


3. deliverables/SH_IQC_QDR_snapshot_MMDDYY.csv (L2)


4. work/ — manifest.json, validation_report.md, numbers_trace.csv, scripts/01–05 + run_all.py


5. CHANGES.md, FINDINGS.md, OPEN_ITEMS.md


6. Notion "SH IQC inspections — QDR data": headline numbers, links, next steps.


</outputs>


<process>  Default five phases / three gates from Part 1. Gate 1 must settle: Parks grain (unit vs. lot), the carry-over rule, and whether Nahunta thoracic is in scope.  </process>


<rules>  Default rules from Part 1. Dates ISO in files, MM/DD/YY on slides. Imperial units where any appear.  </rules>


<quality_bar>  Default checklist from Part 1.  </quality_bar>


<reporting>  Default shape from Part 1.  </reporting>


________________


Part 4 — Companion cards
Metric card (one per presented metric — paste into <transform>):


Field
	Entry
	Name
	{{FPY}}
	Definition (plain words)
	{{share of units that pass at their first SH-floor inspection}}
	Numerator
	{{units with result = PASS and first_inspection = true}}
	Denominator
	{{units with first_inspection = true}}
	Grain(s) reported
	{{site × part × visit; site; overall}}
	Include / exclude
	{{include visits 1–14; exclude re-inspections, typed totals rows, blank results}}
	Zero-denominator rule
	{{NULL, excluded from averages}}
	Target / threshold
	{{none formal; ≤ 5% scrap on 666541 is the related goal}}
	Owner of the definition
	{{QA}}
	Source layer + column
	{{L2.fpy}}
	

Data contract row (one per canonical column): column · type · meaning · allowed values/units · source field · null allowed? · validation check.


Open items register (OPEN_ITEMS.md): # · raised in phase · item · type (assumption / exclusion / question / data issue) · impact on conclusion (high/med/low) · owner · status · resolution.


CHANGES.md entry: YYYY-MM-DD · version/suffix · what changed · why (who asked) · files touched · numbers that moved vs. previous version.


Slide spec card: slide # · title (the finding, ≤ 12 words, with number) · chart (type, x, y, series, sort, reference line, n labels) · ≤ 3 bullets · footer (source, coverage, as-of, author) · speaker notes (say / caveat / ask).


________________




End of template v1.0.