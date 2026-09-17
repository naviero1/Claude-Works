#!/usr/bin/env python3
# Iteration-05: rewrite Part 4 of the extended course (course_content.json)
# from "one case, five artifacts" to the nine-step Excel-first sequence.
# Prompts are inserted verbatim from assets/course_prompts.json (the single
# source shared with the deck, the workbook, the builder, the configurator).
# Reusable blocks are grabbed from the old chapter by index with type/prefix
# assertions, so drift fails loudly instead of silently.
import copy
import json
import os

HERE = os.path.dirname(__file__)
PATH = os.path.join(HERE, 'assets', 'course_content.json')
cc = json.load(open(PATH))
cps = json.load(open(os.path.join(HERE, 'assets', 'course_prompts.json')))
old = cc[3]
S = old['sections']
assert old['title'].startswith('Putting prompts to work'), old['title']


def grab(sec_i, blk_i, typ, prefix):
    b = copy.deepcopy(S[sec_i]['blocks'][blk_i])
    assert b['type'] == typ, (sec_i, blk_i, b['type'])
    probe = b.get('text') or b.get('title') or ''
    assert probe.startswith(prefix), (sec_i, blk_i, probe[:80])
    return b


def edit(block, field, old_s, new_s):
    assert old_s in block[field], (old_s[:60], block[field][:120])
    block[field] = block[field].replace(old_s, new_s)
    return block


def p(text):
    return {'type': 'p', 'text': text}


def h3(text):
    return {'type': 'h3', 'text': text}


def mono(text, caption):
    return {'type': 'mono', 'text': text, 'caption': caption}


def callout(kind, title, body):
    return {'type': 'callout', 'kind': kind, 'title': title, 'body': body}


# ---------------- S0: One dataset, nine steps ------------------------------
s0 = {'heading': 'One dataset, nine steps', 'blocks': []}
s0['blocks'].append(grab(0, 0, 'p', 'The question is deliberately ordinary'))
s0['blocks'].append(p(
    'This edition runs the case as a nine-step sequence, and the first rule is set before any prompt: '
    'the whole data arc works from ONE dataset, uploaded once at the very beginning. '
    'Supplier_Data_Exercise.xlsx goes into the chat at intake, and everything through the management '
    'mock-up - the checked analysis, the follow-up, the returned workbook, the dashboard, the '
    'five slides - flows from that single upload. Then the case widens: an email thread, three '
    'quotation documents, and a pack of reference files each bring their own source material, '
    'but the discipline stays the same.'))
s0['blocks'].append({'type': 'table', 'cols': ['Step', 'What you make', 'Where'], 'rows': [
    ['1 · Inspect, then analyze', 'A checked supplier comparison, reconciled to the source', 'Deck 34 · tab 1-Analyze-Data'],
    ['2 · Follow up in the same chat', 'A month-and-site pattern - values shown, no causes claimed', 'Deck 35 · tab 1-Analyze-Data'],
    ['3 · The assistant returns your workbook', 'Supplier_Data_Analyzed.xlsx - Summary sheet, native charts', 'Deck 36 · tab Excel-Charts'],
    ['4 · Build the dashboard', 'One self-contained offline HTML file from the returned workbook', 'Deck 37-38 · tab 2-Build-Dashboard'],
    ['5 · Present the findings', 'A five-slide management mock-up from the same verified findings', 'Deck 39 · tab 3-Present-Findings'],
    ['6 · Organize the email thread', 'The structured brief - decisions, actions, "Not stated"', 'Deck 40-41 · tab 4-Summarize-Email'],
    ['7 · Extract the quotes', 'A Raw Extraction sheet - verbatim values, cited sources', 'Deck 42 · tab Quote-Extract'],
    ['8 · Compare the quotes', 'A Normalized Comparison - or an honest "not yet"', 'Deck 43 · tab Quote-Compare'],
    ['9 · Build the research workbook', 'Evidence · Synthesis · Sources, every claim traced', 'Deck 44 · tab Research'],
]})
b = grab(0, 2, 'p', 'Why one case instead of five?')
edit(b, 'text', 'Why one case instead of five?', 'Why one case instead of nine unrelated ones?')
s0['blocks'].append(b)
s0['blocks'].append(grab(0, 3, 'h3', 'A basic prompt'))
b = grab(0, 4, 'mono', 'Analyze the supplier data')
b['caption'] = 'The starter prompt. Run it once before improving anything - then compare it with what follows.'
s0['blocks'].append(b)
s0['blocks'].append(grab(0, 5, 'p', 'This prompt runs, and it returns something confident.'))
s0['blocks'].append(grab(0, 10, 'callout', 'Write the requirement, not the wish'))

# ---------------- S1: Step 1 - inspect, then analyze ------------------------
s1 = {'heading': 'Step 1: inspect, then analyze', 'blocks': []}
b = grab(1, 0, 'p', 'Open the Data tab of Course_Workbook.xlsx.')
edit(b, 'text', 'Open the Data tab of Course_Workbook.xlsx.',
     'The live exercise starts with exactly one file open: references/exercise-data/'
     'Supplier_Data_Exercise.xlsx, a workbook whose single Data sheet holds the case records.')
s1['blocks'].append(b)
b = grab(1, 1, 'p', 'Two quirks are planted on purpose')
edit(b, 'text', ', and both are documented in that README tab: the last row of the Data tab',
     ': the last row of the Data sheet')
edit(b, 'text', 'one Inspection_Hours cell contains the text "n/a"',
     'one Inspection_Hours cell is simply blank')
s1['blocks'].append(b)
s1['blocks'].append(grab(1, 2, 'callout', 'Profile first, analyze second'))
s1['blocks'].append(mono(cps['inspect'],
    'The inspection prompt, verbatim - workbook tab 1-Analyze-Data. "Then wait" is the working '
    'boundary: no analysis until the profile is confirmed.'))
s1['blocks'].append(grab(1, 5, 'callout', 'Success check'))
b = grab(1, 6, 'p', 'The two quirks need different treatment.')
edit(b, 'text', 'The "n/a" cell', 'The blank cell')
s1['blocks'].append(b)
s1['blocks'].append(h3('The checked analysis'))
s1['blocks'].append(mono(cps['analyze'], 'The analysis prompt, verbatim - workbook tab 1-Analyze-Data.'))
b = grab(1, 9, 'p', 'Whether you run this compact version or the full improved prompt, the result is checkable')
b['text'] = 'The result is checkable to the digit:'
s1['blocks'].append(b)
s1['blocks'].append(grab(1, 10, 'table', ''))
s1['blocks'].append(grab(1, 11, 'p', 'Bravo Plastics has the highest return rate'))
s1['blocks'].append(grab(1, 12, 'callout', 'Confidence is not the deliverable'))
s1['blocks'].append(grab(1, 18, 'h3', 'Common wrong turns'))
s1['blocks'].append(grab(1, 19, 'callout', 'Five ways to be confidently wrong'))
b = grab(1, 20, 'bullets', '')
b['items'] = [i.replace('Treating the "n/a" text as zero', 'Treating the blank inspection-hours cell as zero')
              .replace('the "n/a"', 'the blank cell') for i in b['items']]
s1['blocks'].append(b)
s1['blocks'].append(grab(1, 21, 'h3', 'Acceptance checks'))
s1['blocks'].append(grab(1, 22, 'bullets', ''))
b = grab(1, 23, 'p', 'The full worked key ships')
edit(b, 'text', "in the workbook's KEY-Analysis tab (instructor material) and in the course deck's reference appendix",
     "in the workbook's KEY-Analysis tab and in the deck's speaker notes on the exercise slide (both instructor material - participant slides carry no answers)")
s1['blocks'].append(b)

# ---------------- S2: Step 2 - one follow-up, same chat ---------------------
s2 = {'heading': 'Step 2: one follow-up, in the same chat', 'blocks': [
    p('The second step costs one sentence, because it spends context the first step already paid for. '
      'The chat that ran the inspection and the analysis knows the file, the row grain, the exclusions, '
      'and the metric definitions - so a follow-up question inherits all of it. Starting a fresh chat '
      'would mean re-earning that scope; asking in the same chat keeps it pinned.'),
    mono(cps['followup'], 'The follow-up prompt, verbatim - workbook tab 1-Analyze-Data.'),
    p("This too has a checkable answer. Bravo's monthly return rate is elevated and volatile rather "
      'than steadily worsening - it peaks near 0.737% in April 2026, drops to roughly 0.14% in the '
      'quiet months of June and July 2026, and sits near 0.465% in August 2026. "Volatile, with no '
      'steady improvement" passes; any claimed cause fails, because nothing in the file supports one.'),
    callout('key', 'Patterns yes, causes no',
            'The prompt asks for the values behind the pattern and the additional data an investigation '
            'would need - and explicitly forbids a causal claim. The file shows which supplier has more '
            'returns and when; it cannot show why.'),
]}
s2['blocks'].append(grab(1, 16, 'p', 'The on-time question is the denominator lesson'))

# ---------------- S3: Step 3 - the returned workbook ------------------------
s3 = {'heading': 'Step 3: the assistant returns your workbook', 'blocks': [
    p('The third step changes the deliverable from an answer to a file. Modern assistants can edit the '
      'workbook you uploaded and hand it back - and that turns the prompt into a file contract: what '
      'the returned file is named, what it must contain, and what must survive untouched.'),
    mono(cps['excel_charts'], 'The Excel analysis-and-charts prompt, verbatim - workbook tab Excel-Charts.'),
    p('When the file comes back, open it like an auditor. The original Data sheet must be unchanged, '
      'the missing value still missing. The new Summary sheet must reconcile to the Data totals through '
      'traceable logic - formulas you can click, not pasted numbers. And the two charts must be native '
      'Excel charts: retitle one, recolor a series. If you cannot, it is a picture, and pictures fail '
      'the contract.'),
    callout('check', 'Editable-native is the acceptance test',
            'Summary totals reconcile to the Data sheet - 224,902 units shipped, 432 returns, with a '
            'reconciliation check on the sheet itself - and both charts respond to editing. '
            'A returned file that fails either test goes back with the failure named.'),
    p('The prepared fallback ships in references/exercise-data/: Supplier_Data_Analyzed.xlsx, the '
      'returned workbook this exact prompt produced. It matters beyond this step - the dashboard and '
      'the presentation both take it as their input, so the metric definitions verified here carry '
      'forward instead of being re-derived.'),
]}

# ---------------- S4: Step 4 - dashboard from the returned workbook ---------
s4 = {'heading': 'Step 4: a dashboard from the returned workbook', 'blocks': []}
s4['blocks'].append(p(
    'The fourth step turns the analysis into a tool. The input is not a fresh export - it is the '
    'returned Supplier_Data_Analyzed.xlsx from step 3, checked definitions and all, so the dashboard '
    'can never quietly disagree with the analysis about what a return rate is.'))
s4['blocks'].append(grab(2, 1, 'callout', 'You specify behavior, not code'))
s4['blocks'].append(p(
    'Workbook tab 2-Build-Dashboard carries the prompt, the states requirement, and the acceptance '
    'check side by side.'))
s4['blocks'].append(mono(cps['dashboard'], 'The dashboard prompt, verbatim - workbook tab 2-Build-Dashboard.'))
s4['blocks'].append(grab(2, 4, 'h3', 'What makes a KPI worth a tile'))
s4['blocks'].append(grab(2, 5, 'p', 'A KPI is a number someone acts on'))
s4['blocks'].append(grab(2, 6, 'bullets', ''))
s4['blocks'].append(grab(2, 7, 'h3', 'Name the parts and you can ask for them'))
s4['blocks'].append(grab(2, 8, 'p', 'Each control earns its place'))
s4['blocks'].append(grab(2, 9, 'table', ''))
s4['blocks'].append(grab(2, 10, 'h3', 'Empty, missing, and zero are three different facts'))
b = grab(2, 11, 'mono', 'Show the active selections at all times.')
b['caption'] = 'The states requirement, verbatim - workbook tab 2-Build-Dashboard.'
s4['blocks'].append(b)
s4['blocks'].append(grab(2, 12, 'p', 'An empty selection means no records matched'))
s4['blocks'].append(grab(2, 13, 'h3', 'The check that makes it trustworthy'))
b = grab(2, 14, 'mono', 'Filter to Site = Berlin')
b['caption'] = 'The acceptance check, verbatim - workbook tab 2-Build-Dashboard.'
s4['blocks'].append(b)
s4['blocks'].append(grab(2, 15, 'callout', 'The filtered check'))
s4['blocks'].append(grab(2, 16, 'p', 'This is the coordinated-views requirement made concrete'))
s4['blocks'].append(grab(2, 17, 'h3', 'The prepared fallback, and two cautions'))
b = grab(2, 18, 'p', 'A finished, checked build ships in the package')
edit(b, 'text', 'built from the same cleaned records and metric definitions as your analysis',
     'built from the same records and metric definitions as the analyzed workbook')
s4['blocks'].append(b)
s4['blocks'].append(grab(2, 19, 'p', 'Building the file yourself needs an assistant'))
s4['blocks'].append(grab(2, 20, 'callout', 'A snapshot, not a system'))

# ---------------- S5: Step 5 - five slides ----------------------------------
s5 = {'heading': 'Step 5: five slides from the same findings', 'blocks': []}
for i in range(len(S[3]['blocks'])):
    s5['blocks'].append(copy.deepcopy(S[3]['blocks'][i]))
assert s5['blocks'][2]['type'] == 'mono'
s5['blocks'][2] = mono(cps['present'], 'The presentation prompt, verbatim - workbook tab 3-Present-Findings.')

# ---------------- S6: Step 6 - the email thread -----------------------------
s6 = {'heading': 'Step 6: organize the email thread', 'blocks': []}
s6['blocks'].append(grab(4, 0, 'p', 'An email summary has a job to do.'))
s6['blocks'].append(h3('Choose the result you need'))
s6['blocks'].append(p(
    'One thread can serve five different jobs, and choosing the job IS the prompt - one sentence each '
    'once the outcome is named. In Outlook the workflow is: run the built-in Copilot summary first, '
    'then refine it in the Copilot chat pane, scoped to the same conversation, with the line that '
    'matches what you need.'))
s6['blocks'].append({'type': 'table', 'cols': ['You need', 'Say'], 'rows': [
    ['Catch me up', '"Summarize the current situation in three sentences."'],
    ['What changed', '"List changed dates or decisions and show the latest version."'],
    ['Who owes what', '"Create a table with task, owner, due date, and dependency."'],
    ['What remains open', '"List unanswered questions, approval conditions, and missing attachments."'],
    ['Prepare my reply', '"Draft a concise response. Use brackets where I still need to decide. Do not invent commitments."'],
]})
s6['blocks'].append(grab(4, 1, 'p', 'The requirement types for this artifact'))
s6['blocks'].append(mono(cps['email'], 'The structured brief, verbatim - workbook tab 4-Summarize-Email.'))
for i in range(3, 17):
    s6['blocks'].append(copy.deepcopy(S[4]['blocks'][i]))

# ---------------- S7: Step 7 - extract the quotes ---------------------------
s7 = {'heading': 'Step 7: extract the quotes', 'blocks': [
    p('After the email arc the case turns commercial. Three fictional quotation documents - '
      'Quote_Alpha_Components.pdf, Quote_Bravo_Plastics.pdf, and Quote_Cardinal_Metals.pdf in '
      'references/exercise-data/ - answer the follow-up the analysis proposed. The job is documents '
      'in, spreadsheet out, and it is deliberately split into two steps: faithful extraction first, '
      'judgment second.'),
    mono(cps['quote_extract'], 'The extraction prompt, verbatim - workbook tab Quote-Extract.'),
    p('Every discipline in that prompt exists because its absence has a failure mode. Verbatim values, '
      'because a "helpfully" rounded price cannot be audited. Original currencies and units, because '
      'silent conversion smuggles in an unstated exchange rate. "Not stated" for absent fields, because '
      'a guessed freight term looks exactly like a real one. And a source file and page per commercial '
      'value, so any number can be checked against its document in seconds.'),
    callout('key', 'Extraction before judgment',
            'Mixing extraction with comparison is how errors hide: a wrong number that enters the sheet '
            'unnoticed poisons every later calculation. Step 7 produces a sheet you can verify against '
            'the source documents; only then does step 8 get to reason on it.'),
    p('The prepared example ships as references/exercise-data/Quote_Comparison_Workbook.xlsx (sheet '
      '"Raw Extraction"), and the instructor key as instructor-keys/Quote_Comparison_Key.md - grade '
      'your run against the documents first, the key second.'),
]}

# ---------------- S8: Step 8 - compare, and refuse to pick ------------------
s8 = {'heading': 'Step 8: compare the quotes - and refuse to pick a winner', 'blocks': [
    p('Comparison is where invented certainty creeps in, so the prompt makes the rule explicit: '
      'normalize only what has a stated basis, show the formulas, and keep the original values '
      'visible next to every derived one.'),
    mono(cps['quote_compare'], 'The comparison prompt, verbatim - workbook tab Quote-Compare.'),
    p('Run on the three sample documents, the arithmetic itself is easy. At the quoted 5,000-unit '
      'volume with one-time tooling spread across the units, Alpha Components lands at USD 15.60 per '
      'unit (13.90 plus 8,500 of tooling over 5,000 units) on FOB terms; Bravo Plastics at EUR 14.70 '
      'per unit (11.90 plus a 2.80 charge) EXW; Cardinal Metals at USD 16.40 all-in, DDP, tooling '
      'waived. And that is exactly where a careful comparison stops: Bravo is quoted in euros with no '
      'exchange-rate basis supplied, and the three delivery terms put freight, duties, and risk on '
      'different sides of the line.'),
    callout('check', 'The correct answer is "not yet"',
            'The sample quotes are engineered so the honest deliverable is a comparison that stops - '
            'naming the euro conversion basis, freight, and taxes as blocking gaps - rather than a '
            'winner. If your run picked a best quote, it invented at least one basis; find which.'),
    p('A defensible "cannot compare yet, and here is exactly what is missing" is a better deliverable '
      'than a confident wrong recommendation - it hands the requester a short list of questions '
      'instead of a decision built on air. The prepared sheet ("Normalized Comparison" in the same '
      'workbook) and the instructor key show the full expected shape.'),
]}

# ---------------- S9: Step 9 - the research workbook ------------------------
s9 = {'heading': 'Step 9: reference files become a research workbook', 'blocks': [
    p('The last live step generalizes everything the quotes taught. The material is a research pack - '
      'references/exercise-data/research-pack/, four fictional files: a quality-manual excerpt, a '
      'supplier-quality newsletter, an undated scorecard guideline, and an 8D problem-solving '
      'one-pager - and a research question: how should supplier quality reviews be run? The '
      'deliverable is a workbook in three sheets: Evidence, Synthesis, Sources.'),
    mono(cps['research'], 'The research prompt, verbatim - workbook tab Research.'),
    p('The pack is engineered the way real source material behaves: two of the sources disagree on '
      'review cadence - the manual excerpt says quarterly, the newsletter says monthly - and the '
      'scorecard guideline carries no date at all.'),
    callout('check', 'Conflicts stay visible',
            'The Evidence sheet must carry both cadence claims as separate rows, the Synthesis sheet '
            'must name the conflict as a conflict, and the undated guideline keeps "Not stated" in its '
            'date column. A tidy synthesis that quietly picks a side is a defect - however confident '
            'it reads.'),
    p('The prepared example ships as references/exercise-data/Research_Workbook.xlsx - twelve traced '
      'evidence rows, a synthesis that names the agreements, the conflict, and the gaps, and a source '
      'index - with the instructor key in instructor-keys/Research_Workbook_Key.md.'),
]}

# ---------------- S10: reference exercise - explain clearly -----------------
s10 = {'heading': 'Reference exercise: explain a topic clearly', 'blocks': [
    p('One artifact steps out of the live hour in this edition and into the reference layer: the '
      'plain-language document. It remains part of the method - run it as self-study, with the same '
      'requirement discipline as everything above.'),
]}
for i in range(len(S[5]['blocks'])):
    s10['blocks'].append(copy.deepcopy(S[5]['blocks'][i]))
mono_i = [i for i, b in enumerate(s10['blocks']) if b['type'] == 'mono']
assert len(mono_i) == 1
s10['blocks'][mono_i[0]] = mono(cps['explain'],
    'The plain-language prompt, verbatim - workbook tab 5-Explain-Clearly (reference exercise).')
for b in s10['blocks']:
    if b['type'] == 'h3' and b['text'].startswith('The live topic'):
        b['text'] = 'The worked topic: reorder points and safety stock'
    if b['type'] == 'h3' and b['text'] == 'Two variations, same requirements':
        b['text'] = 'Three variations, same requirements'
    if b['type'] == 'p' and b['text'].startswith('The pack holds two self-study variations'):
        b['text'] = ('The pack holds three self-study variations beside the worked topic, each with a '
                     'SOURCE text and a sample output: household budgeting (household_budgeting.md), '
                     'the water cycle (water_cycle.md), and how an internet message travels '
                     '(internet_message.md), all in references/exercise-data/plain-language/ with the '
                     'checks in the pack README.')

# ---------------- S11: the arc, complete ------------------------------------
oldarc = S[6]['blocks']
arc_table = grab(6, 1, 'table', '')
new_rows = [arc_table['rows'][0],
            ['Returned Excel workbook',
             'File contract: returned-file naming, a Summary that reconciles, native editable charts, traceable formulas'],
            arc_table['rows'][1], arc_table['rows'][2], arc_table['rows'][3],
            ['Quotation extraction',
             'Fidelity: verbatim values, original currencies and units, "Not stated" for gaps, a citation per value'],
            ['Quotation comparison',
             'Basis discipline: normalize only on a stated basis, visible formulas, no winner while gaps remain'],
            ['Research workbook',
             'Traceability: claim-level sourcing, conflicts kept visible, confidence and open questions per row'],
            arc_table['rows'][4]]
arc_table['rows'] = new_rows
s11 = {'heading': 'The arc, complete', 'blocks': [
    p('Nine steps, one method. Every prompt in this chapter had the same anatomy - sources and scope, '
      'selected artifact requirements, acceptance evidence, and boundaries - and every step ended with '
      'a check you could actually perform: 144 detail rows reconciling to 224,902 units shipped and '
      '432 returns, a returned workbook whose Summary reconciles to its own Data sheet, a Berlin '
      'filter showing 8,575 units and 21 returns at 0.245%, five slides mapping to a coverage list, '
      'a brief that catches four planted traps, a quotation comparison that correctly refuses to name '
      'a winner, and a research workbook that keeps a planted conflict visible.'),
    arc_table,
    grab(6, 2, 'callout', 'The connecting insight'),
]}
b = grab(6, 3, 'p', 'Everything in this chapter is packaged for reuse.')
edit(b, 'text', 'The five prompts sit in copy-paste cells', 'The course prompts sit in copy-paste cells')
edit(b, 'text', 'tabs 1-Analyze-Data through 5-Explain-Clearly',
     'tabs 1-Analyze-Data, Excel-Charts, 2-Build-Dashboard, 3-Present-Findings, 4-Summarize-Email, '
     'Quote-Extract, Quote-Compare, and Research - in training order, with 5-Explain-Clearly as the '
     'reference exercise')
s11['blocks'].append(b)
b = grab(6, 4, 'p', 'One thing was constant')
edit(b, 'text', 'across all five tasks', 'across all nine steps')
s11['blocks'].append(b)

# ---------------- assemble ---------------------------------------------------
cc[3] = {
    'title': 'Putting prompts to work: one dataset, nine steps',
    'kicker': old['kicker'],
    'intro': (
        'Everything so far has been about writing requirements. This part puts them to work on a single '
        'running case: a fictional supplier-quality question whose one dataset is uploaded once, at the '
        'very beginning, and then carried through a nine-step sequence - a checked analysis and a '
        'follow-up, a returned Excel workbook with native charts, an interactive dashboard, a management '
        'presentation, an email brief, a two-step quotation comparison, and a research workbook - with a '
        'plain-language explanation as the reference exercise. The data, the prompts, and the checked '
        'answers all ship with the course, so you can run every step yourself and verify every number '
        'you produce.'),
    'sections': [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11],
}
json.dump(cc, open(PATH, 'w'), ensure_ascii=False, indent=1)
n = sum(len(s['blocks']) for s in cc[3]['sections'])
print(f'chapter 4 rewritten: {len(cc[3]["sections"])} sections, {n} blocks')
