#!/usr/bin/env python3
"""SNP site visit — printable working agenda with write-on space."""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Flowable, Table, TableStyle, KeepTogether,
                                PageBreak)

NAVY   = colors.HexColor("#1F3864")
STEEL  = colors.HexColor("#4E79A7")
GREY   = colors.HexColor("#595959")
RULE   = colors.HexColor("#C9CFD6")
BAND   = colors.HexColor("#EAEEF4")
GOLD   = colors.HexColor("#FFF3D0")
GOLDLN = colors.HexColor("#E0B84C")

W, H = LETTER
LM = RM = 0.6*inch
TM = 0.62*inch
BM = 0.55*inch

def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

S_TITLE = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=17, leading=20, textColor=NAVY)
S_SUB   = ParagraphStyle("s", fontName="Helvetica-Oblique", fontSize=8.8, leading=11, textColor=GREY)
S_SEC   = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=11.5, leading=14, textColor=colors.white)
S_SUBH  = ParagraphStyle("sh", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=NAVY,
                         spaceBefore=2, spaceAfter=3)
S_Q     = ParagraphStyle("q", fontName="Helvetica", fontSize=9.3, leading=12.2, textColor=colors.black,
                         leftIndent=11, bulletIndent=2, spaceAfter=1.5)
S_NOTE  = ParagraphStyle("n", fontName="Helvetica-Oblique", fontSize=8.4, leading=10.8, textColor=GREY,
                         leftIndent=11, spaceAfter=2)
S_BOX   = ParagraphStyle("b", fontName="Helvetica", fontSize=9, leading=12, textColor=colors.black)
S_BOXB  = ParagraphStyle("bb", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=NAVY)
S_FOOT  = ParagraphStyle("f", fontName="Helvetica", fontSize=7.5, textColor=GREY)


class Rules(Flowable):
    """Ruled lines for handwriting."""
    def __init__(self, n=3, gap=17, indent=11, color=RULE):
        Flowable.__init__(self); self.n=n; self.gap=gap; self.indent=indent; self.color=color
    def wrap(self, aw, ah):
        self.width = aw
        return (aw, self.n*self.gap + 3)
    def draw(self):
        c = self.canv
        c.setStrokeColor(self.color); c.setLineWidth(0.45)
        y = self.n*self.gap
        for _ in range(self.n):
            c.line(self.indent, y, self.width, y)
            y -= self.gap


class Band(Flowable):
    """Navy section header band."""
    def __init__(self, text, h=19, fill=NAVY, fg=colors.white, size=11.5):
        Flowable.__init__(self); self.text=text; self.h=h; self.fill=fill; self.fg=fg; self.size=size
    def wrap(self, aw, ah):
        self.width = aw
        return (aw, self.h+4)
    def draw(self):
        c=self.canv
        c.setFillColor(self.fill); c.rect(0, 2, self.width, self.h, stroke=0, fill=1)
        c.setFillColor(self.fg); c.setFont("Helvetica-Bold", self.size)
        c.drawString(6, 2+self.h/2-self.size*0.36, self.text)


class CheckRow(Flowable):
    """A checkbox followed by text."""
    def __init__(self, text, size=9.3, box=9, gap=16):
        Flowable.__init__(self); self.text=text; self.size=size; self.box=box; self.gap=gap
    def wrap(self, aw, ah):
        self.width=aw
        return (aw, self.gap)
    def draw(self):
        c=self.canv
        c.setStrokeColor(NAVY); c.setLineWidth(0.8)
        c.rect(2, 1.5, self.box, self.box, stroke=1, fill=0)
        c.setFillColor(colors.black); c.setFont("Helvetica", self.size)
        c.drawString(2+self.box+6, 3.5, self.text)


def boxed(flowables, fill=BAND, line=STEEL, pad=7):
    t = Table([[flowables]], colWidths=[W-LM-RM])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), fill),
        ("BOX",(0,0),(-1,-1), 0.9, line),
        ("LEFTPADDING",(0,0),(-1,-1), pad+3),
        ("RIGHTPADDING",(0,0),(-1,-1), pad),
        ("TOPPADDING",(0,0),(-1,-1), pad),
        ("BOTTOMPADDING",(0,0),(-1,-1), pad),
    ]))
    return t


def q(text):
    return Paragraph(esc(text), S_Q, bulletText="•")
def note(text):
    return Paragraph(esc(text), S_NOTE)
def subh(text):
    return Paragraph(esc(text), S_SUBH)


# ---------------- build ----------------
story = []
A = story.append

# ---- header ----
A(Paragraph("SNP — Site Visit Working Agenda", S_TITLE))
A(Paragraph("Personal prep document. Not for distribution.", S_SUB))
A(Spacer(1, 7))

hdr = Table([
    [Paragraph("<b>Date</b>", S_BOX), "", Paragraph("<b>Location</b>", S_BOX), ""],
    [Paragraph("<b>SNP attendees</b>", S_BOX), "", Paragraph("<b>Ours</b>", S_BOX), ""],
], colWidths=[1.05*inch, 2.45*inch, 0.8*inch, 3.0*inch], rowHeights=[20,20])
hdr.setStyle(TableStyle([
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("LINEBELOW",(1,0),(1,-1),0.6,RULE),
    ("LINEBELOW",(3,0),(3,-1),0.6,RULE),
    ("LEFTPADDING",(0,0),(-1,-1),0),
    ("BOTTOMPADDING",(0,0),(-1,-1),2),
]))
A(hdr)
A(Spacer(1, 9))

# ---- before you go ----
inner = [
    Paragraph("BEFORE YOU GO", S_BOXB), Spacer(1,3),
    Paragraph(esc("Do not signal the second-source work. Every technical question here has a truthful cover: we are formalising internal "
                  "spec documentation. That is genuinely true and it explains all of it."), S_BOX),
    Spacer(1,4),
    Paragraph(esc("Strategic frame worth testing today: our research concluded SNP is a PVA-cooking specialist — it is their product line, "
                  "not a side job — which is exactly why $0.75/lb has been hard to beat (market base ~$1.40/lb). An outside second source "
                  "costs +$11k–$43k/yr. So the real question is whether redundancy INSIDE SNP — second line, second site, staged resin, "
                  "safety stock — buys more continuity per dollar. If it does, it reframes the whole initiative."), S_BOX),
    Spacer(1,4),
    Paragraph(esc("One discipline: you will want to fill silences by explaining why you are asking. Don't."), S_BOX),
]
A(boxed(inner, fill=GOLD, line=GOLDLN))
A(Spacer(1, 8))

# ---- quick reference ----
ref = [[Paragraph("<b>OUR NUMBERS — quick reference</b>", S_BOXB), ""],
       [Paragraph(esc("Volume: ~1,300 lb/week · 450 lb/drum · ~150 drums/yr"), S_BOX),
        Paragraph(esc("Price: $0.75/lb delivered ≈ $337.50/drum ≈ $50,700/yr"), S_BOX)],
       [Paragraph(esc("Spec: 10–12% solids · <2,500 cps (#3, 10 rpm, 25 °C)"), S_BOX),
        Paragraph(esc("Shelf life: 18 days · fresh material typically <1,000 cps"), S_BOX)],
       [Paragraph("<b>Open gaps we can close today:</b> pH target &#183; viscosity lower bound &#183; colour standard &#183; "
                  "exact resin grade &#183; cleanup procedure &#183; hazard classification &#183; drum spec &#183; test method", S_BOX), ""]]
t = Table(ref, colWidths=[(W-LM-RM)/2]*2)
t.setStyle(TableStyle([
    ("SPAN",(0,0),(1,0)), ("SPAN",(0,3),(1,3)),
    ("BACKGROUND",(0,0),(-1,-1), BAND),
    ("BOX",(0,0),(-1,-1),0.9,STEEL),
    ("INNERGRID",(0,1),(-1,2),0.3,colors.white),
    ("LEFTPADDING",(0,0),(-1,-1),8), ("RIGHTPADDING",(0,0),(-1,-1),8),
    ("TOPPADDING",(0,0),(-1,-1),5), ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("VALIGN",(0,0),(-1,-1),"TOP"),
]))
A(t)
A(Spacer(1, 11))

# =============== PART A ===============
def block(title, items, notes=(), rules=4):
    fl = [subh(title)]
    for x in items: fl.append(q(x))
    for n in notes: fl.append(note(n))
    fl.append(Rules(rules))
    fl.append(Spacer(1, 8))
    return KeepTogether(fl)

A(Band("PART A  —  YOUR TEAM'S ASKS"))
A(Spacer(1, 5))

A(block("1 \u00b7 Drum recycling", [
 "Do you run a returnable / reconditioned drum program? Could empties go back on the SAME truck that delivers (backhaul, no added freight)?",
 "Who owns cleaning, and does our residue qualify as RCRA-empty?",
 "Does returning drums reduce our per-drum price — and by how much?",
 "Do you offer recycled-content or reconditioned drums as an option?",
 "What drum do you use for us today — poly or steel, open or tight head?",
], [
 "Our angle: water-soluble PVA rinses with hot water, unlike solvent or hazardous residues — that makes our drums unusually good "
 "reconditioning candidates. ~150 drums/yr also maps to Intuitive sustainability targets, which is an internal win to report.",
], 4))

A(block("2 \u00b7 CoA vs CoC — Tom's item   \u2605 highest-value item of the visit", [
 "Move us from Certificate of CONFORMANCE to Certificate of ANALYSIS. Fields: lot #, production date, % total solids, final pH, viscosity.",
 "\u2605 Your exact viscosity METHOD: instrument series (LV / RV / HA / HB), spindle designation, RPM, temperature + tolerance, and reading time.",
 "Can we get 12–24 months of historical CoA data?",
 "Do you keep retained samples, and for how long?",
], [
 "Why the method matters: 'spindle #3, 10 rpm, 25 \u00b0C' is NOT a complete method. LV-3 and RV-3 are different geometries and impose "
 "different shear rates, so they give different numbers on a shear-thinning fluid like ours. SNP's method is the de facto reference "
 "standard — and right now we don't know it.",
 "Why the history matters: one dataset closes three gaps at once — the missing pH target and tolerance, a real viscosity LOWER bound, "
 "and normal batch-to-batch variation.",
], 6))

A(block("3 \u00b7 Other hydrogels — the engineers' interest", [
 "What other water-soluble polymer solutions do you make? (PVP, PEG, cellulosics — HEC/HPMC, alginate, polyacrylamide, gelatin, carbomer)",
 "Can you formulate blends — PVA/PVP, PVA/gelatin? Do you have R&D / formulation support to help develop variants?",
 "To tune mechanical properties, what levers do you see: PVA molecular weight and hydrolysis grade, solids loading, blends, or chemical "
 "crosslinking (borate, glutaraldehyde) vs our physical freeze/thaw route?",
 "Do you have freeze/thaw cryogel experience? Cycle count, freeze rate and solids all tune stiffness — they may know things we don't.",
], [
 "Strategic read: if SNP can make several hydrogel chemistries they stop being a commodity supplier and become a development partner. "
 "That is an argument for deepening the relationship rather than diversifying away from it.",
], 5))

A(block("4 \u00b7 Their volume, capacity, and where we sit", [
 "Total plant capacity — how many reactors, what sizes, one site or several?",
 "What fraction of your output are we? (We're ~150 drums, ~34 tons/yr — likely a very small account.)",
 "Where do we sit in your customer mix? Does our weekly cadence cause friction, or fit neatly?",
 "Lead time normally vs at peak. Is there a busy season?",
 "\u2605 If your primary reactor goes down, what happens to us?",
], [
 "Knowing our share honestly tells you two things at once: how much leverage you have, and how easy you are for them to serve. "
 "The last question is the redundancy question, asked innocently.",
], 5))

A(Spacer(1, 4))

# =============== PART B ===============
A(Band("PART B  —  MY ADDITIONS"))
A(Spacer(1, 5))

A(block("5 \u00b7 Business continuity  (the strategic one)", [
 "Do you have a documented BCP? A second line or second site that could run our product?",
 "Could you pre-stage or hold safety stock of our resin, so an upstream disruption doesn't stop our drums?",
 "Would you support us holding a buffer — and what actually limits that?",
], (), 4))

A(block("6 \u00b7 Shelf life — why 18 days?", [
 "\u2605 What actually limits the 18 days: microbial growth, viscosity build, phase separation, or pigment settling?",
 "What is the viscosity at time of MANUFACTURE vs what we measure on receipt? Confirm the build behaviour.",
 "If we restructured the spec as fresh target + end-of-life ceiling, could the usable window be longer?",
], [
 "This is upstream of a lot of our economics. If the limit is viscosity build rather than microbiology, a longer window would change "
 "order cadence, allow larger batches, and materially lower the cost of any second source. We've treated 18 days as a given and never "
 "asked what drives it.",
], 5))

A(block("7 \u00b7 Close our open spec gaps — they can answer every one of these", [
 "Exact resin grade and manufacturer. Our notes say 'Selvol S-1551F-D or equivalent' but that code doesn't match Sekisui's usual "
 "catalogue numbering. (May be treated as proprietary — frame as continuity documentation.)",
 "pH target and tolerance — currently missing entirely from our spec.",
 "Colour standard — is there an L*a*b* target with a \u0394E tolerance, or is a retain used as the visual standard?",
 "Cleanup procedure — theirs, in writing.",
 "Hazard classification: flammable / corrosive / toxic / MARINE POLLUTANT? (The biocide is aquatic-toxic; whether the diluted product "
 "trips the threshold is a real question and their SDS answers it.)",
 "Who authors the SDS, and can we have the current version?",
], (), 6))

A(block("8 \u00b7 Commercial — light touch", [
 "Volume tiers — is there a break at higher annual volume?",
 "Would an annual agreement buy price stability? How do raw-material moves pass through?",
 "Payment terms. Any freight optimisation if we adjusted order size or frequency?",
], ["Frame as budgeting and forecasting, not negotiation."], 4))

A(block("9 \u00b7 People", [
 "Named technical contact + their backup. QA contact for CoA questions.",
], ["Single-point-of-contact risk is real for a small account."], 3))

A(PageBreak())

# =============== WALK OUT WITH ===============
A(Band("WHAT TO WALK OUT WITH"))
A(Spacer(1, 8))
for x in [
 "Their exact viscosity test method, written down — the reference standard everything else is judged against.",
 "A commitment to CoA instead of CoC, with the fields agreed.",
 "Historical CoA data, or a firm promise of it — closes the pH and viscosity-bound gaps in one step.",
 "A straight answer on what actually limits shelf life.",
 "A read on whether internal redundancy at SNP is real — if it is, it is likely cheaper and faster than anything we've been chasing.",
 "Named technical + QA contacts.",
]:
    A(CheckRow(x)); A(Spacer(1,4))
A(Spacer(1, 10))

A(Band("FOLLOW-UPS  /  ACTIONS", fill=STEEL))
A(Spacer(1, 4))
owner = Table([[Paragraph("<b>Action</b>", S_BOX), Paragraph("<b>Owner</b>", S_BOX), Paragraph("<b>By when</b>", S_BOX)]],
              colWidths=[(W-LM-RM)*0.62, (W-LM-RM)*0.19, (W-LM-RM)*0.19])
owner.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),BAND),("BOX",(0,0),(-1,-1),0.5,RULE),
                           ("INNERGRID",(0,0),(-1,-1),0.5,RULE),
                           ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4)]))
A(owner)
rows=[[ "", "", "" ] for _ in range(9)]
tt=Table(rows, colWidths=[(W-LM-RM)*0.62,(W-LM-RM)*0.19,(W-LM-RM)*0.19], rowHeights=[21]*9)
tt.setStyle(TableStyle([("BOX",(0,0),(-1,-1),0.5,RULE),("INNERGRID",(0,0),(-1,-1),0.5,RULE)]))
A(tt)

A(PageBreak())
A(Band("NOTES"))
A(Spacer(1, 8))
A(Rules(34, gap=20, indent=0))

A(PageBreak())
A(Band("NOTES"))
A(Spacer(1, 8))
A(Rules(34, gap=20, indent=0))


# ---------------- doc ----------------
def footer(canv, doc):
    canv.saveState()
    canv.setStrokeColor(RULE); canv.setLineWidth(0.5)
    canv.line(LM, BM-8, W-RM, BM-8)
    canv.setFont("Helvetica", 7.5); canv.setFillColor(GREY)
    canv.drawString(LM, BM-19, "SNP site visit — working agenda · personal prep, not for distribution")
    canv.drawRightString(W-RM, BM-19, "Page %d" % doc.page)
    canv.restoreState()

out = "/home/user/Claude-Works/PVA second supplier initiative/SNP_Visit_Agenda.pdf"
doc = BaseDocTemplate(out, pagesize=LETTER,
                      leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM+14,
                      title="SNP Site Visit — Working Agenda", author="Oscar Penny")
frame = Frame(LM, BM+14, W-LM-RM, H-TM-BM-14, id="f", leftPadding=0, rightPadding=0,
              topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=footer)])
doc.build(story)
print("saved", out)
