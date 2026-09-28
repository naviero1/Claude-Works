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
sub_lb=52*DRUM; A6_total=(LB1-sub_lb)*SNP+sub_lb*PCI_SUB; A6_prem=A6_total-LB1*SNP
cjb_total=(LB1-sub_lb)*SNP+sub_lb*CJB; cjb_prem=cjb_total-LB1*SNP
five_prem=sum(vol(y)/3*(PCI_Q-SNP) for y in range(1,6))
batch_lb=BATCH*DRUM; days_full=batch_lb/(LBWK/7); cycle_wk=batch_lb/(LBWK/3); snp_on_wk=cycle_wk-batch_lb/LBWK
days_two_thirds=batch_lb/(LBWK*2/3/7)
print(f"A@3.50: total ${A35_total:,.0f} premium ${A35_prem:,.0f} ({A35_prem/(LB1*SNP):.0%}); 5yr ${five_prem:,.0f}; BE 5% ${A35_prem/.05:,.0f} 10% ${A35_prem/.10:,.0f}")
print(f"A@6 (1 drum/wk): total ${A6_total:,.0f} premium ${A6_prem:,.0f} ({A6_prem/(LB1*SNP):.0%})")
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

# ---- Supplier Quotes ----
ws=wb.create_sheet("Supplier Quotes",1)
title(ws,"All price points on the table — real quotes vs references","One place for every $/lb figure used anywhere in the analysis, with its basis. Real quotes in green; references in grey; superseded assumptions in amber.")
hdr(ws,5,["Source","$/lb finished","Basis / terms","Type","Status","Date / reference"])
rows=[("SNP Inc. (Durham, NC) — incumbent",0.75,"Delivered, all-in. 1/450-lb drum. ~2.9 drums/week today.","REAL QUOTE","Active sole source","SNP Estimate 012726-1"),
      ("PCI Manufacturing (St. Louis, MO) — one 5-drum batch",3.50,"One batch = 5 drums (2,250 lb). Confirm delivered/all-in and validity.","REAL QUOTE","Capable — experiment successful; not yet contracted","2026-09-28"),
      ("PCI Manufacturing — below one batch",6.00,"Any order smaller than 5 drums (e.g. 1 drum/week).","REAL QUOTE","Uneconomic version","2026-09-28"),
      ("CJB Applied Technologies (Valdosta, GA)",8.42,"$8.00–8.50/lb toll EXCLUDING materials + ~$75/drum resin = ~$8.42 landed. Qual fee $4,900.","REAL QUOTE","Eliminated on price (~11x SNP)","CJB email 'RE: mix test'"),
      ("Market — COMPETITIVE quantity (drum scale, 30–55 gal)",tier("competitive"),f"Inferred from comparable pre-mixed PVA solutions sold today; range {TIERS.get('competitive_range','—')}; n={TIERS.get('n_competitive','—')}","MARKET STUDY","Reference — see Market Study tab","Verified market study 2026-09-28"),
      ("Market — LOW quantity (pints to 5-gal pails)",tier("low"),f"Retail/lab packs; range {TIERS.get('low_range','—')}; n={TIERS.get('n_low','—')}","MARKET STUDY","Reference — see Market Study tab","Verified market study 2026-09-28"),
      ("Market — HIGH quantity (totes / bulk / tonnage)",tier("high"),f"Bulk and contract pricing; range {TIERS.get('high_range','—')}; n={TIERS.get('n_high','—')}. Quality/regulatory context differs.","MARKET STUDY","Reference — see Market Study tab","Verified market study 2026-09-28"),
      ("— Superseded / historical references (kept for the record) —",None,"","","",""),
      ("Triangulated market LOW / BASE / HIGH (Sept)",1.40,"$0.85 / $1.40 / $2.55 — resin floor + labor build-up + retail ceiling","TRIANGULATED","SUPERSEDED by market study","Market Research tab (cost-scenarios workbook)"),
      ("Material floor",0.18,"PVA resin $1.26–1.60/lb x 11% solids = $0.16–0.20","DERIVED","Reference only","ChemAnalyst / IMARC 2026"),
      ("July 2026 assumption (KPI deck)",1.125,"'$1.00–1.25/lb, ~35% share, ~$6–12k/yr insurance'","ASSUMPTION","SUPERSEDED by PCI quote","KPI review deck 2026-07-09"),
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
sc=[("All-SNP (today)","0","SNPlb"),("A — PCI at 1/3, 5-drum batches (10/yr)","50","PCIq"),("A — PCI 1 drum/week, below-batch price","52","PCIsub"),("A — PCI at 1/3 but below-batch price (for reference)","50","PCIsub"),("CJB at 1/3 (for scale)","50","CJBlb")]
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
r=12; ws.cell(row=r,column=2,value="Five years at 1/3 share, PCI $3.50, volume +10%/yr").font=F(True,11,NAVY); r+=1
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
                       ("Days of FULL demand in one batch","=B{r0}/(LbWk/7)",'0.0',"Must be consumed within the 18-day shelf life -> use at full rate on receipt"),
                       ("Cycle length at 1/3 share (weeks)","=B{r0}/(LbWk/3)",'0.0',"One PCI batch every ~5 weeks"),
                       ("Weeks on SNP material per cycle","=B{r2}-B{r0}/LbWk",'0.0',"SNP sees a ~12-day gap every cycle: LUMPY demand"),
                       ("Days to consume a batch at 2/3 rate (needs 30-day shelf life)","=B{r0}/(LbWk*2/3/7)",'0.0',"With a validated 30-day life, SNP can keep supplying at 1/3 rate during a PCI batch -> smoother"),
                       ("One qualification batch — cost","=B{r0}*PCIq",CUR,"A single production-scale batch (Option B-plus)"),
                       ("One qualification batch — premium over SNP","=B{r0}*(PCIq-SNPlb)",CUR,"~4% of annual volume; invisible to SNP's year")]:
    r0=r if lab.startswith("Batch size") else r0
    ws.cell(row=r,column=2,value=lab).font=F(True)
    c=ws.cell(row=r,column=3,value=f.format(r0=r0,r2=r0+2)); c.number_format=fmt; c.border=BORD
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
cols=[LGT,STL,LGT,GRN,NAV,REDc,REDc]
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

# Chart B: annual cost side by side (stacked SNP + second source), premium labelled
scen=[("All-SNP\n(today)",LB1*SNP,0),("A: PCI $3.50\n1/3, 5-drum batches",snp_lb*SNP,pci_lb*PCI_Q),("A: PCI $6.00\n1 drum/week",(LB1-sub_lb)*SNP,sub_lb*PCI_SUB),("CJB $8.42\n(for scale)",(LB1-sub_lb)*SNP,sub_lb*CJB)]
fig,ax=plt.subplots(figsize=(11,5.2)); x=range(len(scen))
b1=ax.bar(x,[s[1] for s in scen],color=GRN,label="SNP Inc. spend"); b2=ax.bar(x,[s[2] for s in scen],bottom=[s[1] for s in scen],color=NAV,label="Second-source spend")
for i,s in enumerate(scen):
    tot=s[1]+s[2]; prem=tot-LB1*SNP
    ax.text(i,tot*1.02,f"${tot/1000:,.0f}k"+(f"\n(+${prem/1000:,.0f}k, {prem/(LB1*SNP):.0%})" if prem>0 else ""),ha="center",va="bottom",fontsize=9.5,fontweight="bold")
ax.set_xticks(list(x)); ax.set_xticklabels([s[0] for s in scen]); ax.yaxis.set_major_formatter(money); ax.set_ylabel("Annual PVA spend, Year 1")
ax.set_title("Annual cost side by side — what each option adds to today's $50.7k",fontsize=12.5,color=NAV,loc="left",fontweight="bold")
ax.legend(frameon=False,loc="upper left"); ax.spines[["top","right"]].set_visible(False); ax.set_ylim(0,max(s[1]+s[2] for s in scen)*1.22); plt.tight_layout(); plt.savefig("chart_annual_side_by_side.png",dpi=180); plt.close()
print("charts saved")
