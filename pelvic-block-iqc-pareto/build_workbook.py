#!/usr/bin/env python3
"""
Build the Pelvic Block IQC Pareto + Root-Cause Framework workbook.

Ingests rejected-pelvic-block IQC inspection data (SH: Martins), normalizes each
free-text scrap reason into a controlled defect taxonomy, and produces a
multi-sheet Excel workbook:

  1. README            - how the framework works + process flow
  2. Inspection Log    - one row per physical block (master data, append future batches here)
  3. Defect Taxonomy   - controlled vocabulary + root-cause map (the framework)
  4. Pareto            - auto-calculating defect Pareto (chart) + supplier-station rollup
  5. Root Cause (5-Why)- structured RCA template seeded for the vital-few defects
  6. Dashboard         - combined KPIs + per-batch breakdown

Counts are driven by formulas referencing the Inspection Log, so appending new
inspection rows updates the Pareto and Dashboard automatically.

Inspection sheets ingested so far (grouped by kill date on the Dashboard):
  * Kill 2026-05-27 (Martins)             - 31 inspected, 8 pass, 23 fail
  * Kill 2026-07-08 (Martins)             - 26 inspected, 1 pass, 25 fail
  * Kill 2026-07-28 (Martins, Rasmin)     - 30 inspected, 1 pass, 29 fail
  * Kill 2026-07-28 (Martins, Toni)       - 12 inspected, 0 pass, 12 fail
"""

import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.axis import ChartLines
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

# ----------------------------------------------------------------------------
# 1. CONTROLLED DEFECT TAXONOMY  (the framework's backbone)
# ----------------------------------------------------------------------------
# Process stations (supplier / slaughterhouse side, upstream of us):
#   S1 Sticking / Bleeding      - exsanguination
#   S2 Bung dropping / Rodding  - rectum + pelvic loosening
#   S3 Evisceration             - belly opening, gut & pluck removal (knife + traction)
#   S4 Carcass splitting        - pelvic / aitch-bone saw
#   S5 Handling & Pit drop      - post-evisceration handling, drop to pit, collection
#   S6 Live animal / physiology - pre-slaughter condition
#
# columns: code, name, definition, severity, process_step, station_code, station_name,
#          rootcause_6m, mechanism, corrective_action
TAXONOMY = [
    ("D1", "Ureters not embedded",
     "Ureter(s) dislodged/stripped from the surrounding pelvic fat & fascia; no longer seated in tissue.",
     "Major", "Gut/pluck removal (traction) + pit handling", "S3", "Evisceration",
     "Method / Handling",
     "Tensile traction: block pulled/stripped so fascia separates from ureter; over-trim.",
     "Standardize gut-pull technique & pull-force; reduce stripping of perirenal fat; gentler drop to pit."),
    ("D2", "Ureter cut / severed",
     "Ureter partially or fully transected / cut off (sharp cut edge).",
     "Major", "Evisceration knife / splitting saw", "S3", "Evisceration",
     "Machine / Method",
     "Sharp laceration by evisceration knife or off-line pelvic saw path.",
     "Retrain knife path around pelvic organs; verify saw alignment through symphysis."),
    ("D3", "Ureter missing",
     "One ureter (left or right) absent from the block.",
     "Major", "Bung dropping / splitting (over-cut) or lost in handling", "S2", "Bung dropping",
     "Method / Handling",
     "Over-aggressive bung/pelvic cut removes ureter, or ureter lost during drop/collection.",
     "Tighten bung-dropping cut boundary; audit pit collection for detached tissue."),
    ("D4", "Suspensory ligaments damaged",
     "Suspensory ligament(s) torn/frayed or holed (incl. bladder suspensory ligament).",
     "Major", "Gut pull (traction) + handling", "S3", "Evisceration",
     "Method / Handling",
     "Excessive pull force / rough handling tears ligament attachments.",
     "Control pull-force & angle on gut set removal; handle block by support surface, not by ligaments."),
    ("D5", "Urethra breach (cut / laceration / hole / separation)",
     "Urethra transected, lacerated, perforated or separated (incl. hole in distal urethra).",
     "Major", "Carcass splitting saw / bung dropping", "S4", "Carcass splitting",
     "Machine / Method",
     "Splitting saw off-center through pelvis, or bung-drop cut catches/perforates urethra.",
     "Center pelvic split on symphysis; calibrate/align splitting saw; slow through pelvic zone."),
    ("D6", "Membrane damage in critical area",
     "Hole/tear in the mesentery membrane separating bowel from pelvic organs, in the critical zone (>1.5\").",
     "Critical", "Evisceration knife technique / bung dropping", "S3", "Evisceration",
     "Method / Man",
     "Knife nick or tensile tear of membrane during gut removal / bung loosening.",
     "Retrain evisceration knife depth & path; slow line in pelvic zone; blunt-dissect where possible."),
    ("D7", "Bladder deformed / deformed attachment",
     "Bladder misshapen or attachment distorted.",
     "Minor", "Live-animal fill state / handling pressure", "S6", "Live / physiology",
     "Material / Handling",
     "Distended (full) bladder at slaughter, or compression during handling.",
     "Manage lairage/feed-water timing to reduce bladder fill; avoid compressing block."),
    ("D8", "Bowel / colon / rectum breach",
     "Bowel integrity breached - cut, hole, or separation of colon/rectum. FOOD-SAFETY / contamination risk.",
     "Critical", "Evisceration / bung dropping", "S3", "Evisceration",
     "Method / Man",
     "Knife slip or aggressive bung separation opens/severs colon or rectum.",
     "Reinforce bung-bagging/tie-off; retrain knife path; treat as contamination CCP at supplier."),
    ("D9", "Blood clots",
     "Retained blood clots in the tissue block.",
     "Minor", "Sticking / bleeding efficiency", "S1", "Sticking / Bleeding",
     "Method",
     "Incomplete exsanguination (stick placement / stun-to-stick interval / bleed time).",
     "Verify stick placement & bleed-out time; check stun-to-stick interval."),
    ("D10", "Broad ligament hole / tear",
     "Large hole/tear in the broad ligament.",
     "Major", "Evisceration / bung dropping", "S3", "Evisceration",
     "Method / Handling",
     "Traction tear or knife nick near broad ligament during gut removal.",
     "Control pull-force; retrain knife path near broad ligament."),
    ("D11", "Bladder neck separation",
     "Bladder detached/separated at the neck (bladder-urethra junction at the pelvic floor).",
     "Major", "Carcass splitting saw / pelvic outlet cut", "S4", "Carcass splitting",
     "Machine / Method",
     "Saw path or traction at the pelvic floor separates the bladder neck from the urethra.",
     "Center pelvic split; protect bladder neck at the pelvic outlet; control traction."),
    ("D12", "Bladder cut / hole (breach)",
     "Bladder wall cut open or holed. Urine-contamination risk. Distinct from D7 (deformed) & D11 (neck separation).",
     "Major", "Evisceration knife / splitting saw", "S3", "Evisceration",
     "Machine / Method",
     "Knife nick or saw path opens the bladder; or over-distended bladder ruptures under handling.",
     "Protect bladder during gut removal; verify saw path; manage bladder fill (lairage/water timing)."),
    ("D13", "Block too short / undersized",
     "Harvested pelvic block dimensionally too short / fails the length template (insufficient tissue retained).",
     "Major", "Pelvic-block separation cut (cut-boundary placement)", "S3", "Evisceration",
     "Method / Man",
     "Separation cut placed too close; insufficient block length retained vs template/spec.",
     "Define & train pelvic-block cut boundaries / minimum length; cut to template; provide a length gauge."),
]
DEFECT_CODES = [t[0] for t in TAXONOMY]
NAME_OF = {t[0]: t[1] for t in TAXONOMY}

# ----------------------------------------------------------------------------
# 2. INGESTED BATCHES  (verbatim scrap reasons -> defect-code expansion)
# ----------------------------------------------------------------------------
# Each row: (n_blocks, result, verbatim_reason, [defect codes], note)
BATCHES = [
    dict(
        insp_date="2026-05-27", kill_date="2026-05-27", harvest_date="", slaughterhouse="Martins",
        sh_tech="", inspector="", batch="", part_name="Pelvic block",
        rows=[
            (3, "Fail", "hole in the distal end of the colon", ["D8"], ""),
            (1, "Fail", "hole in the distal end of the urethra and bladder neck separation", ["D5", "D11"], ""),
            (5, "Pass", '8" hole in the bladder suspencery ligamant. ureter still intact???', [],
                "QUESTIONABLE - pending ME/DE determination (per sheet note). If reclassified Fail -> D4 (suspensory ligament)."),
            (2, "Pass", "no damage found", [], ""),
            (1, "Fail", "ureter cut off", ["D2"], ""),
            (14, "Fail", 'hole in mesentary membrane in critical area greater than 1.5"', ["D6"], ""),
            (1, "Fail", "rectum seperation", ["D8"], ""),
            (2, "Fail", "laceration in urethra", ["D5"], ""),
            (1, "Fail", 'hole in the distal end of the urethra and hole in mesentary membrane in critical area greater than 1.5"', ["D5", "D6"], ""),
            (1, "Pass", "hole in the distal end of the colon passed the template", [], "Colon hole small enough to pass template."),
        ],
    ),
    dict(
        insp_date="2026-07-10", kill_date="2026-07-08", harvest_date="2026-07-08", slaughterhouse="Martins",
        sh_tech="", inspector="", batch="12:30 PM - 12:45 PM", part_name="Tiss, porcine, fem, Pelvic block",
        rows=[
            (1, "Fail", "Large hole near right broad ligament and membrane causing seperation of bowel and ureters.", ["D10", "D6", "D8"], ""),
            (1, "Fail", "2 inch damage on membrane seperating bowel in critical area", ["D6", "D8"], ""),
            (1, "Fail", "urethra is cut", ["D5"], ""),
            (1, "Fail", "bladder deformed 12 inch deformed attachment", ["D7"], ""),
            (1, "Fail", "suspensory ligaments damaged, ureters not embedded", ["D4", "D1"], ""),
            (1, "Fail", "ureters not embedded, suspensory ligaments damaged, cut urethra", ["D1", "D4", "D5"], ""),
            (1, "Fail", "ureters not embedded and cut, suspensory ligaments damaged, cut urethra", ["D1", "D2", "D4", "D5"], ""),
            (1, "Fail", "ureters not embedded, suspensory ligaments damaged, cut urethra, membrane damaged in critical area", ["D1", "D4", "D5", "D6"], ""),
            (1, "Fail", "suspensory ligaments damaged, ureters not embedded", ["D4", "D1"], ""),
            (1, "Fail", "ureters not embedded, suspensory ligaments damaged, cut urethra, membrane damaged in critical area", ["D1", "D4", "D5", "D6"], ""),
            (1, "Fail", "left ureter is missing", ["D3"], ""),
            (2, "Fail", "ureters not embedded, suspensory ligaments damaged, membrane damaged in critical area", ["D1", "D4", "D6"], ""),
            (1, "Fail", "left ureter missing, blood clots", ["D3", "D9"], ""),
            (1, "Fail", "right ureter missing, membrane damage in critical area", ["D3", "D6"], ""),
            (1, "Fail", "membrane damage in critical area, ureters not embedded", ["D6", "D1"], ""),
            (1, "Fail", "membrane damage in critical area, ureters not embedded", ["D6", "D1"], ""),
            (1, "Fail", "ureter cut, membrane damage in critital area, right ureter not embedded", ["D2", "D6", "D1"], ""),
            (1, "Fail", "urethra cut, membrnae damage in critial area", ["D5", "D6"], ""),
            (1, "Fail", "bowel is cut open", ["D8"], ""),
            (1, "Fail", "urethra is cut, membrane damage in critical area", ["D5", "D6"], ""),
            (4, "Fail", "membrane damage in critical area", ["D6"], ""),
            (1, "Pass", "", [], ""),
        ],
    ),
    dict(
        insp_date="2026-07-29", kill_date="2026-07-28", harvest_date="2026-07-28", slaughterhouse="Martins",
        sh_tech="", inspector="Rasmin", batch="", part_name="Pelvic block",
        rows=[
            (2, "Fail", "large hole in bladder", ["D12"], ""),
            (2, "Fail", "Ureter lac", ["D2"], ""),
            (1, "Pass", "no damage found", [], ""),
            (6, "Fail", "ureter not imbedded", ["D1"], ""),
            (12, "Fail", 'hole in mesentary membrane in critical area greater than 1.5"', ["D6"], ""),
            (6, "Fail", "Block too short", ["D13"], ""),
            (1, "Fail", "laceration in urethra", ["D5"],
                "Sheet's handwritten total read '1 Pass / 22 failures'; per-row entries sum to 29 fails (used here)."),
        ],
    ),
    dict(
        insp_date="2026-07-29", kill_date="2026-07-28", harvest_date="2026-07-28", slaughterhouse="Martins",
        sh_tech="", inspector="Toni", batch="", part_name="Tiss, porcine, fem, Pelvic block",
        rows=[
            (1, "Fail", "bowel is cut open", ["D8"], ""),
            (5, "Fail", 'membrane damage greater than .5" in critical area', ["D6"], ""),
            (1, "Fail", "urethra cut, bowel damaged", ["D5", "D8"], ""),
            (2, "Fail", "ureter is damaged and cut off", ["D2"], ""),
            (1, "Fail", "bladder is cut open", ["D12"], ""),
            (1, "Fail", 'bladder is cut open, urethra seperated, membrane damage greater than .5"', ["D12", "D5", "D6"], ""),
            (1, "Fail", "short block", ["D13"], ""),
        ],
    ),
]

# ----- expand into one record per physical block -----
records = []  # dict per block
blk = 1
for b in BATCHES:
    for n, result, reason, codes, note in b["rows"]:
        for _ in range(n):
            records.append(dict(
                bid=f"B{blk:03d}", insp_date=b["insp_date"], kill_date=b["kill_date"],
                harvest_date=b["harvest_date"], slaughterhouse=b["slaughterhouse"],
                sh_tech=b["sh_tech"], inspector=b["inspector"], batch=b["batch"],
                part_name=b["part_name"], result=result, reason=reason,
                codes=set(codes), note=note))
            blk += 1

# ----- counts (for sort order + previews; the workbook itself uses live formulas) -----
counts = {c: 0 for c in DEFECT_CODES}
for r in records:
    for c in r["codes"]:
        counts[c] += 1
order = sorted(DEFECT_CODES, key=lambda c: (-counts[c], int(c[1:])))
total_def = sum(counts.values())

# per-batch stats, grouped by KILL DATE (sheets that share a kill date aggregate into one row)
kill_dates = []
for b in BATCHES:
    if b["kill_date"] not in kill_dates:
        kill_dates.append(b["kill_date"])
batch_stats = []
for kd in sorted(kill_dates):
    recs = [r for r in records if r["kill_date"] == kd]
    insp = len(recs)
    passed = sum(1 for r in recs if r["result"] == "Pass")
    failed = insp - passed
    bcounts = {c: 0 for c in DEFECT_CODES}
    for r in recs:
        for c in r["codes"]:
            bcounts[c] += 1
    top = max(bcounts, key=lambda c: bcounts[c])
    batch_stats.append(dict(kill=kd, insp=insp, passed=passed, failed=failed,
                            fpy=passed / insp if insp else 0, top=top, topn=bcounts[top]))

# station rollup
from collections import defaultdict
station_codes = defaultdict(list); station_name = {}
for t in TAXONOMY:
    station_codes[t[5]].append(t[0]); station_name[t[5]] = t[6]
station_order = sorted(station_codes, key=lambda s: sum(counts[c] for c in station_codes[s]), reverse=True)

# ----------------------------------------------------------------------------
# STYLES
# ----------------------------------------------------------------------------
NAVY="1F3864"; BLUE="305496"; LT_BLUE="D9E1F2"; GREY="808080"; LT_GREY="F2F2F2"
AMBER="FFE699"; RED="F4B183"; GREEN="C6E0B4"; WHITE="FFFFFF"

def font(sz=11, b=False, color="000000", italic=False):
    return Font(name="Calibri", size=sz, bold=b, color=color, italic=italic)
def fill(c): return PatternFill("solid", fgColor=c)
thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT = Alignment(horizontal="left", vertical="center", wrap_text=True)
LEFT_TOP = Alignment(horizontal="left", vertical="top", wrap_text=True)

def style_header(cell, fillc=BLUE, color=WHITE, sz=11):
    cell.font = font(sz, True, color); cell.fill = fill(fillc)
    cell.alignment = CENTER; cell.border = BORDER

def title_block(ws, text, subtitle, ncols):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    c = ws.cell(1, 1, text)
    c.font = font(16, True, WHITE); c.fill = fill(NAVY)
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[1].height = 30
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    c2 = ws.cell(2, 1, subtitle)
    c2.font = font(10, False, WHITE, italic=True); c2.fill = fill(BLUE)
    c2.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[2].height = 18

wb = openpyxl.Workbook()

# ============================================================================
# SHEET 1: README
# ============================================================================
ws = wb.active; ws.title = "README"; ws.sheet_view.showGridLines = False
title_block(ws, "PELVIC BLOCK IQC — PARETO & ROOT-CAUSE FRAMEWORK",
            "Incoming Quality Control of rejected porcine femoral pelvic blocks  |  Purpose: pinpoint where defects originate at the supplier and drive corrective action upstream", 8)
readme = [
    ("", ""),
    ("PURPOSE", "H"),
    ("Ingest IQC results for rejected pelvic blocks, sort defects with a Pareto (the few defects causing most loss), and map every defect back to the", "P"),
    ("point in the SUPPLIER's process where it is created — so corrective action can be taken BEFORE the tissue block reaches us.", "P"),
    ("", ""),
    ("THE PROCESS (where a defect can be born)  —  everything up to 'Delivered to us' is the supplier's to control", "H"),
    ("  Live animal  ->  S1 Sticking/Bleeding  ->  S2 Bung dropping/Rodding  ->  S3 Evisceration (knife + gut pull)  ->  S4 Carcass splitting (saw)  ->  S5 Handling & Pit drop  ->  Delivered to us", "FLOW"),
    ("                                                                                    OUR side ->  Harvest techs receive block from pit  ->  spec-out / accept  ->  IQC inspection (this data)", "FLOW"),
    ("", ""),
    ("THE SHEETS", "H"),
    ("  1. Inspection Log   Master data — ONE ROW PER BLOCK. Each free-text scrap reason is normalized into 1/0 flags against the defect taxonomy. Append future batches here.", "P"),
    ("  2. Defect Taxonomy  Controlled vocabulary (D1–D11) + root-cause map: each defect -> process step, supplier station, 6M cause, mechanism, corrective action.", "P"),
    ("  3. Pareto           Auto-calculating defect Pareto (bar + cumulative line) and a rollup by SUPPLIER STATION — the key view for the supplier conversation.", "P"),
    ("  4. Root Cause 5-Why  Structured RCA template, seeded for the vital-few defects, with a Lessons-Learned column to fill in over time.", "P"),
    ("  5. Dashboard        Combined KPIs + a per-batch breakdown so you can watch the trend batch over batch.", "P"),
    ("", ""),
    ("HOW TO ADD THE NEXT INSPECTION", "H"),
    ("  a. In 'Inspection Log', add one row per inspected block (metadata + Result = Pass/Fail + verbatim reason).", "P"),
    ("  b. Put a 1 in each defect column (D1–D11) that applies. Use the dropdown. If a NEW defect type appears, add it to 'Defect Taxonomy' first, then add its column.", "P"),
    ("  c. Pareto + Dashboard recalc automatically. Re-sort the Pareto table high->low if the ranking changes (counts are live; row order is not).", "P"),
    ("", ""),
    ("WHAT THE DATA SAYS SO FAR  (4 inspection sheets across 3 kill dates: 2026-05-27, 2026-07-08, 2026-07-28 — SH: Martins)", "H"),
    (f"  {sum(bs['insp'] for bs in batch_stats)} blocks inspected · {sum(bs['passed'] for bs in batch_stats)} pass · {sum(bs['failed'] for bs in batch_stats)} fail · combined First Pass Yield {sum(bs['passed'] for bs in batch_stats)/sum(bs['insp'] for bs in batch_stats)*100:.1f}% · {total_def} defect occurrences", "P"),
    ("  Vital few (~80%): membrane damage (critical area), ureters not embedded, urethra breach, bowel/colon/rectum breach, suspensory-ligament damage.  ~84% of ALL defects originate at ONE station: Evisceration.", "P"),
    ("  OPEN ITEMS: (1) 5 blocks (kill 2026-05-27), 8\" hole in bladder suspensory ligament — recorded PASS pending ME/DE (flip to Fail + tag D4 if confirmed).  (2) Rasmin 07-28 sheet handwritten total said '22 fails' but per-row entries sum to 29 (used).", "P"),
    ("", ""),
    ("SEVERITY KEY", "H"),
    ("  Critical = function-destroying or food-safety (e.g. bowel/colon/rectum breach = contamination).   Major = block rejected.   Minor = cosmetic / recoverable.", "P"),
    ("", ""),
    ("SOURCE", "H"),
    ("  IQC Tally Sheets — SH: Martins. Originals kept as source_*.xlsx in this folder.", "P"),
]
r = 4
for text, kind in readme:
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8)
    c = ws.cell(r, 1, text)
    if kind == "H":
        c.font = font(11, True, NAVY); c.fill = fill(LT_BLUE)
        c.alignment = Alignment(horizontal="left", vertical="center", indent=1); ws.row_dimensions[r].height = 18
    elif kind == "FLOW":
        c.font = font(9, True, "1F4E5F"); c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    else:
        c.font = font(10, False, "222222"); c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    r += 1
ws.column_dimensions["A"].width = 20
for col in "BCDEFGH": ws.column_dimensions[col].width = 20

# ============================================================================
# SHEET 2: INSPECTION LOG
# ============================================================================
log = wb.create_sheet("Inspection Log"); log.sheet_view.showGridLines = False
meta_cols = ["Block ID", "Insp. Date", "Kill Date", "Harvest Date", "Slaughterhouse",
             "SH Tech", "Inspector", "Batch/Lot", "Part Name", "Result", "Verbatim Scrap Reason"]
headers = meta_cols + DEFECT_CODES + ["# Defects", "Notes / Disposition"]
DEFECT_START = len(meta_cols) + 1                       # first defect column index (L=12)
CODE_TO_COL = {c: get_column_letter(DEFECT_START + i) for i, c in enumerate(DEFECT_CODES)}
NDEF_COL = DEFECT_START + len(DEFECT_CODES)             # # Defects column index
NOTES_COL = NDEF_COL + 1
RESULT_COL = get_column_letter(10)                      # J
KILL_COL = get_column_letter(3)                         # C

title_block(log, "INSPECTION LOG  (master data — one row per inspected block)",
            "Append future inspections below. Put 1 in each defect column that applies. Pareto/Dashboard update automatically.", len(headers))
hdr_row = 4
for j, h in enumerate(headers, start=1):
    style_header(log.cell(hdr_row, j, h))
log.row_dimensions[hdr_row].height = 28
data_first = hdr_row + 1

for i, rec in enumerate(records):
    rr = data_first + i
    vals = [rec["bid"], rec["insp_date"], rec["kill_date"], rec["harvest_date"], rec["slaughterhouse"],
            rec["sh_tech"], rec["inspector"], rec["batch"], rec["part_name"], rec["result"], rec["reason"]]
    for j, v in enumerate(vals, start=1):
        c = log.cell(rr, j, v); c.border = BORDER; c.font = font(10)
        c.alignment = LEFT_TOP if j == 11 else CENTER
        if j == 10:
            c.font = font(10, True, "833C00" if rec["result"] == "Fail" else "375623")
            c.fill = fill(RED if rec["result"] == "Fail" else GREEN)
    for k, code in enumerate(DEFECT_CODES):
        c = log.cell(rr, DEFECT_START + k, 1 if code in rec["codes"] else None)
        c.border = BORDER; c.alignment = CENTER; c.font = font(10, True, "C00000")
        if code in rec["codes"]: c.fill = fill(AMBER)
    dc0 = get_column_letter(DEFECT_START); dc1 = get_column_letter(DEFECT_START + len(DEFECT_CODES) - 1)
    t = log.cell(rr, NDEF_COL); t.value = f"=SUM({dc0}{rr}:{dc1}{rr})"
    t.border = BORDER; t.alignment = CENTER; t.font = font(10, True)
    nc = log.cell(rr, NOTES_COL, rec["note"]); nc.border = BORDER; nc.alignment = LEFT_TOP; nc.font = font(9, italic=bool(rec["note"]))
    if rec["note"]: nc.fill = fill("FFF2CC")
    log.row_dimensions[rr].height = 30 if rec["result"] == "Fail" or rec["note"] else 16
data_last = data_first + len(records) - 1

widths = {"A":9,"B":11,"C":11,"D":12,"E":13,"F":9,"G":10,"H":16,"I":22,"J":8,"K":42}
for col, w in widths.items(): log.column_dimensions[col].width = w
for k in range(len(DEFECT_CODES)): log.column_dimensions[get_column_letter(DEFECT_START + k)].width = 6
log.column_dimensions[get_column_letter(NDEF_COL)].width = 9
log.column_dimensions[get_column_letter(NOTES_COL)].width = 34
log.freeze_panes = log.cell(data_first, 2)

dv = DataValidation(type="list", formula1='"Pass,Fail"', allow_blank=True); log.add_data_validation(dv)
dv.add(f"J{data_first}:J{data_first+400}")
dv2 = DataValidation(type="list", formula1='"1"', allow_blank=True); log.add_data_validation(dv2)
dv2.add(f"{get_column_letter(DEFECT_START)}{data_first}:{get_column_letter(DEFECT_START+len(DEFECT_CODES)-1)}{data_first+400}")

RNG = f"{data_last+400}"                                # bottom of formula ranges
def code_sum(code): return f"SUM('Inspection Log'!{CODE_TO_COL[code]}{data_first}:{CODE_TO_COL[code]}{RNG})"
dc0 = get_column_letter(DEFECT_START); dc1 = get_column_letter(DEFECT_START + len(DEFECT_CODES) - 1)
total_formula = f"SUM('Inspection Log'!{dc0}{data_first}:{dc1}{RNG})"

# ============================================================================
# SHEET 3: DEFECT TAXONOMY
# ============================================================================
tax = wb.create_sheet("Defect Taxonomy"); tax.sheet_view.showGridLines = False
tax_headers = ["Code", "Defect Mode", "Definition", "Severity", "Likely Process Step (where it's born)",
               "Supplier Station", "Root-Cause Category (6M)", "Likely Mechanism",
               "Recommended Corrective Action (to supplier)", "Lessons Learned  (fill in over time)"]
title_block(tax, "DEFECT TAXONOMY & ROOT-CAUSE MAP",
            "The controlled vocabulary. Every scrap reason maps to a code here — the point where a defect is traced back to the supplier's process.", len(tax_headers))
hr = 4
for j, h in enumerate(tax_headers, start=1): style_header(tax.cell(hr, j, h))
tax.row_dimensions[hr].height = 30
sev_fill = {"Critical": "F4B183", "Major": "FFE699", "Minor": "D9E1F2"}
for i, t in enumerate(TAXONOMY):
    rr = hr + 1 + i
    code, name, defn, sev, step, scode, sname, cause, mech, action = t
    row_vals = [code, name, defn, sev, step, f"{scode} {sname}", cause, mech, action, ""]
    for j, v in enumerate(row_vals, start=1):
        c = tax.cell(rr, j, v); c.border = BORDER; c.font = font(10)
        c.alignment = CENTER if j in (1, 4, 6) else LEFT_TOP
        if j == 1: c.font = font(11, True, NAVY)
        if j == 4: c.fill = fill(sev_fill[sev]); c.font = font(10, True, "833C00" if sev != "Minor" else NAVY)
        if j == 10: c.fill = fill(LT_GREY)
    tax.row_dimensions[rr].height = 46
for col, w in {"A":6,"B":24,"C":42,"D":9,"E":30,"F":18,"G":16,"H":38,"I":42,"J":30}.items():
    tax.column_dimensions[col].width = w
tax.freeze_panes = tax.cell(hr + 1, 1)

# ============================================================================
# SHEET 4: PARETO
# ============================================================================
par = wb.create_sheet("Pareto"); par.sheet_view.showGridLines = False
title_block(par, "PARETO — DEFECT FREQUENCY & SUPPLIER-STATION ROLLUP",
            "Counts pull live from the Inspection Log (all batches). Fix the 'vital few' (cumulative line to ~80%) first. Re-sort high->low if ranking changes.", 6)
ph = 4
par.merge_cells(start_row=ph, start_column=1, end_row=ph, end_column=6)
c = par.cell(ph, 1, "A.  DEFECT PARETO  (by occurrence across all inspected blocks, all batches)")
c.font = font(11, True, NAVY); c.fill = fill(LT_BLUE); c.alignment = Alignment(horizontal="left", indent=1)
ph += 1
for j, h in enumerate(["Rank", "Code", "Defect Mode", "Count", "% of Total", "Cumulative %"], start=1):
    style_header(par.cell(ph, j, h))
par.row_dimensions[ph].height = 24
first = ph + 1; n = len(order)
for i, code in enumerate(order):
    rr = first + i
    par.cell(rr, 1, i + 1).alignment = CENTER
    par.cell(rr, 2, code).font = font(10, True, NAVY)
    par.cell(rr, 3, NAME_OF[code])
    par.cell(rr, 4).value = f"={code_sum(code)}"
    par.cell(rr, 5).value = f"=D{rr}/{total_formula}"
    par.cell(rr, 6).value = f"=E{rr}" if i == 0 else f"=F{rr-1}+E{rr}"
    for j in range(1, 7):
        cc = par.cell(rr, j); cc.border = BORDER
        if j in (1, 2, 4): cc.alignment = CENTER
        if j == 3: cc.alignment = LEFT
        if j in (5, 6): cc.number_format = "0.0%"; cc.alignment = CENTER
        if j == 4: cc.font = font(10, True)
    cumfrac = sum(counts[order[k]] for k in range(i + 1)) / total_def
    if cumfrac <= 0.80 + 1e-9 or i == 0:
        par.cell(rr, 3).fill = fill(AMBER)
last = first + n - 1
tr = last + 1
par.cell(tr, 3, "TOTAL").font = font(10, True)
par.cell(tr, 4).value = f"=SUM(D{first}:D{last})"; par.cell(tr, 4).font = font(10, True); par.cell(tr, 4).alignment = CENTER
for j in range(1, 7): par.cell(tr, j).fill = fill(LT_BLUE); par.cell(tr, j).border = BORDER
par.cell(tr, 5).value = f"=D{tr}/{total_formula}"; par.cell(tr, 5).number_format = "0.0%"; par.cell(tr, 5).alignment = CENTER

# station rollup
sh = tr + 3
par.merge_cells(start_row=sh, start_column=1, end_row=sh, end_column=6)
c = par.cell(sh, 1, "B.  ROLLUP BY SUPPLIER STATION  (which station to fix first)")
c.font = font(11, True, NAVY); c.fill = fill(LT_BLUE); c.alignment = Alignment(horizontal="left", indent=1)
sh += 1
for j, h in enumerate(["Station", "Station Name", "Defect Count", "% of Total", "Defect Codes"], start=1):
    style_header(par.cell(sh, j, h))
par.row_dimensions[sh].height = 24
srow = sh + 1
for i, s in enumerate(station_order):
    rr = srow + i; codes_here = station_codes[s]
    par.cell(rr, 1, s).font = font(10, True, NAVY); par.cell(rr, 1).alignment = CENTER
    par.cell(rr, 2, station_name[s]).alignment = LEFT
    par.cell(rr, 3).value = "=" + "+".join(code_sum(c) for c in codes_here)
    par.cell(rr, 3).font = font(10, True); par.cell(rr, 3).alignment = CENTER
    par.cell(rr, 4).value = f"=C{rr}/{total_formula}"; par.cell(rr, 4).number_format = "0.0%"; par.cell(rr, 4).alignment = CENTER
    par.cell(rr, 5, ", ".join(codes_here)).alignment = LEFT
    for j in range(1, 6): par.cell(rr, j).border = BORDER
    if i == 0:
        for j in range(1, 6): par.cell(rr, j).fill = fill(RED)
slast = srow + len(station_order) - 1
for col, w in {"A":10,"B":22,"C":26,"D":13,"E":26,"F":10}.items(): par.column_dimensions[col].width = w

# ---- styled Pareto chart ----
from openpyxl.chart.marker import DataPoint, Marker
from openpyxl.chart.label import DataLabelList
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.drawing.line import LineProperties
from openpyxl.chart.text import RichText, Text
from openpyxl.chart.title import Title
from openpyxl.drawing.text import (Paragraph, ParagraphProperties, CharacterProperties,
                                   Font as DrawFont, RichTextProperties, RegularTextRun)
C_VITAL="2E5B8A"; C_TAIL="AFC7E3"; C_LINE="C0504D"; C_GRID="E6E6E6"; C_AXTX="595959"

def _txpr(size=900, color=C_AXTX, rot=None, bold=False):
    cp = CharacterProperties(latin=DrawFont(typeface="Calibri"), sz=size, b=bold, solidFill=color)
    body = RichTextProperties(rot=rot) if rot is not None else RichTextProperties()
    return RichText(bodyPr=body, p=[Paragraph(pPr=ParagraphProperties(defRPr=cp), endParaRPr=cp)])
def _title(text, size=1200, color=NAVY):
    cp = CharacterProperties(latin=DrawFont(typeface="Calibri"), sz=size, b=True, solidFill=color)
    rt = RichText(p=[Paragraph(pPr=ParagraphProperties(defRPr=cp), r=[RegularTextRun(rPr=cp, t=text)])])
    t = Title(tx=Text(rich=rt)); t.overlay = False; return t

SHORT = {"D6":"Membrane dmg","D1":"Ureters n/e","D5":"Urethra breach","D4":"Susp. ligament",
         "D8":"Bowel/colon","D2":"Ureter cut","D3":"Ureter missing","D7":"Bladder def.",
         "D9":"Blood clots","D10":"Broad ligament","D11":"Bladder neck sep.",
         "D12":"Bladder breach","D13":"Block too short"}
LBL_COL, THR_COL = 13, 14                              # Pareto-sheet helper cols (M/N), sit UNDER the chart
par.cell(ph, THR_COL, "80% target")
for i, code in enumerate(order):
    par.cell(first + i, LBL_COL, f"{code} · {SHORT.get(code, code)}")
    par.cell(first + i, THR_COL, 0.8)

nfew = sum(1 for i in range(n) if sum(counts[order[k]] for k in range(i + 1)) / total_def <= 0.80 + 1e-9) or 1
bar = BarChart(); bar.type = "col"; bar.grouping = "clustered"; bar.gapWidth = 55
bar.add_data(Reference(par, min_col=4, min_row=first - 1, max_row=last), titles_from_data=True)
bar.set_categories(Reference(par, min_col=LBL_COL, min_row=first, max_row=last))
bs = bar.series[0]
bs.graphicalProperties = GraphicalProperties(solidFill=C_VITAL)
for i in range(n):
    dp = DataPoint(idx=i)
    dp.spPr = GraphicalProperties(solidFill=(C_VITAL if i < nfew else C_TAIL),
                                  ln=LineProperties(solidFill="FFFFFF", w=9525))
    bs.data_points.append(dp)
bdl = DataLabelList(); bdl.showVal = True; bdl.numFmt = "0"; bdl.position = "outEnd"
bdl.txPr = _txpr(950, "404040", bold=True); bs.dLbls = bdl
bar.y_axis.title = "Defect count"; bar.y_axis.number_format = "0"; bar.y_axis.scaling.min = 0
bar.y_axis.majorGridlines = ChartLines(spPr=GraphicalProperties(ln=LineProperties(solidFill=C_GRID, w=6350)))
bar.y_axis.txPr = _txpr(); bar.y_axis.delete = False
bar.x_axis.delete = False; bar.x_axis.majorGridlines = None
bar.x_axis.txPr = _txpr(850, rot=-2700000)
bar.x_axis.spPr = GraphicalProperties(ln=LineProperties(solidFill="BFBFBF", w=9525))

line = LineChart()
line.add_data(Reference(par, min_col=6, min_row=first - 1, max_row=last), titles_from_data=True)
line.add_data(Reference(par, min_col=THR_COL, min_row=ph, max_row=last), titles_from_data=True)
cs = line.series[0]
cs.graphicalProperties = GraphicalProperties(ln=LineProperties(solidFill=C_LINE, w=28575))
cs.marker = Marker(symbol="circle", size=6)
cs.marker.spPr = GraphicalProperties(solidFill=C_LINE, ln=LineProperties(solidFill="FFFFFF", w=9525))
cs.smooth = False
cdl = DataLabelList(); cdl.showVal = True; cdl.numFmt = "0%"; cdl.position = "t"
cdl.txPr = _txpr(850, C_LINE, bold=True); cs.dLbls = cdl
ts = line.series[1]
_lp = LineProperties(solidFill="A6A6A6", w=9525); _lp.prstDash = "dash"
ts.graphicalProperties = GraphicalProperties(ln=_lp); ts.marker = Marker(symbol="none"); ts.smooth = False
line.y_axis.axId = 200; line.y_axis.title = "Cumulative %"; line.y_axis.crosses = "max"
line.y_axis.scaling.min = 0; line.y_axis.scaling.max = 1; line.y_axis.number_format = "0%"
line.y_axis.majorGridlines = None; line.y_axis.txPr = _txpr(); line.y_axis.delete = False
bar.y_axis.crosses = "autoZero"
bar += line
bar.title = _title("Defect Pareto — Rejected Pelvic Blocks   (SH: Martins · 3 kill dates)")
bar.legend.position = "b"; bar.legend.overlay = False
bar.width = 26; bar.height = 12.5
par.add_chart(bar, "H4")
par.cell(ph, LBL_COL).font = font(8, italic=True, color=GREY)

from openpyxl.drawing.image import Image as XLImage
_img = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Station_rollup_preview.png")
if os.path.exists(_img):
    im = XLImage(_img); im.width = int(im.width * 0.60); im.height = int(im.height * 0.60)
    par.add_image(im, f"A{slast + 3}")

# ============================================================================
# SHEET 5: ROOT CAUSE 5-WHY
# ============================================================================
rc = wb.create_sheet("Root Cause 5-Why"); rc.sheet_view.showGridLines = False
rc_headers = ["Code", "Defect Mode", "Why 1", "Why 2", "Why 3", "Why 4", "Why 5 (root cause)",
              "Countermeasure (at supplier)", "Owner", "Target Date", "Status", "Lessons Learned"]
title_block(rc, "ROOT CAUSE — 5-WHY WORKSHEET",
            "Seeded with a starting hypothesis chain for the vital-few defects. Drive each to a true root cause with the supplier, then log the countermeasure & lesson.", len(rc_headers))
hr = 4
for j, h in enumerate(rc_headers, start=1): style_header(rc.cell(hr, j, h))
rc.row_dimensions[hr].height = 26
seed = {
    "D6": ["Membrane torn/holed in critical area (>1.5\")", "Knife path too deep / tensile tear during gut pull",
           "Evisceration technique not standardized for pelvic zone", "No defined knife depth/path SOP + line-speed pressure",
           "(confirm w/ supplier) training + line-speed control gap",
           "Retrain knife depth & path in pelvic zone; blunt-dissect; slow line through pelvic cut",
           "SH Martins - Evisceration lead", "", "Open", ""],
    "D1": ["Ureters not embedded in tissue", "Fascia/perirenal fat stripped away from ureter",
           "Excessive pull force / over-trim during gut set removal", "Pull technique & trim spec not controlled",
           "(confirm) handling standard missing",
           "Standardize pull-force & angle; limit fat stripping; gentler pit drop",
           "SH Martins - Evisceration lead", "", "Open", ""],
    "D5": ["Urethra cut / laceration / hole", "Sharp transection or perforation through pelvic zone",
           "Splitting saw off-center / bung-drop cut catches urethra", "Saw alignment & pelvic-split centering not verified",
           "(confirm) saw calibration + technique gap",
           "Center split on symphysis; calibrate/align saw; slow through pelvic zone",
           "SH Martins - Splitting lead", "", "Open", ""],
    "D4": ["Suspensory ligaments torn/frayed/holed", "Block pulled/handled by the ligaments",
           "Rough handling + high traction on removal", "No 'support-surface' handling rule",
           "(confirm) handling standard missing",
           "Handle block by support surface, not ligaments; control pull force",
           "SH Martins - Evisceration lead", "", "Open", ""],
    "D8": ["Bowel/colon/rectum breached (FOOD SAFETY)", "Knife slip or aggressive bung separation opens colon/rectum",
           "Bung not adequately bagged/tied before cut", "Bung-dropping CCP not robust",
           "(confirm) contamination-control gap at bung station",
           "Reinforce bung bag/tie-off; retrain knife path; treat as contamination CCP",
           "SH Martins - Bung/Evisc. lead", "", "Open", ""],
}
seed_order = ["D6", "D1", "D5", "D4", "D8"]
for i, code in enumerate(seed_order):
    rr = hr + 1 + i
    vals = [code, NAME_OF[code]] + seed[code]
    for j, v in enumerate(vals, start=1):
        c = rc.cell(rr, j, v); c.border = BORDER; c.font = font(9)
        c.alignment = CENTER if j in (1, 9, 10, 11) else LEFT_TOP
        if j == 1: c.font = font(11, True, NAVY)
        if j == 2: c.font = font(9, True)
        if j == 7: c.fill = fill(AMBER)
        if j == 8: c.fill = fill(GREEN)
        if j == 11: c.fill = fill("FFF2CC"); c.font = font(9, True, "833C00")
        if j == 12: c.fill = fill(LT_GREY)
    rc.row_dimensions[rr].height = 60
for i in range(3):
    rr = hr + 1 + len(seed_order) + i
    for j in range(1, len(rc_headers) + 1):
        c = rc.cell(rr, j, None); c.border = BORDER
        if j == 7: c.fill = fill(AMBER)
        if j == 8: c.fill = fill(GREEN)
        if j == 12: c.fill = fill(LT_GREY)
    rc.row_dimensions[rr].height = 40
for col, w in {"A":6,"B":24,"C":22,"D":22,"E":22,"F":20,"G":22,"H":30,"I":16,"J":12,"K":9,"L":26}.items():
    rc.column_dimensions[col].width = w
rc.freeze_panes = rc.cell(hr + 1, 3)
dv3 = DataValidation(type="list", formula1='"Open,In Progress,Verifying,Closed"', allow_blank=True)
rc.add_data_validation(dv3); dv3.add(f"K{hr+1}:K{hr+40}")

# ============================================================================
# SHEET 6: DASHBOARD
# ============================================================================
dash = wb.create_sheet("Dashboard"); dash.sheet_view.showGridLines = False
title_block(dash, "DASHBOARD — SUMMARY",
            "SH: Martins  |  4 inspection sheets across 3 kill dates (2026-05-27, 2026-07-08, 2026-07-28)", 7)
kpis = [
    ("Blocks Inspected", f"=COUNTIF('Inspection Log'!{RESULT_COL}{data_first}:{RESULT_COL}{RNG},\"Pass\")+COUNTIF('Inspection Log'!{RESULT_COL}{data_first}:{RESULT_COL}{RNG},\"Fail\")", "0"),
    ("Pass", f'=COUNTIF(\'Inspection Log\'!{RESULT_COL}{data_first}:{RESULT_COL}{RNG},"Pass")', "0"),
    ("Fail", f'=COUNTIF(\'Inspection Log\'!{RESULT_COL}{data_first}:{RESULT_COL}{RNG},"Fail")', "0"),
    ("First Pass Yield", f'=IFERROR(COUNTIF(\'Inspection Log\'!{RESULT_COL}{data_first}:{RESULT_COL}{RNG},"Pass")/(COUNTIF(\'Inspection Log\'!{RESULT_COL}{data_first}:{RESULT_COL}{RNG},"Pass")+COUNTIF(\'Inspection Log\'!{RESULT_COL}{data_first}:{RESULT_COL}{RNG},"Fail")),0)', "0.0%"),
    ("Total Defect Occurrences", f"={total_formula}", "0"),
    ("Defects per Failed Block", f'=IFERROR({total_formula}/COUNTIF(\'Inspection Log\'!{RESULT_COL}{data_first}:{RESULT_COL}{RNG},"Fail"),0)', "0.00"),
]
kr = 4
dash.cell(kr, 1, "KEY METRICS (all batches)").font = font(12, True, NAVY); kr += 1
for label, formula, fmt in kpis:
    dash.cell(kr, 1, label).font = font(11, True, "222222")
    dash.cell(kr, 1).fill = fill(LT_BLUE); dash.cell(kr, 1).alignment = Alignment(horizontal="left", indent=1); dash.cell(kr, 1).border = BORDER
    vc = dash.cell(kr, 2); vc.value = formula; vc.number_format = fmt
    vc.font = font(13, True, NAVY); vc.alignment = CENTER; vc.fill = fill(LT_GREY); vc.border = BORDER
    dash.row_dimensions[kr].height = 22; kr += 1

# per-batch breakdown
kr += 1
dash.cell(kr, 1, "PER-BATCH BREAKDOWN (watch the trend)").font = font(12, True, NAVY); kr += 1
bh = kr
for j, h in enumerate(["Kill Date", "Inspected", "Pass", "Fail", "First Pass Yield", "Top Defect (this batch)"], start=1):
    style_header(dash.cell(bh, j, h))
kr += 1
for bs in sorted(batch_stats, key=lambda x: x["kill"]):
    kd = bs["kill"]
    dash.cell(kr, 1, kd).alignment = CENTER
    dash.cell(kr, 2).value = f'=COUNTIF(\'Inspection Log\'!{KILL_COL}{data_first}:{KILL_COL}{RNG},"{kd}")'
    dash.cell(kr, 3).value = f'=COUNTIFS(\'Inspection Log\'!{KILL_COL}{data_first}:{KILL_COL}{RNG},"{kd}",\'Inspection Log\'!{RESULT_COL}{data_first}:{RESULT_COL}{RNG},"Pass")'
    dash.cell(kr, 4).value = f'=COUNTIFS(\'Inspection Log\'!{KILL_COL}{data_first}:{KILL_COL}{RNG},"{kd}",\'Inspection Log\'!{RESULT_COL}{data_first}:{RESULT_COL}{RNG},"Fail")'
    dash.cell(kr, 5).value = f"=IFERROR(C{kr}/B{kr},0)"; dash.cell(kr, 5).number_format = "0.0%"
    dash.cell(kr, 6, f"{bs['top']} {NAME_OF[bs['top']]} ({bs['topn']})")
    for j in range(1, 7):
        cc = dash.cell(kr, j); cc.border = BORDER
        cc.alignment = CENTER if j in (1, 2, 3, 4, 5) else LEFT
        if j == 5 and bs["fpy"] < 0.10: cc.fill = fill(RED)
    kr += 1

# callouts
kr += 1
dash.cell(kr, 1, "Top defect (all batches)").font = font(12, True, NAVY); kr += 1
dash.cell(kr, 1, f"{order[0]} {NAME_OF[order[0]]}").font = font(12, True, "833C00"); dash.cell(kr, 1).fill = fill(AMBER)
dash.merge_cells(start_row=kr, start_column=1, end_row=kr, end_column=4)
dash.cell(kr, 1).alignment = Alignment(horizontal="left", indent=1); dash.cell(kr, 1).border = BORDER
kr += 1
dash.cell(kr, 1, "Dominant supplier station").font = font(11, True, NAVY); kr += 1
dash.cell(kr, 1, f"{station_order[0]} {station_name[station_order[0]]}  ->  primary target for corrective action").font = font(11, True, "833C00")
dash.merge_cells(start_row=kr, start_column=1, end_row=kr, end_column=5); dash.cell(kr, 1).fill = fill(RED)
dash.cell(kr, 1).alignment = Alignment(horizontal="left", indent=1); dash.cell(kr, 1).border = BORDER
kr += 2
fs_codes = [t[0] for t in TAXONOMY if t[3] == "Critical"]
fs_formula = "=" + "+".join(code_sum(c) for c in fs_codes)
dash.cell(kr, 1, "Critical / food-safety defect occurrences").font = font(11, True, "C00000")
dash.cell(kr, 1).fill = fill(LT_BLUE); dash.cell(kr, 1).alignment = Alignment(horizontal="left", indent=1); dash.cell(kr, 1).border = BORDER
vc = dash.cell(kr, 2); vc.value = fs_formula; vc.font = font(13, True, "C00000"); vc.alignment = CENTER; vc.border = BORDER
kr += 1
dash.cell(kr, 1, "  (Critical codes: " + ", ".join(fs_codes) + " — membrane damage & bowel/colon/rectum breach)").font = font(9, italic=True, color=GREY)
kr += 2
dash.cell(kr, 1, "OPEN ITEMS").font = font(11, True, "C00000"); dash.cell(kr, 1).fill = fill(AMBER); dash.cell(kr, 1).border = BORDER
kr += 1
dash.cell(kr, 1, "1)  5 blocks (kill 2026-05-27), 8\" hole in bladder suspensory ligament, recorded as PASS pending ME/DE determination. If confirmed Fail -> tag D4.").font = font(9, italic=True, color="833C00")
dash.merge_cells(start_row=kr, start_column=1, end_row=kr, end_column=7)
kr += 1
dash.cell(kr, 1, "2)  Rasmin 07-28 sheet: handwritten total read '1 Pass / 22 failures', but the per-row entries sum to 29 fails — the granular rows were used. Confirm with inspector.").font = font(9, italic=True, color="833C00")
dash.merge_cells(start_row=kr, start_column=1, end_row=kr, end_column=7)

dash.column_dimensions["A"].width = 34
dash.column_dimensions["B"].width = 14
for col in "CDE": dash.column_dimensions[col].width = 12
dash.column_dimensions["F"].width = 30; dash.column_dimensions["G"].width = 12

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pelvic_Block_IQC_Pareto_RootCause.xlsx")
wb.save(out)
print("SAVED:", out)
print("Records:", len(records), "| Pass:", sum(1 for r in records if r["result"]=="Pass"), "| Fail:", sum(1 for r in records if r["result"]=="Fail"))
print("Combined defect counts:", {c: counts[c] for c in order})
print("Total defect occurrences:", total_def)
print("Station rollup:", {s: sum(counts[c] for c in station_codes[s]) for s in station_order})
for bs in sorted(batch_stats, key=lambda x: x["kill"]):
    print(f"  Batch {bs['kill']}: insp={bs['insp']} pass={bs['passed']} fail={bs['failed']} FPY={bs['fpy']*100:.1f}% top={bs['top']}({bs['topn']})")
