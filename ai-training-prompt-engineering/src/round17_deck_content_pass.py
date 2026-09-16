#!/usr/bin/env python3
# Round 17 content pass over work.pptx (101 slides) -> revised.pptx
import re
from pptx import Presentation
from pptx.dml.color import RGBColor

p = Presentation('work.pptx')
S = p.slides


def shapes_with_text(sl):
    return [sh for sh in sl.shapes if sh.has_text_frame]


def find_shape(sl, startswith=None, contains=None):
    for sh in shapes_with_text(sl):
        t = sh.text_frame.text
        if startswith and t.startswith(startswith):
            return sh
        if contains and contains in t:
            return sh
    return None


def set_shape_text(sh, text):
    """Replace a shape's text, keeping the first run's font for everything."""
    tf = sh.text_frame
    f = None
    for para in tf.paragraphs:
        if para.runs:
            f = para.runs[0].font
            break
    props = None
    if f is not None:
        props = (f.name, f.size, f.bold, f.italic,
                 f.color.rgb if f.color and f.color.type is not None else None)
    tf.text = text
    if props:
        for para in tf.paragraphs:
            for r in para.runs:
                r.font.name = props[0]
                if props[1]: r.font.size = props[1]
                r.font.bold = props[2]
                r.font.italic = props[3]
                if props[4] is not None:
                    r.font.color.rgb = props[4]


def replace_run_text(sl, old, new, required=True):
    for sh in shapes_with_text(sl):
        for para in sh.text_frame.paragraphs:
            for r in para.runs:
                if old in r.text:
                    r.text = r.text.replace(old, new)
                    return True
    if required:
        raise AssertionError(f'run not found: {old!r}')
    return False


def get_notes(sl):
    return sl.notes_slide.notes_text_frame.text


def set_notes(sl, text):
    sl.notes_slide.notes_text_frame.text = text


def notes_replace(sl, old, new, required=True):
    t = get_notes(sl)
    if old not in t:
        if required:
            raise AssertionError(f'notes text not found: {old!r}')
        return
    set_notes(sl, t.replace(old, new))


def rows_of(sl):
    """Return the 4 (label, desc) shape pairs of a donor-layout slide, by x position."""
    labs, descs = [], []
    for sh in shapes_with_text(sl):
        x = sh.left / 914400
        y = sh.top / 914400
        w = sh.width / 914400
        if 0.5 < x < 0.9 and 1.9 < y < 5.6 and 2.5 < w < 3.5:
            labs.append((y, sh))
        if 3.5 < x < 4.3 and 1.9 < y < 5.6:
            descs.append((y, sh))
    labs.sort(); descs.sort()
    return [l[1] for l in labs], [d[1] for d in descs]


def fill_donor(sl, chip, title, rows, band, footer, pageno, notes):
    ch = find_shape(sl, contains=':') if False else None
    for sh in shapes_with_text(sl):
        t = sh.text_frame.text
        if t in ('REFERENCE   SELF-STUDY', 'REFERENCE   0:10', 'REFERENCE  0:10', 'DO   2:00') and sh.top < 914400:
            set_shape_text(sh, chip)
            break
    labs, descs = rows_of(sl)
    assert len(labs) == 4 and len(descs) == 4, (len(labs), len(descs))
    # title = the big shape near top
    tsh = None
    for sh in shapes_with_text(sl):
        if 0.6 < sh.top / 914400 < 1.1 and sh.width / 914400 > 10:
            tsh = sh
    set_shape_text(tsh, title)
    from pptx.util import Pt
    for (lab, desc), (lsh, dsh) in zip(rows, zip(labs, descs)):
        set_shape_text(lsh, lab)
        set_shape_text(dsh, desc)
        for para in dsh.text_frame.paragraphs:
            for r in para.runs:
                r.font.size = Pt(14)
    for sh in shapes_with_text(sl):
        if 6.1 < sh.top / 914400 < 6.6 and sh.width / 914400 > 10:
            set_shape_text(sh, band)
        if 7.0 < sh.top / 914400 < 7.4 and sh.width / 914400 > 5:
            set_shape_text(sh, footer)
        if 7.0 < sh.top / 914400 < 7.4 and sh.width / 914400 < 1.0:
            set_shape_text(sh, pageno)
    set_notes(sl, notes)


REF_NOTES = ("MODE: REFERENCE\n\nTIME: 0:00 (optional self-study; no live allocation)\n\n"
             "PURPOSE: Support independent study with the checked exercise material.\n\nLAND THIS: {land}\n\nSAY:\n- {say}\n\nDO: None.\n\n"
             "BRIDGE: Optional self-study. Return to the related live slide or continue the reference material as needed.\n\nIF LATE: SKIP\n\n{extra}")

# ---------- timing chips + notes TIME lines ----------
TIMING = {2: ('0:45', '0:35'), 7: ('1:25', '1:00'), 9: ('1:00', '0:50'), 10: ('1:00', '0:50'),
          14: ('1:00', '0:50'), 29: ('0:45', '0:30'), 46: ('1:00', '0:45'), 58: ('0:45', '0:40'),
          60: ('0:45', '0:40'), 63: ('0:30', '0:25')}
for n, (old, new) in TIMING.items():
    sl = S[n - 1]
    replace_run_text(sl, f'TEACH   {old}', f'TEACH   {new}')
    notes_replace(sl, f'TIME: {old}', f'TIME: {new}')

# ---------- S34 divider subtitle ----------
replace_run_text(S[33], 'Analysis, dashboards, and communication', 'One supplier case, five artifacts')
notes_replace(S[33], 'LAND THIS: Participants now apply the concepts to work artifacts.',
              'LAND THIS: One case runs through all five artifacts: analysis, dashboard, presentation, email brief, plain-language note.')

# ---------- S35 rework (donor layout in place) ----------
sl = S[34]
old_notes = get_notes(sl)
tail = old_notes[old_notes.find('CONNECTING INSIGHT'):] if 'CONNECTING INSIGHT' in old_notes else ''
fill_donor(
    sl, 'TEACH   1:00', 'One question, one improving prompt',
    [('The question', 'Which supplier has the highest return rate, and what should we investigate next? The same case runs through all five artifacts today.'),
     ('A basic prompt', '“Analyze the supplier data and tell me which supplier is worst.” It runs — but it decides scope, metric, and “worst” for you, silently.'),
     ('Its weaknesses', 'No source scope, no metric definition, no denominator rule, no missing-data rule, no check. Every gap becomes the model’s guess.'),
     ('The improved prompt', 'Names the file and detail rows, defines return rate as totals ÷ totals, keeps defects separate, handles the missing value, demands reconciliation.')],
    'Each added line is a requirement type fixing one named weakness — write the requirement, not the wish.',
    'Detailed explanation: slide 81', '35',
    "MODE: TEACH\n\nTIME: 1:00\n\nPURPOSE: Open the connected case and show incremental prompt improvement.\n\n"
    "LAND THIS: A prompt improves by adding the requirement that fixes a specific observed weakness.\n\nSAY:\n"
    "- Read the basic prompt aloud, then ask what it left the model to decide.\n"
    "- Each improvement line maps to a requirement type from the earlier lesson; the workbook tab 1-Analyze-Data shows the full iteration.\n"
    "- The same cleaned records feed the dashboard, the presentation, and the rest of today’s case.\n\nDO: None.\n\n"
    "BRIDGE: Move to “Exercise: inspect the workbook”.\n\nIF LATE: COMPRESS\n\n" + tail)

# ---------- S36 notes: name the file ----------
notes_replace(S[35], 'Give participants the supplied workbook or demonstrate from the prepared file.',
              'Give participants Course_Workbook.xlsx (Data tab) or demonstrate from the prepared file.')

# ---------- S38 quotations now included ----------
sl = S[37]
replace_run_text(sl, 'Three quotations for the same commercial scope. Source quotations are not included in this package.',
                 'Three fictional quotations for the same commercial scope — the Quote_*.pdf files in your pack.')
replace_run_text(sl, 'Run this optional exercise only after supplying the quotations and a checked answer key.',
                 'Optional self-study: quotation PDFs + workbook tab EX-Quotes are in your pack — normalize before you compare.')
notes_replace(sl, 'The source quote files are not included in the current package; this is an optional future exercise.',
              'The three fictional quotation PDFs and workbook tab EX-Quotes ship in this package; run it as optional self-study.')
notes_replace(sl, 'MATERIALS: The source quotation files are not included in the current package. Keep this as an optional reference exercise until those files are supplied.',
              'MATERIALS: Quote_Alpha_Components.pdf, Quote_Bravo_Plastics.pdf, Quote_Cardinal_Metals.pdf + workbook tab EX-Quotes (all in the pack).')

# ---------- S39 five artifacts ----------
replace_run_text(S[38], 'Spreadsheet, dashboard, presentation, or document: specify the result and its acceptance checks.',
                 'Spreadsheet, dashboard, presentation, email brief, or document: specify the result and its acceptance checks.')

# ---------- S40 dashboard demo connected ----------
sl = S[39]
replace_run_text(sl, 'Create one self-contained HTML (HyperText Markup Language) dashboard from the prepared dataset.',
                 'Open the prepared dashboard — one self-contained HTML (HyperText Markup Language) file built from the SAME cleaned supplier records as the analysis.')
replace_run_text(sl, 'Include a category filter, one chart, a sortable table, and visible metric definitions. Embed the data so the file works offline.',
                 'Filter to Berlin × Bravo Plastics, 2026-03 to 2026-08 — and watch the tiles, chart, and table change together.')
replace_run_text(sl, 'Requirements: behavior + data + usability + delivery. Check one filtered total against the source.',
                 'Check: 8,575 units, 21 returns, 0.245% — matches the workbook; the page footer runs the same self-check.')
old_notes = get_notes(sl)
tail = old_notes[old_notes.find('CONNECTING INSIGHT'):] if 'CONNECTING INSIGHT' in old_notes else ''
set_notes(sl,
    "MODE: DO\n\nTIME: 4:00\n\nPURPOSE: Create observable practice and a result participants can check.\n\n"
    "LAND THIS: You specify a dashboard’s BEHAVIOR in plain language; the page is structure, JavaScript supplies the behavior — no code needed to ask for it.\n\nSAY:\n"
    "- Prepared output: Supplier_Quality_Dashboard.html in the pack — same cleaned records, same definitions as the exercise you just ran.\n"
    "- Name the controls as you use them: month range, supplier/site filters, compare-by, granularity, metric selector, drill-down, sort, Reset — the vocabulary lives in workbook tab 2-Build-Dashboard.\n"
    "- One filter must re-scope EVERY view — tiles, charts, and table always agree; empty results say so; missing is not zero.\n"
    "- Say aloud: it is a data snapshot, not a live reporting system.\n\n"
    "DO: 0:00–0:45 show the build prompt (v1→v3, reference page 98); 0:45–1:30 open the prepared file offline; 1:30–3:00 run the Berlin × Bravo filter and compare 8,575 / 21 / 0.245% with the workbook; 3:00–4:00 one refinement participants name using the control vocabulary.\n\n"
    "BRIDGE: Move to “An email summary has a job to do”.\n\nIF LATE: KEEP\n\n"
    "PROTECTED APPLICATION: Use prepared inputs and fallback outputs. Compress reference material before reducing this activity.\n\n" + tail)

# ---------- S41 notes: thread file ----------
notes_replace(S[40], 'Use the fictional packaging thread included at the end of this deck.',
              'Use the fictional packaging thread at the end of this deck — also supplied as Packaging_Change_Thread.txt for copy-paste.')

# ---------- S42 pointers + workflow ----------
sl = S[41]
replace_run_text(sl, 'Fictional source thread: slides 88–89',
                 'Fictional source thread: slides 88–89 · Packaging_Change_Thread.txt in your pack')
notes_replace(sl, 'Open the included fictional thread in advance or paste it into the approved assistant.',
              'Open Packaging_Change_Thread.txt in advance or paste it into the approved assistant. The full reusable prompt: workbook tab 4-Summarize-Email and reference page 101.')
notes_replace(sl, 'Copilot and Outlook access depends on the participant’s actual setup; the supplied-text exercise works as a fallback.',
              'Verified Sep 2026 (notes/research/r28): Outlook offers “Summary by Copilot” on an open thread with numbered citations; drafts stay drafts. The full experience needs the organization’s Copilot license — the supplied-text exercise is the fallback that always works.')

# ---------- S43 repurposed: presentation self-study demo (donor layout) ----------
fill_donor(
    S[42], 'REFERENCE   0:10', 'Self-study demonstration: present the findings',
    [('What it makes', 'An editable five-slide management deck: question & scope · supplier comparison · the trend · proposed follow-up · limitations & next steps.'),
     ('The prompt’s spine', 'Audience and decision named · one main message per slide · accurate units and period · speaker notes · findings separated from recommendations · nothing invented.'),
     ('The prepared output', 'Supplier_Quality_Mock_Presentation.pptx in your pack — every number traced to the workbook; open it beside the analysis.'),
     ('Check it like an artifact', 'Count slides against the coverage list, reconcile two numbers with the workbook, inspect the exported slides for clipping and readability.')],
    'Full prompt and requirement checklist: workbook tab 3-Present-Findings · reference page 99.',
    'REFERENCE · SELF-STUDY', '43',
    REF_NOTES.format(land='The verified analysis becomes a five-slide management story without inventing results.',
                     say='Orient in one breath: the case continues — same numbers, now aimed at a decision audience. The mock deck is the prepared output; audit it before reusing the prompt.',
                     extra='RELATED: workbook tab 3-Present-Findings; reference page 99; prepared file Supplier_Quality_Mock_Presentation.pptx.'))

# ---------- S44 repurposed: DO documents demonstration ----------
sl = S[43]
# restyle chip + hairline to DO colors taken from slide 36
src = S[35]
chip36 = None; hair36 = None
for sh in src.shapes:
    if sh.has_text_frame and sh.text_frame.text.startswith('DO'):
        chip36 = sh
    if sh.top == 0 and sh.width / 914400 > 13:
        hair36 = sh
chip44 = None; hair44 = None
for sh in sl.shapes:
    if sh.has_text_frame and sh.text_frame.text.startswith('REFERENCE'):
        if sh.top / 914400 < 1:
            chip44 = sh
    if sh.top == 0 and sh.width / 914400 > 13:
        hair44 = sh
do_font_color = None
for para in chip36.text_frame.paragraphs:
    for r in para.runs:
        if r.font.color and r.font.color.type is not None:
            do_font_color = r.font.color.rgb
            break
try:
    from pptx.enum.dml import MSO_FILL
    if hair36.fill.type == MSO_FILL.SOLID:
        hair44.fill.solid(); hair44.fill.fore_color.rgb = hair36.fill.fore_color.rgb
except Exception as e:
    print('hairline restyle skipped:', e)
fill_donor(
    sl, 'DO   2:00', 'Demonstration: explain it clearly',
    [('The task', 'Using the supplied source, explain reorder points and safety stock so a reader at a fifth-grade reading level understands — main idea first, adult tone.'),
     ('The requirements', 'Familiar words · short sentences · one concrete example · terms defined at first use · analogy only if accurate, with its limit stated · conditions preserved.'),
     ('The learning check', 'Three comprehension questions with a short answer key — answerable from the text alone.'),
     ('The fidelity check', 'Compare against the source: any simplification that changes the meaning gets flagged. Readability scores are supporting evidence, not proof.')],
    'Success check: main idea in the first sentence · analogy limit stated · the review caveat survived the simplification.',
    'From Prompts to Agents', '44',
    "MODE: DO\n\nTIME: 2:00\n\nPURPOSE: Create observable practice and a result participants can check.\n\n"
    "LAND THIS: Plain language is a requirements problem: audience, vocabulary, fidelity, and a learning check — not dumbing down.\n\nSAY:\n"
    "- Run the reusable prompt live on the inventory-replenishment source (exercise-data/plain-language/); the sample output is the fallback.\n"
    "- Respectful adult tone — never childish; meaning and caveats survive or the simplification failed.\n"
    "- Self-study variations: the water cycle · how an internet message travels (sources + samples + keys in the pack).\n\n"
    "DO: 0:00–0:30 show the prompt and source; 0:30–1:20 run it or open the sample; 1:20–2:00 check the three success items together.\n\n"
    "BRIDGE: Move to “Part 5: agentic work”.\n\nIF LATE: COMPRESS to showing the sample output and the three checks.\n\n"
    "PROTECTED APPLICATION: Use prepared inputs and fallback outputs.\n\n"
    "MATERIALS: exercise-data/plain-language/README.md (reusable prompt) + three topic files; workbook tab 5-Explain-Clearly.")
if do_font_color is not None:
    for para in chip44.text_frame.paragraphs:
        for r in para.runs:
            r.font.color.rgb = do_font_color

# ---------- S97: relocated old slide 43 ----------
sl = S[96]
for sh in shapes_with_text(sl):
    t = sh.text_frame.text
    if t.startswith('REFERENCE'):
        set_shape_text(sh, 'REFERENCE   SELF-STUDY')
    if t == '43':
        set_shape_text(sh, '97')
    if t.startswith('Your vote decides'):
        set_shape_text(sh, 'Extensions to request after the course — each follows the same source → output → verification pattern as today’s five artifacts.')
set_notes(sl, REF_NOTES.format(land='Future applications follow the same source, output, and verification pattern.',
                               say='This page lists candidate extensions for later sessions; each maps onto the same requirement types taught today.',
                               extra='RELOCATED from the live sequence (old slide 43) when the presentation demonstration took its slot.'))

# ---------- S98-101: new reference pages (donor layout) ----------
fill_donor(
    S[97], 'REFERENCE   SELF-STUDY', 'Full exercise: build the supplier dashboard',
    [('Prompt v1 — the core', 'One self-contained offline HTML file from the cleaned supplier records: summary tiles, one chart, a sortable table — data embedded, definitions and snapshot date visible.'),
     ('Prompt v2 — behavior', 'Add controls by name: month range (inclusive) · Supplier and Site multi-select · compare by supplier or site · monthly/quarterly trend · metric selector · drill-down · sort · Reset.'),
     ('Prompt v3 — the states', 'Active selections visible · one filter rule re-scopes every view · empty results explained · missing ≠ zero · zero denominators show “—”.'),
     ('The checks', 'Berlin × Bravo Plastics, 2026-03..2026-08 → 8,575 units, 21 returns, 0.245%. Rates recomputed from filtered sums; every view must agree.')],
    'Copy-paste prompts: workbook tab 2-Build-Dashboard · prepared output: Supplier_Quality_Dashboard.html.',
    'REFERENCE · SELF-STUDY', '98',
    REF_NOTES.format(land='Interaction behavior is specified in plain language, control by control, with a checkable state rule.',
                     say='The three prompt versions build on each other; the vocabulary table in workbook tab 2-Build-Dashboard names every control with reusable wording.',
                     extra='RELATED: live demonstration slide 40; Supplier_Data_Clean.csv; the dashboard’s footer self-check.'))
fill_donor(
    S[98], 'REFERENCE   SELF-STUDY', 'Full exercise: the five-slide mock presentation',
    [('Coverage', 'Question & scope · supplier comparison · one time or site view · proposed follow-up · limitations and next steps — one main message per slide.'),
     ('Fidelity rules', 'Only verified findings · units and period accurate · uncertainty and missing-data limits preserved · findings separated from recommendations · no invented causes or benefits.'),
     ('Delivery', 'An editable .pptx with brief speaker notes; truthful, labeled charts; every number checked against the analysis; exported slides inspected for clipping and readability.'),
     ('The prepared output', 'Supplier_Quality_Mock_Presentation.pptx — the sample this prompt produced; audit it against this checklist before reusing the prompt.')],
    'Copy-paste prompt: workbook tab 3-Present-Findings · live orientation: slide 43.',
    'REFERENCE · SELF-STUDY', '99',
    REF_NOTES.format(land='A presentation is an artifact with narrative, fidelity, and delivery requirements — not decorated bullet points.',
                     say='The mock deck is deliberately auditable: every number traces to the workbook and the limitations slide names what the data cannot say.',
                     extra='RELATED: slide 43 (live orientation); workbook tab 3-Present-Findings.'))
fill_donor(
    S[99], 'REFERENCE   SELF-STUDY', 'Full exercise: explain a topic clearly',
    [('The prompt’s core', 'Main idea first · familiar words, short sentences, meaningful headings · one concrete example · technical terms defined at first use · clear adult tone.'),
     ('Fidelity', 'Analogies only when accurate, with the limit stated · conditions and uncertainty preserved · no invented facts · meaning-changing simplifications flagged.'),
     ('The learning check', 'Three comprehension questions with a short answer key, answerable from the text alone. Readability scores are supporting evidence, not proof of understanding.'),
     ('Practice topics', 'Inventory replenishment (the live demonstration) · the water cycle · how an internet message travels — sources and sample outputs in exercise-data/plain-language/.')],
    'Copy-paste prompt: workbook tab 5-Explain-Clearly · live demonstration: slide 44.',
    'REFERENCE · SELF-STUDY', '100',
    REF_NOTES.format(land='Accessible language preserves meaning, conditions, and useful detail — fidelity is the hard requirement.',
                     say='Each sample file shows the source, the sample output, and its own fidelity note — the note is part of the deliverable.',
                     extra='RELATED: slide 44 (live demonstration); exercise-data/plain-language/.'))
fill_donor(
    S[100], 'REFERENCE   SELF-STUDY', 'The email-summary prompt, in full',
    [('Scope & brief', 'Review the selected conversation about [topic] using only the messages and attachments you can access. Brief the current situation, then tables of decisions and actions.'),
     ('The tables', 'Decisions: status, conditions, supporting message. Actions: task, explicitly stated owner, due date, status, supporting message. Mark superseded dates as superseded.'),
     ('Honesty rules', 'List unanswered questions, conflicts, missing information, and inaccessible attachments · “Not stated” for gaps · separate source facts from your interpretation.'),
     ('Boundaries', 'End with the next clarification needed. A reply, if requested, is a draft for human review — never sent automatically. Copilot access depends on your license.')],
    'Copy-paste version: workbook tab 4-Summarize-Email · source thread: Packaging_Change_Thread.txt · key: slides 88–89.',
    'REFERENCE · SELF-STUDY', '101',
    REF_NOTES.format(land='The email prompt is a portable specification: scope, extraction fields, evidence, and authority boundaries.',
                     say='Verified Sep 2026 (r28): Outlook’s “Summary by Copilot” covers the native path with numbered citations; the supplied-text version works in any approved assistant.',
                     extra='SOURCES: support.microsoft.com — Summarize an email thread with Copilot in Outlook; Draft an email message with Copilot in Outlook (retrieved 2026-09-16). The full trap answer key: slide 89 + instructor-keys/Packaging_Change_Expected_Brief.md.'))

p.save('revised.pptx')
print('saved revised.pptx')
