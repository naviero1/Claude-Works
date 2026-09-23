#!/usr/bin/env python3
"""Leadership deck v3: Feasibility -> Cost (x2) -> Logistics + the PCI question -> Decision. Concise, one message per slide."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

NAVY=RGBColor(0x1F,0x38,0x64); STEEL=RGBColor(0x4E,0x79,0xA7); GREY=RGBColor(0x59,0x59,0x59)
WHITE=RGBColor(0xFF,0xFF,0xFF); GREEN=RGBColor(0x2E,0x7D,0x46); RED=RGBColor(0xB2,0x3A,0x2E)
AMBER=RGBColor(0x9C,0x5A,0x0C); LIGHT=RGBColor(0xEE,0xF2,0xF7); PALE=RGBColor(0xF6,0xF8,0xFB)
LGREEN=RGBColor(0xE2,0xEF,0xDA); LRED=RGBColor(0xFC,0xE4,0xD6); LAMB=RGBColor(0xFF,0xF2,0xCC)

prs=Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
BLANK=prs.slide_layouts[6]

def slide(): return prs.slides.add_slide(BLANK)
def rect(s,l,t,w,h,fill,line=None):
    sp=s.shapes.add_shape(MSO_SHAPE.RECTANGLE,Inches(l),Inches(t),Inches(w),Inches(h))
    sp.fill.solid(); sp.fill.fore_color.rgb=fill
    if line: sp.line.color.rgb=line; sp.line.width=Pt(0.75)
    else: sp.line.fill.background()
    sp.shadow.inherit=False; return sp
def box(s,l,t,w,h):
    tf=s.shapes.add_textbox(Inches(l),Inches(t),Inches(w),Inches(h)).text_frame; tf.word_wrap=True; return tf
def par(p,text,size,color=NAVY,bold=False,italic=False,align=PP_ALIGN.LEFT,after=4):
    p.text=text; p.alignment=align; p.space_after=Pt(after)
    r=p.runs[0]; r.font.size=Pt(size); r.font.color.rgb=color; r.font.bold=bold; r.font.italic=italic; r.font.name="Calibri"; return p
def title_bar(s,text,section=None):
    rect(s,0,0,13.333,1.0,NAVY)
    tf=box(s,0.5,0.14,10.6,0.8); par(tf.paragraphs[0],text,26,WHITE,bold=True)
    if section:
        tf=box(s,10.9,0.3,2.2,0.5); par(tf.paragraphs[0],section,11,RGBColor(0xBD,0xD7,0xEE),align=PP_ALIGN.RIGHT)
def bullets(s,l,t,w,h,items,size=14,gap=8,color=GREY):
    tf=box(s,l,t,w,h)
    for i,it in enumerate(items):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.space_after=Pt(gap)
        lead,rest=(it if isinstance(it,tuple) else (None,it))
        if lead:
            r=p.add_run(); r.text="•  "+lead; r.font.bold=True; r.font.size=Pt(size); r.font.color.rgb=NAVY; r.font.name="Calibri"
            r2=p.add_run(); r2.text=rest; r2.font.size=Pt(size); r2.font.color.rgb=color; r2.font.name="Calibri"
        else:
            r=p.add_run(); r.text="•  "+rest; r.font.size=Pt(size); r.font.color.rgb=color; r.font.name="Calibri"
    return tf
def card(s,l,t,w,h,value,label,vcolor=NAVY,fill=LIGHT,vsize=24):
    rect(s,l,t,w,h,fill)
    tf=box(s,l+0.12,t+0.12,w-0.24,h-0.24); tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    par(tf.paragraphs[0],value,vsize,vcolor,bold=True,align=PP_ALIGN.CENTER,after=2)
    par(tf.add_paragraph(),label,10.5,GREY,align=PP_ALIGN.CENTER)
def takeaway(s,text,t=6.55,fill=NAVY,color=WHITE,size=14):
    rect(s,0.6,t,12.1,0.62,fill)
    tf=box(s,0.8,t+0.08,11.7,0.5); tf.vertical_anchor=MSO_ANCHOR.MIDDLE; par(tf.paragraphs[0],text,size,color,bold=True)
def table(s,l,t,w,h,rows,colw,size=11,hdr_fill=NAVY,fills=None,align_first_left=True):
    tbl=s.shapes.add_table(len(rows),len(rows[0]),Inches(l),Inches(t),Inches(w),Inches(h)).table
    for i,cw in enumerate(colw): tbl.columns[i].width=Inches(cw)
    for ri,row in enumerate(rows):
        for ci,val in enumerate(row):
            c=tbl.cell(ri,ci); c.text=str(val); p=c.text_frame.paragraphs[0]
            p.alignment=PP_ALIGN.LEFT if (ci==0 and align_first_left) or ci==len(row)-1 and len(row)>3 else PP_ALIGN.CENTER
            r=(p.runs[0] if p.runs else p.add_run()); r.font.size=Pt(size); r.font.name="Calibri"; c.fill.solid()
            if ri==0: r.font.bold=True; r.font.color.rgb=WHITE; c.fill.fore_color.rgb=hdr_fill
            else:
                r.font.color.rgb=NAVY; c.fill.fore_color.rgb=(fills[ri][ci] if fills and fills[ri] and fills[ri][ci] else WHITE)
                if ci==0: r.font.bold=True
    return tbl
def panel(s,l,t,w,h,title,items,tcolor,fill,size=12):
    rect(s,l,t,w,h,fill); tf=box(s,l+0.2,t+0.15,w-0.4,h-0.3); par(tf.paragraphs[0],title,14,tcolor,bold=True,after=7)
    for it in items: par(tf.add_paragraph(),"•  "+it,size,GREY,after=6)
    return tf

# ================= 1 TITLE =================
s=slide(); rect(s,0,0,13.333,7.5,NAVY); rect(s,0,4.85,13.333,0.06,STEEL)
tf=box(s,0.8,1.6,11.7,2.8)
par(tf.paragraphs[0],"Liquid PVA: One Supplier or Two?",42,WHITE,bold=True)
par(tf.add_paragraph(),"Feasibility  ·  Cost  ·  Logistics  ·  Decision",22,RGBColor(0xBD,0xD7,0xEE))
tf=box(s,0.8,5.1,11.7,1.6)
par(tf.paragraphs[0],"PVA = polyvinyl alcohol — the liquid we buy in 55-gallon drums from SNP Inc. (Durham, NC) to make our hydrogels. Sole-sourced today.",14,WHITE)
par(tf.add_paragraph(),"Oscar Penny  ·  Supply Chain  ·  22 September 2026  ·  Decision requested",12,RGBColor(0x9D,0xC3,0xE6))

# ================= 2 FEASIBILITY =================
s=slide(); title_bar(s,"Feasibility: two things limited the field — temperature, then expertise","1 · FEASIBILITY")
card(s,0.6,1.2,2.9,1.3,"94","US suppliers screened")
card(s,3.7,1.2,2.9,1.3,"~10","could hold 90–95 °C",vcolor=AMBER,fill=LAMB)
card(s,6.8,1.2,2.9,1.3,"1","proved the expertise (PCI Manufacturing)",vcolor=GREEN,fill=LGREEN)
card(s,9.9,1.2,2.8,1.3,"~6 months","to get there",vcolor=RED,fill=LRED)
panel(s,0.6,2.75,3.95,3.6,"Limit 1 — Temperature",
 ["Super-hydrolyzed, high-molecular-weight PVA only dissolves with a 30–45 min hold at 90–95 °C",
  "Most toll blenders top out lower. ArroChem Inc. (85 °C ceiling), ILC Dover and Columbus Chemical Industries all failed here",
  "This single gate removed most of the 94"],RED,LRED,11.5)
panel(s,4.7,2.75,3.95,3.6,"Limit 2 — Expertise",
 ["Getting through the gate is not the same as making the product: no fisheyes, no gels, viscosity on target",
  "Brenntag's trial: viscosity 'too high to read'. PCI Manufacturing's first batch: 2,420 cP vs ~1,000 target — fixed only after finding the solids root cause",
  "Handful of shops in the US have done this before"],AMBER,LAMB,11.5)
panel(s,8.8,2.75,3.9,3.6,"Then — cost & fit",
 ["The one toll quote through the gate (CJB Applied Technologies): ~11× SNP Inc.",
  "18-day shelf life ⇒ small batches; suppliers with 220–250 gal minimums (Royal Chemical, CORECHEM) overshoot it",
  "Every viable supplier needs ≥1 drum/week to engage"],NAVY,LIGHT,11.5)
takeaway(s,"SNP Inc. is not just cheap — it is one of very few shops that can make this at all, and it does so as its core product.")

# ================= 3 COST 1/2 — WHERE PRICES COME FROM =================
s=slide(); title_bar(s,"Cost (1 of 3): where every price on the table comes from","2 · COST")
rows=[["$/lb finished","Source","How it is built — and why"],
 ["$0.16–0.20","Material floor","Raw PVA resin $1.26–1.60/lb (ChemAnalyst / IMARC, N. America 2026) × 11% solids. Everything above this is conversion, freight and margin."],
 ["$0.75","SNP Inc. — real quote","Estimate 012726-1, delivered all-in. Below market because PVA cooking is their core product and their tanks are right-sized to our batch."],
 ["$0.85 / $1.40 / $2.55","Market low / base / high (triangulated)","Resin floor + loaded labor (~$40/hr, 25% margin) + QC + 1-drum freight ($0.22–0.55/lb). High case anchored by a retail comp (~$2.03/lb bulk PVA solution)."],
 ["$2.50 – $5.00","PCI Manufacturing — our forecast","Not yet quoted. Range reflects a capable but non-specialist shop pricing a small, unfamiliar, high-temperature batch — with risk built in."],
 ["$8.42","CJB Applied Technologies — real quote","$8.00–8.50/lb toll EXCLUDING materials (+~$75/drum resin). ~50× the material floor, ~11× SNP: an outlier, shown for scale."]]
fills=[None,None,[None,LGREEN,None],None,[None,LAMB,None],[None,LRED,None]]
table(s,0.6,1.2,12.1,3.55,rows,[1.7,2.9,7.5],size=11,fills=fills)
panel(s,0.6,4.9,5.95,1.5,"Why a new supplier carries a premium at our volume",
 ["Conversion cost is mostly FIXED per batch — setup, heat-up, hold, cleaning, QC, paperwork (~$400–900/batch). Spread over one 450-lb drum that alone is $0.90–2.00/lb.",
  "Add one-drum freight and a 'learning our product' risk margin, and $2.50–5.00 is what a good shop will ask."],NAVY,LIGHT,10.5)
panel(s,6.75,4.9,5.95,1.5,"Why SNP Inc. is cheap — specialization",
 ["PVA solution is their product line, not a side job: process dialed-in, no learning premium.",
  "Multiple tank sizes let them right-size each batch to our order — the fixed cost per pound stays low. A generalist runs our drum in whatever tank is free."],GREEN,LGREEN,10.5)
takeaway(s,"$0.75/lb is a specialist's price. Every credible second source will sit at $2.50–5.00 — not because they are greedy, but because of batch economics.")

# ================= 4 COST 2/2 — WHAT EACH OPTION COSTS US =================
s=slide(); title_bar(s,"Cost (2 of 3): what each option costs us, per year and over five","2 · COST")
s.shapes.add_picture("chart_premium_by_price.png",Inches(0.6),Inches(1.15),width=Inches(7.6))
rect(s,8.45,1.15,4.25,5.2,PALE,STEEL); tf=box(s,8.62,1.28,3.95,5.0)
par(tf.paragraphs[0],"Options at one drum/week to PCI (~1/3)",13,NAVY,bold=True,after=6)
rows=[["","Per year","5 years*"],["All-SNP (today)","$50.7k","—"],["A @ $2.50","+$41k","+$242k"],["A @ $3.75 (mid)","+$70k","+$415k"],["A @ $5.00","+$99k","+$588k"],["CJB, for scale","+$179k","—"]]
tb=s.shapes.add_table(6,3,Inches(8.62),Inches(1.75),Inches(3.95),Inches(2.3)).table
tb.columns[0].width=Inches(1.75); tb.columns[1].width=Inches(1.05); tb.columns[2].width=Inches(1.15)
for ri,row in enumerate(rows):
    for ci,v in enumerate(row):
        c=tb.cell(ri,ci); c.text=v; p=c.text_frame.paragraphs[0]; p.alignment=PP_ALIGN.LEFT if ci==0 else PP_ALIGN.CENTER
        r=(p.runs[0] if p.runs else p.add_run()); r.font.size=Pt(10.5); r.font.name="Calibri"; c.fill.solid()
        if ri==0: r.font.bold=True; r.font.color.rgb=WHITE; c.fill.fore_color.rgb=NAVY
        else:
            r.font.color.rgb=NAVY; c.fill.fore_color.rgb=(LAMB if ri==3 else (LRED if ri==5 else WHITE))
            if ci==0: r.font.bold=True
tf=box(s,8.62,4.15,3.95,2.1)
par(tf.paragraphs[0],"*volume +10%/yr; plus ~$15k one-time qualification",9.5,GREY,italic=True,after=6)
par(tf.add_paragraph(),"There is no smaller version: 1 drum/week is the least any supplier will take. July's '$6–12k' assumed a price and a share that don't exist.",11,NAVY,bold=True,after=6)
par(tf.add_paragraph(),"If SNP Inc. re-prices the ~2/3 it keeps (+10–20%): add $3–7k/yr.",10.5,GREY)
takeaway(s,"A second source costs 80–195% of today's entire PVA spend, every year, growing with volume. That is the price of the insurance.")

# ================= 4b COST 3/3 — THE UPSIDE CASE =================
s=slide(); title_bar(s,"Cost (3 of 3): what if the price comes in below $2.50?","2 · COST")
tf=box(s,0.6,1.15,12.1,0.7)
par(tf.paragraphs[0],"Everything so far assumes a non-specialist price. The market base is $1.40/lb — so a capable shop at $1.00–2.50 is plausible, not wishful. If one exists, the picture changes completely.",13.5,NAVY,bold=True)
rows=[["Price / lb","Premium per year","5-year premium","Outage cost that justifies it (5% / 10% per yr)","What it would mean"],
 ["$1.00","+$6k","+$35k","~$120k / ~$60k","The July plan, as described. Clear yes — insurance cheaper than almost any outage."],
 ["$1.25","+$12k","+$69k","~$235k / ~$120k","Clear yes."],
 ["$1.40  (market base)","+$15k","+$90k","~$305k / ~$150k","Likely yes — the premium is a rounding error against a product line."],
 ["$1.50","+$18k","+$104k","~$350k / ~$175k","Likely yes. This is the trigger already in the plan."],
 ["$2.00","+$29k","+$173k","~$585k / ~$295k","Borderline — the outage-cost number decides."],
 ["$2.50","+$41k","+$242k","~$820k / ~$410k","Needs a large outage cost to justify (today's base case)."]]
fills=[None,[None,LGREEN,LGREEN,None,LGREEN],[None,LGREEN,LGREEN,None,LGREEN],[None,LGREEN,LGREEN,None,LGREEN],[None,LGREEN,LGREEN,None,LGREEN],[None,LAMB,LAMB,None,LAMB],[None,LRED,LRED,None,LRED]]
table(s,0.6,1.95,12.1,3.15,rows,[1.8,1.6,1.6,3.0,4.1],size=10.5,fills=fills)
panel(s,0.6,5.25,5.95,1.2,"The opportunity cost of not looking",
 ["If a $1–1.50/lb source exists and we stop, we forgo insurance that costs less than one bad week — and a live price reference that alone would discipline SNP Inc.'s pricing."],RED,LRED,11)
panel(s,6.75,5.25,5.95,1.2,"How we find out — cheaply",
 ["Issue the RFQ to PCI Manufacturing against the agreed spec (11% solids, 900–1,100 cP) now. A real number in ~2 weeks, at no cost, decides which side of the table we are on."],GREEN,LGREEN,11)
takeaway(s,"Below ~$1.50/lb this is an easy yes; above ~$2.50 it needs a big outage cost. Price discovery is the cheapest decision we can make.")

# ================= 5 LOGISTICS =================
s=slide(); title_bar(s,"Logistics: what two suppliers look like under an 18–30 day shelf life","3 · LOGISTICS")
panel(s,0.6,1.2,5.95,2.55,"The rhythm",
 ["Every drum is made to order — an 18–30 day shelf life means no safety stock from either supplier. Drums arrive already aged, so real time-to-survive is ~1–1.5 weeks, not 2½",
  "PCI Manufacturing: 1 drum/week (its minimum). SNP Inc.: ~2 drums/week. Each drum consumed within ~2 weeks of receipt, first-in-first-out by production date",
  "Two lead times, two ship lanes (Durham NC vs St. Louis MO), two order calendars to keep in phase"],NAVY,LIGHT,11)
panel(s,6.75,1.2,5.95,2.55,"The control we would need — and how",
 ["One harmonized spec for both: 11% solids, 900–1,100 cP fresh, pH target — and ONE viscometer method, or the numbers cannot be compared",
  "Incoming test on every lot (viscosity, solids, pH) against a Certificate of Analysis (CoA) from each supplier; lot traceability to source so hydrogel performance can be tracked by supplier",
  "Two cleaning procedures (PCI's residual-film issue is open), two Supplier Quality Agreements with change-notification and audit rights, quarterly scorecards"],NAVY,LIGHT,11.5)
panel(s,0.6,3.95,5.95,2.4,"What it costs to run",
 ["A standing overhead: ~1 extra incoming-QC lot per week, dual documentation, two relationships — plus R&D and Quality time for hydrogel equivalence by source and CAPA across two streams. Two suppliers also means two chances of a quality escape",
  "A written ramp plan for PCI Manufacturing (1 → 3 drums/week) — without it, the second source cannot actually cover an SNP Inc. outage",
  "Sub-tier check: if both cook the same producer's resin, a second cooker hedges cooking, not resin — the shelf-stable resin buffer is the hedge either way"],AMBER,LAMB,10.5)
panel(s,6.75,3.95,5.95,2.4,"What it buys — and the cheapest lever of all",
 ["Recovery in weeks, not months, if SNP Inc. fails — provided the ramp plan is real; a live price reference; a second set of process knowledge",
  "It does NOT remove the exposure: ~2/3 of volume still stops until the ramp completes",
  "Under either option, a validated 30–45-day shelf-life study (biocide / refrigeration) lengthens time-to-survive for a lab study's cost — worth doing first"],GREEN,LGREEN,10.5)
takeaway(s,"Running two suppliers is manageable — but it is a permanent operating discipline, not a one-time qualification.")

# ================= 6 THE PCI QUESTION =================
s=slide(); title_bar(s,"The PCI question: if we deem them capable and then don't buy, what happens?","3 · LOGISTICS")
bullets(s,0.6,1.2,6.6,5.0,[
 ("What PCI Manufacturing has already invested — unpaid. ","Two lab batches, a dilution study, viscosity-method work, a revised process; shelf-life and hydrogel studies queued. Months of engineering time on a ~$25–50k/yr account."),
 ("Yes, walking away carries a real risk. ","Small and mid-size shops remember. The realistic outcomes: they decline to re-engage, deprioritize us behind paying customers, or require paid development and a volume commitment next time. Our 'cold-start' plan would lose its most valuable part — a willing, proven supplier."),
 ("It is also a soft cost that Option B does not show. ","Choosing B is not free: it spends goodwill we may need in a crisis. That belongs on the ledger next to the $41–99k/yr."),
 ("How to handle it honestly. ","Decide BEFORE asking them to run the shelf-life and hydrogel studies. If we lean B: be transparent about the volume reality and the triggers, and offer to pay for the qualification work done (~$15k — the same money any second source would cost to qualify). If we lean A: commit to the drum a week now, not after another round of free experiments."),
],size=12.5,gap=9)
rect(s,7.5,1.2,5.2,5.0,PALE,STEEL); tf=box(s,7.7,1.35,4.8,4.8)
par(tf.paragraphs[0],"Three ways to leave the door open",13.5,NAVY,bold=True,after=8)
for k,v in [("Pay for the work","Fund the qualification already done. Converts 'free experiments' into a paid development engagement they can justify internally."),
            ("Be explicit about the triggers","Tell them when we would switch (outage-cost threshold, an SNP Inc. risk signal, their price at ≤ ~$1.50/lb). A defined path is a relationship; silence is not."),
            ("Keep the file warm, not the orders","Approved-source documentation, agreed spec, their test record — refreshed annually with a call, so a restart is months, not a year.")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+"  "; r.font.bold=True; r.font.size=Pt(12); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text="— "+v; r2.font.size=Pt(11.5); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(9)
takeaway(s,"If the answer is 'not now', we owe PCI Manufacturing a candid conversation and a cheque — before the next round of experiments, not after.",fill=AMBER)

# ================= 7 DECISION =================
s=slide(); title_bar(s,"Decision: A or B — and the one number that settles it","4 · DECISION")
rows=[["","A · Second source (PCI Manufacturing, 1 drum/wk)","B · Single source (SNP Inc.), strengthened"],
 ["Annual premium","+$70k mid  ($41–99k)","~$3–12k/yr continuity bundle"],
 ["5-year premium","~$415k  ($242–588k)","~$15–60k, plus ~$5–10k one-time"],
 ["Exposure if SNP Inc. fails","~2/3 of volume until PCI ramps","100%"],
 ["Time to recover","weeks (with a ramp plan)","6–12 months; 3–4 with the cold-start kit current"],
 ["Relationship","Takes a third of SNP Inc.'s line; PCI engaged","Deeper SNP partnership; PCI door kept open (paid)"],
 ["Pays off when…","6-month outage cost > ~$700k (10%/yr risk) or ~$1.4M (5%)","outage cost below that, and SNP Inc. stays healthy and engaged"]]
fills=[None]+[[None,LRED,LGREEN] for _ in range(6)]
table(s,0.6,1.2,12.1,2.75,rows,[2.3,4.9,4.9],size=10.5,fills=fills)
panel(s,0.6,4.05,5.95,2.4,"Recommendation — in this order",
 ["1. Price discovery first: RFQ to PCI Manufacturing on the agreed spec (~2 weeks, no cost). ≤ $1.50/lb → A; ≥ $2.50 → B unless the outage cost is large; between → the outage number decides.",
  "2. Either way, strengthen SNP Inc. now: forecast, hydrogel program, continuity terms, shelf-stable RESIN on consignment, annual financial check; confirm their capacity headroom for +10%/yr; say plainly that continuity planning is a quality-system requirement, not a loss of confidence.",
  "3. If B: settle with PCI Manufacturing honestly — pay for the work, state the triggers. Waiting is not passive: growth widens the feasible supplier set (minimum share 35% → 24% by year 5)."],GREEN,LGREEN,9.2)
panel(s,6.75,4.05,5.95,2.4,"Switch to A the moment any trigger fires",
 ["Finance's outage estimate clears the break-even  ·  an SNP Inc. risk signal (finances, key person, missed lot, odd price move)",
  "PCI Manufacturing quotes ≤ ~$1.50/lb (premium falls to ~$18k)  ·  a new hydrogel line makes PVA strategic  ·  SNP Inc. declines the partnership",
  "SNP Inc.'s capacity headroom falls short of year-5 volume (~99k lb) — then this is a capacity question, not an insurance one"],AMBER,LAMB,9.5)
takeaway(s,"Asks: (1) the outage cost — per hydrogel SKU: revenue, contribution margin, deferrable vs lost demand (fallback: more or less than $1M? $3M?); (2) get PCI's price now; (3) formalize SNP Inc.",size=12)

# ================= 8 APPENDIX =================
s=slide(); title_bar(s,"Appendix: assumptions, sources, suppliers, acronyms")
rows=[["Assumption","Value","Basis"],
 ["Demand today","1,300 lb/wk ≈ 150 drums/yr","Confirmed 2026-06-26"],
 ["SNP Inc. price","$0.75/lb delivered = $337.50/drum","SNP Estimate 012726-1"],
 ["PCI Manufacturing price","$2.50 / $3.75 / $5.00 per lb","Leadership range; not yet quoted"],
 ["Supplier minimum","1 drum/week (52/yr ≈ 35% today)","Supplier condition"],
 ["Volume growth","+10%/yr","Leadership assumption"],
 ["Market reference","$0.85 / $1.40 / $2.55 per lb","Resin floor + labor build-up + retail ceiling"],
 ["CJB quote","$8.00–8.50/lb toll excl. materials ≈ $8.42 landed","CJB email 'RE: mix test'"],
 ["Qualification cost","~$15k one-time","PLACEHOLDER — confirm"],
 ["Outage cost","not yet estimated","NEEDED from Finance / Ops"]]
table(s,0.6,1.15,6.9,3.3,rows,[2.0,2.7,2.2],size=9)
tf=box(s,0.6,4.5,6.9,2.3)
par(tf.paragraphs[0],"Frameworks behind the analysis (independently fact-checked)",11,NAVY,bold=True,after=3)
par(tf.add_paragraph(),"Kraljic (HBR 1983), bottleneck items: 'Volume insurance (at cost premium if necessary). Control of vendors. Security of inventories. Backup plans' — pay for a backup when the premium is proportionate. Gelderman & van Weele (2003): 'hold' vs 'move' — move only when economically worthwhile. Simchi-Levi et al. (Interfaces 2015, Ford): disruption impact is uncorrelated with spend. Sheffi & Rice (MIT SMR 2005): single sourcing is legitimate only with a deep, managed relationship. Tomlin (2006); Chopra & Sodhi (2014): assuming zero disruption probability is the expensive mistake. Pulles, Schiele et al. (2016): preferential treatment follows attractiveness, not volume. Deloitte CPO 2025: 'active alternative sources' rated most effective (74%); McKinsey 2024 (secondary): 46% cutting risk buffers. QMSR / ISO 13485 §7.4 / GHTF N17: controls proportionate to risk — no second source required. In-house make: a ~$30–60k bench cook is a bridge only. Six research lenses; four refuted claims excluded; memo in the repo.",8.5,GREY)
rect(s,7.75,1.15,4.95,5.4,PALE,STEEL); tf=box(s,7.9,1.22,4.7,5.3)
par(tf.paragraphs[0],"Suppliers named",12,NAVY,bold=True,after=3)
for k,v in [("SNP Inc.","Durham, NC — incumbent, sole source"),("PCI Manufacturing","St. Louis, MO — CMS Manufacturing group; candidate in testing"),("CJB Applied Technologies","Valdosta, GA — quoted ~11×"),("ArroChem Inc.","Mount Holly, NC — 85 °C ceiling"),("ILC Dover","Frederica, DE — could not hold temperature"),("Columbus Chemical Industries","Columbus, WI — could not hold temperature"),("Brenntag","distributor — trial viscosity unreadable"),("Piedmont Chemical Industries","High Point, NC — reserve"),("APV Engineered Coatings","Akron, OH — reserve")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+"  "; r.font.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text="— "+v; r2.font.size=Pt(9.5); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(2)
p=tf.add_paragraph(); par(p,"Acronyms",12,NAVY,bold=True,after=3); p.space_before=Pt(6)
for k,v in [("PVA","polyvinyl alcohol"),("cP","centipoise — viscosity unit"),("CoA","Certificate of Analysis"),("SQA","Supplier Quality Agreement"),("QMSR","FDA Quality Management System Regulation"),("GHTF","Global Harmonization Task Force"),("HBR","Harvard Business Review")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+"  "; r.font.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text="— "+v; r2.font.size=Pt(9.5); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(2)
tf=box(s,0.6,6.85,12.1,0.45); par(tf.paragraphs[0],"Full model: PVA_Second_Supplier_Leadership_Model.xlsx — every input editable, including the supplier minimum.",9,GREY,italic=True)

# ================= SPEAKER NOTES =================
NOTES = [
 "One supply-risk item, one decision. Four parts: was a second supplier even feasible; what it costs; what running two would look like day to day, including what we owe the candidate; and the decision itself.",
 "Feasibility. Two things limited the field. First, temperature: this PVA only dissolves with a 30 to 45 minute hold at 90 to 95 degrees C, and most toll blenders cannot get there - ArroChem, ILC Dover and Columbus Chemical all failed on that alone. Second, expertise: getting through the gate is not the same as making the product. Brenntag's trial came back with viscosity too high to read; PCI's first batch was more than double our target until we found the solids root cause. Then cost and fit: the one quote through the gate was eleven times SNP, and everyone viable needs at least a drum a week. The point: SNP is not just cheap - it is one of very few shops that can make this at all.",
 "Cost, part one - where every number comes from, because you will be asked. The material floor is 16 to 20 cents a pound - resin at market price times 11 percent solids. SNP's 75 cents is a real quote. The market range - 85 cents, a dollar forty, two fifty-five - is built bottom-up from resin, labor, QC and freight, with the high end anchored by a retail comparable. PCI's 2.50 to 5 dollars is our forecast, not their number. CJB's 8.42 is real, and it is an outlier. Why does a new supplier cost more? Because conversion cost is fixed per batch, and spread over one drum that alone is one to two dollars a pound. Why is SNP cheap? Specialization: it is their product line, and they have tank sizes that fit our batch - so the fixed cost per pound stays low.",
 "Cost, part two - what it means for us. Each bar is the extra we pay per year at one drum a week. PCI at 2.50 to 5 dollars: 41 to 99 thousand a year - roughly today's entire PVA bill again, every year, growing with volume. Five years: 242 to 588 thousand. There is no smaller version of this, because a drum a week is the least any supplier will take. And if SNP re-prices the volume it keeps, add a few thousand more.",
 "Cost, part three - the upside case, because it changes everything. Everything so far assumed a non-specialist price. But the market base is a dollar forty, so a capable shop at one to two-fifty is plausible. At a dollar to a dollar fifty the premium is 6 to 18 thousand a year and it pays off against almost any outage - that is the July plan, as described. At two dollars it is borderline. At two-fifty it needs a big outage cost. So the opportunity cost of not looking is real: we could be leaving cheap insurance on the table, plus a live price reference on SNP. And finding out is free - an RFQ to PCI on the spec we have already agreed, about two weeks.",
 "Logistics. With an 18 to 30 day shelf life nothing is stockpiled - every drum is made to order from both suppliers, and because drums arrive already aged, our real time-to-survive is one to one-and-a-half weeks, not two and a half. One check we have not done: whether SNP and PCI cook the same producer's resin - if so, a second cooker hedges cooking, not resin, and the resin buffer is the hedge either way. And the cheapest lever of all under either option is a validated 30-to-45-day shelf-life study. That means one harmonized spec and one viscometer method, an incoming test on every lot from both, lot traceability so we can see hydrogel performance by source, two cleaning procedures, two quality agreements. It is manageable, but it is a permanent discipline. And one thing it needs that we do not yet have: a written ramp plan for PCI. Without that, the second source cannot actually cover an outage - two-thirds of our volume still stops.",
 "The PCI question - because it is a fair one. They have put months of unpaid engineering into a small account. If we deem them capable and then do not buy, the realistic outcomes are that they decline to re-engage, deprioritize us, or demand paid development and a commitment next time. That is a real soft cost of Option B that the spreadsheet does not show. The honest way to handle it: decide before the next round of free experiments; if we lean B, be transparent about the triggers and pay for the work done - about the same 15 thousand any second source would cost to qualify; if we lean A, commit to the drum a week now.",
 "The decision. A costs about 70 thousand a year at the mid price and buys recovery in weeks - if the ramp plan is real. B costs almost nothing and leaves us exposed for months if SNP fails. A pays off only if a six-month outage would cost us more than about 700 thousand at a 10 percent annual risk, or 1.4 million at 5 percent. My recommendation, in order: first, price discovery - get PCI's real number, it is free and it decides this; at or below a dollar fifty we go to A, at two-fifty and above we stay B unless the outage cost is large, and in between the outage number decides. Second, either way, strengthen SNP now. Third, if it is B, settle with PCI honestly. Three asks: the outage-cost number from Finance and Ops - per hydrogel SKU, trailing revenue, contribution margin, and how much demand would be deferred versus lost; if they will not commit, two yes-or-no answers place us on the table: is a six-month stop more or less than a million dollars, more or less than three; the go-ahead to get PCI's price now; and approval to formalize SNP. LIKELY QUESTIONS. One: 'In July you said six to twelve thousand; now it is seventy.' Both were honest: July assumed a dollar to a dollar twenty-five and a share no supplier will accept; this is the same plan at real prices - and if PCI comes in at a dollar fifty, July's number is back. Two: 'If SNP burns down tomorrow, what actually happens?' Today, production stops for six to twelve months. Under A with a signed ramp, a gap of two to six weeks. Under B with the resin buffer and the cold-start kit, months rather than a year. No option closes the gap without PCI's written capacity commitment - which is why getting it is step one. Three: 'Why not just pay the seventy thousand - it is a rounding error against the device line?' Because at that price it covers a third of supply, not all of it; it drops us below one percent of SNP's revenue at the moment we want first call on their capacity and innovation; and standing risk lines are the first thing cut in a budget cycle - nearly half of companies in McKinsey's 2024 survey were cutting risk buffers. If the outage cost clears the break-even, we pay it; the triggers make that automatic.",
 "Assumptions, sources, suppliers by full name, and acronyms. The model is in the workbook; every input is editable, including the supplier minimum.",
]
for sl, txt in zip(prs.slides, NOTES): sl.notes_slide.notes_text_frame.text = txt

prs.save("PVA_Second_Supplier_Leadership_Deck.pptx"); print("saved deck:", len(prs.slides._sldIdLst), "slides")
