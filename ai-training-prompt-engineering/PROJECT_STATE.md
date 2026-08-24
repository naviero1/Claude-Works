# PROJECT STATE — continuation brief for any future session

**Project:** "From Prompts to Agents" — prompt-engineering training + template system
**Owner:** Oscar Penny (owns all content and the quarterly refresh)
**Branch:** v1.1 merged to `main`; v1.2 developed on `claude/training-course-polish-oxohwj`
**Last updated:** 2026-08-24 — v1.2 (presenter polish + taxonomy handout slide)

## What this project is

A focused training (deck + one-page cheat sheet), a 13-template prompt library with a deep
element field guide (ELEMENTS.md), and a machine-readable **element taxonomy**
(`prompt-library/taxonomy/*.json` — 19 elements · 70 attributes · ~250 options · 18 presets)
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

## v1.2 (2026-08-24) — presenter polish + taxonomy handout

Owner asked for: (1) the taxonomy introduced in the course as a side handout with an
explanation, (2) a per-slide review for gaps/engagement/format/pictures, (3) speaker notes
that expand every acronym and give the reading sequence per slide, (4) presenting direction.
Deck is now **57 slides**:

- **New slide 26** (Part 3, after the safety-valves slide): "Your field map — the Prompt
  Element Taxonomy" — what the handout is, the element→attribute→option tree (drawn from
  the real Role element), the counts band (19 · 70 · ~250 · 18), and the handout pack.
- **Every slide's notes rewritten** to three sections: `HOW TO PRESENT` (numbered
  say/point/walk sequence + bridge line to the next slide), `ACRONYMS` (each acronym on
  that slide, expanded with a one-line meaning), `CONTENT` (the prior notes: facts,
  sources; `[REFRESH QUARTERLY]` markers preserved, and added to the storage-map slide
  which was missing its marker).
- **Engagement/format adds:** course-progress pill bar on all six dark dividers (current
  part highlighted — `H.partMarker`); a 3:00 clock badge on all five rep slides
  (`H.repTimer`); tokens slide now draws the sentence as real token chips + a "try a
  tokenizer" callout; who's-who slide gains the "one question decides" rule card; demo 2
  gains the backup-plan band; rep 6 gains the five-rung pill picker; glossary adds
  "Taxonomy" (17 terms); welcome + playbook-pointer slides now name the full handout pack.
- **Fixes:** stale absolute cross-ref on the 2026-update slide ("slide 22" → relative);
  README's stale counts (deck 49→57; taxonomy 78 attrs/286 opts/14 presets → 70/~250/18,
  computed from the JSON).
- **Run_of_Show.pdf regenerated (V1.2):** new slide numbers (S1 = 1–36, S2 = 37–57), a
  0:39 taxonomy segment (compressible to 30 s, never skipped outright), handout-pack prep
  item, updated contingency cuts.

## v1.3 (2026-08-24) — owner re-evaluation of slides 20–24; Run of Show retired

Owner feedback: slides 20/21/23 unclear value, 24 not explanatory enough; Run of Show PDF
not needed; the Taxonomy Reference stays as the output PDF. Deck stays **57 slides**;
slide numbers from the valves slide (25) onward are unchanged.

- **Slide 20 (new):** "Three of your real tasks beat every leaderboard" — merges the old
  rankings-caution slide and Rep 2 into one action slide with a built-in 60-second
  write-down. Part 2 no longer has a separate rep.
- **Slide 22 (new, replaces the vendor table):** the anatomy SHOWN — a real ~70-word
  prompt as five tagged blocks (ROLE/TASK/CONTEXT/FORMAT/EXAMPLES) with a compact
  "same recipe, every vendor" side panel; the vendor-quote detail moved to notes.
- **Slides 23–24 (split from old 24):** "The elements, defined" 1 of 2 (Role·Task·Context)
  and 2 of 2 (Format·Examples) — each element now carries its job, WHY IT WORKS, the
  failure it PREVENTS, and the weak→strong pair at readable size; slide 24 closes with
  the "pattern behind all five" band bridging to the diagnosis grid.
- **Run_of_Show.pdf and src/build_runofshow.py deleted** — presenting direction lives in
  the speaker notes (and the owner's presenter-guide artifact). Prep/contingency content
  preserved there.
- **Prompt_Element_Taxonomy_Reference.pdf regenerated** from the taxonomy JSON (25 pp) —
  it remains the side-handout PDF, per owner.

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
