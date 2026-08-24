# PROJECT STATE — continuation brief for any future session

**Project:** "From Prompts to Agents" — prompt-engineering training + template system
**Owner:** Oscar Penny (owns all content and the quarterly refresh)
**Branch:** `claude/ai-training-prompting-agentic-kzcsps` → being merged to `main` after v1.1
**Last updated:** 2026-08 — v1.1 COMPLETE, merged to main; iterate on main

## What this project is

A focused training (deck + one-page cheat sheet), a 13-template prompt library with a deep
element field guide (ELEMENTS.md), and a machine-readable **element taxonomy**
(`prompt-library/taxonomy/*.json` — 19 elements · 78 attributes · ~290 options · presets)
that generates three tools: an interactive HTML **Template Creator**, a taxonomy **reference
PDF**, and an **XLSX configurator**. All research behind it is in `notes/research/` (16
sourced files). Everything regenerates from source:

```bash
cd src
node deck_main.js                    # deck  -> deliverables/From_Prompts_to_Agents_Training.pptx
python3 build_cheatsheet.py          # cheat sheet PDF
python3 build_elements_guide.py      # ELEMENTS field-guide PDF
python3 build_builder.py             # Template Creator HTML (validates taxonomy)
python3 build_taxonomy_pdf.py        # taxonomy reference PDF
python3 build_configurator_xlsx.py   # configurator XLSX — then ALWAYS recalc:
python3 <xlsx-skill>/scripts/recalc.py ../deliverables/Prompt_Template_Configurator.xlsx
# render-check pattern: soffice --headless --convert-to pdf … then pdftoppm -png, view pages
# (needs libreoffice-impress + libreoffice-calc installed; HOME=/root for soffice)
```

## HARD RULES (do not violate)

1. **No company data anywhere** — no part numbers, supplier/site names, internal codes,
   people other than the owner, or personal data. All examples generic/fictional. A scrub
   was completed (commits `ca5f865`/`81214ef`); keep it that way.
2. Prompt *usage patterns* (generic job shapes, habits) are allowed; identifying data is not.
3. Taxonomy JSON is the single source of truth — edit there, regenerate artifacts, never
   hand-edit deliverables.
4. Every currency-sensitive fact carries an "as of" date; research files hold the sources.

## Decisions log (owner's answers, 2026-08)

- **A1 YES** — add element-definition slides (Part 3 pair) + inheritance-map slide (Part 5).
- **A2 B** — Part 4 restructure: keep divider + G2 anatomy; replace the four catalog slides
  with two live-demo slides (G3 blind critique, G6 dashboard-from-a-paste) + one
  handout-pointer slide.
- **A3 YES** — one skippable "three-minute rep" mini-slide per part (P1, P2, P3, P5, P6;
  Part 4's demos are its rep).
- **A4 YES** — merge old slides 2+3; cut embeddings sidebar on the ladder slide; mark dated
  slides (assistants, agent gallery, task matrix, storage map) as quarterly-refresh in notes.
- **B5** — two 1-hour sessions; split after Part 4; add a Session-2 recap slide before Part 5.
- **B6 YES** — build a run-of-show (two 60-min sessions, demo scripts, contingency cuts).
- **B7 NO** — no 30-day follow-up mechanism.
- **C8** — pilot the Template Creator AFTER the training.
- **C9 YES** — add 4 generic presets: comparison study, scored comparison workbook,
  versioned model update, master-doc → audience variants.
- **C10** — owner will provide a curated prompt doc (his favorite prompts, redacted) — first
  intake priority; mine it for taxonomy options when it arrives.
- **D11** — iterate on main: after v1.1, produce a gap analysis (v1.0 → v1.1) and merge the
  branch into main; continue work on main.
- **D12** — Oscar owns all refresh/maintenance.

## v1.1 checklist (current build)

- [x] Merge slides 2+3 (deck_pt1.js)
- [x] Cut embeddings sidebar, widen ladder cards (deck_pt1.js)
- [x] P1 rep mini-slide (deck_pt1.js)
- [x] P2 rep mini-slide + OpenClaw "slide 38" ref → "Part 5" (deck_pt2.js)
- [x] Element-definition slide pair after anatomy slide (deck_pt3.js)
- [x] Fix "slide 25" cross-ref on techniques slide → relative wording (deck_pt3.js)
- [x] Part 4 rebuild: demos + handout pointer, remove old 29–32 (deck_pt3.js)
- [x] P3 rep mini-slide (deck_pt3.js)
- [x] Session-2 recap slide before Part 5 divider (deck_pt4.js)
- [x] Inheritance-map slide after the distinction slide (deck_pt4.js — table from
      ELEMENTS.md Part 3)
- [x] "slide 38" ref in agent-blocks slide → "later this part" (deck_pt4.js)
- [x] P5 + P6 rep mini-slides (deck_pt4.js)
- [x] Quarterly-refresh notes on dated slides (speaker notes) + README ownership section
- [x] Rebuild deck; render-check every new/changed slide
- [x] Add 4 presets to presets.json; rebuild builder/taxonomy-PDF/xlsx (+recalc)
- [x] RUN_OF_SHOW (md + PDF via new src/build_runofshow.py, house style)
- [x] GAP_ANALYSIS.md (v1.0 → v1.1, mapped to decisions)
- [x] Commit branch → merge into main → push main (owner authorized D11)
- [x] Send updated deck + run-of-show to owner

## Open intake (waiting on owner; see INTAKE.md)

Curated prompt doc (first) · Berryman & Huyen books as EPUB/split-PDF (<10MB parts; Drive
originals exceed the API download limit) · complete Phoenix & Taylor copy (all current copies
end at Ch. 1) · three product screenshots (Copilot gallery filters, prompt-improver output,
Canvas sliders). When material lands in `notes/intake/`: mine → update taxonomy → regenerate.

## Style notes for continuity

House palette/fonts live in `src/deck_lib.js` (teal `#0E7C7B`, ink `#232A31`, Cambria/Calibri)
and are mirrored in every PDF generator. Slide idiom: kicker + message-title, cards, icon
circles, callout bands, speaker notes on every content slide. Deck cross-references must be
relative ("two slides ahead", "later this part") — never absolute slide numbers.
