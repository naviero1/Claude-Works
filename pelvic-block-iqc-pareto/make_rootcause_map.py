#!/usr/bin/env python3
"""Root-cause map infographic: the four caudal evisceration substeps, the defects
each creates, and the damage signature that identifies it."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
plt.rcParams["font.family"] = "DejaVu Sans"

NAVY="#1F3864"; VITAL="#2E5B8A"; SLATE="#5B7189"; LINE="#C0504D"; AX="#595959"; LT="#EAF0FA"

fig, ax = plt.subplots(figsize=(14.5, 8.6))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")

# ---- title ----
ax.text(50, 97.5, "Root-Cause Map — where each pelvic-block defect is born",
        ha="center", va="top", fontsize=17, fontweight="bold", color=NAVY)
ax.text(50, 92.3, "≈84% of all 122 defects trace to the Evisceration zone (belly opening + gut-set traction). Read the damage signature to name the station.",
        ha="center", va="top", fontsize=10.5, color=AX)

# ---- process ribbon ----
ribbon_y = 84
ax.text(2, ribbon_y, "Live  →  Stun / Stick", ha="left", va="center", fontsize=9, color=AX, style="italic")
ax.text(98, ribbon_y, "Pit  →  Harvest tech  →  Us", ha="right", va="center", fontsize=9, color=AX, style="italic")
ax.annotate("", xy=(97, ribbon_y-3.2), xytext=(3, ribbon_y-3.2),
            arrowprops=dict(arrowstyle="-|>", color="#B8B8B8", lw=2))

# ---- four substep cards ----
cards = [
    dict(tag="STEP 8 · S2", title="Bung + Aitch bone",
         creates="Rectum nick · distal ureter\ncut/missing · urethra &\nbladder-neck cut",
         sig="Clean KNIFE slit\n(fecal spill if rectum)",
         fix="Coring depth/axis · ≥½\" margin ·\naitch-blade alignment",
         color=SLATE, hot=False),
    dict(tag="STEP 9 · S3", title="Belly opening",
         creates="Bladder hole ·\nmedian-ligament cut",
         sig="Single slit +\nURINE spill",
         fix="\"Unzip\" handle-in cut ·\nsharper knives · FAST the hogs",
         color=VITAL, hot=True),
    dict(tag="STEP 10 · S3", title="Evisceration traction",
         creates="Ureters not embedded ·\nmembrane/ligament tears ·\navulsed ureter",
         sig="Frayed STRETCHED tear ·\nNO bone dust",
         fix="CUT attachments before pulling ·\nslower removal · ergonomics",
         color=VITAL, hot=True),
    dict(tag="STEP 11 · S4", title="Carcass split saw",
         creates="Urethra / bladder-neck /\nureter transection",
         sig="Straight KERF + bone dust ·\nmirror cut on other side",
         fix="Saw/guide calibration ·\nblade condition · size sorting",
         color=SLATE, hot=False),
]
n = len(cards); margin = 3.5; gap = 2.2
cw = (100 - 2*margin - (n-1)*gap) / n
top = 78; card_h = 43
for i, c in enumerate(cards):
    x = margin + i*(cw+gap)
    # connector from ribbon to card
    ax.annotate("", xy=(x+cw/2, top+0.3), xytext=(x+cw/2, ribbon_y-3.4),
                arrowprops=dict(arrowstyle="-|>", color=c["color"], lw=1.6))
    # card
    box = FancyBboxPatch((x, top-card_h), cw, card_h, boxstyle="round,pad=0.3,rounding_size=1.4",
                         linewidth=1.4, edgecolor=c["color"], facecolor=(LT if c["hot"] else "#FFFFFF"))
    ax.add_patch(box)
    # header band
    hb = FancyBboxPatch((x, top-9), cw, 9, boxstyle="round,pad=0.3,rounding_size=1.4",
                        linewidth=0, facecolor=c["color"])
    ax.add_patch(hb)
    ax.text(x+cw/2, top-2.4, c["tag"], ha="center", va="top", fontsize=8, color="#DDE6F2", fontweight="bold")
    ax.text(x+cw/2, top-5.0, c["title"], ha="center", va="top", fontsize=11.5, color="white", fontweight="bold")
    yy = top-12
    for label, val, col in [("CREATES", c["creates"], "#333333"),
                            ("SIGNATURE", c["sig"], LINE),
                            ("FIX", c["fix"], "#2E6B34")]:
        ax.text(x+1.6, yy, label, ha="left", va="top", fontsize=7.5, color=col, fontweight="bold")
        ax.text(x+1.6, yy-2.4, val, ha="left", va="top", fontsize=8.3, color="#222222")
        yy -= (2.4 + val.count("\n")*2.7 + 4.2)

# ---- signature legend strip ----
ly = 12.5
ax.add_patch(FancyBboxPatch((3, 3), 94, 9.2, boxstyle="round,pad=0.3,rounding_size=1.2",
                            linewidth=1, edgecolor="#C9C9C9", facecolor="#F7F7F7"))
ax.text(5, ly-2.0, "DAMAGE SIGNATURE  →  STATION", fontsize=9, fontweight="bold", color=NAVY, va="top")
sig_items = [
    ("Straight kerf + bone dust", "Saw (S4)"),
    ("Clean single slit", "Knife (S2/S3)"),
    ("Frayed stretched tear", "Traction (S3)"),
    ("Petechiae / speckle", "Stun–stick (S1)"),
]
sx = 5
for s, st in sig_items:
    ax.text(sx, ly-5.2, s, fontsize=8.2, color="#222222", va="top", fontweight="bold")
    ax.text(sx, ly-7.4, "→ "+st, fontsize=8.2, color=LINE, va="top")
    sx += 23.3

plt.savefig("RootCause_map.png", dpi=130, bbox_inches="tight")
print("saved RootCause_map.png")
