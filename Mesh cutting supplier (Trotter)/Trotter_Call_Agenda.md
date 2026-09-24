# Trotter — Call Agenda & Question Sheet
**6-Month Outlook & Replenishment Cycle Review · 24 × 27 in cut mesh**

| | |
|---|---|
| **Supplier** | Trotter — slits the 750 ft × 101 in roll and cuts 24 × 27 in pieces |
| **Date** | Thu 24 Sep 2026, afternoon  **Contacts:** __________ (+ Todd, production) |
| **Their framing** | "Review the 6-month outlook schedule, ensuring it aligns with our standard 2-week turnaround" |
| **Their data point** | Last PO: 1,300 pcs of 24×27 took ~1 day to cut, including slitting |
| **Our situation** | Count today: **937 pcs** (70 loose + 2 boxes of ~433) — **below the 1,080 reorder point** → PO-0 releases today |
| **Workbook** | `Mesh_Maths_Production.xlsx` → tabs **Cycle Time** (type answers in column D), **PO Schedule**, **6-Month Forecast** |

**One-line context for them:** We pull one roll (1,300 pcs) about every 5 weeks — 11 rolls a year, ~11 cutting days of your time. We plan to your standard 2 weeks; today we want the legs of the cycle precisely, the six PO dates checked, and one expedited first roll.

**Posture:** collaborative — they thanked us for streamlining. We are **not** negotiating the 2 weeks down (it costs us ~$16/yr in extra stock to plan to it). 270 pcs/week is *our* assumption to confirm internally, not theirs.

---

## A. PO-0 — TODAY *(the one ask that matters)*
1. We release PO-0 (one roll, 1,300 pcs) today. At the standard chain it lands on our shelf **Mon 19 Oct — the day we run out**. Can you cut it in the **first available slot** (target ship ≈ Fri 2 Oct)? ☐ Y ☐ N — earliest ship: _______
2. Is a 750 ft roll available now, or does it need to be ordered? _______
3. Partial shipment OK if you cut in two runs? _______

## B. LEG 1 — Roll gets to Trotter *(we assume 3 days)*
4. Who orders the roll — you or us — and from where? _______
5. Roll **held in stock** at Trotter or ordered per PO? Door-to-door days: _______
6. Could the **next roll be pre-positioned** at your dock (removes this leg from every cycle)? _______
7. How quickly is a PO acknowledged? _______

## C. LEG 2 — Receive & queue *(we assume 12 days; this is where the "2 weeks" lives)*
8. When does your 2-week clock start — **PO receipt or roll receipt**? _______
9. 2 weeks = **10 business days or 14 calendar days**? _______
10. Realistic wait to slot a 1-day job? Any fixed cutting days? _______
11. Incoming inspection of rolls (width, defects)? Hold time before release to the floor? _______
12. **Plant shutdowns:** Thanksgiving (26–27 Nov)? Christmas–New Year (24 Dec–1 Jan)? Other: _______

## D. LEG 3 — Slit, cut & pack *(1-day cut confirmed; we assume +1 day to pack)*
13. Pieces per box/bundle? **Piece count on the label?** (1,300 ÷ 3 boxes is not a whole number — our count is ±1) _______
14. Count verification before shipping? _______
15. Same-day carrier pickup or next day? _______
16. Is **1,300 the full yield of a roll, or the PO quantity** with remnant left over? Should the PO read "one full roll (≈1,300)"? _______
17. Expect ~1,300 good pieces per roll again? Scrap / short-piece handling? _______

## E. LEG 4 — Ship to us *(we assume 2 days transit + 1 day our receiving)*
18. Carrier, service level, typical transit days? _______
19. Ship terms — who books and pays freight? _______
20. Ship notice with piece count + tracking? _______

## F. The six PO dates *(PO Schedule tab — dates move with whatever we confirm)*
| PO | Release (Mon) | Roll due at Trotter | Cut week | Latest ship | On our shelf | Flag |
|---|---|---|---|---|---|---|
| PO-0 | Thu 24 Sep | 28 Sep | 12 Oct | 16 Oct | 19 Oct | **lands the day we run out → expedite** |
| PO-1 | 19 Oct | 22 Oct | 2 Nov | 6 Nov | 10 Nov | — |
| PO-2 | 23 Nov | 26 Nov | 7 Dec | 11 Dec | 15 Dec | roll due on Thanksgiving |
| PO-3 | 28 Dec | 31 Dec | 11 Jan | 15 Jan | 19 Jan | Christmas–New Year |
| PO-4 | 1 Feb | 4 Feb | 15 Feb | 19 Feb | 23 Feb | — |
| PO-5 | 8 Mar | 11 Mar | 22 Mar | 26 Mar | 30 Mar | — |

21. Each release gives you ~15 days from roll arrival to latest ship (1 day inside the standard). Any of these weeks a problem? _______
22. Pull PO-2 / PO-3 releases forward a week for the holidays? ☐ Y ☐ N

## G. Mechanics now that you're onboarded
23. Discrete PO per roll (~every 5 weeks) or a blanket PO with dated releases? _______
24. **Expedite path** for rare cases: notice needed, realistic fastest PO→ship, any charge? _______
25. Who buys the raw roll (decides whether we need a raw-roll part number in SAP)? _______

---

**After the call:** type the confirmed days into **Cycle Time!D12:D28** and switch **Cycle Time!B5** to *Confirmed on call*. Inputs, Order Cadence, the 6-Month Forecast and PO Schedule recalc. Then set SAP: reorder point 1,080 · fixed lot 1,300 · safety stock 270 · planned delivery time = Cycle Time row 36 · GR processing time = row 37. Send the follow-up email with the agreed legs and PO calendar.
