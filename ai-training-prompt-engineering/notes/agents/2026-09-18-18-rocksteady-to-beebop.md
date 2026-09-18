# Rocksteady → Beebop: integration v06 — restored slides moved into the opening block

Date: 2026-09-18. Explains the v06 integration build (`src/build_integration_v06.py`, deck `notes/visual-polish/pilot/From_Prompts_to_Agents_Visual_Pilot_v06.pptx`), posted at Oscar's direct instruction ("state what you did and why", and today: "tell beebop of the changes we found").

## Why

Two owner corrections in session, both about placement:

1. The restored classics were sitting in the appendix (v03–v05 positions 104–111). Oscar: they must be **in the final deck's main flow** — appendix placement did not satisfy "put them in the deck".
2. My first integration draft placed the vehicle slide at 52 and the context-failures slide at 60, at their thematic homes in Parts 5–6. Oscar rejected that before it shipped: *"I need them within the first slides, I am not going to make it to those slides in the first training."* The first session only reaches the early deck, so every restored slide he values must sit in the opening stretch.

## What was done

v06 = v05 reordered to 109 slides. All eight restored classics now sit within the first 23:

| New pos | Slide | Origin |
|---|---|---|
| 4 | Four eras: rules → learning → generative → agentic | rich original (replaces summarized live 4, dropped) |
| 6 | The hardware story — chips, Nvidia, data centers | rich original (replaces summarized live 6, dropped) |
| 16 | Fluency is not evidence | original 14 |
| 17 | Real, public, verified — and all avoidable (hall of shame) | original 15 |
| 18 | The flattery bias — measured, and all over the news | original 29 |
| 21 | Pick by task, not habit — September 2026 | original 17 |
| 22 | Chat, workflow, or agent — the path decides | rebuild in house idiom |
| 23 | Four context failures — name it, then cure it | rebuild in house idiom |

Everything else keeps its v05 relative order (live 18–103 shift +6). Machinery, all in the deterministic builder: sldIdLst reorder; the two superseded twins properly dropped (`drop_rel`); every `page-number` shape renumbered; every textual "slide N" cross-reference remapped in visible text **and** speaker notes via the old→new map (44 remaps this run, list printed by the builder); integrated slides' appendix footers swapped for the live footer.

## The defects we found and fixed (folded into the builder)

1. **Historical quote over-remap.** The reference remapper initially renumbered the owner's frozen v1.10 CONSOLIDATION quotes inside speaker notes ("slides 28, 29 and 33" → mangled). Historical quotes are records of past decisions, not live references — the builder now skips any run containing the v1.10 marker. Verified verbatim-intact on the two carrying slides (now 34 and 85).
2. **Leftover appendix footers.** Integrated slides initially kept "DETAILED REFERENCE · Restored classic · Related live slide N" footers — self-referential once the slide IS the live slide. The builder now replaces them with the live footer on every integrated slide while leaving genuine appendix reference pages untouched.
3. **The placement lesson itself**, twice over: appendix ≠ "in the deck", and thematically-correct late positions ≠ usable — the facilitator's actual first-session reach governs placement. Recorded so neither of us re-litigates it.

## Verification

109 slides; titles at 4/6/16–18/21–23 machine-checked; zero "Restored classic" strings and zero appendix footers anywhere in the live zone; every page-number shape equals its position; v1.10 quotes verbatim; full-deck render clean. Deck delivered to Oscar with a first-24-slides contact sheet; committed on the working branch.

## Impact on your instruction 13 (still pending Oscar's go)

Positions have moved: the speaker-notes gap you flagged now applies to slides **4, 6, 16, 17, 18, 21, 22, 23**. Source notes for the six ported slides live in the preserved original (old 4, 6, 14, 15, 29, 17); slides 22–23 are rebuilds and need authored notes. One open item flagged to Oscar (his call, not blocking): the integrated slides still carry the "REFERENCE STUDY" top chrome from their appendix build even though they now sit in the taught flow.

Deck files stay in the private repo per standing rule. Your graph recommendations and first Nano Banana prompt batch should target the v06 numbering above.
