# Pratt Richmond → KWE Sterling (VA) — Order Cadence & Restock Plan

**Scope:** Custom box (OD 24×16×18) + 2" recycled-paper insulation (Part A / Part B, Chillin Liners / MP Global) from Pratt Industries, Richmond VA → KWE warehouse, Sterling VA.
**Usage rate:** 100 boxes/month (assumed = 100 boxes + 100 Part A + 100 Part B, i.e. 1 insulation set per box).
**Prepared:** July 8, 2026. Calendar dates below assume the first PO goes to Pratt this week and usage starts ~Aug 1 — shift everything if kickoff slips.

---

## TL;DR — the answers

**How much, how often?**
- **Insulation (Part A + B):** Buy the 15-pallet MOQ (500 A / 450 B) and have **Pratt hold it in Richmond** (they've agreed to hold insulation only). Pull it over in small biweekly transfers instead of cramming it into KWE.
- **Transfer truck Richmond → Sterling every 2 weeks**, averaging 2–3 pallets. Per month that works out to **2 pallets of Part A (100 units) + 1 pallet of Part B (90 units)**, with one extra B pallet every ~9 months (B pallets hold 90 but you use 100/month).
- **Boxes:** Pratt won't hold boxes, so order **175 boxes (2 pallets) about every 7½ weeks** — 7 orders/year. Place each box PO 2 weeks ahead (their quoted lead time), when KWE on-hand drops to ~135 boxes.

**When do we need to be restocked from Pratt (new production runs)?**
- Each MOQ buy covers ~4.5–5 months of Part B (the binding part at 100/month usage). Place a **new MOQ PO with Pratt roughly every 4.5–5 months** — in year 1: **now (PO-1), ~early September (PO-2), ~mid-February (PO-3)**, with PO-4 due ~early July. That's 3 insulation POs in the first 12 months.

**Why this shape?** 100 boxes/month burns ~4.3 pallets/month of material (2.0 plt A + 1.1 plt B + ~1.15 plt boxes). If KWE really can only hold ~6 pallets, that's only ~5–6 weeks of total coverage on the floor — so KWE has to run lean (~2-week buffers) and the Richmond hold is your real safety stock. Frequent small transfers are what make the 6-pallet cap workable.

---

## Reference data (from Pratt quote)

| Item | Price | Pack-out | Order rules |
|---|---|---|---|
| Custom box OD 24×16×18 | $5.50 ea | ~80–90/pallet (175 = 2 pallets) | Order qty 175, 2-week lead. Pratt will **not** hold. |
| Insulation set (A+B) | $11.60/set | Part A: 50/pallet · Part B: 90/pallet | MOQ 15 pallets = 10 plt A (500) + 5 plt B (450). Pratt holds in Richmond. |
| Sub-MOQ option | +$400/order | — | Min 4 plt A (200) + 3 plt B (270). |
| Holding fee (Pratt) | **TBD** — requested 7/7 | — | Insulation only. |
| Delivery Richmond→Sterling | **TBD** — not yet shared | — | — |

KWE Sterling capacity: **~6 pallets (unconfirmed — "my guess, need to confirm").**

---

## Operating rules (steady state)

A truck comes from Richmond every 2 weeks. What goes on it is decided by simple reorder points at KWE:

| Part | Add to truck when KWE on-hand is… | Quantity | Effective cadence |
|---|---|---|---|
| Part A | ≤ 60 units (≤ 25 → send 2 pallets) | 1 pallet (50) | ~every truck; 2 plt/month avg, 24 plt/year |
| Part B | ≤ 75 units | 1 pallet (90) | ~every other truck; ~13–14 plt/year |
| Boxes | Projected ≤ 90 at next truck (≈ on-hand ≤ 135 today) → place PO now (2-wk lead) | 175 (2 pallets) | every ~7½ weeks; 7 POs/year |
| **New Pratt MOQ PO** | **Richmond hold ≤ 180 units of B (2 pallets)** | MOQ 15 plt | every ~4.5–5 months (~3/year) |

The Pratt-PO trigger assumes ~4 weeks production lead for insulation (unconfirmed — boxes are quoted at 2 weeks). If Pratt's insulation lead is longer, raise the trigger accordingly.

**MOQ mix suggestion:** the standard 10 A / 5 B mix (500/450) over-buys A by 50 units per PO if usage is truly 1:1. Ask Pratt to alternate the 15-pallet mix — **10A/5B, then 9A/6B (450 A / 540 B)** — which keeps A and B balanced and avoids surplus A piling up in Richmond and accruing holding fees.

---

## First-6-months calendar (dates = week of; validated by simulation)

| Date | Action / delivery to KWE | Pallets in | Notes |
|---|---|---|---|
| **Jul 8** | Place **PO-1** with Pratt: MOQ insulation (500 A / 450 B, hold in Richmond) + 175 boxes | — | Also send the open questions below |
| **Jul 22** | **Go-live delivery:** 175 boxes + 2 plt A (100) + 1 plt B (90) | 5 | KWE at 5 positions on day one |
| Aug 5 | — (no truck needed) | 0 | |
| Aug 19 | 1 plt A + 1 plt B | 2 | Place box PO #2 |
| **Sep 2** | 1 plt A + 1 plt B + 175 boxes | 4 | **Place PO-2 with Pratt** (request 9A/6B mix) |
| Sep 16 | 1 plt A | 1 | |
| Sep 30 | 1 plt A + 1 plt B | 2 | PO-2 stock lands in Richmond ~now |
| Oct 14 | 1 plt A | 1 | Place box PO #3 |
| Oct 28 | 1 plt B + 175 boxes | 3 | |
| Nov 11 | 2 plt A | 2 | |
| Nov 25 | 1 plt B | 1 | |
| Dec 9 | 2 plt A | 2 | Place box PO #4 |
| Dec 23 | 1 plt B + 175 boxes | 3 | |
| Jan 6 | 1 plt A | 1 | |
| Jan 20 | 1 plt A + 1 plt B | 2 | Place box PO #5 |

Continuing pattern for the rest of year 1: box deliveries ~Feb 3, Mar 31, May 26, Jul 21; **PO-3 with Pratt ~Feb 17** (in stock mid-March), PO-4 ~early July.

**KWE occupancy through the year:** typically **4–6 pallet positions**, with brief peaks of 7–8 on heavy delivery days (when a 2-pallet box drop coincides with insulation). Mitigations: consolidate partial pallets (these are light paper-insulation and half-used box pallets — easy to re-stack), or split heavy trucks into two lighter ones a week apart. This is the single point to clear with KWE (see open questions). Note Part A occasionally dips to ~15 units (<1 week of cover) just before its truck arrives — if that feels thin, raise the A trigger to 70, at the cost of one more pallet position at peak.

---

## Cost picture (materials only — freight & holding TBD)

| | Monthly | Annual | Per PO |
|---|---|---|---|
| Boxes (100 × $5.50) | $550 | $6,600 | $962.50 per 175-box PO |
| Insulation (100 sets × $11.60) | $1,160 | $13,920 | ~$5,220–5,800 per MOQ PO (~450–500 sets; billing basis needs confirming) |
| **Total materials** | **$1,710** | **$20,520** | ≈ **$17.10 per shipped box** |

Still unpriced: freight per Richmond→Sterling truck (~26 trucks/year on the biweekly cadence — this decides biweekly vs monthly), and Pratt's insulation holding fee (requested 7/7). The $400 sub-MOQ option is a fallback only: using it ~5–6×/year adds ~$2,000–2,400 (~17% on insulation spend), so it only makes sense if Pratt's holding fees turn out steep.

---

## Fallback: monthly truck (if freight cost dominates)

If per-trip freight is high and KWE can flex to ~8 positions (or reliably consolidate partials), collapse to **one truck per month: 2 plt A + 1 plt B**, with boxes riding along whenever due, and 2 plt B in month 1 and ~every 9th month. Same annual volumes, half the trips — but simulation shows KWE peaks at 7–9 positions on delivery weeks and Part A buffer drops to ~zero between trucks, so this needs KWE's confirmed flexibility plus a one-time extra A pallet (safety build) in month 2.

---

## What we still need (open questions)

**For Pratt:**
1. Holding fee for insulation in Richmond (requested 7/7 — chase if not back this week).
2. Freight cost & minimums Richmond→Sterling — per trip or per pallet? Can boxes ride the insulation transfer truck to share freight?
3. Production lead time for an MOQ insulation run (model assumes 4 weeks; boxes are 2 weeks).
4. Notice required to release/ship pallets from the Richmond hold (model assumes ≤2 weeks).
5. Can the 15-pallet MOQ mix flex (e.g. 9 A / 6 B) to match 1:1 usage?
6. Billing: does $11.60/set = one Part A + one Part B? How are unmatched units (the extra 50 A per standard MOQ) billed?

**For KWE:**
7. Confirm the ~6-pallet figure — hard position count or approximate floor space? Can partial pallets be consolidated/double-stacked? OK to peak at 7–8 positions for a day or two around deliveries?

**Internal:**
8. Confirm usage really is 1 box + 1 A + 1 B per unit shipped, and whether any existing Sterling stock offsets the go-live order.
9. If usage grows past ~150/month, the 6-pallet cap drops below 4 weeks of coverage → move to weekly transfers or renegotiate KWE space.

---

*Numbers validated with a daily inventory simulation (`restock_simulation.py` in this folder) covering Jul 2026–Jul 2027: no stockouts, box on-hand never below ~2 weeks, Richmond hold never runs dry, 3 Pratt POs in year 1.*
