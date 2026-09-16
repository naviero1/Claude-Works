# Claude Code instructions: revise the complete training package

You are revising my “From Prompts to Agents” training and its supporting artifacts. Implement the changes, inspect the outputs, and return the complete revised package. Do not stop after proposing changes.

## Start from this completed iteration

You did not participate in the latest facilitation revision. Read the attached **From_Prompts_to_Agents_Facilitated_60_Minute.pptx**, including speaker notes, before editing. Use it as the baseline instead of reverting to the original deck. Also read **From_Prompts_to_Agents_Facilitation_Plan.md** and **Requirements_by_Artifact.md**.

The baseline has 96 slides: a 70-slide main sequence containing selectively taught material, followed by 26 optional reference pages. This is a facilitated 60-minute course, not a request to present 96 slides in order. The current allocation is 30 minutes of protected application and 30 minutes across explanation, brief reference orientation, and navigation.

The new requirements lesson is on slide 22, its worked reference is on slide 90, and the requirement-type menus are on slides 91–96. Slide numbers may change in your revision. Preserve the concepts and update every cross-reference.

Part 4 is now titled **Putting Prompts to Work**. Keep that title. The next stage is to make the examples a connected learning sequence and adapt every supporting artifact to it.

## Central design principle

**The training determines the exercises. The exercises determine the reusable prompts. The HTML tool supports those prompts.**

Do not let the current builder, its fields, the G2 template, or any other numbered template determine what the training can teach. Use clear task names. Retain useful legacy templates as optional material at the end or in a secondary reference area.

Make this insight explicit throughout: **role, context, tone, format, methods, constraints, and acceptance checks specify requirements for a reply or artifact.** Context also contains background facts; explain how important facts constrain the work. A role title alone does not guarantee expertise. Pair it with observable behavior.

Teach two complementary ideas:

1. **Requirement type:** What must be specified for this artifact? Examples include data definitions, narrative, interaction behavior, reading level, editability, and delivery format.
2. **Requirement quality:** Is the selected requirement necessary, clear, complete enough, consistent, feasible, singular, and verifiable?

Retain the requirements-writing sources in the deck and catalog. Describe the artifact taxonomy as an instructional application, not an externally standardized classification. Explain verification as meeting written criteria and validation as serving the real need.

Expand useful requirement types by artifact, with a concrete instruction and acceptance check for each. Present them as a menu. A simple task should not require filling every field. Distinguish required outcomes from preferences, identify conflicts, and preserve free-form requirements.

## Learning experience and facilitation

Preserve this progression: understand artificial intelligence and prompting; construct a useful brief; distinguish ASK from DELEGATE; produce and check something useful; leave with material usable at work.

Introduce the connection to requirements, standard operating procedures, specifications, acceptance criteria, and test protocols before detailed prompt construction. Refer back to it during exercises.

Maintain approximately 30 minutes of foundations and 30 minutes of application. Integrate short explanations into examples where useful. Protect practice first when time is tight. Use a connected hands-on case plus shorter demonstrations for the other activities; put full-length practice versions in the reference material. Do not pretend five complete workshops fit into 30 minutes.

Classify every slide by instructional contribution:

- **TEACH:** actively explain one important idea.
- **DO:** exercise, demonstration, or discussion with protected time.
- **REFERENCE:** independently understandable detail; orient briefly or skip live.
- **DIVIDER:** navigation with minimal time.

Identify anchors and record realistic timing, including opening files, generation, checking, discussion, and transitions. Recalculate the total after restructuring. Label appendix material as having no live allocation. Provide a prepared-output fallback for every live generation step.

Use these speaker-note fields on every slide:

```text
MODE: TEACH / DO / REFERENCE / DIVIDER
TIME:
PURPOSE:
LAND THIS: [one idea]
SAY: [2–4 concise talking points]
DO: [participant action, demonstration, question, or none]
BRIDGE:
IF LATE: KEEP / COMPRESS / SKIP
```

Preserve useful source references below the current notes. Resolve obsolete instructions rather than allowing conflicting timing or directions to remain authoritative.

Keep the restrained visual system: deep teal `#0E7C7B` for TEACH, amber `#C47A1F` for DO, cool gray `#A7B0B5` for REFERENCE, and charcoal `#232A31` for DIVIDER. Reinforce color with text labels. Use large live text, aligned margins, useful whitespace, and clear actions. Avoid excessive cards, tiny prompt screenshots, decorative graphics, and dense projected paragraphs. Put complete prompts in the workbook and reference layer.

## Main exercise sequence

### 1. Excel: inspect, analyze, and verify

Use the supplied supplier dataset in Course_Workbook.xlsx. Start with a basic request, inspect its weaknesses, then improve it by adding requirements that solve specific problems.

Teach source scope, row grain, reporting period, column types, metric definitions, aggregation, missing-data handling, units, output structure, and acceptance evidence. Preserve the original raw data and create a clearly identified cleaned detail dataset for subsequent exercises.

Use one main business question: **Which supplier has the highest return rate, and what should we investigate next?** Define return rate as total returned units divided by total shipped units within the same scope. Do not average row percentages. Avoid claiming a cause from a descriptive comparison.

Known checks to independently confirm:

- 144 detail records; exclude the existing TOTAL row.
- Total shipped units: 224,902. Returns: 432. Defect occurrences: 2,207.
- Alpha Components: 75,060 units, 74 returns, approximately 0.099% return rate.
- Bravo Plastics: 75,184 units, 262 returns, approximately 0.349% return rate.
- Cardinal Metals: 74,658 units, 96 returns, approximately 0.129% return rate.
- One missing inspection-hours value; missing is not zero.
- Delivery counts are absent, so monthly on-time percentages cannot establish a true overall delivery rate.
- Do not add defects and returns and label the sum as distinct defective units.

Provide the starter prompt, improved prompt, annotated requirement types, expected output, answer key, and one transfer question. Save the verified analysis for the next activity.

### 2. HTML: visualize the same data and specify behavior

Use the same cleaned supplier records and verified definitions to produce a self-contained HyperText Markup Language (HTML) dashboard. Introduce the chart and summary first, then add useful interactions through prompt revisions.

Teach the vocabulary a trainee needs to ask for a dashboard:

- Date or month range, inclusive endpoints, default range, and time granularity.
- Category filter, dropdown, single selection, multiple selection, and search.
- Supplier and Site filters; grouping, comparison, and metric selection.
- Type, Class, or Status controls only where a real source field or explicitly defined mapping exists. Do not invent these fields in the supplier data.
- Sorting, supporting-row detail, drill-down, and export of selected records when useful.
- Active-filter indicators, Reset, empty results, missing values, zero denominators, and invalid inputs.
- Consistent calculations and selection state across charts, summary values, and tables.
- Keyboard access, meaningful labels, readable contrast, and usable layout on a smaller screen.
- Embedded data, offline operation, snapshot date, and any dependencies.

For each term, give plain-language wording trainees can reuse and a visible check. For example: “Changing the month range must update every chart, total, and table using the same selected records.” Verify one filtered total independently. Recompute rates from filtered sums.

Deliver a working example dashboard and a prepared fallback, not only a prompt or screenshot. Clearly distinguish a static data snapshot from a live reporting system. Exercise the controls against known expected results.

### 3. Mock presentation: communicate the same findings

Finish the data sequence by turning the verified analysis and dashboard findings into an editable five-slide mock management presentation. Include an actual sample deck plus the instructions for creating it.

Use this prompt as a starting point and refine it:

> Create an editable five-slide management presentation using only the verified supplier analysis. The audience must decide what follow-up is warranted. Cover the business question and scope, the supplier comparison, one useful time or site view, a proposed follow-up, and limitations with next steps. Give each slide one main message, readable evidence, accurate units and reporting period, and brief speaker notes. Preserve uncertainty and missing-data limits. Do not invent causes or unsupported benefits. Check every number against the analysis and inspect the exported slides for clipping and readability.

Teach audience, decision, narrative, slide count, evidence, chart choice, typography, source attribution, notes, editability, and file-delivery requirements. Keep the mock business presentation distinct from the course deck.

### 4. Copilot and Outlook: evaluate a conversation and extract important data

Build a practical email exercise using the complete fictional packaging-change thread already included in the revised deck. Supply it as a standalone file suitable for copy and paste. Do not require participants to use private mail.

Provide this reusable prompt, with placeholders where needed:

> Review the selected conversation about [topic] using only the messages and attachments you can access. Create a brief of the current situation, followed by tables of decisions and actions. For each decision, show its status, conditions, and supporting message. For each action, show the task, explicitly stated owner, due date, status, and supporting message. Distinguish current dates from dates that were superseded. List unanswered questions, conflicts, missing information, and referenced attachments you cannot access. Preserve approval conditions. Write “Not stated” for missing details. Separate source facts from your interpretation. End with the next clarification needed. If requested, draft a reply for review; do not send it.

Explain the importance of source scope, chronology, extraction fields, evidence, and action boundaries. Verify the actual Copilot and Outlook workflow against current official documentation, and state any account or feature dependency. Supply the pasted-thread fallback.

Answer-key traps: October 2 is the proposed change date, conditional on quality sign-off; September 25 is the updated trial date; the 18,000 cost cap remains; Luis’s revised plan is due September 16; freight responsibility remains unresolved; the drawing is mentioned but unavailable. Do not invent final approval or missing due dates.

### 5. Documents: explain a topic at a fifth-grade reading level

Provide one short live demonstration and additional topic variations for self-study. Use respectful language for adult readers. Preserve meaning, necessary caveats, and technical accuracy.

Reusable prompt:

> Using [source], explain [topic] so a reader at a fifth-grade reading level can understand it. State the main idea first. Use familiar words, short sentences, meaningful headings, and one concrete example. Define necessary technical terms when first used. Use an analogy only if it is accurate, and explain where it stops being useful. Preserve important conditions and uncertainty. Do not invent facts or use a childish tone. End with three comprehension questions and a short answer key. Check the explanation against the source and identify any simplification that changes the meaning.

Include different topics, such as the water cycle, inventory replenishment, and how an internet message travels, using suitable source material. Treat readability scores as supporting evidence rather than proof of comprehension. Teach audience, vocabulary, structure, examples, fidelity, tone, accessibility, and learning-check requirements.

## Revise every supporting artifact

Inventory the supplied files first. Inspect their contents and existing behavior before editing. Use the following mapping, accommodating equivalent filenames if needed:

| Artifact | Required revision |
|---|---|
| Revised course PowerPoint | Build the connected exercise progression, preserve facilitation modes and reference depth, integrate requirement types, update notes, timing, sources, anchors, and links. |
| Course_Workbook.xlsx | Add a clear exercise index, step-by-step participant instructions, prompt iterations, requirement annotations, spaces for checks and revisions, links or filenames for outputs, and clearly separated instructor answer keys. Preserve raw data and provide checked detail data. |
| Prompt_Template_Configurator.xlsx | Align task names, selectable requirement types, wording, defaults, examples, and generated prompts with the course and HTML builder. Keep relevant advanced options optional. Check validation lists, formulas, references, and generated output. |
| Prompt_Template_Creator (1).html | Reorganize around the five real tasks. Make artifact-specific requirement menus, examples, and checks available. Preserve free-form input and manual edits. Fix the issue where changing a selection overwrites edits in the generated prompt. Avoid a “ready” status when the task is still empty. Test copy, reset, state changes, and exports. |
| Prompt_Anatomy_Cheat_Sheet (1).pdf | Produce a readable quick reference: task and audience, selected requirement types, one before/after example, and a short acceptance-check checklist. Do not compress the whole taxonomy into tiny text. Supply an editable source. |
| Elements_of_Prompting_Field_Guide.pdf | Reorganize around requirement quality, artifact-specific types, worked exercises, and troubleshooting. Repair clipped headings, spacing, sparse pages, and inconsistent formatting. Include reusable prompts and checks. Supply an editable source. |
| Prompt_Element_Taxonomy_Reference (2).pdf | Map role, context, tone, format, sources, methods, interaction, boundaries, and checks to requirement types. Add artifact-specific instruction/acceptance examples. Preserve useful depth while removing mandatory G-number navigation. Supply an editable source. |
| Requirements_by_Artifact.md | Expand and maintain the shared artifact taxonomy. Keep examples and acceptance checks consistent with every course artifact. Do not claim this teaching taxonomy is a formal standard. |
| Facilitation plan | Rebuild the complete slide classification, timing, anchors, protected exercises, and change rationale after slide edits. |
| Exercise source and output files | Supply cleaned data, a working dashboard, the five-slide mock presentation, the fictional email thread, expected email brief, plain-language sample documents, and answer keys. |
| Any existing prompt-library or resource folder | Update actual supplied files and references. Move legacy templates to an optional section. Remove dead links and references to folders that do not exist. |

The builder and spreadsheet configurator must offer the same five primary task families: analyze spreadsheet data, build an interactive dashboard, prepare a presentation, summarize an email conversation, and explain a topic clearly. Let the user select an artifact and see its relevant requirement types. Keep examples and manual additions available without forcing a rigid wizard.

A course exercise must remain usable by copying its prompt directly into an appropriate assistant. The builder is a convenience that follows the training. Keep older templates as optional additions at the end.

## Implementation order and acceptance

1. Inspect all supplied artifacts and the new facilitation baseline. Record missing inputs and identify claims needing current source verification.
2. Establish the connected exercises, requirement taxonomy, expected outputs, and checks. Map each requirement to the artifact that teaches or supports it.
3. Update the slide architecture and realistic 60-minute timing before visual redesign. Then revise the course, notes, and participant workbook.
4. Adapt the builder and configurator to the established exercises. Update the cheat sheet, field guide, taxonomy reference, and resource files from the same content definitions where practical.
5. Create all needed source samples and prepared outputs. Keep any invented training material clearly fictional and separate from the original supplier data.
6. Verify the complete package: data totals and denominators; dashboard controls and states; presentation editability and fit; email evidence and conditions; document fidelity and comprehension; builder edit preservation; spreadsheet formulas; reference links; consistent names and wording; and complete speaker notes.
7. Return the revised course PowerPoint, every updated supporting artifact, working exercise files, a facilitation plan, and a concise change log. Include a package index explaining what to open and in what order. Keep participant materials distinct from instructor keys.

Proceed through implementation using reasonable choices. Do not pause merely to ask approval for reversible edits. If a needed source is absent, complete what can be grounded in the supplied material, label the specific gap, and avoid claiming an unavailable file or feature was tested.

The final package should teach people to identify requirements, express them clearly, produce an artifact, and check whether it meets the actual need.
