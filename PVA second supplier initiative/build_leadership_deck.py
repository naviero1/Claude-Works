#!/usr/bin/env python3
"""Leadership deck: Liquid PVA — one supplier or two? (sequenced decision narrative)."""
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
def title_bar(s,text,step=None,total=None):
    rect(s,0,0,13.333,1.0,NAVY)
    tf=box(s,0.5,0.14,11.4,0.8); par(tf.paragraphs[0],text,26,WHITE,bold=True)
    if step:
        tf=box(s,11.9,0.3,1.2,0.5); par(tf.paragraphs[0],f"{step} / {total}",12,RGBColor(0xBD,0xD7,0xEE),align=PP_ALIGN.RIGHT)
def bullets(s,l,t,w,h,items,size=15,gap=8,color=GREY):
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
def card(s,l,t,w,h,value,label,vcolor=NAVY,fill=LIGHT,vsize=26):
    rect(s,l,t,w,h,fill)
    tf=box(s,l+0.12,t+0.12,w-0.24,h-0.24); tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    par(tf.paragraphs[0],value,vsize,vcolor,bold=True,align=PP_ALIGN.CENTER,after=2)
    par(tf.add_paragraph(),label,11,GREY,align=PP_ALIGN.CENTER)
def takeaway(s,text,t=6.55,fill=NAVY,color=WHITE):
    rect(s,0.6,t,12.1,0.62,fill)
    tf=box(s,0.8,t+0.08,11.7,0.5); tf.vertical_anchor=MSO_ANCHOR.MIDDLE; par(tf.paragraphs[0],text,14,color,bold=True)
def table(s,l,t,w,h,rows,colw,size=12,hdr_fill=NAVY,first_col_bold=True,fills=None):
    tbl=s.shapes.add_table(len(rows),len(rows[0]),Inches(l),Inches(t),Inches(w),Inches(h)).table
    for i,cw in enumerate(colw): tbl.columns[i].width=Inches(cw)
    for ri,row in enumerate(rows):
        for ci,val in enumerate(row):
            c=tbl.cell(ri,ci); c.text=str(val); p=c.text_frame.paragraphs[0]
            p.alignment=PP_ALIGN.LEFT if ci==0 else PP_ALIGN.CENTER
            r=(p.runs[0] if p.runs else p.add_run()); r.font.size=Pt(size); r.font.name="Calibri"; c.fill.solid()
            if ri==0: r.font.bold=True; r.font.color.rgb=WHITE; c.fill.fore_color.rgb=hdr_fill
            else:
                r.font.color.rgb=NAVY; c.fill.fore_color.rgb=(fills[ri][ci] if fills and fills[ri] and fills[ri][ci] else WHITE)
                if ci==0 and first_col_bold: r.font.bold=True
    return tbl

N=13  # numbered content slides

# ---------- 1 TITLE ----------
s=slide(); rect(s,0,0,13.333,7.5,NAVY); rect(s,0,4.85,13.333,0.06,STEEL)
tf=box(s,0.8,1.7,11.7,2.6)
par(tf.paragraphs[0],"Liquid PVA: One Supplier or Two?",42,WHITE,bold=True)
par(tf.add_paragraph(),"What a second source really costs, what the alternative looks like, and whether our volume justifies it today",20,RGBColor(0xBD,0xD7,0xEE))
tf=box(s,0.8,5.1,11.7,1.6)
par(tf.paragraphs[0],"PVA = polyvinyl alcohol, the liquid we buy in 55-gallon drums to make our hydrogels",14,WHITE)
par(tf.add_paragraph(),"Oscar Penny  ·  Supply Chain  ·  22 September 2026  ·  Decision requested",12,RGBColor(0x9D,0xC3,0xE6))

# ---------- 2 EXEC SUMMARY ----------
s=slide(); title_bar(s,"The decision in one slide",1,N)
tf=box(s,0.6,1.2,12.1,0.8)
par(tf.paragraphs[0],"Should we carry a second supplier for liquid PVA now — or stay with SNP and invest in making that single source resilient?",16,NAVY,bold=True)
card(s,0.6,2.15,2.9,1.5,"$50.7k/yr","Today's entire PVA spend (SNP, $0.75/lb)")
card(s,3.7,2.15,2.9,1.5,"+$39–96k/yr","A 2nd supplier at 1/3 of volume, $2.50–5.00/lb",vcolor=RED,fill=LRED)
card(s,6.8,2.15,2.9,1.5,"$240–585k","5-year cumulative premium (volume +10%/yr)",vcolor=RED,fill=LRED)
card(s,9.9,2.15,2.8,1.5,"~$6–14k/yr","A 'warm' backup at 5% instead",vcolor=GREEN,fill=LGREEN)
bullets(s,0.6,3.95,12.1,2.5,[
 ("The honest headline: ","a full second source would cost 80–190% of what we spend on PVA today — 4–8× the '$6–12k' insurance we described in July, because realistic pricing is $2.50–5.00/lb, not $1.00–1.25."),
 ("What we learned the hard way: ","six months and 94 suppliers to get one candidate (PCI) close to qualified. That is our real time-to-recover if SNP ever fails — and it is the strongest argument for NOT starting from zero."),
 ("Recommendation: ","strengthen SNP now (forecast sharing, joint hydrogel development, continuity terms) AND finish qualifying PCI as a warm backup at ~5% — keeping the option alive for ~$10k/yr. Move to a full split only when defined triggers are hit."),
],size=14,gap=9)
takeaway(s,"Ask today: approve the SNP partnership steps, the warm-backup budget, and give us one number — what a 6-month PVA outage would cost the business.")

# ---------- 3 WHY WE'RE HERE ----------
s=slide(); title_bar(s,"Why we're here: a small spend with an outsized failure mode",2,N)
bullets(s,0.6,1.25,6.6,4.6,[
 ("Single point of failure. ","Liquid PVA (P/N 666438) is sole-sourced from SNP, a ~$4M specialist for whom PVA cooking is the core product."),
 ("No buffer is possible. ","18-day shelf life means every drum is made fresh. If SNP stops, we have roughly 2½ weeks of material — our 'time-to-survive'."),
 ("Recovery is slow. ","Qualifying a replacement from zero has taken us ~6 months and counting — our 'time-to-recover'. When recovery time exceeds survival time, the exposure is real."),
 ("Small money, critical input. ","$50.7k/yr is a rounding error in spend, but it gates a product line. In procurement terms this is a 'bottleneck' item: low spend, high supply risk — the category where the textbook answer is to secure supply, not to chase price."),
],size=14,gap=10)
rect(s,7.5,1.25,5.2,4.6,PALE,STEEL)
tf=box(s,7.75,1.4,4.7,4.3)
par(tf.paragraphs[0],"What we told you in July — and what changed",14,NAVY,bold=True,after=8)
par(tf.add_paragraph(),"July: 'qualify a capped ~35% second source as low-cost insurance, ~$6–12k/yr' — priced at $1.00–1.25/lb.",12,GREY,after=8)
par(tf.add_paragraph(),"Since then: the first toll blender that got through our technical gate quoted ~11× SNP. The candidate now in testing (PCI) will realistically land at $2.50–5.00/lb.",12,GREY,after=8)
par(tf.add_paragraph(),"Same plan, real prices: +$39–96k/yr, not $6–12k. We owe you the corrected picture before you decide.",12,NAVY,bold=True)
takeaway(s,"The risk is unchanged. The price of insuring it turned out to be much higher than we first estimated.")

# ---------- 4 WHAT WE LEARNED ----------
s=slide(); title_bar(s,"What six months of searching taught us",3,N)
card(s,0.6,1.25,2.9,1.35,"94","US suppliers screened")
card(s,3.7,1.25,2.9,1.35,"~6 mo","to get one candidate close to qualified",vcolor=AMBER,fill=LAMB)
card(s,6.8,1.25,2.9,1.35,"~11×","the one toll quote we got vs SNP (CJB)",vcolor=RED,fill=LRED)
card(s,9.9,1.25,2.8,1.35,"1","credible candidate today (PCI)",vcolor=GREEN,fill=LGREEN)
bullets(s,0.6,2.85,12.1,3.5,[
 ("Most suppliers cannot make this product. ","The 90–95 °C dissolution cook eliminated the majority; batch minimums that overshoot an 18-day shelf life eliminated most of the rest."),
 ("The market price for this work is not $0.75/lb. ","Triangulated market range: $0.85 low / $1.40 base / $2.55 high per lb. SNP is cheap because this is their core competence. Any second source is a premium supplier by definition."),
 ("PCI is promising but not yet there. ","Viscosity root cause found (solids content), spec agreed (11% solids, 900–1,100 cP), new batch in work. Still open: shelf-life study, hydrogel performance, cleaning."),
 ("The real lesson: ","if SNP failed tomorrow with no preparation, we would be looking at 6–12 months of exposure and crisis-priced material. That number — not the price per pound — is what a second source is insurance against."),
],size=14,gap=9)
takeaway(s,"We now own the spec, the RFQ package, and a screened longlist. Even without a second supplier, our recovery time is already shorter than it was in March.")

# ---------- 5 ANNUAL COST ----------
s=slide(); title_bar(s,"What a second supplier really costs — per year",4,N)
s.shapes.add_picture("chart_premium_by_price.png",Inches(0.6),Inches(1.15),width=Inches(8.4))
rect(s,9.25,1.15,3.45,5.2,PALE,STEEL)
tf=box(s,9.45,1.3,3.1,5.0)
par(tf.paragraphs[0],"How to read this",14,NAVY,bold=True,after=6)
par(tf.add_paragraph(),"Each bar = the EXTRA we pay per year if a second source takes 1/3 of volume at that price. The drums are bought either way; the premium is the decision number.",11.5,GREY,after=8)
par(tf.add_paragraph(),"PCI range ($2.50–5.00): +$39k to +$96k/yr — i.e., 80–190% of today's whole PVA bill.",12,NAVY,bold=True,after=8)
par(tf.add_paragraph(),"Green bar = what we described in July. Red bar = the CJB quote, shown for scale.",11.5,GREY,after=8)
par(tf.add_paragraph(),"Not shown: if SNP re-prices the 2/3 it keeps (+10–20%), add another $3–7k/yr.",11.5,GREY)
takeaway(s,"At realistic prices, a one-third second source roughly doubles what we spend on PVA. That is the cost of the insurance.")

# ---------- 6 FIVE-YEAR ----------
s=slide(); title_bar(s,"The five-year view: the premium grows with our volume",5,N)
s.shapes.add_picture("chart_five_year.png",Inches(0.6),Inches(1.15),width=Inches(8.4))
rect(s,9.25,1.15,3.45,5.2,PALE,STEEL)
tf=box(s,9.45,1.3,3.1,5.0)
par(tf.paragraphs[0],"Why it compounds",14,NAVY,bold=True,after=6)
par(tf.add_paragraph(),"The premium is share × price gap × pounds. Volume grows ~10%/yr, so the premium does too.",11.5,GREY,after=8)
par(tf.add_paragraph(),"Five-year cost of a 1/3 split: $240k (at $2.50) to $585k (at $5.00). Mid case ~$413k.",12,NAVY,bold=True,after=8)
par(tf.add_paragraph(),"A 5% 'warm' backup over the same period: ~$62k.",12,GREEN,bold=True,after=8)
par(tf.add_paragraph(),"Plus a one-time qualification cost (~$15k placeholder: engineering time, samples, hydrogel tests, quality agreement) for ANY second source, warm or active.",11.5,GREY)
takeaway(s,"Over five years the difference between a full split and a warm backup is roughly $180–520k.")

# ---------- 7 WHAT IT BUYS ----------
s=slide(); title_bar(s,"What that money buys — and what it doesn't",6,N)
rect(s,0.6,1.25,5.95,5.1,LGREEN); tf=box(s,0.8,1.4,5.6,4.9)
par(tf.paragraphs[0],"What a 1/3 second source BUYS",15,GREEN,bold=True,after=8)
for it in ["A qualified, practiced supplier — recovery in weeks, not months, if SNP fails",
           "Price discipline on SNP (a credible alternative at the table)",
           "A defensible supplier-control story for auditors (though not required — see appendix)",
           "Two sets of production knowledge on a product only a handful of shops can make",
           "Real-world hydrogel performance data from a second process"]:
    par(tf.add_paragraph(),"•  "+it,12.5,GREY,after=7)
rect(s,6.75,1.25,5.95,5.1,LRED); tf=box(s,6.95,1.4,5.6,4.9)
par(tf.paragraphs[0],"What it DOESN'T buy",15,RED,bold=True,after=8)
for it in ["Full protection: 2/3 of volume still stops if SNP fails, until PCI can ramp (unknown capacity)",
           "A better price: every pound moved to PCI costs 3–7× more; SNP may re-price the volume it keeps",
           "Simplicity: two specs, two Certificates of Analysis (CoA), two cleaning procedures, two relationships to manage",
           "Goodwill: taking a third of a small partner's core product line is a signal SNP will read — at the moment we are asking them to co-develop new hydrogels",
           "Certainty on cost: PCI is not yet quoted; $2.50–5.00 is our forecast, not their number"]:
    par(tf.add_paragraph(),"•  "+it,12.5,GREY,after=7)
takeaway(s,"Dual-sourcing reduces the worst case — it does not eliminate it, and it changes the relationship we most depend on.")

# ---------- 8 ALTERNATIVE: SINGLE + STRENGTHEN ----------
s=slide(); title_bar(s,"The alternative: one supplier, done deliberately",7,N)
tf=box(s,0.6,1.15,12.1,0.6); par(tf.paragraphs[0],"Keep SNP as sole source, but convert an informal dependency into a managed partnership with a written continuity plan.",14,NAVY,bold=True)
rows=[["Lever","What it means in practice","Cost / effort","Risk it reduces"],
 ["Share our forecast","Rolling 12-month volume + growth plan; quarterly review","Low — a meeting","Capacity surprises; gives SNP reason to invest"],
 ["Co-develop new hydrogels","Already scheduled — make it a standing joint program","Low — engineering time","Lock-in works both ways; makes us their most interesting customer"],
 ["Continuity terms in a Supplier Quality Agreement (SQA)","Second line/site plan, key-person cover, advance change notice, right to audit","Low–medium — legal + quality","Silent process changes; single-line outages"],
 ["Buffer the RESIN, not the solution","Dry PVA resin is shelf-stable for years; hold 8–12 weeks at SNP (consignment) or with us","Low — ~$2–3k tied up","Raw-material shortages; the most common upstream failure"],
 ["Process escrow + bench-cook capability","SNP's recipe/process on file; our lab can cook small batches in a crisis","Low — documentation + a lab day","Total knowledge loss; buys weeks in an emergency"],
 ["Financial-health check","Annual review of a ~$4M private supplier's viability","Low","Sudden business failure — the one risk that gives no warning"],
 ["Keep the cold-start kit current","Spec, RFQ package, screened longlist maintained annually","Low","Cuts recovery from 6–12 months toward 3–4"]]
table(s,0.6,1.8,12.1,4.3,rows,[2.6,4.2,2.1,3.2],size=10.5)
takeaway(s,"Total cost of Option B: a few thousand dollars and some engineering time — versus $39–96k/yr. Residual risk: a true SNP failure still means months of exposure.")

# ---------- 9 MIDDLE PATH: WARM BACKUP ----------
s=slide(); title_bar(s,"A middle path: finish PCI, then keep it warm",8,N)
bullets(s,0.6,1.25,6.6,4.8,[
 ("The idea. ","Complete PCI's qualification (we are most of the way there), then give them a small, steady trickle — about 5% of volume, one drum every ~7 weeks — so the process, people and paperwork stay current."),
 ("What it costs. ","~$6–14k/yr at $2.50–5.00/lb, plus the one-time qualification. Five-year total ~$62k at the mid price."),
 ("What it buys. ","Recovery in weeks instead of months if SNP fails; a real quote on file; leverage without taking a third of SNP's business; the six months already invested becomes a standing option instead of a sunk cost."),
 ("Where it can fail. ","5% may be too little for PCI to care — this needs an explicit 'readiness' understanding, not just orders. Capacity to ramp from 5% to 100% in a crisis must be confirmed in writing. And a dormant supplier drifts: annual re-check batch required."),
],size=13.5,gap=10)
rect(s,7.5,1.25,5.2,4.8,PALE,STEEL); tf=box(s,7.7,1.4,4.8,4.6)
par(tf.paragraphs[0],"Option C by the numbers (mid price $3.75)",14,NAVY,bold=True,after=8)
for k,v in [("Share to PCI","~5%  (~8 drums/yr)"),("Annual premium","~$10k"),("5-year premium","~$62k"),("One-time qualification","~$15k (placeholder)"),("Volume exposed if SNP fails","95% — until PCI ramps"),("Time to recover","weeks–months (re-activate), not 6–12 months")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+":  "; r.font.bold=True; r.font.size=Pt(12); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text=v; r2.font.size=Pt(12); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(7)
takeaway(s,"For roughly a fifth of the cost of a full split, we keep the option to switch — which is the thing we actually need.",fill=GREEN)

# ---------- 10 BREAK-EVEN ----------
s=slide(); title_bar(s,"Does the volume justify it? The break-even test",9,N)
s.shapes.add_picture("chart_breakeven.png",Inches(0.6),Inches(1.15),width=Inches(8.4))
rect(s,9.25,1.15,3.45,5.2,PALE,STEEL); tf=box(s,9.45,1.3,3.1,5.0)
par(tf.paragraphs[0],"The test",14,NAVY,bold=True,after=6)
par(tf.add_paragraph(),"Insurance pays when: annual premium ≤ (probability of an SNP outage in a year) × (loss the backup would avoid).",11.5,GREY,after=8)
par(tf.add_paragraph(),"Mid case, 1/3 split ($68k/yr): at a 5%-a-year outage risk, the avoided loss must exceed ~$1.35M; at 10%, ~$680k.",12,NAVY,bold=True,after=8)
par(tf.add_paragraph(),"Warm backup ($10k/yr): at 5%, ~$200k; at 10%, ~$100k — a far easier bar to clear.",12,GREEN,bold=True,after=8)
par(tf.add_paragraph(),"The number we don't have: what a 6-month PVA outage costs us (lost revenue, expedite, line-down). That single figure decides this.",11.5,RED,bold=True)
takeaway(s,"At today's volume, a full split only pays if an SNP failure would cost us well over half a million dollars. A warm backup pays at a fraction of that.")

# ---------- 11 SIDE BY SIDE ----------
s=slide(); title_bar(s,"The three options, side by side",10,N)
rows=[["","A · Dual-source now (1/3 to PCI)","B · Single source + strengthen SNP","C · Warm backup (finish PCI, ~5%)"],
 ["Annual premium (mid $3.75)","+$68k  (range $39–96k)","~$0  (+ small continuity spend)","~$10k  (range $6–14k)"],
 ["5-year premium (+10%/yr)","~$413k  ($240–585k)","~$0","~$62k"],
 ["One-time qualification","~$15k","none (document only)","~$15k"],
 ["Volume exposed if SNP fails","2/3 until PCI ramps","100%","95% until PCI ramps"],
 ["Time to recover","weeks","6–12 months (3–4 with cold-start kit)","weeks–months"],
 ["Signal to SNP","We took a third of their line","Deeper partnership","Minor"],
 ["Compliance posture","Strong","Defensible if risk + plan documented","Strong"],
 ["Best when…","outage cost > ~$700k–1.4M and we can't fix SNP's fragility","SNP is healthy, engaged, and we can document the plan","we want the option without paying full price for it"]]
fills=[None]+[[None,LRED,LGREEN,LAMB] for _ in range(8)]
table(s,0.6,1.25,12.1,4.95,rows,[2.5,3.2,3.2,3.2],size=11,fills=fills)
takeaway(s,"B and C are not alternatives to each other — together they are the balanced answer at our current volume.")

# ---------- 12 RECOMMENDATION ----------
s=slide(); title_bar(s,"Recommendation: B + C now; A when the triggers say so",11,N)
rect(s,0.6,1.25,5.95,5.1,LGREEN); tf=box(s,0.8,1.4,5.6,4.9)
par(tf.paragraphs[0],"Do now (next 90 days)",15,GREEN,bold=True,after=8)
for it in ["Formalize the SNP partnership: share the forecast, make the hydrogel co-development a standing program, add continuity terms to a Supplier Quality Agreement",
           "Put 8–12 weeks of dry PVA resin on consignment at SNP (or with us) — resin is shelf-stable; the solution is not",
           "Finish PCI qualification (shelf-life, hydrogel, cleaning) and lock a written per-drum price",
           "Start the 5% warm trickle with an explicit readiness understanding and a confirmed ramp plan",
           "Keep the cold-start kit (spec, RFQ, longlist) current — annual refresh"]:
    par(tf.add_paragraph(),"•  "+it,12.5,GREY,after=7)
rect(s,6.75,1.25,5.95,5.1,LAMB); tf=box(s,6.95,1.4,5.6,4.9)
par(tf.paragraphs[0],"Move to a full split (A) if any of these hit",15,AMBER,bold=True,after=8)
for it in ["Finance puts the cost of a 6-month PVA outage above ~$700k (10% risk) or ~$1.4M (5% risk)",
           "A credible SNP risk signal: financial stress, key-person loss, capacity strain, a missed lot, or an unexplained price move",
           "PCI's real price comes in at or below ~$1.50/lb — the premium then drops to ~$17k/yr and the calculus flips",
           "Volume growth or a new hydrogel line makes PVA a larger, more strategic spend",
           "SNP declines the partnership or continuity terms"]:
    par(tf.add_paragraph(),"•  "+it,12.5,GREY,after=7)
takeaway(s,"We keep the option, strengthen the source we depend on, and spend ~$10k/yr instead of ~$68k — with clear triggers to escalate.")

# ---------- 13 ASKS ----------
s=slide(); title_bar(s,"What we need from you",12,N)
items=[("1","A number: what does a 6-month liquid-PVA outage cost the business?","Finance + Ops · this is the input that makes the break-even rigorous"),
       ("2","Approval to formalize the SNP partnership (forecast sharing, continuity terms in the SQA)","Leadership · signals intent to SNP; legal/quality support"),
       ("3","Budget for the warm backup: ~$15k one-time + ~$10k/yr","Leadership · small, reversible"),
       ("4","Confirm the volume outlook (+10%/yr) and any new hydrogel lines in plan","Product/R&D · drives both the premium and the strategic weight of PVA"),
       ("5","Agreement on the escalation triggers on the previous slide","Leadership · so we don't re-litigate this each quarter")]
y=1.35
for n,a,who in items:
    rect(s,0.6,y,0.7,0.85,NAVY); tf=box(s,0.6,y+0.18,0.7,0.5); par(tf.paragraphs[0],n,20,WHITE,bold=True,align=PP_ALIGN.CENTER)
    rect(s,1.4,y,7.3,0.85,LIGHT); tf=box(s,1.55,y+0.1,7.1,0.7); tf.vertical_anchor=MSO_ANCHOR.MIDDLE; par(tf.paragraphs[0],a,13,NAVY,bold=True)
    rect(s,8.8,y,3.9,0.85,PALE); tf=box(s,8.9,y+0.1,3.7,0.7); tf.vertical_anchor=MSO_ANCHOR.MIDDLE; par(tf.paragraphs[0],who,11,GREY)
    y+=0.98
takeaway(s,"With #1 in hand, we can restate the recommendation in one line: the premium is, or is not, cheaper than the expected loss.")

# ---------- 14 APPENDIX: EVIDENCE ----------
s=slide(); title_bar(s,"Appendix · What the evidence says about dual vs single sourcing",13,N)
EVIDENCE = [
 ("Bottleneck items call for securing supply, not splitting it. ","Kraljic's portfolio model classifies low-spend/high-risk items as 'bottleneck'; the prescribed strategies are volume insurance, vendor control, contingency planning and security of supply — a second source is one tool among several. (Kraljic, Harvard Business Review, 1983)"),
 ("Exposure = recovery time vs survival time. ","Simchi-Levi's Time-to-Recover / Time-to-Survive model (MIT; Harvard Business Review 2014, Ford case) quantifies risk as the gap between how long we can run without a supplier and how long it takes to replace them — here ~2.5 weeks vs 6–12 months."),
 ("Mitigation vs contingency depends on disruption profile. ","Tomlin (Management Science, 2006) shows that for rare, long disruptions a contingent backup is often preferable to carrying a dual source continuously — the theoretical basis for the 'warm backup' option."),
 ("Dual-sourcing surged after 2020, then cooled on cost. ","McKinsey's supply-chain surveys reported the majority of companies pursued dual-sourcing for critical inputs in 2021–22; later surveys show many scaling resilience investments back as the cost became visible. Resilience is bought, not free."),
 ("Being a preferred customer is a risk lever. ","Customer-attractiveness research (Schiele et al.) shows suppliers allocate capacity, innovation and attention to customers they value — forecast sharing and joint development are the documented ways to earn that status."),
 ("Regulators require controlled, risk-proportionate suppliers — not two of them. ","FDA's QMSR (21 CFR 820, incorporating ISO 13485:2016 clause 7.4) and GHTF/SG3/N17 require supplier evaluation and controls proportionate to risk; a documented risk assessment and contingency plan is the expectation for a sole source."),
]
bullets(s,0.6,1.2,12.1,5.3,EVIDENCE,size=12,gap=8)
tf=box(s,0.6,6.65,12.1,0.5); par(tf.paragraphs[0],"Sources listed on the next page. Claims were fact-checked independently; see the accompanying research memo for the verification record.",10,GREY,italic=True)

# ---------- 15 APPENDIX: ASSUMPTIONS + GLOSSARY ----------
s=slide(); title_bar(s,"Appendix · Assumptions, sources and acronyms")
rows=[["Assumption","Value","Basis"],
 ["Demand today","1,300 lb/week ≈ 150 drums/yr","Confirmed 2026-06-26"],
 ["SNP price","$0.75/lb delivered, $337.50/drum","SNP Estimate 012726-1"],
 ["PCI price forecast","$2.50 low · $3.75 mid · $5.00 high per lb","Leadership range; PCI not yet quoted"],
 ["Share to second source","1/3 (Option A) · 5% (Option C)","Leadership assumption"],
 ["Volume growth","+10% per year","Leadership assumption"],
 ["Market reference","$0.85 / $1.40 / $2.55 per lb","Resin floor + labor build-up + retail ceiling"],
 ["CJB quote","$8.00–8.50/lb toll excl. materials ≈ $8.42/lb landed","CJB email 'RE: mix test'"],
 ["Qualification cost","~$15k one-time","PLACEHOLDER — to confirm"],
 ["Outage cost","not yet estimated","NEEDED from Finance/Ops"]]
table(s,0.6,1.2,7.4,4.7,rows,[2.2,2.9,2.3],size=10.5)
rect(s,8.25,1.2,4.45,5.6,PALE,STEEL); tf=box(s,8.4,1.3,4.2,5.4)
par(tf.paragraphs[0],"Acronyms",13,NAVY,bold=True,after=6)
for k,v in [("PVA","polyvinyl alcohol"),("SNP","our incumbent PVA supplier"),("PCI","candidate second supplier (in testing)"),("CJB","toll blender that quoted ~11× SNP"),
            ("cP","centipoise — viscosity unit"),("CoA","Certificate of Analysis"),("SQA","Supplier Quality Agreement"),("RFQ","Request for Quotation"),
            ("TTS / TTR","Time-to-Survive / Time-to-Recover"),("QMSR","FDA Quality Management System Regulation"),("ISO 13485","medical-device quality standard"),("GHTF","Global Harmonization Task Force")]:
    p=tf.add_paragraph(); r=p.add_run(); r.text=k+"  "; r.font.bold=True; r.font.size=Pt(10.5); r.font.color.rgb=NAVY; r.font.name="Calibri"
    r2=p.add_run(); r2.text="— "+v; r2.font.size=Pt(10.5); r2.font.color.rgb=GREY; r2.font.name="Calibri"; p.space_after=Pt(4)
tf=box(s,0.6,6.05,7.4,0.9); par(tf.paragraphs[0],"Full model: PVA_Second_Supplier_Leadership_Model.xlsx (all inputs editable). Research memo with verified sources accompanies this deck.",10,GREY,italic=True)


# ---------- SPEAKER NOTES (talk track, in sequence) ----------
NOTES = [
 "Today I am asking for a decision on one supply-risk item: liquid PVA. About 12 minutes: what changed since July, what a second supplier truly costs, the alternative, and a recommendation with clear triggers.",
 "Headline first. A full second source would cost 80-190% of today's PVA spend - far more than the ~$6-12k we estimated in July. The reason is price: realistic $2.50-5.00/lb versus the $1.00-1.25 we assumed. My recommendation: strengthen SNP AND keep PCI as a warm backup, escalating to a full split only on defined triggers. The one number I need from you is what a six-month outage would cost the business.",
 "The risk itself has not changed. Sole source; 18-day shelf life, so about two and a half weeks of survival if SNP stops. Recovery - qualifying a replacement - has taken us six months. When recovery time exceeds survival time, that is the definition of exposure. In procurement terms this is a bottleneck item: small spend, critical input. The textbook answer is to secure supply, not chase price.",
 "94 suppliers screened. Most cannot hold the 90-95 C cook; most of the rest have batch minimums that overshoot an 18-day shelf life. The one toll quote we got was about 11 times SNP. PCI is promising - viscosity root cause found, spec agreed - but not yet qualified. The lesson: from zero, an SNP failure means 6-12 months of exposure at crisis prices. THAT is what a second source insures against.",
 "Each bar is the extra we would pay per year if a second source takes a third of volume at that price. The drums are bought either way; the premium is the decision number. PCI at $2.50-5.00 means +$39k to +$96k a year. Green is what we described in July. Red is the CJB quote, for scale. Not on the chart: if SNP re-prices the two-thirds it keeps, add $3-7k.",
 "Volume grows about 10% a year, so the premium compounds: $240k to $585k over five years for a full split, versus about $62k for a warm backup. Any second source also carries a one-time qualification cost - roughly $15k as a placeholder.",
 "Let me be honest about what the money buys and does not. It buys a practiced supplier and price discipline. It does NOT buy full protection - two-thirds of our volume still stops unless PCI can ramp, and we have not confirmed they can. And it sends SNP a signal at exactly the moment we are asking them to co-develop new hydrogels with us.",
 "Option B: keep SNP but manage the dependency deliberately. Share the forecast; make the hydrogel co-development a standing program; write continuity terms into the quality agreement; and the lever people miss - buffer the RESIN, not the solution. Dry PVA resin is shelf-stable for years; the solution is not. Total cost: a few thousand dollars and some engineering time. Residual risk: a true SNP failure still means months of exposure.",
 "Option C: finish PCI's qualification, then keep them warm at about 5% - one drum every seven weeks. Roughly $10k a year. It turns six months of sunk effort into a standing option. Two failure modes to manage: 5% may be too little for PCI to care, so we need an explicit readiness understanding; and we must confirm in writing that they can ramp.",
 "Here is the test leadership can apply: the premium is worth paying only if it is less than the probability of an outage times the loss the backup would avoid. Mid case, a full split at $68k a year: at a 5% annual risk the outage must cost more than $1.35M to justify it; at 10%, about $680k. The warm backup clears the bar at $200k and $100k. I do not have the outage cost - that is the input I need from Finance and Operations.",
 "Side by side. B and C are not alternatives to each other - together they are the balanced answer at our current volume. A full split is right only if the outage cost is well over half a million dollars, or if SNP shows real fragility.",
 "The recommendation. Do now: formalize the SNP partnership, put resin on consignment, finish PCI, start the 5% trickle, keep the cold-start kit current. Escalate to a full split on any of these triggers: an outage-cost number above the threshold, an SNP risk signal, PCI pricing at or below $1.50, volume growth or a new hydrogel line, or SNP declining the partnership.",
 "Five asks. The first is the one that matters: with the outage-cost number, I can restate this whole recommendation in one line.",
 "For the record, the frameworks and evidence: Kraljic on bottleneck items; Simchi-Levi's time-to-recover versus time-to-survive; Tomlin on when a contingent backup beats continuous dual-sourcing; McKinsey's surveys showing dual-sourcing surged after 2020 and then cooled as the cost became visible; customer-attractiveness research on earning preferred-customer status; and what FDA and ISO actually require of a sole source - controls proportionate to risk, not two suppliers.",
 "Assumptions, sources, and acronyms for reference. The full model is in the workbook; every input is editable.",
]
for sl, txt in zip(prs.slides, NOTES):
    sl.notes_slide.notes_text_frame.text = txt

prs.save("PVA_Second_Supplier_Leadership_Deck.pptx"); print("saved deck:", len(prs.slides._sldIdLst), "slides")
