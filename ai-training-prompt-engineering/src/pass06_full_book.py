#!/usr/bin/env python3
# Owner request (2026-09-17): the course PDF as the FULL written edition —
# compiled to the slide sections, with all knowledge, examples, copy-paste
# prompts, and exercises. Gap analysis showed two reference-layer teachings
# missing from the book; this pass adds them in slide order. (The slide-map
# front page is added in build_course_pdf.py.) One-shot; asserts fail loudly
# before the file is written.
import json
import os

P = os.path.join(os.path.dirname(__file__), 'assets', 'course_content.json')
cc = json.load(open(P))

# ---- 1. ch3: "The prompt is a document, not a sentence" (deck p81) ---------
ch3 = cc[2]
heads = [s['heading'] for s in ch3['sections']]
assert 'The prompt is a document, not a sentence' not in heads, 'already added'
at = heads.index('One task through the improvement loop') + 1
G2 = {'heading': 'The prompt is a document, not a sentence', 'blocks': [
    {'type': 'p', 'text':
     'A prompt that has been through the improvement loop a few times stops looking like a sentence '
     'and starts looking like a one-page document with named parts. That is the mature form of the '
     'work specification, and the course ships a worked template for the data-analysis case: five '
     'labeled parts, each with a reason it exists.'},
    {'type': 'mono', 'text':
     '<role>    Careful analyst: compute by RUNNING CODE - never mental math. '
     'State n. Never drop data silently.\n'
     '<data>    File · sheet · header row · what one row means · exact column '
     'names · known quirks · metric definitions.\n'
     '<task>    Numbered questions in priority order - "and stop when they’re '
     'answered."\n'
     '<method>  Profile first and show me · reconcile to a known total · flag '
     'small groups and explain the limitation · "associated with", never '
     '"caused by".\n'
     '<format>  Headline answer with the number FIRST, then the table; '
     'assumptions and caveats at the end.',
     'caption': 'The template skeleton. The full version with blanks marked is in workbook tab '
                'G2-DataAnalysis - copy-paste, don’t retype.'},
    {'type': 'table', 'cols': ['Part', 'Why it is written this way'], 'rows': [
        ['Role - code, not vibes',
         'LLM arithmetic is unreliable; code makes the computation inspectable - and the formula still '
         'needs checking through code, spreadsheet formulas, or an independent calculation.'],
        ['Data - schema first',
         'The model guessing your row grain and denominator is an important source of wrong answers.'],
        ['Task - questions, not topics',
         'Topics generate exploration; questions generate answers. The "and stop" prevents ten charts '
         'and no answer.'],
        ['Method - one anchor',
         'Reconciliation checks the totals; other errors may require other checks - and the language '
         'discipline ("associated with", never "caused by") survives into the deck leadership reads.'],
        ['Format - answer first',
         'You read the answer in ten seconds and audit the rest only if it matters.'],
    ]},
    {'type': 'callout', 'kind': 'key', 'title': 'Documents are reusable; sentences are not',
     'body': 'Every prompt in this course lives in a named workbook tab for exactly this reason: a '
             'one-page document with labeled parts can be copied, filled, reviewed, and improved. '
             'A clever sentence cannot.'},
]}
ch3['sections'].insert(at, G2)
print(f'ch3: G2 document-template section inserted at position {at}')

# ---- 2. ch4 step 6: the five email shapes (deck p82) -----------------------
ch4 = cc[3]
sec6 = [s for s in ch4['sections'] if s['heading'] == 'Step 6: organize the email thread'][0]
joined = json.dumps(sec6)
assert 'TL;DR triage' not in joined, 'already added'
# insert after the choose-the-result table's following paragraph block
# (before the requirement-types paragraph that introduces the structured brief)
idx = next(i for i, b in enumerate(sec6['blocks'])
           if b['type'] == 'p' and b['text'].startswith('The requirement types for this artifact'))
SHAPES = [
    {'type': 'h3', 'text': 'The five output shapes, named'},
    {'type': 'p', 'text':
     'Behind the menu sit five reusable output shapes. Naming the shape is what turns "summarize '
     'this" into a specification - each shape has a job, and blank cells beat guessed ones in every '
     'one of them.'},
    {'type': 'table', 'cols': ['Shape', 'What it is - and when to use it'], 'rows': [
        ['1 · TL;DR triage', 'One sentence, ~30 words: current state or decision needed - not the '
                             'history. For clearing an inbox.'],
        ['2 · The structured brief', 'OVERVIEW · DECISIONS · ACTION ITEMS · OPEN QUESTIONS. The '
                                     'default when filing, forwarding, or catching up - the prompt '
                                     'below is this shape, grown up.'],
        ['3 · Action-items table', 'Task | Owner | Due | Blocked by. For moving work into your '
                                   'to-do system.'],
        ['4 · Decisions log', 'Decision | Decided by | Reasoning | Date - settled items only, '
                              'proposals flagged. For defending choices later.'],
        ['5 · “Who owes what”', 'Every unanswered question + “X owes Y: [thing]”, latest state '
                                'only. For preparing your reply.'],
    ]},
]
sec6['blocks'][idx:idx] = SHAPES
print(f'ch4 step 6: five-shapes reference inserted at block {idx}')

json.dump(cc, open(P, 'w'), ensure_ascii=False, indent=1)
print('saved')
