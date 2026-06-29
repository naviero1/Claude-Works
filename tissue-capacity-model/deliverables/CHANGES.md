# Deliverables — flat-250 pelvic attainment

Updated copies of two source files. Originals remain untouched in [`../source-files/`](../source-files/).

Scope, as instructed: **only 666506 (Pelvic Block Non-Intact) and 666541 (Female Pelvic), at Martin.**

## `Weekly_goals_2026_SUMMARY_062426.xlsx`
- **New tab added: `Attainment @250 (Pelvics)`.** Mirrors the `Attainment & Allocations` per-tissue logic but forces the **Ask to a flat 250** for every period and recomputes `% = Attained ÷ 250`.
  - *Biweekly block* (rows 5–17) — the 12 points that feed slide 2.
  - *Weekly detail* (rows 20+) — every week for each pelvic, with Ask hard-set to 250.
- The tab was **injected surgically** (added as a single new worksheet part); all **18 existing charts** and every other sheet are preserved byte-for-byte. The file was *not* re-saved through a library that would strip them.

## `Tissue_Capacity_2026_2027.pptx`
- **Slide 2 chart** re-pointed to the flat-250 series:
  - Female Pelvic (541's): `48, 56, 52, 54, 87, 115, 62, 108, 86, 69, 79, 49`
  - Pelvic Block (506's): `40, 7, 32, 13, 40, 15, 4, 17, 55, 54, 41, 29`
  - "Ask (100%)" line kept — it now represents the **250/wk standard**.
- **Fixed the mislabeled series:** "Female Pelvic (506's)" → **"Pelvic Block (506's)"** (666506 is Pelvic Block, not Female Pelvic).
- **Text made consistent with the new basis:** chart title "vs ASK" → "vs 250/WK STANDARD"; footnote "harvested ÷ ask" → "harvested ÷ 250/wk flat ask"; the sticky note "Add 250 as denominator" → "✓ 250 denominator applied".

## How the denominator was applied
Each biweekly point sums two weeks of **Attained** and divides by **500** (= 250/week × 2 weeks), matching the chart's existing biweekly cadence. On the weekly detail tab each single week is `Attained ÷ 250`. (Biweekly % is just the average of its two weekly %s — internally consistent.)

> Reads differently on purpose: against a flat 250 both pelvics sit **mostly below the 100% line** all year, instead of bouncing around their own moving ask. That's the apples-to-apples view you asked for.
