#!/usr/bin/env python3
"""Leadership model: cost of a second PVA supplier — options A/B/C, PCI $2.50-$5.00/lb range."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# ---------------- inputs ----------------
DRUM=450; SNP=0.75; LBWK=1300; WEEKS=52; GROWTH=0.10; SHARE=1/3; WARM=0.05
PCI_LO, PCI_MID, PCI_HI = 2.50, 3.75, 5.00
MKT_LO, MKT_BASE, MKT_HI = 0.85, 1.40, 2.55
CJB_LANDED = 8.42
QUAL_ONE_TIME = 15000   # placeholder: engineering time + samples + testing + SQA (user to confirm)
LB_Y1 = LBWK*WEEKS
def vol(y): return LB_Y1*(1+GROWTH)**(y-1)
def prem(price, share, y=1): return vol(y)*share*(price-SNP)

# ---------------- workbook ----------------
wb=openpyxl.Workbook()
NAVY="1F3864"; STEEL="4E79A7"; GREY="595959"
HDR=PatternFill("solid",fgColor=NAVY); SUB=PatternFill("solid",fgColor="D6DCE5")
INP=PatternFill("solid",fgColor="FFF2CC"); OUT=PatternFill("solid",fgColor="F2F2F2")
GOOD=PatternFill("solid",fgColor="C6EFCE"); BAD=PatternFill("solid",fgColor="FFC7CE"); AMB=PatternFill("solid",fgColor="FFEB9C")
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
def name(wb,n,ref): wb.defined_names[n]=DefinedName(n,attr_text=ref)

# ---- Inputs ----
ws=wb.active; ws.title="Inputs"
title(ws,"Second-Supplier Decision — Inputs","Yellow = editable. Everything else recalculates. Define acronyms: PVA = polyvinyl alcohol; SNP = incumbent supplier; PCI = candidate second source.")
rows=[("Drum net weight (lb)",DRUM,NUM,"Confirmed (SNP: 1/450-lb drum)","DrumLb"),
      ("SNP price ($/lb delivered, all-in)",SNP,CUR2,"Real quote — SNP Est 012726-1","SNPlb"),
      ("Demand today (lb/week)",LBWK,NUM,"Confirmed 2026-06-26","LbWk"),
      ("Weeks / year",WEEKS,NUM,"","Weeks"),
      ("Volume growth per year",GROWTH,PCT,"Leadership assumption","Growth"),
      ("Share of volume to 2nd source (Option A)",SHARE,'0.0%',"One-third of business","Share"),
      ("Share for a 'warm' backup (Option C)",WARM,PCT,"~1 drum every 7 weeks","WarmShare"),
      ("PCI price — LOW ($/lb)",PCI_LO,CUR2,"Forecast floor","PCIlo"),
      ("PCI price — MID ($/lb)",PCI_MID,CUR2,"Midpoint of range","PCImid"),
      ("PCI price — HIGH ($/lb)",PCI_HI,CUR2,"Forecast ceiling","PCIhi"),
      ("Market reference — LOW ($/lb)",MKT_LO,CUR2,"Triangulated (resin floor + labor bottom-up)","MktLo"),
      ("Market reference — BASE ($/lb)",MKT_BASE,CUR2,"Triangulated","MktBase"),
      ("Market reference — HIGH ($/lb)",MKT_HI,CUR2,"Triangulated (retail ceiling)","MktHi"),
      ("CJB quote, landed ($/lb) — reference only",CJB_LANDED,CUR2,"$8-8.50 toll excl. materials + $75/drum resin; ~11x SNP","CJBlb"),
      ("One-time qualification cost ($)",QUAL_ONE_TIME,CUR,"PLACEHOLDER — engineering hrs, samples, hydrogel tests, SQA, audit. Confirm.","QualCost"),
      ("Disruption probability per year (for break-even)",0.05,PCT,"PLACEHOLDER — leadership judgement","Pdis"),
      ("Cost of a 6-month SNP outage ($)",500000,CUR,"PLACEHOLDER — revenue at risk + expedite + line-down. NEEDED FROM FINANCE/OPS.","Dcost")]
hdr(ws,5,["Input","Value","Source / note"])
for i,(lab,val,fmt,note,nm) in enumerate(rows):
    r=6+i; ws.cell(row=r,column=2,value=lab).font=F(); c=ws.cell(row=r,column=3,value=val); c.number_format=fmt; c.fill=INP; c.font=F(True); c.border=BORD
    ws.cell(row=r,column=4,value=note).font=F(False,9,GREY,True); name(wb,nm,f"Inputs!$C${r}")
ws.column_dimensions['B'].width=46; ws.column_dimensions['C'].width=14; ws.column_dimensions['D'].width=70

# ---- 5-Year ----
ws=wb.create_sheet("5-Year")
title(ws,"Five-year cost of Option A (dual-source at the chosen share)","Premium = share x (PCI price - SNP price) x annual lb. It scales 1:1 with volume, so growth compounds it.")
hdr(ws,5,["Year","Volume (lb)","Drums","All-SNP baseline","Option A @ PCI LOW","Option A @ PCI MID","Option A @ PCI HIGH","Premium LOW","Premium MID","Premium HIGH"])
for y in range(1,6):
    r=5+y; ws.cell(row=r,column=2,value=y).font=F(True)
    ws.cell(row=r,column=3,value=f"=LbWk*Weeks*(1+Growth)^({y}-1)").number_format=NUM
    ws.cell(row=r,column=4,value=f"=C{r}/DrumLb").number_format=NUM
    ws.cell(row=r,column=5,value=f"=C{r}*SNPlb").number_format=CUR
    for j,p in enumerate(["PCIlo","PCImid","PCIhi"]):
        ws.cell(row=r,column=6+j,value=f"=C{r}*(1-Share)*SNPlb+C{r}*Share*{p}").number_format=CUR
        ws.cell(row=r,column=9+j,value=f"={get_column_letter(6+j)}{r}-E{r}").number_format=CUR
        ws.cell(row=r,column=9+j).fill=OUT
    for c in range(2,12): ws.cell(row=r,column=c).border=BORD
r=11; ws.cell(row=r,column=2,value="5-yr total").font=F(True)
for c in range(3,12):
    col=get_column_letter(c); ws.cell(row=r,column=c,value=f"=SUM({col}6:{col}10)").number_format=(NUM if c<=4 else CUR); ws.cell(row=r,column=c).font=F(True); ws.cell(row=r,column=c).fill=SUB; ws.cell(row=r,column=c).border=BORD
ws.cell(row=13,column=2,value="Plus one-time qualification cost (Inputs) — applies to any second source, warm or active:").font=F(False,9,GREY,True)
ws.cell(row=13,column=5,value="=QualCost").number_format=CUR
for c,w in zip("BCDEFGHIJK",[10,13,9,16,18,18,18,14,14,14]): ws.column_dimensions[c].width=w

# ---- Sensitivity ----
ws=wb.create_sheet("Sensitivity")
title(ws,"What drives the premium: 2nd-source price and share (Year 1)","Premium is linear in both. The share is the lever we control; the price is what the market gives us.")
hdr(ws,5,["2nd-source $/lb","Basis","Premium @ 1/3 share","x baseline","Premium @ 5% (warm)"])
sens=[("=MktLo","Market LOW"),("=MktBase","Market BASE"),(1.00,"Told to leadership (low)"),(1.25,"Told to leadership (high)"),("=MktHi","Market HIGH"),("=PCIlo","PCI LOW"),(3.00,"PCI original assumption"),("=PCImid","PCI MID"),("=PCIhi","PCI HIGH"),("=CJBlb","CJB quote (landed)")]
for i,(p,lab) in enumerate(sens):
    r=6+i; c=ws.cell(row=r,column=2,value=p); c.number_format=CUR2; c.border=BORD
    ws.cell(row=r,column=3,value=lab).font=F(False,9,GREY)
    ws.cell(row=r,column=4,value=f"=LbWk*Weeks*Share*(B{r}-SNPlb)").number_format=CUR
    ws.cell(row=r,column=5,value=f"=D{r}/(LbWk*Weeks*SNPlb)").number_format='0.0"x"'
    ws.cell(row=r,column=6,value=f"=LbWk*Weeks*WarmShare*(B{r}-SNPlb)").number_format=CUR
    for c in range(2,7): ws.cell(row=r,column=c).border=BORD
r=18; hdr(ws,r,["Share to 2nd source","Drums/yr","Premium @ PCI LOW","Premium @ PCI MID","Premium @ PCI HIGH"])
for i,s in enumerate([0.05,0.10,0.20,1/3,0.50]):
    rr=r+1+i; c=ws.cell(row=rr,column=2,value=s); c.number_format='0%'; c.border=BORD
    ws.cell(row=rr,column=3,value=f"=LbWk*Weeks*B{rr}/DrumLb").number_format=NUM
    for j,p in enumerate(["PCIlo","PCImid","PCIhi"]):
        ws.cell(row=rr,column=4+j,value=f"=LbWk*Weeks*B{rr}*({p}-SNPlb)").number_format=CUR
    for c in range(2,7): ws.cell(row=rr,column=c).border=BORD
for c,w in zip("BCDEF",[20,26,20,20,20]): ws.column_dimensions[c].width=w

# ---- SNP re-price ----
ws=wb.create_sheet("SNP Re-price")
title(ws,"If SNP raises price on the volume it keeps (Year 1, PCI MID)","Losing a third of our volume may cost SNP its batch efficiency. A surcharge on the retained two-thirds compounds the premium.")
hdr(ws,5,["SNP surcharge","SNP $/lb","SNP annual (2/3)","PCI annual (1/3)","Total","Premium vs today"])
for i,up in enumerate([0,0.05,0.10,0.20,0.33]):
    r=6+i; c=ws.cell(row=r,column=2,value=up); c.number_format=PCT; c.border=BORD
    ws.cell(row=r,column=3,value=f"=SNPlb*(1+B{r})").number_format=CUR2
    ws.cell(row=r,column=4,value=f"=LbWk*Weeks*(1-Share)*C{r}").number_format=CUR
    ws.cell(row=r,column=5,value=f"=LbWk*Weeks*Share*PCImid").number_format=CUR
    ws.cell(row=r,column=6,value=f"=D{r}+E{r}").number_format=CUR
    ws.cell(row=r,column=7,value=f"=F{r}-LbWk*Weeks*SNPlb").number_format=CUR
    for c in range(2,8): ws.cell(row=r,column=c).border=BORD
for c,w in zip("BCDEFG",[16,12,18,18,14,18]): ws.column_dimensions[c].width=w

# ---- Break-even ----
ws=wb.create_sheet("Break-even")
title(ws,"Is the insurance worth it? Premium vs (probability x avoided loss)","A second source is justified only if: annual premium <= P(SNP disruption in a year) x loss the second source would AVOID. Note: at 1/3 share, 2/3 of volume is still exposed unless the second source can ramp.")
hdr(ws,5,["Option","Annual premium","p = 2%","p = 5%","p = 10%","p = 20%"])
opts=[("A — dual @ PCI LOW","=LbWk*Weeks*Share*(PCIlo-SNPlb)"),("A — dual @ PCI MID","=LbWk*Weeks*Share*(PCImid-SNPlb)"),("A — dual @ PCI HIGH","=LbWk*Weeks*Share*(PCIhi-SNPlb)"),("C — warm 5% @ PCI MID","=LbWk*Weeks*WarmShare*(PCImid-SNPlb)")]
for i,(lab,f) in enumerate(opts):
    r=6+i; ws.cell(row=r,column=2,value=lab).font=F(True); ws.cell(row=r,column=3,value=f).number_format=CUR
    for j,p in enumerate([0.02,0.05,0.10,0.20]):
        ws.cell(row=r,column=4+j,value=f"=C{r}/{p}").number_format=CUR
    for c in range(2,8): ws.cell(row=r,column=c).border=BORD
ws.cell(row=11,column=2,value="Read: each cell = the avoided loss a disruption would have to cause for the premium to pay off. Compare to Inputs 'Cost of a 6-month SNP outage'.").font=F(False,9,GREY,True)
ws.cell(row=13,column=2,value="Expected annual loss with NO second source = Pdis x Dcost:").font=F(True)
ws.cell(row=13,column=4,value="=Pdis*Dcost").number_format=CUR
ws.cell(row=14,column=2,value="Verdict @ PCI MID, 1/3 share:").font=F(True)
ws.cell(row=14,column=4,value='=IF(D13>=C7,"Premium is justified","Premium exceeds expected loss")')
for c,w in zip("BCDEFG",[26,16,16,16,16,16]): ws.column_dimensions[c].width=w

# ---- Options summary ----
ws=wb.create_sheet("Options")
title(ws,"The three options, side by side (Year 1, PCI MID unless noted)")
hdr(ws,5,["","A — Dual-source now (1/3)","B — Single + strengthen SNP","C — Warm backup (5%)"])
lines=[("Annual purchase cost","=LbWk*Weeks*(1-Share)*SNPlb+LbWk*Weeks*Share*PCImid","=LbWk*Weeks*SNPlb","=LbWk*Weeks*(1-WarmShare)*SNPlb+LbWk*Weeks*WarmShare*PCImid"),
       ("Premium vs today","=B6-LbWk*Weeks*SNPlb","0","=D6-LbWk*Weeks*SNPlb"),
       ("One-time qualification","=QualCost","0 (plan/document only)","=QualCost"),
       ("5-yr premium (10% growth)","=B7*(1+(1+Growth)+(1+Growth)^2+(1+Growth)^3+(1+Growth)^4)","0","=D7*(1+(1+Growth)+(1+Growth)^2+(1+Growth)^3+(1+Growth)^4)"),
       ("Volume still exposed if SNP fails","2/3 (until PCI ramps)","100%","95% (until PCI ramps)"),
       ("Time to recover if SNP fails","weeks (PCI ramp)","6-12 months (cold start)","weeks-months (re-activate)"),
       ("Signal to SNP","Lost a third of volume","Deeper partnership","Minor"),
       ("Compliance posture","Strong","Defensible if documented","Strong")]
for i,(lab,a,b,c_) in enumerate(lines):
    r=6+i; ws.cell(row=r,column=2,value=lab).font=F(True)
    for j,v in enumerate([a,b,c_]):
        cell=ws.cell(row=r,column=3+j,value=v)
        if isinstance(v,str) and v.startswith("="): cell.number_format=CUR
        cell.border=BORD; cell.alignment=Alignment(wrap_text=True,vertical="top")
for c,w in zip("BCDE",[30,28,28,28]): ws.column_dimensions[c].width=w

wb.save("PVA_Second_Supplier_Leadership_Model.xlsx"); print("saved model")

# ---------------- charts ----------------
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10})
NAV="#1F3864"; STL="#4E79A7"; AMBc="#C9A227"; REDc="#B23A2E"; GRN="#2E7D46"; LGT="#D6DCE5"
money=FuncFormatter(lambda v,_: (f"${v/1e6:,.1f}M" if v>=1e6 else f"${v/1000:,.0f}k"))

# Chart 1: premium vs price
labels=["Market\nLOW\n$0.85","Market\nBASE\n$1.40","Told to\nleadership\n$1.00-1.25","Market\nHIGH\n$2.55","PCI\nLOW\n$2.50","PCI\nMID\n$3.75","PCI\nHIGH\n$5.00","CJB\nquote\n$8.42"]
vals=[prem(MKT_LO,SHARE),prem(MKT_BASE,SHARE),prem(1.125,SHARE),prem(MKT_HI,SHARE),prem(PCI_LO,SHARE),prem(PCI_MID,SHARE),prem(PCI_HI,SHARE),prem(CJB_LANDED,SHARE)]
cols=[LGT,LGT,GRN,LGT,STL,NAV,NAV,REDc]
fig,ax=plt.subplots(figsize=(11,5.2)); bars=ax.bar(labels,vals,color=cols,edgecolor="white")
ax.axhline(LB_Y1*SNP,color=GRN,ls="--",lw=1.2); ax.text(-0.4,LB_Y1*SNP*1.04,"= today's entire PVA spend ($50.7k)",ha="left",va="bottom",fontsize=9,color=GRN)
for b,v in zip(bars,vals): ax.text(b.get_x()+b.get_width()/2,v*1.02,f"${v/1000:,.0f}k",ha="center",va="bottom",fontsize=9,fontweight="bold")
ax.yaxis.set_major_formatter(money); ax.set_ylabel("Annual premium over all-SNP (Year 1, 1/3 share)"); ax.set_title("What a second source adds per year, by its price per pound",fontsize=13,color=NAV,loc="left",fontweight="bold")
ax.spines[["top","right"]].set_visible(False); ax.set_ylim(0,max(vals)*1.12); plt.tight_layout(); plt.savefig("chart_premium_by_price.png",dpi=180); plt.close()

# Chart 2: 5-yr cumulative
yrs=[1,2,3,4,5]
def cum(price,share): 
    out=[];s=0
    for y in yrs: s+=prem(price,share,y); out.append(s)
    return out
fig,ax=plt.subplots(figsize=(11,5.2))
for price,lab,col,ls in [(PCI_HI,"A: dual @ $5.00 (high)",REDc,"-"),(PCI_MID,"A: dual @ $3.75 (mid)",NAV,"-"),(PCI_LO,"A: dual @ $2.50 (low)",STL,"-"),(PCI_MID,"C: warm 5% @ $3.75",GRN,"--")]:
    sh=WARM if lab.startswith("C") else SHARE
    ys=cum(price,sh); ax.plot(yrs,ys,marker="o",color=col,ls=ls,lw=2.2,label=lab); ax.text(5.08,ys[-1],f"${ys[-1]/1000:,.0f}k",va="center",fontsize=9,color=col,fontweight="bold")
ax.set_xticks(yrs); ax.set_xlabel("Year (volume +10%/yr)"); ax.yaxis.set_major_formatter(money); ax.set_ylabel("Cumulative premium paid")
ax.set_title("Cumulative cost of carrying a second source over five years",fontsize=13,color=NAV,loc="left",fontweight="bold")
ax.legend(frameon=False,loc="upper left"); ax.spines[["top","right"]].set_visible(False); ax.set_xlim(0.8,5.6); plt.tight_layout(); plt.savefig("chart_five_year.png",dpi=180); plt.close()

# Chart 3: break-even
ps=[0.02,0.05,0.10,0.20,0.30]
fig,ax=plt.subplots(figsize=(11,5.2))
for price,lab,col in [(PCI_HI,"A @ $5.00",REDc),(PCI_MID,"A @ $3.75",NAV),(PCI_LO,"A @ $2.50",STL)]:
    ax.plot([p*100 for p in ps],[prem(price,SHARE)/p for p in ps],marker="o",color=col,lw=2.2,label=f"Option {lab}")
ax.plot([p*100 for p in ps],[prem(PCI_MID,WARM)/p for p in ps],marker="o",color=GRN,ls="--",lw=2.2,label="Option C warm 5% @ $3.75")
ax.set_yscale("log"); ax.yaxis.set_major_formatter(money); ax.set_xlabel("Probability SNP is disrupted in a given year (%)"); ax.set_ylabel("Avoided loss needed to justify the premium (log)")
ax.set_title("Break-even: how big must the avoided outage be for the insurance to pay?",fontsize=13,color=NAV,loc="left",fontweight="bold")
ax.legend(frameon=False); ax.grid(axis="y",alpha=.25); ax.spines[["top","right"]].set_visible(False); plt.tight_layout(); plt.savefig("chart_breakeven.png",dpi=180); plt.close()
print("charts saved")

# print key numbers for the deck
print("\nKEY NUMBERS")
for p,l in [(PCI_LO,"LOW"),(PCI_MID,"MID"),(PCI_HI,"HIGH")]:
    print(f"  PCI {l} ${p:.2f}: Y1 premium ${prem(p,SHARE):,.0f} | 5-yr ${cum(p,SHARE)[-1]:,.0f} | warm5% Y1 ${prem(p,WARM):,.0f}")
