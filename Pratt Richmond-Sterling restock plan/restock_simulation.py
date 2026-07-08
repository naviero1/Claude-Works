"""Daily inventory simulation for the Pratt Richmond -> KWE Sterling restock plan.

Validates the order cadence in Restock_Plan.md: biweekly transfer truck with
reorder-point triggers, box POs on a 2-week lead, and Pratt MOQ POs replenishing
the Richmond hold. Adjust the assumptions below and rerun to test scenarios
(e.g. higher usage, longer production lead, different triggers).

Run: python3 restock_simulation.py
"""
import math
from datetime import date, timedelta

# ---- Assumptions (edit these) ----
USAGE_PER_MONTH = 100          # boxes shipped/month; 1 box = 1 Part A + 1 Part B
BOX_PER_PLT = 87.5             # Pratt: 80-90 boxes/pallet, 175 = 2 pallets
A_PER_PLT = 50
B_PER_PLT = 90
BOX_ORDER_QTY = 175            # fixed order increment, 2-week lead
MOQ_STD = (500, 450)           # 10 plt A / 5 plt B
MOQ_ALT = (450, 540)           # 9 plt A / 6 plt B (proposed alternate mix)
INSULATION_LEAD_DAYS = 28      # assumed production lead for an MOQ run (unconfirmed)
TRUCK_INTERVAL_DAYS = 14       # Richmond -> Sterling transfer cadence

A_TRIGGER = 60                 # send 1 plt A when KWE on-hand <= this (2 plt if <= 25)
B_TRIGGER = 75                 # send 1 plt B when KWE on-hand <= this
BOX_NEXT_TRUCK_MIN = 90        # order boxes when projected on-hand at next truck <= this
RICHMOND_B_TRIGGER = 180       # place next Pratt MOQ PO when Richmond B <= this

FIRST_DELIVERY = date(2026, 7, 22)   # go-live: 175 boxes + 2 plt A + 1 plt B (5 positions)
USAGE_START = date(2026, 8, 1)
END = date(2027, 7, 31)
# ----------------------------------

daily = USAGE_PER_MONTH / 30.44
box, a, b = float(BOX_ORDER_QTY), 100.0, 90.0
rich_a, rich_b = MOQ_STD[0] - a, MOQ_STD[1] - b   # PO-1 held in Richmond

pending_po = None      # (arrival_date, qty_a, qty_b, placed_date)
po_log = []
box_order_next = False
trucks, loads, alerts = [], [], []
t = FIRST_DELIVERY + timedelta(days=TRUCK_INTERVAL_DAYS)
while t <= END:
    trucks.append(t)
    t += timedelta(days=TRUCK_INTERVAL_DAYS)

rows, month_key, month_peak, month_min = [], None, 0, None
d = FIRST_DELIVERY
while d <= END:
    if pending_po and d == pending_po[0]:
        rich_a += pending_po[1]
        rich_b += pending_po[2]
        po_log.append(pending_po)
        pending_po = None
    if d in trucks:
        la = 100 if a <= 25 else (50 if a <= A_TRIGGER else 0)
        lb = 90 if b <= B_TRIGGER else 0
        lbox = BOX_ORDER_QTY if box_order_next else 0
        box_order_next = False
        a += la; b += lb; box += lbox
        rich_a -= la; rich_b -= lb
        if la or lb or lbox:
            plt = math.ceil(la / A_PER_PLT) + math.ceil(lb / B_PER_PLT) + math.ceil(lbox / BOX_PER_PLT)
            loads.append((d, la, lb, lbox, plt, rich_a, rich_b))
        if box - daily * TRUCK_INTERVAL_DAYS <= BOX_NEXT_TRUCK_MIN:
            box_order_next = True   # PO placed today, arrives on next truck (2-wk lead)
        if pending_po is None and rich_b <= RICHMOND_B_TRIGGER:
            mix = MOQ_ALT if len(po_log) % 2 == 0 else MOQ_STD   # PO-2 alt, PO-3 std, ...
            pending_po = (d + timedelta(days=INSULATION_LEAD_DAYS), mix[0], mix[1], d)
    if d >= USAGE_START:
        box -= daily; a -= daily; b -= daily
    if min(box, a, b) < -0.5:
        alerts.append(f"{d} STOCKOUT box={box:.0f} A={a:.0f} B={b:.0f}")
    if rich_a < -0.5 or rich_b < -0.5:
        alerts.append(f"{d} RICHMOND SHORT A={rich_a:.0f} B={rich_b:.0f}")
    pos = (math.ceil(max(box, 0) / BOX_PER_PLT) + math.ceil(max(a, 0) / A_PER_PLT)
           + math.ceil(max(b, 0) / B_PER_PLT))
    mk = (d.year, d.month)
    if mk != month_key:
        if month_key:
            rows.append((month_key, month_peak, month_min))
        month_key, month_peak, month_min = mk, pos, (box, a, b)
    month_peak = max(month_peak, pos)
    month_min = tuple(min(x, y) for x, y in zip(month_min, (box, a, b)))
    d += timedelta(days=1)
rows.append((month_key, month_peak, month_min))

print(f"Go-live {FIRST_DELIVERY}: 175 boxes + 100 A + 90 B (5 pallet positions)\n")
print("=== Truck deliveries (units of A / B / boxes -> pallets; Richmond hold after) ===")
for dt, la, lb, lbox, plt, ra, rb in loads:
    print(f"{dt}  A={la:3d} B={lb:3d} box={lbox:3d}  {plt} plt   Richmond {ra:4.0f}A/{rb:4.0f}B")
print("\n=== Pratt MOQ POs (Richmond hold replenishment) ===")
print(f"placed 2026-07-08 -> in stock {FIRST_DELIVERY}: {MOQ_STD[0]}A/{MOQ_STD[1]}B  (PO-1)")
for arr, qa, qb, placed in po_log:
    print(f"placed {placed} -> in stock {arr}: {qa}A/{qb}B")
if pending_po:
    print(f"placed {pending_po[3]} -> in stock {pending_po[0]}: {pending_po[1]}A/{pending_po[2]}B (in transit at sim end)")
print("\n=== Monthly KWE peak pallet positions / min on-hand ===")
for (y, m), pk, mn in rows:
    print(f"{y}-{m:02d}  peak {pk} plt   min box={mn[0]:4.0f} A={mn[1]:4.0f} B={mn[2]:4.0f}")
print("\n" + ("\n".join(alerts) if alerts else "No stockouts; Richmond hold never ran short."))
