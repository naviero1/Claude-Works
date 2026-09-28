#!/usr/bin/env python3
"""v4: add PCI's real quote to the leadership workbook (new tabs, inputs) and build comparison charts."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.workbook.defined_name import DefinedName
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

DRUM=450; SNP=0.75; LBWK=1300; WEEKS=52; GROWTH=0.10
PCI_Q=3.50; PCI_SUB=6.00; BATCH=5
MKT=(0.85,1.40,2.55); CJB=8.42; JULY=(1.00,1.25); FORECAST=(2.50,3.75,5.00)
LB1=LBWK*WEEKS; DRUMS1=LB1/DRUM
def vol(y): return LB1*(1+GROWTH)**(y-1)
# Market tiers from the verified market study (market_tiers.json). Keys: low, competitive, high (+ *_range, n_*, points[]).
import json, os
TIERS=json.load(open("market_tiers.json")) if os.path.exists("market_tiers.json") else {}
def tier(k): return TIERS.get(k)
def tier_txt(k): return (f"${TIERS[k]:.2f}" if TIERS.get(k) is not None else "PENDING — market study running")

# ---------- economics ----------
pci_drums=50; pci_lb=pci_drums*DRUM                       # 10 batches of 5
snp_lb=LB1-pci_lb
A35_total=snp_lb*SNP+pci_lb*PCI_Q; A35_prem=A35_total-LB1*SNP
sub_lb=pci_lb; A6_total=(LB1-sub_lb)*SNP+sub_lb*PCI_SUB; A6_prem=A6_total-LB1*SNP      # same one-third, ordered below batch size
cjb_total=(LB1-sub_lb)*SNP+sub_lb*CJB; cjb_prem=cjb_total-LB1*SNP
five_prem=sum(vol(y)/3*(PCI_Q-SNP) for y in range(1,6))
batch_lb=BATCH*DRUM; days_full=batch_lb/(LBWK/7); cycle_wk=batch_lb/(LBWK/3); snp_on_wk=cycle_wk-batch_lb/LBWK
days_two_thirds=batch_lb/(LBWK*2/3/7)
print(f"A@3.50: total ${A35_total:,.0f} premium ${A35_prem:,.0f} ({A35_prem/(LB1*SNP):.0%}); 5yr ${five_prem:,.0f}; BE 5% ${A35_prem/.05:,.0f} 10% ${A35_prem/.10:,.0f}")
print(f"A@6 (same 1/3, below batch size): total ${A6_total:,.0f} premium ${A6_prem:,.0f} ({A6_prem/(LB1*SNP):.0%})")
print(f"Batch {batch_lb} lb = {days_full:.1f} days at full rate; cycle {cycle_wk:.2f} wk; SNP on {snp_on_wk:.2f} wk; at 2/3 rate {days_two_thirds:.1f} days")
print(f"One qualification batch: cost ${batch_lb*PCI_Q:,.0f}, premium over SNP ${batch_lb*(PCI_Q-SNP):,.0f}")

# ---------- workbook ----------
wb=openpyxl.load_workbook("PVA_Second_Supplier_Leadership_Model.xlsx")
NAVY="1F3864"; GREY="595959"
HDR=PatternFill("solid",fgColor=NAVY); SUB=PatternFill("solid",fgColor="D6DCE5"); INP=PatternFill("solid",fgColor="FFF2CC")
OUT=PatternFill("solid",fgColor="F2F2F2"); GOOD=PatternFill("solid",fgColor="C6EFCE"); BAD=PatternFill("solid",fgColor="FFC7CE"); AMB=PatternFill("solid",fgColor="FFEB9C")
thin=Side(style="thin",color="BFBFBF"); BORD=Border(left=thin,right=thin,top=thin,bottom=thin)
def F(bold=False,size=10,color="000000",italic=False): return Font(name="Arial",bold=bold,size=size,color=color,italic=italic)
CUR='"$"#,##0'; CUR2='"$"#,##0.00'; PCT='0%'; NUM='#,##0'
def title(ws,t,sub=None):
    ws['B2']=t; ws['B2'].font=F(True,14,NAVY)
    if sub: ws['B3']=sub; ws['B3'].font=F(False,9,GREY,True)
def hdr(ws,r,cols,c0=2):
    for i,h in enumerate(cols):
        c=ws.cell(row=r,column=c0+i,value=h); c.fill=HDR; c.font=F(True,10,"FFFFFF"); c.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True); c.border=BORD
    ws.row_dimensions[r].height=30
def name(n,ref): wb.defined_names[n]=DefinedName(n,attr_text=ref)
def wrow(ws,r,vals,fmts=None,fill=None,bold_first=True,wrap=False):
    for i,v in enumerate(vals):
        c=ws.cell(row=r,column=2+i,value=v); c.border=BORD; c.font=F(bold_first and i==0)
        if fmts and fmts[i]: c.number_format=fmts[i]
        if fill: c.fill=fill
        if wrap: c.alignment=Alignment(wrap_text=True,vertical="top")
for t in ("Supplier Quotes","PCI Quote Scenarios","PCI Experiment"):
    if t in wb.sheetnames: del wb[t]

# ---- Inputs: append PCI quote rows ----
ws=wb["Inputs"]; r=ws.max_row+2
if "PCIq" in wb.defined_names:
    r=None
if r is not None:
  ws.cell(row=r,column=2,value="PCI MANUFACTURING — REAL QUOTE (2026-09-28)").font=F(True,10,NAVY); r+=1
  for lab,val,fmt,note,nm in [("PCI quoted price — one batch of 5 drums ($/lb)",PCI_Q,CUR2,"Real quote. CONFIRM: delivered? materials, drum, freight included? validity period?","PCIq"),
                            ("PCI price — orders below one batch ($/lb)",PCI_SUB,CUR2,"Real quote. Makes any sub-batch (e.g. 1 drum/week) uneconomic.","PCIsub"),
                            ("PCI batch size (drums)",BATCH,NUM,"One batch = 5 drums = 2,250 lb = ~12 days of full demand","PCIbatch")]:
      ws.cell(row=r,column=2,value=lab).font=F(); c=ws.cell(row=r,column=3,value=val); c.number_format=fmt; c.fill=INP; c.font=F(True); c.border=BORD
      ws.cell(row=r,column=4,value=note).font=F(False,9,GREY,True); name(nm,f"Inputs!$C${r}"); r+=1
  ws.cell(row=r,column=2,value="The $2.50 / $3.75 / $5.00 rows above were the pre-quote forecast; keep for history. The quote ($3.50) sits at the forecast mid.").font=F(False,9,GREY,True)

# ---- Repoint the pre-quote tabs (5-Year, Sensitivity, SNP Re-price, Break-even, Options) to the real quote and the 50-drum share ----
ws=wb["Inputs"]
ws["B11"]="Legacy: pre-quote supplier minimum (drums/week) — superseded by batch pricing (rows 27–29)"; ws["D11"]="Kept for history. The real constraint is whole 5-drum batches at $3.50; anything smaller is $6.00/lb."
ws["D12"]="Legacy (34.6%). Not used by any headline figure."
ws["D13"]="One-third of demand is the target share for Option A."
ws["C14"]="=ROUNDDOWN(Share*LbWk*Weeks/(DrumLb*PCIbatch),0)*DrumLb*PCIbatch/(LbWk*Weeks)"; ws["D14"]="One-third rounded DOWN to whole 5-drum batches: Year 1 = 10 batches = 50 drums = 22,500 lb = 33.3% — the figure on the slides."
ws["C16"]="=PCIq"; ws["D16"]="= the real quote (row 27). Every 'MID' figure in the legacy tabs now uses $3.50."
ws["D15"]="Sensitivity band below the quote"; ws["D17"]="Sensitivity band above the quote"
ws["B30"]="The $2.50 / $5.00 rows are kept as a sensitivity band; MID points at the real quote ($3.50), within 7% of the pre-quote mid-case ($3.75)."
if tier("high") is not None:
    for cell,k,lab in [("18","high","Market — HIGH quantity, bulk/tote ($/lb)"),("19","competitive","Market — COMPETITIVE quantity, drum scale ($/lb)"),("20","low","Market — LOW quantity, small packs ($/lb)")]:
        ws["B"+cell]=lab; ws["C"+cell]=tier(k); ws["D"+cell]=f"Verified market study 2026-09-28 — comparable pre-mixed PVA solutions; range {TIERS.get(k+'_range','—')}, n={TIERS.get('n_'+k,'—')}"
fy=wb["5-Year"]; fy["B3"]="Second source at an exact one-third of each year's demand (batches round differently each year). The Year-1 headline elsewhere uses 10 whole batches (50 drums, $61,875) — $92 apart. Premium = share x (PCI price - SNP price) x volume; MID = the real quote."
for r_ in range(6,11): fy[f"E{r_}"]="=Share"
sv=wb["Sensitivity"]; sv["B2"]="What drives the premium (Year 1, second source = 10 whole 5-drum batches = 50 drums)"; sv["B3"]="Price is what the market gives us. Below one 5-drum batch PCI charges $6.00/lb, so there is no cheap small-order version."
sv["C6"]="Market — high quantity (bulk/tote)"; sv["C9"]="Market — competitive quantity (drum scale)"; sv["C12"]="Market — low quantity (small packs)"
sv["C7"]="July 2026 assumption, low (superseded)"; sv["C8"]="July 2026 assumption, high (superseded)"
sv["C13"]="Sensitivity — below the quote"; sv["C14"]="PCI real quote ($3.50, one 5-drum batch)"; sv["C15"]="Sensitivity — above the quote"
sv["C17"]="Batches of 5 drums / yr"; sv["D17"]="Available at $3.50?"; sv["E17"]="Premium @ PCI quote"
for r_ in range(18,23):
    sv[f"C{r_}"]=f"=B{r_}*LbWk*Weeks/(DrumLb*PCIbatch)"; sv[f"C{r_}"].number_format='0.0'
    sv[f"D{r_}"]=f'=IF(C{r_}<1,"Below one batch — $6.00/lb","Yes at $3.50 — no volume term attached to the batch price so far (confirm in writing)")'
    sv[f"E{r_}"]=f"=B{r_}*LbWk*Weeks*(PCIq-SNPlb)"; sv[f"E{r_}"].number_format=CUR
sv["B24"]="No small-order version exists at this price: below a 5-drum batch PCI charges $6.00/lb. Above it, the $3.50 batch price carries no volume term so far — Option 3 (1–2 batches a year) rests on that; confirm it in writing."
wb["SNP Re-price"]["B2"]="If SNP Inc. raises price on the volume it keeps (Year 1, PCI quote $3.50, 50 drums to PCI)"
be=wb["Break-even"]; be["B6"]="Sensitivity $2.50"; be["B7"]="PCI quote $3.50"; be["B8"]="Sensitivity $5.00"
be["B3"]="Option A is justified only if: annual premium <= P(SNP disruption in a year) x loss the second source would AVOID. Full avoidance counts only with PCI's written ramp commitment; with ~1/3 coverage, the outage must be ~3x larger."
op=wb["Options"]; op["B2"]="The options, side by side (Year 1, PCI quote $3.50; second source = 10 whole 5-drum batches = 50 drums)"
op["B3"]="Legacy A/B layout = Option 1 / Option 2. Option 3 (keep-alive: 1–2 batches of 5 drums a year at $3.50, no volume term so far) is on the PCI Quote Scenarios and Summary tabs."
op["D11"]="~3-6 months cold start (decays after ~12 months idle); ~2-3 with a yearly re-check batch"; op["C12"]="Lost a third of its volume; cadence level only if we carry a small rolling stock"

# ---- Supplier Quotes ----
ws=wb.create_sheet("Supplier Quotes",1)
title(ws,"All price points on the table — real quotes vs references","One place for every $/lb figure used anywhere in the analysis, with its basis. Real quotes in green; references in grey; superseded assumptions in amber.")
hdr(ws,5,["Source","$/lb finished","Basis / terms","Type","Status","Date / reference"])
rows=[("SNP Inc. (Durham, NC) — incumbent",0.75,"Delivered, all-in. 1/450-lb drum. ~2.9 drums/week today.","REAL QUOTE","Active sole source","SNP Estimate 012726-1"),
      ("PCI Manufacturing (St. Louis, MO) — one 5-drum batch",3.50,"One batch = 5 drums (2,250 lb). Confirm delivered/all-in and validity.","REAL QUOTE","Capable — experiment successful; not yet contracted","2026-09-28"),
      ("PCI Manufacturing — below one batch",6.00,"Any order smaller than 5 drums (e.g. 1 drum/week).","REAL QUOTE","Uneconomic version","2026-09-28"),
      ("CJB Applied Technologies (Valdosta, GA)",8.42,"$8.00–8.50/lb toll EXCLUDING materials + ~$75/drum resin = ~$8.42 landed. Their trial would have cost $6,400 (per Oscar, 28 Sep; the email thread recorded a $4,900 qualification fee + $700 x 7 batch credit) — we declined, so their capability was never corroborated.","REAL QUOTE","Eliminated on price 2026-08-04 (~11x SNP); trial declined","CJB email 'RE: mix test'"),
      ("Brenntag (distributor) — trial blends, Nov 2025 onward",None,"Tried our formula (125 grade and the requested grade): viscosity above range, unreadable on their viscometer. They stalled; no quote was ever received. Mar 2026: sent us a 125-grade resin sample instead.","NO QUOTE","Never met viscosity; no quote","Sam (Brenntag) emails"),
      ("Market — COMPETITIVE quantity (drum scale, 30–55 gal)",tier("competitive"),f"Inferred from comparable pre-mixed PVA solutions sold today; range {TIERS.get('competitive_range','—')}; n={TIERS.get('n_competitive','—')}","MARKET STUDY","Reference — see Market Study tab","Verified market study 2026-09-28"),
      ("Market — LOW quantity (pints to 5-gal pails)",tier("low"),f"Retail/lab packs; range {TIERS.get('low_range','—')}; n={TIERS.get('n_low','—')}","MARKET STUDY","Reference — see Market Study tab","Verified market study 2026-09-28"),
      ("Market — HIGH quantity (totes / bulk / tonnage)",tier("high"),f"Bulk and contract pricing; range {TIERS.get('high_range','—')}; n={TIERS.get('n_high','—')}. Quality/regulatory context differs.","MARKET STUDY","Reference — see Market Study tab","Verified market study 2026-09-28"),
      ("— Superseded / historical references (kept for the record) —",None,"","","",""),
      ("Triangulated market LOW / BASE / HIGH (Sept)",1.40,"$0.85 / $1.40 / $2.55 — resin floor + labor build-up + retail ceiling","TRIANGULATED","SUPERSEDED by market study","Market Research tab (cost-scenarios workbook)"),
      ("Material floor",0.18,"PVA resin $1.26–1.60/lb x 11% solids = $0.14–0.18 (upper bound plotted)","DERIVED","Reference only","ChemAnalyst / IMARC 2026"),
      ("July 2026 assumption (key performance indicator (KPI) review deck)",1.125,"'$1.00–1.25/lb, ~35% share, ~$6–12k/yr insurance'","ASSUMPTION","SUPERSEDED by PCI quote","KPI review deck 2026-07-09"),
      ("Pre-quote forecast (this deck, Sept)",3.75,"$2.50 low / $3.75 mid / $5.00 high","ASSUMPTION","SUPERSEDED by PCI quote (quote = mid)","2026-09-22")]
for i,(a,b,c,d,e,f) in enumerate(rows):
    rr=6+i; fill=GOOD if d=="REAL QUOTE" else (AMB if d=="ASSUMPTION" else (SUB if d=="MARKET STUDY" else OUT))
    wrow(ws,rr,[a,(b if b is not None else ("" if a.startswith("—") else "pending")),c,d,e,f],[None,CUR2,None,None,None,None],fill=fill,wrap=True)

# ---- Market Study (data points + tiers) ----
if "Market Study" in wb.sheetnames: del wb["Market Study"]
ms=wb.create_sheet("Market Study",2)
title(ms,"Market study — comparable pre-mixed PVA solutions, by quantity tier","Every data point verified against its URL; $/lb of SOLUTION (8.5 lb/gal unless weight given). Polyvinyl ALCOHOL only — acetate glues, resin powder and films excluded.")
hdr(ms,5,["Tier","Recommended $/lb for chart","Range","n","Basis"])
for i,(k,lab) in enumerate([("competitive","COMPETITIVE quantity — drum scale (30–55 gal)"),("low","LOW quantity — pints to 5-gal pails"),("high","HIGH quantity — totes / bulk / tonnage")]):
    r=6+i; wrow(ms,r,[lab,(tier(k) if tier(k) is not None else "pending"),TIERS.get(k+"_range","—"),TIERS.get("n_"+k,"—"),TIERS.get(k+"_basis","")],[None,CUR2,None,None,None],wrap=True)
hdr(ms,11,["Product","Vendor","Chemistry","Solids %","Pack","Pack lb","Price $","$ / lb","Tier","Verdict","URL"])
for i,p in enumerate(TIERS.get("points",[])):
    r=12+i; wrow(ms,r,[p.get("product"),p.get("vendor"),p.get("chemistry"),p.get("solids_pct"),p.get("pack_size"),p.get("pack_lb"),p.get("price_usd"),p.get("usd_per_lb"),p.get("quantity_tier"),p.get("verdict"),p.get("url")],[None,None,None,None,None,NUM,CUR2,CUR2,None,None,None],wrap=False,bold_first=False)
for c,w in zip("BCDEFGHIJKL",[40,22,14,9,14,9,10,9,13,11,60]): ms.column_dimensions[c].width=w
for c,w in zip("BCDEFG",[44,13,58,14,34,30]): ws.column_dimensions[c].width=w

# ---- PCI Quote Scenarios ----
ws=wb.create_sheet("PCI Quote Scenarios",2)
title(ws,"What PCI's real quote means — Year 1 and five years","Second source at one-third of demand = 50 drums/yr = 10 batches of 5. Formulas reference Inputs.")
hdr(ws,5,["Scenario","Drums to PCI / yr","PCI $/lb","PCI annual $","SNP annual $ (retained)","Total $","Premium vs all-SNP","x today's spend"])
sc=[("All-SNP (today) = Option 2 purchase cost","0","SNPlb"),("Option 1 — PCI at 1/3 (50 drums = 10 batches of 5) at $3.50 — chart bar","50","PCIq"),("Option 1 — same 1/3 but ordered below batch size ($6.00) — chart bar","50","PCIsub"),("CJB at the same 1/3 (for scale) — chart bar","50","CJBlb"),("Option 3 — keep-alive: 1 batch of 5 drums / yr at $3.50","5","PCIq"),("Option 3 — keep-alive: 2 batches (10 drums) / yr at $3.50","10","PCIq"),("Reference: 1 drum/week (52 drums) at the below-batch price","52","PCIsub")]
for i,(lab,d,p) in enumerate(sc):
    r=6+i; ws.cell(row=r,column=2,value=lab).font=F(True); ws.cell(row=r,column=3,value=int(d)).number_format=NUM
    ws.cell(row=r,column=4,value=f"={p}").number_format=CUR2
    ws.cell(row=r,column=5,value=f"=C{r}*DrumLb*D{r}").number_format=CUR
    ws.cell(row=r,column=6,value=f"=(LbWk*Weeks-C{r}*DrumLb)*SNPlb").number_format=CUR
    ws.cell(row=r,column=7,value=f"=E{r}+F{r}").number_format=CUR
    ws.cell(row=r,column=8,value=f"=G{r}-LbWk*Weeks*SNPlb").number_format=CUR
    ws.cell(row=r,column=9,value=f"=H{r}/(LbWk*Weeks*SNPlb)").number_format='0.00"x"'
    for c in range(2,10): ws.cell(row=r,column=c).border=BORD
    if i==1:
        for c in range(2,10): ws.cell(row=r,column=c).fill=AMB
r=14; ws.cell(row=r,column=2,value="Five years at 1/3 share (Option 1), PCI $3.50, volume +10%/yr").font=F(True,11,NAVY); r+=1
hdr(ws,r,["Year","Volume (lb)","Lb to PCI (1/3)","Batches of 5 (rounded)","Premium ($2.75/lb x lb to PCI)","Cumulative"]); r+=1
for y in range(1,6):
    ws.cell(row=r,column=2,value=y).font=F(True)
    ws.cell(row=r,column=3,value=f"=LbWk*Weeks*(1+Growth)^({y}-1)").number_format=NUM
    ws.cell(row=r,column=4,value=f"=C{r}/3").number_format=NUM
    ws.cell(row=r,column=5,value=f"=ROUND(D{r}/DrumLb/PCIbatch,0)").number_format=NUM
    ws.cell(row=r,column=6,value=f"=D{r}*(PCIq-SNPlb)").number_format=CUR
    ws.cell(row=r,column=7,value=(f"=F{r}" if y==1 else f"=G{r-1}+F{r}")).number_format=CUR
    for c in range(2,8): ws.cell(row=r,column=c).border=BORD
    r+=1
r+=1; ws.cell(row=r,column=2,value="Break-even — outage cost that justifies the premium").font=F(True,11,NAVY); r+=1
hdr(ws,r,["Premium (Y1)","p = 2%","p = 5%","p = 10%","p = 20%"]); r+=1
ws.cell(row=r,column=2,value="=H7").number_format=CUR
for j,p in enumerate([0.02,0.05,0.10,0.20]): ws.cell(row=r,column=3+j,value=f"=B{r}/{p}").number_format=CUR
for c in range(2,7): ws.cell(row=r,column=c).border=BORD
r+=2; ws.cell(row=r,column=2,value="Block-rotation logistics of a 5-drum batch (shelf life 18 days)").font=F(True,11,NAVY); r+=1
for lab,f,fmt,note in [("Batch size (lb)","=PCIbatch*DrumLb",NUM,""),
                       ("Days of FULL demand in one batch","=B{r0}/(LbWk/7)",'0.0',"12.1 days — must be consumed within the shelf life -> use at full rate on receipt"),
                       ("Cycle length at 1/3 share (weeks)","=B{r0}/(LbWk/3)",'0.0',"One PCI batch every ~5 weeks (Year 1: 10 batches; ~15 by Year 5)"),
                       ("Weeks on SNP material per cycle","=B{r2}-B{r0}/LbWk",'0.0',"Cadence is a choice: (i) block rotation = a ~12-day pause in SNP orders per cycle; (ii) SNP keeps ~2 drums/wk and we hold ~3 drums of rolling stock (peak ~8 drums, strict first-in-first-out) — the shelf-life study decides"),
                       ("Age of PCI drums on receipt (days: cook, release, transit) — INPUT",4,'0',"Assumption: the 18-day clock starts at manufacture. Confirm PCI lead time and transit St. Louis -> site"),
                       ("Usable days on receipt (18-day life)","=18-B{r4}",'0.0',""),
                       ("Slack in block rotation (days)","=B{r5}-B{r1}",'0.0',"~1–2 days: block rotation has almost no margin at 18 days; a validated 21-day life gives real margin"),
                       ("Days to consume a batch at 2/3 rate","=B{r0}/(LbWk*2/3/7)",'0.0',"18.2 days — needs a validated life longer than 18.2 days plus the age on receipt"),
                       ("Days to consume a batch at an exact 1/3 rate","=B{r0}/(LbWk/3/7)",'0.0',"36.3 days — a true one-third blend needs a ~40-day validated life"),
                       ("Minimum PCI share of rate under a 30-day life","=B{r0}/((30-B{r4})*LbWk/7)",PCT,"~47% at 4 days' age: even a 30-day life does not allow a one-third blend"),
                       ("One qualification batch — cost","=B{r0}*PCIq",CUR,"A single production-scale batch (Option B-plus); $7.9k gross"),
                       ("One qualification batch — premium over SNP","=B{r0}*(PCIq-SNPlb)",CUR,"3.3% of annual volume (2,250 of 67,600 lb); one ~12-day pause in SNP orders")]:
    r0=r if lab.startswith("Batch size") else r0
    ws.cell(row=r,column=2,value=lab).font=F(True)
    c=ws.cell(row=r,column=3,value=(f.format(r0=r0,r1=r0+1,r2=r0+2,r4=r0+4,r5=r0+5) if isinstance(f,str) else f)); c.number_format=fmt; c.border=BORD
    if not isinstance(f,str): c.fill=INP
    ws.cell(row=r,column=4,value=note).font=F(False,9,GREY,True); r+=1
for c,w in zip("BCDEFGHI",[46,16,12,16,20,14,18,12]): ws.column_dimensions[c].width=w

# ---- PCI Experiment ----
ws=wb.create_sheet("PCI Experiment",3)
title(ws,"PCI Manufacturing — qualification experiment record","What was tested, what was found, what is still open. Source: email-chain summary 2026-09-22 + quote 2026-09-28.")
hdr(ws,5,["Attribute","Status","Result / detail"])
exp=[("Capability — 90–95 °C cook","PROVEN","Lab batches produced; dissolution achieved"),
     ("Viscosity (primary concern)","ROOT CAUSE FOUND","First sample 2,420 cP vs ~1,000 target; dilution to 10.8% solids -> 1,590 cP; cause = elevated solids from water loss during processing; fix = water adjustment at end of mix"),
     ("Agreed fresh-material spec","LOCKED","11% total solids; 900–1,100 cP fresh (Brookfield #3, 10 rpm, 25 °C); <2,500 cP ceiling"),
     ("Colour","NOT A CRITERION","No formal spec; minor mismatch acceptable"),
     ("Shelf-life study","REQUESTED","Viscosity every 3–5 days; trend to usable life (18 vs 30 days matters for batch logistics)"),
     ("Hydrogel compression strength","PLANNED","vs current material — must hold on 100% PCI material under block rotation"),
     ("Cleaning / residual film","OPEN","Film observed during processing; vinegar partially effective; procedure not final"),
     ("Viscometer method basis","OPEN","10 vs 60 rpm, LV vs RV series — all cP comparisons depend on it"),
     ("Commercial — price","QUOTED","$3.50/lb at one 5-drum batch; $6.00/lb below a batch"),
     ("Commercial — terms to confirm","OPEN","Delivered/all-in? Validity? ~10 batches/yr on a ~5-week rhythm acceptable? Crisis ramp to ~3 batches/month? Resin grade/producer (sub-tier convergence with SNP)?"),
     ("What PCI has invested (unpaid)","NOTED","Two+ lab batches, dilution study, method work, revised process — months of engineering on a ~$50k/yr account")]
for i,(a,b,c_) in enumerate(exp):
    r=6+i; fill=GOOD if b in ("PROVEN","LOCKED","ROOT CAUSE FOUND","QUOTED") else (AMB if b in ("REQUESTED","PLANNED","NOTED","NOT A CRITERION") else BAD)
    wrow(ws,r,[a,b,c_],fill=fill,wrap=True); ws.row_dimensions[r].height=32
for c,w in zip("BCD",[34,20,100]): ws.column_dimensions[c].width=w

# ---- Summary: every slide figure as a formula ----
if "Summary" in wb.sheetnames: del wb["Summary"]
sm=wb.create_sheet("Summary",0)
title(sm,"Summary — the figures on the leadership slides (all formulas; change Inputs and this tab follows)","Second source = one-third of demand rounded down to whole 5-drum batches (Year 1: 10 batches = 50 drums = 22,500 lb), identical in every option. Internal hours and one-time costs are on the slides, not here.")
hdr(sm,5,["Figure","Value","Where it is used"])
srows=[("Demand, Year 1 (lb)","=LbWk*Weeks",NUM,"Slide 5 — identical in every bar"),
 ("Demand, Year 1 (drums)","=LbWk*Weeks/DrumLb",'0',"Slide 5"),
 ("Second source, Year 1 (lb)","=EffShare*LbWk*Weeks",NUM,"Slide 5 — every option"),
 ("Second source (drums / batches)",'=ROUND(EffShare*LbWk*Weeks/DrumLb,0)&" drums / "&ROUND(EffShare*LbWk*Weeks/(DrumLb*PCIbatch),0)&" batches of 5"',None,"Slides 3, 5, 7, 8"),
 ("All-SNP annual spend (today)","=LbWk*Weeks*SNPlb",CUR,"Slide 5"),
 ("SNP Inc. retained spend (2/3) — same in every option","=(1-EffShare)*LbWk*Weeks*SNPlb",CUR,"Slide 5"),
 ("Option A annual — PCI $3.50","=(1-EffShare)*LbWk*Weeks*SNPlb+EffShare*LbWk*Weeks*PCIq",CUR,"Slides 5, 8"),
 ("Premium vs today (Year 1)","=B12-B10",CUR,"Slides 5, 6, 8, 11"),
 ("Premium as % of today's spend","=B13/B10",PCT,"Slide 5"),
 ("Same 1/3 at PCI's below-batch price $6.00","=(1-EffShare)*LbWk*Weeks*SNPlb+EffShare*LbWk*Weeks*PCIsub",CUR,"Slide 5"),
 ("Same 1/3 at CJB $8.42 (for scale)","=(1-EffShare)*LbWk*Weeks*SNPlb+EffShare*LbWk*Weeks*CJBlb",CUR,"Slide 5"),
 ("Five-year premium at $3.50 (exact third, +10%/yr, undiscounted)","='5-Year'!L11",CUR,"Slides 6, 8"),
 ("Break-even avoided loss @ p = 10%/yr","=B13/0.10",CUR,"Slide 11"),
 ("Break-even avoided loss @ p = 5%/yr","=B13/0.05",CUR,"Slide 11"),
 ("Break-even avoided loss @ p = 2%/yr","=B13/0.02",CUR,"Appendix"),
 ("One 5-drum batch — cost (gross)","=PCIbatch*DrumLb*PCIq",CUR,"Slides 6, 8, 9, 11"),
 ("One 5-drum batch — premium over SNP","=PCIbatch*DrumLb*(PCIq-SNPlb)",CUR,"Slides 6, 9"),
 ("One batch as % of annual volume","=PCIbatch*DrumLb/(LbWk*Weeks)",'0.0%',"Slides 6, 8"),
 ("Batch = days of full demand","=PCIbatch*DrumLb/(LbWk/7)",'0.0',"Slides 3, 7"),
 ("Cycle at one-third (weeks)","=PCIbatch*DrumLb/(LbWk/3)",'0.0',"Slide 7"),
 ("Premium if PCI were $1.50/lb (trigger)","=EffShare*LbWk*Weeks*(1.5-SNPlb)",CUR,"Slide 11"),
 ("Option 3 — one batch/yr: gross / premium","=PCIbatch*DrumLb*PCIq&\" / \"&PCIbatch*DrumLb*(PCIq-SNPlb)",None,"Slides 6, 8, 9, 11"),
 ("Option 3 — two batches/yr: gross / premium","=2*PCIbatch*DrumLb*PCIq&\" / \"&2*PCIbatch*DrumLb*(PCIq-SNPlb)",None,"Slides 8, 9"),
 ("Option 3 — share of volume at 1 / 2 batches","=TEXT(PCIbatch*DrumLb/(LbWk*Weeks),\"0.0%\")&\" / \"&TEXT(2*PCIbatch*DrumLb/(LbWk*Weeks),\"0.0%\")",None,"Slide 8")]
for i,(a,f,fmt,u) in enumerate(srows):
    rr=6+i; wrow(sm,rr,[a,f,u],[None,fmt,None],fill=(AMB if a.startswith("Premium vs today") else None))
for c,w in zip("BCD",[58,20,34]): sm.column_dimensions[c].width=w
order=["Summary","Inputs","Supplier Quotes","Market Study","PCI Quote Scenarios","PCI Experiment","5-Year","Sensitivity","SNP Re-price","Break-even","Options"]
wb._sheets=[wb[n] for n in order if n in wb.sheetnames]+[ws_ for ws_ in wb._sheets if ws_.title not in order]
wb.save("PVA_Second_Supplier_Leadership_Model.xlsx"); print("workbook updated:", wb.sheetnames)

# ---------- charts ----------
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10})
NAV="#1F3864"; STL="#4E79A7"; REDc="#B23A2E"; GRN="#2E7D46"; LGT="#D6DCE5"; AMBc="#C9A227"
money=FuncFormatter(lambda v,_: (f"${v/1e6:,.1f}M" if v>=1e6 else f"${v/1000:,.0f}k"))

# Chart A: $/lb side by side
def rng(k):
    s=TIERS.get(k+"_range");
    try:
        lo,hi=[float(x.replace("$","").strip()) for x in s.replace("–","-").split("-")[:2]]; return lo,hi
    except Exception: return None
labels=["Market —\nhigh quantity\n(bulk / tote)","Market —\ncompetitive quantity\n(drum scale)","Market —\nlow quantity\n(small packs)","SNP Inc.\n(real quote)","PCI 5-drum\nbatch (real)","PCI below\nbatch (real)","CJB\n(real quote)"]
vals=[tier("high"),tier("competitive"),tier("low"),0.75,3.50,6.00,8.42]
PCI_D="#B9770E"; PCI_L="#E3B24A"; G1="#8E9BA7"; G2="#B5BFC9"; G3="#D6DCE5"   # PCI: two shades of one amber; market: three greys
cols=[G3,G1,G2,GRN,PCI_D,PCI_L,REDc]
keep=[i for i,v in enumerate(vals) if v is not None]
labels=[labels[i] for i in keep]; vals=[vals[i] for i in keep]; cols=[cols[i] for i in keep]
fig,ax=plt.subplots(figsize=(11,5.4)); bars=ax.bar(labels,vals,color=cols,edgecolor="white")
for lab,b,v in zip(labels,bars,vals):
    ax.text(b.get_x()+b.get_width()/2,v+0.12,f"${v:.2f}",ha="center",va="bottom",fontsize=9.5,fontweight="bold")
    key={"high":"high","competitive":"competitive","low":"low"}
    for k in key:
        if lab.startswith("Market") and k in lab.split("\n")[1] and rng(k):
            lo,hi=rng(k); ax.vlines(b.get_x()+b.get_width()/2,lo,hi,color="#7A8A99",lw=1.4); ax.hlines([lo,hi],b.get_x()+b.get_width()*0.35,b.get_x()+b.get_width()*0.65,color="#7A8A99",lw=1.4)
ax.set_ylabel("$ per lb of finished solution"); ax.set_title("Price per pound, side by side — market price of comparable PVA solutions by quantity, then the real quotes",fontsize=12,color=NAV,loc="left",fontweight="bold")
ax.spines[["top","right"]].set_visible(False); ax.set_ylim(0,9.6); plt.tight_layout(); plt.savefig("chart_price_side_by_side.png",dpi=180); plt.close()

# Chart B: annual cost side by side — SAME demand and SAME one-third second-source quantity in every option
share_lb=pci_drums*DRUM; snp_keep=LB1-share_lb          # 22,500 lb (50 drums) / 45,100 lb
scen=[("All-SNP\n(today)",LB1*SNP,0,None),
      ("PCI $3.50\n5-drum batches",snp_keep*SNP,share_lb*PCI_Q,PCI_Q),
      ("PCI $6.00\nordered below batch size",snp_keep*SNP,share_lb*PCI_SUB,PCI_SUB),
      ("CJB $8.42\n(for scale)",snp_keep*SNP,share_lb*CJB,CJB)]
fig,ax=plt.subplots(figsize=(11,5.4)); x=range(len(scen))
ax.bar(x,[s[1] for s in scen],color=GRN,label="SNP Inc. at $0.75/lb")
second_cols=[NAV,PCI_D,PCI_L,REDc]
ax.bar(x,[s[2] for s in scen],bottom=[s[1] for s in scen],color=second_cols,label="Second source — one-third of demand (22,500 lb, 50 drums): PCI amber, CJB red")
for i,s in enumerate(scen):
    tot=s[1]+s[2]; prem=tot-LB1*SNP
    ax.text(i,tot+4500,f"${tot/1000:,.1f}k"+(f"\n+${prem/1000:,.1f}k  ({prem/(LB1*SNP):.0%})" if prem>0 else ""),ha="center",va="bottom",fontsize=9.5,fontweight="bold")
    lb_snp=LB1 if s[2]==0 else snp_keep
    ax.text(i,s[1]/2,f"{lb_snp:,.0f} lb\n${s[1]/1000:,.1f}k",ha="center",va="center",fontsize=8.5,color="white",fontweight="bold")
    if s[2]>0: ax.text(i,s[1]+s[2]/2,f"{share_lb:,.0f} lb × ${s[3]:.2f}\n${s[2]/1000:,.1f}k",ha="center",va="center",fontsize=8.5,color=(NAV if second_cols[i]==PCI_L else "white"),fontweight="bold")
ax.set_xticks(list(x)); ax.set_xticklabels([s[0] for s in scen]); ax.yaxis.set_major_formatter(money); ax.set_ylabel("Annual PVA spend (one year)")
ax.set_title(f"Annual cost side by side — demand {LB1:,.0f} lb/yr ({DRUMS1:.0f} drums); second source at one-third in every option",fontsize=11.5,color=NAV,loc="left",fontweight="bold")
ax.legend(frameon=False,loc="upper left",fontsize=9); ax.spines[["top","right"]].set_visible(False); ax.set_ylim(0,max(s[1]+s[2] for s in scen)*1.24); plt.tight_layout(); plt.savefig("chart_annual_side_by_side.png",dpi=180); plt.close()
print(f"apples-to-apples @1/3: PCI$6 total ${snp_keep*SNP+share_lb*PCI_SUB:,.0f} (+${share_lb*(PCI_SUB-SNP):,.0f}); CJB total ${snp_keep*SNP+share_lb*CJB:,.0f} (+${share_lb*(CJB-SNP):,.0f})")

# Chart C: the three options — first 12 months all-in (range) and each year after (range), $k
opts=[("Option 1\nSecond supplier at 1/3",(80,110),(65,70),PCI_D),
      ("Option 2\nStrengthen SNP Inc. only",(13,32),(3,12),GRN),
      ("Option 3\nKeep-alive: 1–2 batches/yr",(31,78),(9,24),STL)]
fig,ax=plt.subplots(figsize=(12,2.0)); y=list(range(len(opts)))[::-1]
for yi,(lab,y1,yr,col) in zip(y,opts):
    ax.barh(yi+0.18,y1[1]-y1[0],left=y1[0],height=0.32,color=col,alpha=0.95)
    ax.barh(yi-0.18,yr[1]-yr[0],left=yr[0],height=0.32,color=col,alpha=0.45)
    ax.text(y1[1]+1.5,yi+0.18,f"${y1[0]}–{y1[1]}k first 12 months, all-in",va="center",fontsize=9,fontweight="bold",color=NAV)
    ax.text(yr[1]+1.5,yi-0.18,f"${yr[0]}–{yr[1]}k each year after",va="center",fontsize=8.5,color="#595959")
ax.set_yticks(y); ax.set_yticklabels([o[0] for o in opts],fontsize=9.5,fontweight="bold",color=NAV)
ax.set_xlim(0,150); ax.xaxis.set_major_formatter(FuncFormatter(lambda v,_: f"${v:.0f}k")); ax.tick_params(axis="x",labelsize=8.5)
ax.spines[["top","right","left"]].set_visible(False); ax.set_title("What each option costs — internal hours, supplier payments and material premium (excludes ~$15k already spent)",fontsize=10.5,color=NAV,loc="left",fontweight="bold")
plt.tight_layout(); plt.savefig("chart_options_year1.png",dpi=180); plt.close()
print("charts saved")
