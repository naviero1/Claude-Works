# From Prompts to Agents — AI Training

A focused training on **prompt engineering** across two modes: **generative AI** (prompts that
write) and **agentic AI** (prompts that work). Built August 2026 as the companion to
"Working Smart with AI."

## What's in here

| Path | What it is |
|---|---|
| `deliverables/From_Prompts_to_Agents_Training.pptx` | The training deck (59 slides, incl. two "why each dial matters" evidence-map reference slides). Every slide's speaker notes carry three sections: HOW TO PRESENT (the numbered reading/pointing sequence), ACRONYMS (every acronym on the slide, expanded), and CONTENT (facts, sources, refresh markers). Runs as one 2-hour session or two 1-hour halves (split after Part 4). |
| `deliverables/Prompt_Anatomy_Cheat_Sheet.pdf` | One-page printable: generative anatomy + agentic mission brief side by side. |
| `prompt-library/` | 13 copy-ready templates — 8 generative (G1–G8), 5 agentic (A1–A5) — plus `ELEMENTS.md` (the element field guide) and the library's management conventions in its README. |
| `prompt-library/taxonomy/` | The machine-readable element ontology (19 elements · 78 attributes · 286 options · 18 presets — counted including nested sub-attributes, as the tools count). v1.1: every attribute carries a research-backed `why` — what that dial does to the output, with its evidence (citations in `notes/research/`). Source of truth for the three tools below; introduced in the deck as the Part 3 "field map" handout slide. |
| `deliverables/Prompt_Template_Creator.html` | Interactive template builder: toggle elements, pick options, watch the prompt assemble; loads any library template as a starting instance. Single file, works offline. |
| `deliverables/Prompt_Element_Taxonomy_Reference.pdf` | The full ontology in print: every element, attribute, and option with guidance (25 pp). |
| `deliverables/Prompt_Template_Configurator.xlsx` | Spreadsheet version: dropdown pickers per attribute, prompt assembles by formula. |
| `deliverables/Elements_of_Prompting_Field_Guide.pdf` | Deep definitions of every element — mechanism, weak-vs-strong fills, failure modes (7 pp). |
| `notes/research-notes.md` | Synthesis of the research behind every slide; headline verified facts; UNVERIFIED list. |
| `notes/research/` | The ten full research files with inline source URLs, all verified Aug 21, 2026. |
| `src/` | Build sources: `node deck_main.js` rebuilds the deck (pptxgenjs); `python3 build_cheatsheet.py` rebuilds the cheat sheet (reportlab); `assets/make_icons.js` regenerates icon PNGs. |

## The training at a glance

1. **The primer** — four eras of AI; tokens, context windows, RAG, reasoning models, hallucination.
2. **Models & tools** — the Aug-2026 landscape; what the Chinese open-weight wave changed; the agentic tool gallery; right-tool-for-the-task matrix.
3. **Prompt engineering** — the universal anatomy (Role · Task · Context · Format · Examples); the elements defined + two safety valves; the taxonomy field-map handout; seven techniques; evidence vs. myth; prompting thinking models.
4. **The playbook** — templates applied: data analysis, writing, evaluations, spreadsheets, decks, interactive HTML, research.
5. **Agentic prompting** — the mission brief (12 blocks); the ETL→Presentation worked example; gates, autonomy rules, guardrails; standing memory (CLAUDE.md, reuse by diff).
6. **Prompt management** — the promotion ladder; where prompts live per tool; conventions and governance.

## Rebuilding

```bash
cd src
npm install            # pptxgenjs, react-icons, sharp (once)
node assets/make_icons.js   # regenerate icons (once)
node deck_main.js      # -> deliverables/From_Prompts_to_Agents_Training.pptx
python3 build_cheatsheet.py # -> deliverables/Prompt_Anatomy_Cheat_Sheet.pdf
```

## Maintenance & ownership

**Owner: Oscar Penny — all content and cadence.** The dated material (assistant landscape,
agent gallery, task matrix, storage map — marked `[REFRESH QUARTERLY]` in speaker notes)
gets a quarterly pass: re-verify names/features, edit sources, rebuild. Delivery: two
one-hour sessions (split after Part 4); the per-slide presenting direction lives in each
slide's speaker notes (HOW TO PRESENT / ACRONYMS / CONTENT — the Run of Show PDF was
retired in v1.3 in favor of the notes). Project state and continuation instructions:
`PROJECT_STATE.md`.

## House rules baked into the material

- All examples are generic — no internal document names or confidential data anywhere.
- Every currency-sensitive fact is dated ("as of Aug 2026") and traceable to `notes/research/`.
- The organization's AI policy and approved-tool list outrank anything in this training.
