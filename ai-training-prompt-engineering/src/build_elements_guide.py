#!/usr/bin/env python3
# The Elements of Prompting — multi-page field guide PDF (house style)
import os, json
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, KeepTogether, PageBreak, Image)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FD = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV', FD + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DV-B', FD + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DVSer-B', FD + 'DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Mono', FD + 'DejaVuSansMono.ttf'))
pdfmetrics.registerFont(TTFont('Mono-B', FD + 'DejaVuSansMono-Bold.ttf'))

INK = colors.HexColor('#232A31'); SLATE = colors.HexColor('#46545F'); MUTE = colors.HexColor('#7A8790')
TEAL = colors.HexColor('#0E7C7B'); TEAL_D = colors.HexColor('#0A5B5A'); TEAL_T = colors.HexColor('#E4F0EF')
PANEL = colors.HexColor('#F2F5F6'); LINE = colors.HexColor('#DCE3E6')
AMBER = colors.HexColor('#B96A1B'); AMBER_T = colors.HexColor('#FBF0E0')
RED = colors.HexColor('#AF3230'); RED_T = colors.HexColor('#F9E9E8')
GREEN = colors.HexColor('#3B8560'); GREEN_T = colors.HexColor('#E7F2EC')
DARK = colors.HexColor('#1C272E')

W, H = letter
M = 0.75 * inch
CW = W - 2 * M
out = os.path.join(os.path.dirname(__file__), '..', 'references', 'Elements_of_Prompting_Field_Guide.pdf')

S = {
    'h1': ParagraphStyle('h1', fontName='DVSer-B', fontSize=17, leading=21, textColor=INK, spaceBefore=4, spaceAfter=6),
    'h2': ParagraphStyle('h2', fontName='DVSer-B', fontSize=13, leading=16.5, textColor=TEAL_D, spaceBefore=10, spaceAfter=4),
    'kicker': ParagraphStyle('k', fontName='DV-B', fontSize=8, leading=10, textColor=TEAL, spaceAfter=2),
    'body': ParagraphStyle('b', fontName='DV', fontSize=9.2, leading=13, textColor=SLATE, spaceAfter=5),
    'label': ParagraphStyle('lb', fontName='DV-B', fontSize=9.2, leading=13, textColor=INK, spaceBefore=3, spaceAfter=1),
    'boxbody': ParagraphStyle('bb', fontName='DV', fontSize=8.8, leading=12.2, textColor=SLATE, spaceAfter=2),
    'cell': ParagraphStyle('c', fontName='DV', fontSize=8.4, leading=11.2, textColor=SLATE),
    'cellb': ParagraphStyle('cb', fontName='DV-B', fontSize=8.4, leading=11.2, textColor=INK),
    'cellh': ParagraphStyle('ch', fontName='DV-B', fontSize=8.6, leading=11.5, textColor=TEAL_D),
}


def hf(cv, doc):
    cv.saveState()
    if doc.page == 1:
        cv.setFillColor(DARK)
        cv.rect(0, H - 1.05 * inch, W, 1.05 * inch, stroke=0, fill=1)
        cv.setFillColor(colors.HexColor('#5FB8B0')); cv.setFont('DV-B', 7.5)
        cv.drawString(M, H - 0.38 * inch, 'FROM PROMPTS TO AGENTS  ·  COMPANION TO THE PROMPT LIBRARY  ·  SEPTEMBER 2026')
        cv.setFillColor(colors.white); cv.setFont('DVSer-B', 21)
        cv.drawString(M, H - 0.68 * inch, 'The Elements of Prompting — Field Guide')
        cv.setFillColor(colors.HexColor('#A9BBC4')); cv.setFont('DV', 7.6)  # 7.6pt: 497pt < 504pt available, no clipping
        cv.drawString(M, H - 0.9 * inch, 'Requirement quality · elements as requirement types · menus by artifact · the five exercises, worked · the evidence compendium.')
    else:
        cv.setFillColor(MUTE); cv.setFont('DV', 7)
        cv.drawString(M, H - 0.42 * inch, 'THE ELEMENTS OF PROMPTING · FIELD GUIDE')
    cv.setFillColor(MUTE); cv.setFont('DV', 7)
    cv.drawString(M, 0.32 * inch, 'Templates: prompt-library/ · Deep sources: notes/research/')
    cv.drawRightString(W - M, 0.32 * inch, str(cv.getPageNumber()))
    cv.restoreState()


doc = BaseDocTemplate(out, pagesize=letter, leftMargin=M, rightMargin=M, topMargin=0.6 * inch, bottomMargin=0.55 * inch)
f_first = Frame(M, 0.55 * inch, CW, H - 1.05 * inch - 0.7 * inch, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
f_later = Frame(M, 0.55 * inch, CW, H - 0.55 * inch - 0.62 * inch, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id='first', frames=[f_first], onPage=hf),
                      PageTemplate(id='later', frames=[f_later], onPage=hf)])

E = []
E.append(Paragraph('<font face="DV-B" color="#0A5B5A">Why elements instead of “good prompts”:</font> output quality swings up to 76 accuracy points from formatting alone (Sclar et al., ICLR 2024). You don’t reword your way to a reliable prompt — you find which <b>element</b> failed and fix that one. Learn the elements and you can diagnose any bad output, and build templates of your own instead of collecting other people’s.', S['body']))
E.append(Spacer(1, 4))

# Diagnosis grid
grid = [[Paragraph('The output is…', S['cellh']), Paragraph('The element that failed', S['cellh'])],
        [Paragraph('the wrong altitude, tone, or posture', S['cell']), Paragraph('Role', S['cellb'])],
        [Paragraph('an answer to a different (or vaguer) question', S['cell']), Paragraph('Task', S['cellb'])],
        [Paragraph('generically right, specifically wrong for us', S['cell']), Paragraph('Context', S['cellb'])],
        [Paragraph('right content, unusable shape or length', S['cell']), Paragraph('Format', S['cellb'])],
        [Paragraph('not matching the standard in your head', S['cell']), Paragraph('Examples', S['cellb'])],
        [Paragraph('confidently invented', S['cell']), Paragraph('The Out (missing)', S['cellb'])],
        [Paragraph('sprawling past what you asked', S['cell']), Paragraph('The Stop (missing)', S['cellb'])]]
t = Table(grid, colWidths=[CW * 0.62, CW * 0.38])
t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), TEAL_T),
                       ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
                       ('GRID', (0, 0), (-1, -1), 0.5, LINE),
                       ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                       ('TOPPADDING', (0, 0), (-1, -1), 3.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5)]))
E.append(KeepTogether([Paragraph('THE DIAGNOSIS GRID', S['kicker']), t]))
E.append(Spacer(1, 8))

# ---------------------------------------------------------------------------
# R17 · PART 1 — REQUIREMENT QUALITY (prompts as small work specifications)
# ---------------------------------------------------------------------------
E.append(Paragraph('PART 1 — REQUIREMENT QUALITY', S['kicker']))
E.append(Paragraph('Write requirements, not wishes', S['h1']))
E.append(Paragraph('You already write work specifications: requirements, standard operating procedures, acceptance criteria, test protocols. A prompt is the same craft at small scale — it specifies the content, behavior, and quality of a reply or artifact. Two ideas carry the whole course: <b>requirement type</b> (WHAT must be specified for this artifact — parts 2, 3, and 6) and <b>requirement quality</b> (how well each one is written — this page). The quality bar below applies the writing principles summarized by NASA and INCOSE; it improves clarity and checkability without guaranteeing model compliance.', S['body']))
E.append(Spacer(1, 4))
q_rows = [[Paragraph('Quality', S['cellh']), Paragraph('For a prompt, it means', S['cellh']), Paragraph('The failure it prevents', S['cellh'])],
    [Paragraph('Necessary', S['cellb']), Paragraph('Every line earns its place; a simple task needs only a few requirements.', S['cell']), Paragraph('Rule piles that bury the ones that matter.', S['cell'])],
    [Paragraph('Clear', S['cellb']), Paragraph('One reading; named columns, defined terms, no "etc."', S['cell']), Paragraph('The model resolving ambiguity its own way, silently.', S['cell'])],
    [Paragraph('Complete enough', S['cellb']), Paragraph('The consequential facts and rules are stated — not every fact.', S['cell']), Paragraph('Gaps filled with the most plausible guess.', S['cell'])],
    [Paragraph('Consistent', S['cellb']), Paragraph('No requirement contradicts another; trade-offs made explicit.', S['cell']), Paragraph('The model reconciling you with yourself, its way.', S['cell'])],
    [Paragraph('Feasible', S['cellb']), Paragraph('Possible with the data and tools actually supplied.', S['cell']), Paragraph('Confident output resting on data that cannot support it.', S['cell'])],
    [Paragraph('Singular', S['cellb']), Paragraph('One requirement per line — separable, checkable, revisable.', S['cell']), Paragraph('Half-followed compound instructions nobody can audit.', S['cell'])],
    [Paragraph('Verifiable', S['cellb']), Paragraph('An observable check exists: a number to reconcile, a behavior to exercise, a list to cover.', S['cell']), Paragraph('"Looks done" standing in for done.', S['cell'])]]
tq = Table(q_rows, colWidths=[CW * 0.16, CW * 0.46, CW * 0.38])
tq.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), TEAL_T),
                        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
                        ('GRID', (0, 0), (-1, -1), 0.5, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                        ('TOPPADDING', (0, 0), (-1, -1), 3.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5)]))
E.append(tq)
E.append(Spacer(1, 5))
E.append(Paragraph('<font face="DV-B" color="#232A31">Three boundary rules.</font> A role title is a starting point — observable behavior makes it useful. Context also supplies background facts: turn the consequential ones into explicit instructions when their use matters. And prompt instructions request compliance — actual permissions and configured controls determine which actions a tool can take. <font face="DV-B" color="#0A5B5A">Verification</font> asks whether the output meets the written criteria; <font face="DV-B" color="#0A5B5A">validation</font> asks whether it serves the actual need — check both, every time.', S['body']))
E.append(Spacer(1, 8))


def box(text_pairs, fill):
    rows = [[Paragraph(f'<font face="DV-B" color="#232A31">{k}</font> {v}', S['boxbody'])] for k, v in text_pairs]
    tb = Table(rows, colWidths=[CW - 12])
    tb.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), fill),
                            ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                            ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
    return tb


def element(number, name, tagline, paras, ws=None, mono=False):
    disp = f'&lt;{name}&gt;' if mono else name
    flow = [Paragraph(f'{number} · <font color="#0A5B5A">{disp}</font> — {tagline}', S['h2'])]
    for label, text in paras:
        flow.append(Paragraph(f'<font face="DV-B" color="#232A31">{label}</font> {text}', S['body']))
    if ws:
        flow.append(box(ws, PANEL))
        flow.append(Spacer(1, 3))
    return KeepTogether(flow[:2]), flow[2:]


def emit(number, name, tagline, paras, ws=None, mono=False):
    head, rest = element(number, name, tagline, paras, ws, mono)
    E.append(head)
    E.extend(rest)


E.append(Paragraph('PART 2 — GENERATIVE ELEMENTS: THE SEVEN REQUIREMENT TYPES OF A REPLY', S['kicker']))
E.append(Paragraph('A prompt that writes: five elements, two safety valves', S['h1']))
E.append(Paragraph('A generative prompt commissions <b>one piece of text you will read and act on</b>. Everything you need to control fits in five elements — plus two one-sentence safety valves that shut off the two signature failures.', S['body']))

emit('1', 'ROLE', 'who is answering', [
    ('Definition.', 'The identity, expertise posture, and — critically — the <b>behavioral commitments</b> you assign before the task begins.'),
    ('Mechanism.', 'An LLM completes documents by predicting what plausibly comes next. The role selects <i>which region of everything it has read</i> the completion is drawn from: vocabulary, caution level, what gets foregrounded. “You are a careful analyst” makes analyst-style continuations more probable — it does not add analyst knowledge.'),
    ('Evidence &amp; nuance.', 'Personas do <b>not</b> improve factual accuracy (162-persona study, Zheng et al. 2024) — “you are a genius mathematician” doesn’t fix arithmetic. They <b>do</b> reliably shift tone, framing, and foregrounded knowledge (Salewski et al. 2023). Use Role for <i>how</i> it answers; never as a substitute for checking <i>what</i> it answers. Behaviors beat titles because behaviors are auditable in the output.'),
], ws=[('Weak:', '“You are a senior data scientist.” — a credential; produces nothing checkable.'),
      ('Strong:', '“You are a careful analyst. You compute every number by running code, you state n for every proportion, you never drop data silently, and you say ‘the data can’t answer that’ when it can’t.” — four behaviors, each auditable.'),
      ('Failure it prevents:', 'the generic-assistant voice — mid-distribution, hedge-everything output.')])

emit('2', 'TASK', 'what, for whom, to what end', [
    ('Definition.', 'The single clear ask: a <b>verb + object + audience + success criterion</b>.'),
    ('Mechanism.', 'The most load-bearing words in the prompt — they define the target the completion optimizes toward. Vendors agree to the point of redundancy: Google calls the task “the most important component”; for Microsoft the Goal is the <i>only</i> required part.'),
    ('Nuance.', 'One task per prompt; if several, number them in priority order and add the Stop. A <b>question beats an instruction</b> because it carries its own completion test — either it got answered or it didn’t. Include the audience and the outcome: “the reader should be able to decide X.”'),
], ws=[('Weak:', '“Analyze the returns data.” — a topic. Topics generate exploration.'),
      ('Strong:', '“Answer: what is the return rate by site for Q2 versus the 2.0% target, and which three reason codes drive 80% of returns?” — questions generate answers.'),
      ('Failure it prevents:', 'wandering output — ten observations and no answer.')])

emit('3', 'CONTEXT', 'what the model cannot know', [
    ('Definition.', 'Everything true in <i>your</i> world that isn’t in the training data: raw material, definitions, constraints, history, quirks — and the <b>reasons</b> behind your rules.'),
    ('Mechanism.', 'The model fills every information gap with the most statistically plausible filler. Context replaces plausible-in-general with true-for-you — this is the anti-hallucination element; most “lies” are really unsupplied context.'),
    ('What goes in it.', 'The raw material itself (never assume it knows your documents) · a glossary for terms with local meaning, used exactly · constraints and sensitivities · known quirks <i>each with the rule to apply</i> · and the why behind non-obvious rules — “this will be read aloud, so no ellipses” measurably outperforms “no ellipses”; models generalize from reasons.'),
    ('Discipline.', 'Delimit context from instructions (tags, fences, headers) so material to work on is never confused with orders to follow — also your first defense when the material itself contains instruction-like text.'),
], ws=[('Weak:', '“Use our standard definitions.” — the model’s “standard” is the internet’s average.'),
      ('Strong:', '“Glossary — use exactly: Return rate = returned units ÷ shipped units (shipped_q2.csv). Known quirk: the export has a totals row at the bottom — exclude it and say so.”'),
      ('Failure it prevents:', 'generically-correct, specifically-wrong output — the plausible number with your company’s name on it.')])

emit('4', 'FORMAT', 'the output contract', [
    ('Definition.', 'The required shape of the response: structure, length, tone, medium, what to include and omit.'),
    ('Mechanism.', 'Models imitate structure more readily than they obey descriptions of it — so Format works best stated positively (“respond in flowing prose paragraphs” beats “don’t use markdown”) and best of all demonstrated (see Examples).'),
    ('Nuance.', 'Give a <b>numeric length cap with a priority rule</b> (“≤120 words — cut content before quality”); adjectives like “short” are unenforceable. On genuinely hard reasoning, heavy format constraints can tax accuracy — let it reason free-form first, then format the answer in a second step.'),
], ws=[('Weak:', '“Keep it short and professional.”'),
      ('Strong:', '“Max 120 words. Structure: the ask in sentence one; two supporting facts with numbers; the deadline. Nothing else.”'),
      ('Failure it prevents:', 'the 3×-too-long draft; the buried answer; output you must re-shape by hand.')])

emit('5', 'EXAMPLES', 'show, don’t describe', [
    ('Definition.', '3–5 realistic demonstrations of the task done right, placed in the prompt.'),
    ('Mechanism.', 'In-context learning (Brown et al. 2020 — the discovery that founded prompt engineering): the model infers the pattern from demonstrations without retraining. The strongest steering signal that exists for format, tone, and edge-case handling.'),
    ('Nuance.', 'Diversity is the point: include the awkward case (missing field, borderline grade, angry customer) — the model handles edges exactly as your examples do. Wrap them in tags so they can’t be mistaken for live input. <b>2026:</b> on thinking models, start zero-shot; add examples only when format drifts (few-shot measurably degrades some reasoning models).'),
], ws=[('Weak:', 'three examples that are the same happy case reworded.'),
      ('Strong:', 'one typical case + one edge case + one reject/escalate case — now the model knows the boundaries, not just the center.'),
      ('Failure it prevents:', 'the model guessing your standard from the internet’s average; format drift across runs.')])

valves = [[Paragraph('<font face="DV-B" color="#0A5B5A">THE OUT — permission to not know.</font> “If the document doesn’t say, say so.” Models are trained on benchmarks that reward guessing over abstaining (OpenAI, 2025); the Out re-opens the abstain option and drastically cuts invented answers. Without it you have implicitly ordered the model to always produce something.', S['boxbody'])],
          [Paragraph('<font face="DV-B" color="#0A5B5A">THE STOP — the scope boundary.</font> “Answer these three questions, then stop — do not go exploring.” Converts open-ended capability into bounded work. In agentic prompts it grows up to become gates and autonomy rules.', S['boxbody'])]]
tv = Table(valves, colWidths=[CW - 12])
tv.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), TEAL_T),
                        ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                        ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))
E.append(KeepTogether([Paragraph('THE TWO SAFETY VALVES', S['kicker']), tv]))

# no PageBreak: the safety valves end light — Part 3 pulls up to fill the page
E.append(Paragraph('PART 3 — AGENTIC ELEMENTS: REQUIREMENTS FOR DELEGATED WORK', S['kicker']))
E.append(Paragraph('A prompt that works: the twelve blocks of the mission brief', S['h1']))
E.append(Paragraph('An agentic prompt commissions <b>a job, not a text</b>: the agent plans, acts through tools, checks results, and iterates — mostly while you are not watching. Every generative element still applies. The additional blocks exist for one reason: <b>text that fails costs you a re-prompt; actions that fail change the world</b> — files overwritten, emails sent, wrong numbers published. So the agentic elements govern <i>conduct</i>: where the agent may act, how it must verify itself, when it must stop and ask, and how it proves what it did. (Template A1; worked version A2.)', S['body']))

emit('1', 'role', 'the standing behavioral contract', [
    ('', 'Same element as generative Role, with higher stakes: in chat it shapes one answer you’re about to read; in an agent it biases <b>hundreds of unsupervised decisions</b>. Write it as the behaviors you’d want if you couldn’t check any single step: “never invents numbers, logs every transformation with a row count, prefers reproducible scripts over manual edits.” <font face="DV-B">Prevents:</font> an agent that improvises its professional standards mid-run.'),
], mono=True)
emit('2', 'mission', 'the goal and the definition of done', [
    ('', 'The agentic Task: one goal, the decision it feeds, audience, deadline — plus the line chat never needs: <b>“done looks like: …”.</b> An agent runs a loop; the mission is its exit condition. Vendor grounding: give the agent “a check it can run… without one, ‘looks done’ is the only signal available.” <font face="DV-B">Prevents:</font> the agent deciding for itself what finished means — plausible activity, indefinitely.'),
], mono=True)
emit('3', 'context', 'tribal knowledge, written down', [
    ('', 'Same element as generative Context; the agentic difference is <b>coverage pressure</b> — an agent touches your domain at every step, so every unstated quirk gets stepped on. The glossary becomes a controlled vocabulary (it will otherwise compute three subtly different “yields”); each quirk carries its rule (“Site B records this part under a legacy code — map it to the canonical number”). <font face="DV-B">Prevents:</font> silent invented fixes — the most expensive agent error, because they look like diligence.'),
], mono=True)
emit('4', 'environment', 'the workspace contract', [
    ('', '<b>New in kind.</b> Where the agent may read, where it must write, what tools exist, what is forbidden. Load-bearing distinctions: <b>inputs are read-only</b> · <b>outputs are versioned</b> (never overwrite what a human opened) · <b>scratch is regenerable</b>. Name forbidden actions explicitly (no network calls, no emails, no writes outside the folder). Least privilege as prose — enforce with sandboxing too: the prompt is policy, the sandbox is physics. <font face="DV-B">Prevents:</font> the agent “helpfully” editing your master workbook.'),
], mono=True)
emit('5', 'inputs', 'the source register', [
    ('', '<b>New in kind.</b> One block per source: location, exact format, <b>grain</b> (“one row = one inspected unit” vs “one lot with counts” — the line that determines every denominator downstream), primary key, coverage, owner, <b>trust level</b> (authoritative / derived / manual entry), known issues. Cardinal rule: a fact you can’t establish is written <font face="Mono-B">UNKNOWN</font> and raised as an open item — <b>never guessed</b>. <font face="DV-B">Prevents:</font> the agent inferring your schema — where most wrong numbers are born.'),
], mono=True)
emit('6', 'plan', 'bounded method', [
    ('', 'The steps in order, plus two lists chat prompts don’t carry: <b>methods allowed</b> (boring, reproducible) and <b>methods not allowed without asking</b> (dropping data, causal claims, model fits, new dependencies). Specific enough to prevent improvised rigor, open enough to adapt to what it finds. <font face="DV-B">Prevents:</font> creative methodology at step 14 of 20, discovered only at review.'),
], mono=True)
emit('7', 'checks', 'machine-evaluable verification', [
    ('', '<b>New in kind — the honesty engine of the whole brief.</b> Verification the agent can actually <i>run</i>, split by consequence: <b>HARD</b> checks stop the run (totals reconcile to a trusted number; pass + fail = inspected; no duplicate keys); <b>SOFT</b> checks flag and continue (null spikes, small n, metric moved &gt;X vs last cycle). Two disciplines: write checks as equalities and set-memberships, not aspirations (“check data quality” is not a check); and always include <b>one reconciliation anchor</b> — a number you already trust from outside the run. Without an anchor, every other check can pass on the wrong data. <font face="DV-B">Prevents:</font> plausible-but-wrong deliverables — the agent’s version of hallucination.'),
], mono=True)
emit('8', 'outputs', 'the deliverable contract and audit trail', [
    ('', 'The agentic Format: exact filenames (with date suffixes), exact locations, and the <b>three logs</b> that make a run auditable — CHANGES.md (what changed, when, why) · FINDINGS.md (claims → evidence → confidence) · OPEN_ITEMS.md (assumptions and questions, each with owner and status). A colleague should be able to find, understand, and regenerate everything from the folder alone. <font face="DV-B">Prevents:</font> results you can’t locate and conclusions you can’t trace six weeks later.'),
], mono=True)
emit('9', 'process', 'phases and human gates', [
    ('', '<b>New in kind.</b> The job cut into phases with human checkpoints at the <b>cheap-error points</b>: Gate 1 confirms <i>definitions</i> before any data is touched · Gate 2 reviews <i>reconciliation</i> before analysis builds on the numbers · Gate 3 approves <i>headlines as plain text</i> before anything renders or ships. A definition error caught at Gate 1 costs a sentence; the same error after the deck circulated costs a retraction. <font face="DV-B">Prevents:</font> compounding — hours of competent work on a wrong foundation.'),
], mono=True)
emit('10', 'autonomy rules', 'when to proceed, when to stop (inside <process>)', [
    ('', 'The agentic Stop, matured. Between gates the agent proceeds <b>without asking</b>; it must stop when: a HARD check fails · an input isn’t as described · a definition is ambiguous · an action is hard to reverse (delete, send, publish, overwrite) · a previously published number would change. Both halves matter: without “proceed” you built a slow chatbot; without “stop” you built a liability. General principle: <b>reversible → act; irreversible → ask.</b>'),
])
emit('11', 'rules + quality_bar', 'the invariants, and done-as-a-checklist', [
    ('', '<font face="Mono-B" color="#0A5B5A">&lt;rules&gt;</font> are the non-negotiables kept short and absolute so they survive a long context: never invent or back-fill a number · sources are immutable · every transformation logged with a row count · assumptions stated as assumptions. Rules differ from checks: checks are <i>evaluated</i> at defined points; rules <i>hold everywhere</i>. <font face="DV-B">Prevents:</font> standards drift in hour three.'),
    ('', '<font face="Mono-B" color="#0A5B5A">&lt;quality_bar&gt;</font> is the definition of done made auditable: every placeholder resolved or logged · all HARD checks pass, every SOFT flag noted · every deliverable re-opened and verified · logs written · every presented number traceable to a source cell. Checks verify the <i>work</i> mid-run; the quality bar verifies <i>completeness</i> at the end. <font face="DV-B">Prevents:</font> “done” meaning “I stopped.”'),
])
emit('12', 'reporting', 'the interface back to you', [
    ('', 'The agentic Format for the message, fixed in shape: <b>status</b> (done / stopped at gate n / blocked) · <b>headline answer with the number</b> · deliverable paths · checks summary · open items needing a human · risks. Under 25 lines; <b>evidence, not assertions</b> — the test it ran and what it returned, not “everything went well.” Details live in the files. <font face="DV-B">Prevents:</font> a narrative essay where a status should be.'),
], mono=True)

# no PageBreak: element 12 ends light — Part 4 pulls up to fill the page
E.append(Paragraph('PART 4 — THE MAPPING', S['kicker']))
E.append(Paragraph('The agentic brief is the generative anatomy, grown up to survive autonomy', S['h1']))
mp = [[Paragraph('Generative element', S['cellh']), Paragraph('Agentic descendant(s)', S['cellh']), Paragraph('What was added, and why', S['cellh'])],
      [Paragraph('Role', S['cellb']), Paragraph('&lt;role&gt;', S['cell']), Paragraph('persists across unsupervised decisions → behaviors only', S['cell'])],
      [Paragraph('Task', S['cellb']), Paragraph('&lt;mission&gt;', S['cell']), Paragraph('+ definition of done — the loop needs an exit condition', S['cell'])],
      [Paragraph('Context', S['cellb']), Paragraph('&lt;context&gt; + &lt;inputs&gt;', S['cell']), Paragraph('+ per-source register with grain &amp; trust — agents touch every source repeatedly', S['cell'])],
      [Paragraph('Format', S['cellb']), Paragraph('&lt;outputs&gt; + &lt;reporting&gt;', S['cell']), Paragraph('+ audit logs and a fixed status shape — actions must be traceable', S['cell'])],
      [Paragraph('Examples', S['cellb']), Paragraph('the filled brief (A2)', S['cell']), Paragraph('a worked run is the agentic few-shot', S['cell'])],
      [Paragraph('The Out', S['cellb']), Paragraph('UNKNOWN → open items', S['cell']), Paragraph('not-knowing becomes a logged, owned item', S['cell'])],
      [Paragraph('The Stop', S['cellb']), Paragraph('gates + autonomy rules', S['cell']), Paragraph('scope control becomes checkpointed process', S['cell'])],
      [Paragraph('(none)', S['cellb']), Paragraph('&lt;environment&gt; &lt;plan&gt; &lt;checks&gt; &lt;rules&gt; &lt;quality_bar&gt;', S['cell']), Paragraph('new in kind — conduct, method, verification, invariants, completeness: things text-only prompts never needed', S['cell'])]]
tm = Table(mp, colWidths=[CW * 0.17, CW * 0.31, CW * 0.52])
tm.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), TEAL_T),
                        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
                        ('GRID', (0, 0), (-1, -1), 0.5, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
E.append(tm)

E.append(Spacer(1, 10))
E.append(Paragraph('PART 5 — BUILDING YOUR OWN TEMPLATES', S['kicker']))
E.append(Paragraph('A template is elements + reasons, assembled against failure modes', S['h1']))
steps = [('1.', 'Name the task’s three most expensive failure modes (wrong denominator? invented facts? unusable format? irreversible action?).'),
         ('2.', 'Pick the element that owns each failure — the diagnosis grid on page 1; reversibility → autonomy rules.'),
         ('3.', 'Write those elements strong; keep the rest light. A template where every element is maximal is a template nobody fills in.'),
         ('4.', 'Add one filled example — the gold standard teaches faster than the instructions do.'),
         ('5.', 'Test on 3–5 real cases (one edge case), version it, name an owner, add it to the library.')]
for n, t_ in steps:
    E.append(Paragraph(f'<font face="DV-B" color="#0A5B5A">{n}</font> {t_}', S['body']))

# ---------------------------------------------------------------------------
# R17 · PART 6 — REQUIREMENTS BY ARTIFACT (generated from Requirements_by_Artifact.md)
# ---------------------------------------------------------------------------
def _parse_catalog(md, heading):
    i = md.find('## ' + heading)
    assert i >= 0, heading
    rows_ = []
    for line in md[i:].split('\n')[1:]:
        if line.startswith('## '):
            break
        if line.startswith('|') and not set(line) <= set('|- '):
            cells = [c.strip() for c in line.strip('|').split('|')]
            if len(cells) >= 3 and cells[0] != 'Requirement type':
                rows_.append(cells[:3])
    assert len(rows_) >= 10, heading
    return rows_

_catalog = open(os.path.join(os.path.dirname(__file__), '..', 'Requirements_by_Artifact.md')).read()
_cps = json.load(open(os.path.join(os.path.dirname(__file__), 'assets', 'course_prompts.json')))

E.append(PageBreak())
E.append(Paragraph('PART 6 — REQUIREMENTS BY ARTIFACT', S['kicker']))
E.append(Paragraph('The menu, per artifact: pick what resolves ambiguity', S['h1']))
E.append(Paragraph('The artifact decides which requirement types matter: calculation rules for a spreadsheet, behavior and state for a dashboard, narrative and editability for a presentation, chronology and evidence for an email brief, reading level and fidelity for a document. For each selected type write: <b>requirement → example → acceptance evidence</b>. These menus are maintained in Requirements_by_Artifact.md (the shared catalog behind the Template Creator and the Configurator); this is a teaching taxonomy, not a formal standard.', S['body']))
for _head, _label in [
    ('Spreadsheet analysis: requirements to choose', 'Spreadsheet analysis'),
    ('HTML dashboards: requirements to choose', 'Interactive dashboards'),
    ('Presentations: requirements to choose', 'Presentations'),
    ('Email summaries: requirements to choose', 'Email summaries'),
    ('Plain-language documents: requirements to choose', 'Plain-language documents')]:
    _rows = _parse_catalog(_catalog, _head)
    data_ = [[Paragraph('Requirement type', S['cellh']), Paragraph('Example instruction', S['cellh']), Paragraph('How to check it', S['cellh'])]]
    for r_ in _rows:
        data_.append([Paragraph(r_[0], S['cellb']), Paragraph(r_[1], S['cell']), Paragraph(r_[2], S['cell'])])
    t_ = Table(data_, colWidths=[CW * 0.2, CW * 0.47, CW * 0.33], repeatRows=1)
    t_.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), TEAL_T),
                            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
                            ('GRID', (0, 0), (-1, -1), 0.5, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                            ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                            ('TOPPADDING', (0, 0), (-1, -1), 2.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5)]))
    E.append(KeepTogether([Paragraph(_label.upper(), S['kicker']), Spacer(1, 1)]))
    E.append(t_)
    E.append(Spacer(1, 8))

# ---------------------------------------------------------------------------
# R17 · PART 7 — THE FIVE EXERCISES, WORKED (reusable prompts + their checks)
# ---------------------------------------------------------------------------
S['mono'] = ParagraphStyle('mono', fontName='Mono', fontSize=7.8, leading=10.4, textColor=SLATE)
E.append(Paragraph('PART 7 — THE FIVE EXERCISES, WORKED', S['kicker']))
E.append(Paragraph('The course prompts — copy, adapt, keep the checks', S['h1']))
E.append(Paragraph('One fictional supplier case runs through the first three: analyze → dashboard → presentation, on the same cleaned records and definitions. Full step-by-step versions with iteration commentary: Course_Workbook tabs 1–5. Every prompt below is designed to be copied straight into an assistant.', S['body']))
_ex = [
    ('1 · Analyze spreadsheet data', 'analyze',
     'Check: 144 detail rows · 224,902 shipped · 432 returns · highest return rate Bravo Plastics ≈ 0.348% (262 ÷ 75,184) · reconciles to the TOTAL row · defects (2,207) reported separately.'),
    ('2 · Build an interactive dashboard', 'dashboard',
     'Check: Berlin × Bravo Plastics, 2026-03..2026-08 → 6 records, 8,575 units, 21 returns, 0.245% — identical in tiles, chart, and table. Prepared output: Supplier_Quality_Dashboard.html (footer self-check).'),
    ('3 · Prepare a presentation', 'present',
     'Check: five slides mapped to the coverage list · every number reconciled · findings separated from recommendations · exported slides inspected. Prepared output: Supplier_Quality_Mock_Presentation.pptx.'),
    ('4 · Summarize an email conversation', 'email',
     'Check (the four traps): change date Sep 25 → Oct 2 conditional on sign-off · trial date Sep 25 supersedes Sep 18 · 18,000 cap holds, freight unresolved · drawing referenced but not accessible. Source: Packaging_Change_Thread.txt.'),
    ('5 · Explain a topic clearly', 'explain',
     'Check: main idea first · terms defined at first use · analogy limit stated · conditions preserved against the source · three answerable questions · adult tone. Samples: exercise-data/plain-language/.'),
]
for _name, _pid, _chk in _ex:
    _box = Table([[Paragraph(_cps[_pid].replace('&', '&amp;').replace('<', '&lt;'), S['mono'])]], colWidths=[CW - 12])
    _box.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), PANEL),
                              ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                              ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))
    E.append(KeepTogether([Paragraph(_name, S['h2']), _box, Spacer(1, 2),
                           Paragraph('<font face="DV-B" color="#0A5B5A">Acceptance evidence.</font> ' + _chk, S['boxbody'])]))
    E.append(Spacer(1, 5))
E.append(Spacer(1, 4))

# ---------------------------------------------------------------------------
# PART 5 — THE EVIDENCE COMPENDIUM (v1.1: proven-vs-myth slide + the 2026
# Do/Don't/Expired playbook, merged, with the WHY behind every line; r20 + r25)
# ---------------------------------------------------------------------------
S['ev'] = ParagraphStyle('ev', fontName='DV', fontSize=7.6, leading=10, textColor=MUTE)
S['claim'] = ParagraphStyle('cl', fontName='DV', fontSize=8.6, leading=11.6, textColor=SLATE)


def band(text, color):
    tb = Table([[Paragraph(text, ParagraphStyle('bd', fontName='DV-B', fontSize=9.5, leading=12,
                                                textColor=colors.white))]], colWidths=[CW])
    tb.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), color),
                            ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                            ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
    return tb


def verdict_table(rows):
    data = [[Paragraph(f'<font face="DV-B" color="#232A31">{c}</font><br/>{w}', S['claim']),
             Paragraph(ev, S['ev'])] for c, w, ev in rows]
    t = Table(data, colWidths=[CW * 0.76, CW * 0.24])
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, LINE),
                           ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, PANEL]),
                           ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                           ('TOPPADDING', (0, 0), (-1, -1), 3.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5)]))
    return t


E.append(PageBreak())
E.append(Paragraph('PART 8 — THE EVIDENCE COMPENDIUM', S['kicker']))
E.append(Paragraph('What works, what’s myth, what expired — and why', S['h1']))
E.append(Paragraph('Half the prompting advice in circulation is folklore from 2023. This chapter is the course’s evidence layer in one place — every technique given a verdict, with the <b>why</b> behind it. Three verdicts: <font face="DV-B" color="#3B8560">WORKS</font> (replicated — use it) · <font face="DV-B" color="#AF3230">MYTH</font> (never survived replication, including some standard 2023 advice) · <font face="DV-B" color="#46545F">EXPIRED</font> (was genuinely right, then the product absorbed it). Researched September 2026 — this field moves; the study behind every line is in the PLAYBOOK tab of the Course Workbook and <font face="Mono-B">notes/research/</font>.', S['body']))
E.append(Spacer(1, 4))

E.append(KeepTogether([band('WORKS — replicated, reliably helps today', GREEN), verdict_table([
    ('Be specific: task, constraints, success criteria.',
     'The model optimizes toward the target you state — every unstated need is filled with the most plausible average guess, which matches your intent only ~41% of the time, and vague prompts double the risk of a wrong turn.',
     'Yang 2026 (41.1%)'),
    ('One tested, versioned template — delimiters separating instructions from material.',
     'Models are exquisitely sensitive to wrapper and layout: formatting alone swings accuracy by up to 76 points, the wrapper alone by up to 40%. A tested template removes that lottery and makes runs comparable.',
     'Sclar, ICLR 2024 · He 2024'),
])]))
E.append(verdict_table([
    ('Long inputs: documents at the top, question at the END — bookend both ends when very long.',
     'Attention concentrates at the edges of the context and thins in the middle (“lost in the middle”); the last thing read is the freshest instruction. Placement alone is worth up to ~30% on long documents. (The 2023 recipe — “instructions, ###, then the text” — was written for 4–8K-token windows; as contexts grew to a million tokens the guidance inverted.)',
     'Liu 2023 · Anthropic docs · GPT-4.1 guide 2025'),
    ('Give it an out — in checkable shape — and require citations.',
     'Models are trained on benchmarks that reward a confident guess over “I don’t know,” so inventing is the default way to obey you. The out re-opens honest abstention; the checkable shape (“anything not stated: write UNKNOWN — never estimate; list the gaps”) makes compliance visible in the output.',
     'Omar 2025 (66%→44%) · OpenAI 2025'),
    ('Zero-shot first; add 3–5 targeted, diverse examples only when format or tone matters.',
     'Examples are the strongest format signal there is (in-context learning) — but modern reasoning models degrade under example piles. Demonstrate the standard, edge case included; don’t crowd the reasoning.',
     'OpenAI reasoning practices · Anthropic 2026'),
    ('Concrete numeric budgets for anything measurable — words, bullets, steps, tool calls.',
     'A number is enforceable and self-checkable; an adjective (“short,” “concise”) is a mood the model resolves to the internet’s average. Current models adhere well to concrete length guidance.',
     'GPT-5.1 guide · GPT-5 guide'),
    ('Persona and audience for VOICE and level — never for accuracy.',
     'A role selects which region of everything the model has read the answer draws from — vocabulary, caution, framing. It adds no knowledge: assigned traits are detectable in output up to 80% of the time while accuracy doesn’t move.',
     'PersonaLLM 2024 · Google PTCF'),
    ('Self-check against NAMED criteria, with evaluation blinded from generation.',
     '“Check your work” produces a generic pass. Named criteria give the check something falsifiable to fail, and blinding the checker from the draft’s authorship stops the mirror from grading its own reflection. Fact scores jump 56→71 with planned verification.',
     'CoVe, ACL 2024 · Cheng, Science 2026'),
    ('Ask the AI to improve your prompt (metaprompting).',
     'Prompt wording is a search problem, and models search phrasing-space better than people do — optimizer-written prompts beat human ones, and every major vendor now ships an official prompt improver. Describing what you want and letting the AI draft the prompt is a proven move, not cheating.',
     'OPRO, ICLR 2024 · GEPA 2026 · official vendor tools'),
]))
E.append(Spacer(1, 8))

E.append(KeepTogether([band('MYTH & MISTAKE — never worked, or hurts today', RED), verdict_table([
    ('“Tell it it’s a genius and it gets smarter.”',
     'Personas move style, not competence — knowledge is not gated behind flattery. 162 expert personas tested: zero accuracy gain; dumbed-down personas actively hurt. Standard 2023 advice that never survived replication.',
     'Zheng, EMNLP 2024 · Wharton R4, Dec 2025'),
    ('Tips, threats, “this is important to my career.”',
     'No stable mechanism: effects wash out on average while adding ±35% per-question chaos. The famous “+115%” was the cherry-picked best case — the honest average is ~2.6%, null on modern models. Real stakes stated as factual context (“this goes to a regulator”) are fine: they change the task, not the mood.',
     'Wharton R3 · Salinas 2024 · EmotionPrompt recalc'),
])]))
E.append(verdict_table([
    ('Magic phrases (“take a deep breath”).',
     'Each was one optimizer’s local optimum — for one model, on one benchmark; none replicate across models (“the only trend may be no trend”). The method that found the phrase — automated optimization — is what actually works.',
     'OPRO, ICLR 2024 · IEEE Spectrum, Mar 2024'),
    ('“Longer prompts are better.”',
     'The useful variable is information density, not length. Length without information dilutes attention: reasoning accuracy falls 0.92→0.68 with ~3,000 tokens of padding. Detail helps; filler hurts.',
     'Levy et al., ACL 2024'),
    ('“Are you sure?” as verification.',
     'Pushback is a social signal, not a re-derivation — the model re-reads you, not its work, and folds: answers flip in 58% of cases, 14.7% of them right→wrong. Verification is a named-criteria check or an outside source, never social pressure.',
     'SycEval, AIES 2025 · Huang, ICLR 2024'),
    ('“The AI knows what I mean.”',
     'It fills every unstated requirement with the most statistically plausible filler — right ~41% of the time. Deliberately the same number as WORKS №1: “say what you mean” is the cure for this myth.',
     'Yang 2026'),
    ('Bare “do not hallucinate” commands.',
     'A ban with no honest alternative triggers over-refusal — the model starts refusing facts that ARE in the context (researchers call it the “Safety Tax”). Say what TO do instead: the out, plus required citations.',
     'arXiv:2601.02023, Jan 2026'),
    ('Contradictory instructions.',
     'Reasoning models burn their thinking budget reconciling you with yourself — and settle the conflict silently, their way.',
     'GPT-5 guide 2025'),
    ('Piling micro-rules.',
     'Instruction-following degrades past ~150 simultaneous rules, biased toward the earliest — later rules quietly fall off. Ship the smallest prompt that preserves the contract. (Task detail is information density and helps; rule count is what hurts.)',
     'IFScale · GPT-5.5 guide'),
    ('ALL-CAPS / ALWAYS / NEVER as an emphasis crutch.',
     'Absolutes lock judgment in cases you didn’t foresee — numeric caps constrain quantity, which is different and fine. Reserve absolutes for true invariants.',
     'GPT-5.x guides · Gemini 3 guide'),
    ('Demanding JSON or schemas a human will just read.',
     'Structure serves whoever consumes the output; when that’s a person, the schema buys nothing. When a system consumes it, use structured outputs — and let the model reason first, format second.',
     'OpenAI 2024'),
    ('Concluding “the model can’t do X” from one phrasing.',
     'Formatting alone swings results up to 76 points — one failed phrasing is a data point about the prompt, not the capability ceiling. Rephrase before you conclude.',
     'Sclar, ICLR 2024 · Wharton R1'),
]))
E.append(Spacer(1, 8))

E.append(KeepTogether([band('EXPIRED — was right in 2022–23; do the replacement instead', SLATE), verdict_table([
    ('“Let’s think step by step”  →  pick a reasoning model, set the effort dial.',
     'It was real — it took one math benchmark from 10% to 41% in 2022. Then vendors built the stepping in, and manual chain-of-thought now adds latency and variability on frontier models (it remains legitimate on small local ones). Advice expires when the product absorbs it.',
     'Kojima 2022 · OpenAI guidance · Wharton R2'),
    ('Piles of few-shot examples (10+)  →  zero-shot first, then 3–5 format-definers.',
     'In-context learning founded prompt engineering in 2020; instruction tuning then absorbed the bulk of it, and example piles now actively degrade reasoning models.',
     'Brown 2020 · DeepSeek-R1 paper 2025'),
])]))
E.append(verdict_table([
    ('Hand-run voting and micro-decomposed steps  →  effort settings; chain only for auditable intermediates.',
     'Sampling-and-voting and step-scripting were absorbed into test-time compute, and over-prescribing steps now underperforms outcome-first prompts — give a clear destination, let it choose the path. Chaining stays a feature where regulated work needs auditable intermediates.',
     'Wang, ICLR 2023 · Anthropic 2026 · GPT-5.5 guide'),
    ('Carrying your 2023–24 prompt stack onto each new model  →  re-baseline on every upgrade.',
     'Legacy scaffolds tuned to an old model’s quirks actively degrade newer ones. Strip to the anatomy, re-test your gold cases, re-add only what earns its place — the improvement loop (PDCA), applied to model upgrades.',
     'GPT-5.5 guide, Apr 2026'),
]))
E.append(Spacer(1, 8))

mirror_box = Table([[Paragraph('<font face="DV-B" color="#0A5B5A">THE BIAS UNDER THE MYTHS — THE MIRROR.</font> AI agrees with you about half again as often as a person would (+49%; 11 leading models — Stanford/CMU, <i>Science</i> 2026). Root cause: trained on human preference data, and we prefer agreement. This is why “are you sure?” fails and why revealing your preferred answer poisons a review. <font face="DV-B">Countermeasures, usable today:</font> never reveal your preferred answer when asking for judgment · ask for the case AGAINST (“three weakest points”) · paste your own draft as “a colleague’s” · treat agreement under pushback as noise, not confirmation. <font face="DV-B">See it yourself:</font> rate the same paragraph in two chats — “a colleague wrote this” vs. “I wrote this and I’m proud of it” — and watch the score move.', S['boxbody'])]], colWidths=[CW - 12])
mirror_box.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), TEAL_T),
                                ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                                ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))
E.append(KeepTogether([mirror_box]))
E.append(Spacer(1, 6))

E.append(KeepTogether([box([
    ('WHY THE RULES DON’T CONTRADICT —', 'five seams, resolved:'),
    ('Caps vs. absolutes:', 'numeric caps constrain QUANTITY; ALWAYS/NEVER locks JUDGMENT — reserve absolutes for true invariants.'),
    ('Bookending vs. no-repetition:', 'repeat verbatim at both ends of LONG context, or not at all — paraphrased blanket repetition is the anti-pattern.'),
    ('Task detail vs. rule-piling:', 'detail is information density (helps); piling is rule COUNT (past ~150, quality sags and early rules win).'),
    ('Chain-of-thought’s dual status:', 'expired on frontier reasoning models only — still legitimate on small, local, non-thinking models.'),
    ('The out vs. “don’t hallucinate”:', 'the out IS “don’t hallucinate” said positively — itself a live demo of “say what TO do.”'),
], PANEL)]))
E.append(Spacer(1, 6))
E.append(Paragraph('<font face="DV-B" color="#232A31">Contested — honest edges of the evidence:</font> politeness engineering is inconsistent in both directions (shifts up to ~11% on quality rubrics, direction depends on model and language — be normally civil, don’t engineer tone). “Prompt engineering is dead” is a half-myth: the job title faded, but phrasing still swings results by double digits on frontier models and all three major vendors shipped new prompting guides in 2025–26 — the skill moved into everyone’s job description.', S['body']))

# ---------------------------------------------------------------------------
# PART 6 — THE FAILURE MODES (v1.1: hallucination's four kinds + run-time grid)
# (no PageBreak: Part 5 ends light — Part 6 pulls up to fill the page)
# ---------------------------------------------------------------------------
E.append(Spacer(1, 10))
E.append(Paragraph('PART 9 — TROUBLESHOOTING: THE FAILURE MODES', S['kicker']))
E.append(Paragraph('Hallucination’s four characters — and the run-time grid', S['h1']))
E.append(Paragraph('The mechanism: models are optimized for the most <i>plausible</i> next token, not the most true one — trouble concentrates where training data is thin (rare facts, citations, numbers, names). Benchmarks reward confident guessing over “I don’t know,” so models learn to be good test-takers; the better word is <b>confabulation</b> — gaps filled with plausible material, in-format, so fake citations LOOK like citations. Models trained to say “I don’t know” produce roughly 3× fewer false claims. <font face="DV-B">Fluency is not evidence.</font> And none of the defenses below eliminates hallucination — they convert unverifiable claims into verifiable ones.', S['body']))
E.append(Spacer(1, 4))
hall = [[Paragraph('The character', S['cellh']), Paragraph('What it looks like', S['cellh']), Paragraph('The defense', S['cellh'])],
        [Paragraph('THE CONFIDENT GUESS<br/><font face="DV">invented facts</font>', S['cellb']),
         Paragraph('Free recall where data was thin — a wrong fact, delivered with total certainty.', S['cell']),
         Paragraph('The out, in checkable shape, plus required citations; numbers from code, current facts from search — never free recall.', S['cell'])],
        [Paragraph('THE FAKE RECEIPT<br/><font face="DV">invented sources</font>', S['cellb']),
         Paragraph('Citations, cases, book titles that look perfectly real — and don’t exist.', S['cell']),
         Paragraph('Click through before quoting anywhere formal — a citation is a claim, not proof.', S['cell'])],
        [Paragraph('THE JOKE TAKEN SERIOUSLY<br/><font face="DV">wrong source, confident answer</font>', S['cellb']),
         Paragraph('Fluent, cited — and built on satire, a joke, or the wrong revision.', S['cell']),
         Paragraph('Ask where a claim comes from; ground the answer in documents you supply.', S['cell'])],
        [Paragraph('GARBAGE IN, GOSPEL OUT<br/><font face="DV">runs with your false premise</font>', S['cellb']),
         Paragraph('It assumes your prompt is true: feed it a wrong “fact” and it politely builds on it.', S['cell']),
         Paragraph('State uncertain premises as questions; ask it to check the premise first — premise-checking measurably cuts agreement bias.', S['cell'])]]
th = Table(hall, colWidths=[CW * 0.26, CW * 0.35, CW * 0.39])
th.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), TEAL_T),
                        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
                        ('GRID', (0, 0), (-1, -1), 0.5, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
E.append(th)
E.append(Spacer(1, 10))

E.append(Paragraph('THE RUN-TIME DIAGNOSIS GRID — WHEN THE RUN GOES WRONG', S['kicker']))
E.append(Paragraph('The diagnosis grid on page 1 names the failed <b>element</b> when the answer is wrong. This is its agentic twin: when a long or tool-using <b>run</b> goes wrong, name the context failure — then apply its cure.', S['body']))
run_grid = [[Paragraph('Failure', S['cellh']), Paragraph('The smell', S['cellh']), Paragraph('The cure', S['cellh'])],
            [Paragraph('POISONING', S['cellb']),
             Paragraph('One bad “fact” entered the log early — every later step politely builds on it.', S['cell']),
             Paragraph('Fresh session; re-load only what you trust — the standing brief plus verified files.', S['cell'])],
            [Paragraph('DRIFT', S['cellb']),
             Paragraph('A long run wanders off the goal; the middle of a huge context gets skimmed.', S['cell']),
             Paragraph('Re-inject the mission; compact (the handoff move); stop conditions in the brief.', S['cell'])],
            [Paragraph('CONFUSION', S['cellb']),
             Paragraph('Too many tools on the desk — it picks the wrong one, or dithers between them.', S['cell']),
             Paragraph('Fewer tools per phase; the &lt;plan&gt; names the methods allowed.', S['cell'])],
            [Paragraph('CLASH', S['cellb']),
             Paragraph('Two sources disagree and the run silently picks one of them.', S['cell']),
             Paragraph('One source of truth per fact, named in &lt;inputs&gt;; an explicit override order.', S['cell'])]]
tr = Table(run_grid, colWidths=[CW * 0.16, CW * 0.44, CW * 0.40])
tr.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), TEAL_T),
                        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
                        ('GRID', (0, 0), (-1, -1), 0.5, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
E.append(tr)
E.append(Spacer(1, 4))
E.append(Paragraph('<font face="DV-B" color="#232A31">“Why did it ignore me?”</font> Instructions stack in layers — system prompt · project file (CLAUDE.md / AGENTS.md) · skill · your message — and conflicts resolve by precedence; the layer you typed is the easiest to lose. Find which layer said what before you blame the model, and put one-job rules in a skill, not another standing paragraph. Tool descriptions are prompts too — the agent reads them like a junior reads an API doc.', S['body']))

# ---------------------------------------------------------------------------
# PART 7 — CHOOSING THE ENGINE AND THE VEHICLE (v1.1: two speeds + model
# spectrum, Sep 2026 snapshot; chat / workflow / agent)
# ---------------------------------------------------------------------------
E.append(Spacer(1, 10))
E.append(Paragraph('PART 10 — CHOOSING THE ENGINE AND THE VEHICLE', S['kicker']))
E.append(Paragraph('Fast vs. thinking, the model spectrum, and chat vs. workflow vs. agent', S['h1']))
E.append(Paragraph('Every vendor ships a <b>fast tier</b> — one pass, instant, cheap — and a <b>thinking tier</b> that drafts, checks and revises internally before answering (it isn’t literally “thinking”: it generates intermediate tokens that improve the final answer). The bill: thinking is charged as output tokens, the expensive kind — a hard question can quietly cost 5–20× a simple one, and deep-research modes run order-of-magnitude 100×+. The discipline: pick the smallest mode that can succeed; <b>escalate on failure, not by default</b>.', S['body']))
E.append(KeepTogether([box([
    ('Think ON:', 'multi-step analysis · math · root-cause work · code · tradeoffs across a long document — anywhere being wrong is expensive.'),
    ('Think OFF:', 'lookups · reformatting · summaries · routine drafting — deliberation you don’t need, at 5–20× the price.'),
], TEAL_T)]))
E.append(Spacer(1, 8))

veh = [[Paragraph('CHAT<br/><font face="DV">you are the loop</font>', S['cellb']),
        Paragraph('Exploring, drafting, judging as you go. You read every answer and steer every turn — the generative craft, live.', S['cell'])],
       [Paragraph('WORKFLOW<br/><font face="DV">the loop is frozen</font>', S['cellb']),
        Paragraph('Known path, few tools, same steps every time — script it (n8n, Zapier, Power Automate). Cheaper, predictable, auditable; no judgment needed mid-run. A pipeline can also enforce output schemas at the system level.', S['cell'])],
       [Paragraph('AGENT<br/><font face="DV">the loop runs inside</font>', S['cellb']),
        Paragraph('Unknown path — the next step depends on what it finds. Brief it (Part 3 of this guide), with gates where the judgment stays yours. Your control lives in the brief, not the conversation.', S['cell'])]]
tv2 = Table(veh, colWidths=[CW * 0.2, CW * 0.8])
tv2.setStyle(TableStyle([('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, PANEL]),
                         ('GRID', (0, 0), (-1, -1), 0.5, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                         ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                         ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
E.append(KeepTogether([
    Paragraph('PICK THE VEHICLE — CHAT, WORKFLOW, OR AGENT', S['kicker']),
    tv2,
    Spacer(1, 4),
    Paragraph('<font face="DV-B" color="#0A5B5A">The decision rule:</font> known path + few tools → workflow. Unknown path, real judgment → agent, with gates. Still thinking it through → chat. <font face="DV-B">The wrong vehicle costs:</font> an agent on a known path pays judgment prices for clerk work; a workflow on an unknown path is a script that breaks on the first surprise. And don’t chat with an agent — hand it a work order.', S['body']),
]))


chart_path = os.path.join(os.path.dirname(__file__), 'assets', 'speed_accuracy_chart.png')
E.append(KeepTogether([
    Image(chart_path, width=CW * 0.92, height=CW * 0.92 * 6.4 / 10.4, hAlign='CENTER'),
    Spacer(1, 2),
    Paragraph('<font size="7.6" color="#7A8790">One panel per company; inside each, that company’s current versions. Data: notes/research/r27 — refresh quarterly.</font>', S['ev']),
]))
E.append(Spacer(1, 8))

spec = [[Paragraph('Assistant', S['cellh']), Paragraph('Fast ↔ thinking, in its own names', S['cellh']), Paragraph('Worth knowing', S['cellh'])],
        [Paragraph('ChatGPT<br/><font face="DV">OpenAI</font>', S['cellb']),
         Paragraph('GPT-5.6 family (tiers Sol · Terra · Luna) — one family, speed by setting: the “Think” button (free) or the thinking slider (paid) moves it between speeds; deep research on top.', S['cell']),
         Paragraph('Largest user base; fast model churn and renaming — tier names rotate.', S['cell'])],
        [Paragraph('Claude<br/><font face="DV">Anthropic</font>', S['cellb']),
         Paragraph('A ladder of models: Haiku = the fast tier · Sonnet 5 = the everyday workhorse (1M-token context) · Opus 5 / Fable 5 = the frontier deep end — with “extended thinking” as the toggle on top.', S['cell']),
         Paragraph('Tops coding and real-work evals (SWE-bench, GDPval); 2026 writing evals rank its prose #1.', S['cell'])],
        [Paragraph('Gemini<br/><font face="DV">Google</font>', S['cellb']),
         Paragraph('Gemini 3.6 Flash = the fast line · Gemini 3 / 3.1 Pro = the reasoning line · Deep Think = the separate hard-reasoning mode (Ultra tier).', S['cell']),
         Paragraph('1B+ monthly users; the default AI across Workspace (Gmail, Docs, Meet).', S['cell'])],
        [Paragraph('Copilot<br/><font face="DV">Microsoft</font>', S['cellb']),
         Paragraph('No frontier models of its own — GPT-5.6 plus selectable Claude, inside your tenant. Quick response ↔ Think Deeper; Researcher is its deep-research agent.', S['cell']),
         Paragraph('The governed option — lives inside the M365 compliance boundary IT already audits.', S['cell'])],
        [Paragraph('Perplexity', S['cellb']),
         Paragraph('Routes by question: its own search-tuned stack for fast, cited answers · a “Model Council” of frontier models (GPT + Claude + Gemini) for depth.', S['cell']),
         Paragraph('Research with receipts — inline citations by default; click through before quoting.', S['cell'])],
        [Paragraph('Grok<br/><font face="DV">xAI</font>', S['cellb']),
         Paragraph('Grok 4.6, one family — the modes are the spectrum: Auto · Fast · Expert (reasoning) · Heavy (multi-agent, top tier).', S['cell']),
         Paragraph('Fewer guardrails by design — mind brand-sensitive work.', S['cell'])],
        [Paragraph('DeepSeek', S['cellb']),
         Paragraph('The open-weights house, heir of the famous R1: V4 Pro = the reasoning line · V4.1 Flash = the fast line. MIT-licensed — IT can self-host it.', S['cell']),
         Paragraph('The value leader, ~8 months behind the frontier (NIST CAISI, May 2026); the hosted app stores data in the PRC.', S['cell'])]]
ts = Table(spec, colWidths=[CW * 0.14, CW * 0.55, CW * 0.31], repeatRows=1)
ts.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), TEAL_T),
                        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
                        ('GRID', (0, 0), (-1, -1), 0.5, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
E.append(Paragraph('THE MODEL SPECTRUM — WHO SELLS WHICH SPEED (AS OF SEPTEMBER 2026)', S['kicker']))
E.append(ts)
E.append(Spacer(1, 4))
E.append(Paragraph('The names above are the September 2026 snapshot and <b>will</b> churn — refresh quarterly. The pattern won’t: every vendor sells the same two speeds under different labels. Learn to recognize the tier, not memorize the name.', S['body']))
E.append(Spacer(1, 8))

# ---------------------------------------------------------------------------
# PART 8 — TEN THINGS + GLOSSARY (v1.1: the deck's wrap-up + reference, in print)
# ---------------------------------------------------------------------------
E.append(Spacer(1, 6))
E.append(Paragraph('PART 11 — TEN THINGS WORTH REMEMBERING', S['kicker']))
E.append(Paragraph('The whole course in ten lines', S['h1']))
ten_things = [
    'The prompt is the whole steering wheel — everything the model knows about your task must be in it (or in files it can read).',
    'Anatomy beats inspiration: Role · Task · Context · Format · Examples — plus the Out and the Stop. A prompt is a requirement, new audience.',
    'The context window is a desk, not a filing cabinet: documents at the top, question at the end, fresh chat per topic.',
    'Numbers come from code execution, quotes come from documents, current facts come from search — never from free recall.',
    'Fluency is not evidence. Uncited claims are drafts. Give the model an out and demand citations.',
    'Never reveal your preferred answer when asking for judgment — AI affirms you ~49% more than a human would.',
    'On thinking models: drop the step-by-step scripts, keep the clarity. Contradictions now cost real money.',
    'A generative prompt says what to write; an agentic prompt is a work order: mission, environment, checks, gates, autonomy.',
    'Gates catch errors cheapest: definitions before data, reconciliation before analysis, headlines before rendering.',
    'Prompts that work are assets: name them, version them, store them where the team (and the agent) can find them.',
]
S['ten'] = ParagraphStyle('ten', parent=S['body'], fontSize=9.0, leading=12.2, spaceAfter=2.4)
for i, t_ in enumerate(ten_things, 1):
    E.append(Paragraph(f'<font face="DVSer-B" color="#0E7C7B">{i}</font>&nbsp;&nbsp;{t_}', S['ten']))
E.append(Spacer(1, 4))
E.append(Paragraph('<i>And if you keep only one sentence: a prompt deletes wrong guesses, binds the job, and decides what sits on the desk.</i>', ParagraphStyle('wrap', parent=S['body'], textColor=TEAL_D)))

E.append(Spacer(1, 5))
E.append(Paragraph('APPENDIX — GLOSSARY: TWENTY TERMS THAT MATTER', S['kicker']))
glossary = [
    ('Escalation ladder', 'prompt first, retrieve second, fine-tune last — capability triage'),
    ('Promotion ladder', 'one-off → personal → team → packaged → as-code — where a prompt lives'),
    ('Token', 'the text chunk a model actually reads (~¾ of a word); pricing and limits count these'),
    ('Context window', 'working memory per conversation — everything must fit; cleared when the chat ends'),
    ('Knowledge cutoff', 'where training data stops; anything after needs search or your documents'),
    ('RAG', 'retrieval-augmented generation — fetch relevant passages, answer from them, with citations'),
    ('Embedding', 'a text’s coordinate in meaning-space; powers semantic search and RAG retrieval'),
    ('Hallucination', 'fluent, confident, wrong — plausibility optimized instead of truth'),
    ('Few-shot', 'teaching by 3–5 examples in the prompt'),
    ('Reasoning model', 'drafts and checks internally before answering; slower, costlier, better at hard problems'),
    ('Chain-of-thought', 'prompting visible step-by-step reasoning — now built into thinking models'),
    ('Metaprompting', 'asking the model to critique or rewrite your prompt'),
    ('Sycophancy', 'the trained tendency to agree with you; blind the review to defuse it'),
    ('Agent', 'model + tools + instructions in a loop, acting until done or stopped'),
    ('MCP', 'Model Context Protocol — the open standard for plugging tools into agents'),
    ('Mission brief', 'an agentic prompt: goal, environment, inputs, process, checks, gates, reporting'),
    ('Gate', 'a human checkpoint inside an agent’s process — approve before it proceeds'),
    ('Open weights', 'a downloadable model you can self-host — the data-privacy end of the spectrum'),
    ('Taxonomy', 'the element → attribute → option catalog behind the Template Creator — your parts list'),
    ('Context engineering', 'choosing everything on the desk — prompt, files, history, tool results; parent of agentic prompting'),
]
S['gcell'] = ParagraphStyle('gc', parent=S['cell'], leading=10.6)
gl_cells = [Paragraph(f'<font face="DV-B" color="#0A5B5A">{t_}</font> — {d}', S['gcell']) for t_, d in glossary]
gl_rows = [[gl_cells[i], gl_cells[i + 10]] for i in range(10)]
tg = Table(gl_rows, colWidths=[CW / 2, CW / 2])
tg.setStyle(TableStyle([('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, PANEL]),
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                        ('TOPPADDING', (0, 0), (-1, -1), 1.8), ('BOTTOMPADDING', (0, 0), (-1, -1), 1.8)]))
E.append(tg)

doc.build(E)
print('elements guide written:', out)
