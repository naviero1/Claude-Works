#!/usr/bin/env python3
"""Render clear, labeled PNG charts for the PVA cost scenarios and embed in xlsx."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.patches as mpatches

# ---------- numbers ----------
DRUM_LB=450; SNP_LB=0.75; TOLL_MID=8.25; MATERIALS=75; FREIGHT=0
QUAL=4900; CREDIT=700; CREDIT_N=7
DEMAND=1300; WEEKS=52
SNP_DRUM=DRUM_LB*SNP_LB                       # 337.50
CJB_LANDED=DRUM_LB*TOLL_MID+MATERIALS+FREIGHT # 3787.5
CJB_CREDITED=CJB_LANDED-CREDIT
DRUMS_YR=DEMAND*WEEKS/DRUM_LB                 # 150.2
MKT_LB=2.55; MKT_DRUM=MKT_LB*DRUM_LB          # 1147.5  (HIGH-end market rate per user request)
def acct(split, secprice, credit=0):
    return DRUMS_YR*(1-split)*SNP_DRUM + DRUMS_YR*split*secprice - credit
baseline=DRUMS_YR*SNP_DRUM

NAVY="#1F3864"; SNPc="#4E79A7"; MKTc="#59A14F"; CJBc="#C0392B"; CJBc1="#E8897E"; GREYc="#8C8C8C"
def money(x,_=None): return f"${x:,.0f}"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.edgecolor":"#CCCCCC"})

# ============ CHART 1 — the $700 credit over first 7 orders ============
fig,ax=plt.subplots(figsize=(11,5.6),dpi=150)
orders=list(range(1,11))
net=[CJB_CREDITED if i<=CREDIT_N else CJB_LANDED for i in orders]
colors=[MKTc if i<=CREDIT_N else CJBc for i in orders]
bars=ax.bar(orders,net,color=colors,zorder=3,width=0.62)
# ghost cap = the $700 credit removed on orders 1-7
for i in orders:
    if i<=CREDIT_N:
        ax.bar(i,CREDIT,bottom=CJB_CREDITED,color="none",edgecolor=CJBc,
               hatch="////",linewidth=1.1,zorder=2,width=0.62)
for b,i,v in zip(bars,orders,net):
    ax.text(b.get_x()+b.get_width()/2,v+40,money(v),ha="center",va="bottom",
            fontsize=9,fontweight="bold",color=NAVY)
ax.axhline(SNP_DRUM,color=SNPc,ls="--",lw=1.6,zorder=1)
ax.text(10.6,SNP_DRUM,f"SNP ${SNP_DRUM:,.0f}/order",ha="right",va="bottom",color=SNPc,fontsize=9,fontweight="bold")
ax.set_title("What the $700 credit does — CJB cost per order (one 55-gal drum)",
             fontsize=14,fontweight="bold",color=NAVY,pad=30,loc="left")
ax.text(0,1.045,"Orders 1–7 get \$700 off (green + hatch = the credit). That returns the \$4,900 qual fee, then stops — order 8 onward is full price.",
        transform=ax.transAxes,fontsize=10,color="#555555")
ax.set_xlabel("Order number (1 order = 1 batch = 1 drum)"); ax.set_ylabel("Cost per order")
ax.set_xticks(orders); ax.yaxis.set_major_formatter(FuncFormatter(money))
ax.set_ylim(0,CJB_LANDED*1.15); ax.set_xlim(0.4,10.9)
ax.grid(axis="y",color="#EEEEEE",zorder=0)
for s in ("top","right"): ax.spines[s].set_visible(False)
leg=[mpatches.Patch(color=MKTc,label="Orders 1–7: net after $700 credit"),
     mpatches.Patch(facecolor="none",edgecolor=CJBc,hatch="////",label="The $700 credit (per order)"),
     mpatches.Patch(color=CJBc,label="Order 8+: full price, no credit")]
ax.legend(handles=leg,loc="upper left",fontsize=9,framealpha=0.95)
fig.tight_layout(); fig.savefig("chart1_credit.png",bbox_inches="tight"); plt.close(fig)

# ============ CHART 2 — total annual cost, ALL options (horizontal) ============
rows=[("All-SNP baseline",baseline,GREYc),
      ("Market (high) @25%",acct(0.25,MKT_DRUM),MKTc),
      ("Market (high) @35% (~1 drum/wk)",acct(0.35,MKT_DRUM),MKTc),
      ("CJB @25% — Year 1 (credit)",acct(0.25,CJB_LANDED,QUAL),CJBc1),
      ("CJB @25% — Year 2+",acct(0.25,CJB_LANDED),CJBc),
      ("CJB @35% — Year 1 (credit)",acct(0.35,CJB_LANDED,QUAL),CJBc1),
      ("CJB @35% — Year 2+",acct(0.35,CJB_LANDED),CJBc)]
labels=[r[0] for r in rows]; vals=[r[1] for r in rows]; cols=[r[2] for r in rows]
fig,ax=plt.subplots(figsize=(11,5.8),dpi=150)
y=range(len(rows))
bars=ax.barh(list(y),vals,color=cols,zorder=3,height=0.66)
ax.invert_yaxis()
for b,v in zip(bars,vals):
    ax.text(v+2500,b.get_y()+b.get_height()/2,money(v),va="center",ha="left",
            fontsize=10,fontweight="bold",color=NAVY)
ax.axvline(baseline,color=GREYc,ls="--",lw=1.4,zorder=1)
ax.text(baseline,-0.7,f"baseline {money(baseline)}",color=GREYc,fontsize=9,ha="center")
ax.set_yticks(list(y)); ax.set_yticklabels(labels,fontsize=10)
ax.xaxis.set_major_formatter(FuncFormatter(money))
ax.set_xlim(0,max(vals)*1.18)
ax.set_title("Total annual account cost — all options",fontsize=14,fontweight="bold",color=NAVY,pad=28,loc="left")
ax.text(0,1.04,"Whole account (2nd-source slice + retained SNP). Market shown at the HIGH-end rate \$2.55/lb. CJB still runs ~2.5–3.5× even the high market; its \$4,900 credit is invisible here.",
        transform=ax.transAxes,fontsize=9.5,color="#555555")
ax.set_xlabel("$ per year")
ax.grid(axis="x",color="#EEEEEE",zorder=0)
for s in ("top","right"): ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig("chart2_all.png",bbox_inches="tight"); plt.close(fig)

# ============ CHART 3 — realistic options (SNP vs Market), with premium ============
r3=[("All-SNP\nbaseline",baseline,GREYc),
    ("Market\n@25%",acct(0.25,MKT_DRUM),MKTc),
    ("Market @35%\n(~1 drum/wk)",acct(0.35,MKT_DRUM),MKTc)]
labels=[r[0] for r in r3]; vals=[r[1] for r in r3]; cols=[r[2] for r in r3]
fig,ax=plt.subplots(figsize=(8.5,5.6),dpi=150)
x=range(len(r3))
bars=ax.bar(list(x),vals,color=cols,zorder=3,width=0.64)
for b,v in zip(bars,vals):
    ax.text(b.get_x()+b.get_width()/2,v+400,money(v),ha="center",va="bottom",fontsize=11,fontweight="bold",color=NAVY)
# premium annotations
for i,(lab,v,c) in enumerate(r3):
    if i>0:
        d=v-baseline
        ax.text(i,v*0.42,f"+${d/1000:.1f}k\n(+{d/baseline*100:.0f}%)",ha="center",va="center",
                fontsize=11,fontweight="bold",color="white")
ax.axhline(baseline,color=GREYc,ls="--",lw=1.3,zorder=1)
ax.set_xticks(list(x)); ax.set_xticklabels(labels,fontsize=10)
ax.yaxis.set_major_formatter(FuncFormatter(money)); ax.set_ylim(0,max(vals)*1.18)
ax.set_title("Realistic options — cost of a second source vs staying all-SNP",
             fontsize=13.5,fontweight="bold",color=NAVY,pad=28,loc="left")
ax.text(0,1.045,"Using the HIGH-end researched market rate of \$2.55/lb (≈3.4× SNP) — the conservative worst case. Bars exclude CJB, which is still ~2.5–3.5× higher, off-scale.",
        transform=ax.transAxes,fontsize=9.5,color="#555555")
ax.set_ylabel("$ per year")
ax.grid(axis="y",color="#EEEEEE",zorder=0)
for s in ("top","right"): ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig("chart3_realistic.png",bbox_inches="tight"); plt.close(fig)

print("charts rendered: chart1_credit.png chart2_all.png chart3_realistic.png")

# ============ embed into workbook ============
import openpyxl
from openpyxl.drawing.image import Image as XLImage
from openpyxl.styles import Font
wb=openpyxl.load_workbook("PVA_Cost_Scenarios.xlsx")
# drop native charts on the two tabs
for tab in ("Per-Order (credit)","Annual Scenarios"):
    ws=wb[tab]
    ws._charts=[]
# add a Charts tab at front
if "Charts" in wb.sheetnames: del wb["Charts"]
ch=wb.create_sheet("Charts",0)
ch.sheet_view.showGridLines=False
ch["B2"]="PVA Second Source — Cost Charts"; ch["B2"].font=Font(name="Arial",bold=True,size=15,color="1F3864")
ch["B3"]="Every bar is labeled. See data tabs for the underlying numbers and the Market Research tab for sources."
ch["B3"].font=Font(name="Arial",italic=True,size=9,color="595959")
anchors=[("chart1_credit.png","B5"),("chart2_all.png","B36"),("chart3_realistic.png","B67")]
for img,anchor in anchors:
    im=XLImage(img); ch.add_image(im,anchor)
# also embed chart1 on Per-Order tab and 2/3 on Annual tab for context
wb["Per-Order (credit)"].add_image(XLImage("chart1_credit.png"),"G5")
wb["Annual Scenarios"].add_image(XLImage("chart2_all.png"),"E5")
wb["Annual Scenarios"].add_image(XLImage("chart3_realistic.png"),"E36")
wb.save("PVA_Cost_Scenarios.xlsx")
print("embedded into PVA_Cost_Scenarios.xlsx")
