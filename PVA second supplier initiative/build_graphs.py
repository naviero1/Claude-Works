#!/usr/bin/env python3
"""PVA_Cost_Scenarios.xlsx — SNP vs CJB vs Market, with charts.
Values are computed in Python and written as numbers so charts render even
without a working recalc engine. Editable inputs + sources documented on tabs.
MARKET rates are filled from the deep-research pass (see MARKET_* below)."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, LineChart, Reference, Series
from openpyxl.chart.label import DataLabelList

# ---------- REAL / FIXED INPUTS ----------
DRUM_LB      = 450          # confirmed
SNP_LB       = 0.75         # real quote, delivered all-in
CJB_TOLL_LO  = 8.00         # real quote, excl materials
CJB_TOLL_HI  = 8.50
CJB_TOLL_MID = (CJB_TOLL_LO+CJB_TOLL_HI)/2
QUAL         = 4900
CREDIT       = 700
CREDIT_N     = 7
DEMAND_LB_WK = 1300
WEEKS        = 52

# materials (sourced floor) + freight (input)
RESIN_LB     = 1.52         # PVA resin $/lb — ChemAnalyst USA Jun-2026 $3,340/MT
SOLIDS       = 0.11         # product spec 10-12%
MATERIALS    = round(RESIN_LB*SOLIDS*DRUM_LB)   # ~ $75/drum PVA floor
FREIGHT      = 0            # unquantified; add when CJB confirms

# ---------- MARKET (from deep research; LOW/BASE/HIGH $/lb finished, delivered) ----------
# >>> FILLED FROM RESEARCH <<<  triangulated: resin floor + cited labor bottom-up + retail ceiling
MARKET_LB_LO   = 0.85
MARKET_LB_BASE = 1.40
MARKET_LB_HI   = 2.55
MARKET_SOURCE  = "Triangulated: resin floor (ChemAnalyst) + $40/hr loaded labor bottom-up + retail ceiling ~$2.03/lb (US Composites). Base ~$1.40/lb."

# ---------- DERIVED ----------
SNP_DRUM   = DRUM_LB*SNP_LB
CJB_TOLL_DRUM = DRUM_LB*CJB_TOLL_MID
CJB_LANDED = CJB_TOLL_DRUM + MATERIALS + FREIGHT
DRUMS_YR   = DEMAND_LB_WK*WEEKS/DRUM_LB

def scenario(split, second_price_drum, credit_total=0):
    sec = DRUMS_YR*split
    snp = DRUMS_YR*(1-split)
    return snp*SNP_DRUM + sec*second_price_drum - credit_total

def build():
    assert MARKET_LB_BASE is not None, "Fill MARKET_* from research first"
    MKT_DRUM_LO = MARKET_LB_LO*DRUM_LB
    MKT_DRUM_BASE = MARKET_LB_BASE*DRUM_LB
    MKT_DRUM_HI = MARKET_LB_HI*DRUM_LB

    ARIAL="Arial"
    def f(bold=False,size=10,color="000000",italic=False):
        return Font(name=ARIAL,bold=bold,size=size,color=color,italic=italic)
    YEL=PatternFill("solid",fgColor="FFFF00"); HDR=PatternFill("solid",fgColor="1F3864")
    SUB=PatternFill("solid",fgColor="D6DCE5"); GREY=PatternFill("solid",fgColor="F2F2F2")
    BAD=PatternFill("solid",fgColor="FFC7CE"); GOOD=PatternFill("solid",fgColor="C6EFCE")
    AMB=PatternFill("solid",fgColor="FFEB9C")
    thin=Side(style="thin",color="BFBFBF"); BORD=Border(left=thin,right=thin,top=thin,bottom=thin)
    CUR0='$#,##0'; CUR='$#,##0.00'

    wb=openpyxl.Workbook()

    # ---- TAB 1: Inputs ----
    ws=wb.active; ws.title="Inputs & Sources"
    ws.sheet_view.showGridLines=False
    for k,v in {'A':2,'B':42,'C':14,'D':54}.items(): ws.column_dimensions[k].width=v
    ws['B2']="PVA Cost Scenarios — Inputs & Sources"; ws['B2'].font=f(bold=True,size=14,color="1F3864")
    ws['B3']="Real quotes + sourced market estimate. Values feed the Per-Order and Annual tabs (numbers are snapshotted so charts render)."
    ws['B3'].font=f(italic=True,size=9,color="595959")
    rows=[
     ("REAL",None,None,None),
     ("Drum net weight (lb)",DRUM_LB,None,"Confirmed. SNP '1/450 lb drum'."),
     ("SNP $/lb delivered all-in",SNP_LB,CUR,"Real quote — SNP Est 012726-1."),
     ("CJB toll $/lb (midpoint of 8.00-8.50)",CJB_TOLL_MID,CUR,"Real quote, excl materials — CJB 'RE: mix test'."),
     ("CJB qualification fee",QUAL,CUR0,"Applies win/lose."),
     ("CJB credit per batch x first 7",CREDIT,CUR0,"Only if trial succeeds + 1-yr deal."),
     ("Demand (lb/wk)",DEMAND_LB_WK,None,"Confirmed 2026-06-26."),
     ("MATERIALS/FREIGHT (we supply)",None,None,None),
     ("PVA resin commodity $/lb",RESIN_LB,CUR,"ChemAnalyst/IMARC, N.America ~$1.26-1.41/lb."),
     ("Solids %",SOLIDS,None,"Spec 10-12%."),
     ("Materials $/drum (PVA floor)",MATERIALS,CUR0,"= resin x solids x 450. Excl minor NaCl/pigment."),
     ("Freight $/drum",FREIGHT,CUR0,"Unquantified — add when CJB confirms."),
     ("MARKET (deep research)",None,None,None),
     ("Market $/lb — LOW",MARKET_LB_LO,CUR,MARKET_SOURCE),
     ("Market $/lb — BASE",MARKET_LB_BASE,CUR,MARKET_SOURCE),
     ("Market $/lb — HIGH",MARKET_LB_HI,CUR,MARKET_SOURCE),
    ]
    r=5
    for label,val,fmt,note in rows:
        if val is None and fmt is None and note is None:
            c=ws.cell(row=r,column=2,value=label); c.font=f(bold=True,color="FFFFFF")
            for col in range(2,5): ws.cell(row=r,column=col).fill=HDR
        else:
            ws.cell(row=r,column=2,value=label).font=f()
            c=ws.cell(row=r,column=3,value=val); c.font=f(bold=True,color="0000FF"); c.alignment=Alignment(horizontal="center"); c.fill=YEL; c.border=BORD
            if fmt: c.number_format=fmt
            ws.cell(row=r,column=4,value=note).font=f(size=9,color="595959")
        r+=1

    # ---- TAB 2: Per-Order (credit) ----
    po=wb.create_sheet("Per-Order (credit)")
    po.sheet_view.showGridLines=False
    for k,v in {'A':2,'B':30,'C':16,'D':16,'E':16}.items(): po.column_dimensions[k].width=v
    po['B2']="CJB — Cost per Order, and what the $700 credit does"; po['B2'].font=f(bold=True,size=13,color="1F3864")
    po['B3']=(f"CJB landed per drum ≈ ${CJB_LANDED:,.0f} (toll ${CJB_TOLL_DRUM:,.0f} + materials ${MATERIALS} + freight ${FREIGHT}). "
              f"Credit = ${CREDIT} off each of the first {CREDIT_N} orders. SNP, for scale, is ${SNP_DRUM:,.0f}/order.")
    po['B3'].font=f(italic=True,size=9,color="595959")
    hdr=["Order #","CJB WITHOUT credit","CJB WITH credit","Cumulative credit"]
    r=5
    for i,h in enumerate(hdr):
        c=po.cell(row=r,column=2+i,value=h); c.font=f(bold=True,color="FFFFFF"); c.fill=HDR; c.alignment=Alignment(horizontal="center",wrap_text=True); c.border=BORD
    data_start=6
    cum=0
    for i in range(1,11):
        rr=data_start+i-1
        credited = CJB_LANDED - (CREDIT if i<=CREDIT_N else 0)
        if i<=CREDIT_N: cum+=CREDIT
        po.cell(row=rr,column=2,value=i).alignment=Alignment(horizontal="center")
        po.cell(row=rr,column=3,value=round(CJB_LANDED)).number_format=CUR0
        po.cell(row=rr,column=4,value=round(credited)).number_format=CUR0
        po.cell(row=rr,column=5,value=cum).number_format=CUR0
        for col in range(2,6): po.cell(row=rr,column=col).font=f(); po.cell(row=rr,column=col).alignment=Alignment(horizontal="center"); po.cell(row=rr,column=col).border=BORD
    last=data_start+9
    # bar chart: with vs without credit per order
    ch=BarChart(); ch.type="col"; ch.grouping="clustered"; ch.title="CJB cost per order — credit applies to first 7 only"
    ch.y_axis.title="$ per order (drum)"; ch.x_axis.title="Order #"; ch.height=9; ch.width=20
    dref=Reference(po,min_col=3,max_col=4,min_row=5,max_row=last)
    cats=Reference(po,min_col=2,min_row=data_start,max_row=last)
    ch.add_data(dref,titles_from_data=True); ch.set_categories(cats)
    po.add_chart(ch,"G5")
    po.cell(row=18,column=2,value=f"The credit returns the full ${QUAL:,} qualification fee over the first {CREDIT_N} orders, then stops.").font=f(size=9,italic=True,color="404040")
    po.cell(row=19,column=2,value="After order 7, every CJB order is at full price. The credit refunds the qual; it is not an ongoing discount.").font=f(size=9,italic=True,color="404040")

    # ---- TAB 3: Annual scenarios ----
    an=wb.create_sheet("Annual Scenarios")
    an.sheet_view.showGridLines=False
    for k,v in {'A':2,'B':34,'C':16}.items(): an.column_dimensions[k].width=v
    an['B2']="Total Annual Account Cost — by supplier, split, and year"; an['B2'].font=f(bold=True,size=13,color="1F3864")
    an['B3']=(f"Whole-account cost (2nd source + retained SNP). Total demand ≈ {DRUMS_YR:.0f} drums/yr. "
              "35% split ≈ 1 drum/week. CJB Year-1 reflects the one-time $4,900 credit; Year-2+ does not.")
    an['B3'].font=f(italic=True,size=9,color="595959")

    baseline = DRUMS_YR*SNP_DRUM
    scen=[
     ("All-SNP baseline", baseline),
     ("Market @25%", scenario(0.25,MKT_DRUM_BASE)),
     ("Market @35%", scenario(0.35,MKT_DRUM_BASE)),
     ("CJB @25% — Yr 1 (credit)", scenario(0.25,CJB_LANDED,QUAL)),
     ("CJB @25% — Yr 2+", scenario(0.25,CJB_LANDED)),
     ("CJB @35% — Yr 1 (credit)", scenario(0.35,CJB_LANDED,QUAL)),
     ("CJB @35% — Yr 2+", scenario(0.35,CJB_LANDED)),
    ]
    r=5
    an.cell(row=r,column=2,value="Scenario").font=f(bold=True,color="FFFFFF"); an.cell(row=r,column=2).fill=HDR; an.cell(row=r,column=2).border=BORD
    an.cell(row=r,column=3,value="Annual $").font=f(bold=True,color="FFFFFF"); an.cell(row=r,column=3).fill=HDR; an.cell(row=r,column=3).border=BORD
    for i,(name,val) in enumerate(scen):
        rr=6+i
        an.cell(row=rr,column=2,value=name).font=f(); an.cell(row=rr,column=2).border=BORD
        c=an.cell(row=rr,column=3,value=round(val)); c.number_format=CUR0; c.alignment=Alignment(horizontal="center"); c.border=BORD
        if "baseline" in name: an.cell(row=rr,column=2).fill=GREY; c.fill=GREY
        elif "Market" in name: an.cell(row=rr,column=2).fill=GOOD; c.fill=GOOD
        else: an.cell(row=rr,column=2).fill=BAD; c.fill=BAD
    last=6+len(scen)-1
    ch=BarChart(); ch.type="bar"; ch.title="Total annual account cost — all options"
    ch.x_axis.title="$ / year"; ch.height=10; ch.width=22
    dref=Reference(an,min_col=3,min_row=5,max_row=last)
    cats=Reference(an,min_col=2,min_row=6,max_row=last)
    ch.add_data(dref,titles_from_data=True); ch.set_categories(cats); ch.legend=None
    an.add_chart(ch,"E5")

    # realistic-only chart (baseline + market), CJB excluded so scale is readable
    an.cell(row=16,column=2,value="Realistic options only (CJB excluded — it is ~10x and dwarfs the scale)").font=f(bold=True,size=10,color="1F3864")
    r=17
    real=[("All-SNP baseline",baseline),("Market @25%",scenario(0.25,MKT_DRUM_BASE)),("Market @35%",scenario(0.35,MKT_DRUM_BASE))]
    an.cell(row=r,column=2,value="Scenario").font=f(bold=True,color="FFFFFF"); an.cell(row=r,column=2).fill=HDR
    an.cell(row=r,column=3,value="Annual $").font=f(bold=True,color="FFFFFF"); an.cell(row=r,column=3).fill=HDR
    for i,(name,val) in enumerate(real):
        rr=18+i
        an.cell(row=rr,column=2,value=name).font=f(); an.cell(row=rr,column=3,value=round(val)).number_format=CUR0
        an.cell(row=rr,column=3).alignment=Alignment(horizontal="center")
    rlast=18+len(real)-1
    ch2=BarChart(); ch2.type="col"; ch2.title="Realistic options — SNP baseline vs Market (2nd source)"
    ch2.y_axis.title="$ / year"; ch2.height=9; ch2.width=18
    d2=Reference(an,min_col=3,min_row=17,max_row=rlast); c2=Reference(an,min_col=2,min_row=18,max_row=rlast)
    ch2.add_data(d2,titles_from_data=True); ch2.set_categories(c2); ch2.legend=None
    an.add_chart(ch2,"E24")

    # ---- TAB 4: Market Research (sourced) ----
    mr=wb.create_sheet("Market Research")
    mr.sheet_view.showGridLines=False
    for k,v in {'A':2,'B':40,'C':13,'D':13,'E':13,'F':40}.items(): mr.column_dimensions[k].width=v
    mr['B2']="Market Cost — deep research (all-in $/lb finished, delivered)"; mr['B2'].font=f(bold=True,size=13,color="1F3864")
    mr['B3']="Triangulated from cited sources. No public toll rate exists; the per-batch conversion fee is the key unknown and needs real quotes."
    mr['B3'].font=f(italic=True,size=9,color="595959")
    # range headline
    r=5
    mr.cell(row=r,column=2,value="MARKET RANGE ($/lb finished, delivered)").font=f(bold=True,color="FFFFFF")
    for col in range(2,6): mr.cell(row=r,column=col).fill=HDR
    for i,(lab,val) in enumerate([("LOW",MARKET_LB_LO),("BASE",MARKET_LB_BASE),("HIGH",MARKET_LB_HI)]):
        mr.cell(row=6,column=3+i,value=lab).font=f(bold=True,color="FFFFFF"); mr.cell(row=6,column=3+i).fill=HDR; mr.cell(row=6,column=3+i).alignment=Alignment(horizontal="center")
        c=mr.cell(row=7,column=3+i,value=val); c.number_format=CUR; c.font=f(bold=True); c.fill=GOOD; c.alignment=Alignment(horizontal="center"); c.border=BORD
    mr.cell(row=7,column=2,value="all-in $/lb finished").font=f()
    mr.cell(row=8,column=2,value="  = per 450-lb drum").font=f(italic=True,size=9,color="595959")
    for i,val in enumerate([MARKET_LB_LO,MARKET_LB_BASE,MARKET_LB_HI]):
        c=mr.cell(row=8,column=3+i,value=round(val*DRUM_LB)); c.number_format=CUR0; c.font=f(italic=True,size=9,color="595959"); c.alignment=Alignment(horizontal="center")
    mr.cell(row=9,column=2,value="  vs SNP $0.75/lb").font=f(italic=True,size=9,color="595959")
    for i,val in enumerate([MARKET_LB_LO,MARKET_LB_BASE,MARKET_LB_HI]):
        c=mr.cell(row=9,column=3+i,value=val/SNP_LB); c.number_format='0.0"x"'; c.font=f(italic=True,size=9,color="595959"); c.alignment=Alignment(horizontal="center")

    # bottom-up
    r=11
    mr.cell(row=r,column=2,value="BOTTOM-UP BUILD (per lb finished)").font=f(bold=True,color="FFFFFF")
    for col in range(2,6): mr.cell(row=r,column=col).fill=HDR
    mr.cell(row=r,column=3,value="LOW").font=f(bold=True,color="FFFFFF"); mr.cell(row=r,column=4,value="BASE").font=f(bold=True,color="FFFFFF"); mr.cell(row=r,column=5,value="HIGH").font=f(bold=True,color="FFFFFF")
    for c in (3,4,5): mr.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    bu=[("Raw material (resin ~$1.52/lb x ~11%)",0.16,0.18,0.20),
        ("Conversion (labor $40/hr + QC + margin)",0.47,0.85,1.80),
        ("Freight (1-drum LTL, regional)",0.22,0.37,0.55),]
    rr=12
    for lab,lo,ba,hi in bu:
        mr.cell(row=rr,column=2,value=lab).font=f()
        for i,val in enumerate([lo,ba,hi]):
            c=mr.cell(row=rr,column=3+i,value=val); c.number_format=CUR; c.alignment=Alignment(horizontal="center"); c.border=BORD; c.font=f()
        rr+=1
    mr.cell(row=rr,column=2,value="ALL-IN $/lb").font=f(bold=True)
    for i,val in enumerate([MARKET_LB_LO,MARKET_LB_BASE,MARKET_LB_HI]):
        c=mr.cell(row=rr,column=3+i,value=val); c.number_format=CUR; c.font=f(bold=True); c.fill=AMB; c.alignment=Alignment(horizontal="center"); c.border=BORD

    # ceilings / anchors + caveats + sources
    notes=[
     "",
     "ANCHORS (sourced):",
     "- Retail ceiling: bulk PVA release solution ~$2.03/lb (US Composites, 20 gal) — a marked-up finished good; toll should sit below it.",
     "- Resin floor: PVA ~$1.38-1.60/lb (ChemAnalyst/IMARC, N.America 2026) -> material ~$0.16-0.20/lb of solution.",
     "- Loaded contract-mfg labor ~$40/hr incl overhead; 25% margin; QC ~$30/test (cited).",
     "- Density ~8.5 lb/gal -> 55 gal ~ 460 lb (Kuraray SG ~1.27).",
     "",
     "KEY CAVEAT:",
     "- No public toll/per-batch rate exists. The per-batch conversion/minimum fee ($400-900/batch est.) is triangulation, NOT a citation.",
     "- Energy is negligible (~$3-10/batch) and materials ~$0.20/lb — do not accept these as large line items.",
     "- The single biggest $/lb lever is batch size/frequency: 2 drums/batch roughly halves fixed-cost-per-lb.",
     "- Confidence: MODERATE. Pin it with 2-3 real quotes (APV / Piedmont / Columbus).",
     "",
     "SOURCES:",
     "- ChemAnalyst PVA pricing: chemanalyst.com/Pricing-data/polyvinyl-alcohol-1108",
     "- IMARC PVA pricing: imarcgroup.com/polyvinyl-alcohol-pricing-report",
     "- US Composites mold release (retail comp): uscomposites.com/moldrelease.html",
     "- Fibre Glast #13 PVA release film: fibreglast.com/products/pva-release-film-13",
     "- Contract-mfg cost-plus ($40/hr, 25% margin): blog.thedigisource.com/contract-manufacturing-cost-plus",
     "- ITC toll blending cost factors (qualitative): itctollblenders.com/2025/11/what-are-the-main-toll-blending-cost-factors/",
     "- Kuraray Poval physical properties (density): kuraray-poval.com (basic physical properties)",
     "- Drum LTL freight: volunteerdrum.com/drum-and-tote-shipping-costs-explained/",
    ]
    rr+=2
    for t in notes:
        c=mr.cell(row=rr,column=2,value=t)
        if t.endswith(":"): c.font=f(bold=True,color="1F3864")
        elif t.startswith("- "): c.font=f(size=8,color="404040")
        else: c.font=f(size=9,color="404040")
        rr+=1

    try: wb.calculation.fullCalcOnLoad=True
    except Exception: pass
    out="/home/user/Claude-Works/PVA second supplier initiative/PVA_Cost_Scenarios.xlsx"
    wb.save(out); print("saved",out)
    # echo key numbers
    print("SNP/drum",SNP_DRUM,"CJB landed/drum",round(CJB_LANDED),"baseline",round(baseline))
    for name,val in scen: print(f"  {name}: ${round(val):,}")

if __name__=="__main__":
    build()
