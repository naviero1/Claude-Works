export const meta = {
  name: 'ranking-precedent',
  description: 'Research how comparable published work presents large scored datasets, then propose outlines',
  phases: [
    { title: 'Precedent', detail: 'five traditions of published ranking and scoring work' },
    { title: 'Outlines', detail: 'candidate structures for this dataset, grounded in the precedent' },
    { title: 'Synthesize', detail: 'one comparable set of options with honest tradeoffs' },
  ],
}

const DATA = `THE DATASET THAT HAS TO BE PRESENTED. This is real, already compiled, and not negotiable in size.

  87 dishes, one at each of 87 restaurants in the Research Triangle, North Carolina, all orderable by delivery.
  43 distinct cuisines, from North Carolina barbecue to Burmese tea-leaf salad to a Chinese takeout diet menu.
  Every dish scored 0-10 on NINE criteria:
     seven health criteria - kidney (sodium), liver (saturated fat + calories), muscle (protein density),
     gut (live ferments + plant variety), energy (glycemic proxy), inflammation (omega-3 + plant diversity),
     sugar - plus flavour and cost. Six are arithmetic on the macros; three are rubric judgements.
  Weights: six health criteria x1.0, sugar x0.7, flavour x0.5, cost x0.5. A composite health score and an
     overall score follow from those.
  Per dish also: price, calories, protein, sodium, saturated fat, fibre, sugar, a build description saying
     exactly how to order it, a data-confidence tier (published nutrition / partial / estimated), and a
     DoorDash store id where one was confirmed.
  116 scored ALTERNATIVE orders at 30 of the restaurants - "order this instead" rows with their own figures.
  A verification log of 53 checked claims: what was wrong, what held, what could not be settled.

  THE FINDINGS, which are the reason anyone would read it:
   - price and health correlate at +0.05; every extra $5 buys 105mg more sodium and 1.1g less fibre
   - only four dishes are on the price-health efficient frontier; all 30 above $17 are dominated
   - flavour is bought with salt (+572mg) not saturated fat (+2.0g)
   - the spread of orders inside one restaurant (1.44 pts) exceeds the spread across all restaurants (1.25)
   - a five-dinner week costs $61.93 picked for value against $93.10 picked from the top, and covers better
   - 11 of 13 dishes got worse when rebuilt from the restaurant's own published figures

  WHAT EXISTS NOW: a 60-page reference document (the full compendium, with the ranking table, four analysis
  chapters, the model written out, and the verification log), and a 7-page brochure for a general audience
  that carries the findings and a nine-dish shortlist but NO ranking table. The task is to get the ranking
  into a presentable form for a general audience without turning it back into a 60-page reference.`

const PRECEDENT_SCHEMA = {
  type: 'object',
  required: ['works', 'lessons'],
  properties: {
    works: {
      type: 'array',
      items: {
        type: 'object',
        required: ['name', 'publisher', 'what_it_ranks', 'how_it_presents', 'entry_anatomy',
                   'what_to_steal', 'what_to_avoid'],
        properties: {
          name: { type: 'string' },
          publisher: { type: 'string' },
          era: { type: 'string', description: 'when it ran or runs' },
          scale: { type: 'string', description: 'how many entries, how many criteria' },
          what_it_ranks: { type: 'string' },
          how_it_presents: { type: 'string', description: 'the actual structure - sections, order, formats' },
          entry_anatomy: { type: 'string', description: 'what a single entry contains, field by field' },
          scoring_disclosure: { type: 'string', description: 'how much of its method it shows the reader' },
          what_to_steal: { type: 'string', description: 'specifically applicable to an 87-dish scored set' },
          what_to_avoid: { type: 'string' },
          source: { type: 'string' },
        },
      },
    },
    lessons: { type: 'string', description: 'what this tradition as a whole teaches about presenting a scored set' },
  },
}

const TRADITIONS = [
  {
    key: 'food-guides',
    brief: `RESTAURANT AND FOOD GUIDES. How the established guides structure a ranked or rated set of eating places.
Cover at least: the Michelin Guide (stars, Bib Gourmand, the Plate - and how little method it discloses);
Zagat (crowd scores out of 30 across food/decor/service, the burgundy print books, the quote-collage entry);
the Good Food Guide (UK) and its 1-10 cooking score; the Infatuation and Eater's ranked city lists and their
"38 essential restaurants" format; the World's 50 Best Restaurants and its voting method; the Bib Gourmand's
value framing specifically, since value is this dataset's central finding. For each: what one entry actually
contains on the page, how entries are ordered and grouped, and how much scoring method is shown.`,
  },
  {
    key: 'consumer-testing',
    brief: `CONSUMER TESTING PUBLICATIONS - the tradition that most closely matches a multi-criteria scored table.
Cover at least: Consumer Reports and its ratings tables with the filled-harvey-ball scale, its "recommended"
and "best buy" marks, and how it lays out a scored comparison across many criteria; Which? (UK) and its Best
Buy / Don't Buy marks; Wirecutter and its single-pick-plus-runners-up structure; Cook's Illustrated / America's
Test Kitchen and its winner-and-loser tasting tables with tasting notes; Stiftung Warentest and its German
scored-grid convention; Rtings.com for how a deep scored dataset gets navigated on the web. Pay particular
attention to HOW THEY SHOW A MULTI-CRITERIA SCORE PER ROW - harvey balls, bar segments, letter grades, coloured
cells - and to how they mark a value pick as distinct from a quality pick.`,
  },
  {
    key: 'nutrition-scoring',
    brief: `NUTRITION SCORING AND FOOD LABELLING SYSTEMS. How a composite food score gets shown to a lay reader.
Cover at least: Nutri-Score (the A-E five-colour letter scale, its algorithm, and the criticism of it);
the UK/Australia multiple traffic light label and the Health Star Rating; NOVA food-processing classification;
Guiding Stars; Open Food Facts and how it exposes both the score and its inputs; the US FDA Nutrition Facts
panel redesign and what it chose to emphasise; and any published work scoring RESTAURANT or delivery meals
rather than packaged food. For each: how a composite is communicated without hiding its inputs, and how
these systems handle the objection that any weighting is a judgement call.`,
  },
  {
    key: 'data-journalism',
    brief: `DATA JOURNALISM THAT PRESENTS A LARGE RANKED OR SCORED SET AS A STORY.
Cover at least: The Pudding's essays built on a scored dataset; FiveThirtyEight's ranking and rating pieces
(their burrito bracket is directly on point - a scored food ranking with a model); New York Times Upshot
ranking interactives; The Economist's indices (Big Mac index, liveability, democracy) and how an index is
published with its methodology; Bloomberg and Reuters graphics-led ranking pieces; and any piece where the
HEADLINE FINDING led and the full table followed. Report the actual narrative order these pieces use - where
the table sits relative to the argument, whether the full dataset is shown at all, and how they handle a
reader who wants to check the working.`,
  },
  {
    key: 'reference-guides',
    brief: `LARGE REFERENCE GUIDES WITH RANKED OR SCORED ENTRIES, especially in print, where space is finite.
Cover at least: wine - Robert Parker's Wine Advocate and Wine Spectator's 100-point scale, and how a tasting
note plus score plus price is laid out; the Good Beer Guide and CAMRA's entry format; Fodor's, Rough Guides
and Lonely Planet for how hundreds of entries get grouped and made scannable; Which Hi-Fi and What Car? for
scored product entries with a verdict line; the Guide Rouge's print typography; and Bradshaw's or a timetable
for the extreme case of dense tabular reference. Focus on: how a 60-100 entry set is CHUNKED (by score band,
by geography, by category, by price), how an entry is compressed to a scannable unit, and what typographic
devices carry a rating in a small space.`,
  },
]

phase('Precedent')
const precedent = await parallel(TRADITIONS.map(t => () =>
  agent(`You are researching precedent for a published, scored ranking of food.

${DATA}

YOUR TRADITION: ${t.brief}

Use WebSearch and WebFetch. Name real, specific, verifiable works - not generic categories. For each, describe
the ACTUAL page structure, because the goal is to borrow structure, not vibes. Where you can find an image or
description of a single entry, reproduce its anatomy field by field.
Be concrete about what would and would not transfer to 87 dishes scored on nine criteria with a strong
contrarian finding about price. Return 5-8 works.`,
    { label: `precedent:${t.key}`, phase: 'Precedent', schema: PRECEDENT_SCHEMA, effort: 'high' })
))

const works = precedent.filter(Boolean).flatMap(r => r.works || [])
const lessons = precedent.filter(Boolean).map((r, i) => `${TRADITIONS[i].key}: ${r.lessons}`)
log(`${works.length} precedent works catalogued across ${TRADITIONS.length} traditions`)

// ---------------------------------------------------------------- outlines
const OUTLINE_SCHEMA = {
  type: 'object',
  required: ['outlines'],
  properties: {
    outlines: {
      type: 'array',
      items: {
        type: 'object',
        required: ['name', 'one_line', 'precedent', 'structure', 'entry_anatomy',
                   'how_the_ranking_appears', 'best_for', 'weakness', 'length'],
        properties: {
          name: { type: 'string', description: 'a short memorable name for this structure' },
          one_line: { type: 'string', description: 'the shape in one sentence' },
          precedent: { type: 'string', description: 'which real published work this borrows from, by name' },
          structure: { type: 'array', items: { type: 'string' },
                       description: 'the ordered sections, each one line' },
          entry_anatomy: { type: 'string', description: 'what a single ranked dish looks like in this treatment' },
          how_the_ranking_appears: { type: 'string',
                       description: 'the crux - how all 87 are shown, or why fewer are' },
          handles_nine_criteria: { type: 'string', description: 'how the nine scores are made legible' },
          best_for: { type: 'string' },
          weakness: { type: 'string', description: 'be honest - every structure gives something up' },
          length: { type: 'string', description: 'realistic page or screen count' },
        },
      },
    },
  },
}

phase('Outlines')
const DESIGNERS = [
  { key: 'reader-first', brief: 'Structures that put the READER’S DECISION first - someone who wants to know what to order tonight. Borrow from consumer testing and food guides. The ranking has to serve a choice, not an archive.' },
  { key: 'argument-first', brief: 'Structures that put the ARGUMENT first - the contrarian price finding is the reason this exists. Borrow from data journalism and index publishing. The ranking is evidence for a thesis.' },
  { key: 'reference-first', brief: 'Structures that treat this as a REFERENCE people return to - a guide with a shelf life. Borrow from wine, beer and travel guides. The ranking is the product; the findings are the introduction.' },
]

const outlineRuns = await parallel(DESIGNERS.map(d => () =>
  agent(`You are proposing how to present an already-compiled dataset.

${DATA}

PRECEDENT CATALOGUED BY THE RESEARCH PASS - borrow structure from these by name:
${JSON.stringify(works.map(w => ({ name: w.name, publisher: w.publisher, how_it_presents: w.how_it_presents,
    entry_anatomy: w.entry_anatomy, steal: w.what_to_steal, avoid: w.what_to_avoid })), null, 1).slice(0, 22000)}

WHAT EACH TRADITION TEACHES:
${lessons.join('\n')}

YOUR STANCE: ${d.brief}

Propose 3 DISTINCT outlines from this stance. Each must be a real structure someone could build from - an
ordered list of sections, what a single ranked entry contains, and specifically HOW ALL 87 DISHES APPEAR
(or a defensible argument for showing fewer). Name the published work each borrows from.
The nine criteria per dish are the hard part: a reader must be able to tell what a dish is good and bad at
without decoding a legend every time. Say how your structure solves that.
Be honest about what each one gives up. Do not propose the same outline three times with different names.`,
    { label: `outline:${d.key}`, phase: 'Outlines', schema: OUTLINE_SCHEMA, effort: 'high' })
))

const outlines = outlineRuns.filter(Boolean).flatMap((r, i) =>
  (r.outlines || []).map(o => ({ ...o, stance: DESIGNERS[i].key })))
log(`${outlines.length} candidate outlines proposed`)

// ---------------------------------------------------------------- synthesize
phase('Synthesize')
const FINAL_SCHEMA = {
  type: 'object',
  required: ['recommended', 'options', 'precedent_summary', 'ranking_display_options'],
  properties: {
    recommended: { type: 'string', description: 'the name of the option you would build, and why, in 3 sentences' },
    options: {
      type: 'array',
      description: '4-5 genuinely different options, strongest first',
      items: {
        type: 'object',
        required: ['name', 'one_line', 'precedent', 'structure', 'how_the_ranking_appears',
                   'handles_nine_criteria', 'best_for', 'weakness', 'length'],
        properties: {
          name: { type: 'string' }, one_line: { type: 'string' }, precedent: { type: 'string' },
          structure: { type: 'array', items: { type: 'string' } },
          entry_anatomy: { type: 'string' },
          how_the_ranking_appears: { type: 'string' }, handles_nine_criteria: { type: 'string' },
          best_for: { type: 'string' }, weakness: { type: 'string' }, length: { type: 'string' },
        },
      },
    },
    ranking_display_options: {
      type: 'array',
      description: 'the distinct ways the 87-row ranking itself could be shown, independent of the outline',
      items: {
        type: 'object', required: ['name', 'how', 'precedent', 'tradeoff'],
        properties: { name: { type: 'string' }, how: { type: 'string' },
                      precedent: { type: 'string' }, tradeoff: { type: 'string' } },
      },
    },
    precedent_summary: { type: 'string', description: 'the 6-10 works most worth knowing about, one clause each' },
  },
}

const final = await agent(`You are choosing how to present an already-compiled dataset.

${DATA}

${outlines.length} candidate outlines were proposed from three stances:
${JSON.stringify(outlines, null, 1).slice(0, 30000)}

Precedent works catalogued:
${JSON.stringify(works.map(w => ({ n: w.name, p: w.publisher, steal: w.what_to_steal })), null, 1).slice(0, 12000)}

Produce the final comparison. Rules:
- Merge duplicates ruthlessly. Several stances will have proposed the same shape; keep the best statement of it.
- Return 4-5 options that are GENUINELY different in structure, not in tone. If two share a section order they
  are one option.
- Every option must name the real published work it borrows from.
- Separately, list the distinct ways the 87-row ranking itself could be displayed - that decision is somewhat
  independent of the outline and the user needs to see it as its own choice.
- Be honest in every 'weakness'. An option with no stated cost is not being assessed.
- Recommend one, in three sentences, and say what it gives up.`,
  { label: 'synthesize:options', phase: 'Synthesize', schema: FINAL_SCHEMA, effort: 'high' })

return { final, outlines, works, lessons }
