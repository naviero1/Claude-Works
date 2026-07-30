#!/usr/bin/env python3
"""Yield snapshot: good pelvics across the board + the tech<->inspector alignment point."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "DejaVu Sans"

NAVY="#1F3864"; VITAL="#2E5B8A"; TAIL="#D9E1F2"; RED="#C0504D"; AX="#595959"; GOODC="#4F8A5B"

good, inspected = 10, 99
rej = inspected - good
pct = good/inspected*100

fig = plt.figure(figsize=(12.8, 5.9))
fig.suptitle("Good pelvics across the board", x=0.5, y=0.97, fontsize=17, fontweight="bold", color=NAVY)
fig.text(0.5, 0.895, "Only 1 in 10 blocks that reach inspection passes on the first look — first a supplier signal, but it also frames the tech/inspector questions.",
         ha="center", fontsize=10, color=AX)

# --- left: donut good vs rejected ---
axd = fig.add_axes([0.03, 0.14, 0.34, 0.66])
axd.pie([good, rej], colors=[GOODC, "#E6E6E6"], startangle=90, counterclock=False,
        wedgeprops=dict(width=0.34, edgecolor="white", linewidth=2))
axd.text(0, 0.12, f"{pct:.1f}%", ha="center", va="center", fontsize=30, fontweight="bold", color=GOODC)
axd.text(0, -0.22, f"{good} good / {inspected} inspected", ha="center", va="center", fontsize=10.5, color=AX)
axd.set_title("Good (pass IQC) vs rejected", fontsize=10.5, color=NAVY, fontweight="bold", pad=6)

# --- middle: good% by kill date (the collapse) ---
axb = fig.add_axes([0.44, 0.20, 0.24, 0.58])
kd = ["2026-05-27", "2026-07-08", "2026-07-28"]
gp = [25.8, 3.8, 2.4]
bars = axb.bar(range(3), gp, color=[VITAL, VITAL, VITAL], width=0.62, zorder=3, edgecolor="white")
for b, v in zip(bars, gp):
    axb.text(b.get_x()+b.get_width()/2, v+0.8, f"{v}%", ha="center", fontsize=10, fontweight="bold", color=NAVY)
axb.set_xticks(range(3)); axb.set_xticklabels([d[5:] for d in kd], fontsize=9, color=AX)
axb.set_ylim(0, 30); axb.set_yticks([0,10,20,30]); axb.tick_params(colors=AX, labelsize=8)
axb.grid(axis="y", color="#EAEAEA", zorder=0); axb.set_axisbelow(True)
for s in ("top","right"): axb.spines[s].set_visible(False)
axb.spines["left"].set_color("#BFBFBF"); axb.spines["bottom"].set_color("#BFBFBF")
axb.set_title("Good rate by kill date", fontsize=10.5, color=NAVY, fontweight="bold", pad=6)
axb.text(1, 27, "yield is\ncollapsing", ha="center", fontsize=8.5, color=RED, style="italic")

# --- right: alignment callout ---
axc = fig.add_axes([0.71, 0.14, 0.27, 0.66]); axc.axis("off")
axc.add_patch(plt.Rectangle((0,0),1,1, transform=axc.transAxes, facecolor="#F4F7FC", edgecolor="#C9D6EA", lw=1.2))
axc.text(0.5, 0.93, "TECH ↔ INSPECTOR ALIGNMENT", ha="center", va="top", fontsize=10, fontweight="bold", color=NAVY, transform=axc.transAxes)
lines = [
    ("~10%", "of blocks the harvest techs KEPT, inspectors also passed", GOODC),
    ("~90%", "of kept blocks were rejected by inspectors — a misalignment signal on the KEEP call", RED),
]
y = 0.76
for big, txt, col in lines:
    axc.text(0.08, y, big, ha="left", va="top", fontsize=17, fontweight="bold", color=col, transform=axc.transAxes)
    axc.text(0.08, y-0.10, txt, ha="left", va="top", fontsize=8.6, color="#333333", wrap=True, transform=axc.transAxes)
    y -= 0.30
axc.text(0.08, 0.14, "Confounded with material quality (84% of defects are supplier/evisceration-origin). To measure true alignment, log each tech's keep/discard vs the inspector's pass/fail.",
         ha="left", va="top", fontsize=7.8, color=AX, style="italic", transform=axc.transAxes)

plt.savefig("Yield_snapshot.png", dpi=130, bbox_inches="tight")
print("saved Yield_snapshot.png")
