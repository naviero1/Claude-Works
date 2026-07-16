#!/usr/bin/env python3
"""
Build the Pelvic Block IQC Pareto + Root-Cause Framework workbook.

Ingests the rejected-pelvic-block inspection data (SH: Martins, kill 2026-07-08),
normalizes each free-text scrap reason into a controlled defect taxonomy, and
produces a multi-sheet Excel workbook:

  1. README            - how the framework works + process flow
  2. Inspection Log    - one row per physical block (master data, append future batches here)
  3. Defect Taxonomy   - controlled vocabulary + root-cause map (the framework)
  4. Pareto            - auto-calculating defect Pareto (chart) + supplier-station rollup
  5. Root Cause (5-Why)- structured RCA template seeded for the vital-few defects
  6. Dashboard         - batch KPI summary

Counts are driven by formulas that reference the Inspection Log, so adding new
inspection rows updates the Pareto and Dashboard automatically.
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, NamedStyle
from openpyxl.chart import BarChart, LineChart, Reference, Series
from openpyxl.chart.axis import ChartLines
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

# ----------------------------------------------------------------------------
# 1. CONTROLLED DEFECT TAXONOMY  (the framework's backbone)
# ----------------------------------------------------------------------------
# Each defect is mapped to: definition, severity, the supplier PROCESS STEP where
# it most likely originates, the primary supplier STATION, the 6M root-cause
# category, the likely physical MECHANISM, and a recommended corrective action.
#
# Process stations (supplier / slaughterhouse side, upstream of us):
#   S1 Sticking / Bleeding      - exsanguination
#   S2 Bung dropping / Rodding  - rectum + pelvic loosening
#   S3 Evisceration             - belly opening, gut & pluck removal (knife + traction)
#   S4 Carcass splitting        - pelvic / aitch-bone saw
#   S5 Handling & Pit drop      - post-evisceration handling, drop to pit, collection
#   S6 Live animal / physiology - pre-slaughter condition
#
# columns: code, name, definition, severity, process_step, station_code, station_name,
#          rootcause_6m, mechanism, corrective_action, log_col
TAXONOMY = [
    ("D1", "Ureters not embedded",
     "Ureter(s) dislodged/stripped from the surrounding pelvic fat & fascia; no longer seated in tissue.",
     "Major",
     "Gut/pluck removal (traction) + pit handling",
     "S3", "Evisceration",
     "Method / Handling",
     "Tensile traction: block pulled/stripped so fascia separates from ureter; over-trim.",
     "Standardize gut-pull technique & pull-force; reduce stripping of perirenal fat; gentler drop to pit.",
     "L"),
    ("D2", "Ureter cut / severed",
     "Ureter partially or fully transected (sharp cut edge).",
     "Major",
     "Evisceration knife / splitting saw",
     "S3", "Evisceration",
     "Machine / Method",
     "Sharp laceration by evisceration knife or off-line pelvic saw path.",
     "Retrain knife path around pelvic organs; verify saw alignment through symphysis.",
     "M"),
    ("D3", "Ureter missing",
     "One ureter (left or right) absent from the block.",
     "Major",
     "Bung dropping / splitting (over-cut) or lost in handling",
     "S2", "Bung dropping",
     "Method / Handling",
     "Over-aggressive bung/pelvic cut removes ureter, or ureter lost during drop/collection.",
     "Tighten bung-dropping cut boundary; audit pit collection for detached tissue.",
     "N"),
    ("D4", "Suspensory ligaments damaged",
     "Suspensory ligament(s) of the pelvic block torn/frayed.",
     "Major",
     "Gut pull (traction) + handling",
     "S3", "Evisceration",
     "Method / Handling",
     "Excessive pull force / rough handling tears ligament attachments.",
     "Control pull-force & angle on gut set removal; handle block by support surface, not by ligaments.",
     "O"),
    ("D5", "Urethra cut",
     "Urethra transected (sharp cut).",
     "Major",
     "Carcass splitting saw / bung dropping",
     "S4", "Carcass splitting",
     "Machine / Method",
     "Splitting saw off-center through pelvis, or bung-drop cut catches urethra.",
     "Center pelvic split on symphysis; calibrate/align splitting saw; slow through pelvic zone.",
     "P"),
    ("D6", "Membrane damage in critical area",
     "Hole/tear in the membrane separating bowel from the pelvic organs, in the critical (functional) zone.",
     "Critical",
     "Evisceration knife technique / bung dropping",
     "S3", "Evisceration",
     "Method / Man",
     "Knife nick or tensile tear of membrane during gut removal / bung loosening.",
     "Retrain evisceration knife depth & path; slow line in pelvic zone; blunt-dissect where possible.",
     "Q"),
    ("D7", "Bladder deformed / deformed attachment",
     "Bladder misshapen or attachment distorted.",
     "Minor",
     "Live-animal fill state / handling pressure",
     "S6", "Live / physiology",
     "Material / Handling",
     "Distended (full) bladder at slaughter, or compression during handling.",
     "Manage lairage/feed-water timing to reduce bladder fill; avoid compressing block.",
     "R"),
    ("D8", "Bowel cut / opened / separated",
     "Bowel integrity breached (cut open or separated from block).  FOOD-SAFETY / contamination risk.",
     "Critical",
     "Evisceration / bung dropping",
     "S3", "Evisceration",
     "Method / Man",
     "Knife slip or aggressive bung separation opens/severs bowel.",
     "Reinforce bung-bagging/tie-off; retrain knife path; treat as contamination CCP at supplier.",
     "S"),
    ("D9", "Blood clots",
     "Retained blood clots in the tissue block.",
     "Minor",
     "Sticking / bleeding efficiency",
     "S1", "Sticking / Bleeding",
     "Method",
     "Incomplete exsanguination (stick placement / stun-to-stick interval / bleed time).",
     "Verify stick placement & bleed-out time; check stun-to-stick interval.",
     "T"),
    ("D10", "Broad ligament hole / tear",
     "Large hole/tear in the broad ligament.",
     "Major",
     "Evisceration / bung dropping",
     "S3", "Evisceration",
     "Method / Handling",
     "Traction tear or knife nick near broad ligament during gut removal.",
     "Control pull-force; retrain knife path near broad ligament.",
     "U"),
]
CODE_TO_COL = {t[0]: t[10] for t in TAXONOMY}   # defect code -> Inspection Log column letter

# ----------------------------------------------------------------------------
# 2. RAW INSPECTION ROWS (verbatim scrap reasons) -> defect tag expansion
# ----------------------------------------------------------------------------
# (n_blocks, verbatim_reason, [defect codes present])
# The one PASS block is added separately.
RAW_ROWS = [
    (1, "Large hole near right broad ligament and membrane causing seperation of bowel and ureters.", ["D10", "D6", "D8"]),
    (1, "2 inch damage on membrane seperating bowel in critical area", ["D6", "D8"]),
    (1, "urethra is cut", ["D5"]),
    (1, "bladder deformed 12 inch deformed attachment", ["D7"]),
    (1, "suspensory ligaments damaged, ureters not embedded", ["D4", "D1"]),
    (1, "ureters not embedded, suspensory ligaments damaged, cut urethra", ["D1", "D4", "D5"]),
    (1, "ureters not embedded and cut, suspensory ligaments damaged, cut urethra", ["D1", "D2", "D4", "D5"]),
    (1, "ureters not embedded, suspensory ligaments damaged, cut urethra, membrane damaged in critical area", ["D1", "D4", "D5", "D6"]),
    (1, "suspensory ligaments damaged, ureters not embedded", ["D4", "D1"]),
    (1, "ureters not embedded, suspensory ligaments damaged, cut urethra, membrane damaged in critical area", ["D1", "D4", "D5", "D6"]),
    (1, "left ureter is missing", ["D3"]),
    (2, "ureters not embedded, suspensory ligaments damaged, membrane damaged in critical area", ["D1", "D4", "D6"]),
    (1, "left ureter missing, blood clots", ["D3", "D9"]),
    (1, "right ureter missing, membrane damage in critical area", ["D3", "D6"]),
    (1, "membrane damage in critical area, ureters not embedded", ["D6", "D1"]),
    (1, "membrane damage in critical area, ureters not embedded", ["D6", "D1"]),
    (1, "ureter cut, membrane damage in critital area, right ureter not embedded", ["D2", "D6", "D1"]),
    (1, "urethra cut, membrnae damage in critial area", ["D5", "D6"]),
    (1, "bowel is cut open", ["D8"]),
    (1, "urethra is cut, membrane damage in critical area", ["D5", "D6"]),
    (4, "membrane damage in critical area", ["D6"]),
]

# ----------------------------------------------------------------------------
# Batch metadata (from source tally sheet)
# ----------------------------------------------------------------------------
META = dict(
    insp_date="2026-07-10", kill_date="2026-07-08", harvest_date="2026-07-08",
    slaughterhouse="Martins", sh_tech="", inspector="",
    batch="12:30 PM - 12:45 PM", part_no="", part_name="Tiss, porcine, fem, Pelvic block",
    total_inspected=26, total_pass=1, total_fail=25,
)

# ----------------------------------------------------------------------------
# STYLES
# ----------------------------------------------------------------------------
NAVY = "1F3864"; BLUE = "305496"; LT_BLUE = "D9E1F2"; LT_BLUE2 = "EAF0FA"
GREY = "808080"; LT_GREY = "F2F2F2"; AMBER = "FFE699"; RED = "F4B183"; GREEN = "C6E0B4"
WHITE = "FFFFFF"

def font(sz=11, b=False, color="000000", italic=False):
    return Font(name="Calibri", size=sz, bold=b, color=color, italic=italic)

def fill(c):
    return PatternFill("solid", fgColor=c)

thin = Side(style="thin", color="BFBFBF")
med = Side(style="medium", color=BLUE)
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT = Alignment(horizontal="left", vertical="center", wrap_text=True)
LEFT_TOP = Alignment(horizontal="left", vertical="top", wrap_text=True)

def style_header(cell, fillc=BLUE, color=WHITE, sz=11):
    cell.font = font(sz, True, color)
    cell.fill = fill(fillc)
    cell.alignment = CENTER
    cell.border = BORDER

def title_block(ws, text, subtitle, ncols):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    c = ws.cell(1, 1, text)
    c.font = font(16, True, WHITE); c.fill = fill(NAVY); c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[1].height = 30
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    c2 = ws.cell(2, 1, subtitle)
    c2.font = font(10, False, WHITE, italic=True); c2.fill = fill(BLUE); c2.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[2].height = 18

wb = openpyxl.Workbook()

# ============================================================================
# SHEET 1: README
# ============================================================================
ws = wb.active
ws.title = "README"
ws.sheet_view.showGridLines = False
title_block(ws, "PELVIC BLOCK IQC — PARETO & ROOT-CAUSE FRAMEWORK",
            "Incoming Quality Control of rejected porcine femoral pelvic blocks  |  Purpose: pinpoint where defects originate at the supplier and drive corrective action upstream", 8)

readme = [
    ("", ""),
    ("PURPOSE", "H"),
    ("This workbook ingests IQC inspection results for rejected pelvic blocks, sorts the defects with a Pareto (which few defects cause most of the loss), and", "P"),
    ("maps every defect back to the point in the SUPPLIER's process where it is created — so corrective action can be taken BEFORE the tissue block reaches us.", "P"),
    ("", ""),
    ("THE PROCESS (where a defect can be born)  —  everything up to 'Delivered to us' is the supplier's to control", "H"),
    ("  Live animal  ->  S1 Sticking/Bleeding  ->  S2 Bung dropping/Rodding  ->  S3 Evisceration (knife + gut pull)  ->  S4 Carcass splitting (saw)  ->  S5 Handling & Pit drop  ->  Delivered to us", "FLOW"),
    ("                                                                                                                                                          |", "FLOW"),
    ("                                                                                                              OUR side ->  Harvest techs receive block from pit  ->  spec-out / accept decision  ->  IQC inspection (this data)", "FLOW"),
    ("", ""),
    ("HOW THE SHEETS FIT TOGETHER", "H"),
    ("  1. Inspection Log   Master data — ONE ROW PER BLOCK. Each free-text scrap reason is normalized into 1/0 flags against the defect taxonomy. Append future batches here.", "P"),
    ("  2. Defect Taxonomy  The controlled vocabulary (D1–D10) + the root-cause map: each defect -> process step, supplier station, 6M cause, mechanism, corrective action.", "P"),
    ("  3. Pareto           Auto-calculating defect Pareto (bar + cumulative line) and a rollup by SUPPLIER STATION — the single most useful view for the supplier conversation.", "P"),
    ("  4. Root Cause 5-Why  A structured RCA template, pre-seeded for the vital-few defects, with a Lessons-Learned column for you to fill in over time.", "P"),
    ("  5. Dashboard        Batch KPI summary (yield, top defect, food-safety flags).", "P"),
    ("", ""),
    ("HOW TO ADD THE NEXT INSPECTION (keep the framework alive)", "H"),
    ("  a. Go to 'Inspection Log'. Add one row per inspected block (copy the metadata columns, set Result = Pass/Fail, paste the verbatim reason).", "P"),
    ("  b. Put a 1 in each defect column (D1–D10) that applies to that block; leave the rest blank/0. Use the dropdown list; if a NEW defect appears, add it to 'Defect Taxonomy' first.", "P"),
    ("  c. The Pareto and Dashboard recalculate automatically. (Re-sort the Pareto table high->low if the ranking changes — counts update live, row order does not.)", "P"),
    ("", ""),
    ("READING THE PARETO", "H"),
    ("  The 'vital few' are the leftmost bars whose cumulative line reaches ~80%. Fix those first. For THIS batch they are membrane damage, ureters-not-embedded,", "P"),
    ("  suspensory-ligament damage and urethra cuts — and ~77% of all defects trace to ONE supplier station: Evisceration.", "P"),
    ("", ""),
    ("SEVERITY KEY", "H"),
    ("  Critical = function-destroying or food-safety (e.g. bowel breach = contamination).   Major = block rejected.   Minor = cosmetic / recoverable.", "P"),
    ("", ""),
    ("SOURCE", "H"),
    ("  IQC Tally Sheet — SH: Martins — Kill/Harvest 2026-07-08 — 26 inspected, 1 pass, 25 fail (First Pass Yield 3.8%).  Original file kept as source_IQC_Martins_failed_blocks_2026-07-08.xlsx", "P"),
]
r = 4
for text, kind in readme:
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8)
    c = ws.cell(r, 1, text)
    if kind == "H":
        c.font = font(11, True, NAVY); c.fill = fill(LT_BLUE)
        c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        ws.row_dimensions[r].height = 18
    elif kind == "FLOW":
        c.font = font(9, True, "1F4E5F"); c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    else:
        c.font = font(10, False, "222222"); c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    r += 1
ws.column_dimensions["A"].width = 20
for col in "BCDEFGH":
    ws.column_dimensions[col].width = 20
ws.sheet_view.zoomScale = 110

# ============================================================================
# SHEET 2: INSPECTION LOG  (master data, one row per block)
# ============================================================================
log = wb.create_sheet("Inspection Log")
log.sheet_view.showGridLines = False
meta_cols = ["Block ID", "Insp. Date", "Kill Date", "Harvest Date", "Slaughterhouse",
             "SH Tech", "Inspector", "Batch/Lot", "Part Name", "Result", "Verbatim Scrap Reason"]
defect_codes = [t[0] for t in TAXONOMY]
headers = meta_cols + defect_codes + ["# Defects"]
title_block(log, "INSPECTION LOG  (master data — one row per inspected block)",
            "Append future inspections below. Put 1 in each defect column that applies. Counts on Pareto/Dashboard update automatically.", len(headers))

hdr_row = 4
for j, h in enumerate(headers, start=1):
    style_header(log.cell(hdr_row, j, h))
log.row_dimensions[hdr_row].height = 28

# build block rows
rows = []
blk = 1
for n, reason, codes in RAW_ROWS:
    for _ in range(n):
        rows.append((f"B{blk:03d}", reason, "Fail", set(codes)))
        blk += 1
# the single pass block
rows.append((f"B{blk:03d}", "", "Pass", set()))

ncol_defect_start = len(meta_cols) + 1
data_first = hdr_row + 1
for i, (bid, reason, result, codes) in enumerate(rows):
    rr = data_first + i
    vals = [bid, META["insp_date"], META["kill_date"], META["harvest_date"], META["slaughterhouse"],
            META["sh_tech"], META["inspector"], META["batch"], META["part_name"], result, reason]
    for j, v in enumerate(vals, start=1):
        c = log.cell(rr, j, v)
        c.border = BORDER
        c.font = font(10)
        c.alignment = LEFT_TOP if j == 11 else CENTER
        if j == 10:  # Result
            c.font = font(10, True, "833C00" if result == "Fail" else "375623")
            c.fill = fill(RED if result == "Fail" else GREEN)
    for k, code in enumerate(defect_codes):
        c = log.cell(rr, ncol_defect_start + k, 1 if code in codes else None)
        c.border = BORDER; c.alignment = CENTER; c.font = font(10, True, "C00000")
        if code in codes:
            c.fill = fill(AMBER)
    # # Defects formula
    dc0 = get_column_letter(ncol_defect_start)
    dc1 = get_column_letter(ncol_defect_start + len(defect_codes) - 1)
    tot = log.cell(rr, len(headers))
    tot.value = f"=SUM({dc0}{rr}:{dc1}{rr})"
    tot.border = BORDER; tot.alignment = CENTER; tot.font = font(10, True)
    log.row_dimensions[rr].height = 30 if result == "Fail" else 16

data_last = data_first + len(rows) - 1

# widths
widths = {"A":9,"B":11,"C":11,"D":12,"E":13,"F":9,"G":10,"H":16,"I":24,"J":8,"K":48}
for col, w in widths.items():
    log.column_dimensions[col].width = w
for k in range(len(defect_codes)):
    log.column_dimensions[get_column_letter(ncol_defect_start + k)].width = 6
log.column_dimensions[get_column_letter(len(headers))].width = 9
log.freeze_panes = log.cell(data_first, 2)

# data validation: Result dropdown
dv = DataValidation(type="list", formula1='"Pass,Fail"', allow_blank=True)
log.add_data_validation(dv)
dv.add(f"J{data_first}:J{data_first+400}")
# defect flags 0/1
dv2 = DataValidation(type="list", formula1='"1"', allow_blank=True)
log.add_data_validation(dv2)
dv2.add(f"{get_column_letter(ncol_defect_start)}{data_first}:{get_column_letter(ncol_defect_start+len(defect_codes)-1)}{data_first+400}")

# ============================================================================
# SHEET 3: DEFECT TAXONOMY & ROOT-CAUSE MAP  (the framework)
# ============================================================================
tax = wb.create_sheet("Defect Taxonomy")
tax.sheet_view.showGridLines = False
tax_headers = ["Code", "Defect Mode", "Definition", "Severity", "Likely Process Step (where it's born)",
               "Supplier Station", "Root-Cause Category (6M)", "Likely Mechanism",
               "Recommended Corrective Action (to supplier)", "Lessons Learned  (fill in over time)"]
title_block(tax, "DEFECT TAXONOMY & ROOT-CAUSE MAP",
            "The controlled vocabulary. Every scrap reason must map to a code here. This is where a defect is traced back to the supplier's process.", len(tax_headers))
hr = 4
for j, h in enumerate(tax_headers, start=1):
    style_header(tax.cell(hr, j, h))
tax.row_dimensions[hr].height = 30

sev_fill = {"Critical": "F4B183", "Major": "FFE699", "Minor": "D9E1F2"}
for i, t in enumerate(TAXONOMY):
    rr = hr + 1 + i
    code, name, defn, sev, step, scode, sname, cause, mech, action, _col = t
    row_vals = [code, name, defn, sev, step, f"{scode} {sname}", cause, mech, action, ""]
    for j, v in enumerate(row_vals, start=1):
        c = tax.cell(rr, j, v)
        c.border = BORDER; c.font = font(10)
        c.alignment = CENTER if j in (1, 4, 6) else LEFT_TOP
        if j == 1:
            c.font = font(11, True, NAVY)
        if j == 4:
            c.fill = fill(sev_fill[sev]); c.font = font(10, True, "833C00" if sev != "Minor" else "1F3864")
        if j == 10:
            c.fill = fill(LT_GREY)
    tax.row_dimensions[rr].height = 46
tax_widths = {"A":6,"B":24,"C":40,"D":9,"E":30,"F":18,"G":16,"H":38,"I":42,"J":30}
for col, w in tax_widths.items():
    tax.column_dimensions[col].width = w
tax.freeze_panes = tax.cell(hr + 1, 1)

# ============================================================================
# SHEET 4: PARETO
# ============================================================================
par = wb.create_sheet("Pareto")
par.sheet_view.showGridLines = False
title_block(par, "PARETO — DEFECT FREQUENCY & SUPPLIER-STATION ROLLUP",
            "Counts pull live from the Inspection Log. Fix the 'vital few' (cumulative line to ~80%) first. Re-sort high->low if ranking changes.", 6)

# ---- Defect Pareto table (sorted by CURRENT counts, formulas keep values live) ----
# Compute current counts to determine sort order
counts = {code: 0 for code in defect_codes}
for _, _, _, codes in rows:
    for cd in codes:
        counts[cd] += 1
order = sorted(defect_codes, key=lambda c: counts[c], reverse=True)
name_of = {t[0]: t[1] for t in TAXONOMY}

ph = 4
par.merge_cells(start_row=ph, start_column=1, end_row=ph, end_column=6)
c = par.cell(ph, 1, "A.  DEFECT PARETO  (by occurrence across all inspected blocks)")
c.font = font(11, True, NAVY); c.fill = fill(LT_BLUE); c.alignment = Alignment(horizontal="left", indent=1)
ph += 1
pareto_hdr = ["Rank", "Code", "Defect Mode", "Count", "% of Total", "Cumulative %"]
for j, h in enumerate(pareto_hdr, start=1):
    style_header(par.cell(ph, j, h))
par.row_dimensions[ph].height = 24

first = ph + 1
n = len(order)
# total defects formula range: sum of the whole defect block in the log
dc0 = get_column_letter(ncol_defect_start)
dc1 = get_column_letter(ncol_defect_start + len(defect_codes) - 1)
total_formula = f"SUM('Inspection Log'!{dc0}{data_first}:{dc1}{data_last+400})"
for i, code in enumerate(order):
    rr = first + i
    col_letter = CODE_TO_COL[code]
    cnt_formula = f"=SUM('Inspection Log'!{col_letter}{data_first}:{col_letter}{data_last+400})"
    par.cell(rr, 1, i + 1).alignment = CENTER
    par.cell(rr, 2, code).font = font(10, True, NAVY)
    par.cell(rr, 3, name_of[code])
    par.cell(rr, 4).value = cnt_formula
    par.cell(rr, 5).value = f"=D{rr}/{total_formula}"
    if i == 0:
        par.cell(rr, 6).value = f"=E{rr}"
    else:
        par.cell(rr, 6).value = f"=F{rr-1}+E{rr}"
    for j in range(1, 7):
        cc = par.cell(rr, j); cc.border = BORDER
        if j in (1, 2, 4): cc.alignment = CENTER
        if j == 3: cc.alignment = LEFT
        if j in (5, 6): cc.number_format = "0.0%"; cc.alignment = CENTER
        if j == 4: cc.font = font(10, True)
    # highlight vital few (cumulative <= ~80%)
    if counts and sum(counts[order[k]] for k in range(i+1)) / sum(counts.values()) <= 0.80 + 1e-9 or i == 0:
        par.cell(rr, 3).fill = fill(AMBER)
last = first + n - 1
# totals row
tr = last + 1
par.cell(tr, 3, "TOTAL").font = font(10, True)
par.cell(tr, 4).value = f"=SUM(D{first}:D{last})"
par.cell(tr, 4).font = font(10, True); par.cell(tr, 4).alignment = CENTER
for j in range(1, 7):
    par.cell(tr, j).fill = fill(LT_BLUE); par.cell(tr, j).border = BORDER
par.cell(tr, 5).value = f"=D{tr}/{total_formula}"; par.cell(tr,5).number_format="0.0%"; par.cell(tr,5).alignment=CENTER

# ---- Supplier-station rollup ----
sh = tr + 3
par.merge_cells(start_row=sh, start_column=1, end_row=sh, end_column=6)
c = par.cell(sh, 1, "B.  ROLLUP BY SUPPLIER STATION  (which station to fix first)")
c.font = font(11, True, NAVY); c.fill = fill(LT_BLUE); c.alignment = Alignment(horizontal="left", indent=1)
sh += 1
station_hdr = ["Station", "Station Name", "Defect Count", "% of Total", "Defect Codes", ""]
for j, h in enumerate(station_hdr[:5], start=1):
    style_header(par.cell(sh, j, h))
par.row_dimensions[sh].height = 24
# aggregate stations
from collections import defaultdict, OrderedDict
station_codes = defaultdict(list)
station_name = {}
for t in TAXONOMY:
    station_codes[t[5]].append(t[0]); station_name[t[5]] = t[6]
station_order = sorted(station_codes.keys(), key=lambda s: sum(counts[c] for c in station_codes[s]), reverse=True)
srow = sh + 1
for i, s in enumerate(station_order):
    rr = srow + i
    codes_here = station_codes[s]
    cnt_formula = "=" + "+".join(f"SUM('Inspection Log'!{CODE_TO_COL[c]}{data_first}:{CODE_TO_COL[c]}{data_last+400})" for c in codes_here)
    par.cell(rr, 1, s).font = font(10, True, NAVY); par.cell(rr,1).alignment=CENTER
    par.cell(rr, 2, station_name[s]).alignment = LEFT
    par.cell(rr, 3).value = cnt_formula; par.cell(rr,3).font=font(10,True); par.cell(rr,3).alignment=CENTER
    par.cell(rr, 4).value = f"=C{rr}/{total_formula}"; par.cell(rr,4).number_format="0.0%"; par.cell(rr,4).alignment=CENTER
    par.cell(rr, 5, ", ".join(codes_here)).alignment = LEFT
    for j in range(1, 6):
        par.cell(rr, j).border = BORDER
    if i == 0:
        for j in range(1, 6): par.cell(rr, j).fill = fill(RED)
slast = srow + len(station_order) - 1

par.column_dimensions["A"].width = 10
par.column_dimensions["B"].width = 22
par.column_dimensions["C"].width = 26
par.column_dimensions["D"].width = 13
par.column_dimensions["E"].width = 24
par.column_dimensions["F"].width = 10

# ---- Pareto chart ----
bar = BarChart()
bar.type = "col"; bar.style = 10
bar.title = "Defect Pareto — Rejected Pelvic Blocks (SH: Martins, 2026-07-08)"
bar.y_axis.title = "Defect count"
bar.x_axis.title = "Defect mode"
data_ref = Reference(par, min_col=4, min_row=first-1, max_row=last)   # include header for legend
cats_ref = Reference(par, min_col=3, min_row=first, max_row=last)
bar.add_data(data_ref, titles_from_data=True)
bar.set_categories(cats_ref)
bar.y_axis.majorGridlines = ChartLines()
bar.gapWidth = 40

line = LineChart()
cum_ref = Reference(par, min_col=6, min_row=first-1, max_row=last)
line.add_data(cum_ref, titles_from_data=True)
line.y_axis.axId = 200
line.y_axis.title = "Cumulative %"
line.y_axis.crosses = "max"
line.y_axis.number_format = "0%"
line.y_axis.scaling.min = 0
line.y_axis.scaling.max = 1
s = line.series[0]
s.smooth = False
s.marker.symbol = "circle"; s.marker.size = 5

bar.y_axis.crosses = "autoZero"
bar += line
bar.width = 24; bar.height = 12
par.add_chart(bar, "H4")

# station-rollup snapshot image (visual aid for the supplier conversation)
import os
from openpyxl.drawing.image import Image as XLImage
_img = "/home/user/Claude-Works/pelvic-block-iqc-pareto/Station_rollup_preview.png"
if os.path.exists(_img):
    im = XLImage(_img)
    im.width = int(im.width * 0.62); im.height = int(im.height * 0.62)
    par.add_image(im, "H28")

# ============================================================================
# SHEET 5: ROOT CAUSE 5-WHY
# ============================================================================
rc = wb.create_sheet("Root Cause 5-Why")
rc.sheet_view.showGridLines = False
rc_headers = ["Code", "Defect Mode", "Why 1", "Why 2", "Why 3", "Why 4", "Why 5 (root cause)",
              "Countermeasure (at supplier)", "Owner", "Target Date", "Status", "Lessons Learned"]
title_block(rc, "ROOT CAUSE — 5-WHY WORKSHEET",
            "Seeded with a starting hypothesis chain for the vital-few defects. Drive each chain to a true root cause with the supplier, then log the countermeasure & lesson.", len(rc_headers))
hr = 4
for j, h in enumerate(rc_headers, start=1):
    style_header(rc.cell(hr, j, h))
rc.row_dimensions[hr].height = 26

# seed the vital few (top 4) + the food-safety critical (bowel)
seed = {
    "D6": ["Membrane torn/holed in critical area",
           "Knife path too deep / tensile tear during gut pull",
           "Evisceration technique not standardized for pelvic zone",
           "No defined knife depth/path SOP + line speed pressure",
           "(confirm w/ supplier) training + line-speed control gap",
           "Retrain knife depth & path in pelvic zone; blunt-dissect; slow line through pelvic cut",
           "SH Martins - Evisceration lead", "", "Open", ""],
    "D1": ["Ureters not embedded in tissue",
           "Fascia/perirenal fat stripped away from ureter",
           "Excessive pull force / over-trim during gut set removal",
           "Pull technique & trim spec not controlled",
           "(confirm) handling standard missing",
           "Standardize pull-force & angle; limit fat stripping; gentler pit drop",
           "SH Martins - Evisceration lead", "", "Open", ""],
    "D4": ["Suspensory ligaments torn/frayed",
           "Block pulled/handled by the ligaments",
           "Rough handling + high traction on removal",
           "No 'support-surface' handling rule",
           "(confirm) handling standard missing",
           "Handle block by support surface, not ligaments; control pull force",
           "SH Martins - Evisceration lead", "", "Open", ""],
    "D5": ["Urethra cut",
           "Sharp transection through pelvic zone",
           "Splitting saw off-center / bung-drop cut catches urethra",
           "Saw alignment & pelvic-split centering not verified",
           "(confirm) saw calibration + technique gap",
           "Center split on symphysis; calibrate/align saw; slow through pelvic zone",
           "SH Martins - Splitting lead", "", "Open", ""],
    "D8": ["Bowel cut open / separated (FOOD SAFETY)",
           "Knife slip or aggressive bung separation opens bowel",
           "Bung not adequately bagged/tied before cut",
           "Bung-dropping CCP not robust",
           "(confirm) contamination-control gap at bung station",
           "Reinforce bung bag/tie-off; retrain knife path; treat as contamination CCP",
           "SH Martins - Bung/Evisc. lead", "", "Open", ""],
}
seed_order = ["D6", "D1", "D4", "D5", "D8"]
for i, code in enumerate(seed_order):
    rr = hr + 1 + i
    vals = [code, name_of[code]] + seed[code]
    for j, v in enumerate(vals, start=1):
        c = rc.cell(rr, j, v)
        c.border = BORDER; c.font = font(9)
        c.alignment = CENTER if j in (1, 9, 10, 11) else LEFT_TOP
        if j == 1: c.font = font(11, True, NAVY)
        if j == 2: c.font = font(9, True)
        if j == 7: c.fill = fill(AMBER)          # root cause column
        if j == 8: c.fill = fill(GREEN)          # countermeasure
        if j == 11:
            c.fill = fill("FFF2CC"); c.font = font(9, True, "833C00")
        if j == 12: c.fill = fill(LT_GREY)
    rc.row_dimensions[rr].height = 60
# a couple of blank rows for the remaining defects
for i in range(2):
    rr = hr + 1 + len(seed_order) + i
    for j in range(1, len(rc_headers) + 1):
        c = rc.cell(rr, j, None); c.border = BORDER
        if j == 7: c.fill = fill(AMBER)
        if j == 8: c.fill = fill(GREEN)
        if j == 12: c.fill = fill(LT_GREY)
    rc.row_dimensions[rr].height = 40

rc_widths = {"A":6,"B":22,"C":22,"D":22,"E":22,"F":20,"G":22,"H":30,"I":16,"J":12,"K":9,"L":26}
for col, w in rc_widths.items():
    rc.column_dimensions[col].width = w
rc.freeze_panes = rc.cell(hr + 1, 3)
# status dropdown
dv3 = DataValidation(type="list", formula1='"Open,In Progress,Verifying,Closed"', allow_blank=True)
rc.add_data_validation(dv3)
dv3.add(f"K{hr+1}:K{hr+40}")

# ============================================================================
# SHEET 6: DASHBOARD
# ============================================================================
dash = wb.create_sheet("Dashboard")
dash.sheet_view.showGridLines = False
title_block(dash, "DASHBOARD — BATCH SUMMARY",
            "SH: Martins  |  Kill/Harvest 2026-07-08  |  Batch 12:30–12:45 PM", 6)

result_col = "J"
kpis = [
    ("Blocks Inspected", f"=COUNTA('Inspection Log'!A{data_first}:A{data_last+400})-COUNTBLANK('Inspection Log'!A{data_first}:A{data_last+400})", "0"),
    ("Pass", f'=COUNTIF(\'Inspection Log\'!{result_col}{data_first}:{result_col}{data_last+400},"Pass")', "0"),
    ("Fail", f'=COUNTIF(\'Inspection Log\'!{result_col}{data_first}:{result_col}{data_last+400},"Fail")', "0"),
    ("First Pass Yield", f'=IFERROR(COUNTIF(\'Inspection Log\'!{result_col}{data_first}:{result_col}{data_last+400},"Pass")/(COUNTA(\'Inspection Log\'!A{data_first}:A{data_last+400})-COUNTBLANK(\'Inspection Log\'!A{data_first}:A{data_last+400})),0)', "0.0%"),
    ("Total Defect Occurrences", f"={total_formula}", "0"),
    ("Defects per Failed Block", f'=IFERROR({total_formula}/COUNTIF(\'Inspection Log\'!{result_col}{data_first}:{result_col}{data_last+400},"Fail"),0)', "0.00"),
]
kr = 4
dash.cell(kr, 1, "KEY METRICS").font = font(12, True, NAVY)
kr += 1
for label, formula, fmt in kpis:
    dash.cell(kr, 1, label).font = font(11, True, "222222")
    dash.cell(kr, 1).fill = fill(LT_BLUE); dash.cell(kr,1).alignment = Alignment(horizontal="left", indent=1); dash.cell(kr,1).border=BORDER
    vc = dash.cell(kr, 2); vc.value = formula; vc.number_format = fmt
    vc.font = font(13, True, NAVY); vc.alignment = CENTER; vc.fill = fill(LT_GREY); vc.border = BORDER
    dash.row_dimensions[kr].height = 22
    kr += 1

# top defect + food safety callouts
kr += 1
dash.cell(kr, 1, "TOP DEFECT (this batch)").font = font(12, True, NAVY); kr += 1
dash.cell(kr, 1, name_of[order[0]]).font = font(12, True, "833C00"); dash.cell(kr,1).fill=fill(AMBER)
dash.merge_cells(start_row=kr, start_column=1, end_row=kr, end_column=3)
dash.cell(kr,1).alignment = Alignment(horizontal="left", indent=1); dash.cell(kr,1).border=BORDER
kr += 1
dash.cell(kr, 1, "Dominant supplier station").font = font(11, True, NAVY); kr += 1
dash.cell(kr, 1, f"{station_order[0]} {station_name[station_order[0]]}  ->  primary target for corrective action").font = font(11, True, "833C00")
dash.merge_cells(start_row=kr, start_column=1, end_row=kr, end_column=4); dash.cell(kr,1).fill=fill(RED)
dash.cell(kr,1).alignment = Alignment(horizontal="left", indent=1); dash.cell(kr,1).border=BORDER
kr += 2
fs_codes = [t[0] for t in TAXONOMY if t[3] == "Critical"]
fs_formula = "=" + "+".join(f"SUM('Inspection Log'!{CODE_TO_COL[c]}{data_first}:{CODE_TO_COL[c]}{data_last+400})" for c in fs_codes)
dash.cell(kr, 1, "Critical / food-safety defect occurrences").font = font(11, True, "C00000")
dash.cell(kr, 1).fill = fill(LT_BLUE); dash.cell(kr,1).alignment=Alignment(horizontal="left",indent=1); dash.cell(kr,1).border=BORDER
vc = dash.cell(kr, 2); vc.value = fs_formula; vc.font = font(13, True, "C00000"); vc.alignment=CENTER; vc.border=BORDER
kr += 1
dash.cell(kr, 1, "  (Critical codes: " + ", ".join(fs_codes) + " — membrane damage & bowel breach)").font = font(9, italic=True, color=GREY)

dash.column_dimensions["A"].width = 34
dash.column_dimensions["B"].width = 16
for col in "CDEF":
    dash.column_dimensions[col].width = 14

# ----------------------------------------------------------------------------
out = "/home/user/Claude-Works/pelvic-block-iqc-pareto/Pelvic_Block_IQC_Pareto_RootCause.xlsx"
wb.save(out)
print("SAVED:", out)
print("Blocks:", len(rows), "| Fail:", sum(1 for r in rows if r[2]=="Fail"), "| Pass:", sum(1 for r in rows if r[2]=="Pass"))
print("Defect counts:", {c: counts[c] for c in order})
print("Total defect occurrences:", sum(counts.values()))
print("Station rollup:", {s: sum(counts[c] for c in station_codes[s]) for s in station_order})
