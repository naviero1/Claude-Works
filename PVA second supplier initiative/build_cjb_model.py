#!/usr/bin/env python3
"""Build PVA_CJB_vs_SNP_vs_Market.xlsx — cost comparison model."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment

# ---- styles ----
ARIAL = "Arial"
def f(bold=False, size=10, color="000000", italic=False):
    return Font(name=ARIAL, bold=bold, size=size, color=color, italic=italic)
BLUE = "0000FF"      # hardcoded input
GREEN = "008000"     # cross-sheet link
BLACK = "000000"     # formula
RED = "FF0000"
YEL = PatternFill("solid", fgColor="FFFF00")     # key input to edit
HDR = PatternFill("solid", fgColor="1F3864")     # dark header
SUB = PatternFill("solid", fgColor="D6DCE5")     # section band
GREY = PatternFill("solid", fgColor="F2F2F2")
GOOD = PatternFill("solid", fgColor="C6EFCE")
BAD  = PatternFill("solid", fgColor="FFC7CE")
AMB  = PatternFill("solid", fgColor="FFEB9C")
thin = Side(style="thin", color="BFBFBF")
BORD = Border(left=thin, right=thin, top=thin, bottom=thin)
CUR = '$#,##0.00'
CUR0 = '$#,##0'
PCT = '0.0%'
LB = '#,##0.0'

wb = openpyxl.Workbook()

def band(ws, row, text, span=4):
    c = ws.cell(row=row, column=2, value=text)
    c.font = f(bold=True, size=10, color="FFFFFF")
    for col in range(2, 2+span):
        ws.cell(row=row, column=col).fill = HDR
    return c

# =====================================================================
# SHEET 1 — ASSUMPTIONS
# =====================================================================
ws = wb.active
ws.title = "Assumptions"
ws.sheet_view.showGridLines = False
ws.column_dimensions['A'].width = 2
ws.column_dimensions['B'].width = 44
ws.column_dimensions['C'].width = 15
ws.column_dimensions['D'].width = 62

ws['B2'] = "PVA Second Source — CJB vs SNP vs Market"
ws['B2'].font = f(bold=True, size=15, color="1F3864")
ws['B3'] = "Cost model. Edit only the YELLOW cells; black/green cells are calculated. Built 2026-07-29 from CJB 'RE: CJB PVA mix test' + confirmed demand."
ws['B3'].font = f(italic=True, size=9, color="595959")

def inp(ws, row, label, value, note, fmt=None, key=True):
    ws.cell(row=row, column=2, value=label).font = f()
    c = ws.cell(row=row, column=3, value=value)
    c.font = f(bold=True, color=BLUE); c.alignment = Alignment(horizontal="center")
    if key: c.fill = YEL
    c.border = BORD
    if fmt: c.number_format = fmt
    n = ws.cell(row=row, column=4, value=note); n.font = f(size=9, color="595959")
    return c

def calc(ws, row, label, formula, note, fmt=None, link=False):
    ws.cell(row=row, column=2, value=label).font = f()
    c = ws.cell(row=row, column=3, value=formula)
    c.font = f(bold=True, color=GREEN if link else BLACK); c.alignment = Alignment(horizontal="center")
    c.fill = GREY; c.border = BORD
    if fmt: c.number_format = fmt
    n = ws.cell(row=row, column=4, value=note); n.font = f(size=9, color="595959")
    return c

band(ws, 5, "1) ACCOUNT FUNDAMENTALS  (established / confirmed)")
inp(ws, 6, "Drum net weight (lb)", 450, "From SNP quote '1/450 lb. drum'. ~1.0 density aqueous solution.")
inp(ws, 7, "Weeks per year", 52, "")
inp(ws, 8, "TOTAL demand (lb finished PVA / week)", 1300, "Confirmed by Oscar 2026-06-26. This is how SNP bills (per lb).")
inp(ws, 9, "SNP price ($/lb, delivered all-in)", 0.75, "SNP Estimate 012726-1, item 5TT-11A. Includes materials + processing + freight.", CUR)
inp(ws, 10, "Second-source split % (of total volume)", 0.25, "Decided fixed split ~20-25% to the 2nd source. Adjust to test.", PCT)
calc(ws, 11, "SNP price per drum ($)", "=C6*C9", "= $/lb x drum lb.", CUR)
calc(ws, 12, "Total drums per year", "=C8*C7/C6", "= (lb/wk x wks) / drum lb.", LB)
calc(ws, 13, "2nd-source drums per year", "=C12*C10", "The slice we hand to a 2nd source.", LB)
calc(ws, 14, "SNP drums per year (retained)", "=C12*(1-C10)", "", LB)
calc(ws, 15, "CURRENT all-SNP annual spend ($)", "=C12*C11", "Baseline: 100% to SNP. The number to beat.", CUR0)

band(ws, 17, "2) PRODUCT / MATERIALS  (for toll costing — we supply the raw materials)")
inp(ws, 18, "Total solids (% of finished weight)", 0.11, "Product spec ~10-12% solids in water. Midpoint used.", PCT)
inp(ws, 19, "PVA resin loading (% of finished weight)", 0.10, "Resin is ~90% of solids (rest = NaCl + pigment). ESTIMATE — refine from formula.", PCT)
calc(ws, 20, "PVA resin lb per drum", "=C6*C19", "Toll basis under Interpretation A (per lb of resin).", LB)
inp(ws, 21, "Resin cost ($/lb, specialty, small-qty)", 3.00, "Selvol S-1551F-D via distributor, drum qty. Commodity PVOH index ~$1.3/lb; specialty/small-qty ~$3.", CUR)
inp(ws, 22, "Other materials $/drum (NaCl+Proxel+pigment+drum)", 65, "ESTIMATE. Refine with actual BOM.", CUR0)
calc(ws, 23, "Raw materials $/drum (we supply)", "=C20*C21+C22", "= resin lb x resin $/lb + other. We consign these to the toller.", CUR0)
inp(ws, 24, "Finished-goods freight $/drum (GA -> us)", 75, "ESTIMATE, single-drum LTL from Valdosta GA. Confirm with CJB.", CUR0)
calc(ws, 25, "Our materials + freight $/drum", "=C23+C24", "Everything the toll price does NOT cover.", CUR0)

band(ws, 27, "3) CJB PROPOSAL TERMS  (from 'RE: CJB PVA mix test')")
inp(ws, 28, "Qualification fee ($)", 4900, "Reduced from $6,300. Applies REGARDLESS of trial success.", CUR0)
inp(ws, 29, "Credit per production batch ($)", 700, "Only if trial succeeds AND a 1-year production agreement is signed.", CUR0)
inp(ws, 30, "# of production batches credited", 7, "$700 x 7 = full $4,900 credited back over the first seven batches.")
calc(ws, 31, "Total qualification credit ($)", "=C29*C30", "", CUR0)
inp(ws, 32, "Toll processing $/lb — LOW", 8.00, "CJB estimate, EXCLUDING raw materials. *** PER POUND OF WHAT? confirm basis. ***", CUR)
inp(ws, 33, "Toll processing $/lb — HIGH", 8.50, "Final pricing to be confirmed after lab trial validates handling.", CUR)

band(ws, 35, "4) MARKET / 3rd-SUPPLIER BENCHMARK  ($/lb finished, delivered all-in)")
inp(ws, 36, "Market LOW ($/lb finished)", 1.00, "APV-type competitive 2nd-source anchor (~+33% vs SNP).", CUR)
inp(ws, 37, "Market LIKELY ($/lb finished)", 1.12, "Small-batch toll premium ~+50% over incumbent (model's 'Likely').", CUR)
inp(ws, 38, "Market HIGH ($/lb finished)", 1.50, "Worst-case competitive quote (~+100%).", CUR)

ws['B40'] = "LEGEND"
ws['B40'].font = f(bold=True, size=9)
ws['B41'] = "Yellow = edit these.   Blue = input.   Green = links another tab.   Grey = calculated."
ws['B41'].font = f(size=9, color="595959")
ws['B42'] = "Market range is built independently of CJB: SNP floor ($0.75) + APV-type 2nd-source target + documented small-batch toll premium. See 'Benchmark' tab."
ws['B42'].font = f(size=9, italic=True, color="595959")

# comments on the pivotal cells
ws['C32'].comment = Comment("PIVOTAL AMBIGUITY: is $8.00-8.50 per lb of RESIN they process, or per lb of FINISHED solution?\n"
                            "Resin basis (45 lb/drum) -> ~$371 toll/drum: viable.\n"
                            "Finished basis (450 lb/drum) -> ~$3,713 toll/drum: 11x SNP, non-starter.\n"
                            "MUST confirm with CJB before deciding.", "model")
ws['C19'].comment = Comment("Swings the toll cost under Interpretation A. If the real formula is 10-12% resin, edit here.", "model")

# =====================================================================
# SHEET 2 — CJB PROPOSAL (both interpretations)
# =====================================================================
cp = wb.create_sheet("CJB Proposal")
cp.sheet_view.showGridLines = False
cp.column_dimensions['A'].width = 2
cp.column_dimensions['B'].width = 46
cp.column_dimensions['C'].width = 22
cp.column_dimensions['D'].width = 22
cp.column_dimensions['E'].width = 40

cp['B2'] = "CJB Proposal — Costed Out (two unit interpretations)"
cp['B2'].font = f(bold=True, size=14, color="1F3864")
cp['B3'] = "CJB quoted toll processing at $8.00-8.50 'per pound' excluding raw materials. The BASIS is ambiguous and swings the answer ~9x."
cp['B3'].font = f(italic=True, size=9, color="C00000")

# header row
r = 5
cp.cell(row=r, column=2, value="Line item (per drum unless noted)").font = f(bold=True, color="FFFFFF")
cp.cell(row=r, column=3, value="Interp A: $/lb of RESIN").font = f(bold=True, color="FFFFFF")
cp.cell(row=r, column=4, value="Interp B: $/lb of FINISHED").font = f(bold=True, color="FFFFFF")
cp.cell(row=r, column=5, value="Comment").font = f(bold=True, color="FFFFFF")
for col in range(2,6): cp.cell(row=r, column=col).fill = HDR
cp.cell(row=r,column=3).fill = PatternFill("solid", fgColor="2E7D32")
cp.cell(row=r,column=4).fill = PatternFill("solid", fgColor="C0392B")

def cprow(r, label, fa, fb, note, fmt=CUR, bold=False, fillrow=None):
    cp.cell(row=r, column=2, value=label).font = f(bold=bold)
    a = cp.cell(row=r, column=3, value=fa); a.font = f(bold=bold, color=BLACK); a.number_format=fmt; a.alignment=Alignment(horizontal="center"); a.border=BORD
    b = cp.cell(row=r, column=4, value=fb); b.font = f(bold=bold, color=BLACK); b.number_format=fmt; b.alignment=Alignment(horizontal="center"); b.border=BORD
    cp.cell(row=r, column=5, value=note).font = f(size=9, color="595959")
    if fillrow:
        for col in (3,4): cp.cell(row=r, column=col).fill = fillrow
    return r

cprow(6, "Toll basis — lb per drum", "=Assumptions!C20", "=Assumptions!C6",
      "Resin lb/drum vs full finished lb/drum.", LB)
cprow(7, "Toll $/drum @ $8.00/lb", "=C6*Assumptions!C32", "=D6*Assumptions!C32", "")
cprow(8, "Toll $/drum @ $8.50/lb", "=C6*Assumptions!C33", "=D6*Assumptions!C33", "")
cprow(9, "Toll $/drum (midpoint)", "=(C7+C8)/2", "=(D7+D8)/2", "CJB's service fee only.", CUR, bold=True)
cprow(10, "+ Raw materials $/drum (we supply)", "=Assumptions!C23", "=Assumptions!C23", "Not in the toll fee.")
cprow(11, "+ Finished freight $/drum", "=Assumptions!C24", "=Assumptions!C24", "GA -> us.")
cprow(12, "= LANDED cost $/drum (midpoint)", "=C9+C10+C11", "=D9+D10+D11", "What a drum actually costs us.", CUR, bold=True, fillrow=AMB)
cprow(13, "Landed $/lb finished", "=C12/Assumptions!C6", "=D12/Assumptions!C6", "Common basis vs SNP $0.75 & market.", CUR, bold=True)
cprow(14, "vs SNP $/drum (Delta)", "=C12-Assumptions!C11", "=D12-Assumptions!C11", "", CUR)
cprow(15, "vs SNP (%)", "=C14/Assumptions!C11", "=D14/Assumptions!C11", "", PCT)
cprow(16, "2nd-source drums / year", "=Assumptions!C13", "=Assumptions!C13", "", LB)
cprow(17, "Annual running cost — 2nd-source slice", "=C12*C16", "=D12*D16", "Excludes one-time qual fee.", CUR0, bold=True)

# qual block
band(cp, 19, "QUALIFICATION ECONOMICS  ($4,900 batch — win or lose)", span=4)
cp.cell(row=20, column=2, value="Qualification fee — paid upfront (win or lose)").font=f()
cp.cell(row=20, column=3, value="=Assumptions!C28").number_format=CUR0; cp.cell(row=20,column=3).font=f(color=GREEN); cp.cell(row=20,column=3).alignment=Alignment(horizontal="center")
cp.cell(row=21, column=2, value="Credit if trial succeeds + 1-yr deal ($700 x 7)").font=f()
cp.cell(row=21, column=3, value="=-Assumptions!C31").number_format=CUR0; cp.cell(row=21,column=3).font=f(color=BLACK); cp.cell(row=21,column=3).alignment=Alignment(horizontal="center")
cp.cell(row=22, column=2, value="NET qualification cost — if deal proceeds").font=f(bold=True)
c=cp.cell(row=22, column=3, value="=C20+C21"); c.number_format=CUR0; c.font=f(bold=True); c.fill=GOOD; c.alignment=Alignment(horizontal="center")
cp.cell(row=22, column=5, value="Fully credited back over the first ~year of production.").font=f(size=9,color="595959")
cp.cell(row=23, column=2, value="NET qualification cost — if trial fails / no deal").font=f(bold=True)
c=cp.cell(row=23, column=3, value="=C20"); c.number_format=CUR0; c.font=f(bold=True); c.fill=BAD; c.alignment=Alignment(horizontal="center")
cp.cell(row=23, column=5, value="Sunk. This is the money at risk if the trial doesn't validate.").font=f(size=9,color="595959")

cp['B25'] = "READ THIS: Interp B (per lb of finished) makes CJB ~11x SNP — almost certainly NOT what they mean, but"
cp['B25'].font = f(size=9, italic=True, color="C00000")
cp['B26'] = "it must be ruled out in writing. The whole comparison hinges on confirming the toll basis."
cp['B26'].font = f(size=9, italic=True, color="C00000")

# =====================================================================
# SHEET 3 — COMPARISON (headline)
# =====================================================================
cm = wb.create_sheet("Comparison")
cm.sheet_view.showGridLines = False
cm.column_dimensions['A'].width = 2
cm.column_dimensions['B'].width = 42
for col in "CDEFGH": cm.column_dimensions[col].width = 14

cm['B2'] = "Head-to-Head — SNP vs Market vs CJB"
cm['B2'].font = f(bold=True, size=14, color="1F3864")
cm['B3'] = "All on a common DELIVERED basis. SNP & Market are all-in delivered; CJB = toll + our-supplied materials + freight."
cm['B3'].font = f(italic=True, size=9, color="595959")

heads = ["", "SNP (incumbent)", "Market LOW", "Market LIKELY", "Market HIGH", "CJB (Interp A)", "CJB (Interp B)"]
r=5
for i,h in enumerate(heads):
    c = cm.cell(row=r, column=2+i, value=h); c.font=f(bold=True, color="FFFFFF"); c.alignment=Alignment(horizontal="center", wrap_text=True); c.fill=HDR
cm.cell(row=r,column=2,value="Metric").fill=HDR
cm.cell(row=r,column=3).fill=PatternFill("solid",fgColor="2E7D32")
cm.cell(row=r,column=7).fill=PatternFill("solid",fgColor="7D6608")
cm.cell(row=r,column=8).fill=PatternFill("solid",fgColor="C0392B")

# columns C..H map to SNP, MktLow, MktLikely, MktHigh, CJB-A, CJB-B
# $/lb finished
def setrow(r, label, vals, fmt, bold=False):
    cm.cell(row=r, column=2, value=label).font=f(bold=bold)
    for i,v in enumerate(vals):
        c = cm.cell(row=r, column=3+i, value=v); c.number_format=fmt; c.alignment=Alignment(horizontal="center")
        c.font=f(bold=bold); c.border=BORD
    return r

setrow(6, "$/lb finished (delivered/landed)",
    ["=Assumptions!C9","=Assumptions!C36","=Assumptions!C37","=Assumptions!C38","='CJB Proposal'!C13","='CJB Proposal'!D13"],
    CUR, bold=True)
setrow(7, "$/drum (delivered/landed)",
    ["=Assumptions!C11","=D6*Assumptions!C6","=E6*Assumptions!C6","=F6*Assumptions!C6","='CJB Proposal'!C12","='CJB Proposal'!D12"],
    CUR0, bold=True)
setrow(8, "Delta $/drum vs SNP",
    ["=C7-$C$7","=D7-$C$7","=E7-$C$7","=F7-$C$7","=G7-$C$7","=H7-$C$7"], CUR0)
setrow(9, "Delta % vs SNP",
    ["=C8/$C$7","=D8/$C$7","=E8/$C$7","=F8/$C$7","=G8/$C$7","=H8/$C$7"], PCT)
setrow(10, "Annual cost — 2nd-source slice (drums)",
    ["=C7*Assumptions!$C$13","=D7*Assumptions!$C$13","=E7*Assumptions!$C$13","=F7*Assumptions!$C$13","=G7*Assumptions!$C$13","=H7*Assumptions!$C$13"],
    CUR0, bold=True)
setrow(11, "Cost of redundancy (vs same drums at SNP)",
    ["=C10-Assumptions!$C$13*Assumptions!$C$11","=D10-Assumptions!$C$13*Assumptions!$C$11","=E10-Assumptions!$C$13*Assumptions!$C$11","=F10-Assumptions!$C$13*Assumptions!$C$11","=G10-Assumptions!$C$13*Assumptions!$C$11","=H10-Assumptions!$C$13*Assumptions!$C$11"],
    CUR0, bold=True)

# highlight CJB-A and market-likely columns
for rr in range(6,12):
    cm.cell(row=rr, column=5).fill = GREY      # market likely
    cm.cell(row=rr, column=7).fill = AMB       # CJB A
    cm.cell(row=rr, column=8).fill = BAD       # CJB B

cm['B13']="Takeaway"; cm['B13'].font=f(bold=True, color="1F3864")
cm['B14']="If CJB's $8/lb is per lb of RESIN (the sensible reading), CJB lands at the TOP of the market band —"
cm['B15']="roughly double the redundancy premium of a competitively-quoted toll blender (APV / Piedmont / Columbus)."
cm['B16']="If it is per lb of FINISHED solution, CJB is a non-starter. Get 2-3 competing toll quotes before committing."
for rr in (14,15,16): cm.cell(row=rr,column=2).font=f(size=9, color="595959")

# =====================================================================
# SHEET 4 — REDUNDANCY (total account)
# =====================================================================
rd = wb.create_sheet("Redundancy")
rd.sheet_view.showGridLines = False
rd.column_dimensions['A'].width = 2
rd.column_dimensions['B'].width = 34
for col in "CDEFGHIJ": rd.column_dimensions[col].width = 13

rd['B2'] = "Total-Account Cost of Redundancy (75% SNP + 25% 2nd source)"
rd['B2'].font = f(bold=True, size=14, color="1F3864")
rd['B3'] = "The real decision: what does dual-sourcing add to the whole account vs staying 100% SNP?"
rd['B3'].font = f(italic=True, size=9, color="595959")

cols = ["Scenario","SNP drums/yr","2nd drums/yr","SNP annual $","2nd-src annual $","Qual (yr-1 net)","TOTAL yr-1 $","Delta vs baseline $","Delta %","Steady-state yr2+ $"]
r=5
for i,h in enumerate(cols):
    c=rd.cell(row=r, column=2+i, value=h); c.font=f(bold=True,color="FFFFFF"); c.fill=HDR; c.alignment=Alignment(horizontal="center", wrap_text=True); c.border=BORD

# row 6: baseline all-SNP
def rrow(r, name, snpd, secd, snpann, secann, qual, fill=None):
    rd.cell(row=r, column=2, value=name).font=f(bold=(fill is None))
    vals = {3:snpd,4:secd,5:snpann,6:secann,7:qual}
    for col,v in vals.items():
        c=rd.cell(row=r, column=col, value=v); c.alignment=Alignment(horizontal="center"); c.border=BORD
        c.number_format = LB if col in (3,4) else CUR0
        c.font=f()
    # total yr1 = snpann+secann+qual
    t=rd.cell(row=r, column=8, value=f"=E{r}+F{r}+G{r}"); t.number_format=CUR0; t.font=f(bold=True); t.border=BORD; t.alignment=Alignment(horizontal="center")
    d=rd.cell(row=r, column=9, value=f"=H{r}-$H$6"); d.number_format=CUR0; d.font=f(); d.border=BORD; d.alignment=Alignment(horizontal="center")
    p=rd.cell(row=r, column=10, value=f"=IF($H$6=0,0,I{r}/$H$6)"); p.number_format=PCT; p.font=f(); p.border=BORD; p.alignment=Alignment(horizontal="center")
    ss=rd.cell(row=r, column=11, value=f"=E{r}+F{r}"); ss.number_format=CUR0; ss.font=f(); ss.border=BORD; ss.alignment=Alignment(horizontal="center")
    if fill:
        for col in range(2,12): rd.cell(row=r, column=col).fill = fill

rrow(6, "Baseline — 100% SNP", "=Assumptions!C12", 0, "=Assumptions!C12*Assumptions!C11", 0, 0)
rrow(7, "+ 25% Market LIKELY", "=Assumptions!C14", "=Assumptions!C13", "=C7*Assumptions!C11", "=D7*'Comparison'!E7", 0, GREY)
rrow(8, "+ 25% CJB (Interp A: resin)", "=Assumptions!C14", "=Assumptions!C13", "=C8*Assumptions!C11", "=D8*'Comparison'!G7", 0, AMB)
rrow(9, "+ 25% CJB (Interp B: finished)", "=Assumptions!C14", "=Assumptions!C13", "=C9*Assumptions!C11", "=D9*'Comparison'!H7", 0, BAD)

rd['B11']="Notes"; rd['B11'].font=f(bold=True)
notes=[
 "Qual (yr-1 net) = $0 for CJB: the $4,900 is credited back over the first 7 batches IF the trial succeeds and a 1-yr deal is signed.",
 "If the trial FAILS or no deal is signed, add $4,900 sunk to CJB year-1 (see 'CJB Proposal' tab).",
 "Market scenario assumes a competitive 2nd-source quote (~$1.12/lb delivered); no market qual fee is modeled (unknown — most toll qual runs are $2-6k).",
 "Steady-state (yr2+) drops all one-time fees: pure running cost of the split.",
 "Cost of redundancy = the insurance premium for not being single-sourced on SNP.",
]
for i,n in enumerate(notes):
    rd.cell(row=12+i, column=2, value="- "+n).font=f(size=9, color="595959")

# =====================================================================
# SHEET 5 — BENCHMARK & SOURCES
# =====================================================================
bm = wb.create_sheet("Benchmark")
bm.sheet_view.showGridLines = False
bm.column_dimensions['A'].width = 2
bm.column_dimensions['B'].width = 40
bm.column_dimensions['C'].width = 20
bm.column_dimensions['D'].width = 58

bm['B2']="Market Benchmark — how the 3rd-supplier range was built"
bm['B2'].font=f(bold=True, size=14, color="1F3864")
bm['B3']="Built independently of CJB, so CJB is measured against the market — not treated as the standard."
bm['B3'].font=f(italic=True, size=9, color="595959")

band(bm,5,"Anchors", span=3)
rows=[
 ("Incumbent floor — SNP", "$0.75/lb finished", "A real competitive quote we already hold. $337.50/drum delivered."),
 ("APV-type 2nd-source target", "~$1.00/lb finished", "Coatings/pigment house, 5-gal floor; ~+33% over incumbent. The realistic competitive 2nd-source price."),
 ("Small-batch toll premium", "+50% to +100%", "Micro-volume (~1 drum/wk) tolling premium over incumbent -> $1.12-1.50/lb."),
 ("PVA resin (raw) — commodity index", "~$1.26-1.41/lb", "North America PVOH, Dec-2025/Mar-2026. Specialty super-hydrolyzed grade in drum qty runs higher (~$3/lb)."),
 ("Toll conversion rates", "quote-driven (not public)", "Toll blenders price per-lb / per-batch / flat fee; no public rate card. Must get quotes."),
]
r=6
for name,val,note in rows:
    bm.cell(row=r,column=2,value=name).font=f(bold=True)
    bm.cell(row=r,column=3,value=val).font=f(color=BLUE); bm.cell(row=r,column=3).alignment=Alignment(horizontal="center")
    bm.cell(row=r,column=4,value=note).font=f(size=9,color="595959")
    for col in (2,3,4): bm.cell(row=r,column=col).border=BORD
    r+=1

band(bm,13,"Candidate 2nd sources to get competing quotes from (from Supplier Roster)", span=3)
cands=[
 ("APV Engineered Coatings (Akron, OH)","INTERVIEWING","5-gal floor; pigment-dispersion specialty; ISO 9001. Best price-competitive candidate."),
 ("Piedmont Chemical (High Point, NC)","Active","Textile/PVA heritage = real PVA know-how; 5-gal pilot reactors."),
 ("Columbus Chemical / CCI (WI/AZ)","Active","Widest batch range (20 L-20,000 L); in-house lab; least shelf-life waste."),
 ("CORECHEM (Knoxville, TN)","Caution","250-gal min may overshoot 18-day shelf life; ask about partial batches."),
]
r=14
for name,st,note in cands:
    bm.cell(row=r,column=2,value=name).font=f(bold=True)
    bm.cell(row=r,column=3,value=st).font=f(); bm.cell(row=r,column=3).alignment=Alignment(horizontal="center")
    bm.cell(row=r,column=4,value=note).font=f(size=9,color="595959")
    for col in (2,3,4): bm.cell(row=r,column=col).border=BORD
    r+=1

band(bm,20,"Sources", span=3)
srcs=[
 "PVOH price index (North America ~$3.10/kg Dec-2025; ~$2,778/MT Mar-2026): chemanalyst.com / imarcgroup.com PVA pricing reports.",
 "Toll blending pricing structure (per-lb / per-batch / flat fee; quote-driven): hydrite.com, royalchemical.com, jayneproducts.com.",
 "SNP price: SNP Estimate 012726-1, item 5TT-11A ($0.75/lb).",
 "CJB terms: email thread 'RE: CJB PVA mix test' (qual $4,900; $700 x 7 credit; toll $8.00-8.50/lb ex-materials).",
 "Demand & drum spec: confirmed by Oscar 2026-06-26 (1,300 lb/wk; 450 lb/drum).",
]
r=21
for s in srcs:
    bm.cell(row=r,column=2,value="- "+s).font=f(size=9,color="404040")
    r+=1

# order & save
wb.move_sheet("Benchmark", offset=0)
out = "/home/user/Claude-Works/PVA second supplier initiative/PVA_CJB_vs_SNP_vs_Market.xlsx"
wb.save(out)
print("saved", out)
