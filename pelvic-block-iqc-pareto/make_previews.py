#!/usr/bin/env python3
"""Render preview PNGs that faithfully mirror the native Excel chart design
(combined across all ingested batches)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
plt.rcParams["font.family"] = "DejaVu Sans"

C_VITAL="#2E5B8A"; C_TAIL="#AFC7E3"; C_LINE="#C0504D"; C_GRID="#E6E6E6"; C_TITLE="#1F3864"; C_AX="#595959"

# combined counts (all batches), sorted desc
codes  = ["D6","D1","D5","D8","D4","D2","D13","D12","D3","D7","D9","D10","D11"]
short  = ["Membrane dmg","Ureters n/e","Urethra breach","Bowel/colon","Susp. ligament",
          "Ureter cut","Block too short","Bladder breach","Ureter missing","Bladder def.",
          "Blood clots","Broad ligament","Bladder neck sep."]
counts = [49,17,14,9,8,7,7,4,3,1,1,1,1]
NFEW = 5
total=sum(counts); cum=[]; run=0
for c in counts: run+=c; cum.append(run/total*100)
xlabels=[f"{c} · {s}" for c,s in zip(codes,short)]

fig, ax = plt.subplots(figsize=(14.5,6.9)); fig.subplots_adjust(bottom=0.27, top=0.87)
cols=[C_VITAL if i<NFEW else C_TAIL for i in range(len(counts))]
bars=ax.bar(range(len(counts)),counts,color=cols,edgecolor="white",linewidth=1,zorder=3,width=0.72)
ax.set_ylabel("Defect count",fontsize=11,fontweight="bold",color=C_AX)
ax.set_xticks(range(len(counts))); ax.set_xticklabels(xlabels,rotation=45,ha="right",fontsize=9,color=C_AX)
ax.set_ylim(0,54); ax.set_yticks(range(0,55,6)); ax.tick_params(colors=C_AX)
for b,c in zip(bars,counts):
    ax.text(b.get_x()+b.get_width()/2,c+0.4,str(c),ha="center",va="bottom",fontsize=10,fontweight="bold",color="#404040")
ax.grid(axis="y",color=C_GRID,zorder=0,linewidth=0.8); ax.set_axisbelow(True)
for s in ("top","right"): ax.spines[s].set_visible(False)
ax.spines["left"].set_color("#BFBFBF"); ax.spines["bottom"].set_color("#BFBFBF")

ax2=ax.twinx()
# cumulative line = subtle reference (no per-point labels); exact %s live in the Pareto table
ax2.plot(range(len(counts)),cum,color=C_LINE,marker="o",ms=4.5,lw=1.7,zorder=4,mec="white",mew=0.8,alpha=0.9)
ax2.axhline(80,color="#A6A6A6",ls=(0,(5,3)),lw=1.1,zorder=2)
ax2.yaxis.set_major_formatter(PercentFormatter()); ax2.set_ylim(0,105); ax2.set_yticks(range(0,101,20))
ax2.set_ylabel("Cumulative %",fontsize=11,fontweight="bold",color=C_AX); ax2.tick_params(colors=C_AX)
ax2.spines["top"].set_visible(False)
leg=[Patch(facecolor=C_VITAL,label="Count (vital few — fix first)"),Patch(facecolor=C_TAIL,label="Count (tail)"),
     Line2D([0],[0],color=C_LINE,marker="o",label="Cumulative %"),
     Line2D([0],[0],color="#A6A6A6",ls="--",label="80% line")]
ax.legend(handles=leg,loc="upper center",bbox_to_anchor=(0.5,-0.30),ncol=4,frameon=False,fontsize=9)
ax.set_title("Defect Pareto — Rejected Pelvic Blocks   (SH: Martins · 3 kill dates · 99 inspected · 89 fail · 122 defects)",
             fontsize=12.5,fontweight="bold",color=C_TITLE,pad=14)
plt.savefig("Pareto_preview.png",dpi=130,bbox_inches="tight"); print("saved Pareto_preview.png")

# station rollup
fig2,axs=plt.subplots(figsize=(9,4.4)); fig2.subplots_adjust(top=0.82,bottom=0.16)
st_lbl=["S3 Evisceration","S4 Carcass\nsplitting","S2 Bung +\naitch bone","S1 Sticking /\nbleeding","S6 Live /\nphysiology"]
st_cnt=[102,15,3,1,1]; st_col=[C_VITAL]+[C_TAIL]*4
b2=axs.bar(range(len(st_cnt)),st_cnt,color=st_col,edgecolor="white",linewidth=1,zorder=3,width=0.66)
axs.set_xticks(range(len(st_cnt))); axs.set_xticklabels(st_lbl,fontsize=9,color=C_AX)
axs.set_ylabel("Defect count",fontweight="bold",color=C_AX); axs.tick_params(colors=C_AX)
for b,c in zip(b2,st_cnt):
    axs.text(b.get_x()+b.get_width()/2,c+1.2,f"{c}  ({c/122*100:.0f}%)",ha="center",va="bottom",fontsize=9.5,fontweight="bold",color="#404040")
axs.set_ylim(0,115); axs.grid(axis="y",color=C_GRID,zorder=0,linewidth=0.8); axs.set_axisbelow(True)
for s in ("top","right"): axs.spines[s].set_visible(False)
axs.spines["left"].set_color("#BFBFBF"); axs.spines["bottom"].set_color("#BFBFBF")
axs.set_title("Where the defects are born — rollup by SUPPLIER STATION\n84% of all defects originate at Evisceration",
              fontsize=11.5,fontweight="bold",color=C_TITLE)
plt.savefig("Station_rollup_preview.png",dpi=130,bbox_inches="tight"); print("saved Station_rollup_preview.png")
