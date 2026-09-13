#!/usr/bin/env python3
# One-page printable cheat sheet — "From Prompts to Agents"
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, FrameBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FD = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV', FD + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DV-B', FD + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DV-I', FD + 'DejaVuSans.ttf'))  # no oblique face installed; reuse regular
pdfmetrics.registerFont(TTFont('DVSer-B', FD + 'DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Mono-B', FD + 'DejaVuSansMono-Bold.ttf'))
pdfmetrics.registerFontFamily('DV', normal='DV', bold='DV-B', italic='DV-I')

INK = colors.HexColor('#232A31'); SLATE = colors.HexColor('#46545F'); MUTE = colors.HexColor('#7A8790')
TEAL = colors.HexColor('#0E7C7B'); TEAL_D = colors.HexColor('#0A5B5A'); TEAL_T = colors.HexColor('#E4F0EF')
PANEL = colors.HexColor('#F2F5F6'); LINE = colors.HexColor('#DCE3E6')
AMBER = colors.HexColor('#B96A1B'); AMBER_T = colors.HexColor('#FBF0E0')
RED = colors.HexColor('#AF3230'); RED_T = colors.HexColor('#F9E9E8')
GREEN = colors.HexColor('#3B8560'); GREEN_T = colors.HexColor('#E7F2EC')
DARK = colors.HexColor('#1C272E')

W, H = letter
M = 0.38 * inch
HEADER_H = 0.62 * inch
FOOTER_H = 0.32 * inch
GUT = 0.22 * inch
colw = (W - 2 * M - GUT) / 2

out = os.path.join(os.path.dirname(__file__), '..', 'deliverables', 'Prompt_Anatomy_Cheat_Sheet.pdf')

S_head = ParagraphStyle('h', fontName='DV-B', fontSize=8.2, leading=10.5, textColor=TEAL_D, spaceAfter=2)
S_body = ParagraphStyle('b', fontName='DV', fontSize=7.0, leading=9.3, textColor=SLATE, spaceAfter=1.5)
S_mode = ParagraphStyle('m', fontName='DV-B', fontSize=10, leading=12, textColor=TEAL_D, spaceAfter=1)
S_modesub = ParagraphStyle('ms', fontName='DV-I', fontSize=6.8, leading=8.5, textColor=MUTE, spaceAfter=4)


def box(title, rows, fill, title_color=TEAL_D, key_mono=False, key_w=None):
    flow = [Paragraph(title, ParagraphStyle('t', parent=S_head, textColor=title_color))]
    for k, v in rows:
        if k:
            kf = 'Mono-B' if key_mono else 'DV-B'
            kc = '#0A5B5A' if key_mono else '#232A31'
            txt = f'<font face="{kf}" color="{kc}">{k}</font> {v}'
        else:
            txt = v
        flow.append(Paragraph(txt, S_body))
    t = Table([[flow]], colWidths=[colw])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), fill),
        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
    ]))
    return t


def header_footer(cv, doc):
    cv.saveState()
    cv.setFillColor(DARK)
    cv.rect(0, H - HEADER_H, W, HEADER_H, stroke=0, fill=1)
    cv.setFillColor(colors.HexColor('#5FB8B0')); cv.setFont('DV-B', 7)
    cv.drawString(M, H - 0.24 * inch, 'FROM PROMPTS TO AGENTS  ·  CHEAT SHEET  ·  SEPTEMBER 2026')
    cv.setFillColor(colors.white); cv.setFont('DVSer-B', 14.5)
    cv.drawString(M, H - 0.48 * inch, 'One skill, two modes: prompts that write — and prompts that work')
    cv.setFillColor(MUTE); cv.setFont('DV', 6.2)
    cv.drawString(M, 0.18 * inch, 'Concepts: tokens = the bricks · context window = the desk · RAG = open-book exam · fluency is not evidence.')
    cv.drawRightString(W - M, 0.18 * inch, 'Templates: prompt-library/ · sources: notes/research/')
    cv.restoreState()


doc = BaseDocTemplate(out, pagesize=letter, leftMargin=M, rightMargin=M,
                      topMargin=HEADER_H + 0.12 * inch, bottomMargin=FOOTER_H)
fh = H - HEADER_H - 0.12 * inch - FOOTER_H
f1 = Frame(M, FOOTER_H, colw, fh, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
f2 = Frame(M + colw + GUT, FOOTER_H, colw, fh, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id='two', frames=[f1, f2], onPage=header_footer)])

E = []
gap = Spacer(1, 6)

# ---------------- LEFT: GENERATIVE ----------------
E.append(Paragraph('GENERATIVE — a prompt that writes', S_mode))
E.append(Paragraph('you ask → it produces text → you read it and act', S_modesub))

E.append(box('THE ANATOMY — SEVEN ELEMENTS (THE DESIGN LAYER)', [
    ('Role', '— behaviours, not titles (“never invent numbers”). Shapes tone and framing, not IQ.'),
    ('Task', '— one clear ask with a verb, the audience, and a success criterion.'),
    ('Context', '— raw material, glossary, constraints; explain WHY a rule exists.'),
    ('Format', '— structure, length cap, tone; say what TO do, not what to avoid.'),
    ('Examples', '— 2–3 realistic samples of “good”, one edge case included.'),
    ('The Out', '— the escape route for missing info: “anything not stated: write UNKNOWN — never estimate; list the gaps.”'),
    ('The Stop', '— where the action ends: “deliver X, then stop — nothing beyond.”'),
], PANEL))
E.append(gap)

E.append(box('THE TOOLKIT IS A LOOP — PLAN · DO · CHECK · ACT', [
    ('PLAN', '— design the ask: the seven elements, filled; be specific and say why; separate your ask from pasted material.'),
    ('DO', '— run it in order: NUMBERED steps; “wait for my OK” where you want control; documents on top, ask at the end.'),
    ('CHECK', '— verify before you trust: name the failed element; self-check against NAMED criteria (never “are you sure?”); blind review; reconcile numbers to a known total.'),
    ('ACT', '— deliver + improve: fix ONE element and rerun; metaprompt; works twice? name it, version it; re-baseline on model upgrades.'),
    ('Layers', '— you WRITE with the anatomy; you IMPROVE with the loop. In agentic work the loop is written INTO the brief — which is why it works best there.'),
], TEAL_T))
E.append(gap)

E.append(box('THE EVIDENCE — WORKS · MYTH · EXPIRED', [
    ('Works:', 'specificity with success criteria · one tested template · docs top, ask at the END · the checkable out + citations · named-criteria self-check · numeric budgets · metaprompting.'),
    ('Myth:', '“genius” personas · tips &amp; threats · magic phrases · length for its own sake · bare “don’t hallucinate” (backfires) · “are you sure?” — it folds, it doesn’t check.'),
    ('Expired:', '“think step by step” · example piles · ### layouts · hand-run voting — the product absorbed them; re-baseline on every model upgrade.'),
    ('Sycophancy:', 'AI affirms you ~49% more than humans would. Never reveal your preferred answer; ask for the case AGAINST; paste your draft as “a colleague’s.”'),
    ('', 'The why behind every line: Field Guide part 5 · sources: PLAYBOOK tab of the Course Workbook.'),
], PANEL))
E.append(gap)

E.append(box('TASK CHEATS — TEMPLATES G1–G8', [
    ('Analysis (G2):', 'exact columns + what one row means; all numbers via code; reconcile to a known total; numbered questions, then stop.'),
    ('Writing (G1):', 'feed raw material; hard word cap; “add no facts”; edit beats draft.'),
    ('Evaluate (G3):', 'anchored rubric; quotes as evidence; “not addressed = 1.”'),
    ('Sheets (G4):', 'name exact columns; README tab; formulas, not pasted values.'),
    ('Decks (G5):', 'titles = findings with numbers; approve text before rendering.'),
    ('HTML (G6):', 'single file, data embedded, works offline; show formulas on screen.'),
    ('Research (G7):', 'a question, not a topic; every bullet gets link + date; demand the gaps section.'),
    ('Documents (G8):', 'summaries serve a decision; verbatim quotes for anything contractual or numeric.'),
], PANEL))

# ---------------- RIGHT: AGENTIC ----------------
E.append(FrameBreak())
E.append(Paragraph('AGENTIC — a prompt that works', S_mode))
E.append(Paragraph('you brief a job → it plans, uses tools, checks itself, reports with evidence', S_modesub))

E.append(box('THE MISSION BRIEF — 12 BLOCKS (TEMPLATE A1)', [
    ('&lt;role&gt;', 'behaviours, not job titles'),
    ('&lt;mission&gt;', 'goal, audience, deadline, “done looks like…”'),
    ('&lt;context&gt;', 'glossary, quirks, targets — the tribal knowledge'),
    ('&lt;environment&gt;', 'read-only inputs / outputs / forbidden actions'),
    ('&lt;inputs&gt;', 'each source: location, format, grain, trust level'),
    ('&lt;plan&gt;', 'steps in order; methods allowed vs ask-first'),
    ('&lt;checks&gt;', 'HARD = stop the run · SOFT = flag and continue'),
    ('&lt;outputs&gt;', 'exact filenames + CHANGES / FINDINGS / OPEN_ITEMS logs'),
    ('&lt;process&gt;', 'phases with human gates'),
    ('&lt;rules&gt;', 'never invent data; version outputs; log assumptions'),
    ('&lt;quality_bar&gt;', 'definition of done as an auditable checklist'),
    ('&lt;reporting&gt;', 'status · headline · evidence · open items, under 25 lines'),
    ('', 'Design thick, ship lean: design against all 12 — SHIP the four-section PLAN·DO·CHECK·ACT brief, one screen long.'),
], TEAL_T, key_mono=True))
E.append(gap)

E.append(box('GATES — CATCH ERRORS AT THE CHEAP END', [
    ('Gate 1:', 'definitions confirmed before any data is touched.'),
    ('Gate 2:', 'numbers reconciled to a total you already trust.'),
    ('Gate 3:', 'headlines approved as plain text before anything renders.'),
    ('Autonomy:', 'between gates, proceed. Stop and ask if: a HARD check fails · an input isn’t as described · a definition is ambiguous · a published number would change.'),
], AMBER_T, AMBER))
E.append(gap)

E.append(box('GUARDRAILS', [
    ('', 'Reversible → proceed. Irreversible (delete / send / publish / overwrite) → ask first.'),
    ('', 'Least privilege: the minimum folders, tools, and accounts for the job.'),
    ('', 'Anything the agent reads can carry hostile instructions (prompt injection). Highest risk when private data + untrusted content + outbound channels combine.'),
    ('', 'Vet third-party skills/plugins like software. Demand evidence of “done,” then spot-check.'),
    ('', 'A gate in the prompt is a suggestion; a gate in the harness is a control — put approvals in tool permissions too.'),
], RED_T, RED))
E.append(gap)

E.append(box('MANAGE PROMPTS LIKE ASSETS', [
    ('Ladder:', 'one-off → personal doc → team library → skills/instructions → repo (as code).'),
    ('Trigger:', 'explained the same task more than once? Package it.'),
    ('Each entry:', 'name · owner · version + change note · model tested · a filled example.'),
    ('Eval lite:', 'three gold cases (typical · edge · should-abstain) + a rubric; a new version must BEAT the current one; re-run on model upgrades.'),
    ('Governance:', 'prompts contain data — classify the library like the documents it quotes; secrets/PII never in a template ({{placeholders}} at run time).'),
], GREEN_T, GREEN))

doc.build(E)
print('cheat sheet written:', out)
