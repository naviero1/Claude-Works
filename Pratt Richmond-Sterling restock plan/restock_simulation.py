"""Daily inventory simulation for the Pratt Richmond -> KWE Sterling restock plan.

Rev B (Jul 9): Pratt clarified that deliveries to KWE come in FIXED INCREMENTS
per part, two options:

  Option 1 (as quoted)   boxes 175 (2 plt) | Part A 200 (4 plt) | Part B 180 (2 plt)
                         insulation MOQ 500 A / 450 B (last release of each MOQ is partial)
  Option 2 (adjusted)    boxes 250 (3 plt) | Part A 250 (5 plt) | Part B 270 (3 plt)
                         insulation MOQ 500 A / 540 B (= exactly 2 releases per part)

Each part rides its own cadence: a release/PO is placed (2-week lead assumed)
when projected stock at arrival hits the safety floor. Insulation ships from the
MOQ stock Pratt holds in Richmond; a new MOQ PO is placed when the hold can no
longer fill one full release. KWE warehouse space is UNKNOWN — this sim reports
the space each option needs (average and receipt-day peak positions).

Usage: 100 boxes/month = 100 boxes + 100 Part A + 100 Part B (1 set per box).
Run: python3 restock_simulation.py
Writes Restock_Schedule_Year1.csv for the baseline scenario (Option 1).
"""
import csv
import math
import os
from datetime import date, timedelta

# ---- Shared assumptions (edit these) ----
USAGE_PER_MONTH = 100
A_PER_PLT = 50
B_PER_PLT = 90
RELEASE_LEAD_DAYS = 14         # notice for a release from the Richmond hold (assumed)
BOX_LEAD_DAYS = 14             # quoted box production lead
INSULATION_LEAD_DAYS = 28      # assumed production lead for an MOQ run (unconfirmed)
SAFETY_UNITS = 50              # order so stock at arrival >= ~2 weeks of usage

FIRST_DELIVERY = date(2026, 7, 22)
USAGE_START = date(2026, 8, 1)
END = date(2027, 7, 31)

SCENARIOS = [
    {"name": "Option 1 (as quoted)", "inc_a": 200, "inc_b": 180, "box_qty": 175, "box_plt": 2,
     "moq": (500, 450), "baseline": True},
    {"name": "Option 2 (adjusted)", "inc_a": 250, "inc_b": 270, "box_qty": 250, "box_plt": 3,
     "moq": (500, 540), "baseline": False},
]
# -----------------------------------------

daily = USAGE_PER_MONTH / 30.44


def run(sc):
    inc_a, inc_b = sc["inc_a"], sc["inc_b"]
    box_per_plt = sc["box_qty"] / sc["box_plt"]
    moq_a, moq_b = sc["moq"]

    # go-live: first A + B releases and first box order arrive together
    a, b, box = float(inc_a), float(inc_b), float(sc["box_qty"])
    rich_a, rich_b = moq_a - inc_a, moq_b - inc_b
    golive_plt = math.ceil(inc_a / A_PER_PLT) + math.ceil(inc_b / B_PER_PLT) + sc["box_plt"]

    sched = [{"Date": "2026-07-08", "Event": "Pratt PO-1 placed", "Part A": moq_a, "Part B": moq_b,
              "Boxes": sc["box_qty"], "Pallets to KWE": "",
              "Notes": f"MOQ held in Richmond + first box order; in stock {FIRST_DELIVERY}"},
             {"Date": str(FIRST_DELIVERY), "Event": "Go-live delivery to KWE", "Part A": inc_a,
              "Part B": inc_b, "Boxes": sc["box_qty"], "Pallets to KWE": golive_plt,
              "Notes": "First release of every part together — peak footprint"}]

    pend = {"a": None, "b": None, "box": None}   # arrival date + qty
    pending_moq = None
    moq_pos = [("2026-07-08", str(FIRST_DELIVERY))]
    drops = {"a": 0, "b": 0, "box": 0}
    monthly = {}
    alerts = []
    peak_overall = 0

    d = FIRST_DELIVERY + timedelta(days=1)
    while d <= END:
        if pending_moq and d == pending_moq[0]:
            rich_a += pending_moq[1]
            rich_b += pending_moq[2]
            sched.append({"Date": str(pending_moq[3]), "Event": f"Pratt PO-{len(moq_pos) + 1} placed",
                          "Part A": pending_moq[1], "Part B": pending_moq[2], "Boxes": "",
                          "Pallets to KWE": "", "Notes": f"MOQ for Richmond hold; in stock {d}"})
            moq_pos.append((str(pending_moq[3]), str(d)))
            pending_moq = None
        if pend["a"] and d == pend["a"][0]:
            qa = pend["a"][1]
            a += qa
            drops["a"] += 1
            sched.append({"Date": str(d), "Event": "Part A release to KWE", "Part A": qa, "Part B": "",
                          "Boxes": "", "Pallets to KWE": math.ceil(qa / A_PER_PLT),
                          "Notes": f"Richmond A after: {rich_a:.0f}" + (" (partial)" if qa != inc_a else "")})
            pend["a"] = None
        if pend["b"] and d == pend["b"][0]:
            qb = pend["b"][1]
            b += qb
            drops["b"] += 1
            sched.append({"Date": str(d), "Event": "Part B release to KWE", "Part A": "", "Part B": qb,
                          "Boxes": "", "Pallets to KWE": math.ceil(qb / B_PER_PLT),
                          "Notes": f"Richmond B after: {rich_b:.0f}" + (" (partial)" if qb != inc_b else "")})
            pend["b"] = None
        if pend["box"] and d == pend["box"][0]:
            box += sc["box_qty"]
            drops["box"] += 1
            sched.append({"Date": str(d), "Event": "Box delivery to KWE", "Part A": "", "Part B": "",
                          "Boxes": sc["box_qty"], "Pallets to KWE": sc["box_plt"], "Notes": ""})
            pend["box"] = None

        if pend["a"] is None and rich_a > 0 and a - daily * RELEASE_LEAD_DAYS <= SAFETY_UNITS:
            qa = min(inc_a, rich_a)
            rich_a -= qa
            pend["a"] = (d + timedelta(days=RELEASE_LEAD_DAYS), qa)
        if pend["b"] is None and rich_b > 0 and b - daily * RELEASE_LEAD_DAYS <= SAFETY_UNITS:
            qb = min(inc_b, rich_b)
            rich_b -= qb
            pend["b"] = (d + timedelta(days=RELEASE_LEAD_DAYS), qb)
        # replenish the Richmond hold when total insulation runway (Sterling + Richmond
        # + in-transit) drops below production lead + 2-week buffer
        pipe_a = a + rich_a + (pend["a"][1] if pend["a"] else 0)
        pipe_b = b + rich_b + (pend["b"][1] if pend["b"] else 0)
        if pending_moq is None and min(pipe_a, pipe_b) / daily <= INSULATION_LEAD_DAYS + 21:
            pending_moq = (d + timedelta(days=INSULATION_LEAD_DAYS), moq_a, moq_b, d)
        if pend["box"] is None and box - daily * BOX_LEAD_DAYS <= SAFETY_UNITS:
            pend["box"] = (d + timedelta(days=BOX_LEAD_DAYS), sc["box_qty"])
            sched.append({"Date": str(d), "Event": "Box PO placed", "Part A": "", "Part B": "",
                          "Boxes": sc["box_qty"], "Pallets to KWE": "",
                          "Notes": f"2-week lead; arrives {d + timedelta(days=BOX_LEAD_DAYS)}"})

        if d >= USAGE_START:
            a -= daily; b -= daily; box -= daily
        if min(a, b, box) < -0.5:
            alerts.append(f"{d} STOCKOUT A={a:.0f} B={b:.0f} box={box:.0f}")
        pos = (math.ceil(max(a, 0) / A_PER_PLT) + math.ceil(max(b, 0) / B_PER_PLT)
               + math.ceil(max(box, 0) / box_per_plt))
        peak_overall = max(peak_overall, pos)
        mk = f"{d.year}-{d.month:02d}"
        cur = monthly.setdefault(mk, {"peak": 0, "sum": 0, "n": 0})
        cur["peak"] = max(cur["peak"], pos)
        cur["sum"] += pos
        cur["n"] += 1
        d += timedelta(days=1)

    return {"sched": sorted(sched, key=lambda r: r["Date"]), "monthly": monthly, "drops": drops,
            "moq_pos": moq_pos, "peak": peak_overall, "alerts": alerts, "golive_plt": golive_plt}


for sc in SCENARIOS:
    r = run(sc)
    avg = sum(m["sum"] for m in r["monthly"].values()) / max(1, sum(m["n"] for m in r["monthly"].values()))
    print("=" * 78)
    print(f"{sc['name']}   A {sc['inc_a']}/drop, B {sc['inc_b']}/drop, boxes {sc['box_qty']}/drop")
    print(f"  go-live footprint: {r['golive_plt']} pallet positions")
    print(f"  year-1 drops after go-live: A x{r['drops']['a']}, B x{r['drops']['b']}, boxes x{r['drops']['box']}")
    print(f"  Pratt MOQ POs: {len(r['moq_pos'])} placed {[p[0] for p in r['moq_pos']]}")
    print(f"  KWE space needed: avg {avg:.1f} positions, worst receipt-day peak {r['peak']}")
    print(f"  monthly peaks: " + " ".join(f"{k}:{v['peak']}" for k, v in sorted(r['monthly'].items())))
    print("  " + ("; ".join(r["alerts"]) if r["alerts"] else "no stockouts"))
    if sc["baseline"]:
        csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Restock_Schedule_Year1.csv")
        with open(csv_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["Date", "Event", "Part A", "Part B", "Boxes",
                                              "Pallets to KWE", "Notes"])
            w.writeheader()
            w.writerows(r["sched"])
        print(f"  baseline schedule written to {csv_path}")
