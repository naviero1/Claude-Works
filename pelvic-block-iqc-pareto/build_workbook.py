#!/usr/bin/env python3
"""
Build the Pelvic Block IQC Pareto + Root-Cause Framework workbook.

Ingests rejected-pelvic-block IQC inspection data (SH: Martins), normalizes each
free-text scrap reason into a controlled defect taxonomy, and produces a
multi-sheet Excel workbook:

  1. README              - how the framework works + process flow
  2. Inspection Log      - one row per physical block (master data, append future batches here)
  3. Defect Taxonomy     - controlled vocabulary + root-cause map (the framework)
  4. Pareto              - auto-calculating defect Pareto (chart) + supplier-station rollup
  5. Root-Cause Deep-Dive- pork evisceration process study; damage-signature diagnostic
  6. Root Cause (5-Why)  - structured RCA template seeded for the vital-few + new defects
  7. Dashboard           - combined KPIs + per-batch breakdown
  8. Yield & Alignment   - good-pelvic rate across the board + harvest-tech / inspector alignment

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
     "Major", "Evisceration traction (gut-set withdrawal)", "S3", "Evisceration",
     "Method / Handling",
     "The ureter runs retroperitoneally in sublumbar fat (ventral to psoas, through the lateral bladder ligaments); caudo-ventral pull on the gut set peels it out of that fat bed intact-but-loose.",
     "Cut the ureters & sublumbar attachments BEFORE withdrawing the gut set (per hand-slaughter standard); slower, controlled set removal; gentler pit drop."),
    ("D2", "Ureter cut / severed",
     "Ureter partially or fully transected / cut off (sharp cut edge).",
     "Major", "Bung/aitch coring, split saw, or traction avulsion", "S3", "Evisceration",
     "Machine / Method",
     "Coring knife/aitch blade cuts the pelvic ureter (step 8); split saw shears it if off-center (11); over-pull avulses it at the narrow external-iliac crossing (10).",
     "Coring depth/axis control; verify aitch-blade & split-saw alignment; cut-don't-over-pull the gut set."),
    ("D3", "Ureter missing",
     "One ureter (left or right) absent from the block.",
     "Major", "Bung/aitch over-cut or lost in the dropped set", "S2", "Bung + aitch bone",
     "Method / Handling",
     "Aitch/bung over-cut removes the distal ureter, or it avulses at the iliac crossing and is lost in the dropped gut set / pit.",
     "Tighten bung/aitch cut boundary & coring axis; audit pit collection for detached tissue."),
    ("D4", "Suspensory ligaments damaged",
     "Suspensory ligament(s) torn/frayed or holed (incl. bladder suspensory ligament).",
     "Major", "Evisceration traction (gut-set withdrawal)", "S3", "Evisceration",
     "Method / Handling",
     "The bladder is slung by a median ligament (ventral) & paired lateral ligaments (dorsolateral, carrying the ureters); traction on the gut set tears these off the bladder/body wall; the midline knife/saw severs the median ligament.",
     "Handle the block by a support surface, not by the ligaments; control pull-force & angle; cut attachments first."),
    ("D5", "Urethra breach (cut / laceration / hole / separation)",
     "Urethra transected, lacerated, perforated or separated (incl. hole in distal urethra).",
     "Major", "Aitch-bone cut & carcass split saw (midline)", "S4", "Carcass splitting",
     "Machine / Method",
     "The urethra sits on the midline directly under the pubic symphysis — in the path of BOTH the aitch-bone cut (step 8) and the split saw (step 11); a midline pizzle cut severs the penile urethra in barrows.",
     "Center the pelvic split on the symphysis; calibrate/align split saw & guide; verify aitch-blade alignment; size-class sorting; keep the pizzle cut off-center."),
    ("D6", "Membrane damage in critical area",
     "Hole/tear in the mesentery membrane separating bowel from pelvic organs, in the critical zone (>1.5\").",
     "Critical", "Evisceration traction (gut-set withdrawal)", "S3", "Evisceration",
     "Method / Man",
     "The thin, fenestrated mesentery/broad-ligament membrane is the weakest element under traction and tears/holes first — especially where fingers/hook engage it to pull, or where the knife releases the set.",
     "Cut membrane attachments before pulling; blunt-dissect; slow the line through the pelvic zone; ergonomic relief so operators aren't yanking to keep pace."),
    ("D7", "Bladder deformed / deformed attachment",
     "Bladder misshapen or attachment distorted.",
     "Minor", "Live-animal fill state / handling pressure", "S6", "Live / physiology",
     "Material / Handling",
     "Distended (full) bladder at slaughter, or compression/traction on the attachment during handling.",
     "Manage lairage feed/water withdrawal (fasting) to empty the bladder; avoid compressing the block."),
    ("D8", "Bowel / colon / rectum breach",
     "Bowel integrity breached - cut, hole, or separation of colon/rectum. FOOD-SAFETY / contamination risk.",
     "Critical", "Bung margin / belly-opening knife / traction", "S3", "Evisceration",
     "Method / Man",
     "A <1/2\" circumanal margin nicks the rectum (step 8); the knife perforates the colon at belly opening (step 9); pull separates colon from rectum (step 10). Bung not sealed before withdrawal.",
     "Hold a >=1/2\" circumanal margin; seal/bag the bung BEFORE pulling; retrain knife path; treat as a contamination CCP."),
    ("D9", "Blood clots",
     "Retained blood clots / blood-splash speckle in the tissue block.",
     "Minor", "Stunning + sticking (stun-to-stick interval)", "S1", "Sticking / Bleeding",
     "Method",
     "Electrical-stun blood-pressure spike + a long/variable stun-to-stick interval ruptures capillaries (splash/speckle) and leaves vessels filled; incomplete bleed-out.",
     "Shorten & stabilize the stun-to-stick interval; verify stick placement & bleed-out time; consider CO2 stun (fewer hemorrhages)."),
    ("D10", "Broad ligament hole / tear",
     "Large hole/tear in the broad ligament (mesometrium in gilts).",
     "Major", "Evisceration traction (gut-set withdrawal)", "S3", "Evisceration",
     "Method / Handling",
     "The broad ligament suspending the uterus/ovary is torn by the same caudo-ventral pull on the gut set; the ovarian suspensory ligament is a common tear point.",
     "Control pull-force; cut attachments before pulling; retrain knife path near the broad ligament."),
    ("D11", "Bladder neck separation",
     "Bladder detached/separated at the neck (bladder-urethra junction at the pelvic floor).",
     "Major", "Aitch-bone cut & split saw (symphysis plane)", "S4", "Carcass splitting",
     "Machine / Method",
     "The neck is sheared at the pubic-symphysis plane by the aitch cut / split saw, or avulsed by traction on the urethra/ligaments.",
     "Center the pelvic split; protect the bladder neck at the pelvic outlet; verify aitch-blade alignment; control traction."),
    ("D12", "Bladder cut / hole (breach)",
     "Bladder wall cut open or holed. Urine-contamination risk. Distinct from D7 (deformed) & D11 (neck separation).",
     "Major", "Belly opening (knife) - full-bladder risk", "S3", "Evisceration",
     "Machine / Method",
     "The knife tip enters the cavity and punctures a distended, thin-walled bladder (a full bladder sits abdominally, in the knife's path) instead of riding along the body wall.",
     "'Unzip' belly cut (handle inside, blade riding outward); sharper knives; fasting/feed-water withdrawal to empty the bladder before slaughter."),
    ("D13", "Block too short / undersized",
     "Harvested pelvic block dimensionally too short / fails the length template (insufficient tissue retained).",
     "Major", "Aitch/split cut height + harvester recovery boundary", "S3", "Evisceration",
     "Method / Man",
     "The distal urethra/bladder-neck was already transected high at the aitch-bone cut or split (steps 8/11), leaving insufficient distal length; or the harvester sets the cranial boundary too tight to the bladder.",
     "Define minimum block length & cut boundaries vs a template/gauge; align aitch/split to preserve distal urethra length; train the recovery boundary cut."),
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
    ("  1. Inspection Log      Master data — ONE ROW PER BLOCK. Each free-text scrap reason is normalized into 1/0 flags against the defect taxonomy. Append future batches here.", "P"),
    ("  2. Defect Taxonomy     Controlled vocabulary (D1–D13) + root-cause map: each defect -> process step, supplier station, 6M cause, mechanism, corrective action.", "P"),
    ("  3. Pareto              Auto-calculating defect Pareto (bar + cumulative line) and a rollup by SUPPLIER STATION — the key view for the supplier conversation.", "P"),
    ("  4. Root-Cause Deep-Dive  The pork evisceration process studied: where each defect is BORN, a damage-signature diagnostic, contributing factors, supplier questions, glossary.", "P"),
    ("  5. Root Cause 5-Why     Structured RCA template, seeded for the vital-few + new defects, with a Lessons-Learned column to fill in over time.", "P"),
    ("  6. Dashboard           Combined KPIs + a per-batch breakdown so you can watch the trend batch over batch.", "P"),
    ("  7. Yield & Alignment   Good-pelvic % across the board; what it may mean for harvest-tech training; and tech<->inspector alignment (with input cells).", "P"),
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
def _vals_only(num_fmt, size, color, position, bold=True):
    """Data labels that show ONLY the value (Excel otherwise adds series + category names)."""
    dl = DataLabelList()
    dl.showVal = True; dl.showSerName = False; dl.showCatName = False
    dl.showLegendKey = False; dl.showPercent = False; dl.showBubbleSize = False
    dl.numFmt = num_fmt; dl.position = position; dl.txPr = _txpr(size, color, bold=bold)
    return dl
def _no_labels():
    dl = DataLabelList()
    dl.showVal = False; dl.showSerName = False; dl.showCatName = False
    dl.showLegendKey = False; dl.showPercent = False; dl.showBubbleSize = False
    return dl

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
bs.dLbls = _vals_only("0", 1000, "404040", "outEnd")
bar.y_axis.title = "Defect count"; bar.y_axis.number_format = "0"; bar.y_axis.scaling.min = 0
bar.y_axis.majorGridlines = ChartLines(spPr=GraphicalProperties(ln=LineProperties(solidFill=C_GRID, w=6350)))
bar.y_axis.txPr = _txpr(); bar.y_axis.delete = False
bar.x_axis.delete = False; bar.x_axis.majorGridlines = None
bar.x_axis.txPr = _txpr(850, rot=-2700000)
bar.x_axis.spPr = GraphicalProperties(ln=LineProperties(solidFill="BFBFBF", w=9525))

line = LineChart()
line.add_data(Reference(par, min_col=6, min_row=first - 1, max_row=last), titles_from_data=True)
line.add_data(Reference(par, min_col=THR_COL, min_row=ph, max_row=last), titles_from_data=True)
cs = line.series[0]                                  # cumulative % — subtle reference, NO point labels
cs.graphicalProperties = GraphicalProperties(ln=LineProperties(solidFill=C_LINE, w=19050))
cs.marker = Marker(symbol="circle", size=5)
cs.marker.spPr = GraphicalProperties(solidFill=C_LINE, ln=LineProperties(solidFill="FFFFFF", w=9525))
cs.smooth = False
cs.dLbls = _no_labels()                              # declutter: exact %s live in the Pareto table, not on the line
ts = line.series[1]
_lp = LineProperties(solidFill="A6A6A6", w=9525); _lp.prstDash = "dash"
ts.graphicalProperties = GraphicalProperties(ln=_lp); ts.marker = Marker(symbol="none"); ts.smooth = False
ts.dLbls = _no_labels()
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
# SHEET 5: ROOT-CAUSE DEEP-DIVE  (pork evisceration process study)
# ============================================================================
dd = wb.create_sheet("Root-Cause Deep-Dive"); dd.sheet_view.showGridLines = False
DDN = 5
title_block(dd, "ROOT-CAUSE DEEP-DIVE — THE PORK EVISCERATION PROCESS",
            "Where each defect is BORN, before the block reaches the harvest tech. Read the damage 'signature' (Section D) to name the station.", DDN)

def dd_sec(r, text):
    dd.merge_cells(start_row=r, start_column=1, end_row=r, end_column=DDN)
    c = dd.cell(r, 1, text); c.font = font(11, True, WHITE); c.fill = fill(NAVY)
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1); dd.row_dimensions[r].height = 22
    return r + 1

def dd_row(r, cells, header=False, zebra=False, h=46, fillc=None):
    col = 1
    for text, span in cells:
        for k in range(span):
            cc = dd.cell(r, col + k); cc.border = BORDER
            if header: cc.fill = fill(BLUE)
            elif fillc: cc.fill = fill(fillc)
            elif zebra: cc.fill = fill(LT_GREY)
        c = dd.cell(r, col, text)
        if span > 1: dd.merge_cells(start_row=r, start_column=col, end_row=r, end_column=col + span - 1)
        if header: c.font = font(10, True, WHITE); c.alignment = CENTER
        else: c.font = font(9); c.alignment = LEFT_TOP
        col += span
    dd.row_dimensions[r].height = h
    return r + 1

def dd_text(r, text, bold=False, h=30, color="222222", fillc=None):
    dd.merge_cells(start_row=r, start_column=1, end_row=r, end_column=DDN)
    c = dd.cell(r, 1, text); c.font = font(10, bold, color); c.alignment = LEFT_TOP
    if fillc: c.fill = fill(fillc)
    dd.row_dimensions[r].height = h
    return r + 1

r = 4
# --- A. Orientation ---
r = dd_sec(r, "A.  WHERE YOUR PELVIC BLOCK COMES FROM")
r = dd_text(r, "Your pelvic block is NOT harvested as a designed unit. It is the caudal (tail) end of the 'gut set' (green offal) — the abdominal-pelvic digestive tract plus the urogenital organs (bladder, ureters, urethra, bladder neck, ligaments, membranes, adjacent colon/rectum) — that is dropped out of the carcass during EVISCERATION onto the viscera table ('the pit'). The supplier's harvester then recovers the pelvic portion from that dropped set.", h=60)
r = dd_text(r, "So almost every defect is inflicted during one of FOUR caudal kill-floor substeps — (1) bung + aitch-bone cut, (2) belly opening, (3) evisceration traction, (4) the split saw — or during the harvester's own boundary cut. The damage SIGNATURE (Section D) tells you which one.", bold=True, h=44, color=NAVY, fillc=LT_BLUE)
r += 1

# --- B. Process flow ---
r = dd_sec(r, "B.  THE PROCESS (stunning -> chilling) — steps 8-11 are the ones that touch the pelvic block")
r = dd_row(r, [("Step", 1), ("Operation", 2), ("Touches the pelvic block?", 2)], header=True, h=20)
flow = [
    ("1", "Stunning", "Indirect — drives blood splash / clot retention", False),
    ("2", "Sticking / bleeding (exsanguination)", "Indirect — stun-to-stick interval -> retained clots", False),
    ("3-6", "Scald -> dehair -> singe -> polish/wash", "No", False),
    ("7", "Head dropping", "No", False),
    ("8", "Bung dropping + AITCH-BONE opening", "YES - PRIMARY: rectum, bladder neck, urethra, distal ureters", True),
    ("9", "Belly + brisket opening", "YES - HIGH: bladder puncture; sets the plane the gut set is pulled through", True),
    ("10", "EVISCERATION (gut-set / green-offal withdrawal)", "YES - PRIMARY: strips ureters, tears membranes & ligaments", True),
    ("11", "Carcass SPLITTING (saw through spine + pelvis)", "YES - HIGH: off-center split shears urethra / bladder neck / ureter", True),
    ("12", "Final-rail trim & inspection", "Trimming can shorten attached urogenital tissue", False),
    ("13", "Chilling", "No", False),
]
for step, op, touch, hot in flow:
    r = dd_row(r, [(step, 1), (op, 2), (touch, 2)], h=26, fillc=(AMBER if hot else None))
r += 1

# --- C. The four caudal substeps -> what they create ---
r = dd_sec(r, "C.  THE FOUR CAUDAL SUBSTEPS  —  what each one creates, and how")
r = dd_row(r, [("Substep (station)", 1), ("Defects it creates", 1), ("Mechanism", 1), ("Damage signature", 1), ("Primary fix", 1)], header=True, h=30)
substeps = [
    ("Bung dropping + aitch-bone (S2, step 8)",
     "Rectum nick (D8); distal ureter cut/missing (D2/D3); urethra & bladder-neck cut (D5/D11)",
     "Coring knife too deep / off-axis; the aitch blade crosses the midline urethra & bladder neck",
     "Clean knife slit; fecal spill if rectum",
     "Coring depth/axis control; >=1/2\" circumanal margin; aitch-blade alignment; size-adaptive settings"),
    ("Belly + brisket opening (S3, step 9)",
     "Bladder hole (D12); median-ligament cut (D4)",
     "Knife tip stabs the distended bladder instead of riding the body wall",
     "Single clean slit; URINE spill",
     "'Unzip' handle-in belly cut; sharper knives; FAST the hogs to empty the bladder"),
    ("Evisceration traction (S3, step 10)",
     "Ureters not embedded (D1); mesentery / broad / suspensory tears (D6/D10/D4); avulsed ureter (D2)",
     "Caudo-ventral PULL peels the ureter out of its sublumbar fat bed; the thin membranes tear first",
     "Irregular, stretched, FRAYED tear; NO bone dust",
     "Cut ureters & attachments BEFORE pulling; slower set removal; ergonomic relief"),
    ("Carcass split saw (S4, step 11)",
     "Urethra / bladder-neck / ureter transection (D5/D11/D2)",
     "Saw through the pubic symphysis bisects the midline urogenital tissue; off-center shears one side",
     "Straight parallel KERF + bone dust; matching cut on the mirror side",
     "Saw/guide calibration; blade condition; size-class sorting"),
]
for a, b, c, d, e in substeps:
    r = dd_row(r, [(a, 1), (b, 1), (c, 1), (d, 1), (e, 1)], h=74, zebra=True)
r += 1

# --- D. Damage-signature diagnostic ---
r = dd_sec(r, "D.  DAMAGE-SIGNATURE DIAGNOSTIC  —  read the defect, name the station  (the most useful tool here)")
r = dd_row(r, [("What you see on the block", 2), ("What it means", 2), ("Look at this station", 1)], header=True, h=20)
sigs = [
    ("Straight, parallel-sided cut + bone dust/marrow; matching cut on the mirror side", "SAW cut", "S4 Carcass splitting"),
    ("Single clean slit, no bone dust", "KNIFE cut", "S2 Bung/aitch  or  S3 belly opening"),
    ("Irregular, stretched, FRAYED tear; no bone dust", "TRACTION tear", "S3 Evisceration (the pull)"),
    ("Petechiae / speckle in fat & connective tissue", "Blood splash", "S1 Stunning / sticking"),
    ("Fecal spill at the cut", "Rectum / colon breach", "S2 bung margin  /  S3 belly knife"),
    ("Urine spill at the cut", "Bladder breach", "S3 belly opening (full bladder)"),
    ("Missing distal urethra / short block", "Cut too high upstream", "S2 aitch / S4 split, then harvest boundary"),
]
for s, m, st in sigs:
    r = dd_row(r, [(s, 2), (m, 2), (st, 1)], h=30, zebra=True)
r += 1

# --- E. Contributing factors ---
r = dd_sec(r, "E.  CONTRIBUTING FACTORS  —  track these as covariates (by shift, station, hog weight class)")
r = dd_row(r, [("Factor", 1), ("Why it matters", 2), ("What to do / track", 2)], header=True, h=20)
factors = [
    ("Line speed", "NSIS removed the federal max line-speed cap; a faster line = rushed coring margins, off-center saw, more yanking", "Correlate defect rate with line speed / shift; ergonomic relief"),
    ("Hog size variability", "Bung / aitch / saw are set for an 'average' pelvis and mis-locate on off-size hogs", "Size-class sorting; size-adaptive tool settings; track defects by weight class"),
    ("Bladder fill (fasting)", "A full bladder is abdominal & thin-walled, in the knife's path; fasting empties it (~70% of contamination variance)", "Enforce feed/water withdrawal; verify lairage time; track by fasting time"),
    ("Stun-to-stick interval", "Long / variable interval -> blood splash & retained clots (D9)", "Shorten & stabilize the interval; consider CO2 stun"),
    ("Knife sharpness", "A dull knife needs more force -> over-travel into bladder / urethra / ureter", "Steel/replace on schedule; sharpness checks"),
    ("Saw alignment / calibration", "Off-center / worn saw shears the midline urogenital tissue", "Calibrate guide & blade; preventive-maintenance schedule"),
    ("Operator training / fatigue", "Margin-setting, the 'unzip' cut, and the cut-vs-yank decision are all skill & attention dependent", "Train the four substeps; rotate to manage fatigue; track by station/shift"),
]
for f, w, t in factors:
    r = dd_row(r, [(f, 1), (w, 2), (t, 2)], h=40, zebra=True)
r += 1

# --- F. Take to the supplier ---
r = dd_sec(r, "F.  TAKE TO THE SUPPLIER  —  walk the line and ask / observe")
supplier_q = [
    ("Bung / aitch (S2):", "What coring tool & margin? Is the bung sealed/bagged BEFORE withdrawal? Is aitch-blade alignment checked per hog? Size-adaptive?"),
    ("Belly opening (S3):", "Is the 'unzip' (handle-in) technique used? Knife-sharpening schedule? What is the fasting / feed-water-withdrawal time before slaughter?"),
    ("Traction (S3):", "Are the ureters & sublumbar attachments CUT before the gut set is pulled, or yanked? Line speed at evisceration? Operator ergonomics?"),
    ("Split saw (S4):", "How is the split centered? Guide/blade calibration & PM frequency? Are hogs sorted by size class?"),
    ("Cross-cut:", "Can they share defect data by shift, station, and hog weight class so we can correlate?"),
]
for lab, q in supplier_q:
    r = dd_row(r, [(lab, 1), (q, 4)], h=32, zebra=True)
r += 1

# --- G. Glossary ---
r = dd_sec(r, "G.  GLOSSARY  (use the right terms with the supplier)")
gloss = [
    ("Aitch bone", "The pelvic bone / pubic symphysis. 'Opening the aitch' = splitting the symphysis on the midline to open the pelvic canal."),
    ("Bung", "The terminal rectum / anus. 'Bunging' / 'bung dropping' = coring it free of the pelvic wall and sealing it (tie / clip / bag)."),
    ("Rodding", "Inserting a rod to free & seal a tube — classically the weasand (esophagus) — before the pull. A 'rodding gun' does the coring/sealing."),
    ("Weasand", "The esophagus (industry term)."),
    ("Pluck", "The thoracic organ set removed together — heart, lungs, liver, trachea ('red offal')."),
    ("Gut set / green offal", "The abdominal-pelvic digestive tract removed as a unit (stomach, intestines, rectum), carrying the bladder/urogenital organs. Your block is its caudal end."),
    ("Brisket cut", "The cut that opens the sternum / chest to access the pluck."),
    ("Pizzle", "The penis (barrows); in the pig it is the extrapelvic continuation of the urethra, so a mishandled pizzle cut is a urethra defect."),
    ("Split / sides", "Sawing the carcass into two 'sides' down the spine and through the pelvis."),
]
for term, mean in gloss:
    r = dd_row(r, [(term, 1), (mean, 4)], h=28, zebra=True)
r += 1
r = dd_text(r, "Process grounded in the USDA-FSIS swine HACCP model, Purdue Extension AS-671-W hand-slaughter guide, the FAO slaughter manual, Frontmatec/DMRI/Marel equipment references, and porcine pelvic anatomy (ureter retroperitoneal course; bladder median/lateral ligaments; midline urethra under the pubic symphysis). Defect->substep attributions are engineering inferences — validate them against your incoming-defect photos and a walk of the supplier's evisceration & splitting stations.", h=56, color=GREY)

for col, w in {"A": 21, "B": 30, "C": 31, "D": 25, "E": 29}.items():
    dd.column_dimensions[col].width = w
dd.freeze_panes = dd.cell(4, 1)

# ============================================================================
# SHEET 6: ROOT CAUSE 5-WHY
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
    "D6": ["Hole/tear in mesentery membrane, critical zone (>1.5\")",
           "The thin fenestrated membrane is the weakest element under traction — it tears first",
           "Gut set pulled caudo-ventrally; fingers/hook engage the membrane to pull",
           "'Pull-don't-cut' evisceration; attachments not released first; line-speed pressure",
           "(confirm) no cut-first SOP for pelvic attachments + speed/ergonomic load on eviscerator",
           "Cut membrane attachments BEFORE pulling; blunt-dissect; slow line through pelvic zone; ergonomic relief",
           "SH Martins - Evisceration lead", "", "Open", ""],
    "D1": ["Ureter lying free, its fat bed empty (not embedded)",
           "Retroperitoneal ureter (in sublumbar fat) peeled out of its bed during the pull",
           "Gut set withdrawn WITHOUT first releasing ureter / sublumbar attachments",
           "Hand-slaughter standard ('cut the ureters, don't yank') not applied on the line",
           "(confirm) cut-first standard missing; speed rewards pulling over cutting",
           "Cut ureters & sublumbar attachments before withdrawing the set; controlled removal; gentler pit drop",
           "SH Martins - Evisceration lead", "", "Open", ""],
    "D5": ["Urethra cut / laceration / hole / separation",
           "The urethra sits on the midline directly under the pubic symphysis",
           "In the plane of BOTH the aitch-bone cut and the split saw; off-axis / over-deep cut hits it",
           "Saw/guide & aitch-blade alignment not verified per hog size; size variability",
           "(confirm) size-adaptive settings + saw calibration gap",
           "Center split on symphysis; calibrate saw/guide; verify aitch-blade; size-class sorting",
           "SH Martins - Splitting / Bung lead", "", "Open", ""],
    "D8": ["Rectum / colon breached (FOOD SAFETY)",
           "<1/2\" circumanal margin nicks rectum; knife perforates colon; pull separates colon",
           "Coring margin too tight at speed; bung not sealed before the pull",
           "Margin/seal SOP not enforced; bung-dropping CCP not robust",
           "(confirm) contamination-control gap at the bung/aitch station + speed",
           "Hold >=1/2\" margin; seal/bag bung BEFORE pulling; retrain knife path; contamination CCP",
           "SH Martins - Bung/Evisc. lead", "", "Open", ""],
    "D4": ["Median/lateral bladder & suspensory ligaments torn",
           "Traction on the gut set/bladder tears the ligaments off the bladder/body wall",
           "Block pulled/handled BY the ligaments; median ligament severed by midline knife/saw",
           "No 'handle-by-support-surface' rule; pull-force & angle uncontrolled",
           "(confirm) handling standard missing + speed",
           "Handle by a support surface, not the ligaments; control pull-force; cut attachments first",
           "SH Martins - Evisceration lead", "", "Open", ""],
    "D12": ["Bladder cut open / large hole (urine spill)",
            "Knife tip punctures a distended, thin-walled bladder during belly opening",
            "Bladder full & sitting abdominally (in the knife's path); stab entry, not an 'unzip'",
            "Fasting (feed/water withdrawal) not enforced; belly-cut technique not standardized",
            "(confirm) lairage feed-water timing + belly-opening technique gap",
            "Fasting to empty the bladder; 'unzip' handle-in belly cut; sharper knives",
            "SH Martins - Evisc./Lairage lead", "", "Open", ""],
    "D13": ["Block too short / fails the length template",
            "Distal urethra/bladder-neck already transected high at the aitch-bone cut or split",
            "Aitch/split cut takes too much distal length, OR harvester boundary set too tight to bladder",
            "No cut-height / minimum-length spec vs a template at aitch/split + recovery",
            "(confirm) length spec/gauge missing across aitch, split, and recovery cut",
            "Define min block length & boundaries vs template/gauge; align aitch/split to preserve distal urethra",
            "SH Martins - Splitting + Harvest lead", "", "Open", ""],
}
seed_order = ["D6", "D1", "D5", "D8", "D4", "D12", "D13"]
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
for i in range(2):
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

# ============================================================================
# SHEET 8: YIELD & ALIGNMENT
# ============================================================================
ya = wb.create_sheet("Yield & Alignment"); ya.sheet_view.showGridLines = False
YAN = 7
title_block(ya, "YIELD & INSPECTOR–TECH ALIGNMENT",
            "How many pelvics are good across the board — and what it may say about harvest-tech training and tech<->inspector alignment.", YAN)
INSP_COL = get_column_letter(7)   # G = Inspector

def ya_countifs(crit, result=None):
    parts = [f"'Inspection Log'!{col}{data_first}:{col}{RNG},\"{val}\"" for col, val in crit]
    if result:
        parts.append(f"'Inspection Log'!{RESULT_COL}{data_first}:{RESULT_COL}{RNG},\"{result}\"")
    return "COUNTIFS(" + ",".join(parts) + ")"

def ya_sec(r, text):
    ya.merge_cells(start_row=r, start_column=1, end_row=r, end_column=YAN)
    c = ya.cell(r, 1, text); c.font = font(11, True, WHITE); c.fill = fill(NAVY)
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1); ya.row_dimensions[r].height = 20
    return r + 1

def ya_text(r, text, bold=False, color="222222", h=30, italic=False, fillc=None):
    ya.merge_cells(start_row=r, start_column=1, end_row=r, end_column=YAN)
    c = ya.cell(r, 1, text); c.font = font(10, bold, color, italic=italic); c.alignment = LEFT_TOP
    if fillc: c.fill = fill(fillc)
    ya.row_dimensions[r].height = h
    return r + 1

pass_all = ya_countifs([], "Pass"); fail_all = ya_countifs([], "Fail")

r = 4
# --- headline ---
r = ya_sec(r, "GOOD PELVICS — ACROSS THE BOARD  (First Pass Yield = good / inspected)")
ya.merge_cells(start_row=r, start_column=1, end_row=r + 2, end_column=2)
big = ya.cell(r, 1)
big.value = f"=IFERROR({pass_all}/({pass_all}+{fail_all}),0)"
big.number_format = "0.0%"; big.font = Font(name="Calibri", size=40, bold=True, color="C00000")
big.alignment = CENTER
for rr in range(r, r + 3):
    for cc in (1, 2): ya.cell(rr, cc).border = BORDER; ya.cell(rr, cc).fill = fill(LT_GREY)
ya.merge_cells(start_row=r, start_column=3, end_row=r, end_column=YAN)
ya.cell(r, 3, "of pelvic blocks that reach inspection pass IQC on the first look.").font = font(11, True, "222222")
ya.cell(r, 3).alignment = LEFT
ya.merge_cells(start_row=r + 1, start_column=3, end_row=r + 1, end_column=YAN)
ya.cell(r + 1, 3).value = f'="= "&{pass_all}&" good  /  "&({pass_all}+{fail_all})&" inspected  ->  ~9 of every 10 blocks are rejected"'
ya.cell(r + 1, 3).font = font(11, False, "444444"); ya.cell(r + 1, 3).alignment = LEFT
ya.merge_cells(start_row=r + 2, start_column=3, end_row=r + 2, end_column=YAN)
ya.cell(r + 2, 3, "A yield this low is first a SUPPLIER signal (84% of defects are evisceration-origin) — but it also frames the tech/inspector questions below.").font = font(10, True, "833C00")
ya.cell(r + 2, 3).alignment = LEFT_TOP
ya.row_dimensions[r].height = 28; ya.row_dimensions[r + 1].height = 18; ya.row_dimensions[r + 2].height = 30
r += 3
r = ya_text(r, "Caveat: the 8 passes on 2026-05-27 include 5 blocks recorded Pass pending ME/DE. If those are confirmed failures, the across-the-board good rate falls to ~5% (5/99).", italic=True, color=GREY, h=16)
r += 1

# --- by inspection sheet ---
r = ya_sec(r, "GOOD RATE BY INSPECTION SHEET  (kill date x inspector)")
hdrs = ["Kill Date", "Inspector", "Inspected", "Good (pass)", "Good %", "", ""]
for j, hh in enumerate(hdrs[:5], start=1): style_header(ya.cell(r, j, hh))
ya.row_dimensions[r].height = 22
r += 1
for b in BATCHES:
    crit = [(KILL_COL, b["kill_date"])]
    if b["inspector"]: crit.append((INSP_COL, b["inspector"]))
    insp_f = f"={ya_countifs(crit,'Pass')}+{ya_countifs(crit,'Fail')}"
    ya.cell(r, 1, b["kill_date"]).alignment = CENTER
    ya.cell(r, 2, b["inspector"] or "(unnamed)").alignment = CENTER
    ya.cell(r, 3).value = insp_f
    ya.cell(r, 4).value = f"={ya_countifs(crit,'Pass')}"
    ya.cell(r, 5).value = f"=IFERROR(D{r}/C{r},0)"; ya.cell(r, 5).number_format = "0.0%"
    for j in range(1, 6):
        cc = ya.cell(r, j); cc.border = BORDER; cc.font = font(10); cc.alignment = CENTER
    r += 1
# total
ya.cell(r, 1, "ALL").font = font(10, True, NAVY); ya.cell(r, 1).alignment = CENTER
ya.cell(r, 2, "").border = BORDER
ya.cell(r, 3).value = f"={pass_all}+{fail_all}"
ya.cell(r, 4).value = f"={pass_all}"
ya.cell(r, 5).value = f"=IFERROR(D{r}/C{r},0)"; ya.cell(r, 5).number_format = "0.0%"
for j in range(1, 6):
    cc = ya.cell(r, j); cc.border = BORDER; cc.fill = fill(LT_BLUE); cc.font = font(10, True); cc.alignment = CENTER
r += 2

# --- interpretation: training ---
r = ya_sec(r, "WHAT THIS COULD MEAN ABOUT HARVEST-TECH TRAINING")
r = ya_text(r, "The harvest techs are the first-pass filter: they recover blocks from the pit and keep (spec-out) or discard each one. A ~10% good rate can mean two very different things, and the current data cannot fully separate them:", h=30)
r = ya_text(r, "1)  MATERIAL (most likely).  The incoming tissue is overwhelmingly defective — 84% of defects are evisceration-origin — so even a perfectly-trained tech would keep mostly-bad blocks because there is little good material to choose from. Here the low yield is a SUPPLIER signal, not a tech signal.", h=42, fillc=LT_GREY)
r = ya_text(r, "2)  CALIBRATION GAP.  If the techs are keeping blocks that inspectors then reject, their internal 'good/bad' threshold is looser than the inspection spec — a training / standardization gap. The tell for this is a high tech KEEP rate paired with a low IQC pass rate (see alignment below).", h=42, fillc=LT_GREY)
r = ya_text(r, "Reading them together: because the defects are dominated by real, supplier-side damage, (1) is the stronger explanation today — but (2) cannot be ruled out until we log the techs' keep/discard decisions. A quick check: have a lead re-grade a sample of kept AND discarded blocks against the written spec and compare to both the tech and the inspector.", bold=True, color=NAVY, h=44)
r += 1

# --- alignment ---
r = ya_sec(r, "INSPECTOR <-> HARVEST-TECH ALIGNMENT  (agreement on the good/bad call)")
r = ya_text(r, "Alignment = do the harvest tech (keep/discard) and the inspector (pass/fail) make the SAME good/bad call on the same block? What we can see now: the inspected blocks are the ones the techs KEPT, and inspectors pass only ~10% of them — so on the KEEP decision the two groups agree ~10% of the time (9 of 10 blocks a tech judged good enough to keep, the inspector rejected). That is a strong misalignment signal, but it is confounded with material quality, and we cannot yet see the techs' DISCARD calls.", h=64)
r = ya_text(r, "To measure alignment properly, enter the harvest-tech first-pass numbers below (received from pit, discarded first-pass). Then the agreement metrics compute automatically. Also re-inspect a sample of discarded blocks to catch over-discarding (good blocks thrown away).", bold=True, color=NAVY, h=34)
r += 1
al_hdr = ["Kill Date", "Received from pit  (enter)", "Tech discarded 1st-pass  (enter)", "IQC inspected (=kept)", "IQC good", "Tech reject %", "Good-from-pit %"]
for j, hh in enumerate(al_hdr, start=1): style_header(ya.cell(r, j, hh))
ya.row_dimensions[r].height = 34
r += 1
al_first = r
for kd in sorted(kill_dates):
    crit = [(KILL_COL, kd)]
    ya.cell(r, 1, kd).alignment = CENTER
    ya.cell(r, 2).fill = fill("FFF2CC")            # input: received
    ya.cell(r, 3).fill = fill("FFF2CC")            # input: discarded
    ya.cell(r, 4).value = f"={ya_countifs(crit,'Pass')}+{ya_countifs(crit,'Fail')}"   # kept = inspected
    ya.cell(r, 5).value = f"={ya_countifs(crit,'Pass')}"
    ya.cell(r, 6).value = f'=IF(B{r}="","",IFERROR(C{r}/B{r},0))'; ya.cell(r, 6).number_format = "0.0%"
    ya.cell(r, 7).value = f'=IF(B{r}="","",IFERROR(E{r}/B{r},0))'; ya.cell(r, 7).number_format = "0.0%"
    for j in range(1, 8):
        cc = ya.cell(r, j); cc.border = BORDER; cc.font = font(10); cc.alignment = CENTER
    r += 1
ya.cell(r, 1, "Tech reject % = discarded / received.   Good-from-pit % = IQC good / received (the true end-to-end yield).   IQC good / IQC inspected = the agreement on kept blocks (headline above).").font = font(9, italic=True, color=GREY)
ya.merge_cells(start_row=r, start_column=1, end_row=r, end_column=YAN); ya.row_dimensions[r].height = 26

for col, w in {"A": 13, "B": 24, "C": 26, "D": 18, "E": 12, "F": 14, "G": 16}.items():
    ya.column_dimensions[col].width = w

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pelvic_Block_IQC_Pareto_RootCause.xlsx")
wb.save(out)
print("SAVED:", out)
print("Records:", len(records), "| Pass:", sum(1 for r in records if r["result"]=="Pass"), "| Fail:", sum(1 for r in records if r["result"]=="Fail"))
print("Combined defect counts:", {c: counts[c] for c in order})
print("Total defect occurrences:", total_def)
print("Station rollup:", {s: sum(counts[c] for c in station_codes[s]) for s in station_order})
for bs in sorted(batch_stats, key=lambda x: x["kill"]):
    print(f"  Batch {bs['kill']}: insp={bs['insp']} pass={bs['passed']} fail={bs['failed']} FPY={bs['fpy']*100:.1f}% top={bs['top']}({bs['topn']})")
