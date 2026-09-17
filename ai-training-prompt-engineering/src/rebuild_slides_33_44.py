#!/usr/bin/env python3
"""Iteration-06 deterministic rebuild of slides 33-44 (owner-approved).

Method (per the verifier's constraints):
  - The pristine baseline is extracted from git commit 50c729e (pinned below)
    into build/ and NEVER edited; the rebuild happens on a separate working
    copy and only replaces deliverables/ after validation passes.
  - No slides are inserted, deleted, duplicated, or reordered: the twelve
    existing positions are repurposed in place. presentation.xml is untouched.
  - No XML surgery: shapes are removed and created through the python-pptx
    API only (element detach via the shape's own parent, the library's
    supported idiom; no part rewriting, no relationship editing).
  - No coordinate-inferred roles: every rebuilt slide is cleared completely
    and rebuilt from explicit per-mode templates measured from same-mode
    exemplar slides in the baseline (specs recorded in the commit message
    and notes/design). Nothing is located by approximate position.
  - All paths are repository-relative.

Visual system (measured from baseline exemplars):
  DIVIDER = canonical dark treatment of slides 3/20/45/57 (nav chips, Cambria
  title). TEACH = teal treatment of 22/28/35/39/42. DO = amber treatment of
  36/37/43/56/61/64. A slide's chip, accent, title treatment, and notes MODE
  always agree.
"""
import copy
import os
import subprocess

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.util import Emu, Inches, Pt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
BUILD = os.path.join(HERE, 'build')
BASELINE_SHA = '50c729ebac5a85a772bb0fa4e886ce39bad2cfd0'
DECK_RELPATH = 'deliverables/From_Prompts_to_Agents_Facilitated_60_Minute.pptx'
BASELINE = os.path.join(BUILD, 'baseline_50c729e.pptx')
WORKING = os.path.join(BUILD, 'rebuild_working.pptx')

# ---------------------------------------------------------------------------
# palette + geometry constants (measured; see docstring)
# ---------------------------------------------------------------------------
TEAL = '0E7C7B'          # accent bar / active chip
TEAL_TEXT = '0A6261'     # teal text: chips, titles, labels
TEAL_BAND = 'EAF3F2'     # teach takeaway band fill
INK = '232A31'           # body text
TAKEAWAY = '3D4B50'      # band text
MUTED = '657278'         # footer / page number
AMBER_CHIP = '875012'    # DO chip text (dark amber-brown)
AMBER_BAR = 'C47A1F'     # DO accent bar
AMBER_BAND = 'F7EEDC'    # DO band fill (cream)
DK_BG = '1C272E'         # divider background
DK_BAR = '232A31'        # divider hairline + badge
DK_CHIP_IN = '2A3842'    # inactive nav chip fill
DK_CHIP_LN = '3A4A55'    # inactive nav chip line
DK_KICK = '5FB8B0'       # divider kicker teal
DK_TITLE = 'ECF2F4'      # divider title near-white
DK_MUTED = 'A9BBC4'      # divider description / inactive chip text
DK_PAGENO = 'DCE7E9'


def _rgb(hexstr):
    return RGBColor.from_string(hexstr)


def clear_slide(slide):
    """Remove every shape from the slide via the python-pptx element tree."""
    for shp in list(slide.shapes):
        shp._element.getparent().remove(shp._element)


def set_bg(slide, hexstr):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = _rgb(hexstr)


def _apply_tf(tf, anchor=MSO_ANCHOR.TOP, l=0.1, t=0.05, r=0.1, b=0.05, wrap=True):
    tf.word_wrap = wrap
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.vertical_anchor = anchor
    tf.margin_left = Inches(l)
    tf.margin_right = Inches(r)
    tf.margin_top = Inches(t)
    tf.margin_bottom = Inches(b)


def add_box(slide, name, x, y, w, h, paras, fill=None, line=None, line_w=None,
            anchor=MSO_ANCHOR.TOP, margins=(0.1, 0.05, 0.1, 0.05), wrap=True,
            shape=MSO_SHAPE.RECTANGLE, adj=None):
    """One shape with styled paragraphs.

    paras: list of (text, font_pt, bold, italic, color_hex, align, line_spacing)
           — align/line_spacing optional (None = default left / single).
    """
    sp = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    sp.name = name
    if adj is not None:
        try:
            sp.adjustments[0] = adj
        except (IndexError, ValueError):
            pass
    if fill:
        sp.fill.solid()
        sp.fill.fore_color.rgb = _rgb(fill)
    else:
        sp.fill.background()
    if line:
        sp.line.color.rgb = _rgb(line)
        sp.line.width = Pt(line_w or 0.75)
    else:
        sp.line.fill.background()
    sp.shadow.inherit = False
    tf = sp.text_frame
    _apply_tf(tf, anchor=anchor, l=margins[0], t=margins[1], r=margins[2],
              b=margins[3], wrap=wrap)
    for i, spec in enumerate(paras):
        text, size, bold, italic, color = spec[:5]
        align = spec[5] if len(spec) > 5 else None
        lsp = spec[6] if len(spec) > 6 else None
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align if align is not None else PP_ALIGN.LEFT
        if lsp is not None:
            p.line_spacing = lsp
        run = p.add_run()
        run.text = text
        f = run.font
        f.name = 'Calibri'
        f.size = Pt(size)
        f.bold = bold
        f.italic = italic
        f.color.rgb = _rgb(color)
    return sp


def set_notes(slide, text):
    tf = slide.notes_slide.notes_text_frame
    tf.clear()
    lines = text.strip().split('\n')
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line


# ---------------------------------------------------------------------------
# chrome builders per mode
# ---------------------------------------------------------------------------
NAV_CHIPS = ['1 · PRIMER', '2 · TOOLS', '3 · CRAFT', '4 · APPLICATION',
             '5 · AGENTS', '6 · ASSETS']


def build_divider(slide, pageno, kicker, title, description):
    set_bg(slide, DK_BG)
    add_box(slide, 'FACILITATION_MODE_BAR', 0.0, 0.0, 13.333, 0.042, [], fill=DK_BAR)
    # mode badge — per the verifier: no time chip on this slide, so the badge
    # carries the mode word only (system geometry and styling kept).
    add_box(slide, 'FACILITATION_MODE_LABEL', 10.417, 0.177, 2.552, 0.312,
            [('DIVIDER', 10.5, True, False, 'FFFFFF')], fill=DK_BAR)
    for i, chip in enumerate(NAV_CHIPS):
        active = (i == 3)
        x = 0.55 + i * 1.76
        add_box(slide, f'nav-chip-{i}', x, 0.52, 1.62, 0.36, [],
                fill=(TEAL if active else DK_CHIP_IN),
                line=(None if active else DK_CHIP_LN), line_w=0.75,
                shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.5)
        add_box(slide, f'nav-chip-text-{i}', x, 0.535, 1.62, 0.33,
                [(chip, 8.5, True if active else None,
                  False, 'FFFFFF' if active else DK_MUTED, PP_ALIGN.CENTER)],
                anchor=MSO_ANCHOR.MIDDLE, margins=(0, 0, 0, 0))
    add_box(slide, 'kicker', 0.55, 2.3, 12.0, 0.5,
            [(kicker, 16.0, True, False, DK_KICK)],
            anchor=MSO_ANCHOR.MIDDLE, margins=(0, 0, 0, 0))
    sp = add_box(slide, 'title', 0.55, 2.8, 11.5, 1.9,
                 [(title, 44.0, True, False, DK_TITLE, None, 1.05)],
                 anchor=MSO_ANCHOR.MIDDLE, margins=(0, 0, 0, 0))
    for p in sp.text_frame.paragraphs:
        for r in p.runs:
            r.font.name = 'Cambria'
    add_box(slide, 'description', 0.55, 4.85, 11.0, 0.8,
            [(description, 15.0, None, False, DK_MUTED, None, 1.15)],
            anchor=MSO_ANCHOR.MIDDLE, margins=(0, 0, 0, 0))
    add_box(slide, 'page-number', 12.448, 7.146, 0.521, 0.281,
            [(str(pageno), 10.5, False, False, DK_PAGENO)])


def build_chrome(slide, pageno, mode, time, title, band_text, footer_text,
                 accent, chip_color, band_fill, band_h=0.729, title_size=36.0):
    """Shared chrome for TEACH and DO slides."""
    set_bg(slide, 'FFFFFF')
    add_box(slide, 'FACILITATION_MODE_BAR', 0.0, 0.0, 13.333, 0.062, [], fill=accent)
    add_box(slide, 'mode', 9.167, 0.25, 3.5, 0.365,
            [(f'{mode}   {time}', 13.5, True, False, chip_color)])
    tcolor = TEAL_TEXT if mode.startswith('TEACH') else INK
    tlines = title if isinstance(title, tuple) else (title,)
    add_box(slide, 'title', 0.667, 0.812, 12.0, 1.125,
            [(ln, title_size, True, False, tcolor) for ln in tlines])
    if band_text:
        add_box(slide, 'takeaway', 0.667, 6.302, 12.0, band_h,
                [(band_text, 18.0, True, False, TAKEAWAY)], fill=band_fill)
    add_box(slide, 'footer', 0.667, 7.188, 10.417, 0.26,
            [(footer_text, 10.5, False, False, MUTED)])
    add_box(slide, 'page-number', 12.083, 7.156, 0.583, 0.281,
            [(str(pageno), 12.75, False, False, MUTED)])


def rows_label_body(slide, rows, tops, height, label_size=21.75, body_size=20.0,
                    label_color=TEAL_TEXT):
    for i, ((label, body), top) in enumerate(zip(rows, tops)):
        add_box(slide, f'row-{i}-label', 0.667, top, 3.021, height,
                [(label, label_size, True, False, label_color)])
        add_box(slide, f'row-{i}-body', 3.979, top, 8.688, height,
                [(body, body_size, False, False, INK)])


# (per-slide builders and main flow follow)


# ---------------------------------------------------------------------------
# canonical prompts (single source) for the speaker notes
# ---------------------------------------------------------------------------
def load_prompts():
    import json
    return json.load(open(os.path.join(HERE, 'assets', 'course_prompts.json')))


# ---------------------------------------------------------------------------
# per-slide builders (visible copy per the verifier's iteration-06 spec)
# ---------------------------------------------------------------------------
Q = '“'
QQ = '”'
DOT = ' · '


def para_block(slide, name, x, y, w, h, items, size=22.0, gap=True,
               lead=None, lead_size=22.0):
    """DO-style main content: paragraphs separated by blank paragraphs."""
    paras = []
    if lead:
        paras.append((lead, lead_size, True, False, INK))
        paras.append(('', 11.0, False, False, INK))
    for i, it in enumerate(items):
        paras.append((it, size, False, False, INK))
        if gap and i < len(items) - 1:
            paras.append(('', 11.0, False, False, INK))
    return add_box(slide, name, x, y, w, h, paras)


def s33(slide, notes):
    build_divider(slide, 33, 'PART 4 · APPLICATION', 'Data Analytics Exercise',
                  'Upload one Excel workbook, analyze it, add editable charts, and '
                  'reuse the returned file for a dashboard and presentation.')
    set_notes(slide, notes)


def s34(slide, notes):
    build_chrome(slide, 34, 'DO · ANCHOR', '6:00',
                 'Upload the Workbook and Inspect the Data',
                 'Attempt first — confirm the scope after prompt 1, then analyze.',
                 'From Prompts to Agents',
                 AMBER_BAR, AMBER_CHIP, AMBER_BAND, title_size=33.0)
    add_box(slide, 'lead', 0.667, 2.06, 12.0, 0.45,
            [('Upload Supplier_Data_Exercise.xlsx — attach nothing else.',
              22.0, True, False, INK)])
    rows = [
        (('Prompt 1', 'Inspect'),
         Q + 'Inspect the workbook. List the fields, row count, date range, '
         'suppliers and sites, any total row, and missing values. Then wait for '
         'my scope confirmation.' + QQ),
        (('Prompt 2', 'Analyze'),
         Q + 'Using the confirmed detail rows, compare supplier return rate: total '
         'units returned ÷ total units shipped. Keep defect rate separate. Show '
         'the totals, the missing-data rule, and the reconciliation. Do not infer '
         'causes.' + QQ),
    ]
    for i, ((lab1, lab2), body) in enumerate(rows):
        top = [2.62, 4.38][i]
        add_box(slide, f'row-{i}-label', 0.667, top, 3.021, 1.55,
                [(lab1, 21.75, True, False, AMBER_CHIP),
                 (lab2, 21.75, True, False, AMBER_CHIP)])
        add_box(slide, f'row-{i}-body', 3.979, top, 8.688, 1.55,
                [(body, 20.0, False, False, INK)])
    set_notes(slide, notes)


def s35(slide, notes):
    build_chrome(slide, 35, 'DO', '2:30',
                 ('Follow-Up Analysis:', 'Patterns by Month and Site'),
                 'Findings only — the pattern, its values, and the data you would need next.',
                 'From Prompts to Agents',
                 AMBER_BAR, AMBER_CHIP, AMBER_BAND, title_size=33.0)
    para_block(slide, 'main-prompt', 0.667, 2.135, 12.0, 3.854, [
        Q + 'Using the same data and conversation, compare return rate by month '
        'and site. Identify the clearest increase, decrease, or unusual pattern '
        'and show the supporting values. Describe findings only; do not infer a '
        'cause. List the additional data needed to investigate.' + QQ,
    ], size=24.0, lead='Same chat, same data — one more prompt:', lead_size=22.0)
    set_notes(slide, notes)


def s36(slide, notes):
    build_chrome(slide, 36, 'DO', '4:00',
                 ('Add Editable Excel Charts', 'and Return the File'),
                 'Check: click a chart in the returned workbook — its source range '
                 'must be editable.',
                 'From Prompts to Agents',
                 AMBER_BAR, AMBER_CHIP, AMBER_BAND, title_size=33.0)
    para_block(slide, 'main-prompt', 0.667, 2.135, 12.0, 3.854, [
        'Add a Summary sheet.',
        'Supplier comparison table with an editable native Excel column chart.',
        'Monthly return-rate table with an editable native Excel line chart.',
        'Use formulas, PivotTables, or other traceable Excel logic.',
        'Reconcile the totals and return Supplier_Data_Analyzed.xlsx.',
    ], size=22.0)
    set_notes(slide, notes)


def s37(slide, notes):
    build_chrome(slide, 37, 'TEACH', '1:00', 'Dashboard Requirements',
                 'HyperText Markup Language (HTML) structures the page. JavaScript '
                 'makes the controls work. You only need to describe the behavior.',
                 'From Prompts to Agents',
                 TEAL, TEAL_TEXT, TEAL_BAND)
    vocab = ['Date range', 'Supplier and site filters', 'Grouping', 'Metric selector',
             'Monthly or quarterly trend', 'Drill-down', 'Sort', 'Reset']
    for col in (0, 1):
        paras = []
        for it in vocab[col * 4:(col + 1) * 4]:
            paras.append((it, 24.0, False, False, INK))
            paras.append(('', 12.0, False, False, INK))
        add_box(slide, f'vocab-col-{col}', 0.667 + col * 6.0, 2.25, 5.333, 3.6,
                paras[:-1])
    set_notes(slide, notes)


def s38(slide, notes):
    build_chrome(slide, 38, 'DO', '4:00', 'Build and Test the Dashboard',
                 'Check: verify one filtered result against the workbook before '
                 'trusting any of it.',
                 'From Prompts to Agents',
                 AMBER_BAR, AMBER_CHIP, AMBER_BAND)
    para_block(slide, 'main-prompt', 0.667, 2.135, 12.0, 3.854, [
        'One self-contained HTML file that works offline, detail records kept.',
        'Every control updates the charts, summary values, and table together.',
        'Show the selected period, units, metric definitions, a data-snapshot '
        'label, Reset, and a clear empty-results message.',
    ], size=22.0, lead='Input: Supplier_Data_Analyzed.xlsx — the returned workbook.')
    set_notes(slide, notes)


def s39(slide, notes):
    build_chrome(slide, 39, 'DO', '2:30',
                 ('Create a Five-Slide', 'Management Presentation'),
                 'One message per slide · findings separated from recommendations '
                 '· no invented causes or commitments.',
                 'From Prompts to Agents',
                 AMBER_BAR, AMBER_CHIP, AMBER_BAND, title_size=33.0)
    para_block(slide, 'main-prompt', 0.667, 2.135, 12.0, 3.854, [
        '1  Business question and scope',
        '2  Supplier comparison',
        '3  Important trend',
        '4  Recommended follow-up and supporting evidence',
        '5  Limitations and next steps',
    ], size=22.0, gap=False,
        lead='Audience: Operations leadership' + DOT +
             'Decision: Where should management focus follow-up?')
    # tighten line rhythm for the unnumbered-gap list
    set_notes(slide, notes)


def s40(slide, notes):
    build_chrome(slide, 40, 'TEACH', '1:00', 'Organize an Email Thread in Outlook',
                 'Use only accessible messages and attachments · write '
                 '“Not stated” for missing information · cite the sender and date.',
                 'From Prompts to Agents',
                 TEAL, TEAL_TEXT, TEAL_BAND)
    rows = [
        ('Catch me up', 'Summarize the current situation.'),
        ('What changed', 'List changed dates and decisions.'),
        ('Assign actions', 'Create a task table: owner, due date, status, dependency.'),
        ('Prepare my reply', 'Draft a concise response without inventing commitments.'),
    ]
    rows_label_body(slide, rows, [2.115, 3.062, 4.010, 4.958], 0.885,
                    label_size=20.0, body_size=20.0)
    set_notes(slide, notes)


def s41(slide, notes):
    build_chrome(slide, 41, 'DO', '3:00', 'Email Exercise: Decisions and Actions',
                 'A good result finds the changed deadline, the conditional approval, '
                 'the unresolved question, the missing attachment, and the messages '
                 'needing a reply.',
                 'Fictional source thread: slides 88–89 · '
                 'Packaging_Change_Thread.txt in your pack',
                 AMBER_BAR, AMBER_CHIP, AMBER_BAND)
    add_box(slide, 'main-prompt', 0.667, 2.45, 12.0, 3.54, [
        ('1  Run the built-in Outlook summary —', 24.0, False, False, INK),
        ('     or paste Packaging_Change_Thread.txt.', 24.0, False, False, INK),
        ('', 13.0, False, False, INK),
        ('2  Choose one prompt from the previous slide.', 24.0, False, False, INK),
        ('', 13.0, False, False, INK),
        ('3  Compare the result with the thread.', 24.0, False, False, INK),
    ])
    set_notes(slide, notes)


def s42(slide, notes):
    build_chrome(slide, 42, 'DO', '2:30', 'Extract Supplier Quotes into Excel',
                 'Extraction first — no normalization, ranking, or recommendation yet.',
                 'From Prompts to Agents',
                 AMBER_BAR, AMBER_CHIP, AMBER_BAND)
    para_block(slide, 'main-prompt', 0.667, 2.135, 12.0, 3.854, [
        'Create a Raw Extraction sheet — exact source wording only.',
        'Capture commercial values, timing and terms, and exclusions.',
        'Cite the source file and page; write “Not stated” for missing information.',
    ], size=22.0,
        lead='Attach the three Portable Document Format (PDF) quotations.')
    set_notes(slide, notes)


def s43(slide, notes):
    build_chrome(slide, 43, 'DO', '2:30',
                 'Normalize and Compare the Supplier Quotes',
                 'Do not name a winner while the comparison basis is incomplete.',
                 'From Prompts to Agents',
                 AMBER_BAR, AMBER_CHIP, AMBER_BAND, title_size=33.0)
    para_block(slide, 'main-prompt', 0.667, 2.135, 12.0, 3.854, [
        'Normalize only when the conversion rule or comparison basis is supplied.',
        'Preserve original values; show formulas for comparable totals.',
        'Compare non-price terms as well as price.',
        'List missing information and unresolved scope questions.',
    ], size=22.0)
    set_notes(slide, notes)


def s44(slide, notes):
    build_chrome(slide, 44, 'DO', '3:00',
                 ('Turn Reference Files', 'into a Research Spreadsheet'),
                 'One claim per row · conflicts kept separate · “Not stated” '
                 'for gaps.',
                 'From Prompts to Agents',
                 AMBER_BAR, AMBER_CHIP, AMBER_BAND, title_size=33.0)
    add_box(slide, 'main-prompt', 0.667, 2.135, 12.0, 3.854, [
        ('Question: What should a supplier quality review require, and what '
         'cadence should apply?', 22.0, True, False, INK),
        ('', 12.0, False, False, INK),
        ('Three sheets: Evidence · Synthesis · Sources.', 22.0, False, False, INK),
        ('', 12.0, False, False, INK),
        ('Evidence fields — Claim or instruction · Source · Page or section ·',
         22.0, False, False, INK),
        ('Evidence · Caveat · Relevance · Open question.', 22.0, False, False, INK),
        ('', 12.0, False, False, INK),
        ('Attach the four source documents; exclude the README.', 22.0, False, False, INK),
    ])
    set_notes(slide, notes)


# ---------------------------------------------------------------------------
# speaker notes (full prompts injected from course_prompts.json at run time)
# ---------------------------------------------------------------------------
NOTES = {
 33: """MODE: DIVIDER
TIME: 0:40
PURPOSE: Open the application block and set the single-intake rule.
LAND THIS: One workbook, uploaded once - everything through the management mock-up flows from that single upload.
SAY: From here we stop talking about prompts and start producing artifacts. One fictional supplier workbook goes into the chat once, at the very beginning. We analyze it, get the file back with charts, build a dashboard from the returned file, and end with five slides for management. Then the same discipline runs on an email thread, three quotations, and a research pack.
DO: Speak over the divider; do not read the subtitle verbatim.
BRIDGE: Move to "Upload the Workbook and Inspect the Data".
IF LATE: Cut the preamble to one sentence; the rule is "upload once".""",
 34: """MODE: DO
TIME: 6:00
PURPOSE: The block anchor - inspect before calculating, then a checked comparison.
LAND THIS: Profile first, confirm scope, then analyze - the model must find the total row and the missing value, not stumble over them.
SAY: Upload the workbook and run prompt 1. When the profile comes back, confirm the scope out loud - detail rows only, total row excluded - then run prompt 2.
DO: 1:00 upload + prompt 1; 1:30 confirm the profile together; 2:30 prompt 2; 1:00 debrief the ranking.
FULL PROMPTS (canonical, workbook tab 1-Analyze-Data):
[P1] {P_INSPECT}
[P2] {P_ANALYZE}
EXPECTED RESULT (instructor only): 144 detail rows; one TOTAL row excluded and reconciled against; one blank Inspection_Hours value (2025-12, Austin, Alpha Components) - missing, not zero. Totals 224,902 shipped / 432 returns. Ranking: Bravo Plastics 0.348% (262/75,184) highest, then Cardinal 0.129% (96/74,658), Alpha 0.099% (74/75,060). Defects (2,207) stay separate.
VERIFICATION: The reconciliation matches the TOTAL row exactly; numerator and denominator shown per supplier.
COMMON MISTAKE: Averaging monthly percentages; adding defects to returns; treating the blank as zero; skipping the wait after prompt 1.
EXTENSION: Ask which site drives Bravo's rate - same definitions, one more grouping.
FALLBACK: none needed - the analysis runs in any assistant that reads Excel.
BRIDGE: Move to "Follow-Up Analysis: Patterns by Month and Site".
IF LATE: Confirm the profile quickly and run prompt 2 - this slide is protected.""",
 35: """MODE: DO
TIME: 2:30
PURPOSE: One follow-up in the same chat - the context is already loaded, the scope stays pinned.
LAND THIS: Patterns yes, causes no. A finding names a pattern and shows its values; a cause needs data this file does not contain.
SAY: Same chat - one more prompt. Watch that it reuses the confirmed scope without being told again.
DO: 1:30 run; 1:00 debrief the pattern.
FULL PROMPT (canonical, workbook tab 1-Analyze-Data): {P_FOLLOWUP}
EXPECTED RESULT (instructor only): Bravo's monthly return rate is elevated and volatile, not steadily worsening - peak near 0.737% in 2026-04, quiet months near 0.14% in 2026-06/07, about 0.465% in 2026-08. "Volatile, no steady improvement" passes; any causal claim fails.
VERIFICATION: The values behind the named pattern are shown, month by month.
COMMON MISTAKE: Accepting "the packaging causes returns" - nothing in the file supports a cause.
EXTENSION: Ask for the same view by site only, ranked.
BRIDGE: Move to "Add Editable Excel Charts and Return the File".
IF LATE: Run it without the debrief; the key line is "describe, don't explain".""",
 36: """MODE: DO
TIME: 4:00
PURPOSE: The file contract - the assistant edits the uploaded workbook and returns it.
LAND THIS: Editable-native is the acceptance test. A picture of a chart fails it; a chart whose source range you can edit passes.
SAY: Ask for the file back, by name. When it returns, open it like an auditor: original data untouched, Summary reconciles, charts respond to editing.
DO: 2:00 run; 2:00 open the returned file together and click a chart.
FULL PROMPT (canonical, workbook tab Excel-Charts): {P_EXCEL}
EXPECTED RESULT (instructor only): Data sheet unchanged (blank stays blank); Summary reconciles to 224,902 / 432 with a check cell; native column + line charts.
VERIFICATION: Retitle a chart and recolor a series - both must work; Summary totals match the Data sheet.
COMMON MISTAKE: Accepting an embedded image of a chart; hard-coded chart values instead of ranges.
EXTENSION: Ask for a defect-rate column added to the comparison table, formula visible.
FALLBACK (instructor only): references/exercise-data/Supplier_Data_Analyzed.xlsx - the returned workbook this prompt produced; it feeds the next two steps.
BRIDGE: Move to "Dashboard Requirements".
IF LATE: Show the prepared returned workbook instead of waiting on generation.""",
 37: """MODE: TEACH
TIME: 1:00
PURPOSE: The behavior vocabulary - name the controls and you can ask for them.
LAND THIS: You do not need to write code. You need to describe behavior, control by control, in plain language.
SAY: Each of these eight words is a request you can make verbatim. A dashboard spec is just these names plus your data file.
DO: Point through the eight; do not define each one aloud.
BRIDGE: Move to "Build and Test the Dashboard".
IF LATE: Read only Date range, Filters, Drill-down, Reset.""",
 38: """MODE: DO
TIME: 4:00
PURPOSE: Behavior in plain language becomes a working tool - built on the RETURNED workbook, so definitions carry over.
LAND THIS: One verified filtered result beats admiring the design.
SAY: Feed it the returned workbook and describe the behavior with the vocabulary from the last slide. Then pick one filter and verify the numbers against the workbook.
DO: 2:30 build; 1:30 run the filtered check.
FULL PROMPT (canonical, workbook tab 2-Build-Dashboard): {P_DASHBOARD}
ANSWER KEY (instructor only - NOT on the slide): filter Site = Berlin, Supplier = Bravo Plastics, months 2026-03..2026-08 -> exactly 6 records, 8,575 units shipped, 21 returns, return rate 0.245% - in the tiles, the chart, AND the table. The prepared dashboard's footer runs this same self-check.
VERIFICATION: The filtered totals match an independent filter of the workbook; empty selection shows the empty-results message, not zeros.
COMMON MISTAKE: A dashboard built from a fresh export instead of the returned file - definitions silently drift.
EXTENSION: Ask for one refinement using the vocabulary - a different grouping, metric, or drill-down.
FALLBACK (instructor only): references/exercise-data/Supplier_Quality_Dashboard.html (open offline; footer self-check must say PASSED).
BRIDGE: Move to "Create a Five-Slide Management Presentation".
IF LATE: Open the prepared dashboard and run the check on it instead of building live.""",
 39: """MODE: DO
TIME: 2:30
PURPOSE: The same verified findings become a decision document - the final step of the connected data exercise.
LAND THIS: Findings are what the workbook supports; recommendations are labeled proposals.
SAY: Same chat, same findings. The audience and decision are prefilled - require the five slides and the separation rule.
DO: 1:30 run; 1:00 check one number against the analysis.
FULL PROMPT (canonical, workbook tab 3-Present-Findings): {P_PRESENT}
EXPECTED RESULT (instructor only): five slides mapping to the coverage list; every displayed number traceable to the analysis; limitations named.
VERIFICATION: Count five slides; trace the comparison number; titles alone should tell the story.
COMMON MISTAKE: An invented benefit or cause on slide 4 - the decision audience remembers the made-up number.
EXTENSION: Ask for the deck re-cut for a different audience, same findings.
FALLBACK (instructor only): references/exercise-data/Supplier_Quality_Mock_Presentation.pptx - audit it against the checks before reusing.
BRIDGE: Move to "Organize an Email Thread in Outlook".
IF LATE: Show the prepared mock deck's findings/recommendations split only.""",
 40: """MODE: TEACH
TIME: 1:00
PURPOSE: One thread, four results - choosing the result IS the prompt.
LAND THIS: Pick the outcome first; the prompt is one sentence once you have.
SAY: In Outlook: run the built-in Copilot summary first, then refine in the Copilot chat pane, scoped to the same conversation, with the line that matches what you need. No Copilot license? The pasted-thread path on the next slide always works.
ACCOUNT NOTE (verified Sep 2026, notes/research/r28): the Copilot-in-Outlook experience depends on the organization's license and Outlook version; never practice on real confidential threads.
BRIDGE: Move to "Email Exercise: Decisions and Actions".
IF LATE: Read only "Catch me up" and "Prepare my reply".""",
 41: """MODE: DO
TIME: 3:00
PURPOSE: The structured extraction on a thread with planted traps.
LAND THIS: "Not stated" and a citation per claim - the two habits that survive a real inbox.
SAY: Run it, then we check against the thread itself.
DO: 1:30 run; 1:30 walk the traps.
FULL AUDIT PROMPT (canonical, workbook tab 4-Summarize-Email - run after the built-in summary, in the Copilot chat pane on the same conversation, or on the pasted thread): {P_EMAIL}
ANSWER KEY (instructor only): change date moved Sep 25 -> Oct 2, conditional on quality sign-off; trial date Sep 25 supersedes Sep 18; the 18,000 cap holds and freight is NOT approved; Luis's revised plan due Sep 16; freight responsibility unresolved; the drawing is referenced but not accessible.
VERIFICATION: Each found item cites the sender and date; superseded dates shown as superseded.
COMMON MISTAKE: Reporting "approved" without the condition; inventing an owner or date instead of "Not stated".
EXTENSION: Draft the reply - brackets where the human must decide; nothing sent.
FALLBACK: the pasted-text path IS the fallback; the fictional thread ships in the pack.
BRIDGE: Move to "Extract Supplier Quotes into Excel".
IF LATE: KEEP - this is the email anchor.""",
 42: """MODE: DO
TIME: 2:30
PURPOSE: Documents to spreadsheet, step one - faithful extraction with traceability; judgment comes next.
LAND THIS: Verbatim values, original currencies, "Not stated" for gaps, a citation per value.
SAY: All three quotations cover the same item - EN-450 anodized aluminum enclosure, per drawing rev. D - so every difference you find is real. Extract first; do not let it compare yet.
DO: 1:30 run; 1:00 spot-check two values against the documents.
FULL PROMPT (canonical + extended fields, workbook tab Quote-Extract): {P_QUOTE_EXTRACT}
Also capture: minimum order and warranty (in the full field list for this round; workbook sync pending).
EXPECTED RESULT (instructor only): one row per quotation; original currencies kept (Bravo in EUR); every commercial value traceable to its file and page. Key: instructor-keys/Quote_Comparison_Key.md.
VERIFICATION: Pick any two values and find them verbatim in the cited document.
COMMON MISTAKE: Silent currency conversion; a guessed freight term that looks exactly like a real one.
EXTENSION: Add a "quoted scope differences" column, verbatim only.
FALLBACK (instructor only): references/exercise-data/Quote_Comparison_Workbook.xlsx, sheet "Raw Extraction".
BRIDGE: Move to "Normalize and Compare the Supplier Quotes".
IF LATE: Owner-approved skip - core is the data arc and the email pair.""",
 43: """MODE: DO
TIME: 2:30
PURPOSE: Step two - normalize on a stated basis, compare terms, and stop honestly where the basis ends.
LAND THIS: A defensible "cannot compare yet, here is what is missing" beats a confident wrong winner.
SAY: The arithmetic is easy; the discipline is refusing to invent a basis. Let it flag what blocks the comparison.
DO: 1:30 run; 1:00 debrief the blockers.
FULL PROMPT (canonical, workbook tab Quote-Compare): {P_QUOTE_COMPARE}
ANSWER KEY (instructor only): at 5,000 units with tooling amortized - Alpha USD 15.60/unit (FOB), Bravo EUR 14.70/unit (EXW, no exchange-rate basis supplied), Cardinal USD 16.40 all-in (DDP, tooling waived). Correct outcome: NO best quote - blocking gaps are the EUR conversion basis, freight/duties for Alpha and Bravo, and tax treatment. The key must also flag Bravo's unspecified German Institute for Standardization (DIN) surface requirement and the unresolved drawing-revision / black-anodizing equivalence. Full key: instructor-keys/Quote_Comparison_Key.md.
VERIFICATION: Every derived number is a visible formula; original values remain beside normalized ones.
COMMON MISTAKE: Picking the lowest number; converting EUR at an invented rate.
EXTENSION: Draft the clarification email to the suppliers - one question per gap.
FALLBACK (instructor only): Quote_Comparison_Workbook.xlsx, sheet "Normalized Comparison".
BRIDGE: Move to "Turn Reference Files into a Research Spreadsheet".
IF LATE: Owner-approved skip - core is the data arc and the email pair.""",
 44: """MODE: DO
TIME: 3:00
PURPOSE: Reference files become a traceable research workbook; conflicts stay visible.
LAND THIS: Conflict handling is the skill being tested - agreement is the easy case.
SAY: Four short documents, one question. Watch how it handles the disagreement it is about to find.
DO: 1:30 run; 1:30 walk the Evidence rows and the conflict.
FULL PROMPT (canonical 13-field schema, workbook tab Research - the live slide uses the reduced 7-field version): {P_RESEARCH}
ANSWER KEY (instructor only): two sources disagree on review cadence - the manual excerpt says quarterly, the newsletter says monthly - and the scorecard guideline is undated ("Not stated" in its date column). Both cadence claims must appear as separate rows and the Synthesis must name the conflict. Full key: instructor-keys/Research_Workbook_Key.md.
VERIFICATION: Pick any Evidence row and find its excerpt in the cited file and section.
COMMON MISTAKE: A tidy synthesis that silently picks one cadence; invented citations.
EXTENSION: Add a "what would settle this" column for each open question.
FALLBACK (instructor only): references/exercise-data/Research_Workbook.xlsx (12 traced rows).
BRIDGE: Part 5 - from asking to delegating.
IF LATE: Owner-approved skip - core is the data arc and the email pair.""",
}

# ---------------------------------------------------------------------------
# main flow: pristine baseline -> working copy -> rebuild -> validate -> ship
# ---------------------------------------------------------------------------
BUILDERS = {33: s33, 34: s34, 35: s35, 36: s36, 37: s37, 38: s38,
            39: s39, 40: s40, 41: s41, 42: s42, 43: s43, 44: s44}

# strings that must NOT appear on any participant-visible target slide
FORBIDDEN_VISIBLE = ['0.348', '224,902', '8,575', '21 returns', '0.245',
                     '15.60', '14.70', '16.40', 'Oct 2', 'KEY-', 'instructor',
                     'fallback', 'references/', 'workbook tab', 'five task', '0.737']
CHROME_NAMES = {'FACILITATION_MODE_BAR', 'FACILITATION_MODE_LABEL', 'mode',
                'footer', 'page-number', 'kicker'}


def validate(prs):
    slides = list(prs.slides)
    assert len(slides) == 101, f'slide count {len(slides)} != 101'
    problems = []
    for n in range(33, 45):
        sl = slides[n - 1]
        vis_words = 0
        for sh in sl.shapes:
            if not sh.has_text_frame:
                continue
            for para in sh.text_frame.paragraphs:
                for r in para.runs:
                    if not r.text.strip():
                        continue
                    vis_words += len(r.text.split())
                    sz = r.font.size.pt if r.font.size else None
                    body = (sh.name.startswith(('row-', 'main-prompt', 'vocab-'))
                            or sh.name == 'title')
                    if body and (sz is None or sz < 18.0):
                        problems.append(f'{n}: body run below 18pt in {sh.name}: '
                                        f'{sz} "{r.text[:40]}"')
                    joined = r.text
                    for bad in FORBIDDEN_VISIBLE:
                        if bad in joined and sh.name != 'footer':
                            problems.append(f'{n}: forbidden visible text '
                                            f'"{bad}" in {sh.name}')
        # per-prompt word cap ~120: check the largest single text shape
        for sh in sl.shapes:
            if sh.has_text_frame and sh.name.startswith(('main-prompt', 'row-')):
                words = len(sh.text_frame.text.split())
                if words > 125:
                    problems.append(f'{n}: {sh.name} has {words} words (>125)')
        notes = sl.notes_slide.notes_text_frame.text
        for field in ('MODE:', 'TIME:', 'PURPOSE:', 'LAND THIS:', 'SAY:',
                      'BRIDGE:', 'IF LATE:'):
            if field not in notes:
                problems.append(f'{n}: notes missing {field}')
    return problems


def main():
    os.makedirs(BUILD, exist_ok=True)
    # 1. pristine baseline from the pinned commit (never edited)
    with open(BASELINE, 'wb') as fh:
        subprocess.run(['git', '-C', ROOT, 'show', f'{BASELINE_SHA}:./{DECK_RELPATH}'],
                       stdout=fh, check=True)
    # 2. separate working copy
    with open(BASELINE, 'rb') as src, open(WORKING, 'wb') as dst:
        dst.write(src.read())
    prs = Presentation(WORKING)
    slides = list(prs.slides)
    assert len(slides) == 101, f'baseline has {len(slides)} slides'

    cps = load_prompts()
    subs = {'P_INSPECT': cps['inspect'], 'P_ANALYZE': cps['analyze'],
            'P_FOLLOWUP': cps['followup'], 'P_EXCEL': cps['excel_charts'],
            'P_DASHBOARD': cps['dashboard'], 'P_PRESENT': cps['present'],
            'P_EMAIL': cps['email'], 'P_QUOTE_EXTRACT': cps['quote_extract'],
            'P_QUOTE_COMPARE': cps['quote_compare'], 'P_RESEARCH': cps['research']}

    for n, builder in BUILDERS.items():
        sl = slides[n - 1]
        clear_slide(sl)
        notes = NOTES[n]
        for k, v in subs.items():
            notes = notes.replace('{' + k + '}', v)
        builder(sl, notes)

    problems = validate(prs)
    if problems:
        for p in problems:
            print('FAIL', p)
        raise SystemExit(f'{len(problems)} validation problems - not shipping')
    prs.save(WORKING)
    # re-open and re-validate the saved file
    problems = validate(Presentation(WORKING))
    if problems:
        raise SystemExit('post-save validation failed')
    # 3. ship into deliverables only after validation
    final = os.path.join(ROOT, DECK_RELPATH)
    with open(WORKING, 'rb') as src, open(final, 'wb') as dst:
        dst.write(src.read())
    print(f'rebuilt deck shipped: {final} (101 slides; positions 33-44 rebuilt '
          f'from mode templates; baseline {BASELINE_SHA[:7]} preserved at '
          f'{os.path.relpath(BASELINE, ROOT)})')


if __name__ == '__main__':
    main()
