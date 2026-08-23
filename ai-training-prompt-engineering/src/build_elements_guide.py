#!/usr/bin/env python3
# The Elements of Prompting — multi-page field guide PDF (house style)
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, KeepTogether, PageBreak)
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
out = os.path.join(os.path.dirname(__file__), '..', 'deliverables', 'Elements_of_Prompting_Field_Guide.pdf')

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
        cv.drawString(M, H - 0.38 * inch, 'FROM PROMPTS TO AGENTS  ·  COMPANION TO THE PROMPT LIBRARY  ·  V1.0 AUGUST 2026')
        cv.setFillColor(colors.white); cv.setFont('DVSer-B', 21)
        cv.drawString(M, H - 0.68 * inch, 'The Elements of Prompting — Field Guide')
        cv.setFillColor(colors.HexColor('#A9BBC4')); cv.setFont('DV', 8.5)
        cv.drawString(M, H - 0.9 * inch, 'What every template is made of: each element defined — mechanism, strong vs. weak fills, and the failure it prevents.')
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


E.append(Paragraph('PART 1 — GENERATIVE ELEMENTS', S['kicker']))
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

E.append(PageBreak())
E.append(Paragraph('PART 2 — AGENTIC ELEMENTS', S['kicker']))
E.append(Paragraph('A prompt that works: the twelve blocks of the mission brief', S['h1']))
E.append(Paragraph('An agentic prompt commissions <b>a job, not a text</b>: the agent plans, acts through tools, checks results, and iterates — mostly while you are not watching. Every generative element still applies. The additional blocks exist for one reason: <b>text that fails costs you a re-prompt; actions that fail change the world</b> — files overwritten, emails sent, wrong numbers published. So the agentic elements govern <i>conduct</i>: where the agent may act, how it must verify itself, when it must stop and ask, and how it proves what it did. (Template A1; worked version A2.)', S['body']))

emit('1', 'role', 'the standing behavioral contract', [
    ('', 'Same element as generative Role, with higher stakes: in chat it shapes one answer you’re about to read; in an agent it biases <b>hundreds of unsupervised decisions</b>. Write it as the behaviors you’d want if you couldn’t check any single step: “never invents numbers, logs every transformation with a row count, prefers reproducible scripts over manual edits.” <font face="DV-B">Prevents:</font> an agent that improvises its professional standards mid-run.'),
], mono=True)
emit('2', 'mission', 'the goal and the definition of done', [
    ('', 'The agentic Task: one goal, the decision it feeds, audience, deadline — plus the line chat never needs: <b>“done looks like: …”.</b> An agent runs a loop; the mission is its exit condition. Vendor grounding: give the agent “a check it can run… without one, ‘looks done’ is the only signal available.” <font face="DV-B">Prevents:</font> the agent deciding for itself what finished means — plausible activity, indefinitely.'),
], mono=True)
emit('3', 'context', 'tribal knowledge, written down', [
    ('', 'Same element as generative Context; the agentic difference is <b>coverage pressure</b> — an agent touches your domain at every step, so every unstated quirk gets stepped on. The glossary becomes a controlled vocabulary (it will otherwise compute three subtly different “yields”); each quirk carries its rule (“Parks records PN 668518; it means 666518 — map it”). <font face="DV-B">Prevents:</font> silent invented fixes — the most expensive agent error, because they look like diligence.'),
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

E.append(PageBreak())
E.append(Paragraph('PART 3 — THE MAPPING', S['kicker']))
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
E.append(Spacer(1, 6))
E.append(Paragraph('<font face="DV-B" color="#232A31">When to switch modes:</font> if the work involves files, tools, multiple steps, or a deliverable produced while you’re not watching — write the brief. If you’ll read the output and act on it yourself — the five elements and two valves are enough.', S['body']))

E.append(Spacer(1, 10))
E.append(Paragraph('PART 4 — BUILDING YOUR OWN TEMPLATES', S['kicker']))
E.append(Paragraph('A template is elements + reasons, assembled against failure modes', S['h1']))
steps = [('1.', 'Name the task’s three most expensive failure modes (wrong denominator? invented facts? unusable format? irreversible action?).'),
         ('2.', 'Pick the element that owns each failure — the diagnosis grid on page 1; reversibility → autonomy rules.'),
         ('3.', 'Write those elements strong; keep the rest light. A template where every element is maximal is a template nobody fills in.'),
         ('4.', 'Add one filled example — the gold standard teaches faster than the instructions do.'),
         ('5.', 'Test on 3–5 real cases (one edge case), version it, name an owner, add it to the library.')]
for n, t_ in steps:
    E.append(Paragraph(f'<font face="DV-B" color="#0A5B5A">{n}</font> {t_}', S['body']))

doc.build(E)
print('elements guide written:', out)
