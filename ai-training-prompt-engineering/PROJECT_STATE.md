# PROJECT STATE — continuation brief for any future session

**Project:** "From Prompts to Agents" — prompt-engineering training + template system
**Owner:** Oscar Penny (owns all content and the quarterly refresh)
**Branch:** v1.1 merged to `main`; v1.2 developed on `claude/training-course-polish-oxohwj`
**Last updated:** 2026-09-16 — **ROUND 17 (v2.0): the package pivots to the owner's 60-minute facilitated course.** Baseline = his uploaded 96-slide deck + facilitation plan + Requirements_by_Artifact catalog (pristine copies: notes/intake/round17/). Delivered: revised 101-slide deck (connected five-task Part 4 on one supplier case; new documents demonstration DO 2:00; TEACH −1:50; live total exactly 60:00 with DO 32:00; five appendix pages added; all notes fields intact; validated + rendered) · verified exercise assets (Supplier_Data_Clean.csv; working self-checking dashboard; mock five-slide management deck; canonical email thread + instructor key; plain-language pack; r28 Copilot verification) · workbook rebuilt around tabs 1-Analyze-Data…5-Explain-Clearly with INDEX + computed instructor keys · Template Creator task-first (menus generated from the catalog; edit-preservation + honest-status fixes in both views, machine-tested) · Configurator Tasks sheet (recalc-verified) · cheat sheet, field guide (20pp, requirement-quality spine), taxonomy reference (mapping) all reorganized · facilitation plan regenerated (101 rows, recomputed) · PACKAGE_INDEX + CHANGE_LOG_Round17 in deliverables/. Full record: deliverables/CHANGE_LOG_Round17.md + notes/design/round17_sequence.md. The long-format deck and its legacy tabs remain untouched as the reference layer. — previously v1.15 (owner: the dashboard exercise): new workbook tab **EX-Dashboard** (between EX-Email and EX-Report; uses the workbook's own Data tab) — four staged prompts (SHAPE proposed as plain text then STOP · BUILD single-file offline HTML per G6 with formulas visible · CHECK by TOTAL-row reconciliation + one hand-recomputed tile · REFINE one element), a WHAT-MAKES-A-KPI block (decision · formula · target · level/trend/gap), and the 20-term dashboard VOCABULARY each with an "ask for it like this" phrasing (owner: "this vocabulary will be important in general for data analytics"). Pointers: workbook README, pack header/print (13 exercise tabs), demo-slide grey band + notes homework framing, README.md. Verified by 3-agent workflow (trainee sim on the real workbook · adversarial review vs house rules/G6/dataviz refs · coherence sweep) — previously v1.14 (owner, three directives): (1) NO update/version language in audience-facing handouts — "for an audience that has never seen this training": field-guide header now dateline-only, compendium intro rewritten, taxonomy-PDF "New in v1.1"/"Since v1.8" lines neutralized; (2) the MEASURED speed-vs-capability chart — five vendor panels (Anthropic/OpenAI/Google/xAI/open-weights), every current version plotted at its strongest thinking setting, single-hue small multiples per the dataviz-skill all-pairs rule; data live-fetched from the Artificial Analysis leaderboard 2026-09-13 → notes/research/r27 (REFRESH QUARTERLY), built by src/build_speed_chart.py (matplotlib), embedded in Field Guide Part 7; spectrum-table DeepSeek cell updated V3/R1→V4 Pro/V4.1 Flash (r27 ripple); (3) redundancy audit put to the owner — he chose TWO cuts (placement works/expired pair merged into the WORKS entry with a one-clause history; Part 3's superseded "when to switch modes" line deleted) and explicitly KEPT the persona/examples pairs, repeated stats, mirror entry, the Out drumbeat, and the ten-things page. Field Guide 14pp, layout re-packed (chart page flows into the spectrum table via repeatRows header) — previously v1.13 (owner: "what works / what's myth / expired, explaining why — expand and put it in the PDFs; merge the playbook with the course-summary documents"): the Field Guide grew from 7 to 14 pages — Part 5 = the evidence compendium (proven-vs-myth slide + the full 2026 Do/Don't/Expired playbook, merged and deduplicated, a WHY per line + the mirror box + the five coherence seams + contested edges), Part 6 = the failure modes (hallucination's four characters with defenses; the run-time diagnosis grid + instruction layers), Part 7 = engine & vehicle (fast-vs-thinking; the Sep-2026 MODEL SPECTRUM table — per-vendor fast/thinking model names, REFRESH QUARTERLY; chat/workflow/agent), Part 8 = ten things + one-sentence wrap + 20-term glossary appendix (all owner-picked from the slide survey; hall-of-shame case stories deliberately excluded per owner). Cheat sheet: evidence box upgraded to Works · Myth · Expired + pointer. **Playbook_One_Pager.pdf RETIRED** (owner chose true merge) — build section removed, file deleted; slide 30 band, playbook notes, and the welcome "you leave with" list now point at the Field Guide instead — previously v1.12 (owner hand-edits merged into sources: 14pt bullets, red ladder analogies, gallery moved to Part 5; hardware chart Y-axis labeled in FLOP + data-center equivalence; tokens audience reworded; Part 3 rep = course-log report with new Prompt 1 acknowledgment step; workbook tab EX-Rebuild → EX-Report) — previously v1.11 (the Out redefined everywhere: condition · honest move · surfacing, UNKNOWN + gap list as the checkable default; mirror illustration embedded on the flattery-bias slide; PowerPoint repair prompt fixed — negative shape extents on the eras slide normalized) — previously v1.9 (font floor R14 v2: reading text ≥11pt target, ≥10 hard floor, fewer footnotes; five over-cropped images re-laid at native 16:9) — previously v1.8 (owner's "update"): all 19 owner-generated
illustrations embedded (R16 — Part 1 concept art, four S14 emblems, DeepSeek hospital,
Deming portrait, courier/guardrails/memory-ladder/blueprint/bench/office scenes); three
NEW slides — "Two layers, one craft" (anatomy = design layer, PDCA = process layer, worked
embedded-PDCA brief, 9C), "Pick the vehicle" (chat/workflow/agent), "When the run goes
wrong" (run-time context-failure grid + instruction layers); S30 native mirror bars
(100 vs 149); Round 9 survivors applied with r26-verified wordings (operating-manual test,
design-thick/ship-lean, harness-gate sentence, eagerness dial, eval lite, HANDOFF≡compaction,
context-engineering line + glossary, kill-order in welcome notes, wrap-up sentence); all
three handouts (cheat sheet, taxonomy PDF, Template Creator) reframed onto the PDCA loop;
deck now 69 slides (v1.10: most-used slide cut; the three PDCA slides consolidated to two). Held in intake: certificate emblem (benched), gallery wall (S15 has no
room within the font floor — future use). Bench scene placed on the dark close (flagged:
ledger had slotted the question slide, which had no room at full size).

## What this project is

A focused training (deck + one-page cheat sheet), a 13-template prompt library with a deep
element field guide (ELEMENTS.md), and a machine-readable **element taxonomy**
(`prompt-library/taxonomy/*.json` — 19 elements · 78 attributes · 286 options · 18 presets, counting nested sub-attributes as build_builder.py does)
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

## v1.3 addendum (2026-08-24) — Template Creator UX v2

Owner asked for the Creator polished and made very user friendly. `src/builder_template.html`
rewritten (same data pipeline, byte-identical assembly logic):

- **Template gallery on first visit** — "What do you want the AI to do?", 18 template cards
  with one-line blurbs grouped into "prompts that write" / "briefs that run a job", plus
  start-blank cards. Reachable anytime via 📋 Templates; a 1-2-3 step strip sits under the header.
- **Guided editor** — element cards collapse to a picks summary (count pill + chips);
  sidebar shows green content dots and jump-to-card; PICK ONE / PICK ANY labels; option
  chips are real buttons with hover/focus popovers showing when-to-use + the exact text
  inserted; extended options behind a "+N more" pill; techniques/antipatterns tucked into
  a "Tips & pitfalls" disclosure. OOP jargon hidden behind a "Show technical labels" toggle.
- **Finishing flow** — placeholder bar counts {{ }} with a Find-next jump; token/word
  stats; Copy with honest toasts; Download .txt; Start over with confirm; restored-session
  notice with Start fresh; mobile bottom bar; "How it works" help overlay.
- Fixed a real bug: `[hidden]` was overridden by `display:flex` panels (global
  `[hidden]{display:none!important}`).
- **Counts corrected to canonical** (as build_builder.py counts, incl. nested sub-attributes):
  19 elements · 78 attributes · 286 options · 18 presets — deck slide 26, README, and this
  file updated (the v1.2/v1.3 "70/~250" figures were top-level-only undercounts).

## v1.4 (2026-08-24) — the "why it matters" evidence layer (owner request)

Owner asked to explain, per criteria class (attribute level, not just element level), WHY
each prompting attribute matters and how it affects output — research-grounded.

- **Taxonomy v1.0 → v1.1:** every one of the 78 attributes (incl. nested sub-attributes)
  now carries a `why` field — the effect on output plus compact evidence, drawn from the
  verified research base in `notes/research/` (r3_techniques, t1_prompt_report,
  t6_agentic_attrs) and vendor guidance. `build_builder.py` now FAILS the build if any
  attribute lacks its why, so the layer can't silently erode.
- **Rendered everywhere:** Taxonomy Reference PDF (shaded "Why it matters" band under
  every attribute; now 30 pp), Template Creator (teal why-note under every slot; help
  overlay updated), Configurator (why appended to each guidance cell; recalc clean,
  159 formulas, 0 errors).
- **Deck 57 → 59 slides:** two REFERENCE evidence-map slides after the glossary — "Why
  each dial matters" for the generative criteria (slide 55) and the agentic criteria
  (slide 56), ten criteria classes each with effect-on-output + evidence columns. Slide
  26's tree caption and notes now name the layer.
- Citation style: compact tags on-slide/in-handout (e.g., "Sclar, ICLR 2024"); full URLs
  and as-of dates remain in notes/research/. Claims marked "practitioner consensus" or
  "field practice" where no strong study exists — nothing is dressed up as research that
  isn't.

## v1.5 (2026-09-09) — APPLIED: the review-cycle rebuild + worked-example packs

Owner said "update" after a full slide-by-slide review of Parts 1–3 (protocol: brainstorm
first, apply on "update"). Everything in `PENDING_CHANGES.md` Sections A–C was applied,
plus a mid-update owner request for two worked-example packs. Deck: 59 → **67 slides**,
render-QA'd. Highlights:

- **Part 1 (14 slides):** welcome retitled ("Ask, or delegate"), three-block map, no
  durations, multimodal aside; era cards with schematic mini-diagrams + named techs;
  time-to-100M chart; "deletes wrong guesses" thesis; LEGO token bricks; RAG
  "you already use this" strip; ladder + triage diagnostic; reasoning slide split into
  fast-vs-thinking + the feature menu (verified Sep-2026 mode names per vendor);
  hallucination split into four-kinds + hall of shame (4 locked incidents); P1 rep
  deleted. Eight PROMPT n/8 course-log chips (H.promptChip in deck_lib.js).
- **Part 2 (6 slides):** evidence-backed "known for" layer (ChatGPT-writes-better
  corrected); DeepSeek slide with MoE-on-slide + R1-vs-o1 chart (five pairs + 27× bill);
  servers/tiers/trust redesign (trust the tier, not the logo); gallery split into
  doers + specialist shelf (Manus, Notion Agents, Gemini Notebook, Granola, Gamma/Canva,
  Firefly, Lovable, ElevenLabs/DeepL; Stable Diffusion demoted with rationale); matrix
  and test-set slides retired.
- **Part 3 (12 slides):** elements rebuilt importance-first (what-you-get / why /
  evidence / weak→strong; Out + Stop are elements 6–7); taxonomy slide pulls forward;
  techniques split with a verbatim line to steal per card; evidence corner in plain
  terms; "Advice that expired" reframe; iteration = PDCA (Deming/Toyota; LEI's
  "Prompt-Do-Check-Act" cited) with the diagnosis grid as the Check step; rep rebuilt
  to explain itself.
- **Part 4 (12 slides):** untouched originals + owner-requested walkthroughs: AI data
  analysis end-to-end (4 slides: profile-first, correlations/comparisons, quotation
  normalization, ship-the-artifact) on a generated practice pack
  (`src/build_exercise_pack.py` → `deliverables/exercise-data/`: seeded 144-row dataset
  with planted TOTAL-row + "n/a" quirks; three trap-laden quotation PDFs; a 10-message
  email thread with four planted traps); email-summarization walkthrough (2 slides:
  five shapes + Copilot mechanics/sequence); future-plays menu.
- **Ripples only in Parts 5–6/close:** promotion-ladder qualifiers; glossary 17 → 19
  (both ladders defined).
- All speaker notes on touched slides use the spaced template (HOW TO PRESENT / BRIDGE /
  TRY IT / ACRONYMS / CONTENT, one item per line).
- New research: r11–r16 (trust/servers · tools · reputations+R1 · incidents ·
  per-element evidence · email summarization), all dated 2026-09-09.
- Still open (PENDING_CHANGES.md Section G): Parts 5–6 owner review; reps in 3/5/6
  survive until reviewed; triage drill has six problems (trim to four if asked); final
  prompt numbering confirmed n/8; Part-4 pointer notes still say the old session split
  (owner froze Part 4 content mid-review).

## v1.6 (2026-09-09) — APPLIED: the five-round audit-and-polish pass + closing slides

Owner reviewed the v1.5 deck slide-by-slide in five rounds (all held in PENDING_CHANGES.md
per protocol), then triggered: "Slide 44: Delete… Slide 45: Update… Then update all the
changes. Go ahead with the defaults." Deck stays at **67 slides** (two deleted, two new),
render-QA'd. Highlights:

- **Prompt system rebuilt (R10/R11):** `H.promptChip` v2 renders numbered STEP rows —
  "TYPE THIS →" (Consolas) + "WHY →" (one italic line) — and a "✂ copy-paste, don't
  retype: tab X of your Course Workbook" footer. Every chip call site rewritten with the
  final Round-2 texts. The exercise pack output is now **Course_Workbook.xlsx**
  (README + Data + tabs EX1-TwoModes…EX8-MoE, G2-DataAnalysis, EX-Quotes, EX-Email,
  EX-Rebuild + PLAYBOOK with the full 8+8+8) plus **Playbook_One_Pager.pdf**.
- **Part 1:** S4 era "gave us" outcome lines (verified only); S5 Attention-title
  explainer in notes; S6 web-search/RAG escape hatches + after-ship RLHF; S13 rebuilt as
  four named character cards; counters dropped deck-wide (R13: "· continued").
- **Part 2:** S16 rebuilt as 2×3 identity trading cards with real product logos
  (assertion-evidence, r19; Perplexity leads with CJR 37%-vs-67% per audit H3); S17 big
  bill ($60 vs $2.19, true-proportion bars, 27× badge) + drawn MoE hospital + compressed
  3-row benchmark chart; S18 data-type × tier matrix (PII row) + logos; S19/20 logos +
  Manus/Sora dates. Logo pipeline: `src/fetch_logos.py` → `src/assets/logos/` (favicons;
  `H.logo` falls back to a drawn monogram).
- **Part 3:** S22 rebuilt around the drawn "body of a prompt" figure (7 organs; vendor
  panel to notes; industry-as-context flagged); S26 purpose/origin; S27/28 purpose
  frames; S29 aesthetic pass + hero +49%; S30 rebuilt as the three-column Do/Don't/
  Expired playbook (top-5 each; full lists in the PLAYBOOK tab; r20); S31 drawn PDCA
  wheel + Toyota mark + Deming named card; S32 rep now carries the 60-word report
  excerpt + two R10 steps (tab EX-Rebuild).
- **Part 4:** S34 rebuilt as a document mock with side-car whys; S35 vertical ①②③ flow;
  S36–38 numbered-banner family (`H.stepBig`); blind-critique demo slide DELETED (salvage
  → S29 notes); dashboard demo + capability strip (Claude/ChatGPT/Gemini canvas tools,
  typically paid; Copilot chat can't; fallback spec→IT/Excel); S41 gains a stylized
  3-panel Outlook mockup strip (labeled illustration); playbook-pointer slide DELETED
  (pack rundown + handoff homework → future-plays notes, which now closes Block 2).
- **Part 5 opener** rebuilt as "Block 3 · where we left off" (body anatomy, playbook,
  evidence rules, Course-Workbook take-home; homework = the handoff move).
- **Close:** two new conclusion slides (owner request): "They're called requirements"
  (Stellman/Grove/Spec Kit; user story · Given-When-Then · ISO 29148 mapped onto the
  anatomy; 41.1% callback) and "The best prompt is a question" (95%-confidence flip +
  ClarifyGPT numbers; Five Whys/funnel/Socratic toolkit; Altman + Picasso-1964 quotes,
  attribution-checked). Einstein/Voltaire misattributions explicitly barred in notes.
- **All 22 audit findings fixed** (see AUDIT_v1.5_parts1-3.md status header).
- New research: r17–r21 (explainer prompts · mode names · slide design · do/don't/
  expired · requirements↔prompts + questions), all dated 2026-09-09.
- Still open: Parts 5–6 + close owner review (slides 44–67); Section G open questions.

## v1.7 (2026-09-10) — APPLIED: Rounds 6–7 + the PDCA-toolkit decision (68 slides)

Owner reviewed Parts 1–3 again ahead of presenting; trigger: "fix formats and take
the feedback… focus on the ones I'm presenting tomorrow." Applied same-day: new
hardware slide (r22); S7 letter-counting currency fix + Grok mode row + abstain-vs-
guess chart (r23); prompts renumbered 1/7–7/7 (ladder chip cut; tabs renamed,
BONUS-Ladder added); S10 three-big-steps redesign; S18 server-geography map
(data-type matrix removed — company-policy territory); S20 → "what people actually
use" (r24); S22 stop-as-action; S23–25 two weak→strong pairs per element (Role as
personality requirements, Task + sequence); evidence corner split into proven-vs-
myth + the mirror/sycophancy slide (r25); R14 font floor pass. OWNER DECISION: the
toolkit is now STRUCTURED AS PDCA — one "toolkit is a loop" quadrant slide (methods
per phase, each with a delegate-it line) + "PDCA in practice" deep-dive; Template
Creator + taxonomy reference + cheat sheet all queued to mirror this framing next
session. Owner supplies generated imagery via notes/intake/ (R16); first batch
received in chat (map, body, one character) — awaiting files. New standing intent:
document this human+agent collaboration method as Part 5 teaching material (r26,
future). Rounds recorded in PENDING_CHANGES.md.

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
