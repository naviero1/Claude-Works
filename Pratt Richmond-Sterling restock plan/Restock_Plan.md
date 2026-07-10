# Pratt Richmond → KWE Sterling (VA) — Order Cadence & Restock Plan

**Rev B — July 9, 2026.** Updated for Pratt's clarification that deliveries to KWE come in **fixed increments per part** (two options below), and that **KWE warehouse space is unknown** — the ~6-pallet figure used in Rev A was our own unconfirmed guess. This revision reports how much space each option *requires*, so we know what to ask KWE for.

**Scope:** Custom box (24×16×18 ID) + 2" recycled-paper insulation (Part A / Part B, Chillin Liners / MP Global) from Pratt Industries, Richmond VA → KWE warehouse, Sterling VA.
**Usage:** 100 boxes/month (assumed = 100 boxes + 100 Part A + 100 Part B).
Dates assume PO-1 goes out the week of Jul 8 and usage starts ~Aug 1 — shift everything if kickoff slips.

---

## TL;DR — the answers

**How deliveries work now (per Pratt):** each part arrives in a fixed increment, on its own cadence:

| | Option 1 — as quoted | Option 2 — adjusted |
|---|---|---|
| Boxes | 175 per drop (2 pallets) | 250 per drop (3 pallets) |
| Part A | 200 per drop (4 pallets of 50) | 250 per drop (5 pallets of 50) |
| Part B | 180 per drop (2 pallets of 90) | 270 per drop (3 pallets of 90) |

**How often (at 100/month):**
- **Option 1:** Part A every ~2 months, Part B every ~1.8 months, boxes every ~7½ weeks → ~21 deliveries/year (7+7+7), many combinable onto shared trucks when dates align.
- **Option 2:** every part every ~2.5–2.7 months → ~12 deliveries/year (4+4+4).

**When do we get restocked from Pratt (new MOQ production runs)?** ~Every 4.5 months either way — **3 POs in year 1: now, ~late October (Opt 1) / mid-November (Opt 2), ~mid-March / mid-April.** Trigger: place the next MOQ when total insulation runway (Sterling + Richmond hold) drops to ~7 weeks.

**The decision gate is KWE space** (simulated, no stockouts in either option):

| | Option 1 | Option 2 |
|---|---|---|
| Go-live footprint (all three first drops) | **8 pallets** | **11 pallets** |
| Average standing occupancy | ~7 pallets | ~9 pallets |
| Worst receipt-day peak | 11 pallets | 14 pallets |
| Ask KWE for | **~8 standing, 11 on receipt days** | **~11 standing, 14 on receipt days** |

If KWE can only give us **~6ish pallets**, neither option fits as-is. The lever: ask Pratt to release **Part A in 2-pallet (100-unit) drops** — A is the space hog (only 50/pallet, so a 200-unit drop = 4 positions) — and stagger the three parts' deliveries. That brings the need down to ~6–7 positions. Note a 100-unit A release already happens naturally as each MOQ's final partial drop, so it's physically possible.

**Recommendation:** Option 1, unless KWE space turns out generous *and* freight is priced per trip (then Option 2's ~12 drops/year beats ~21). Confirm KWE space first; it decides.

---

## Reference data (Pratt quote + Jul 9 clarification)

| Item | Price | Pack-out | Order rules |
|---|---|---|---|
| Custom box 24×16×18 ID | $5.50 ea | 83/pallet per Pratt (but "2 pallets = 175"?) | Drop = 175 (Opt 1) or 250 (Opt 2), 2-week lead. Pratt will **not** hold boxes. |
| Insulation set (A+B) | $11.60/set | Part A: 50/pallet · Part B: 90/pallet | MOQ 15 pallets = 500 A / 450 B (Opt 1) or 500 A / 540 B (Opt 2 = 2 full drops of each). Pratt holds in Richmond, releases in drops. |
| Sub-MOQ option | +$400/order | — | Min 4 plt A (200) + 3 plt B (270). Fallback only. |
| Holding fee (Pratt) | **TBD** — requested 7/7 | — | Insulation only. |
| Freight Richmond→Sterling | **TBD** — not yet shared | — | Decides Option 1 vs 2 economics. |

**Data quirk to confirm with Pratt:** 2 pallets × 83 boxes = 166, not 175; 3 × 83 = 249, not 250. Which number governs billing and receiving?

KWE Sterling space: **unknown — not yet negotiated.** (Rev A's ~6-pallet cap was our internal guess, now superseded by "ask KWE what we can get".)

---

## Operating rules (reorder triggers)

Each part rides its own cadence. Place the order/release request when projected stock **at arrival** (2-week lead) hits ~2 weeks of cover (≈50 units):

| Part | Order/release when on-hand is… | Drop (Opt 1) | Cadence (Opt 1) |
|---|---|---|---|
| Part A | ≤ 96 units today (≈50 at arrival) | 200 (4 plt) | every ~2 months |
| Part B | ≤ 96 units today | 180 (2 plt) | every ~1.8 months |
| Boxes | ≤ 96 units today → place PO (2-wk production) | 175 (2 plt) | every ~7½ weeks |
| **New Pratt MOQ PO** | **total A or B runway (Sterling + Richmond) ≤ ~7 weeks** | MOQ 500 A / 450 B | every ~4.5 months (~3/year) |

Ask Pratt to **combine drops onto one truck** whenever release dates land within a few days of each other — the sim shows A+B or B+box frequently align.

**Balance note:** Option 1's MOQ is A-heavy for 1:1 usage (+50 A per MOQ ≈ +130 A/year accumulating at Pratt); Option 2's is slightly B-heavy (+40 B per MOQ). Worth asking Pratt to true-up the mix on every second or third MOQ.

---

## Year-1 calendar — Option 1 baseline (dates ≈, from simulation)

| Date | Event | Qty | Pallets in | Notes |
|---|---|---|---|---|
| **Jul 8** | **PO-1 → Pratt** | MOQ 500 A / 450 B + 175 boxes | — | MOQ held in Richmond |
| **Jul 22** | **Go-live delivery** | 200 A + 180 B + 175 boxes | **8** | Peak footprint — all three first drops |
| Aug 26 | Box PO #2 | 175 | — | |
| Sep 9 | Box delivery | 175 | 2 | |
| Sep 10 | Part B release | 180 | 2 | Richmond B after: 90 |
| Sep 16 | Part A release | 200 | 4 | Richmond A after: 100 |
| Oct 18 | Box PO #3 | 175 | — | |
| **Oct 28** | **PO-2 → Pratt** | MOQ 500 A / 450 B | — | In stock ~Nov 25 |
| Nov 1 | Box delivery | 175 | 2 | |
| Nov 4 | Part B release (partial) | 90 | 1 | Empties Richmond B |
| Nov 16 | Part A release (partial) | 100 | 2 | Empties Richmond A |
| Dec 9 | Part B release | 180 | 2 | From PO-2 stock |
| Dec 10 | Box PO #4 | 175 | — | |
| Dec 16 | Part A release | 200 | 4 | |
| Dec 24 | Box delivery | 175 | 2 | |
| Jan 25 | Part B release | 180 | 2 | |
| Feb 1 | Box PO #5 | 175 | — | |
| Feb 15 | Part A release + box delivery | 200 + 175 | 6 | Combine on one truck |
| **Mar 14** | **PO-3 → Pratt** | MOQ 500 A / 450 B | — | In stock ~Apr 11 |
| Mar 21 | Part B release (partial) | 90 | 1 | |
| Apr 10 | Box delivery | 175 | 2 | PO placed Mar 27 |
| Apr 17 / Apr 25 | Part A (partial 100) / Part B release | 100 / 180 | 2 / 2 | |
| May 18 | Part A release | 200 | 4 | |
| Jun 2 | Box delivery | 175 | 2 | PO placed May 19 |
| Jun 11 | Part B release | 180 | 2 | |
| Jul 18 / Jul 25 | Part A release / box delivery | 200 / 175 | 4 / 2 | PO-4 due ~mid-Jul |

Full machine-generated schedule: `Restock_Schedule_Year1.csv` (regenerated by `restock_simulation.py`; Option 2's equivalent prints in the sim output).

---

## Costs (materials only — freight & holding TBD)

| | Monthly | Annual | Per order |
|---|---|---|---|
| Boxes (100 × $5.50) | $550 | $6,600 | $962.50/drop (Opt 1) · $1,375/drop (Opt 2) |
| Insulation (100 sets × $11.60) | $1,160 | $13,920 | ~$5,220–5,800 per MOQ PO (billing basis TBC) |
| **Total materials** | **$1,710** | **$20,520** | ≈ **$17.10 per shipped box** |

Unit economics are identical across options; they differ in freight (21 vs 12 drops/year), space (8/11 vs 11/14 positions), and cash tied up in inventory (~2 months vs ~2.6 months on hand).

---

## What we still need (open questions)

**For KWE — the gating one:**
1. **How much space can we get?** Option 1 needs ~8 positions standing and up to 11 on receipt days; Option 2 needs ~11 and up to 14. If only ~6 is available, we need Pratt's smaller Part A drops (below). Also: can partial pallets be consolidated/double-stacked?

**For Pratt:**
2. Holding fee for insulation in Richmond (requested 7/7 — chase).
3. Freight cost & minimums Richmond→Sterling; can multiple parts share a truck when drop dates align?
4. If KWE space is tight: can Part A release in 2-pallet (100-unit) drops? (Already happens as each MOQ's final partial release.)
5. Box pallet math: 83/pallet × 2 = 166, quoted as 175 — which governs billing/receiving?
6. Production lead time for an MOQ run (model assumes 4 weeks) and notice for a release from the hold (assumes 2 weeks).
7. Billing of $11.60/set when A and B ship separately; can the MOQ mix be trued up periodically (Opt 1 runs +50 A per MOQ vs 1:1 usage)?

**Internal:**
8. Confirm usage = 1 box + 1 A + 1 B; net any existing Sterling stock off go-live.
9. If usage grows past ~150/month, re-run the model (`restock_simulation.py`) — cadences shorten and space needs rise.

---

*Both options validated with a daily inventory simulation (Jul 2026 – Jul 2027): no stockouts; 3 Pratt MOQ POs in year 1 either way.*
