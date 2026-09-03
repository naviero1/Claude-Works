# Fictiv 3DP Quote Comparison — V4

Tracking workbook for the supine chest / rib-cage 3DP part family (15 parts).
**Deliverable:** `Fictiv_Quote_Comparison_V4.xlsx`

## What changed from V3

V4 adds **Quote 5**, received and dated **September 3, 2026**, transcribed from a
3-page quote supplied as images. Nothing in the Q1–Q4 history was altered — every
V3 figure is carried through unchanged and re-verified.

| Tab | Change |
|---|---|
| `Sources` | Quote 5 row added above the Xometry reference, with its date, basis and tier structure. Intro rewritten for five quotes. |
| `Five-Quote Comparison` *(was `Four-Quote Comparison`)* | Q5 unit-price, extended and Δ Q4→Q5 columns added. Renamed; all cross-sheet references repointed. |
| `Quote 5 Detail` | **New.** As-quoted line items for both tiers, tier reconciliation, landed cost per part, and the three audit blocks. |
| `Summary` | Q5 headline total, Δ Q4→Q5, Δ Q1→Q5, landed totals, Q5-vs-Xometry, audit findings, and observations 7–12. |

## Quote 5 as quoted

Multi Jet Fusion (MJF) / Nylon 12 / Black / Vapor Smoothed / per 2D drawing and DFM.
China production, DAP shipping, 7.5% sales tax on parts.

| | Tier 1 | Tier 2 |
|---|---|---|
| Qty per part | 2 | 30 |
| Lead time | 26 business days | 45 business days |
| Parts subtotal | $23,929.48 | $161,523.60 |
| Freight (DAP) | $1,048.32 | $8,555.32 |
| **Landed total** | **$26,772.51** | **$182,193.19** |

**Transcription proof:** the 15 line items sum to the quote's own stated part-price
totals, and `parts × 1.075 + freight` reproduces both stated grand totals to the cent.
That arithmetic is reproduced live in the workbook (`Quote 5 Detail`, column I).

## Headline

Compared like-for-like — Q5's Tier 1 unit price against the workbook's established
Q2 quantity basis:

| Quote | Total (parts only, @ Q2 qty) |
|---|---|
| Q1 — AI original | $27,518.22 |
| Q2 — AI re-quote (Apr 23) | $11,101.20 |
| Q3 — MP w/ error (May 1) | $11,235.80 |
| Q4 — MP corrected (May 11) ★ | $10,394.00 |
| **Q5 — MJF China (Sep 3) ◆** | **$27,400.08** |

Q5 is **+163.6%** on Q4 and **−0.4%** on Q1 — at prototype volume the pricing has
returned to where the original AI quote started. Against the Xometry benchmark
($8,915.44) Q5 sits **+207%**.

## Audit findings

1. **The volume discount is a flat multiplier.** Every Tier-2 price is exactly 45.00%
   of its Tier-1 price; the spread across all 15 parts is effectively zero. Real
   volume economics would vary part by part (nesting, part height, post-processing
   labour). This is pricing policy layered on top — so it is negotiable, and a
   mid-tier (qty 5–10) is worth asking for rather than jumping 2 → 30.
2. **13 of 15 Tier-1 prices back-solve to a round-dollar base at an 85% divisor**
   ($200, $260, $280, $300, $375, $1,000, $1,100, $1,150, $1,480, $1,850 …),
   implying a round internal cost with 15% margin on top. The two exceptions are
   **670832 and 670833** — the same mirrored rim pair that carried the genuine MP
   discounts in Q3/Q4. Those two look hand-priced; the other 13 came off a rate card.
3. **Freight gives no leverage.** DAP freight is ~4.4% of parts subtotal at Tier 1
   and ~5.3% at Tier 2 — it scales with value rather than flattening. The case for
   Tier 2 rests on the part discount alone.

## Open items

- **Process parity is unverified.** Q5 is explicitly MJF / Nylon 12 / vapor smoothed.
  The workbook never recorded the process for Q1–Q4, and vapor smoothing is a real
  cost adder. Confirm the finish spec matches before treating Δ Q4→Q5 as a pure
  price move — if it does not, much of the jump is scope, not inflation.
- **The vendor is not named on the Q5 pages supplied.** Confirm the issuer before
  this row is cited internally as a Fictiv quote.
- Neither the Fictiv quotes nor Q5 include FAI / inspection; Q5 states explicitly
  that 3DP parts exclude the inspection report.
- Q5 lead times exclude the 9.25–9.27 and 10.1–10.7 holiday periods. Both fall
  inside a 26- or 45-business-day window starting Sep 3, so the delivery dates land
  later than the raw day counts suggest.

## Modelling assumptions

Documented in-sheet on `Quote 5 Detail` (rows 68+), and editable:

| Assumption | Cell | Basis |
|---|---|---|
| 7.5% tax applies to parts only, not freight | `B7` | Confirmed — it is what makes both stated grand totals reconcile exactly |
| DAP freight allocated pro-rata by part value | — | Modelling choice; the quote gives one freight figure per tier, not per part |
| 0.85 back-solve divisor | `B8` | Inferred from the data, not quoted. Change `B8` to test other margin assumptions; column K re-tests every part |

Yellow cells on `Quote 5 Detail` are the as-quoted inputs; everything else is a formula.
Q5 unit prices on the comparison tab pull from `Quote 5 Detail!E19:E33`, so corrections
only need making in one place.

## Reproducing

```
pip install openpyxl
cd src
python build_v4.py && python build_summary_v4.py   # reads V3, writes V4
python /path/to/xlsx-skill/scripts/recalc.py ../Fictiv_Quote_Comparison_V4.xlsx 400
python verify_v4.py                                # independent checks
```

The recalc step is required: openpyxl writes formulas with no cached values, so
without it every formula cell reads back as empty to anything that reads cached
values. It needs **`libreoffice-calc`** installed, not just `libreoffice-core` —
core alone has no spreadsheet import filter and fails with "source file could not
be loaded" (or hangs). `apt-get install libreoffice-calc`.

Last verified: 495 formulas, 0 errors; all Q1-Q4 and Xometry figures byte-identical
to V3; both Q5 tier totals reconciling to the cent.

`q5_data.py` holds the Quote 5 transcription, kept separate so it can be diffed
against the source quote line by line.
