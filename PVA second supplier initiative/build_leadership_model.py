#!/usr/bin/env python3
"""Leadership model: cost of a second PVA supplier. Binary decision — the second source gets max(1/3 of demand, 1 drum/week) or nothing."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# ---------------- inputs ----------------
DRUM=450; SNP=0.75; LBWK=1300; WEEKS=52; GROWTH=0.10; SHARE=1/3
MIN_DRUMS_WK=1                      # smallest volume a second source will accept
PCI_LO, PCI_MID, PCI_HI = 2.50, 3.75, 5.00
MKT_LO, MKT_BASE, MKT_HI = 0.85, 1.40, 2.55
CJB_LANDED = 8.42
QUAL_ONE_TIME = 15000               # placeholder (user to confirm)
LB_Y1 = LBWK*WEEKS
def vol(y): return LB_Y1*(1+GROWTH)**(y-1)
def eff(y): return max(SHARE, MIN_DRUMS_WK*WEEKS*DRUM/vol(y))   # effective share: never below the supplier minimum
def prem(price, y=1): return vol(y)*eff(y)*(price-SNP)

# ---------------- workbook ----------------
wb=openpyxl.Workbook()
NAVY="1F3864"; GREY="595959"
HDR=PatternFill("solid",fgColor=NAVY); SUB=PatternFill("solid",fgColor="D6DCE5")
INP=PatternFill("solid",fgColor="FFF2CC"); OUT=PatternFill("solid",fgColor="F2F2F2"); BAD=PatternFill("solid",fgColor="FFC7CE")
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
EFF="MAX(Share,MinShare)"   # Year-1 effective share, as a formula fragment

# ---- Inputs ----
ws=wb.active; ws.title="Inputs"
title(ws,"Second-Supplier Decision — Inputs","Yellow = editable. PVA = polyvinyl alcohol. SNP Inc. = incumbent. PCI Manufacturing = candidate second source. The second source gets the LARGER of 1/3 of demand and its 1-drum/week minimum — or nothing.")
rows=[("Drum net weight (lb)",DRUM,NUM,"Confirmed (SNP Inc.: 1/450-lb drum)","DrumLb"),
      ("SNP Inc. price ($/lb delivered, all-in)",SNP,CUR2,"Real quote — SNP Estimate 012726-1","SNPlb"),
      ("Demand today (lb/week)",LBWK,NUM,"Confirmed 2026-06-26","LbWk"),
      ("Weeks / year",WEEKS,NUM,"","Weeks"),
      ("Volume growth per year",GROWTH,PCT,"Leadership assumption","Growth"),
      ("Smallest volume a second source will accept (drums/week)",MIN_DRUMS_WK,NUM,"Supplier condition — below this they will not engage","MinDrumsWk"),
      ("  = share of today's demand","=MinDrumsWk*DrumLb/LbWk",'0.0%',"~35%. This is the smallest insurance available.","MinShare"),
      ("Target share of demand (Option A)",SHARE,'0.0%',"One-third. Year 1: 1/3 = 0.96 drums/wk, so the minimum (1.0) governs; from Year 2 the 1/3 governs.","Share"),
      ("  = effective share, Year 1",f"={EFF}",'0.0%',"max(target, minimum)","EffShare"),
      ("PCI price — LOW ($/lb)",PCI_LO,CUR2,"Forecast floor","PCIlo"),
      ("PCI price — MID ($/lb)",PCI_MID,CUR2,"Midpoint of range","PCImid"),
      ("PCI price — HIGH ($/lb)",PCI_HI,CUR2,"Forecast ceiling","PCIhi"),
      ("Market reference — LOW ($/lb)",MKT_LO,CUR2,"Triangulated (resin floor + labor bottom-up)","MktLo"),
      ("Market reference — BASE ($/lb)",MKT_BASE,CUR2,"Triangulated","MktBase"),
      ("Market reference — HIGH ($/lb)",MKT_HI,CUR2,"Triangulated (retail ceiling)","MktHi"),
      ("CJB Applied Technologies quote, landed ($/lb) — reference",CJB_LANDED,CUR2,"$8-8.50 toll excl. materials + $75/drum resin; ~11x SNP","CJBlb"),
      ("One-time qualification cost ($)",QUAL_ONE_TIME,CUR,"PLACEHOLDER — engineering hrs, samples, hydrogel tests, quality agreement. Confirm.","QualCost"),
      ("Disruption probability per year (for break-even)",0.05,PCT,"PLACEHOLDER — leadership judgement","Pdis"),
      ("Cost of a 6-month SNP Inc. outage ($)",500000,CUR,"PLACEHOLDER — revenue at risk + expedite + line-down. NEEDED FROM FINANCE/OPS.","Dcost")]
hdr(ws,5,["Input","Value","Source / note"])
for i,(lab,val,fmt,note,nm) in enumerate(rows):
    r=6+i; ws.cell(row=r,column=2,value=lab).font=F(); c=ws.cell(row=r,column=3,value=val); c.number_format=fmt
    c.fill=(OUT if isinstance(val,str) and val.startswith("=") else INP); c.font=F(True); c.border=BORD
    ws.cell(row=r,column=4,value=note).font=F(False,9,GREY,True); name(wb,nm,f"Inputs!$C${r}")
ws.column_dimensions['B'].width=52; ws.column_dimensions['C'].width=14; ws.column_dimensions['D'].width=78

# ---- 5-Year ----
ws=wb.create_sheet("5-Year")
title(ws,"Five-year cost of Option A","Each year the second source gets max(1/3 of demand, 1 drum/week). Premium = share x (PCI price - SNP price) x annual lb; it grows with volume.")
hdr(ws,5,["Year","Volume (lb)","Drums","Effective share","Drums/wk to PCI","All-SNP baseline","Option A @ PCI LOW","Option A @ PCI MID","Option A @ PCI HIGH","Premium LOW","Premium MID","Premium HIGH"])
for y in range(1,6):
    r=5+y; ws.cell(row=r,column=2,value=y).font=F(True)
    ws.cell(row=r,column=3,value=f"=LbWk*Weeks*(1+Growth)^({y}-1)").number_format=NUM
    ws.cell(row=r,column=4,value=f"=C{r}/DrumLb").number_format=NUM
    ws.cell(row=r,column=5,value=f"=MAX(Share,MinDrumsWk*Weeks*DrumLb/C{r})").number_format='0.0%'
    ws.cell(row=r,column=6,value=f"=D{r}*E{r}/Weeks").number_format='0.00'
    ws.cell(row=r,column=7,value=f"=C{r}*SNPlb").number_format=CUR
    for j,p in enumerate(["PCIlo","PCImid","PCIhi"]):
        ws.cell(row=r,column=8+j,value=f"=C{r}*(1-E{r})*SNPlb+C{r}*E{r}*{p}").number_format=CUR
        ws.cell(row=r,column=11+j,value=f"={get_column_letter(8+j)}{r}-G{r}").number_format=CUR; ws.cell(row=r,column=11+j).fill=OUT
    for c in range(2,14): ws.cell(row=r,column=c).border=BORD
r=11; ws.cell(row=r,column=2,value="5-yr total").font=F(True)
for c in range(3,14):
    if c in (5,6): continue
    col=get_column_letter(c); cell=ws.cell(row=r,column=c,value=f"=SUM({col}6:{col}10)"); cell.number_format=(NUM if c<=4 else CUR); cell.font=F(True); cell.fill=SUB; cell.border=BORD
ws.cell(row=13,column=2,value="Plus one-time qualification cost (Inputs):").font=F(False,9,GREY,True); ws.cell(row=13,column=7,value="=QualCost").number_format=CUR
for c,w in zip("BCDEFGHIJKLM",[8,13,9,12,12,16,18,18,18,14,14,14]): ws.column_dimensions[c].width=w

# ---- Sensitivity ----
ws=wb.create_sheet("Sensitivity")
title(ws,"What drives the premium (Year 1, at the supplier minimum ≈ 1/3)","Price is what the market gives us. Share is NOT a free lever: anything below the supplier minimum is not available.")
hdr(ws,5,["2nd-source $/lb","Basis","Premium (Year 1)","x today's PVA spend"])
sens=[("=MktLo","Market LOW"),(1.00,"Upside case / assumed in July (low)"),(1.25,"Upside case / assumed in July (high)"),("=MktBase","Market BASE"),(1.50,"Upside case — trigger price"),(2.00,"Upside case — borderline"),("=MktHi","Market HIGH"),("=PCIlo","PCI LOW"),("=PCImid","PCI MID"),("=PCIhi","PCI HIGH"),("=CJBlb","CJB quote (landed)")]
for i,(p,lab) in enumerate(sens):
    r=6+i; c=ws.cell(row=r,column=2,value=p); c.number_format=CUR2; c.border=BORD
    ws.cell(row=r,column=3,value=lab).font=F(False,9,GREY)
    ws.cell(row=r,column=4,value=f"=LbWk*Weeks*EffShare*(B{r}-SNPlb)").number_format=CUR
    ws.cell(row=r,column=5,value=f"=D{r}/(LbWk*Weeks*SNPlb)").number_format='0.0"x"'
    for c in range(2,6): ws.cell(row=r,column=c).border=BORD
r=17; hdr(ws,r,["Share to 2nd source","Drums/week","Available?","Premium @ PCI MID"])
for i,sh in enumerate([0.05,0.10,0.20,1/3,0.50]):
    rr=r+1+i; c=ws.cell(row=rr,column=2,value=sh); c.number_format='0%'; c.border=BORD
    ws.cell(row=rr,column=3,value=f"=LbWk*B{rr}/DrumLb").number_format='0.00'
    a=ws.cell(row=rr,column=4,value=f'=IF(C{rr}>=MinDrumsWk,"Yes",IF(B{rr}>=0.3,"Rounds up to the 1-drum minimum","NO — below supplier minimum"))')
    ws.cell(row=rr,column=5,value=f'=IF(B{rr}>=0.3,LbWk*Weeks*MAX(B{rr},MinShare)*(PCImid-SNPlb),"n/a")').number_format=CUR
    if sh<0.3: a.fill=BAD; ws.cell(row=rr,column=5).fill=BAD
    for c in range(2,6): ws.cell(row=rr,column=c).border=BORD
ws.cell(row=24,column=2,value="This is why there is no 'low-cost insurance' version of Option A: the smallest second source anyone will sell us is one drum a week.").font=F(True,9,NAVY)
for c,w in zip("BCDE",[20,26,34,20]): ws.column_dimensions[c].width=w

# ---- SNP re-price ----
ws=wb.create_sheet("SNP Re-price")
title(ws,"If SNP Inc. raises price on the volume it keeps (Year 1, PCI MID)","Losing a third of our volume may cost SNP its batch efficiency. A surcharge on the retained ~2/3 compounds the premium.")
hdr(ws,5,["SNP surcharge","SNP $/lb","SNP annual (retained)","PCI annual","Total","Premium vs today"])
for i,up in enumerate([0,0.05,0.10,0.20,0.33]):
    r=6+i; c=ws.cell(row=r,column=2,value=up); c.number_format=PCT; c.border=BORD
    ws.cell(row=r,column=3,value=f"=SNPlb*(1+B{r})").number_format=CUR2
    ws.cell(row=r,column=4,value=f"=LbWk*Weeks*(1-EffShare)*C{r}").number_format=CUR
    ws.cell(row=r,column=5,value=f"=LbWk*Weeks*EffShare*PCImid").number_format=CUR
    ws.cell(row=r,column=6,value=f"=D{r}+E{r}").number_format=CUR
    ws.cell(row=r,column=7,value=f"=F{r}-LbWk*Weeks*SNPlb").number_format=CUR
    for c in range(2,8): ws.cell(row=r,column=c).border=BORD
for c,w in zip("BCDEFG",[16,12,20,18,14,18]): ws.column_dimensions[c].width=w

# ---- Break-even ----
ws=wb.create_sheet("Break-even")
title(ws,"Is the insurance worth it? Premium vs (probability x avoided loss)","Option A is justified only if: annual premium <= P(SNP disruption in a year) x loss the second source would AVOID. ~2/3 of volume is still exposed until PCI can ramp.")
hdr(ws,5,["Option A price case","Annual premium","p = 2%","p = 5%","p = 10%","p = 20%"])
opts=[("PCI LOW $2.50","=LbWk*Weeks*EffShare*(PCIlo-SNPlb)"),("PCI MID $3.75","=LbWk*Weeks*EffShare*(PCImid-SNPlb)"),("PCI HIGH $5.00","=LbWk*Weeks*EffShare*(PCIhi-SNPlb)")]
for i,(lab,f) in enumerate(opts):
    r=6+i; ws.cell(row=r,column=2,value=lab).font=F(True); ws.cell(row=r,column=3,value=f).number_format=CUR
    for j,p in enumerate([0.02,0.05,0.10,0.20]): ws.cell(row=r,column=4+j,value=f"=C{r}/{p}").number_format=CUR
    for c in range(2,8): ws.cell(row=r,column=c).border=BORD
ws.cell(row=10,column=2,value="Read: each cell = the avoided loss an SNP outage would have to cause for the premium to pay off. Compare to Inputs 'Cost of a 6-month SNP Inc. outage'.").font=F(False,9,GREY,True)
ws.cell(row=12,column=2,value="Expected annual loss with NO second source = Pdis x Dcost:").font=F(True); ws.cell(row=12,column=4,value="=Pdis*Dcost").number_format=CUR
ws.cell(row=13,column=2,value="Verdict @ PCI MID:").font=F(True); ws.cell(row=13,column=4,value='=IF(D12>=C7,"Option A is justified","Premium exceeds expected loss — Option B")')
for c,w in zip("BCDEFG",[24,16,16,16,16,16]): ws.column_dimensions[c].width=w

# ---- Options ----
ws=wb.create_sheet("Options")
title(ws,"The two options, side by side (Year 1, PCI MID unless noted)","There is no smaller version of A: the supplier minimum is one drum a week.")
hdr(ws,5,["","A — Second source (PCI Manufacturing) at ~1/3","B — Single source (SNP Inc.) + strengthen"])
lines=[("Annual purchase cost","=LbWk*Weeks*(1-EffShare)*SNPlb+LbWk*Weeks*EffShare*PCImid","=LbWk*Weeks*SNPlb"),
       ("Premium vs today","=B6-LbWk*Weeks*SNPlb","0 (+ small continuity spend)"),
       ("One-time qualification","=QualCost","0 (plan/document only)"),
       ("5-yr premium (10% growth)","='5-Year'!L11","0"),
       ("Volume still exposed if SNP fails","~2/3 (until PCI ramps — unconfirmed)","100%"),
       ("Time to recover if SNP fails","weeks (PCI ramp)","6-12 months cold start; 3-4 with kit current"),
       ("Signal to SNP Inc.","Lost a third of its volume","Deeper partnership"),
       ("Compliance posture","Strong","Defensible if risk + plan documented")]
for i,(lab,a,b) in enumerate(lines):
    r=6+i; ws.cell(row=r,column=2,value=lab).font=F(True)
    for j,v in enumerate([a,b]):
        cell=ws.cell(row=r,column=3+j,value=v)
        if isinstance(v,str) and v.startswith("="): cell.number_format=CUR
        cell.border=BORD; cell.alignment=Alignment(wrap_text=True,vertical="top")
for c,w in zip("BCD",[30,42,42]): ws.column_dimensions[c].width=w

wb.save("PVA_Second_Supplier_Leadership_Model.xlsx"); print("saved model")

# ---------------- charts ----------------
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10})
NAV="#1F3864"; STL="#4E79A7"; REDc="#B23A2E"; GRN="#2E7D46"; LGT="#D6DCE5"
money=FuncFormatter(lambda v,_: (f"${v/1e6:,.1f}M" if v>=1e6 else f"${v/1000:,.0f}k"))

labels=["Market\nLOW\n$0.85","Market\nBASE\n$1.40","Assumed\nin July\n$1.00-1.25","Market\nHIGH\n$2.55","PCI\nLOW\n$2.50","PCI\nMID\n$3.75","PCI\nHIGH\n$5.00","CJB\nquote\n$8.42"]
vals=[prem(MKT_LO),prem(MKT_BASE),prem(1.125),prem(MKT_HI),prem(PCI_LO),prem(PCI_MID),prem(PCI_HI),prem(CJB_LANDED)]
cols=[LGT,LGT,GRN,LGT,STL,NAV,NAV,REDc]
fig,ax=plt.subplots(figsize=(11,5.2)); bars=ax.bar(labels,vals,color=cols,edgecolor="white")
ax.axhline(LB_Y1*SNP,color=GRN,ls="--",lw=1.2); ax.text(-0.4,LB_Y1*SNP*1.04,"= today's entire PVA spend ($50.7k)",ha="left",va="bottom",fontsize=9,color=GRN)
for b,v in zip(bars,vals): ax.text(b.get_x()+b.get_width()/2,v*1.02,f"${v/1000:,.0f}k",ha="center",va="bottom",fontsize=9,fontweight="bold")
ax.yaxis.set_major_formatter(money); ax.set_ylabel("Annual premium over all-SNP (Year 1, one drum/week ≈ 1/3)")
ax.set_title("What a second source adds per year, by its price per pound — at the smallest volume a supplier will accept",fontsize=12,color=NAV,loc="left",fontweight="bold")
ax.spines[["top","right"]].set_visible(False); ax.set_ylim(0,max(vals)*1.12); plt.tight_layout(); plt.savefig("chart_premium_by_price.png",dpi=180); plt.close()

yrs=[1,2,3,4,5]
def cum(price):
    out=[];s=0
    for y in yrs: s+=prem(price,y); out.append(s)
    return out
fig,ax=plt.subplots(figsize=(11,5.2))
for price,lab,col in [(PCI_HI,"PCI @ $5.00 (high)",REDc),(PCI_MID,"PCI @ $3.75 (mid)",NAV),(PCI_LO,"PCI @ $2.50 (low)",STL)]:
    ys=cum(price); ax.plot(yrs,ys,marker="o",color=col,lw=2.2,label=lab); ax.text(5.08,ys[-1],f"${ys[-1]/1000:,.0f}k",va="center",fontsize=9,color=col,fontweight="bold")
ax.set_xticks(yrs); ax.set_xlabel("Year (volume +10%/yr)"); ax.yaxis.set_major_formatter(money); ax.set_ylabel("Cumulative premium paid")
ax.set_title("Cumulative cost of carrying a second source over five years",fontsize=13,color=NAV,loc="left",fontweight="bold")
ax.legend(frameon=False,loc="upper left"); ax.spines[["top","right"]].set_visible(False); ax.set_xlim(0.8,5.6); plt.tight_layout(); plt.savefig("chart_five_year.png",dpi=180); plt.close()

ps=[0.02,0.05,0.10,0.20,0.30]
fig,ax=plt.subplots(figsize=(11,5.2))
for price,lab,col in [(PCI_HI,"PCI @ $5.00",REDc),(PCI_MID,"PCI @ $3.75",NAV),(PCI_LO,"PCI @ $2.50",STL)]:
    ax.plot([p*100 for p in ps],[prem(price)/p for p in ps],marker="o",color=col,lw=2.2,label=f"Option A, {lab}")
ax.set_yscale("log"); ax.yaxis.set_major_formatter(money); ax.set_xlabel("Probability SNP Inc. is disrupted in a given year (%)"); ax.set_ylabel("Avoided loss needed to justify the premium (log)")
ax.set_title("Break-even: how costly must the avoided outage be for the second source to pay?",fontsize=13,color=NAV,loc="left",fontweight="bold")
ax.legend(frameon=False); ax.grid(axis="y",alpha=.25); ax.spines[["top","right"]].set_visible(False); plt.tight_layout(); plt.savefig("chart_breakeven.png",dpi=180); plt.close()
print("charts saved")

print("\nKEY NUMBERS  (Year-1 effective share = %.1f%% = %d drums)" % (eff(1)*100, round(vol(1)*eff(1)/DRUM)))
for p,l in [(PCI_LO,"LOW"),(PCI_MID,"MID"),(PCI_HI,"HIGH")]:
    print(f"  PCI {l} ${p:.2f}: Y1 premium ${prem(p):,.0f} ({prem(p)/(LB_Y1*SNP):.0%} of spend) | 5-yr ${cum(p)[-1]:,.0f} | break-even @5%: ${prem(p)/0.05:,.0f} @10%: ${prem(p)/0.10:,.0f}")
for y in range(1,6): print(f"  Y{y}: share {eff(y):.1%} = {vol(y)*eff(y)/DRUM/WEEKS:.2f} drums/wk to PCI")
print(f"  Trigger check: PCI at $1.50 -> premium ${prem(1.50):,.0f}/yr")
