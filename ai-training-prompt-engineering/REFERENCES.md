# References and aids

Everything that supports the five deliverables (see `DELIVERABLES.md`). Nothing
here is required in participants' hands; it exists so the course can be run,
checked, extended, and rebuilt.

## Instructor material (`references/`)

| File | What it is |
|---|---|
| `references/From_Prompts_to_Agents_Facilitation_Plan.md` | The instructor run plan: timing to the second, anchors, protected exercises, slide-by-slide audit. |
| `references/exercise-data/instructor-keys/` | The expected email brief and its four traps (task 4 answer key). The workbook's own KEY tabs cover task 1. |
| `references/CHANGE_LOG_Round17.md` | The change record for the course revision that produced this package. |

## Exercise sources and prepared fallbacks (`references/exercise-data/`)

Every live generation step in the course has a prepared fallback here.

| File | Used by |
|---|---|
| `Supplier_Data_Clean.csv` | Task 2 — the checked 144-row detail set (also lives in the workbook's Data_Clean tab). |
| `Supplier_Quality_Dashboard.html` | Task 2 fallback — the working offline dashboard with a visible footer self-check. |
| `Supplier_Quality_Mock_Presentation.pptx` | Task 3 fallback — the five-slide mock management deck, every number traced to the workbook. |
| `Packaging_Change_Thread.txt` | Task 4 — the fictional 10-message thread, copy-paste ready (`Email_Thread_Packaging_Change.txt/.pdf` are the long-course variants). |
| `plain-language/` | Task 5 — the reusable prompt and three practice topics, each with source, sample output, and key. |
| `Quote_*.pdf` | Optional extension — three deliberately non-comparable supplier quotations. |

## Deeper reference

| File | What it is |
|---|---|
| `references/Elements_of_Prompting_Field_Guide.pdf` | Deep definitions of every prompt element — mechanism, weak vs strong fills, failure modes — plus the full evidence compendium (works / myth / expired with the why per line). |
| `references/Prompt_Element_Taxonomy_Reference.pdf` | The full element ontology in print, with the elements-to-requirement-types mapping up front. |
| `references/Prompt_Template_Configurator.xlsx` | The spreadsheet twin of the prompt creator (Tasks sheet + element-level builder sheets). |
| `references/From_Prompts_to_Agents_Training.pptx` | The long-format 69-slide deck the 60-minute course distills; remains usable for extended sessions. |
| `Requirements_by_Artifact.md` | The shared requirements catalog — the single source the creator, configurator, field guide, and deck reference pages draw their menus from (maintenance map inside). |
| `prompt-library/` | 13 copy-ready legacy templates plus the machine-readable element taxonomy (`taxonomy/`). |

## Editable sources and research (`src/`, `notes/`)

| Path | What it is |
|---|---|
| `src/` | Build scripts — every deliverable and reference artifact regenerates from here (see `README.md` → Rebuilding). The 60-minute deck is maintained as a .pptx; its edit scripts and pristine baseline are preserved. |
| `src/assets/course_content.json` | The course PDF's content (chapters and blocks) — edit here, then rebuild. |
| `notes/research/` | The research files behind every dated claim, with retrieval dates. |
| `notes/design/` · `notes/intake/` | Design records and the pristine uploaded baselines. |
| `PROJECT_STATE.md` · `PENDING_CHANGES.md` | Maintainer state and the change ledger. |
