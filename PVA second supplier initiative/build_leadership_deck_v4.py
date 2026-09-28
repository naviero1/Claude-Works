#!/usr/bin/env python3
"""Leadership deck v4: PCI's real quote ($3.50/lb at 5-drum batches; $6 below) — comparison, logistics, strategy propositions, decision timing."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

NAVY=RGBColor(0x1F,0x38,0x64); STEEL=RGBColor(0x4E,0x79,0xA7); GREY=RGBColor(0x59,0x59,0x59)
WHITE=RGBColor(0xFF,0xFF,0xFF); GREEN=RGBColor(0x2E,0x7D,0x46); RED=RGBColor(0xB2,0x3A,0x2E)
AMBER=RGBColor(0x9C,0x5A,0x0C); LIGHT=RGBColor(0xEE,0xF2,0xF7); PALE=RGBColor(0xF6,0xF8,0xFB)
LGREEN=RGBColor(0xE2,0xEF,0xDA); LRED=RGBColor(0xFC,0xE4,0xD6); LAMB=RGBColor(0xFF,0xF2,0xCC)

import json, os
TIERS=json.load(open("market_tiers.json")) if os.path.exists("market_tiers.json") else {}
def T(k): return (f"${TIERS[k]:.2f}" if TIERS.get(k) is not None else "pending")
def TR(k): return TIERS.get(k+"_range","—")
def TN(k): return TIERS.get("n_"+k,"—")
prs=Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
BLANK=prs.slide_layouts[6]
def slide(): return prs.slides.add_slide(BLANK)
def rect(s,l,t,w,h,fill,line=None):
    sp=s.shapes.add_shape(MSO_SHAPE.RECTANGLE,Inches(l),Inches(t),Inches(w),Inches(h)); sp.fill.solid(); sp.fill.fore_color.rgb=fill
    if line: sp.line.color.rgb=line; sp.line.width=Pt(0.75)
    else: sp.line.fill.background()
    sp.shadow.inherit=False; return sp
def box(s,l,t,w,h):
    tf=s.shapes.add_textbox(Inches(l),Inches(t),Inches(w),Inches(h)).text_frame; tf.word_wrap=True; return tf
def par(p,text,size,color=NAVY,bold=False,italic=False,align=PP_ALIGN.LEFT,after=4):
    p.text=text; p.alignment=align; p.space_after=Pt(after)
    r=p.runs[0]; r.font.size=Pt(size); r.font.color.rgb=color; r.font.bold=bold; r.font.italic=italic; r.font.name="Calibri"; return p
def title_bar(s,text,section=None):
    rect(s,0,0,13.333,1.0,NAVY); tf=box(s,0.5,0.14,10.6,0.8); par(tf.paragraphs[0],text,25,WHITE,bold=True)
    if section: tf=box(s,10.9,0.3,2.2,0.5); par(tf.paragraphs[0],section,11,RGBColor(0xBD,0xD7,0xEE),align=PP_ALIGN.RIGHT)
def bullets(s,l,t,w,h,items,size=13,gap=8,color=GREY):
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
def card(s,l,t,w,h,value,label,vcolor=NAVY,fill=LIGHT,vsize=22):
    rect(s,l,t,w,h,fill); tf=box(s,l+0.12,t+0.1,w-0.24,h-0.2); tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    par(tf.paragraphs[0],value,vsize,vcolor,bold=True,align=PP_ALIGN.CENTER,after=2); par(tf.add_paragraph(),label,10.5,GREY,align=PP_ALIGN.CENTER)
def takeaway(s,text,t=6.55,fill=NAVY,color=WHITE,size=13.5):
    rect(s,0.6,t,12.1,0.62,fill); tf=box(s,0.8,t+0.08,11.7,0.5); tf.vertical_anchor=MSO_ANCHOR.MIDDLE; par(tf.paragraphs[0],text,size,color,bold=True)
def table(s,l,t,w,h,rows,colw,size=11,fills=None):
    tbl=s.shapes.add_table(len(rows),len(rows[0]),Inches(l),Inches(t),Inches(w),Inches(h)).table
    for i,cw in enumerate(colw): tbl.columns[i].width=Inches(cw)
    for ri,row in enumerate(rows):
        for ci,val in enumerate(row):
            c=tbl.cell(ri,ci); c.text=str(val); p=c.text_frame.paragraphs[0]
            p.alignment=PP_ALIGN.LEFT if ci==0 or (len(row)>3 and ci==len(row)-1) else PP_ALIGN.CENTER
            r=(p.runs[0] if p.runs else p.add_run()); r.font.size=Pt(size); r.font.name="Calibri"; c.fill.solid()
            if ri==0: r.font.bold=True; r.font.color.rgb=WHITE; c.fill.fore_color.rgb=NAVY
            else:
                r.font.color.rgb=NAVY; c.fill.fore_color.rgb=(fills[ri][ci] if fills and fills[ri] and fills[ri][ci] else WHITE)
                if ci==0: r.font.bold=True
    return tbl
def panel(s,l,t,w,h,title,items,tcolor,fill,size=11.5):
    rect(s,l,t,w,h,fill); tf=box(s,l+0.2,t+0.13,w-0.4,h-0.26); par(tf.paragraphs[0],title,13.5,tcolor,bold=True,after=6)
    for it in items: par(tf.add_paragraph(),"•  "+it,size,GREY,after=5)
    return tf

# ===== 1 TITLE =====
s=slide(); rect(s,0,0,13.333,7.5,NAVY); rect(s,0,4.85,13.333,0.06,STEEL)
tf=box(s,0.8,1.5,11.7,2.9); par(tf.paragraphs[0],"Liquid PVA: One Supplier or Two?",40,WHITE,bold=True)
par(tf.add_paragraph(),"Update: PCI Manufacturing has proven it can make our product — and told us what it costs",20,RGBColor(0xBD,0xD7,0xEE))
tf=box(s,0.8,5.1,11.7,1.6)
par(tf.paragraphs[0],"PVA = polyvinyl alcohol — the liquid we buy in 55-gallon drums from SNP Inc. (Durham, NC) to make our hydrogels. Sole-sourced today.",13.5,WHITE)
par(tf.add_paragraph(),"Oscar Penny  ·  Supply Chain  ·  28 September 2026  ·  Decision requested",12,RGBColor(0x9D,0xC3,0xE6))

# ===== 2 OUTLINE =====
s=slide(); title_bar(s,"Outline — what each slide establishes","OUTLINE")
rows=[["#","Slide","What it establishes"],
 ["3","What changed","PCI Manufacturing's experiment succeeded; their real quote is $3.50/lb at 5-drum batches ($6.00 below a batch); a decision is due before our next SNP Inc. conversation"],
 ["4","Price per pound, side by side","The market price of comparable pre-mixed PVA solutions at competitive, low and high quantities (verified study), then the four real quotes: SNP, PCI per batch, PCI below batch, CJB"],
 ["5","Annual cost, side by side","What each option adds to today's $50.7k: +$62k/yr for PCI at one-third; +$123k at the below-batch price; five-year and break-even"],
 ["6","The PCI experiment — a success, at what cost","What was proven, what PCI invested, what that knowledge is worth, and the standing price of using it vs. the price of walking away"],
 ["7","What 5-drum batches mean operationally","Block rotation under an 18-day shelf life: 12 days on 100% PCI material, then SNP; lumpy demand to SNP; the control needed; the 30-day shelf-life lever"],
 ["8","Strategy propositions","A: commit one-third now · B: strengthen SNP Inc., keep PCI as a dated option · B-plus: one production batch, then B — cost, what each buys, effect on both suppliers"],
 ["9","Keeping a qualified supplier you don't use","How it is done: paid qualification, a no-minimum master agreement, one production batch, a readiness fee, planned re-checks — and the conduct that keeps the relationship intact"],
 ["10","Why decide now","The posture for our next SNP Inc. conversation must match the decision; what to settle in that conversation under each option; what not to do"],
 ["11","Recommendation & asks","B-plus with the existing triggers unless Finance's outage cost clears the break-even; the three things we need from leadership"],
 ["12","Appendix","Assumptions, suppliers by full name, acronyms, frameworks (fact-checked)"]]
table(s,0.6,1.2,12.1,5.25,rows,[0.5,3.0,8.6],size=10)
takeaway(s,"Sequence: feasibility is settled → cost is now real → logistics are specific → strategy → timing → decision.")

# ===== 3 WHAT CHANGED =====
s=slide(); title_bar(s,"What changed: the experiment worked, and we have a real price","1 · WHAT CHANGED")
card(s,0.6,1.2,3.95,1.45,"Spec met","PCI Manufacturing's production experiment hit 11% solids / 900–1,100 cP",vcolor=GREEN,fill=LGREEN)
card(s,4.7,1.2,3.95,1.45,"$3.50 / lb","real quote — one batch of 5 drums (2,250 lb); $6.00/lb for anything smaller",vcolor=NAVY)
card(s,8.8,1.2,3.9,1.45,"Decide now","before our next SNP Inc. conversation — the posture must match the decision",vcolor=AMBER,fill=LAMB)
bullets(s,0.6,2.9,12.1,3.5,[
 ("The capability question is closed. ","Six months and 94 suppliers produced one shop that can hold the 90–95 °C cook and make the product to spec: PCI Manufacturing (St. Louis, MO; CMS Manufacturing group). Viscosity root cause found, spec agreed, batch met it."),
 ("The price question is closed too. ","$3.50/lb sits exactly where the forecast mid-case was ($3.75), so the economics we showed last week hold. The $6.00 below-batch price removes any small-volume version: it is one-third of demand in 5-drum batches, or nothing."),
 ("The batch size is the new fact. ","5 drums = 12 days of full demand. With an 18-day shelf life the drums must be used at full rate on receipt — which shapes the logistics (slide 7) and what SNP Inc. would experience."),
 ("Still to confirm with PCI: ","delivered and all-in (materials, drum, freight)? quote validity? ~10 batches a year on a ~5-week rhythm? crisis ramp to ~3 batches a month? which resin producer they use (sub-tier overlap with SNP)?"),
],size=12.5,gap=8)
takeaway(s,"We now know it can be done and what it costs. The open question is strategy — and it has a deadline.")

# ===== 4 PRICE SIDE BY SIDE =====
s=slide(); title_bar(s,"Price per pound, side by side — and where each number comes from","2 · COST")
s.shapes.add_picture("chart_price_side_by_side.png",Inches(0.6),Inches(1.15),width=Inches(8.1))
rect(s,8.95,1.15,3.75,5.2,PALE,STEEL); tf=box(s,9.1,1.25,3.5,5.05)
par(tf.paragraphs[0],"Where each number comes from",13,NAVY,bold=True,after=5)
for k,v in [(f"Market, competitive quantity {T('competitive')}",f"comparable pre-mixed PVA solutions at drum scale; range {TR('competitive')}, n={TN('competitive')} — verified against vendor pages"),
            (f"Market, low quantity {T('low')}",f"small packs (pints to 5-gal); range {TR('low')}, n={TN('low')} — retail margin and packaging"),
            (f"Market, high quantity {T('high')}",f"totes / bulk / tonnage; range {TR('high')}, n={TN('high')} — different quality and regulatory context"),
            ("SNP Inc. $0.75","real quote (Estimate 012726-1), delivered all-in — a specialist's price"),
            ("PCI $3.50 / $6.00","real quote, 28 Sept: one 5-drum batch / anything smaller"),
            ("CJB $8.42","real quote: $8.00–8.50 toll excluding materials, plus resin; eliminated")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+"  "; r.font.bold=True; r.font.size=Pt(10.5); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text="— "+v; r2.font.size=Pt(10); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(6)
p=tf.add_paragraph(); par(p,"Why a non-specialist is far above the competitive market: batch-fixed conversion cost spread over few pounds, drum-scale freight, and risk priced in. SNP Inc.'s tanks are right-sized to our order and PVA cooking is their core line.",10,NAVY,bold=True); p.space_before=Pt(4)
takeaway(s,f"At competitive quantity the market sells comparable PVA solution around {T('competitive')}/lb. SNP Inc. is below it; PCI is well above it; CJB is off the scale.")

# ===== 5 ANNUAL COST SIDE BY SIDE =====
s=slide(); title_bar(s,"Annual cost, side by side — what each option adds to today's $50.7k","2 · COST")
s.shapes.add_picture("chart_annual_side_by_side.png",Inches(0.6),Inches(1.15),width=Inches(8.1))
rect(s,8.95,1.15,3.75,5.2,PALE,STEEL); tf=box(s,9.1,1.25,3.5,5.05)
par(tf.paragraphs[0],"Reading the chart",13,NAVY,bold=True,after=5)
for k,v in [("A at $3.50 (1/3, 10 batches/yr)","$112.6k total → +$61.9k/yr, 122% of today's spend"),
            ("A at $6.00 (1 drum/week)","$173.6k → +$123k/yr — the small-order version is the expensive one"),
            ("Five years (+10%/yr volume)","~$378k premium at $3.50 (undiscounted)"),
            ("One-time","~$15k qualification placeholder — largely already spent in engineering hours"),
            ("Break-even","pays only if a 6-month SNP Inc. outage costs > ~$620k (10%/yr risk) or ~$1.24M (5%)"),
            ("Not shown","if SNP Inc. re-prices the ~2/3 it keeps (+10–20%): add $3–7k/yr")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+"  "; r.font.bold=True; r.font.size=Pt(10.5); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text="— "+v; r2.font.size=Pt(10); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(6)
takeaway(s,"A second source at PCI's price roughly doubles the PVA bill every year. That is the real cost of the insurance — no longer a forecast.")

# ===== 6 PCI EXPERIMENT =====
s=slide(); title_bar(s,"The PCI experiment: a success — at what cost?","3 · PCI")
panel(s,0.6,1.2,5.95,2.55,"What was proven, and what it is worth",
 ["Capability: the 90–95 °C cook, no fisheyes, viscosity on target after the solids root cause was found; spec (11% / 900–1,100 cP) agreed and met",
  "A qualified-capable, quoted alternative now exists. Even if we never order, a cold start drops from 6–12 months to roughly 2–3: the spec, the process and a willing supplier are known",
  "The one thing not yet proven at scale: hydrogel performance on 100% PCI material, and rate production"],GREEN,LGREEN,11)
panel(s,6.75,1.2,5.95,2.55,"What it cost — and who paid",
 ["PCI Manufacturing: two-plus lab batches, a dilution study, method alignment, a revised process — months of unpaid engineering on a ~$50k/yr account",
  "Us: ~6 months of sourcing and lab time (the $15k qualification placeholder is largely this)",
  "Still queued at PCI's expense unless we decide: the shelf-life study and the hydrogel comparison"],AMBER,LAMB,11)
panel(s,0.6,3.9,5.95,2.45,"The standing price of using it",
 ["+$62k/yr at one-third, growing with volume (~$378k over five years)",
  "Plus a permanent operating discipline: two specs, two Certificate-of-Analysis (CoA) streams, block rotation, two relationships",
  "Plus what it does to SNP Inc.: a third less volume, delivered in lumps"],RED,LRED,11)
panel(s,6.75,3.9,5.95,2.45,"The price of walking away — and a middle",
 ["Goodwill: a supplier that did months of free work and got nothing may not re-engage, or will require paid development and commitments next time",
  "Middle: buy ONE 5-drum production batch (~$7.9k; ~$6.2k premium; ~3% of annual volume). It finishes the qualification at scale, pays PCI with a real order, and is invisible to SNP Inc.'s year",
  "Either way: be candid, and stop consuming free experiments once decided"],NAVY,LIGHT,11)
takeaway(s,"The experiment bought us certainty. Whether we buy the product is a separate decision — and it now has a real price on both sides.")

# ===== 7 LOGISTICS OF 5-DRUM BATCHES =====
s=slide(); title_bar(s,"What 5-drum batches mean operationally","4 · LOGISTICS")
rect(s,0.6,1.2,12.1,1.55,LIGHT); tf=box(s,0.8,1.3,11.7,1.4)
par(tf.paragraphs[0],"Block rotation, every ~5 weeks (at one-third of demand, 18-day shelf life)",13,NAVY,bold=True,after=4)
par(tf.add_paragraph(),"Days 1–12: all production on PCI material (5 drums = 2,250 lb = 12 days at full rate — must be consumed before day 18)   →   Days 13–36: all production on SNP Inc. material (~10 drums)   →   repeat. 10 PCI batches a year.",11.5,GREY,after=3)
par(tf.add_paragraph(),"Why not blend at a one-third rate? A batch consumed at two-thirds rate takes 18.2 days — over the shelf life. A validated 30-day life would allow it, and would let SNP Inc. keep supplying at a reduced rate during a PCI batch instead of pausing.",11,NAVY,bold=True)
panel(s,0.6,2.9,3.95,3.5,"What it does to SNP Inc.",
 ["Loses a third of volume ($50.7k → $33.8k) — and gets it in lumps: a ~12-day gap every ~5 weeks",
  "Lumpy demand is worse for a small specialist than a steady reduced share: idle kettle time, harder resin planning",
  "Our account falls below ~1% of their revenue at the moment we want first call on capacity and innovation"],RED,LRED,10.5)
panel(s,4.7,2.9,3.95,3.5,"What we would have to run",
 ["One harmonized spec and ONE viscometer method; incoming test on every lot from both; lot traceability by source; hydrogel performance tracked by supplier",
  "Five drums on site at once: storage, temperature, strict first-in-first-out inside 12 days",
  "Two cleaning procedures (PCI's residual-film issue is open); two Supplier Quality Agreements; R&D and Quality time for equivalence and CAPA across two streams"],AMBER,LAMB,10.5)
panel(s,8.8,2.9,3.9,3.5,"What it buys — if the ramp is real",
 ["Recovery in weeks if SNP Inc. fails — provided PCI confirms in writing it can go from 1 batch every 5 weeks to ~3 a month",
  "Until then, ~2/3 of volume still stops in an outage",
  "Sub-tier check: if PCI cooks the same producer's resin as SNP, a second cooker hedges cooking, not resin — buffer the shelf-stable resin either way"],GREEN,LGREEN,10.5)
takeaway(s,"Two suppliers is workable — as a permanent discipline, with lumpy demand to SNP Inc. unless we validate a longer shelf life.")

# ===== 8 STRATEGY PROPOSITIONS =====
s=slide(); title_bar(s,"Strategy propositions","5 · STRATEGY")
rows=[["","A · Commit one-third now","B · Single source, strengthened","B-plus · One batch, then B"],
 ["What it is","10 PCI batches/yr in block rotation; SNP Inc. keeps ~2/3","SNP Inc. sole source with continuity terms, forecast sharing, resin buffer, financial check; PCI kept as a dated, quoted option; pay for the work done","Buy one 5-drum production batch now to finish qualification at scale, then run B with a fully qualified alternative on file"],
 ["Cost","+$62k/yr, ~$378k / 5 yrs, + ~$15k one-time","~$3–12k/yr + ~$5–10k one-time; ~$15k settlement with PCI","~$7.9k once (+$6.2k premium) + B's costs"],
 ["What it buys","A practiced second source; recovery in weeks if the ramp is confirmed","Deeper partnership; documented continuity; cold start ~2–3 months given what we now know","Everything B buys, plus proven rate and hydrogel performance on 100% PCI material, and a supplier paid with a real order"],
 ["Effect on SNP Inc.","−1/3 volume, lumpy; relationship strain at the wrong moment","Strengthened; capacity headroom and succession tested","Unchanged (one batch ≈ 3% of a year)"],
 ["Effect on PCI","Engaged and paid","Goodwill at risk unless settled candidly","Paid, qualified, and told the triggers honestly"],
 ["Residual risk","~2/3 exposed until ramp; SNP re-price; two-stream quality load","SNP failure still means months, not weeks","Same as B, with a shorter restart"]]
fills=[None]+[[None,LRED,LGREEN,LAMB] for _ in range(6)]
table(s,0.6,1.2,12.1,5.1,rows,[1.6,3.4,3.55,3.55],size=9.8,fills=fills)
takeaway(s,"B-plus converts six months of experiments into a standing, paid-for option for ~$8k — without touching SNP Inc.'s volume.",fill=GREEN)

# ===== 8b KEEPING A QUALIFIED SUPPLIER YOU DON'T USE =====
s=slide(); title_bar(s,"Keeping a qualified supplier you don't use — how it is done","5 · STRATEGY")
tf=box(s,0.6,1.15,12.1,0.6); par(tf.paragraphs[0],"Medical-device, pharma and aerospace buyers do this routinely. What spoils the relationship is not the 'no' — it is silence and unpaid work. Five instruments, in rising order of commitment:",12.5,NAVY,bold=True)
rows=[["Instrument","What it is","Cost here","What it does for the relationship"],
 ["1 · Pay for the qualification (NRE — non-recurring engineering)","We fund the qualification lots, testing and documentation already done","~$15k (the value of PCI's work)","Turns free experiments into a paid development engagement they can justify internally; leaves an approved-source file"],
 ["2 · Master supply agreement, no volume commitment","Price ($3.50, resin-indexed), spec, lead time, quality and change-notification terms; valid 12–24 months; zero minimum","Legal time","Formal 'approved second source' status for them; a callable option at a known price for us"],
 ["3 · One production-scale order (B-plus)","A single paid 5-drum batch: proves rate and hydrogel performance, completes the file","~$7.9k (+$6.2k over SNP)","Strongest form — they have shipped to us; revenue for their work"],
 ["4 · Readiness / capacity-reservation fee","An option contract: a fee for the right to call volume at a set price with a committed ramp (pharma: ~20% of forecast batch value; multi-million minimums)","Token retainer at most","Rarely worth it at our scale; mention only if PCI raises it"],
 ["5 · Planned re-check (decay is real)","Idle suppliers go stale: PPAP re-approval after 12 months idle; ~18 months idle = 'new supplier again'; ISO 13485 §7.4.1 periodic re-evaluation","One 5-drum re-check batch/yr ≈ $7.9k, or a short requalification lot on restart","Keeps the option honest; restart in weeks, not months"]]
fills=[None,None,None,[None,LGREEN,LGREEN,LGREEN],None,None]
table(s,0.6,1.85,12.1,3.55,rows,[2.9,3.9,2.1,3.2],size=9.6,fills=fills)
panel(s,0.6,5.55,12.1,0.95,"Conduct that keeps it intact",
 ["Tell PCI Manufacturing the volume reality and the exact triggers · pay promptly for value received · share the test results (they learn too) · a quarterly touchpoint · a reference. Suppliers allocate goodwill on trust, long-term orientation and growth prospects — not on current volume (Pulles, Schiele et al. 2016)."],NAVY,LIGHT,10.5)
takeaway(s,"Not using a qualified supplier is normal. Pay for the work, sign the terms, state the triggers, re-check yearly — and the door stays open.",fill=GREEN)

# ===== 9 WHY DECIDE NOW =====
s=slide(); title_bar(s,"Why decide now","6 · TIMING")
bullets(s,0.6,1.2,6.6,5.1,[
 ("The next face-to-face with SNP Inc. is where the strategy becomes real. ","Continuity terms, forecast sharing, resin consignment, a resin-indexed price formula, capacity headroom for +10%/yr, succession and financial health — these get settled in a room, not by email."),
 ("The posture has to match the decision. ","We cannot deepen the partnership and quietly plan to move a third of their core line at the same time. And telling them after a warm visit reads as bait-and-switch."),
 ("If the answer is A: ","the volume conversation belongs in that meeting, face-to-face, with a steady-cadence proposal — not discovered later from the order pattern."),
 ("If the answer is B or B-plus: ","the meeting is the partnership meeting. Continuity planning is presented as a quality-system requirement, not a loss of confidence. PCI is not named; the quote is not waved. 'We have benchmarked the market' is fair context."),
],size=12.5,gap=9)
rect(s,7.5,1.2,5.2,5.1,PALE,STEEL); tf=box(s,7.7,1.35,4.8,4.9)
par(tf.paragraphs[0],"To settle with SNP Inc. under B / B-plus",13,NAVY,bold=True,after=6)
for it in ["Rolling 12-month forecast, refreshed monthly; the hydrogel program as a written joint roadmap",
           "Continuity terms in the Supplier Quality Agreement: second line/site plan, key-person cover, advance change notice, right to audit",
           "8–12 weeks of dry PVA resin on consignment (shelf-stable; ~$2.5–6k tied up)",
           "Their capacity headroom at year-5 volume (~99k lb) — the unasked question",
           "Owner/succession and financial health — the risk that gives no warning",
           "A 30–45-day shelf-life study — the cheapest way to lengthen our time-to-survive"]:
    par(tf.add_paragraph(),"•  "+it,11,GREY,after=6)
takeaway(s,"Decide the strategy first; then use the SNP Inc. conversation to execute it — not to discover it.",fill=AMBER)

# ===== 10 RECOMMENDATION & ASKS =====
s=slide(); title_bar(s,"Recommendation & asks","7 · DECISION")
panel(s,0.6,1.2,5.95,3.15,"Recommendation: B-plus, with the existing triggers",
 ["Order one 5-drum production batch from PCI Manufacturing now (~$7.9k): proves rate and hydrogel performance at scale, pays for the work, keeps the door open",
  "Go into the SNP Inc. conversation as a partner: continuity terms, forecast, resin consignment, capacity headroom, succession, shelf-life study",
  "Tell PCI the triggers candidly; refresh the cold-start kit annually"],GREEN,LGREEN,11)
panel(s,6.75,1.2,5.95,3.15,"Go to A (one-third, 10 batches/yr) if any trigger fires",
 ["Finance's outage estimate exceeds ~$620k (10%/yr risk) or ~$1.24M (5%)",
  "An SNP Inc. risk signal: capacity headroom short of year-5 volume, succession or financial stress, a missed lot, an unexplained price move",
  "PCI's price falls toward ~$1.50/lb, or a new hydrogel line makes PVA strategic, or SNP Inc. declines the partnership terms"],AMBER,LAMB,11)
rect(s,0.6,4.5,12.1,1.85,LIGHT); tf=box(s,0.8,4.6,11.7,1.7)
par(tf.paragraphs[0],"What we need from leadership",13,NAVY,bold=True,after=5)
for it in ["1.  The cost of a 6-month PVA outage — per hydrogel SKU: trailing revenue, contribution margin, deferrable vs lost demand (fallback: more or less than $1M? than $3M?)",
           "2.  The strategy call — A, B or B-plus — before the next SNP Inc. conversation",
           "3.  Approval to formalize SNP Inc. (continuity terms, forecast sharing, resin consignment) and, under B-plus, ~$8k for one PCI production batch"]:
    par(tf.add_paragraph(),it,11.5,GREY,after=5)
takeaway(s,"Keep the option alive for ~$8k, strengthen the source we depend on, and commit ~$62k/yr only when the evidence says so.")

# ===== 11 APPENDIX =====
s=slide(); title_bar(s,"Appendix: assumptions, suppliers, acronyms, frameworks")
rows=[["Assumption","Value","Basis"],
 ["Demand today","1,300 lb/wk ≈ 150 drums/yr; +10%/yr","Confirmed 2026-06-26; leadership growth assumption"],
 ["SNP Inc. price","$0.75/lb delivered = $337.50/drum","SNP Estimate 012726-1"],
 ["PCI Manufacturing price","$3.50/lb per 5-drum batch; $6.00/lb below a batch","Quote 2026-09-28 — confirm delivered/all-in, validity"],
 ["Second-source share","1/3 = 50 drums/yr = 10 batches of 5","Block rotation, ~5-week cycle"],
 ["Market reference","$0.85 / $1.40 / $2.55 per lb","Resin floor + labor build-up + retail ceiling"],
 ["CJB quote","$8.00–8.50/lb toll excl. materials ≈ $8.42 landed","CJB email 'RE: mix test'"],
 ["Qualification cost","~$15k one-time (placeholder)","Largely engineering hours already spent"],
 ["Outage cost","not yet estimated","NEEDED from Finance / Ops"]]
table(s,0.6,1.15,6.9,3.1,rows,[2.0,2.7,2.2],size=9)
tf=box(s,0.6,4.35,6.9,2.45)
par(tf.paragraphs[0],"Frameworks (independently fact-checked)",11,NAVY,bold=True,after=3)
par(tf.add_paragraph(),"Kraljic (HBR 1983), bottleneck items: 'Volume insurance (at cost premium if necessary). Control of vendors. Security of inventories. Backup plans' — pay for a backup when the premium is proportionate. Gelderman & van Weele (2003): 'hold' vs 'move' — move only when economically worthwhile. Simchi-Levi et al. (Interfaces 2015): disruption impact is uncorrelated with spend. Sheffi & Rice (MIT SMR 2005): single sourcing is legitimate only with a deep, managed relationship. Tomlin (2006); Chopra & Sodhi (2014): assuming zero disruption probability is the expensive mistake. Pulles, Schiele et al. (2016): preferential treatment follows attractiveness, not volume. Deloitte CPO 2025: 'active alternative sources' rated most effective (74%). QMSR / ISO 13485 §7.4 / GHTF N17: controls proportionate to risk — no second source required. Six research lenses; four refuted claims excluded; memo in the repo.",8.5,GREY)
rect(s,7.75,1.15,4.95,5.65,PALE,STEEL); tf=box(s,7.9,1.22,4.7,5.55)
par(tf.paragraphs[0],"Suppliers named",12,NAVY,bold=True,after=3)
for k,v in [("SNP Inc.","Durham, NC — incumbent, sole source"),("PCI Manufacturing","St. Louis, MO — CMS Manufacturing group; qualified-capable, quoted"),("CJB Applied Technologies","Valdosta, GA — quoted ~11×; eliminated"),("ArroChem Inc.","Mount Holly, NC — 85 °C ceiling"),("ILC Dover","Frederica, DE — could not hold temperature"),("Columbus Chemical Industries","Columbus, WI — could not hold temperature"),("Brenntag","distributor — trial viscosity unreadable"),("Piedmont Chemical Industries","High Point, NC — reserve"),("APV Engineered Coatings","Akron, OH — reserve")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+"  "; r.font.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text="— "+v; r2.font.size=Pt(9.5); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(2)
p=tf.add_paragraph(); par(p,"Acronyms",12,NAVY,bold=True,after=3); p.space_before=Pt(6)
for k,v in [("PVA","polyvinyl alcohol"),("cP","centipoise — viscosity unit"),("CoA","Certificate of Analysis"),("SQA","Supplier Quality Agreement"),("CAPA","corrective and preventive action"),("QMSR","FDA Quality Management System Regulation"),("GHTF","Global Harmonization Task Force"),("HBR / MIT SMR","Harvard Business Review / MIT Sloan Management Review")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+"  "; r.font.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text="— "+v; r2.font.size=Pt(9.5); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(2)
tf=box(s,0.6,6.85,7.0,0.45); par(tf.paragraphs[0],"Workbook: PVA_Second_Supplier_Leadership_Model.xlsx — tabs 'Supplier Quotes', 'PCI Quote Scenarios', 'PCI Experiment' hold the compiled data.",9,GREY,italic=True)

# ===== SPEAKER NOTES =====
NOTES=[
 "Update on the liquid PVA decision. Since last time, two things happened: PCI Manufacturing's production experiment met our spec, and they gave us a real price. Today I want to show the cost side by side, be honest about what the experiment cost and is worth, walk through what running two suppliers would actually look like, and then put three strategy propositions in front of you - because we need to choose one before our next conversation with SNP.",
 "The outline. Feasibility is settled, cost is now real, logistics are specific, then strategy, timing and the decision. Each slide establishes one thing.",
 "What changed. First, the capability question is closed: PCI hit 11 percent solids and the viscosity window after we found the solids root cause together. Second, the price question is closed: 3.50 a pound for a five-drum batch, and 6 dollars for anything smaller - so there is no small version; it is a third of demand in five-drum batches, or nothing. Third, the batch size is the new fact: five drums is twelve days of our full demand, and with an eighteen-day shelf life those drums have to be used at full rate as soon as they land. A few things to confirm with PCI: whether 3.50 is delivered and all-in, how long the quote is valid, whether they will accept about ten batches a year on a five-week rhythm, whether they could ramp to three batches a month in a crisis, and which resin producer they use.",
 "Price per pound, side by side. Green is SNP's real quote at 75 cents - a specialist's price. Navy and red are PCI's real numbers: 3.50 for a batch, 6 for anything smaller. Red on the far right is CJB, for scale. Grey bars are our market references, built from the resin floor plus labor plus freight, with a retail comparable at the top. Amber is the July assumption - it is superseded. The point: PCI's real number landed right on the mid-case of the range we modelled. The market work was right; the July number was not.",
 "Annual cost side by side. Today: 50.7 thousand, all SNP. PCI at a third in five-drum batches: 112.6 thousand, so plus 62 thousand a year - 122 percent of today's whole bill. PCI at one drum a week at the below-batch price: 173.6 thousand - the small-order version is the expensive one. Five years at ten percent growth: about 378 thousand of premium. Break-even: the second source pays only if a six-month SNP outage would cost us more than about 620 thousand at a ten percent annual risk, or 1.24 million at five percent. I still need that outage number from Finance.",
 "The experiment. What it proved: the cook, the viscosity control, the spec. What it is worth: even if we never order, a cold start is now two to three months instead of six to twelve, because the spec, the process and a willing supplier are known. What it cost: PCI put months of unpaid engineering into a fifty-thousand-dollar account; we put six months of sourcing and lab time in. The standing price of using it is 62 thousand a year plus a permanent operating discipline plus what it does to SNP. The price of walking away is goodwill. And there is a middle: one five-drum production batch, about 7,900 dollars, finishes the qualification at scale, pays PCI with a real order, and is invisible to SNP's year.",
 "Logistics. With five-drum batches and an eighteen-day shelf life, we cannot blend PCI at a one-third rate - a batch consumed at two-thirds rate takes eighteen days, over the limit. So it is block rotation: twelve days on PCI material at full rate, then about three and a half weeks on SNP, repeat every five weeks. For SNP that means losing a third of volume and getting the rest in lumps with a twelve-day gap - worse for a small specialist than a steady reduced share. For us: one spec, one viscometer method, incoming test on every lot, five drums on site at once, strict first-in-first-out, two cleaning procedures, two quality agreements. What it buys - recovery in weeks - only if PCI confirms in writing that they can ramp. And a validated thirty-day shelf life would soften all of this.",
 "Three strategy propositions. A: commit a third now - 62 thousand a year, a practiced second source, but lumpy demand to SNP and relationship strain at the wrong moment. B: single source, strengthened - a few thousand a year, deeper partnership, PCI kept as a dated option and paid for the work done; SNP failure still means months. B-plus: one production batch now, about 8 thousand, then B - everything B buys plus proven rate and hydrogel performance on pure PCI material, a supplier paid with a real order, and SNP untouched. B-plus is my recommendation.",
 "How companies keep a qualified supplier they do not use - because you will be asked whether B-plus is realistic. It is routine in medical devices, pharma and aerospace. What spoils the relationship is silence and unpaid work, not the 'no'. The instruments, in rising order of commitment: pay for the qualification work already done; sign a master agreement with price, spec and terms but no volume commitment; place one production-scale order; a readiness fee, which is rare at our scale; and a planned re-check, because an idle supplier goes stale after about a year. And the conduct: tell PCI the triggers, pay promptly, share results, keep a quarterly touchpoint. The research is clear that suppliers allocate goodwill on trust and growth prospects, not current volume.",
 "Why decide now. Our next face-to-face with SNP is where the strategy becomes real - continuity terms, forecast sharing, resin consignment, capacity headroom, succession. The posture has to match the decision: we cannot deepen the partnership while quietly planning to move a third of their core line, and telling them after a warm visit reads as bait-and-switch. If the answer is A, the volume conversation belongs in that meeting, face to face, with a steady-cadence proposal. If it is B or B-plus, that is the partnership meeting: continuity planning framed as a quality-system requirement, PCI not named, the quote not waved. Decide first; use the meeting to execute, not to discover.",
 "Recommendation: B-plus with the existing triggers. Order one production batch from PCI now; go into the SNP conversation as a partner and settle the six items on the previous slide; tell PCI the triggers candidly. Switch to A if Finance's outage number clears the break-even, if SNP shows a risk signal - capacity, succession, finances, a missed lot - if PCI's price falls toward a dollar fifty, or if SNP declines the terms. Three asks: the outage-cost number, per hydrogel SKU; the strategy call before the SNP conversation; and approval to formalize SNP plus about 8 thousand for one PCI batch.",
 "Assumptions, suppliers by full name, acronyms, and the fact-checked frameworks. The workbook holds every number: the Supplier Quotes tab, PCI Quote Scenarios, and the PCI Experiment record.",
]
for sl,txt in zip(prs.slides,NOTES): sl.notes_slide.notes_text_frame.text=txt
prs.save("PVA_Second_Supplier_Leadership_Deck.pptx"); print("saved deck:",len(prs.slides._sldIdLst),"slides")
