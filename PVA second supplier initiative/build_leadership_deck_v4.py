#!/usr/bin/env python3
"""Leadership deck v4.3 (10 slides; outline and pre-quote slides removed — outline is worked in conversation): PCI's real quote ($3.50/lb at 5-drum batches; $6 below) — chronology, side-by-side cost, logistics, three options, timing.
Succinct slides; the detail lives in the speaker notes. Reads market_tiers.json (market study) when present."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

NAVY=RGBColor(0x1F,0x38,0x64); STEEL=RGBColor(0x4E,0x79,0xA7); GREY=RGBColor(0x59,0x59,0x59)
WHITE=RGBColor(0xFF,0xFF,0xFF); GREEN=RGBColor(0x2E,0x7D,0x46); RED=RGBColor(0xB2,0x3A,0x2E)
AMBER=RGBColor(0x9C,0x5A,0x0C); LIGHT=RGBColor(0xEE,0xF2,0xF7); PALE=RGBColor(0xF6,0xF8,0xFB)
LGREEN=RGBColor(0xE2,0xEF,0xDA); LRED=RGBColor(0xFC,0xE4,0xD6); LAMB=RGBColor(0xFF,0xF2,0xCC); LGT=RGBColor(0xD6,0xDC,0xE5)

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
def timeline(s,l,t,w,events):
    """events: (date, headline, detail, color). Dates/headlines above the line, details below."""
    n=len(events); step=w/n; ly=t+0.95
    rect(s,l,ly-0.02,w,0.04,STEEL)
    for i,(d,h,det,col) in enumerate(events):
        cx=l+step*(i+0.5)
        dot=s.shapes.add_shape(MSO_SHAPE.OVAL,Inches(cx-0.1),Inches(ly-0.1),Inches(0.2),Inches(0.2)); dot.fill.solid(); dot.fill.fore_color.rgb=col; dot.line.color.rgb=WHITE; dot.line.width=Pt(1); dot.shadow.inherit=False
        tf=box(s,cx-step/2+0.02,t,step-0.04,0.85); tf.vertical_anchor=MSO_ANCHOR.BOTTOM
        par(tf.paragraphs[0],d,9,col,bold=True,align=PP_ALIGN.CENTER,after=1); par(tf.add_paragraph(),h,9,NAVY,bold=True,align=PP_ALIGN.CENTER,after=0)
        tf=box(s,cx-step/2+0.02,ly+0.13,step-0.04,1.1); par(tf.paragraphs[0],det,8,GREY,align=PP_ALIGN.CENTER)
def lane(s,l,t,w,h,label,segs,total):
    """segs: (start,end,fill,text,textcolor) on a day scale 0..total; label sits left of the lane."""
    tf=box(s,l,t-0.03,1.9,h+0.06); tf.vertical_anchor=MSO_ANCHOR.MIDDLE; par(tf.paragraphs[0],label,9.5,NAVY,bold=True,after=0)
    l2=l+1.95; w2=w-1.95
    for a,b,fill,txt,tc in segs:
        x=l2+w2*a/total; ww=w2*(b-a)/total; rect(s,x,t,ww,h,fill,line=WHITE)
        if txt:
            tf=box(s,x,t,ww,h); tf.vertical_anchor=MSO_ANCHOR.MIDDLE; par(tf.paragraphs[0],txt,8.5,tc,bold=True,align=PP_ALIGN.CENTER,after=0)
    return l2,w2

# ===== 1 TITLE =====
s=slide(); rect(s,0,0,13.333,7.5,NAVY); rect(s,0,4.85,13.333,0.06,STEEL)
tf=box(s,0.8,1.5,11.7,2.9); par(tf.paragraphs[0],"Liquid PVA: One Supplier or Two?",40,WHITE,bold=True)
par(tf.add_paragraph(),"Update: PCI Manufacturing has proven it can make our product — and told us what it costs",20,RGBColor(0xBD,0xD7,0xEE))
tf=box(s,0.8,5.1,11.7,1.6)
par(tf.paragraphs[0],"PVA = polyvinyl alcohol — the liquid we buy in 55-gallon drums from SNP Inc. (Durham, NC) to make our hydrogels. Sole-sourced today.",13.5,WHITE)
par(tf.add_paragraph(),"Oscar Penny  ·  Supply Chain  ·  28 September 2026  ·  Decision requested",12,RGBColor(0x9D,0xC3,0xE6))

# ===== 4 PRICE SIDE BY SIDE =====
s=slide(); title_bar(s,"Price per pound, side by side — and where each number comes from","1 · COST")
s.shapes.add_picture("chart_price_side_by_side.png",Inches(0.6),Inches(1.15),width=Inches(8.1))
rect(s,8.95,1.15,3.75,5.2,PALE,STEEL); tf=box(s,9.1,1.25,3.5,5.05)
par(tf.paragraphs[0],"Where each number comes from",13,NAVY,bold=True,after=5)
for k,v in [(f"Market, competitive quantity {T('competitive')}",f"comparable pre-mixed PVA solution at drum scale; range {TR('competitive')}, n={TN('competitive')}"),
            (f"Market, low quantity {T('low')}",f"small packs; range {TR('low')}, n={TN('low')}"),
            (f"Market, high quantity {T('high')}",f"totes / bulk; range {TR('high')}, n={TN('high')}"),
            ("SNP Inc. $0.75","real quote, delivered all-in — a specialist's price"),
            ("PCI $3.50 / $6.00","real quote, 28 Sept: one 5-drum batch / anything smaller"),
            ("CJB $8.42","real quote: $8.00–8.50 toll excluding materials, plus resin")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+"  "; r.font.bold=True; r.font.size=Pt(10.5); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text="— "+v; r2.font.size=Pt(10); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(6)
p=tf.add_paragraph(); par(p,"Why a non-specialist sits far above the market: batch-fixed conversion cost over few pounds, drum-scale freight, risk priced in. SNP Inc.'s tanks are right-sized to our order and PVA is their core line.",10,NAVY,bold=True); p.space_before=Pt(4)
takeaway(s,f"At competitive quantity the market sells comparable PVA solution around {T('competitive')}/lb. SNP Inc. is below it; PCI is well above it; CJB is off the scale.")

# ===== 5 ANNUAL COST SIDE BY SIDE =====
s=slide(); title_bar(s,"Annual cost, side by side — what each option adds to today's $50.7k","1 · COST")
s.shapes.add_picture("chart_annual_side_by_side.png",Inches(0.6),Inches(1.15),width=Inches(8.1))
rect(s,8.95,1.15,3.75,5.2,PALE,STEEL); tf=box(s,9.1,1.25,3.5,5.05)
par(tf.paragraphs[0],"Reading the chart (one year)",13,NAVY,bold=True,after=5)
for k,v in [("Demand","67,600 lb = 150 drums — identical in every bar"),
            ("Split","second source takes one-third = 22,500 lb (50 drums, 10 batches); SNP Inc. keeps 45,100 lb × $0.75 = $33.8k in every option"),
            ("All-SNP","67,600 × $0.75 = $50.7k"),
            ("PCI $3.50","22,500 × $3.50 = $78.8k → $112.6k; +$61.9k (122%)"),
            ("PCI $6.00","same third, ordered below batch size → $168.8k; +$118.1k (233%)"),
            ("CJB $8.42","same third, for scale → $223.3k; +$172.6k (340%)"),
            ("Why the bars differ","SNP Inc.'s part never changes; only the second source's price does"),
            ("Not in the chart","Option 3 (1–2 batches/yr, +$6–12k) is a different quantity — the options slide; internal hours and one-time costs — the options slide")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+"  "; r.font.bold=True; r.font.size=Pt(10.5); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text="— "+v; r2.font.size=Pt(10); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(5)
takeaway(s,"Same demand, same one-third split in every option — only the second source's price changes. At PCI's $3.50 the PVA bill more than doubles (2.2×), every year.")

# ===== 6 HOW WE GOT HERE — SERIES OF EVENTS =====
s=slide(); title_bar(s,"How we got here — a series of events, and what the PCI experiment cost","2 · PCI")
timeline(s,0.6,1.12,12.1,[
 ("Nov 2025","Brenntag never meets viscosity","Above range, unreadable on their viscometer. They stalled — no quote ever received. Mar 2026: a resin sample instead",RED),
 ("Mar–Apr 2026","~94 US suppliers screened","ArroChem Inc., Piedmont Chemical Industries, ILC Dover approached. One gate: hold 90–95 °C",NAVY),
 ("May 2026","ArroChem, ILC Dover fail the heat gate","85 °C ceiling; ILC Dover also the wrong kind of company",RED),
 ("26 Jun 2026","CJB Applied Technologies clears the gate","Front-runner. APV Engineered Coatings confirms heat. Demand confirmed: 1,300 lb/week",GREEN),
 ("Jul 2026","Columbus Chemical Industries cannot hold temperature","Eliminated. July review assumed $1.00–1.25/lb",RED),
 ("4 Aug 2026","CJB priced out","$8.00–8.50/lb toll excl. materials (~11× SNP). Their $6,400 trial declined — capability never corroborated",RED),
 ("Aug–Sep 2026","PCI Manufacturing lab batches","Two-plus batches, a dilution study, method work — unpaid",AMBER),
 ("22 Sep 2026","Viscosity root cause found","Elevated solids from water loss. Spec locked: 11% / 900–1,100 cP",GREEN),
 ("28 Sep 2026","Spec met — real quote","$3.50/lb per 5-drum batch; $6.00 below a batch",GREEN)])
panel(s,0.6,3.55,3.95,2.85,"Proven — and worth",
 ["The cook, the viscosity control, the spec — met on PCI's instrument",
  "A qualified-capable, quoted alternative exists: cold start 6–12 months → ~3–6 (2–3 if re-checked yearly)",
  "Not yet proven at scale: production rate; hydrogel performance on 100% PCI material"],GREEN,LGREEN,10.5)
panel(s,4.7,3.55,3.95,2.85,"What it cost — who paid",
 ["PCI: months of unpaid engineering for an account worth ~$79k/yr to them at one-third",
  "Us: ~10 months since Brenntag — ~$15k of internal hours, sunk, excluded from the options",
  "Still queued at PCI's expense: the shelf-life study and the hydrogel comparison"],AMBER,LAMB,10.5)
panel(s,8.8,3.55,3.9,2.85,"Use it · walk away · the middle",
 ["Use it: +$62k/yr at one-third, a permanent two-stream discipline, and the signal to SNP Inc.",
  "Walk away: goodwill — cost = extra months of a cold start × outage cost × probability",
  "The middle (Option 3): 1–2 batches of 5 drums a year, $7.9k each — a paid, practiced supplier"],NAVY,LIGHT,10.5)
takeaway(s,"Ten months, nine suppliers, one shop that can make it — and now a real price. Whether we buy is a separate decision, with a real price on both sides.")

# ===== 7 LOGISTICS OF 5-DRUM BATCHES =====
s=slide(); title_bar(s,"What 5-drum batches mean operationally","3 · LOGISTICS")
tf=box(s,0.6,1.08,12.1,0.4); par(tf.paragraphs[0],"Block rotation at one-third: one 5-drum batch every ~5 weeks. The 18-day shelf life is counted from manufacture.",12.5,NAVY,bold=True)
TOT=36
l2,w2=lane(s,0.6,1.55,12.1,0.4,"PCI batch clock",[(0,4,LGT,"cook → ship ~4 d",NAVY),(4,16.1,NAVY,"12.1 days used at full rate",WHITE),(16.1,18,LAMB,"slack ~2 d",AMBER),(18,36,PALE,"",GREY)],TOT)
rect(s,l2+w2*18/TOT-0.015,1.5,0.03,0.5,RED); tf=box(s,l2+w2*18/TOT-0.9,1.98,1.8,0.25); par(tf.paragraphs[0],"expiry — day 18",8.5,RED,bold=True,align=PP_ALIGN.CENTER,after=0)
lane(s,0.6,2.3,12.1,0.4,"What the line runs on",[(0,4,GREEN,"SNP Inc.",WHITE),(4,16.1,NAVY,"PCI material — 5 drums",WHITE),(16.1,36,GREEN,"SNP Inc. material — ~10 drums  →  repeat every ~5 weeks",WHITE)],TOT)
for d in (0,4,16,36):
    tf=box(s,l2+w2*d/TOT-0.4,2.72,0.8,0.22); par(tf.paragraphs[0],f"day {d}",8,GREY,align=PP_ALIGN.CENTER,after=0)
tf=box(s,0.6,3.0,12.1,0.5); par(tf.paragraphs[0],"Why not blend PCI at one-third alongside SNP Inc.? A batch would last 36 days — twice the life. Even at two-thirds: 18.2 days. A validated 21-day life gives block rotation margin; a 30-day life still needs PCI at ~half of rate.",10.5,NAVY,bold=True)
panel(s,0.6,3.6,3.95,2.8,"What SNP Inc. experiences",
 ["A third less volume ($50.7k → $33.8k/yr)",
  "Cadence is a choice: a ~12-day pause every ~5 weeks — or a steady ~2 drums/week if we hold ~3 drums of rolling stock (strict first-in-first-out)",
  "They read the signal, not the dollars: a third of their core line moved right after we asked for partnership"],RED,LRED,10)
panel(s,4.7,3.6,3.95,2.8,"What we would run",
 ["One spec, one viscometer method; incoming test on every lot; traceability by source",
  "Freeze-protected freight; five drums on site; strict first-in-first-out",
  "Failover in writing: SNP Inc. lead time + a standing cover order — a rejected PCI lot is line-down for that lead time",
  "PCI's residual-film issue closed before any production batch; two Supplier Quality Agreements (SQA)"],AMBER,LAMB,10)
panel(s,8.8,3.6,3.9,2.8,"What it buys",
 ["Recovery in weeks — only if PCI confirms in writing a ramp to ~3 batches a month",
  "Until then, ~2/3 of volume still stops in an outage",
  "If PCI cooks the same producer's resin as SNP: it hedges the cook, not the resin — buffer dry resin either way"],GREEN,LGREEN,10)
takeaway(s,"Two suppliers is workable as a permanent discipline; SNP Inc.'s cadence can stay level if we carry a few drums of margin — the shelf-life study decides.")

# ===== 8 THREE OPTIONS =====
s=slide(); title_bar(s,"Three options","4 · STRATEGY")
s.shapes.add_picture("chart_options_year1.png",Inches(0.6),Inches(1.08),width=Inches(12.1))
rows=[["","Option 1 · Second supplier at one-third","Option 2 · Strengthen SNP Inc. only — no volume moved","Option 3 · Keep-alive: 1–2 batches of 5 drums a year"],
 ["What it is","10 PCI batches/yr; SNP Inc. keeps ~2/3","SNP Inc. sole source with partnership terms; PCI a quoted option; pay a development fee","Option 2, plus 1–2 PCI batches a year — the minimum that keeps a qualified supplier alive"],
 ["Recurring","+$62k/yr premium + ~$3–8k quality overhead (~$378k / 5 yrs)","~$3–12k/yr","+$6.2k/yr per batch ($7.9k gross) + Option 2's ~$3–12k"],
 ["One-time","~$15–40k internal hours to production release","~$5–10k PCI fee + ~$5–10k SNP terms","~$15–40k internal hours + ~$5–10k SNP terms (the batches are PCI's payment)"],
 ["What it buys","A practiced second source; weeks to recover if the ramp is confirmed","Deeper partnership; cold start ~3–6 months (decays after ~12 idle)","Option 2 + production scale proven, a qualification that never goes stale, and a batch price with no volume string attached; restart weeks to months"],
 ["SNP Inc. sees","A third less volume; strain at the wrong moment","A strengthened partner","1–2 pre-announced 12-day pauses a year (3–7%) — or none, with a rolling stock"],
 ["PCI sees","A customer","Goodwill at risk unless settled candidly","A customer — small, but real, every year"],
 ["Residual risk","~2/3 exposed until ramp; SNP re-price; two-stream quality load","SNP failure = months","No volume term on the $3.50 price so far — get it in writing; ~93–97% exposed until PCI ramps"]]
fills=[None]+[[None,LRED,LGREEN,LAMB] for _ in range(7)]
table(s,0.6,3.1,12.1,3.3,rows,[1.35,3.35,3.55,3.85],size=9,fills=fills)
takeaway(s,"Option 3 keeps a paid, practiced supplier for ~$8–16k a year gross — with one or two pre-announced 12-day pauses for SNP Inc., or none with a small rolling stock.",fill=GREEN)

# ===== 9 KEEPING A QUALIFIED SUPPLIER YOU BARELY USE =====
s=slide(); title_bar(s,"Keeping a qualified supplier you barely use — how it is done","4 · STRATEGY")
tf=box(s,0.6,1.12,12.1,0.55); par(tf.paragraphs[0],"Routine in medical devices, pharma and aerospace. What spoils the relationship is not the 'no' — it is silence and unpaid work. Five instruments, rising commitment; Option 3 is instruments 3 and 5 made routine.",12,NAVY,bold=True)
rows=[["Instrument","What it is","Cost here","What it does for the relationship"],
 ["1 · Pay for the qualification (NRE — non-recurring engineering)","Fund the lots, testing and documentation already done","Development fee, ~$5–10k placeholder — PCI to invoice","Free experiments become a paid engagement; an approved-source file"],
 ["2 · Master agreement, no volume commitment","Price ($3.50, resin-indexed), spec, lead time, quality and change terms; 12–24 months; zero minimum — if PCI accepts","Legal time","Formal approved-second-source status; a callable option at a known price"],
 ["3 · One production-scale order (Option 3, step one)","One paid 5-drum batch: proves production scale, completes the file; ramp stays a written commitment to obtain","$7.9k gross (~$6.2k over SNP)","Strongest form — they have shipped to us"],
 ["4 · Readiness / capacity-reservation fee","A fee for the right to call volume at a set price with a committed ramp (pharma: ~20% of batch value; multi-million minimums)","Token retainer at most","Rarely worth it at our scale"],
 ["5 · Planned re-check (Option 3's cadence)","Idle suppliers go stale: Production Part Approval Process (PPAP) re-approval after 12 months idle; ~18 months = 'new supplier'; ISO 13485 §7.4.1","1–2 batches/yr ≈ $7.9–15.8k gross — if PCI accepts","Keeps the option honest and the supplier practiced"]]
fills=[None,None,None,[None,LGREEN,LGREEN,LGREEN],None,[None,LGREEN,LGREEN,LGREEN]]
table(s,0.6,1.75,12.1,3.55,rows,[2.9,4.0,2.2,3.0],size=9.6,fills=fills)
panel(s,0.6,5.5,12.1,0.95,"Conduct that keeps it intact",
 ["Tell PCI the volume reality and the exact triggers · pay promptly · share the test results · a quarterly touchpoint · a reference. Suppliers allocate goodwill on trust, long-term orientation and growth prospects — not on current volume (Pulles, Schiele et al. 2016)."],NAVY,LIGHT,10.5)
takeaway(s,"Barely using a qualified supplier is normal. Pay for the work, sign the terms, state the triggers, order a batch or two a year — and the door stays open.",fill=GREEN)

# ===== 10 WHY DECIDE NOW =====
s=slide(); title_bar(s,"Why decide now","5 · TIMING")
bullets(s,0.6,1.2,6.6,5.1,[
 ("Our next conversation with SNP Inc. is where the strategy becomes real. ","Continuity terms, forecast sharing, resin consignment, a resin-indexed price, capacity headroom, succession — settled in conversation, not by email."),
 ("The posture has to match the decision. ","We cannot ask for a deeper partnership and, in the same period, plan to move a third of their core line without telling them. Announcing it afterwards would undo the partnership conversation."),
 ("If Option 1: ","bring a package, not a cut — a 3-year commitment on ~100 drums/yr growing 10%/yr, a level cadence, forecast sharing, a joint hydrogel roadmap. Reason given: a quality-system continuity requirement."),
 ("If Option 2 or 3: ","that is the partnership conversation. Our continuity file (ISO 13485 clause 7.4 / GHTF N17) includes a qualified alternate cooker and, under Option 3, a verification lot or two a year. The supplier is not named; the quote is not shown."),
],size=12,gap=9)
rect(s,7.5,1.2,5.2,5.1,PALE,STEEL); tf=box(s,7.7,1.3,4.8,4.95)
par(tf.paragraphs[0],"To settle with SNP Inc. under Option 2 / 3",13,NAVY,bold=True,after=5)
for it in ["Give first: rolling 12-month forecast, refreshed monthly; the hydrogel program as a written joint roadmap; a multi-year commitment",
           "Then ask, as Supplier Quality Agreement (SQA) clauses: second line/site plan, key-person cover, advance change notice, right to audit",
           "12–26 weeks of dry PVA resin on consignment (shelf-stable; ~$2–6k tied up)",
           "Capacity headroom at Year-5 volume (~99k lb/yr, ~1,900 lb/week)",
           "Business continuity: ownership, financial resilience — under mutual non-disclosure agreement (NDA)",
           "A shelf-life study: cheap if the limiter is viscosity build; a formulation change if it is microbial — unknown today"]:
    par(tf.add_paragraph(),"•  "+it,10.5,GREY,after=5)
takeaway(s,"Decide the strategy first; then use the SNP Inc. conversation to execute it — not to discover it.",fill=AMBER)

# ===== 11 RECOMMENDATION & ASKS =====
s=slide(); title_bar(s,"Recommendation & asks","6 · DECISION")
panel(s,0.6,1.2,5.95,3.15,"Recommendation: Option 3 at one batch a year, with Option 2's partnership terms",
 ["Decide now; order the first 5-drum batch from PCI Manufacturing ($7.9k) once SNP Inc. has been told a continuity verification lot will run",
  "Go into the SNP Inc. conversation as a partner: continuity terms, forecast, resin consignment, capacity headroom, succession, shelf-life study",
  "Tell PCI the triggers candidly; one batch a year keeps the qualification current — two if an SNP Inc. risk signal appears"],GREEN,LGREEN,11)
panel(s,6.75,1.2,5.95,3.15,"Go to Option 1 (one-third, 10 batches/yr) if any trigger fires",
 ["Finance's estimate of the loss a second source would AVOID in a 6-month SNP Inc. outage exceeds ~$620k (10%/yr risk) or ~$1.24M (5%) — full avoidance only with PCI's written ramp; at ~1/3 coverage the bar is ~$1.9M / ~$3.7M",
  "An SNP Inc. risk signal: capacity short of Year-5 volume, succession or financial stress, a missed lot, an unexplained price move",
  "PCI's price falls toward ~$1.50/lb (premium ≈ $17k/yr), a new hydrogel line makes PVA strategic, or SNP Inc. declines the terms"],AMBER,LAMB,10.5)
rect(s,0.6,4.5,12.1,1.9,LIGHT); tf=box(s,0.8,4.58,11.7,1.78)
par(tf.paragraphs[0],"What we need from leadership",13,NAVY,bold=True,after=4)
for it in ["1.  The strategy call — Option 1, 2 or 3 — before our next conversation with SNP Inc.; Option 3 recommended as the reversible step",
           "2.  Finance, by [date]: the loss a second source would avoid in a 6-month PVA outage, per hydrogel stock-keeping unit (SKU) — revenue, contribution margin, deferrable vs lost (fallback: more or less than $1M? $3M?)",
           "3.  Under Option 3: ~$8k cash per PCI batch (one now, up to two a year), ~$5–10k to formalize SNP Inc., ~$15–40k of internal hours to finish qualification — first 12 months ≈ $31–70k all-in"]:
    par(tf.add_paragraph(),it,11,GREY,after=4)
takeaway(s,"Keep the supplier alive for ~$8k a batch, strengthen the source we depend on, and commit ~$62k/yr only when the evidence says so.")

# ===== 12 APPENDIX =====
s=slide(); title_bar(s,"Appendix: assumptions, suppliers, acronyms, frameworks")
rows=[["Assumption","Value","Basis"],
 ["Demand today","1,300 lb/wk = 67,600 lb ≈ 150 drums/yr; +10%/yr","Confirmed 2026-06-26; growth assumption"],
 ["SNP Inc. price","$0.75/lb delivered = $337.50/drum","SNP Estimate 012726-1"],
 ["PCI price","$3.50/lb per 5-drum batch; $6.00/lb below a batch","Quote 2026-09-28 — confirm terms in writing"],
 ["Option 1 share","1/3 = 50 drums/yr = 10 batches = 22,500 lb","Every chart bar; five-year uses an exact third"],
 ["Option 3 keep-alive","1–2 batches/yr = 5–10 drums = 3.3–6.7%; +$6.2–12.4k/yr","$7.9k gross per batch"],
 ["Market reference",f"{T('high')} / {T('competitive')} / {T('low')} per lb","Market study: high / competitive / low quantity"],
 ["CJB quote","$8.00–8.50/lb toll excl. materials ≈ $8.42 landed","$6,400 trial declined; email 'RE: mix test'"],
 ["Qualification cost","~$15k to date (sunk); ~$15–40k to production release; PCI fee ~$5–10k","Memo §2.3; placeholders"],
 ["Outage risk / avoided loss","2–5%/yr planning band (10% upper case); avoided loss not estimated","Memo §5.2; NEEDED from Finance"]]
table(s,0.6,1.15,6.9,3.0,rows,[1.7,3.0,2.2],size=8)
tf=box(s,0.6,5.0,6.9,1.8)
par(tf.paragraphs[0],"Frameworks (independently fact-checked)",10.5,NAVY,bold=True,after=2)
par(tf.add_paragraph(),"Kraljic (HBR 1983), bottleneck items: 'Volume insurance (at cost premium if necessary). Control of vendors. Security of inventories. Backup plans.' Gelderman & van Weele (2003): 'hold' vs 'move'. Simchi-Levi et al. (Interfaces 2015): disruption impact is uncorrelated with spend. Sheffi & Rice (MIT SMR 2005): single sourcing is legitimate only with a deep, managed relationship. Tomlin (2006); Chopra & Sodhi (2014): assuming zero disruption probability is the expensive mistake. Pulles, Schiele et al. (2016): preferential treatment follows attractiveness, not volume. Deloitte Chief Procurement Officer (CPO) Survey 2025: 'active alternative sources' rated most effective (74%). QMSR / ISO 13485 §7.4 / GHTF N17: controls proportionate to risk — no second source required. Six lenses; four refuted claims excluded; memo in the repo.",7.6,GREY)
rect(s,7.75,1.15,4.95,5.65,PALE,STEEL); tf=box(s,7.9,1.22,4.7,5.55)
par(tf.paragraphs[0],"Suppliers named",12,NAVY,bold=True,after=3)
for k,v in [("SNP Inc.","Durham, NC — incumbent, sole source"),("PCI Manufacturing","St. Louis, MO — CMS Manufacturing group; qualified-capable, quoted"),("CJB Applied Technologies","Valdosta, GA — quoted ~11×; $6,400 trial declined; eliminated 4 Aug 2026"),("ArroChem Inc.","Mount Holly, NC — 85 °C ceiling"),("ILC Dover","Frederica, DE — could not hold temperature"),("Columbus Chemical Industries","Columbus, WI — could not hold temperature"),("Brenntag","distributor — trial blends never met viscosity (Nov 2025); stalled, no quote"),("Piedmont Chemical Industries","High Point, NC — reserve"),("APV Engineered Coatings","Akron, OH — reserve")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+"  "; r.font.bold=True; r.font.size=Pt(9); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text="— "+v; r2.font.size=Pt(9); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(1)
p=tf.add_paragraph(); par(p,"Acronyms",12,NAVY,bold=True,after=2); p.space_before=Pt(5)
for k,v in [("PVA","polyvinyl alcohol"),("cP","centipoise — viscosity unit"),("CoA","Certificate of Analysis"),("SQA","Supplier Quality Agreement"),("NRE","non-recurring engineering"),("NDA","non-disclosure agreement"),("PPAP","Production Part Approval Process"),("SKU","stock-keeping unit"),("CPO","Chief Procurement Officer"),("QMSR","FDA Quality Management System Regulation"),("ISO","International Organization for Standardization"),("GHTF","Global Harmonization Task Force"),("HBR / MIT SMR","Harvard Business Review / MIT Sloan Management Review")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+"  "; r.font.bold=True; r.font.size=Pt(9); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text="— "+v; r2.font.size=Pt(9); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(1)
tf=box(s,0.6,6.85,7.0,0.45); par(tf.paragraphs[0],"Workbook: PVA_Second_Supplier_Leadership_Model.xlsx — 'Summary' holds every slide figure as a formula; 'Supplier Quotes', 'Market Study', 'PCI Quote Scenarios', 'PCI Experiment' hold the compiled data.",9,GREY,italic=True)

# ===== SPEAKER NOTES (the detail lives here) =====
NOTES=[
 "Update on the liquid PVA decision. Since last time, two things happened: PCI Manufacturing's experiment met our spec, and they gave us a real price. Today: the cost side by side, how we got here and what the experiment cost, what running two suppliers would look like, then three options - because we need to choose one before our next conversation with SNP.",
 "Price per pound, side by side. Colors: greys are the market, green is SNP, the two ambers are PCI - dark for the batch price, light for below batch - and red is CJB. The three bars on the left are the market: what comparable pre-mixed PVA solution sells for today at high quantity - totes and bulk - at competitive quantity - drum scale, the one that matters - and at low quantity - small packs; ranges and counts are in the workbook's Market Study tab. Green is SNP's real quote at 75 cents, below the competitive market: a specialist's price. Navy and red are PCI's real numbers: 3.50 for a batch, 6 for anything smaller. Red on the far right is CJB, for scale. Why is a non-specialist so far above the market? Batch-fixed conversion cost spread over few pounds, drum-scale freight, and risk priced in. SNP's tanks are right-sized to our order and this is their core line.",
 "Annual cost side by side, apples to apples. The same 67,600 pounds a year in every bar - 150 drums - and the second source takes exactly one third in every option: 22,500 pounds, 50 drums, ten batches of five. SNP's part is identical everywhere: 45,100 pounds at 75 cents, 33.8 thousand. Only the second source's price changes. At PCI's 3.50 batch price: 78.8 thousand for that third, 112.6 total, plus 61.9 thousand a year - 122 percent of today's bill. At the 6-dollar below-batch price: 168.8 total, plus 118. CJB, for scale: 223 total. Option 3 is not a bar because it is a different quantity - one or two batches a year, plus 6 to 12 thousand - it is on the options slide with the one-time costs.",
 "How we got here, as a series of events. November last year: Brenntag, a distributor, tried our formula - the viscosity came out above range, unreadable on their viscometer; they stalled and we never received a quote; in March they sent us a resin sample instead. March to April: we screened about 94 US suppliers and reached out to ArroChem, Piedmont and ILC Dover with one hard gate - hold 90 to 95 degrees. May: ArroChem and ILC Dover failed that gate. June 26: CJB cleared it and became the front-runner; APV confirmed heat; we confirmed demand at 1,300 pounds a week. July: Columbus Chemical told us they cannot hold the temperature. August 4: CJB's quote came in at 8 to 8.50 a pound for toll processing alone - eleven times SNP - and their trial would have cost 6,400 dollars; we declined, so we never corroborated whether they could actually make it. August to September: PCI Manufacturing ran two-plus lab batches and a dilution study, unpaid. September 22: the viscosity root cause - elevated solids - and a locked spec. September 28: spec met, and a real quote of 3.50 a pound per five-drum batch. What it is worth: a cold start is now months, not a year. What it cost: PCI's unpaid engineering, and about 15 thousand of our own hours, sunk. Using it costs 62 thousand a year plus a permanent discipline; walking away costs goodwill; the middle is one or two batches a year.",
 "Logistics. The shelf-life clock starts at manufacture. PCI cooks on day zero, the five drums land around day four, we run on them at full rate through about day sixteen, and they expire on day eighteen - about two days of slack. Then three and a half weeks on SNP, repeat every five weeks; ten batches in year one, about fifteen by year five. We cannot run PCI alongside SNP at a third of rate: a batch would last thirty-six days; even at two-thirds it takes eighteen. A validated twenty-one-day life gives block rotation real margin; a thirty-day life still needs PCI at about half of rate. For SNP: a third less volume, and a choice of cadence - a twelve-day pause every cycle, or a steady two drums a week if we carry about three drums of rolling stock and use them first; the shelf-life study decides. What SNP reads is the signal, not the dollars. For us: one spec, one viscometer method, freeze-protected freight, five drums on site, a written failover with SNP's lead time, PCI's residual-film issue closed before any production batch, two quality agreements. What it buys - recovery in weeks - only if PCI confirms in writing that they can ramp.",
 "Three options. The chart shows the first twelve months all-in and each year after, as ranges; the table says what each buys and what each supplier sees. Option 1, a second supplier at a third of volume: 62 thousand a year of premium plus a few thousand of quality overhead, plus 15 to 40 thousand of internal hours to reach production release - about 80 to 110 thousand in year one; a practiced second source, but strain with SNP at the wrong moment. Option 2, strengthen SNP only, no volume moved: a development fee to PCI, a few thousand to formalize SNP, 3 to 12 thousand a year - 13 to 32 thousand in year one; deeper partnership, but SNP failure still means months. Option 3, keep-alive: Option 2's partnership plus one or two five-drum batches a year from PCI, 7,900 dollars each gross, 6,200 of premium each - 31 to 70 thousand in year one at one batch, 39 to 78 at two, of which 13 to 26 thousand is cash to suppliers. Everything Option 2 buys plus production scale proven and a qualification that never goes stale; SNP sees one or two pre-announced twelve-day pauses, or none if we carry a small rolling stock. The economic advantage of Option 3: the 3.50 batch price has no volume string attached - nothing in the quote or any contract ties it to a yearly volume - so we can order a batch when we choose; we should get that in writing, and if PCI ever attaches a minimum, Option 3 collapses to Option 2. Internal hours already spent - about 15 thousand - are sunk and excluded everywhere. Option 3 at one batch a year is my recommendation.",
 "How companies keep a qualified supplier they barely use - because you will be asked whether Option 3 is realistic. It is routine in medical devices, pharma and aerospace. What spoils the relationship is silence and unpaid work, not the 'no'. The instruments, in rising order of commitment: pay a development fee for the qualification work already done; sign a master agreement with price, spec and terms but no volume commitment, if PCI accepts one; place one production-scale order; a readiness fee, which is rare at our scale; and a planned re-check, because an idle supplier goes stale after about a year - the Production Part Approval Process rule of thumb is twelve months. Option 3 is the last two made routine. And the conduct: tell PCI the triggers, pay promptly, share results, keep a quarterly touchpoint. The research is clear that suppliers allocate goodwill on trust and growth prospects, not current volume.",
 "Why decide now. Our next conversation with SNP is where the strategy becomes real - continuity terms, forecast sharing, resin consignment, capacity headroom, succession. The posture has to match the decision: we cannot ask for a deeper partnership and, in the same period, plan to move a third of their core line without telling them - announcing it afterwards would undo the partnership conversation. If the answer is Option 1, bring a package, not a cut: a three-year commitment on about a hundred drums a year growing ten percent - back to today's absolute volume by about year five - a level cadence, forecast sharing, a joint hydrogel roadmap; reason given, a quality-system continuity requirement. If it is Option 2 or 3, that is the partnership conversation: our continuity file includes a qualified alternate cooker and, under Option 3, a verification lot or two a year - the supplier is not named and the quote is not shown - the same continuity discipline we are asking SNP to document. Give first, then ask. Decide first; use the conversation to execute, not to discover.",
 "Recommendation: Option 3 at one batch a year, with Option 2's partnership terms and the existing triggers. Decide now; place the first batch order once SNP has been told a continuity verification lot will run; go into the SNP conversation as a partner and settle the items on the previous slide; tell PCI the triggers candidly; a second batch a year if an SNP risk signal appears. Switch to Option 1 if Finance's estimate of the loss a second source would avoid clears about 620 thousand at a ten percent yearly risk or 1.24 million at five - counting full avoidance only with PCI's written ramp commitment - or if SNP shows a risk signal, or PCI's price falls toward a dollar fifty, or SNP declines the terms. Before the first order, confirm with PCI in writing: the 3.50 batch price carries no volume commitment and how long it holds; batch lead time; delivered and all-in with freeze-protected freight; a crisis ramp to about three batches a month in the same kettle; which resin producer they use; and a split-sample viscometer cross-check. Three asks: the strategy call before the SNP conversation, Option 3 recommended; Finance's avoided-loss number by a date, with Option 1 re-tested against it at the next quarterly review; and under Option 3 about 8 thousand cash per PCI batch, 5 to 10 thousand to formalize SNP, and 15 to 40 thousand of internal hours - 31 to 70 thousand all-in in the first twelve months.",
 "Assumptions, suppliers by full name, acronyms, and the fact-checked frameworks. The workbook's Summary tab holds every slide figure as a formula; Supplier Quotes, Market Study, PCI Quote Scenarios and the PCI Experiment record hold the compiled data.",
]
for sl,txt in zip(prs.slides,NOTES): sl.notes_slide.notes_text_frame.text=txt
prs.save("PVA_Second_Supplier_Leadership_Deck.pptx"); print("saved deck:",len(prs.slides._sldIdLst),"slides")
