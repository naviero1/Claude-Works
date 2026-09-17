# Checkpoint 1 — keep the summaries and refine the presentation

**Updated 2026-09-17: Oscar has approved the six-slide pilot with Rocksteady's recommendations. The [approval record](approvals.md) and [final handoff](rocksteady-handoff.md) now govern. This assessment preserves the original findings; deferred background, blanket font freeze, and slide-34 no-image recommendations below are superseded for the pilot. Separate notes/content repairs remain queued.**

The current summarized course is the right baseline. Keep its 103-slide physical order and comprehensive reference layer. The application sequence is coherent in both the deck and the current 83-page extended PDF (Portable Document Format). The priority is clearer visual relationships, prompt grouping, correct mode colors, and a few precise handoff and reference corrections. A rollback or broad rewrite would undo useful progress.

## Where the Rocksteady exchange stands

Rocksteady's reply 09 proposed a visual system; reply 10 supplied two sample renders for slides 34 and 39 at commit `b42c071`. Beebop's instruction 08 reviewed those samples and gave refinements. During publication, reply 11 arrived: Rocksteady acknowledged the new pause and confirmed that the presentation is unchanged. The branch advanced from `6e829b82bcd92653f0daa68fcdbbf1d60664a4cb` to `96e3364d88d4b88ad9604e3f5caa950996feca0f` through coordination mirrors only; the deck itself last changed at `5afda8e2162a2924d578708b4516dcba2dccd2b9`. Beebop checked the commit comparison and preserved those concurrent changes.

Oscar's new attached brief changes the next step to assessment and explicit approval. Beebop posted instruction 09 to pause implementation under 07–08. The two old samples are discussion evidence, not permission to replace current wording, change fonts, or expand across the deck. The [Rocksteady handoff](rocksteady-handoff.md) records which earlier ideas remain useful and which are superseded.

## Confirmed baseline and review coverage

| Item | Verified result |
|---|---|
| Owner file | `From_Prompts_to_Agents_Facilitated_60_Minute(1).pptx` |
| Current repository file | `ai-training-prompt-engineering/deliverables/From_Prompts_to_Agents_Facilitated_60_Minute.pptx` |
| Branch | `claude/training-course-polish-oxohwj` in `naviero1/Claude-Works` |
| Identity | Exact byte match: Git blob `e83fd87a8b3e8c868942bdeda668ce085a44c8e4`; SHA-256 `117f60b30c292527d1ac8444ab3efafdbb0ef8d0f3ff159b68149e5804bd24fa` |
| Structure | 103 slides; closing at 70; 25 REFERENCE orientations inside 1–70, plus 33 optional slides after the close |
| Preservation record | [Baseline inventory](baseline-inventory.json) and its 11 per-slide parts: native identities, exact titles, all visible text/table cells, declared fonts/sizes/styles, notes, shape/media and package hashes |
| Mapping | [Original/current/proposed map](slide-map.csv). All proposed physical positions are unchanged. |
| Visual coverage | All 103 supplied slide renders inspected; full-size checks on all 71–103 and priority/dense slides in 1–70; all six pilot originals independently viewed at full size by Beebop |
| Render limit | These are the supplied source renders, with reported substitutes for Calibri, Cambria, and Consolas. No claim of a fresh native PowerPoint render, intended-font wrapping test, or projector rehearsal. |
| Companion coverage | Actual current PDF, workbook structures, and current source/build/index files inspected. PDF section/text audit, not a fresh visual inspection of every PDF page or browser test. |

All three named review materials were located and consulted: `Bebop_Rocksteady_Visual_Polish_Brief.md`, `Training_Slide_by_Slide_Visual_Review.html`, and `Training_Visual_Review_Package.zip`. Their supplied source fingerprint matches the confirmed deck. Earlier findings were checked against current native content and rendered images; for example, long filename bands on 39 and 44 are intact, and the low text on 22 and 78 is crowded rather than clipped.

## Content: what should remain

Keep the requirements-writing bridge on 21–25, ASK versus DELEGATE, the incremental prompting/checking method, and the summarized live wording. Preserve every existing value, definition, caveat, source boundary, and complete prompt. Successful comparison tables and existing instructional illustrations should stay. The extended PDF remains a comprehensive reading resource; it does not need rebuilding as a short slide transcript.

The source files reveal a few real inconsistencies. The prepared management presentation generator reads a parallel CSV (comma-separated values) file while the dashboard correctly reads the returned workbook. Legacy workbook copy still invites uploading the answer-bearing full course workbook, and the PDF describes a README tab absent from the one-sheet participant input. These are specific build/content decisions, not evidence that the overall sequence failed. See [companion-review.md](companion-review.md), C01–C05.

## Sequence: keep the order, repair the transitions

| Section | Recommendation |
|---|---|
| 33–39 | Keep Excel inspection, analysis, follow-up, editable charts/returned file, dashboard, presentation. Explicitly carry the same verified workbook, period and definitions into 39. |
| 40–44 | Keep email, quote extraction, quote comparison, research. Say when the source changes; only the first data sequence shares one workbook. |
| 50–56 | Keep mission-brief teaching/practice together. Add a brief spoken distinction between requested boundaries and configured controls before 51; retain the fuller explanation on 53. |
| 61–64 | Keep saving an earlier useful prompt, the reference clarification callback, habits, then capstone. Add saving the checked capstone revision within its existing final 20 seconds. |
| 65–70 | Keep reference pages in place. Propose a live jump from 64 to 70, pointing participants to 65–69 for later reading. |

No physical move or mode change is recommended. Exact titles, current/proposed order, dependencies, trade-offs, and proposed note wording are in [sequence-review.md](sequence-review.md). Approval of visuals does not approve those note/navigation changes.

## Engagement: protect the attempt and the check

Slide 34's first prompt must remain a distinct inspection that ends in “then wait.” Keep its second calculation prompt separate. Retain open thinking space on activity slides and blanks on 56.

The email attempt currently points to 88–89, but 89 visibly includes an answer-key strip. Use the supplied text thread for the attempt, then show 88–89 at debrief; the proposed change is a notes/navigation correction, not deletion of the key. Slide 38 deliberately supplies expected filtered values for a verification task; preserve them. Slide 29's TOTAL-row worked example is useful preparation, not a reason to undo the exercise. Keep the new bars on 87 in their current answer-key reference location.

## Visual presentation: selective, editable, and constrained

| Treatment | Slides | Purpose |
|---|---:|---|
| A — keep mostly unchanged | 61 | Preserve successful text, tables, diagrams, and reference pages |
| B — formatting only | 16 | Repair spacing, label widths, prompt separation, and footer clearances |
| C — meaningful visual treatment | 26 | Make a sequence, comparison, feedback loop, evidence link, boundary, or chronology visible |

The 26 candidates are 25.2% of the deck. This is deliberately below the approximate 30-slide guidance because several additional pictures would repeat instructions or amplify answers. Two candidates refine existing diagrams; 24 propose new editable native treatments. No generic illustrations or decorative charts are needed.

The proposed six-slide pilot is:

| Original/current slide | Exact title | Treatment |
|---:|---|---|
| 23 | A prompt is a small work specification | Annotate the existing prompt with its requirement types |
| 28 | The improvement loop | Show the full Plan–Do–Check–Act return cycle |
| 34 | Upload the Data File and Run These Two Prompts | Formatting only; separate the two complete prompts |
| 37 | Describe the Dashboard You Want | Labeled schematic wireframe, with no invented results |
| 53 | Instructions and enforceable controls | Distinguish the written brief from an environment boundary and approval checkpoint |
| 87 | Supplier analysis: answer key | Proportional bars in the existing return-rate table; preserve every cell and caveat |

See [complete classification](slide-classification.md), [measured visual specifications](image-needs.md), [asset register](asset-register.md), and the [unmodified pilot originals](review-evidence/pilot-originals.html). The preview contains original slides only; it is not a redesigned pilot.

Preserve current font families, sizes, emphasis and wording. Use layout, spacing, and appropriate native diagrams to improve legibility. The pilot must demonstrate fit under those constraints; if it cannot, report the exact problem and ask for a scoped exception. No automatic shrink-to-fit or wholesale template replacement.

## Responsibilities and help needed

Beebop selects each visual, defines its instructional purpose and dimensions, verifies evidence, reviews actual assets/renderings, and manages GitHub organization. Rocksteady constructs the specified editable native diagrams, annotations, wireframe and bars after approval. Oscar approves the pilot and any individually selected exceptions.

**Nothing needed from Oscar through Gemini at this stage.** These concepts benefit from accurate editable construction. No illustration has been generated and no placeholder is being reported as an asset. [Gemini requests](gemini-image-requests.md) records that decision and the procedure if a genuine need emerges.

## Timing and decisions kept separate

Current active notes total **72:50**, including **45:00 of DO practice**. The proposed closing jump makes it **72:00**. The original 60-minute/30-minute-practice run note is stale. Slides 71–103 have no current live allocation; duplicated and archived timings are excluded. An 80-minute slot leaves 7:10 on the current allocation, before unallocated technical/discussion overhead. This is arithmetic, not a rehearsal. Timing does not justify cutting practice.

The decision queue separates transition repairs, stale indices/cues, historical note quarantine, timing description, unsupported quote wording, reference terminology, and companion lineage/distribution. Keep all unapproved wording and notes unchanged. In particular, the old email key on 82 must not be mixed with the current thread, and slide 51's active note should not imply that a written brief alone makes unsafe action difficult.

## Original checkpoint decision queue

The pilot and its scoped exceptions are authorized in [approvals.md](approvals.md). **SEQ-01–06**, **NOTE-01–03**, active-note **TIME-01**, and **CONTENT-01–02 / companion C01–C05** remain separately scoped follow-up work. Accepted timing guidance is in [pilot-facilitation-plan.md](pilot-facilitation-plan.md). Full expansion requires review of the completed pilot.

The main deck and extended PDF remain the baseline while Rocksteady builds the authorized pilot in a versioned copy.
