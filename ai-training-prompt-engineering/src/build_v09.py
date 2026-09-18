#!/usr/bin/env python3
"""v09 — exercise-block prompt boxes (owner-directed, in session, 2026-09-18).

Owner: the slide-38 format ("Upload the Data File...") is the model for all
exercises — prompts distinguished in white bordered boxes with a bold header,
uniform font colors. Applied to slides 39-47 (38 already carries it).

All existing wording is preserved verbatim: texts are read out of the current
shapes and re-emitted into the boxed layout. Headers come from the row labels
(uppercased) or are the uniform "THE PROMPT". Colors are uniform: headers
875012, body 232A31, notes 46545F, intro lines bold 232A31 — matching 38.

Input: v08.  Output: From_Prompts_to_Agents_Visual_Pilot_v09.pptx (113).
"""
import os

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE
from pptx.dml.color import RGBColor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "notes", "visual-polish", "pilot", "From_Prompts_to_Agents_Visual_Pilot_v08.pptx")
OUT = os.path.join(ROOT, "notes", "visual-polish", "pilot", "From_Prompts_to_Agents_Visual_Pilot_v09.pptx")

HDR = "875012"
INK = "232A31"
NOTE = "46545F"
BORDER = "A7B0B5"


def sh_by_name(slide, name):
    for sh in slide.shapes:
        if sh.name == name:
            return sh
    return None


def paras_of(sh):
    return [ "".join(r.text for r in p.runs) for p in sh.text_frame.paragraphs
             if "".join(r.text for r in p.runs).strip() ]


def drop(sh):
    sh._element.getparent().remove(sh._element)


def text_shape(slide, name, x, y, w, h, margins=0.0):
    sp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y),
                                Inches(w), Inches(h))
    sp.name = name
    sp.shadow.inherit = False
    sp.fill.background()
    sp.line.fill.background()
    tf = sp.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, Inches(margins))
    return sp


def put(p, text, sz, bold, color):
    p.alignment = PP_ALIGN.LEFT
    r = p.add_run()
    r.text = text
    r.font.size = Pt(sz)
    r.font.bold = bold
    r.font.name = "Calibri"
    r.font.color.rgb = RGBColor.from_string(color)


def box(slide, y, h, header, body_paras, body_sz=14, hdr_sz=15,
        x=0.67, w=12.0):
    panel = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y),
                                   Inches(w), Inches(h))
    panel.name = "ex-box-panel"
    panel.shadow.inherit = False
    panel.fill.solid()
    panel.fill.fore_color.rgb = RGBColor.from_string("FFFFFF")
    panel.line.color.rgb = RGBColor.from_string(BORDER)
    panel.line.width = Pt(1.0)
    tf = panel.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = Inches(0.18)
    tf.margin_right = Inches(0.16)
    tf.margin_top = Inches(0.08)
    tf.margin_bottom = Inches(0.06)
    put(tf.paragraphs[0], header, hdr_sz, True, HDR)
    for t in body_paras:
        put(tf.add_paragraph(), t, body_sz, False, INK)
    return panel


def intro_line(slide, y, text, h=0.44):
    sp = text_shape(slide, "ex-intro", 0.67, y, 12.0, h)
    put(sp.text_frame.paragraphs[0], text, 16, True, INK)
    return sp


def note_line(slide, y, text, h=0.75):
    sp = text_shape(slide, "ex-note", 0.67, y, 12.0, h)
    put(sp.text_frame.paragraphs[0], text, 13, False, NOTE)
    return sp


def convert_rows(slide, n_rows, y0, box_h, step, body_sz=14,
                 header_map=None):
    """Rows -> stacked full-width boxes; header = label text uppercased."""
    rows = []
    for i in range(n_rows):
        lab = sh_by_name(slide, f"row-{i}-label")
        bod = sh_by_name(slide, f"row-{i}-body")
        rows.append((paras_of(lab), paras_of(bod)))
        drop(lab)
        drop(bod)
    for i, (lab, bod) in enumerate(rows):
        header = " · ".join(lab).upper()
        if header_map and i in header_map:
            header = header_map[i]
        box(slide, y0 + i * step, box_h, header, bod, body_sz=body_sz)


def main():
    prs = Presentation(SRC)
    sl = list(prs.slides)
    assert len(sl) == 113

    # s39 — intro + boxed follow-up prompt + note
    s = sl[38]
    mp = sh_by_name(s, "main-prompt")
    p39 = paras_of(mp)
    assert len(p39) == 3, p39
    drop(mp)
    intro_line(s, 2.08, p39[0])
    box(s, 2.66, 1.50, "THE PROMPT", [p39[1]], body_sz=14)
    note_line(s, 4.36, p39[2])

    # s40 — four rows to boxes
    convert_rows(sl[39], 4, y0=2.05, box_h=1.00, step=1.06,
                 header_map={0: "THE PROMPT"})

    # s41 — three rows to boxes
    convert_rows(sl[40], 3, y0=2.05, box_h=1.32, step=1.44,
                 header_map={0: "THE PROMPT"})

    # s42 — intro + test steps box + refinement prompt box
    s = sl[41]
    mp = sh_by_name(s, "main-prompt")
    p42 = paras_of(mp)
    assert len(p42) == 5, p42
    drop(mp)
    intro_line(s, 2.08, p42[0])
    box(s, 2.64, 1.55, "TEST IT", p42[1:4], body_sz=14)
    box(s, 4.33, 1.12, "THE PROMPT", [p42[4]], body_sz=14)

    # s43 — four rows to boxes
    convert_rows(sl[42], 4, y0=2.05, box_h=1.00, step=1.06,
                 header_map={0: "THE PROMPT"})

    # s44 — four rows to compact boxes above the Copilot strip
    convert_rows(sl[43], 4, y0=2.02, box_h=0.80, step=0.88,
                 body_sz=12, header_map=None)

    # s45 — boxed brief prompt + how-to-run note
    s = sl[44]
    mp = sh_by_name(s, "main-prompt")
    p45 = paras_of(mp)
    assert len(p45) == 2, p45
    drop(mp)
    box(s, 2.10, 2.30, "THE PROMPT", [p45[0]], body_sz=14)
    note_line(s, 4.56, p45[1], h=0.9)

    # s46 — one box holding both prompt paragraphs + note
    s = sl[45]
    mp = sh_by_name(s, "main-prompt")
    p46 = paras_of(mp)
    assert len(p46) == 3, p46
    drop(mp)
    box(s, 2.10, 2.85, "THE PROMPT", p46[:2], body_sz=14)
    note_line(s, 5.10, p46[2])

    # s47 — same shape as 46
    s = sl[46]
    mp = sh_by_name(s, "main-prompt")
    p47 = paras_of(mp)
    assert len(p47) == 3, p47
    drop(mp)
    box(s, 2.10, 2.85, "THE PROMPT", p47[:2], body_sz=14)
    note_line(s, 5.10, p47[2])

    prs.save(OUT)
    print("saved", OUT)


if __name__ == "__main__":
    main()
