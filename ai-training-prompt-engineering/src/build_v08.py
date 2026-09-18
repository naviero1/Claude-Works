#!/usr/bin/env python3
"""v08 — owner-approved pass (in session, 2026-09-18).

Owner-approved changes, all in one deterministic build over v07:

A. The seven approved TYPE THIS prompt sets (channel instruction 21, wording
   verbatim; owner in session: "yes, apply the changes from Beebop as well").
   New panels in the deck's own prompt idiom on live slides 2, 7, 8, 9, 11, 12;
   replacement of the existing wording on 23, 77, 78.
B. Tokens slide 8 reclassified REFERENCE -> TEACH (timing kept).
C. Owner: big "term to remember" badges on definitional slides
   (TOKENS 8, CONTEXT WINDOW 9, RAG 10, REASONING EFFORT 11,
   HALLUCINATION 13, MoE 23, ARTIFACT 31).
D. Owner: restyle model-selection slides 18/19 to the house idiom.
E. Owner: slide 22 (four context failures) "very important" - live TEACH
   chrome and heavier failure-term typography.
F. Owner reorder: 20 before 18; 23 (DeepSeek) directly after 19; 21
   (chat/workflow/agent) leaves the live flow to self-study.
G. Owner: craft slides 25, 26, 28, 29, 30 "prettier and more impacting" -
   background tint, kicker, card fills, teal labels, takeaway accent
   (27 untouched: it carries the approved pilot treatment).
H. Owner: slide 31 kicker must not claim to be a Part.

Input: v07 (113).  Output: From_Prompts_to_Agents_Visual_Pilot_v08.pptx (113).
"""
import copy
import os
import re

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE
from pptx.dml.color import RGBColor
from pptx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "notes", "visual-polish", "pilot", "From_Prompts_to_Agents_Visual_Pilot_v07.pptx")
OUT = os.path.join(ROOT, "notes", "visual-polish", "pilot", "From_Prompts_to_Agents_Visual_Pilot_v08.pptx")

TEAL = "0E7C7B"
TEAL_D = "0A5B5A"
CHIP_TEACH = "0A6261"
INK = "232A31"
CHROME = "526267"
GRAY = "657278"
AMBER = "B96A1B"
BODY = "46545F"

# ---------------- approved prompt wording (instruction 21, verbatim) --------
P1 = [("SEND 1", "Use this chat as my course log. When I request a report, use only the conversation available to you and flag any gaps. Acknowledge briefly."),
      ("SEND 2", "Write a farewell message for a coworker in about 50 words."),
      ("SEND 3", "Before revising, ask up to three questions that would most improve the message. Wait for my answers, then revise it.")]
P2 = [("SEND 1", "Finish this sentence five different ways: “We should review the launch date because…” Treat each ending as a hypothetical possibility."),
      ("SEND 2", "Repeat using these facts: we are a business-to-business software company; our beta ends April 20; a competitor launches May 3. Separate supplied facts from assumptions. End with one missing fact that could change the timing decision.")]
P3 = [(None, "Explain tokens to a new colleague using a LEGO-brick analogy, in about 100 words. Show an illustrative word split and explain why the actual split depends on the tokenizer. Connect token counts to context limits and charges when billing is based on tokens. End with one practical implication for working with long documents.")]
P4 = [("SEND 1", "Explain a context window using a desk analogy, in about 100 words. What occupies the desk, and what happens as it fills? Distinguish information available for the current response from saved chat history and optional memory. Identify what depends on the application. End with one useful habit for continuing a long task."),
      ("HANDOFF FOLLOW-UP", "Create a concise HANDOFF from the conversation currently available: goal, decisions, constraints, unresolved questions, and next action. Name any files needed to continue. Mark missing information rather than inventing it.")]
P5 = [(None, "Explain when to start with fast responses versus more reasoning, using three examples: a routine email, inconsistent supplier data, and a problem with several interacting causes. For each, give a starting choice and what would justify increasing effort. Explain the tradeoff in time and resource use without guessing prices. About 120 words.")]
P6 = [(None, "Using the supplied screenshot or copied text of my app’s menu, explain each visible mode in one line: its purpose and a suitable workplace task. Mark anything the supplied information does not establish as needing verification. If the menu is missing, ask for it first.")]
P7 = [(None, "Explain Mixture of Experts using a specialist-hospital analogy, in about 120 words. Describe how selected computational components handle each token and how activating only a subset can reduce computation. Explain one way the hospital analogy can mislead, and why lower computation alone does not determine customer prices.")]


def sh_by_name(slide, name):
    for sh in slide.shapes:
        if sh.name == name:
            return sh
    return None


def set_geom(sh, y=None, x=None, w=None, h=None):
    if y is not None: sh.top = Inches(y)
    if x is not None: sh.left = Inches(x)
    if w is not None: sh.width = Inches(w)
    if h is not None: sh.height = Inches(h)


def clear_tf(tf):
    for p in list(tf.paragraphs):
        for r in list(p.runs):
            r._r.getparent().remove(r._r)
    # keep first paragraph, drop the rest
    ps = tf.paragraphs
    for p in list(ps[1:]):
        p._p.getparent().remove(p._p)
    return tf.paragraphs[0]


def add_run(p, text, sz, bold, color, name="Calibri"):
    r = p.add_run()
    r.text = text
    r.font.size = Pt(sz)
    r.font.bold = bold
    r.font.name = name
    r.font.color.rgb = RGBColor.from_string(color)
    return r


def fill_prompt_body(tf, sends, sz=9.5):
    """Write the approved sends into a prompt body text frame, house style."""
    first = True
    for label, text in sends:
        p = clear_tf(tf) if first else tf.add_paragraph()
        first = False
        p.alignment = PP_ALIGN.LEFT
        if label:
            add_run(p, f"{label} · ", sz + 0.5, True, AMBER)
        add_run(p, "TYPE THIS → ", sz + 0.5, True, TEAL_D)
        add_run(p, f"“{text}”", sz, False, INK)


def add_prompt_panel(dest_slide, tmpl_slide, y, h, num, title, sends,
                     tab=None, body_sz=9.5, x=0.55, w=12.20):
    """Copy the deck's own prompt-panel idiom (from slide 77) onto a slide,
    with explicit geometry so bodies and notes never collide."""
    tmpl = {}
    for nm in ("Shape 25", "Shape 26", "Image 6", "Shape 27",
               "Text 28", "Text 29", "Text 30", "Text 31"):
        tmpl[nm] = sh_by_name(tmpl_slide, nm)
    spTree = dest_slide.shapes._spTree
    new = {}
    for nm, sh in tmpl.items():
        el = copy.deepcopy(sh._element)
        spTree.append(el)
        for blip in el.iter(qn("a:blip")):
            rid = blip.get(qn("r:embed"))
            if rid:
                part = tmpl_slide.part.rels[rid].target_part
                from pptx.opc.constants import RELATIONSHIP_TYPE as RT
                blip.set(qn("r:embed"), dest_slide.part.relate_to(part, RT.IMAGE))
        new[nm] = dest_slide.shapes[-1]
    set_geom(new["Shape 25"], y=y, x=x, w=w, h=h)
    set_geom(new["Shape 26"], y=y + 0.12, x=x + 0.16)
    set_geom(new["Image 6"], y=y + 0.22, x=x + 0.26)
    set_geom(new["Shape 27"], y=y + 0.14, x=x + 0.66)
    set_geom(new["Text 28"], y=y + 0.15, x=x + 0.66)
    set_geom(new["Text 29"], y=y + 0.15, x=x + 2.08, w=w - 2.35)
    p = clear_tf(new["Text 28"].text_frame)
    p.alignment = PP_ALIGN.CENTER
    add_run(p, f"PROMPT {num}/7", 9.5, True, "FFFFFF")
    p = clear_tf(new["Text 29"].text_frame)
    add_run(p, title, 11, True, TEAL_D)
    body = new["Text 30"]
    body.text_frame.word_wrap = True
    body.text_frame.auto_size = MSO_AUTO_SIZE.NONE
    fill_prompt_body(body.text_frame, sends, sz=body_sz)
    note_h = 0.27 if tab else 0.05
    set_geom(body, y=y + 0.50, x=x + 0.20, w=w - 0.40,
             h=max(0.30, h - 0.50 - note_h))
    if tab:
        note = new["Text 31"]
        set_geom(note, y=y + h - 0.28, x=x + 0.20, w=w - 0.40, h=0.24)
        p = clear_tf(note.text_frame)
        add_run(p, f"✂ copy-paste, don’t retype: tab {tab} of your Course Workbook",
                9.5, False, TEAL_D)
    else:
        new["Text 31"]._element.getparent().remove(new["Text 31"]._element)


def shrink_row_fonts(slide, n_rows, label_sz, body_sz):
    for i in range(n_rows):
        for kind, sz in (("label", label_sz), ("body", body_sz)):
            sh = sh_by_name(slide, f"row-{i}-{kind}")
            if sh is not None:
                for p in sh.text_frame.paragraphs:
                    for r in p.runs:
                        r.font.size = Pt(sz)


def add_term_badge(slide, term, x=9.42, y=1.30, w=3.25, sub=None, sz=24):
    from pptx.enum.shapes import MSO_SHAPE
    sp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y),
                                Inches(w), Inches(0.95))
    sp.name = "term-badge"
    sp.shadow.inherit = False
    sp.fill.background()
    sp.line.fill.background()
    tf = sp.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, Inches(0.0))
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    add_run(p, "R E M E M B E R", 8.5, True, CHROME)
    p2 = tf.add_paragraph()
    p2.alignment = PP_ALIGN.RIGHT
    add_run(p2, term, sz, True, TEAL)
    if sub:
        p3 = tf.add_paragraph()
        p3.alignment = PP_ALIGN.RIGHT
        r = add_run(p3, sub, 9, False, GRAY)
        r.font.italic = True


def shrink_rows(slide, n_rows, y0, h, step):
    for i in range(n_rows):
        for kind in ("label", "body"):
            sh = sh_by_name(slide, f"row-{i}-{kind}")
            if sh is not None:
                set_geom(sh, y=y0 + i * step, h=h)


def shrink_cols(slide, body_h):
    for nm in ("left-body", "right-body"):
        sh = sh_by_name(slide, nm)
        if sh is not None:
            sh.height = Inches(body_h)


def set_mode(slide, text, teach):
    bar = sh_by_name(slide, "FACILITATION_MODE_BAR")
    if bar is not None:
        bar.fill.solid()
        bar.fill.fore_color.rgb = RGBColor.from_string(TEAL if teach else "A7B0B5")
    chip = sh_by_name(slide, "mode")
    if chip is not None:
        for p in chip.text_frame.paragraphs:
            for r in p.runs:
                r.text = text
                r.font.color.rgb = RGBColor.from_string(CHIP_TEACH if teach else "5D6B70")


def copy_mode_chrome(dest, src_slide, text):
    spTree = dest.shapes._spTree
    for nm in ("FACILITATION_MODE_BAR", "mode"):
        sh = sh_by_name(src_slide, nm)
        el = copy.deepcopy(sh._element)
        spTree.append(el)
    chip = dest.shapes[-1]
    for p in chip.text_frame.paragraphs:
        for r in p.runs:
            r.text = text


def main():
    prs = Presentation(SRC)
    sl = list(prs.slides)
    assert len(sl) == 113
    s77 = sl[76]

    # ---------- A. prompt panels on live slides ----------
    # s2 - prompt 1/7 (3 sends); shrink columns, tab ref folded into title
    s2 = sl[1]
    shrink_cols(s2, 2.10)
    add_prompt_panel(s2, s77, y=4.98, h=1.28, num=1,
                     title="Your course log — and the first rep · tab EX1-TwoModes",
                     sends=P1, tab=None, body_sz=9)
    # s7 - prompt 2/7 (2 sends)
    s7 = sl[6]
    shrink_cols(s7, 2.10)
    add_prompt_panel(s7, s77, y=4.90, h=1.38, num=2,
                     title="Narrowing the guesses — two separate sends",
                     sends=P2, tab="EX2-Guesses", body_sz=9)
    # s8 - prompt 3/7; rows compressed and panel narrowed beside the image
    s8 = sl[7]
    shrink_rows(s8, 3, y0=2.05, h=0.85, step=0.93)
    shrink_row_fonts(s8, 3, label_sz=15, body_sz=13.5)
    add_prompt_panel(s8, s77, y=4.72, h=1.30, num=3,
                     title="Tokens, explained by the model",
                     sends=P3, tab="EX3-Tokens", body_sz=9, x=0.55, w=8.85)
    # s9 - prompt 4/7; rows compressed, panel narrowed, tab in title
    s9 = sl[8]
    shrink_rows(s9, 3, y0=2.05, h=0.85, step=0.93)
    shrink_row_fonts(s9, 3, label_sz=15, body_sz=13.5)
    add_prompt_panel(s9, s77, y=4.72, h=1.52, num=4,
                     title="The desk — explained · tab EX4-Handoff",
                     sends=P4, tab=None, body_sz=8.5, x=0.55, w=8.85)
    # s11 - prompt 5/7
    s11 = sl[10]
    shrink_cols(s11, 1.95)
    add_prompt_panel(s11, s77, y=4.82, h=1.40, num=5,
                     title="Fast responses vs more reasoning — three examples",
                     sends=P5, tab="EX5-TwoSpeeds", body_sz=9)
    # s12 - prompt 6/7; four rows compressed
    s12 = sl[11]
    shrink_rows(s12, 4, y0=2.11, h=0.72, step=0.79)
    shrink_row_fonts(s12, 4, label_sz=14, body_sz=14)
    add_prompt_panel(s12, s77, y=5.36, h=0.88, num=6,
                     title="Your app’s menu, explained · tab EX6-FeatureMenu",
                     sends=P6, tab=None, body_sz=9)

    # ---------- replacements: 23, 77, 78 ----------
    s23 = sl[22]
    t46 = sh_by_name(s23, "Text 46")
    t46.text_frame.word_wrap = True
    t46.text_frame.auto_size = MSO_AUTO_SIZE.NONE
    t46.height = Inches(0.46)
    fill_prompt_body(t46.text_frame, P7, sz=9)

    t30 = sh_by_name(s77, "Text 30")
    fill_prompt_body(t30.text_frame, P2, sz=9.5)

    s78 = sl[77]
    t26 = sh_by_name(s78, "Text 26")
    fill_prompt_body(t26.text_frame, P4, sz=9)

    # ---------- B. tokens slide 8 -> TEACH ----------
    set_mode(s8, "TEACH   0:10", teach=True)
    f8 = sh_by_name(s8, "footer")
    for p in f8.text_frame.paragraphs:
        for r in p.runs:
            if "REFERENCE" in r.text:
                r.text = "From Prompts to Agents"

    # ---------- C. term badges ----------
    add_term_badge(s8, "TOKENS")
    add_term_badge(s9, "CONTEXT WINDOW", sz=22)
    add_term_badge(sl[9], "RAG", sub="Retrieval-Augmented Generation", sz=26)
    add_term_badge(s11, "REASONING EFFORT", sz=20)
    add_term_badge(sl[12], "HALLUCINATION", sz=22)
    add_term_badge(s23, "MoE", x=10.30, y=0.55, w=2.45,
                   sub="Mixture of Experts", sz=24)
    add_term_badge(sl[30], "ARTIFACT", x=9.95, y=0.50, w=2.85, sz=22)

    # ---------- D. restyle model-selection slides 18/19 ----------
    from pptx.enum.shapes import MSO_SHAPE
    for idx, (kick, mode_src, mode_txt) in (
        (17, ("PART 2 · MODELS & TOOLS — MATCH THE MODEL TO THE JOB", s7, "TEACH   1:00")),
        (18, ("PART 2 · MODELS & TOOLS — STARTING CHOICES BY VENDOR", s8, "REFERENCE   0:30")),
    ):
        s = sl[idx]
        # background
        bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
                                Inches(13.333), Inches(7.5))
        bg.name = "BG"
        bg.shadow.inherit = False
        bg.fill.solid()
        bg.fill.fore_color.rgb = RGBColor.from_string("F7F8F6")
        bg.line.fill.background()
        s.shapes._spTree.remove(bg._element)
        s.shapes._spTree.insert(2, bg._element)
        # kicker
        kk = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.552), Inches(0.40),
                                Inches(9.5), Inches(0.30))
        kk.name = "kicker"
        kk.shadow.inherit = False
        kk.fill.background()
        kk.line.fill.background()
        p = kk.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        add_run(p, kick, 11, True, TEAL)
        # title/subtitle to house type
        ttl = sh_by_name(s, "slide-title")
        set_geom(ttl, y=0.72, x=0.552, w=12.2, h=0.60)
        for p in ttl.text_frame.paragraphs:
            p.alignment = PP_ALIGN.LEFT
            for r in p.runs:
                r.font.name = "Cambria"
                r.font.size = Pt(28)
                r.font.bold = True
                r.font.color.rgb = RGBColor.from_string(INK)
        sub = sh_by_name(s, "slide-subtitle")
        set_geom(sub, y=1.42, x=0.552, w=12.2, h=0.40)
        for p in sub.text_frame.paragraphs:
            p.alignment = PP_ALIGN.LEFT
            for r in p.runs:
                r.font.name = "Calibri"
                r.font.size = Pt(13.5)
                r.font.bold = False
                r.font.color.rgb = RGBColor.from_string(GRAY)
        copy_mode_chrome(s, mode_src, mode_txt)

    # ---------- E. slide 22 (four context failures) gets teaching weight ----
    s22 = sl[21]
    lbl = sh_by_name(s22, "FACILITATION_MODE_LABEL")
    if lbl is not None:
        for p in lbl.text_frame.paragraphs:
            for r in p.runs:
                if r.text.strip():
                    r.text = "TEACH  0:50"
                    r.font.color.rgb = RGBColor.from_string(CHIP_TEACH)
                    r.font.size = Pt(12)
    bar22 = sh_by_name(s22, "FACILITATION_MODE_BAR")
    if bar22 is not None:
        bar22.fill.solid()
        bar22.fill.fore_color.rgb = RGBColor.from_string(TEAL)
    for sh in s22.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip() in (
                "POISONING", "DRIFT", "CONFUSION", "CLASH"):
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(15)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor.from_string(TEAL)

    # ---------- G. craft slides beautify (v07 positions 25,26,28,29,30) ----
    KICKERS = {
        25: "THE CRAFT — YOU ALREADY DO THIS AT WORK",
        26: "THE CRAFT — TESTABLE BEATS VAGUE",
        28: "THE CRAFT — ROLES DESCRIBE BEHAVIOR",
        29: "THE CRAFT — ELEMENTS MAP TO REQUIREMENTS",
        30: "THE CRAFT — EXAMPLES, OUTS, AND STOP RULES",
    }
    for n, kick in KICKERS.items():
        s = sl[n - 1]
        bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
                                Inches(13.333), Inches(7.5))
        bg.name = "BG"
        bg.shadow.inherit = False
        bg.fill.solid()
        bg.fill.fore_color.rgb = RGBColor.from_string("F7F8F6")
        bg.line.fill.background()
        s.shapes._spTree.remove(bg._element)
        s.shapes._spTree.insert(2, bg._element)
        kk = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.67), Inches(0.50),
                                Inches(8.3), Inches(0.28))
        kk.name = "kicker"
        kk.shadow.inherit = False
        kk.fill.background()
        kk.line.fill.background()
        for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
            setattr(kk.text_frame, m, Inches(0.0))
        kp = kk.text_frame.paragraphs[0]
        kp.alignment = PP_ALIGN.LEFT
        add_run(kp, kick, 11, True, TEAL)
        # card fills + teal labels
        for sh in s.shapes:
            nm = sh.name or ""
            if nm.endswith("-body") and sh.has_text_frame:
                sh.fill.solid()
                sh.fill.fore_color.rgb = RGBColor.from_string("F2F5F6")
                sh.line.fill.background()
                sh.text_frame.margin_left = Inches(0.16)
                sh.text_frame.margin_top = Inches(0.10)
                sh.text_frame.margin_right = Inches(0.14)
            if nm.endswith("-label") and sh.has_text_frame:
                for p in sh.text_frame.paragraphs:
                    for r in p.runs:
                        r.font.bold = True
                        r.font.color.rgb = RGBColor.from_string(TEAL)
        ta = sh_by_name(s, "takeaway")
        if ta is not None:
            acc = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.50),
                                     Inches(Emu(ta.top).inches + 0.06),
                                     Inches(0.055), Inches(0.55))
            acc.name = "takeaway-accent"
            acc.shadow.inherit = False
            acc.fill.solid()
            acc.fill.fore_color.rgb = RGBColor.from_string(TEAL)
            acc.line.fill.background()

    # ---------- H. slide 31 kicker: not a Part ----------
    k31 = sh_by_name(sl[30], "kicker")
    for p in k31.text_frame.paragraphs:
        for r in p.runs:
            if "PART" in r.text:
                r.text = "NAME THE DELIVERABLE"

    # ---------- I. exercise-block color templates + Outlook Copilot strip --
    # Owner: 39-44 and 47-48 share the warm orange exercise template; 45-46
    # get the green template; 49 leaves the live flow.
    def tint(slide, colhex):
        bgx = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
                                     Inches(13.333), Inches(7.5))
        bgx.name = "BG"
        bgx.shadow.inherit = False
        bgx.fill.solid()
        bgx.fill.fore_color.rgb = RGBColor.from_string(colhex)
        bgx.line.fill.background()
        slide.shapes._spTree.remove(bgx._element)
        slide.shapes._spTree.insert(2, bgx._element)

    for n in (39, 40, 41, 42, 43, 44, 47, 48):
        tint(sl[n - 1], "FBF0E2")
    for n in (45, 46):
        tint(sl[n - 1], "E9F3EC")

    # where-to-click strip on 45 (rows compressed to make room)
    s45 = sl[44]
    shrink_rows(s45, 4, y0=2.11, h=0.80, step=0.87)
    strip = s45.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.67), Inches(5.62),
                                 Inches(12.0), Inches(0.62))
    strip.name = "copilot-where"
    strip.shadow.inherit = False
    strip.fill.solid()
    strip.fill.fore_color.rgb = RGBColor.from_string("FFFFFF")
    strip.line.color.rgb = RGBColor.from_string(TEAL)
    strip.line.width = Pt(1.0)
    stf = strip.text_frame
    stf.word_wrap = True
    stf.auto_size = MSO_AUTO_SIZE.NONE
    stf.margin_left = Inches(0.14)
    stf.margin_top = Inches(0.06)
    stf.margin_right = Inches(0.12)
    sp = stf.paragraphs[0]
    sp.alignment = PP_ALIGN.LEFT
    add_run(sp, "WHERE TO CLICK IN OUTLOOK \u2192  ", 10.5, True, TEAL_D)
    add_run(sp, "Open the thread \u2014 the \u201cSummary by Copilot\u201d banner sits at the top "
                "of the reading pane; click Summarize. For drafting, select the Copilot button on the "
                "Home ribbon \u2192 Draft with Copilot. Icon missing? Your account needs a Microsoft 365 "
                "Copilot license \u2014 check with IT.", 10, False, INK)

    # ---------- F. reorder: 20 before 18; 23 after 19; 21+49 -> self-study -
    NEW_ORDER = (list(range(1, 18)) + [20, 18, 19, 23, 22]
                 + list(range(24, 49)) + list(range(50, 114)) + [21, 49])
    assert len(NEW_ORDER) == 113
    sldIdLst = prs.slides._sldIdLst
    ids = sldIdLst.findall(qn("p:sldId"))
    elements = {i + 1: el for i, el in enumerate(ids)}
    for el in ids:
        sldIdLst.remove(el)
    for pnum in NEW_ORDER:
        sldIdLst.append(elements[pnum])

    new_pos = {p: i + 1 for i, p in enumerate(NEW_ORDER)}

    # relocation notes: vehicle slide and research-spreadsheet slide
    for oldpos, quote in ((21, "I don’t think we need slide 21."),
                          (49, "get rid of 49")):
        moved = list(prs.slides)[new_pos[oldpos] - 1]
        ntf = moved.notes_slide.notes_text_frame
        ntf.text = ("RELOCATED to self-study per owner direction (2026-09-18): "
                    "“" + quote + "” Content preserved.\n\n" + ntf.text)

    # page numbers
    for i, slide in enumerate(prs.slides, 1):
        for sh in slide.shapes:
            if sh.name == "page-number" and sh.has_text_frame:
                for p in sh.text_frame.paragraphs:
                    for r in p.runs:
                        if r.text.strip().isdigit():
                            r.text = str(i)

    # remap textual slide references
    ref_pat = re.compile(r"\b(slides?)\s+([0-9]{1,3}(?:\s*[–—-]\s*[0-9]{1,3})?"
                         r"(?:\s*,\s*[0-9]{1,3}(?:\s*[–—-]\s*[0-9]{1,3})?)*)\b",
                         re.IGNORECASE)
    num_pat = re.compile(r"[0-9]{1,3}")

    def remap_numbers(numstr):
        def sub(m):
            n = int(m.group(0))
            return str(new_pos.get(n, n)) if 1 <= n <= 113 else m.group(0)
        return num_pat.sub(sub, numstr)

    changed = []

    def process_tf(tf, where):
        for p in tf.paragraphs:
            for r in p.runs:
                if "v1.10 CONSOLIDATION" in r.text:
                    continue
                if "RELOCATED to self-study per owner direction" in r.text:
                    continue  # quotes the owner verbatim; not a live reference
                if r.text and "slide" in r.text.lower():
                    newt = ref_pat.sub(lambda m: m.group(1) + " " + remap_numbers(m.group(2)), r.text)
                    if newt != r.text:
                        changed.append((where, r.text.strip()[:50], newt.strip()[:50]))
                        r.text = newt

    for i, slide in enumerate(prs.slides, 1):
        for sh in slide.shapes:
            if sh.has_text_frame:
                process_tf(sh.text_frame, f"s{i}:{sh.name}")
        if slide.has_notes_slide:
            process_tf(slide.notes_slide.notes_text_frame, f"s{i}:notes")

    # footers pointing at the relocated vehicle must not call it live
    live_fix = re.compile(r"live slide (\d{1,3})")
    for slide in prs.slides:
        for sh in slide.shapes:
            if sh.name == "detail-link" and sh.has_text_frame:
                for p in sh.text_frame.paragraphs:
                    for r in p.runs:
                        m = live_fix.search(r.text)
                        if m and int(m.group(1)) >= min(new_pos[21], new_pos[49]):
                            r.text = live_fix.sub(r"slide \1 (self-study)", r.text)

    print(f"remapped {len(changed)} references")
    for w, a, b in changed:
        print(f"  {w}: '{a}' -> '{b}'")

    assert len(prs.slides._sldIdLst) == 113
    prs.save(OUT)
    print("saved", OUT)


if __name__ == "__main__":
    main()
