// PART 3 (Prompt engineering, v1.5 importance-first rebuild) + PART 4 (Applied playbook + v1.5 walkthroughs)
const { C, F } = require('./deck_lib');

module.exports = function buildPartThree(pres, H) {
  // ---------- 21. PART 3 DIVIDER ----------
  let s = H.slide(null, 21, { dark: true });
  H.partMarker(s, 3);
  s.addText('PART 3 · PROMPT ENGINEERING', { x: 0.55, y: 2.3, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('The craft: getting what\nyou actually meant', { x: 0.55, y: 2.8, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('Seven elements, seven techniques — and for every one of them: what it buys you, and the evidence behind it.', { x: 0.55, y: 4.85, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Progress bar: part 3 — the core craft part; if the room remembers one part, make it this one.\n' +
    '2) Optional cold open (spoken, no slide): read aloud, deadpan — “Analyze the returns data and make it look good for leadership.” Then: “hold that thought — every gap you can feel in that sentence has a name on the next slides.”\n' +
    '3) One framing sentence: “Every vendor’s prompting guidance converges on the same recipe — we teach the convergence, with what each part BUYS you.”\n' +
    '4) Under 30 seconds, advance.\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none on this slide.');

  // ---------- 22. THE ANATOMY, SHOWN ----------
  s = H.slide('PART 3 · THE ANATOMY', 22);
  H.title(s, 'The universal anatomy', 'Seven parts, one body — what good looks like');
  // — the body of a prompt, drawn —
  H.card(s, 0.55, 1.58, 5.55, 4.92, C.PANEL);
  const bcx = 3.32;
  s.addShape('ellipse', { x: bcx - 0.42, y: 1.84, w: 0.84, h: 0.84, fill: { color: 'FFFFFF' }, line: { color: C.TEAL_DARK, width: 2 } });
  s.addShape('roundRect', { x: bcx - 0.55, y: 2.74, w: 1.1, h: 1.62, rectRadius: 0.28, fill: { color: 'FFFFFF' }, line: { color: C.TEAL_DARK, width: 2 } });
  s.addShape('roundRect', { x: bcx - 1.3, y: 2.92, w: 0.78, h: 0.22, rectRadius: 0.11, fill: { color: 'FFFFFF' }, line: { color: C.TEAL_DARK, width: 1.5 }, rotate: 20 });
  s.addShape('roundRect', { x: bcx + 0.52, y: 2.92, w: 0.78, h: 0.22, rectRadius: 0.11, fill: { color: 'FFFFFF' }, line: { color: C.TEAL_DARK, width: 1.5 }, rotate: -20 });
  s.addShape('ellipse', { x: bcx - 1.5, y: 3.14, w: 0.27, h: 0.27, fill: { color: C.TEAL }, line: { type: 'none' } });
  s.addShape('ellipse', { x: bcx + 1.23, y: 3.14, w: 0.27, h: 0.27, fill: { color: C.TEAL }, line: { type: 'none' } });
  s.addShape('roundRect', { x: bcx - 0.44, y: 4.38, w: 0.32, h: 1.12, rectRadius: 0.16, fill: { color: 'FFFFFF' }, line: { color: C.TEAL_DARK, width: 1.5 } });
  s.addShape('roundRect', { x: bcx + 0.12, y: 4.38, w: 0.32, h: 1.12, rectRadius: 0.16, fill: { color: 'FFFFFF' }, line: { color: C.TEAL_DARK, width: 1.5 } });
  s.addShape('ellipse', { x: bcx - 0.32, y: 2.96, w: 0.3, h: 0.3, fill: { color: C.RED }, line: { type: 'none' } });
  s.addShape('line', { x: bcx - 0.17, y: 3.28, w: 0.3, h: 0.95, line: { color: C.RED, width: 1.5, dashType: 'dash' } });
  const bodyLab = [
    [0.68, 1.86, 'ROLE', 'the head — the posture it thinks in', bcx - 0.44, 2.2, 'L'],
    [0.68, 2.86, 'TASK', 'the heart — why it beats', bcx - 0.34, 3.1, 'L'],
    [0.68, 3.86, 'CONTEXT', 'the bloodstream — feeds every organ', bcx - 0.19, 3.9, 'L'],
    [4.82, 1.86, 'FORMAT', 'the skeleton — holds the shape', bcx + 0.42, 2.2, 'R'],
    [4.82, 2.86, 'EXAMPLES', 'the hands — show how it’s done', bcx + 1.45, 3.27, 'R'],
    [4.82, 3.86, 'THE OUT', 'the immune system — rejects invented facts', bcx + 0.5, 3.7, 'R'],
    [4.82, 4.82, 'THE STOP', 'the skin — where the job ends', bcx + 0.4, 4.9, 'R'],
  ];
  bodyLab.forEach(l => {
    s.addText([
      { text: l[2], options: { bold: true, color: C.TEAL_DARK, fontSize: 9.5, breakLine: true } },
      { text: l[3], options: { color: C.SLATE, fontSize: 7.4, italic: true } },
    ], { x: l[0], y: l[1], w: 1.24, h: 0.85, fontFace: F.body, margin: 0, lineSpacingMultiple: 0.95, align: l[6] === 'L' ? 'right' : 'left' });
    const lx = l[6] === 'L' ? l[0] + 1.28 : l[0] - 0.04;
    s.addShape('line', { x: Math.min(lx, l[4]), y: Math.min(l[1] + 0.12, l[5]), w: Math.abs(l[4] - lx), h: Math.abs(l[5] - (l[1] + 0.12)), line: { color: C.MUTE, width: 0.75, dashType: 'sysDot' }, flipV: l[5] < l[1] + 0.12 });
  });
  s.addText('A prompt is a body: miss an organ and it still walks — it just fails in a predictable way.', { x: 0.8, y: 5.72, w: 5.05, h: 0.6, fontFace: F.body, fontSize: 9.5, italic: true, color: C.TEAL_DARK, margin: 0, align: 'center', lineSpacingMultiple: 1.02 });
  // — the same body, written out —
  H.card(s, 6.28, 1.58, 6.47, 4.92, 'FFFFFF', C.LINE);
  const anatEx = [
    ['ROLE', '“You are a precise editor. You add no facts that are not in the source.”'],
    ['TASK', '“Summarize the attached Q2 returns report for the operations lead.”'],
    ['CONTEXT', '“We’re a mid-size electronics manufacturer. Return rate = returns ÷ shipped. The export has a totals row — exclude it.”'],
    ['FORMAT', '“≤ 150 words: the headline number first, then three bullets.”'],
    ['EXAMPLES', '<example> March’s summary — the one the team liked </example>'],
    ['THE OUT', '“If the report doesn’t say — say so.”'],
    ['THE STOP', '“Answer only this — no recommendations yet.”'],
  ];
  anatEx.forEach((r, i) => {
    const y = 1.74 + i * 0.62;
    s.addShape('roundRect', { x: 6.5, y: y + 0.08, w: 1.18, h: 0.34, rectRadius: 0.06, fill: { color: C.TEAL }, line: { type: 'none' } });
    s.addText(r[0], { x: 6.5, y: y + 0.09, w: 1.18, h: 0.32, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 8, bold: true, charSpacing: 0.5, color: 'FFFFFF', margin: 0 });
    s.addText(r[1], { x: 7.82, y, w: 4.75, h: 0.56, fontFace: 'Consolas', fontSize: 8.6, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 1.0 });
  });
  s.addText('Note the industry line: what business you’re in is CONTEXT — name your world; never assume it knows.', { x: 6.55, y: 6.12, w: 6.0, h: 0.32, fontFace: F.body, fontSize: 8.8, italic: true, color: C.AMBER, margin: 0 });
  H.callout(s, 0.55, 6.62, 12.2, 0.5, C.TEAL_TINT, [
    { text: 'Google’s data point: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 10.5 } },
    { text: 'the most fruitful prompts averaged ~21 words with context — most people type fewer than nine. A good prompt is a short briefing, not a search query.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'edit', iconFill: C.TEAL, size: 10.5 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “one prompt, seven parts — and the parts make a BODY. Everything in Part 3 is refinements of this picture.”\n' +
    '2) Walk the FIGURE first, top to bottom, naming each organ: the head thinks in the right posture (Role) · the heart is why it beats at all (Task) · the bloodstream feeds every organ (Context) · the skeleton holds the shape (Format) · the hands show how it’s done (Examples) · the immune system rejects invented facts (the Out) · the skin is where the body ends (the Stop). Then the caption: miss an organ and it still walks — it just fails in a predictable way. That predictability is the diagnosis grid later this part.\n' +
    '3) RIGHT card: the same body written out — read it top to bottom as ONE continuous prompt (~85 words, under two minutes to write).\n' +
    '4) The amber line — owner-requested and worth saying twice: YOUR INDUSTRY IS CONTEXT. “We’re a mid-size electronics manufacturer” changes every answer downstream; people constantly assume the AI knows their world. It doesn’t until you say so.\n' +
    '5) Teal band: ~21 words vs the nine people type.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Now each element properly — and what each one BUYS you.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'Q2 = second quarter. XML-style tags = the angle-bracket fences around examples.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: rebuilt around the body figure (owner: “let’s see how creative and artistic you can get”); the vendor-recipe panel moved off-slide (owner request) — keep in reserve for questions: Anthropic (role · clear task · context · format · examples), OpenAI (role & instructions · context · format · few-shot), Google (Persona·Task·Context·Format), Microsoft (Goal·Context·Source·Expectations) — four official guides, one anatomy: convergence, not our opinion.\n' +
    'The 21-words stat: Google’s Oct 2024 Workspace guide (directional, not gospel).\n' +
    'Anthropic’s golden rule belongs in the room: show the prompt to a colleague with minimal context — if they’d be confused, the model will be too.\n' +
    'If the cold open was used: this slide is its debrief — the vague line is the returns-data prompt with every element filled in.');

  // helper for the importance-first element cards
  const elemCard = (y, h, name, job, get, why, ev, weak, strong) => {
    H.card(s, 0.55, y, 12.2, h, C.PANEL);
    s.addText(name, { x: 0.82, y: y + 0.12, w: 2.15, h: 0.4, fontFace: F.head, fontSize: 16.5, bold: true, color: C.TEAL_DARK, margin: 0 });
    s.addText(job, { x: 0.82, y: y + 0.54, w: 2.15, h: h - 0.66, fontFace: F.body, fontSize: 9.2, italic: true, color: C.INK, margin: 0, lineSpacingMultiple: 1.04 });
    const runs = [
      { text: 'What you get — ', options: { bold: true, color: C.GREEN, fontSize: 10.2 } },
      { text: get, options: { color: C.SLATE, fontSize: 10.2, breakLine: true, paraSpaceAfter: 5 } },
      { text: 'Why — ', options: { bold: true, color: C.INK, fontSize: 10.2 } },
      { text: why + ' ', options: { color: C.SLATE, fontSize: 10.2 } },
      { text: ev ? `(${ev})` : '', options: { color: C.MUTE, fontSize: 8.6, italic: true } },
    ];
    s.addText(runs, { x: 3.12, y: y + 0.1, w: 5.25, h: h - 0.2, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.07 });
    const ws = [];
    if (weak) {
      ws.push({ text: 'weak   ', options: { bold: true, color: C.RED, fontSize: 9.3 } });
      ws.push({ text: weak, options: { color: C.SLATE, fontSize: 9.6, italic: true, breakLine: true, paraSpaceAfter: 5 } });
    }
    ws.push({ text: 'strong ', options: { bold: true, color: C.GREEN, fontSize: 9.3 } });
    ws.push({ text: strong, options: { color: C.INK, fontSize: 9.6, italic: true } });
    s.addText(ws, { x: 8.55, y: y + 0.1, w: 4.0, h: h - 0.2, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.07 });
  };

  // ---------- 23. ELEMENTS 1 of 3 · ROLE + TASK ----------
  s = H.slide('PART 3 · THE ELEMENTS', 23);
  H.title(s, 'The elements · what each buys you — 1 of 3', 'Role & Task: the posture, and the question');
  elemCard(1.62, 2.42, 'Role', 'who is answering — behaviors, not titles',
    'the right altitude and posture: an expert stance you can hold it to, line by line — and a consistent voice readers can feel.',
    'a role won’t make the model smarter — two studies (162 personas; a 2025 six-model replication) found zero accuracy gain — but it reliably reshapes voice and register: readers spot an assigned personality up to 80% of the time. Behavioral commitments are checkable in the output; a title is a vibe it can fake. Beware: dumbed-down personas measurably HURT accuracy.',
    'Zheng 2024 · Wharton 2025 · PersonaLLM 2024',
    '“You are a senior analyst.”',
    '“You never invent numbers; you state n; you say what the data can’t answer.”');
  elemCard(4.2, 2.42, 'Task', 'verb + object + audience + success criterion',
    'an answer to YOUR question, sized for its audience — and a model that knows when it is done.',
    'every requirement you leave unsaid is a coin flip: models guess unstated intent right only ~41% of the time, and vague prompts are twice as likely to break when the model updates. A precise ask carries its own completion test; a vague one gets a fluent answer to a vaguer question.',
    'Yang et al. 2025',
    '“Analyze the returns data.”',
    '“What is the return rate by site for Q2, vs the 2% target?”');
  s.addText('Read each pair aloud — the weak→strong contrast is the lesson.', { x: 0.55, y: 6.78, w: 12.2, h: 0.3, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “each element now gets the full treatment: its job, what it BUYS you, why that works, and a weak-vs-strong pair.”\n' +
    '2) One card at a time, same rhythm: name and job → read the weak fill aloud, flat → read the strong fill aloud, let the contrast land → then “what you get” and the why.\n' +
    '3) Role — land two things: a role does NOT add IQ (zero accuracy gain across 162 personas, replicated in 2025), but it reliably sets voice and posture — and “explain like I’m five” personas actually cost accuracy on factual work.\n' +
    '4) Task — land the number: leave a requirement unsaid and the model guesses it right only about 4 times in 10.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“The next pair is where most disappointment actually comes from.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'n = sample size (“you state n”). Q2 = second quarter.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.5 rebuild (owner: the old definition slides “didn’t tell much” — every card now answers what-you-get / why / with evidence).\n' +
    'Evidence (full citations in notes/research/r15_element_evidence.md): personas-no-accuracy = Zheng et al. EMNLP 2024 + Wharton Prompting Science Report 4 (Dec 2025, six models — low-knowledge personas significantly hurt); personas-shape-voice = PersonaLLM, NAACL 2024 Findings (traits identifiable up to 80%); unstated intent 41.1% and 2× regression = Yang et al., arXiv 2505.13360.');

  // ---------- 24. ELEMENTS 2 of 3 · CONTEXT + FORMAT ----------
  s = H.slide('PART 3 · THE ELEMENTS', 24);
  H.title(s, 'The elements · what each buys you — 2 of 3', 'Context & Format: the facts, and the contract');
  elemCard(1.62, 2.42, 'Context', 'what the model cannot know on its own',
    'answers that are right for US — your definitions, your quirks, your constraints — instead of generically right.',
    'the model fills every gap with the most plausible guess; context deletes wrong guesses (Part 1’s launch-date drill). Measured: telling a model to answer from the supplied text cut memory-override errors from 35% to 3%, and lifted accuracy on unanswerable questions from 31% to 88%. The flip side: it trusts your context even when it’s wrong — quality is on you.',
    'Zhou 2023 · Omar 2025',
    '“Use our standard definitions.”',
    '“Return rate = returns ÷ shipped. Quirk: the export has a totals row — exclude it and say so.”');
  elemCard(4.2, 2.42, 'Format', 'the output contract — shape, cap, tone',
    'output you can use as-is: right shape, right length, no reformatting pass — and answers you can compare across runs.',
    'a numeric cap is enforceable; “short and professional” is a mood the model interprets freely. Spelling out structure is nearly free reliability — schema-enforced output went from under 40% to 100% compliant — and the 2024 scare that strict formats hurt reasoning didn’t survive replication.',
    'OpenAI 2024 · JSONSchemaBench 2025',
    '“Keep it short and professional.”',
    '“≤ 120 words: the ask in sentence one, two facts with numbers, the deadline.”');
  s.addText('Context is the anti-hallucination element; Format is the anti-rework element.', { x: 0.55, y: 6.78, w: 12.2, h: 0.3, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Same rhythm: weak aloud → strong aloud → what you get → why.\n' +
    '2) Context — the numbers to say: grounding instructions cut “the model ignored what I gave it and answered from memory” errors from 35% to 3%. Then the warning: it will trust your context when it’s WRONG, too — planted errors get repeated in up to 83% of cases. Context quality is on you.\n' +
    '3) Format — land “a numeric cap is enforceable; an adjective is a mood.” The myth to kill: “JSON makes models dumber” — the follow-up studies showed well-built format constraints cost nothing and often help.\n' +
    '4) Footer line: Context fights hallucination; Format fights rework.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“One element left — plus the two safety valves.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'JSON = a structured data format (the strictest output contract).\n' +
    '\n' +
    'CONTENT —\n' +
    'Evidence (r15): context-faithful prompting 35.2%→3.0% memorization-ratio and 30.6%→87.8% on unanswerable = Zhou et al., EMNLP 2023 Findings; planted-error propagation up to 83% = Omar et al., Communications Medicine 2025; schema compliance <40%→100% = OpenAI Structured Outputs (Aug 2024); format-constraints replication = JSONSchemaBench (2025) + dottxt rebuttal of Tam et al. 2024.\n' +
    'Teaching nuance kept honest: “reason first, format second” is still a fine manual habit — but do NOT teach “format restrictions hurt reasoning” as settled fact.');

  // ---------- 25. ELEMENTS 3 of 3 · EXAMPLES + THE TWO VALVES ----------
  s = H.slide('PART 3 · THE ELEMENTS', 25);
  H.title(s, 'The elements · what each buys you — 3 of 3', 'Examples — and the two one-sentence safety valves');
  elemCard(1.6, 1.78, 'Examples', '3–5 diverse demonstrations, edge case included',
    'work that matches the standard in your head — including how the hard cases get handled.',
    'the model imitates what it sees: examples teach format and style (few-shot lifted GPT-3 from 64% to 71% on trivia; on modern tuned models they steer shape more than facts). Include one edge case — it copies your edge-case handling too.',
    'Brown 2020 · Min 2022',
    'three clones of the happy case',
    'one typical + one edge + one reject case, fenced in tags');
  elemCard(3.52, 1.58, 'The Out', 'permission to not know',
    'an honest “the document doesn’t say” instead of an invented answer.',
    'models are trained on tests that reward guessing over abstaining. One sentence of permission cut hallucinations on planted-error questions from 53% to 23% (GPT-4o) — and under 8% on GPT-5.',
    'Omar 2025 · OpenAI 2025',
    null,
    '“If the document doesn’t say — say so.”');
  elemCard(5.24, 1.58, 'The Stop', 'the scope boundary',
    'bounded work that ends where you said — not ten charts and no answer.',
    'converts open-ended capability into a scoped job with a finish line. In Part 5 it grows up to become gates and autonomy rules for agents.',
    null,
    null,
    '“Answer these three questions, then stop — do not go exploring.”');
  s.addText('Seven elements. Each moves something out of your head onto the page — when output disappoints, one of them stayed in your head.', { x: 0.55, y: 6.92, w: 12.2, h: 0.3, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Examples: land “the model imitates what it sees — including exactly how your examples handle the hard cases; so include one hard case.”\n' +
    '2) The Out — the number to say slowly: one sentence of permission (“if it doesn’t say, say so”) cut invented answers by more than half in a clinical stress test, and to under 8% on the newest model tested. Cheapest safety feature in AI.\n' +
    '3) The Stop: one sentence converts open-ended capability into a bounded job; file it away — it becomes agent gates in Part 5.\n' +
    '4) Footer, verbatim — it is the unifying idea: every element moves something out of your head onto the page.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“All seven have a full catalog behind them — your field map.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none new on this slide.\n' +
    '\n' +
    'CONTENT —\n' +
    'Evidence (r15): few-shot 64.3→71.2 TriviaQA = Brown et al. 2020; examples-teach-format-not-facts = Min et al. EMNLP 2022 (random labels barely hurt); example ORDER can swing results from near-random to near-SOTA = Lu et al. ACL 2022 — another reason to standardize templates; the Out measured = Omar et al. 2025 (66%→44% six-model mean; GPT-4o 53%→23%) + npj Digital Medicine 2026 (GPT-5, ~8% after mitigation); mechanism = OpenAI “Why language models hallucinate” 2025.\n' +
    'The old diagnosis grid lives on the iteration slide later this part — Inspect is where it belongs.');

  // ---------- 26. THE TAXONOMY HANDOUT ----------
  s = H.slide('PART 3 · YOUR FIELD MAP', 26);
  H.title(s, 'Your field map · a handout you keep', 'The taxonomy — the catalog behind the elements');
  H.bullets(s, 0.55, 1.68, 6.15, 2.9, [
    { t: 'What it is, and why it exists: the seven elements you just met, industrialized into a catalog — so at the moment of doubt you pick a proven fill instead of improvising one.', b: true },
    { t: 'Where it came from: distilled from the official vendor guides and the studies behind this part — built for this course, versioned and updated with it.' },
    { t: 'Every slot carries a plain-language “Why it matters” — the same what-you-get logic from the last three slides, with the research behind it.' },
    { t: 'How to use it: something disappointed → name the element → pick a stronger fill from the menu. You don’t study it; you look things up in it. (Two wings: 7 generative elements + the 12 agentic blocks of Part 5.)' },
  ], { size: 12, gap: 8 });
  H.card(s, 7.0, 1.62, 5.75, 2.95, C.PANEL);
  s.addText('How to read one entry', { x: 7.3, y: 1.82, w: 5.2, h: 0.35, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
  s.addShape('roundRect', { x: 7.3, y: 2.26, w: 2.45, h: 0.42, rectRadius: 0.06, fill: { color: C.TEAL }, line: { type: 'none' } });
  s.addText('ELEMENT · Role', { x: 7.3, y: 2.27, w: 2.45, h: 0.4, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 10.5, bold: true, color: 'FFFFFF', margin: 0 });
  s.addText('who is answering', { x: 9.9, y: 2.3, w: 2.6, h: 0.34, fontFace: F.body, fontSize: 10, italic: true, color: C.MUTE, margin: 0, valign: 'middle' });
  s.addShape('line', { x: 7.55, y: 2.68, w: 0, h: 0.28, line: { color: C.TEAL, width: 1.25 } });
  s.addShape('line', { x: 7.55, y: 2.96, w: 0.15, h: 0, line: { color: C.TEAL, width: 1.25 } });
  s.addShape('roundRect', { x: 7.7, y: 2.76, w: 3.35, h: 0.4, rectRadius: 0.06, fill: { color: C.TEAL_TINT }, line: { color: C.TEAL, width: 0.75 } });
  s.addText('ATTRIBUTE · identity — pick one', { x: 7.7, y: 2.77, w: 3.35, h: 0.38, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 10, bold: true, color: C.TEAL_DARK, margin: 0 });
  s.addShape('line', { x: 7.95, y: 3.16, w: 0, h: 0.28, line: { color: C.MUTE, width: 1 } });
  s.addShape('line', { x: 7.95, y: 3.44, w: 0.15, h: 0, line: { color: C.MUTE, width: 1 } });
  [['“Careful analyst”', 8.1, 1.85], ['“Precise editor”', 10.05, 1.7], ['…', 11.85, 0.45]].forEach((o) => {
    s.addShape('roundRect', { x: o[1], y: 3.25, w: o[2], h: 0.38, rectRadius: 0.06, fill: { color: 'FFFFFF' }, line: { color: C.LINE, width: 0.75 } });
    s.addText(o[0], { x: o[1], y: 3.26, w: o[2], h: 0.36, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 9.5, color: C.SLATE, margin: 0 });
  });
  s.addText('OPTIONS — every option ships with when-to-use guidance, and every slot with its research-backed “Why it matters.” You pick from a vetted menu instead of composing from scratch.', { x: 7.3, y: 3.78, w: 5.2, h: 0.72, fontFace: F.body, fontSize: 9.5, italic: true, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.06 });
  H.card(s, 0.55, 4.75, 12.2, 1.9, C.TEAL_TINT);
  const taxStats = [['19', 'elements\n(7 generative · 12 agentic)'], ['78', 'attributes —\nthe slots you fill'], ['~290', 'vetted options,\neach with guidance'], ['18', 'presets — one-click\nstarting templates']];
  taxStats.forEach((t, i) => {
    const x = 0.85 + i * 1.95;
    s.addText(t[0], { x, y: 4.95, w: 1.8, h: 0.6, fontFace: F.head, fontSize: 30, bold: true, color: C.TEAL_DARK, align: 'center', margin: 0 });
    s.addText(t[1], { x, y: 5.6, w: 1.8, h: 0.85, fontFace: F.body, fontSize: 9, color: C.SLATE, align: 'center', valign: 'top', margin: 0, lineSpacingMultiple: 1.02 });
  });
  s.addShape('line', { x: 8.85, y: 5.0, w: 0, h: 1.4, line: { color: C.TEAL, width: 0.75 } });
  s.addText([
    { text: 'In your handout pack — ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'the printed reference, the Template Creator, and the Configurator. When you fill a template in Part 4, this catalog is the menu you are choosing from.', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 9.15, y: 4.95, w: 3.4, h: 1.5, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.1 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Hold up the physical handout (or show the PDF) and name it: “the Prompt Element Taxonomy — your field map; everyone gets one.”\n' +
    '2) Connect it BACKWARD, explicitly: “the last three slides walked the seven elements and what each buys you — this catalog is that, industrialized: every element, every slot, every vetted fill, with its why.”\n' +
    '3) LEFT bullets top to bottom; land on the last: you don’t study it — you look things up in it, like a catalog.\n' +
    '4) RIGHT card: walk the tree ONCE — element Role → attribute identity → options “Careful analyst” / “Precise editor.”\n' +
    '5) Bottom band: sweep the four numbers (19 · 78 · ~290 · 18), then the pack.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“With the map in hand — seven techniques that cover almost everything.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'HTML = HyperText Markup Language (the Template Creator runs offline as one file). XLSX = Excel format (the Configurator). PDF = the printed reference.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.5: bullets rewritten to pull forward from the new element slides (owner request: “pulling from the concepts and expanding them, from the previous slides”).\n' +
    'Source of truth is prompt-library/taxonomy/*.json — 19 elements, 78 attributes, 286 options, 18 presets; regenerate, never hand-edit.\n' +
    'If an engineer asks about the structure: element = class, attribute = property, option = allowed value, template = saved instance (keep this in reserve — jargon off-slide).');

  // ---------- 27. TOOLKIT 1 of 2 ----------
  s = H.slide('PART 3 · TECHNIQUES', 27);
  H.title(s, 'The toolkit · 1 of 2', 'The elements, turned into moves — each with a line to steal');
  const tech1 = [
    ['edit', '1 · Be specific — and say why', 'Name the audience, length, constraints — and the reason behind a rule; stated reasons improve compliance.',
      '“Two paragraphs for the plant manager, no jargon — this will be read aloud, so no bullet lists.”'],
    ['copy', '2 · Show 3–5 examples', 'The most reliable way to control format, tone, and structure. Diverse and realistic — it imitates what it sees.',
      '“Here are two summaries the team liked, and one we rejected — match the first two.”'],
    ['layers', '3 · Structure with tags', 'Separate instructions / context / input with labeled fences. The model never confuses your orders with the material.',
      '<instructions> summarize </instructions>  <report> …pasted text… </report>'],
    ['help', '4 · Give it an out', 'Permission to admit uncertainty — cuts invented answers by half or more (the numbers were two slides back).',
      '“If the spec doesn’t cover it, say ‘not specified’ — don’t guess.”'],
  ];
  tech1.forEach((t, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.62 + Math.floor(i / 2) * 2.28;
    H.card(s, x, y, 5.95, 2.14, C.PANEL);
    H.iconCircle(s, x + 0.2, y + 0.2, 0.46, t[0], C.TEAL);
    s.addText([
      { text: t[1], options: { bold: true, color: C.INK, fontSize: 12.5, breakLine: true, paraSpaceAfter: 3 } },
      { text: t[2], options: { color: C.SLATE, fontSize: 10 } },
    ], { x: x + 0.8, y: y + 0.12, w: 5.0, h: 1.1, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.05 });
    s.addShape('roundRect', { x: x + 0.24, y: y + 1.38, w: 5.5, h: 0.62, rectRadius: 0.05, fill: { color: 'FFFFFF' }, line: { color: C.LINE, width: 0.75 } });
    s.addText(t[3], { x: x + 0.38, y: y + 1.42, w: 5.25, h: 0.54, fontFace: 'Consolas', fontSize: 8.8, color: C.TEAL_DARK, margin: 0, valign: 'middle', lineSpacingMultiple: 1.02 });
  });
  H.callout(s, 0.55, 6.12, 12.2, 0.55, C.TEAL_TINT, [
    { text: 'Nothing new here: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11 } },
    { text: 'techniques 1–4 are the seven elements, applied — you met every one of them this part.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'check', iconFill: C.TEAL, size: 11 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame — say the purpose plainly (owner request): “the elements are what a prompt IS; the techniques are what you DO with them. Seven techniques cover almost everything — four now, three process moves next slide. Each card has a line you can steal verbatim.”\n' +
    '2) Per card: name the technique, then read the Consolas example line ALOUD — the examples are the teaching (owner request: a concrete line for each).\n' +
    '3) On 4, remind: the Out’s numbers were two slides back — half the invented answers, one sentence.\n' +
    '4) Teal band: nothing new — these are the elements applied.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Three process moves — and one famous retirement.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'XML = the angle-bracket tag style (technique 3).\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.5: split into two slides with a verbatim example per technique (owner request).\n' +
    'Evidence: same-content different-wrapper swings up to 40% (He et al. 2024) — structure is a real variable; vendor guides converge on delimiters/tags (Anthropic XML, OpenAI delimiters).');

  // ---------- 28. TOOLKIT 2 of 2 ----------
  s = H.slide('PART 3 · TECHNIQUES', 28);
  H.title(s, 'The toolkit · 2 of 2', 'Process moves for bigger jobs — chain, check, improve');
  const tech2 = [
    ['branch', '5 · Chain the work', 'Big job → sequential prompts with an approval between steps. You get inspectable intermediates — an audit trail.',
      '“First: outline only. I’ll approve it. Then draft section by section.”'],
    ['eye', '6 · Self-check against criteria', 'A named checklist works; “are you sure?” alone makes models WORSE (it flips correct answers).',
      '“Before finishing, verify: every number has a source · sections under 120 words · no recommendation without a risk.”'],
    ['zap', '7 · Metaprompting', 'Ask the model to improve your prompt — measured practice now, productized by every vendor.',
      '“Here’s my prompt and what it produced. What should I add or delete to get X more consistently?”'],
  ];
  tech2.forEach((t, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.62 + Math.floor(i / 2) * 2.28;
    H.card(s, x, y, 5.95, 2.14, C.PANEL);
    H.iconCircle(s, x + 0.2, y + 0.2, 0.46, t[0], C.TEAL);
    s.addText([
      { text: t[1], options: { bold: true, color: C.INK, fontSize: 12.5, breakLine: true, paraSpaceAfter: 3 } },
      { text: t[2], options: { color: C.SLATE, fontSize: 10 } },
    ], { x: x + 0.8, y: y + 0.12, w: 5.0, h: 1.1, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.05 });
    s.addShape('roundRect', { x: x + 0.24, y: y + 1.38, w: 5.5, h: 0.62, rectRadius: 0.05, fill: { color: 'FFFFFF' }, line: { color: C.LINE, width: 0.75 } });
    s.addText(t[3], { x: x + 0.38, y: y + 1.42, w: 5.25, h: 0.54, fontFace: 'Consolas', fontSize: 8.8, color: C.TEAL_DARK, margin: 0, valign: 'middle', lineSpacingMultiple: 1.02 });
  });
  H.card(s, 6.75, 3.9, 5.95, 2.14, C.AMBER_TINT);
  H.iconCircle(s, 6.95, 4.1, 0.46, 'clock', C.AMBER);
  s.addText([
    { text: 'Where’s “think step by step”? ', options: { bold: true, color: C.INK, fontSize: 12.5, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'Retired to the bench — today’s models reason by default, and boilerplate step-by-step can even hurt. The expired-advice slide, two ahead, settles it.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { x: 7.55, y: 4.05, w: 5.0, h: 1.85, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.08 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame the purpose first: “techniques 1–4 improved one prompt; these three manage a whole JOB — splitting it, checking it, and improving the prompt itself.” Then same rhythm: name the move, read the Consolas line aloud.\n' +
    '2) On 6, say the hazard number: asking “are you sure?” with no criteria made GPT-4 DROP from 95.5% to 89% — a named checklist is what works.\n' +
    '3) On 7, note it’s productized: every vendor now ships a prompt improver; optimizer-written prompts beat human ones by up to 50% on hard benchmarks.\n' +
    '4) Amber card: the famous retirement — “think step by step” — resolved two slides ahead.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Which of these survive scrutiny? The evidence corner.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none new on this slide.\n' +
    '\n' +
    'CONTENT —\n' +
    'Evidence (r15): self-correction without external signal degrades (Huang et al. ICLR 2024: GPT-4 GSM8K 95.5→89.0; the CommonSenseQA 75.8→38.1 collapse was GPT-3.5-Turbo — cite it to that model); criteria-anchored verification works (CoVe, ACL 2024: precision 0.17→0.32); metaprompting gains (OPRO ICLR 2024: up to +8% GSM8K, +50% BBH; GEPA 2025 beats RL fine-tuning).\n' +
    'Chaining = Anthropic guidance (“still useful when you need to inspect intermediate outputs”).');

  // ---------- 29. EVIDENCE CORNER ----------
  s = H.slide('PART 3 · WHAT THE EVIDENCE SAYS', 29);
  H.title(s, 'Evidence corner', 'What’s proven, what’s myth — in plain terms');
  H.card(s, 0.55, 1.65, 6.0, 2.65, C.GREEN_TINT);
  H.iconCircle(s, 0.85, 1.9, 0.5, 'check', C.GREEN);
  s.addText('Proven to work', { x: 1.5, y: 1.95, w: 4.4, h: 0.4, fontFace: F.head, fontSize: 17, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.9, 2.52, 5.4, 1.7, [
    'Being specific, giving context, showing examples — every vendor guide and every study agree',
    'Templates beat improvisation: identical asks, formatted differently, swung accuracy by up to 76 points — write it once, well, and reuse it',
    'Roles shape tone and voice reliably — use them for voice, not for smarts …',
  ], { size: 12, gap: 7 });
  H.card(s, 0.55, 4.5, 6.0, 2.15, C.RED_TINT);
  H.iconCircle(s, 0.85, 4.73, 0.5, 'x', C.RED);
  s.addText('Myth — save your typing', { x: 1.5, y: 4.77, w: 4.4, h: 0.4, fontFace: F.head, fontSize: 17, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.9, 5.32, 5.4, 1.25, [
    '… but “you are a genius” adds zero accuracy (162 personas tested; replicated 2025)',
    'Tips, threats, politeness theater: “I’ll tip $1,000” changed nothing that survives repetition',
  ], { size: 12, gap: 7 });
  H.card(s, 6.75, 1.65, 6.0, 5.0, C.PANEL);
  s.addText('The bias to design against: AI mirrors you', { x: 7.05, y: 1.86, w: 5.4, h: 0.4, fontFace: F.head, fontSize: 17, bold: true, color: C.INK, margin: 0 });
  s.addText('+49%', { x: 7.05, y: 2.3, w: 2.6, h: 0.95, fontFace: F.head, fontSize: 52, bold: true, color: C.RED, margin: 0 });
  s.addText('more often than a human would, the AI tells you you’re right — 11 leading models tested (Stanford/CMU, Science 2026)', { x: 9.75, y: 2.38, w: 2.75, h: 0.95, fontFace: F.body, fontSize: 10.5, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 1.05 });
  H.bullets(s, 7.1, 3.45, 5.4, 1.25, [
    { t: 'A single flattering exchange measurably raised users’ conviction they were right' },
    { t: 'Root cause: models are trained on human preferences — and we prefer agreement' },
  ], { size: 12, gap: 7 });
  H.callout(s, 7.05, 4.85, 5.4, 1.6, C.TEAL_TINT, [
    { text: 'The countermeasures: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12, breakLine: true } },
    { text: 'never reveal your preferred answer when asking for a review · ask for the case AGAINST (“three weakest points”) · paste your draft as “a colleague’s” · don’t treat “are you sure?” as verification.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'shield', iconFill: C.TEAL, size: 11.5 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) LEFT green card — what holds up, in plain words: specificity, context, examples, everywhere; and the case for templates — the same ask, formatted differently, swung results by up to 76 points, so write it once and reuse it.\n' +
    '2) The green card’s last line runs INTO the red card — “roles shape voice… but ‘you are a genius’ adds zero accuracy.” Neither do tips, threats, or politeness theater.\n' +
    '3) RIGHT card — the big number IS the slide: say it as one sentence first: “the AI is a mirror: it agrees with you about half again as often as a person would.” Then the two supporting bullets.\n' +
    '4) Teal countermeasures: read all four; the first one — never reveal your preferred answer — changes behavior TODAY.\n' +
    '5) 60-second live proof if you want one (no slide needed): paste a prepared draft into a fresh chat as “a colleague wrote this — give me the three weakest points,” then in a second chat as “I wrote this — what do you think?” Read both aloud; the contrast performs this slide.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“And 2026 retired some famous advice — the expired list.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'CMU = Carnegie Mellon University (co-authors of the sycophancy study).\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: aesthetic pass — bigger heads and bullets, the 49% promoted to a hero figure (owner request); the cut blind-critique demo survives as the 60-second live proof above.\n' +
    'Sources worth naming aloud: format brittleness = Sclar et al. ICLR 2024 (76-point swings from FORMATTING alone — think gauge R&R for prompts); personas = Zheng et al. EMNLP 2024 + Wharton replication Dec 2025; tipping = Salinas & Morstatter ACL 2024 + Wharton Report 3 (2025); sycophancy = Cheng et al., Science 2026.\n' +
    'The lesson isn’t “AI lies” — it’s “AI mirrors you”; blind it to your preference before asking for judgment.\n' +
    'The 2025 Wharton replication wave (25–100 runs per question) independently confirms this slide’s green and red columns.');

  // ---------- 30. THE 2026 PLAYBOOK — DO / DON'T / EXPIRED ----------
  s = H.slide('PART 3 · THE 2026 PLAYBOOK', 30);
  H.title(s, 'Do · Don’t · Expired — top five each', 'The 2026 prompting playbook');
  const playCols = [
    ['check', C.GREEN, C.GREEN_TINT, 'TO DO — reliably helps', [
      'State the task precisely — verb, constraints, success criteria, and the WHY behind each rule',
      'Structure with delimiters; standardize ONE tested, versioned template',
      'Long inputs: documents at the top, instructions at the END (bookend both ends when very long)',
      'Give an out + require citations',
      'Numeric budgets for anything measurable — words, bullets, steps',
    ]],
    ['x', C.RED, C.RED_TINT, 'NOT TO DO — hurts or wastes', [
      'Contradictory instructions — reasoning models burn tokens reconciling them',
      'Tips, threats, emotional pressure — null on average, chaos per question',
      'Bare “do not hallucinate” commands — they trigger over-refusal; use the out + citations instead',
      'Revealing your preferred answer, or “are you sure?” as verification',
      'Piling micro-rules — quality degrades past ~150 instructions; smallest prompt that keeps the contract',
    ]],
    ['clock', C.SLATE, C.PANEL, 'EXPIRED — was right in 2023', [
      '“Think step by step” → pick a reasoning model, set the effort dial',
      'Piles of examples → zero-shot first, then 3–5 format-definers',
      '“You are a world-class expert” for accuracy → persona for voice only',
      'Magic phrases (“take a deep breath”, “my career depends on it”) → clarity; real stakes as factual context',
      'Carrying your 2023 prompt stack to each new model → re-baseline on every upgrade (next slide’s loop)',
    ]],
  ];
  playCols.forEach((col, ci) => {
    const x = 0.55 + ci * 4.15;
    H.card(s, x, 1.58, 3.95, 4.78, col[2]);
    H.iconCircle(s, x + 0.2, 1.74, 0.42, col[0], col[1]);
    s.addText(col[3], { x: x + 0.72, y: 1.78, w: 3.15, h: 0.38, fontFace: F.head, fontSize: 12.5, bold: true, color: C.INK, margin: 0, valign: 'middle' });
    col[4].forEach((item, ri) => {
      const y = 2.28 + ri * 0.81;
      s.addText([
        { text: `${ri + 1}  `, options: { bold: true, color: col[1], fontSize: 10.5 } },
        { text: item, options: { color: ci === 2 ? C.SLATE : C.INK, fontSize: 8.9 } },
      ], { x: x + 0.22, y, w: 3.55, h: 0.78, fontFace: F.body, margin: 0, valign: 'top', lineSpacingMultiple: 1.0 });
    });
  });
  H.callout(s, 0.55, 6.5, 12.2, 0.6, C.TEAL_TINT, [
    { text: 'The full 8 + 8 + 8, with the study behind every line: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11 } },
    { text: 'tab PLAYBOOK of your Course Workbook — plus the one-page printout in your pack. Notice column 1, rule 4 IS column 2, rule 3 said positively: say what TO do.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'download', iconFill: C.TEAL, size: 10.5 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Why this slide exists, in one line: “half the prompting advice on the internet is from 2023 — here is the 2026 state of play, in three columns: keep, avoid, unlearn.”\n' +
    '2) GREEN column, fast — these five are Part 3 itself, condensed; nothing new, that’s the point.\n' +
    '3) RED column — slow on 3 and 4: bare “do not hallucinate” backfires (models start refusing facts that ARE in the context — researchers call it a Safety Tax; the positive out-and-cite pattern is the fix), and “are you sure?” is not verification (last slide’s mirror).\n' +
    '4) EXPIRED column — tell one origin story so the room trusts the column: “think step by step” was REAL (it took one math benchmark from 10% to 41% in 2022) — then vendors built the stepping in, and OpenAI’s own guide now says avoid chain-of-thought prompts. Advice expires when the product absorbs it. Every expired row ends with its replacement after the arrow.\n' +
    '5) Teal band: the full 8+8+8 with sources lives in the PLAYBOOK tab + the one-pager. And the coherence beat: give-an-out is “don’t hallucinate” said positively — a live demo of “say what TO do.”\n' +
    '\n' +
    'COHERENCE SEAMS (if someone spots a “contradiction”) —\n' +
    'Numeric caps vs no-absolutes: caps constrain QUANTITY; ALWAYS/NEVER locks JUDGMENT — reserve absolutes for true invariants.\n' +
    'Bookending vs no-repetition: repeat verbatim at both ends of LONG context, or not at all — paraphrased blanket repetition is the anti-pattern.\n' +
    'Task detail vs rule-piling: detail = information density (helps); piling = rule COUNT (past ~150, quality sags, early rules win).\n' +
    'CoT expired only on frontier reasoning models — still legitimate on small/local/non-thinking models.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“The craft is stable — here’s the habit that compounds it.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'CoT = Chain-of-Thought — the old “think step by step” style, now built into thinking models.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: rebuilt as the three-column playbook (owner request); full lists + anchors in notes/research/r20_do_dont_expired.md. Key anchors: Yang 2026 (41.1%) · He 2024 (wrapper swings ~40%) · GPT-4.1 guide (bookending) · Omar 2025 (out: 66→44%) · GPT-5.1 guide (length adherence) · Safety Tax arXiv:2601.02023 · Wharton R3 + Salinas 2024 (tips/threats) · Cheng Science 2026 (+49%) · IFScale arXiv:2507.11538 (~150-rule cliff) · Kojima 2022 (10.4→40.7 GSM8K origin) · Sprague ICLR 2025 · Zheng 2024/Wharton R4 (personas) · OPRO 2024 (magic-phrase post-mortem) · EmotionPrompt recalc arXiv:2409.20303 (honest average ~2.6%) · GPT-5.5 guide via Willison Apr 2026 (re-baseline).\n' +
    'What did NOT change (say if the room looks nervous): clarity, context, format, the out, grounding, iteration — the anatomy applies to every model they will ever use; scaffolding tricks retire, briefing skills compound.');

  // ---------- 31. THE HABIT · PDCA + DIAGNOSIS GRID ----------
  s = H.slide('PART 3 · ITERATION', 31);
  H.title(s, 'The habit', 'Draft → Inspect → Refine → Standardize (PDCA)');
  const iter = [
    ['edit', '1 · Draft', 'PLAN + DO', 'Write the prompt with the anatomy: role, task, context, format, examples.'],
    ['eye', '2 · Inspect', 'CHECK', 'Wrong output? Don’t reword at random — use the grid on the right to name the failed element.'],
    ['refresh', '3 · Refine', 'ACT', 'Fix that one element — or metaprompt: “rewrite this prompt so it more consistently produces X.”'],
    ['save', '4 · Standardize', 'STANDARD WORK', 'Works twice? Name it, version it, put it in the library. Then improve the standard, not the improvisation.'],
  ];
  iter.forEach((it, i) => {
    const x = 0.55 + (i % 2) * 3.05;
    const y = 1.62 + Math.floor(i / 2) * 2.05;
    H.card(s, x, y, 2.9, 1.9, i === 3 ? C.TEAL_TINT : C.PANEL);
    H.iconCircle(s, x + 0.2, y + 0.16, 0.44, it[0], C.TEAL);
    s.addText(it[1], { x: x + 0.74, y: y + 0.2, w: 2.1, h: 0.35, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
    s.addShape('roundRect', { x: x + 0.2, y: y + 0.68, w: 1.5, h: 0.28, rectRadius: 0.06, fill: { color: C.AMBER_TINT }, line: { color: C.AMBER, width: 0.6 } });
    s.addText(it[2], { x: x + 0.2, y: y + 0.69, w: 1.5, h: 0.26, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 7.5, bold: true, charSpacing: 0.5, color: C.AMBER, margin: 0 });
    s.addText(it[3], { x: x + 0.2, y: y + 1.02, w: 2.55, h: 0.85, fontFace: F.body, fontSize: 9.3, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.04 });
  });
  H.card(s, 6.85, 1.62, 5.9, 4.1, C.PANEL);
  s.addText('Inspect with this — which element failed?', { x: 7.12, y: 1.8, w: 5.4, h: 0.38, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  const grid = [
    ['wrong altitude, tone, or posture', 'Role'],
    ['answers a different (or vaguer) question', 'Task'],
    ['generically right, specifically wrong for us', 'Context'],
    ['right content, unusable shape or length', 'Format'],
    ['doesn’t match the standard in your head', 'Examples'],
    ['confidently invented', 'The Out (missing)'],
    ['sprawls past what you asked', 'The Stop (missing)'],
  ];
  grid.forEach((g, i) => {
    const y = 2.28 + i * 0.49;
    s.addText(g[0], { x: 7.12, y, w: 3.6, h: 0.42, fontFace: F.body, fontSize: 9.8, color: C.SLATE, margin: 0, valign: 'middle' });
    s.addText(g[1], { x: 10.8, y, w: 1.75, h: 0.42, fontFace: F.body, fontSize: 9.8, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    if (i < 6) s.addShape('line', { x: 7.12, y: y + 0.46, w: 5.35, h: 0, line: { color: C.LINE, width: 0.5 } });
  });
  H.card(s, 0.55, 5.95, 12.2, 1.12, C.AMBER_TINT);
  // — the PDCA wheel, drawn —
  const wcx = 1.42, wcy = 6.51, wr = 0.38;
  [['P', 0, -1], ['D', 1, 0], ['C', 0, 1], ['A', -1, 0]].forEach(q => {
    s.addShape('ellipse', { x: wcx + q[1] * wr - 0.15, y: wcy + q[2] * wr - 0.15, w: 0.3, h: 0.3, fill: { color: q[0] === 'A' ? C.AMBER : C.TEAL }, line: { type: 'none' } });
    s.addText(q[0], { x: wcx + q[1] * wr - 0.15, y: wcy + q[2] * wr - 0.16, w: 0.3, h: 0.3, align: 'center', valign: 'middle', fontFace: F.head, fontSize: 11, bold: true, color: 'FFFFFF', margin: 0 });
  });
  [[0.13, -0.36, 0.2, 0.18], [0.13, 0.2, -0.2, 0.18], [-0.34, 0.2, -0.19, -0.2], [-0.34, -0.18, 0.2, -0.19]].forEach((a, i) => {
    s.addShape('line', { x: wcx + a[0], y: wcy + a[1], w: Math.abs(a[2]), h: Math.abs(a[3]), line: { color: C.SLATE, width: 1, endArrowType: 'triangle' }, flipH: a[2] < 0, flipV: a[3] < 0 });
  });
  H.logo(s, 2.35, 6.06, 0.42, 'toyota', 'T');
  s.addText([
    { text: 'This is PDCA — Plan · Do · Check · Act: ', options: { bold: true, color: C.INK, fontSize: 11.5 } },
    { text: 'the Deming/Toyota improvement cycle, applied to prompts. The Lean Enterprise Institute now literally teaches “Prompt-Do-Check-Act.” Part 3 taught the elements; this loop turns them into tested templates; Part 6 turns templates into a team asset.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { x: 2.92, y: 6.05, w: 7.6, h: 0.95, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.04 });
  s.addShape('roundRect', { x: 10.68, y: 6.13, w: 1.92, h: 0.78, rectRadius: 0.07, fill: { color: 'FFFFFF' }, line: { color: C.AMBER, width: 1 } });
  s.addText([
    { text: 'W. EDWARDS DEMING', options: { bold: true, color: C.INK, fontSize: 8.5, breakLine: true } },
    { text: '1900–1993 · the quality pioneer whose cycle Toyota made famous', options: { color: C.SLATE, fontSize: 7.2, italic: true } },
  ], { x: 10.78, y: 6.17, w: 1.74, h: 0.7, fontFace: F.body, margin: 0, valign: 'middle', lineSpacingMultiple: 0.95 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Walk the four step cards: draft → inspect → refine → standardize — and point at the PDCA tags: this is Plan-Do-Check-Act wearing prompt clothes.\n' +
    '2) At INSPECT, gesture right: the diagnosis grid is the Check step — name the failed element, fix that one; iteration stops being random retyping.\n' +
    '3) At STANDARDIZE, say the Toyota phrase: standardized work — lock in the better way, then improve the standard. That is Part 6’s whole story.\n' +
    '4) Amber band — point at the WHEEL (P→D→C→A, forever), the Toyota mark, and the Deming card: Deming is the American quality pioneer whose cycle Toyota built its production system around — this room already runs PDCA on processes; now run it on prompts. The credential: the Lean Enterprise Institute (the Deming/Toyota home turf) published “Prompt, Do, Check, Act: the new PDCA” in May 2026. Their line: the people who get the most from these tools are the ones willing to run the loop a few more times.\n' +
    '5) Anthropic’s golden rule, spoken: show your prompt to a colleague with minimal context — if they’d be confused, the model will be too.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“One rep to cement it — then the playbook.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'PDCA = Plan-Do-Check-Act — the Deming cycle, core of Toyota-style continuous improvement (kaizen).\n' +
    'gauge R&R = Gauge Repeatability & Reproducibility — a tested template kills prompt-to-prompt variation the way a calibrated gauge kills measurement variation.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: PDCA wheel drawn + Toyota mark + Deming named card added (owner request; a public-domain-clear Deming photo wasn’t confirmed, so the named card stands in — swap in a photo only with a verified license).\n' +
    'Citation: Art Smalley (Toyota veteran), “Prompt, Do, Check, Act: The New PDCA,” Lean Enterprise Institute, May 27, 2026 — lean.org/the-lean-post (r15).\n' +
    'Why standardize, with the number: identical asks formatted differently swung accuracy up to 76 points (Sclar) — the template IS the gauge-R&R answer.');

  // ---------- 32. P3 REP ----------
  s = H.slide('THREE-MINUTE REP · PART 3', 32);
  H.title(s, 'Your turn — rebuild one prompt', 'Same report, two prompts — feel the difference');
  H.repTimer(s);
  H.card(s, 0.55, 1.75, 6.6, 2.15, C.PANEL);
  s.addText('The report — 60 words, in tab EX-Rebuild of your Course Workbook:', { x: 0.85, y: 1.92, w: 6.0, h: 0.35, fontFace: F.body, fontSize: 11, bold: true, color: C.INK, margin: 0 });
  s.addText('“Q2 returns totaled 412 units against 28,400 shipped (1.45%), up from 1.1% in Q1. Site B drove the rise; supplier packaging changes are the suspected cause. Inspection hours were flat; two corrective actions are in draft. Full breakdown by site and supplier is in the appendix table.”', { x: 0.85, y: 2.3, w: 6.0, h: 1.5, fontFace: F.body, fontSize: 10.5, italic: true, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.1 });
  const repSteps = [
    ['STEP 1', '“Summarize this report.” + paste the excerpt', 'the naive baseline — fluent, unfocused, written for nobody in particular.', 1.3],
    ['STEP 2', 'your upgrade: add a Role, a named reader in the Task, a ≤ 80-word cap, and an Out.', 'same report, four elements — watch it change league. That contrast is Part 3.', 1.45],
  ];
  let repY = 4.05;
  repSteps.forEach(st => {
    H.card(s, 0.55, repY, 6.6, st[3], 'FFFFFF', C.LINE);
    s.addText([
      { text: st[0] + ' · ', options: { bold: true, color: C.AMBER, fontSize: 10 } },
      { text: 'TYPE THIS → ', options: { bold: true, color: C.TEAL_DARK, fontSize: 10 } },
      { text: st[1], options: { color: C.INK, fontSize: 10, fontFace: 'Consolas', breakLine: true, paraSpaceAfter: 3 } },
      { text: 'WHY → ', options: { bold: true, color: C.SLATE, fontSize: 9.5 } },
      { text: st[2], options: { color: C.SLATE, fontSize: 9.5, italic: true } },
    ], { x: 0.8, y: repY + 0.08, w: 6.1, h: st[3] - 0.16, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.05 });
    repY += st[3] + 0.12;
  });
  H.card(s, 7.35, 1.75, 5.4, 3.15, C.AMBER_TINT);
  s.addText([
    { text: 'One strong answer (reveal after the rep)', options: { bold: true, color: C.AMBER, fontSize: 11.5, breakLine: true, paraSpaceAfter: 5 } },
    { text: '“You are a precise editor. Summarize this report for the operations lead in ≤ 80 words: the headline number first, what changed since Q1, and what it does NOT explain. If the report doesn’t say, say so.”', options: { color: C.SLATE, fontSize: 11, italic: true } },
  ], { x: 7.62, y: 1.95, w: 4.85, h: 2.8, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.12 });
  H.card(s, 7.35, 5.05, 5.4, 1.6, C.TEAL_TINT);
  s.addText([
    { text: 'Then compare with a neighbor: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'whose STEP 2 summary is more useful — and which ELEMENT made the difference? Different fills, same anatomy.', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 7.62, y: 5.22, w: 4.85, h: 1.3, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.08 });
  s.addText('Why this rep: it is the one moment Part 3 asks you to WRITE — the elements stick when your hands use them once. Skippable if running long.', { x: 0.55, y: 6.85, w: 12.2, h: 0.35, fontFace: F.body, fontSize: 10, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) 3:00 badge. The report is ON the slide now (and in tab EX-Rebuild, copy-paste ready) — nobody has to imagine “a report”; everyone works the same 60 words.\n' +
    '2) Run STEP 1 first, everyone: the naive ask on the excerpt. Let a couple of results be read out — fluent, unfocused.\n' +
    '3) STEP 2: three minutes to upgrade — a Role, a named reader, a ≤80-word cap, an Out. Same excerpt, second send.\n' +
    '4) Neighbor compare — the learning moment: whose version wins and WHICH ELEMENT made the difference.\n' +
    '5) Only then reveal the amber presenter answer.\n' +
    '6) Skip freely if behind — the playbook walkthroughs also exercise the elements.\n' +
    '\n' +
    'ACRONYMS —\n' +
    'Q2 = second quarter.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: the report excerpt now lives on the slide and in tab EX-Rebuild (owner: “summarize what report?” — instructions must name their object); the rep runs as two R10 steps, baseline → upgrade, so the contrast is felt, not described.\n' +
    'The excerpt is fictional and consistent with the practice dataset’s world (sites, suppliers, returns).');

  // ================= PART 4 =================

  // ---------- 33. PART 4 DIVIDER ----------
  s = H.slide(null, 33, { dark: true });
  H.partMarker(s, 4);
  s.addText('PART 4 · THE PLAYBOOK', { x: 0.55, y: 2.1, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('Thirteen templates,\nready to copy', { x: 0.55, y: 2.6, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('Eight generative + five agentic, shipped with this training in prompt-library/.\nEach: the template · a filled example · why it works · the pitfalls.', { x: 0.55, y: 4.6, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  const libNames = ['G1 Writing & editing', 'G2 Data analysis', 'G3 Evaluations & rubrics', 'G4 Spreadsheets', 'G5 Presentations', 'G6 Interactive HTML', 'G7 Research briefs', 'G8 Summarize & compare', 'A1 Mission brief', 'A2 ETL → presentation', 'A3 Recurring cycle', 'A4 CLAUDE.md starter', 'A5 Document pipeline'];
  libNames.forEach((n, i) => {
    const x = 0.55 + (i % 4) * 3.12;
    const y = 5.55 + Math.floor(i / 4) * 0.44;
    s.addText('▸ ' + n, { x, y, w: 3.0, h: 0.38, fontFace: F.body, fontSize: 10.5, color: i < 8 ? C.ON_DARK_MUTE : C.TEAL_LIGHT, margin: 0 });
  });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Progress bar: part 4. One frame: “thirteen templates ship with this training — we walk two worked examples end to end and run one live demo; the rest is your handout.”\n' +
    '2) Point at the list: G = generative, runs in any chat tool; A (in teal) = agentic, for Claude Code / Cowork-class tools — Part 5’s world.\n' +
    '3) Emphasize once: starting points to adapt, not scripts.\n' +
    '4) Advance within 30 seconds.\n' +
    '\n' +
    'ACRONYMS —\n' +
    'ETL = Extract, Transform, Load — A2’s data-pipeline shape. CLAUDE.md = the standing-instructions file agents read at session start (A4). HTML = the single-file web-page format (G6).\n' +
    '\n' +
    'CONTENT —\n' +
    'These are starting points to adapt, not scripts. Generative templates (G) run in any chat assistant; agentic templates (A, in teal) are for Claude Code / Cowork-class tools — Part 5 explains them.');

  // ---------- 34. G2 DEEP DIVE — THE PROMPT AS A DOCUMENT ----------
  s = H.slide('PART 4 · DATA ANALYSIS', 34);
  H.title(s, 'Template anatomy · G2 · Data analysis', 'The prompt is a document, not a sentence');
  // — the document mock —
  s.addShape('roundRect', { x: 0.55, y: 1.58, w: 6.05, h: 5.0, rectRadius: 0.06, fill: { color: 'FFFFFF' }, line: { color: C.SLATE, width: 1.25 }, shadow: { type: 'outer', blur: 6, offset: 2, angle: 45, color: '999999', opacity: 0.35 } });
  s.addShape('roundRect', { x: 0.55, y: 1.58, w: 6.05, h: 0.4, rectRadius: 0.06, fill: { color: C.SLATE }, line: { type: 'none' } });
  ['E74C3C', 'F1C40F', '2ECC71'].forEach((dot, i) => s.addShape('ellipse', { x: 0.72 + i * 0.2, y: 1.71, w: 0.13, h: 0.13, fill: { color: dot }, line: { type: 'none' } }));
  s.addText('G2_data_analysis.txt — your template, one page', { x: 1.4, y: 1.6, w: 5.0, h: 0.36, fontFace: 'Consolas', fontSize: 9.5, color: 'FFFFFF', margin: 0, valign: 'middle' });
  const g2 = [
    ['<role>', 'Careful analyst: compute by RUNNING CODE — never mental math. State n. Never drop data silently.', 'Why code, not vibes', 'LLM arithmetic is unreliable; code execution makes the math real. No code tool → don’t trust computed numbers.'],
    ['<data>', 'File · sheet · header row · what one row means · exact column names · known quirks · metric definitions.', 'Why schema first', 'The model guessing your grain and denominator is the #1 source of wrong answers.'],
    ['<task>', 'Numbered questions in priority order — “and stop when they’re answered.”', 'Why questions, not topics', 'Topics generate exploration; questions generate answers. The stop prevents ten charts and no answer.'],
    ['<method>', 'Profile first and show me · reconcile to a known total · flag n < 20 · “associated with”, never “caused by”.', 'Why one anchor', 'One reconciliation beats ten checks — and the language discipline survives into the deck leadership reads.'],
    ['<format>', 'Headline answer with the number FIRST, then the table; assumptions and caveats at the end.', 'Why answer-first', 'You read the answer in 10 seconds and audit the rest only if it matters.'],
  ];
  g2.forEach((r, i) => {
    const y = 2.14 + i * 0.88;
    s.addShape('roundRect', { x: 0.75, y, w: 5.65, h: 0.8, rectRadius: 0.04, fill: { color: i % 2 ? 'FFFFFF' : C.TEAL_TINT }, line: { color: C.LINE, width: 0.5 } });
    s.addText(r[0], { x: 0.88, y: y + 0.03, w: 1.15, h: 0.74, fontFace: 'Consolas', fontSize: 11, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText(r[1], { x: 2.06, y: y + 0.03, w: 4.25, h: 0.74, fontFace: 'Consolas', fontSize: 7.8, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 1.0 });
    // connector to the why-card
    s.addShape('line', { x: 6.42, y: y + 0.4, w: 0.5, h: 0, line: { color: C.MUTE, width: 0.75, dashType: 'sysDot' } });
    H.card(s, 6.94, y - 0.02, 5.8, 0.84, C.PANEL);
    s.addText([
      { text: r[2] + ' — ', options: { bold: true, color: C.INK, fontSize: 10 } },
      { text: r[3], options: { color: C.SLATE, fontSize: 9.2, italic: true } },
    ], { x: 7.18, y: y + 0.03, w: 5.35, h: 0.74, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.0 });
  });
  H.callout(s, 0.55, 6.7, 12.2, 0.45, C.TEAL_TINT, [
    { text: '✂ Copy-paste, don’t retype: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 10 } },
    { text: 'the full G2 template — blanks marked — is in tab G2-DataAnalysis of your Course Workbook; every prompt in this course lives in a named tab there.', options: { color: C.SLATE, fontSize: 10 } },
  ], { iconName: 'copy', iconFill: C.TEAL, size: 10 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame with the visual: “THIS is what a serious prompt looks like — a one-page DOCUMENT with labeled blocks, not a sentence. The other twelve templates share this shape.”\n' +
    '2) Walk the page TOP TO BOTTOM; per block: name it, one line on what goes in, then read the matching right-hand WHY aloud — the why is the teaching.\n' +
    '3) Slow on <method>: “reconcile to a known total — one anchor beats ten checks.”\n' +
    '4) Teal band — the workbook system, said once for the whole course: every prompt they will ever need today is copy-paste ready in a NAMED TAB of the Course Workbook. Nobody retypes anything.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Enough anatomy — let’s RUN it, on a real file, step by step.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'LLM = Large Language Model. n = sample size (flag n < 20). G2 = this template’s library code.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: rebuilt as a document mock with side-car whys (owner: more visual); workbook-tab pointer added (owner: all prompts copyable from Excel).\n' +
    'Evidence for code-not-vibes: GPT-4 scored ~59% on 3-digit × 3-digit multiplication, falling toward zero as digits grow (Faith and Fate, NeurIPS 2023) — code execution hands the model a calculator. All four major tools now run code for analysis.\n' +
    'For recurring or multi-file pipelines, the agentic sibling is A2 (Part 5).');

  // ---------- 35. WALKTHROUGH · DATA ANALYTICS — THE SETUP ----------
  s = H.slide('PART 4 · WALKTHROUGH 1 · DATA', 35);
  H.title(s, 'Walkthrough · AI data analysis — the setup', 'A real file, a real sequence — any AI tool');
  H.card(s, 0.55, 1.62, 5.9, 2.6, C.PANEL);
  s.addText('Your practice data (in the Course Workbook)', { x: 0.85, y: 1.82, w: 5.3, h: 0.38, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.9, 2.28, 5.3, 1.9, [
    { t: 'Course_Workbook.xlsx, Data tab — 12 months of fictional supplier deliveries: 4 sites × 3 suppliers, 144 rows (units, returns, defects, inspection hours, cost, on-time).' },
    { t: 'The README tab defines every column — that tab IS your <data> block: paste it, don’t retype it.', b: true },
    { t: 'Two quirks are planted on purpose. A good first prompt finds both.' },
  ], { size: 10.8, gap: 7 });
  H.card(s, 0.55, 4.38, 5.9, 2.2, C.TEAL_TINT);
  s.addText([
    { text: 'The rule the whole walkthrough teaches: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12, breakLine: true, paraSpaceAfter: 4 } },
    { text: 'never start with a question. Start by making the AI LOOK at the data and tell you what it sees — profile first, analyze second. Every wrong answer you’ve ever gotten from AI data analysis started with a skipped profile.', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 0.85, y: 4.56, w: 5.3, h: 1.9, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.1 });
  // — the sequence, vertical and numbered —
  H.stepBig(s, 6.75, 1.62, 6.0, 1, 'UPLOAD the workbook to your AI', C.TEAL_TINT);
  s.addShape('line', { x: 9.75, y: 2.16, w: 0, h: 0.2, line: { color: C.TEAL, width: 1.5, endArrowType: 'triangle' } });
  H.stepBig(s, 6.75, 2.4, 6.0, 2, 'TYPE THIS — then wait (tab G2-DataAnalysis)', C.TEAL_TINT);
  H.card(s, 6.75, 2.98, 6.0, 1.5, 'FFFFFF', C.LINE);
  s.addText('Work only with the Data tab of this workbook. Before any analysis: profile it — rows, columns, types, missing or odd values, and anything that would trip a calculation. Show me the profile and STOP. Do not analyze yet.', { x: 6.95, y: 3.08, w: 5.6, h: 1.32, fontFace: 'Consolas', fontSize: 9.6, color: C.TEAL_DARK, margin: 0, lineSpacingMultiple: 1.1 });
  s.addShape('line', { x: 9.75, y: 4.52, w: 0, h: 0.2, line: { color: C.TEAL, width: 1.5, endArrowType: 'triangle' } });
  H.stepBig(s, 6.75, 4.76, 6.0, 3, 'CHECK the profile against this reveal', C.AMBER_TINT);
  H.card(s, 6.75, 5.34, 6.0, 1.32, C.AMBER_TINT);
  s.addText([
    { text: 'A good profile finds: ', options: { bold: true, color: C.AMBER, fontSize: 10.5 } },
    { text: '144 data rows + a TOTAL row to exclude · one Inspection_Hours cell that says “n/a” · clean types elsewhere. Missed a quirk? That’s why this step exists — tell it, and make it re-profile.', options: { color: C.SLATE, fontSize: 10 } },
  ], { x: 6.98, y: 5.44, w: 5.55, h: 1.12, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.06 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “we picked data analysis as walkthrough #1 because it is the single most-used office AI case — and the easiest to get quietly wrong.”\n' +
    '2) LEFT top: the practice data lives in the Course Workbook everyone already has — Data tab is the dataset, README tab is the <data> block from G2, ready-made.\n' +
    '3) Teal card — the rule, verbatim: never start with a question; profile first, analyze second.\n' +
    '4) RIGHT: the numbered sequence ① upload ② type-and-wait ③ check — run it live (Copilot in Excel, a chat upload, or the company assistant — same prompt works in all three).\n' +
    '5) The ③ reveal: the file has two planted traps; a good profile catches both. If the room’s AI missed one, that IS the lesson.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Data profiled and trusted — now the questions.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'RAG = Retrieval-Augmented Generation (Part 1) — “your company RAG assistant” = the internal upload-and-ask tool.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: sequence rebuilt as the vertical ①②③ flow (owner: order was confusing); dataset folded into Course_Workbook.xlsx (Data + README tabs) so trainees carry ONE file.\n' +
    'The workbook lives in deliverables/exercise-data/ and regenerates from src/build_exercise_pack.py (seeded — the numbers quoted on these slides stay true after a rebuild).\n' +
    'Planted quirks: TOTAL row at the bottom; “n/a” text in Inspection_Hours around row 38. Both documented in the README tab.\n' +
    'All data fictional and generated — safe to upload anywhere policy allows.');

  // ---------- 36. WALKTHROUGH · CORRELATIONS & COMPARISONS ----------
  s = H.slide('PART 4 · WALKTHROUGH 1 · DATA', 36);
  H.title(s, 'Walkthrough · correlations & comparisons', 'Numbered questions in, defended answers out');
  const steps2 = [
    ['Ask numbered questions — not topics',
      'Working only on the 144 data rows (exclude the TOTAL row; treat the “n/a” as missing and say so): 1) Which supplier has the highest defect rate — (Defects_Found + Units_Returned) ÷ Units_Shipped — overall, and is it getting better or worse across the year? 2) Is there a relationship between Inspection_Hours and Units_Returned? Compute the correlation by running code, show your working, and describe it as an association, not a cause. 3) Rank the sites by On_Time_Percent. Answer in that order, then stop.'],
    ['Comparative analysis — the scorecard',
      'Build a supplier scorecard: one row per supplier — defect rate, return rate, average unit cost, average on-time % — best value per column marked. Then one paragraph: if we had to consolidate to one supplier, which one, and what does this data NOT tell us about that decision?'],
    ['The trust check',
      'Reconcile: sum Units_Shipped across your 144 rows and compare it to the TOTAL row you excluded. Do they match? If not, what happened?'],
  ];
  steps2.forEach((st, i) => {
    const y = 1.62 + i * 1.68;
    H.stepBig(s, 0.55, y, 12.2, i + 1, st[0], C.TEAL_TINT);
    H.card(s, 0.55, y + 0.56, 12.2, i === 0 ? 1.04 : 0.86, 'FFFFFF', C.LINE);
    s.addText(st[1], { x: 0.75, y: y + 0.63, w: 11.8, h: (i === 0 ? 1.04 : 0.86) - 0.14, fontFace: 'Consolas', fontSize: 8.4, color: C.TEAL_DARK, margin: 0, lineSpacingMultiple: 1.06 });
  });
  H.callout(s, 0.55, 6.7, 12.2, 0.42, C.AMBER_TINT, [
    { text: 'The tension the data holds: ', options: { bold: true, color: C.INK, fontSize: 10 } },
    { text: 'the cheapest supplier is also the most defective, and its defect rate is climbing — the scorecard question has no lazy answer.', options: { color: C.SLATE, fontSize: 10 } },
  ], { iconName: 'target', iconFill: C.AMBER, size: 10 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Read STEP 1 aloud and point at its G2 DNA: numbered questions in priority order · the quirks handled explicitly · compute by running code · “associated with, not caused by” · then STOP.\n' +
    '2) Expected findings (your answer key): Bravo Plastics is the defect leader and trending worse; Inspection_Hours vs Units_Returned comes out NEGATIVE (more inspection, fewer escapes — planted); Osaka leads on-time, Monterrey trails.\n' +
    '3) STEP 2: the scorecard tension — Bravo is cheapest AND most defective. The paragraph question teaches the habit of asking what the data does NOT say (volumes, switching costs, quality trend causes).\n' +
    '4) STEP 3 is the G2 reconciliation anchor performed: the sums should match the TOTAL row. One anchor beats ten checks.\n' +
    '5) Timing: run steps live if the room is hands-on (10 min), or narrate from prepared outputs.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Same discipline, different input — three PDFs nobody wants to read.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none new on this slide.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: step headers joined the numbered-banner family; all three prompts are copy-paste ready in tab G2-DataAnalysis of the Course Workbook.\n' +
    'The dataset is engineered so these findings are real: Bravo base defect rate 1.6% trending +0.08%/month; catch-rate rises with inspection hours (escapes fall); Osaka on-time ~97%, Monterrey ~88%; December volume dip.\n' +
    'If someone asks “can Copilot do correlations?” — yes: in Excel it writes the formulas or Python; the prompt is identical.');

  // ---------- 37. WALKTHROUGH · THE QUOTATION COMPARISON ----------
  s = H.slide('PART 4 · WALKTHROUGH 1 · DATA', 37);
  H.title(s, 'Walkthrough · three quotes, one table', 'Messy documents in, decision-ready table out');
  H.card(s, 0.55, 1.62, 5.9, 2.5, C.PANEL);
  s.addText('The input (also in your pack)', { x: 0.85, y: 1.8, w: 5.3, h: 0.35, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.9, 2.24, 5.3, 1.8, [
    { t: 'Three fictional supplier quotations (PDFs) answering the same RFQ — Alpha Components, Bravo Plastics, Cardinal Metals.' },
    { t: 'Deliberately NOT comparable at first glance: one quotes in euros per 1,000 units, one excludes tooling, one includes shipping, warranties differ 6–24 months.', b: true },
  ], { size: 10.8, gap: 7 });
  H.card(s, 0.55, 4.28, 5.9, 2.3, C.AMBER_TINT);
  s.addText([
    { text: 'What the room should notice: ', options: { bold: true, color: C.AMBER, fontSize: 11.5, breakLine: true, paraSpaceAfter: 4 } },
    { text: 'the “cheapest” quote stops looking cheapest once currency, per-1,000 pricing, tooling and freight are normalized — exactly the kind of buried-terms error AI is good at catching, IF you ask for normalization explicitly. The AI’s exchange rate must be flagged as an assumption to verify.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { x: 0.85, y: 4.46, w: 5.3, h: 2.0, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.08 });
  const qsteps = [
    ['Extract & normalize',
      'Extract every commercial term from these three quotations into one table: supplier, unit price, tooling, MOQ, lead time, payment terms, warranty, shipping terms, validity. Normalize prices to USD per unit at 5,000 units — state the EUR rate you use and flag it as an assumption — include tooling amortized over the 5,000 units, and note what shipping does and doesn’t include. Flag anything that is still not comparable.'],
    ['Recommend, with caveats',
      'Now: which quote has the lowest true landed cost at 5,000 units? Which is the best overall value once warranty, lead time and payment terms count? And what would you negotiate with each supplier before deciding? Keep it to one page; separate facts from judgment.'],
  ];
  qsteps.forEach((st, i) => {
    const y = 1.62 + i * 2.52;
    H.stepBig(s, 6.75, y, 6.0, i + 1, st[0], C.TEAL_TINT);
    H.card(s, 6.75, y + 0.56, 6.0, 1.86, 'FFFFFF', C.LINE);
    s.addText(st[1], { x: 6.95, y: y + 0.66, w: 5.6, h: 1.66, fontFace: 'Consolas', fontSize: 8.7, color: C.TEAL_DARK, margin: 0, lineSpacingMultiple: 1.08 });
  });
  s.addText('Works the same in a chat upload, Copilot, or your company assistant — this is G8 (summarize & compare) grown teeth. ✂ Both prompts: tab EX-Quotes of your Course Workbook.', { x: 0.55, y: 6.72, w: 12.2, h: 0.32, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “same discipline, messier input: three PDFs answering one RFQ — and they don’t line up on purpose.”\n' +
    '2) Name the traps out loud BEFORE running: Bravo quotes EUROS per 1,000 units and excludes tooling and freight (EXW); Alpha is straightforward but FOB; Cardinal looks priciest but includes shipping (DDP), waives tooling, and doubles the warranty.\n' +
    '3) Run STEP 1; check the table catches: per-1,000 → per-unit conversion, the flagged EUR assumption, tooling amortization, shipping inclusions.\n' +
    '4) STEP 2: the punchline — “cheapest” moves once terms are normalized; the negotiation question turns analysis into action.\n' +
    '5) Land the safety line: the exchange rate is an ASSUMPTION the AI must flag — and you must verify (house rule from Part 1).\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Analysis is answers. Next: turning answers into a file you can circulate.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'RFQ = Request for Quotation. MOQ = Minimum Order Quantity.\n' +
    'EXW / FOB / DDP = shipping terms (Incoterms): EXW = buyer collects at the factory; FOB = seller loads, buyer ships; DDP = delivered to your dock, duties paid.\n' +
    '\n' +
    'CONTENT —\n' +
    'Quote contents (answer key, from the generated PDFs): Alpha $13.90/u + $8,500 tooling, FOB, Net 30, 12-mo, 60-day validity · Bravo €11,900 per 1,000 (≈€11.90/u) + €14,000 tooling excluded, EXW, Net 60, 6-mo, 30-day validity · Cardinal $16.40/u, tooling waived, DDP, Net 45, 24-mo, 90-day validity.\n' +
    'At ~1.08 USD/EUR: Bravo ≈ $12.85/u + $3.02/u tooling ≈ $15.87 + freight; Alpha ≈ $15.60 + freight; Cardinal $16.40 all-in with double warranty — the ranking genuinely depends on freight and terms, which is the point.');

  // ---------- 38. WALKTHROUGH · FROM ANSWER TO ARTIFACT ----------
  s = H.slide('PART 4 · WALKTHROUGH 1 · DATA', 38);
  H.title(s, 'Walkthrough · from answer to artifact', 'Make the AI ship the file, not just the answer');
  H.stepBig(s, 0.55, 1.62, 12.2, 4, 'The deliverable — ship the file, not just the answer', C.TEAL_TINT);
  H.card(s, 0.55, 2.18, 12.2, 1.3, 'FFFFFF', C.LINE);
  s.addText('Turn the supplier scorecard into a one-sheet spreadsheet I can circulate: a README tab explaining every column and where the numbers came from, the scorecard tab with formulas visible — not pasted values — and a short caveats section (the “n/a” cell, the excluded TOTAL row, the exchange-rate assumption). Use only numbers from this chat; if one is missing, leave the cell blank and say so — do not invent it.', { x: 0.75, y: 2.28, w: 11.8, h: 1.12, fontFace: 'Consolas', fontSize: 9.2, color: C.TEAL_DARK, margin: 0, lineSpacingMultiple: 1.1 });
  H.card(s, 0.55, 3.65, 5.9, 2.75, C.PANEL);
  s.addText([
    { text: 'Why these spec lines matter', options: { bold: true, color: C.INK, fontSize: 12.5, breakLine: true, paraSpaceAfter: 5 } },
    { text: 'README tab — the file explains itself when it’s forwarded without you.\nFormulas visible — anyone can audit; nothing is a magic number.\nCaveats section — the quirks and assumptions travel WITH the numbers.\n“Don’t invent” + blank cells — the Out, working inside a spreadsheet.', options: { color: C.SLATE, fontSize: 10.8 } },
  ], { x: 0.85, y: 3.85, w: 5.3, h: 2.4, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.15 });
  H.card(s, 6.75, 3.65, 6.0, 2.75, C.TEAL_TINT);
  s.addText([
    { text: 'The same move, everywhere', options: { bold: true, color: C.TEAL_DARK, fontSize: 12.5, breakLine: true, paraSpaceAfter: 5 } },
    { text: 'Copilot in Excel: “build this as a new sheet with formulas” — it writes them in place.\nChat assistants: they produce the .xlsx for download.\nAgentic tools (Part 5): they build the file, chart it, and write the email that sends it.\nThe prompt barely changes — the delegation level does.', options: { color: C.SLATE, fontSize: 10.8 } },
  ], { x: 7.05, y: 3.85, w: 5.4, h: 2.4, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.15 });
  H.callout(s, 0.55, 6.6, 12.2, 0.5, C.RED_TINT, [
    { text: 'Before it ships: ', options: { bold: true, color: C.RED, fontSize: 10.5 } },
    { text: 'open the file, spot-check two formulas against the chat, and verify the exchange rate — the house rule never retires.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'alert', iconFill: C.RED, size: 10.5 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “the last mile — most people copy AI answers into Excel by hand. Don’t: make it ship the artifact.”\n' +
    '2) Read STEP 4 aloud, then the left card: each spec line exists for a reason — README (self-explaining file), visible formulas (auditable), caveats (assumptions travel), don’t-invent (the Out, in spreadsheet form).\n' +
    '3) Right card: the same move in every tool — only the delegation level changes; Part 5 takes it to the fully-delegated end.\n' +
    '4) Red band: verify before it ships. Always.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“That’s the most-used play in office AI, end to end. Now watch two more templates run live.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none new on this slide.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: header joined the numbered-banner family (steps ①–④ across the walkthrough).\n' +
    'This four-slide walkthrough (35–38) = G2 + G8 executed on the practice pack; G4’s spreadsheet rules (README tab, formulas-not-values) reappear as the deliverable spec — the templates compose.\n' +
    'All walkthrough prompts (steps 0–4) are copy-paste ready in tab G2-DataAnalysis of the Course Workbook.\n' +
    'Future library note (ledger): consider promoting the quotation-comparison sequence to a numbered template.');
  // v1.6 WALKTHROUGH 2 (email summarization) follows the live demo — see slides 40–41; slide 42 closes Block 2.

  // ---------- 39. LIVE DEMO · DASHBOARD FROM A PASTE ----------
  s = H.slide('PART 4 · LIVE DEMO', 39);
  H.title(s, 'Live demo · a dashboard from a paste (G6)', 'One prompt, one file, working software');
  const d2 = [
    ['1 · The data', 'Paste a small generic table (20–30 rows: period, category, count — prepared in advance, nothing internal).'],
    ['2 · Run G6', 'Ask for: a SINGLE-FILE interactive HTML dashboard — KPI tiles, one filterable chart, a sortable table; data embedded; works offline from disk; formulas visible.'],
    ['3 · Open it', 'Download the file, double-click it, filter something, sort something. No install, no server, no login.'],
  ];
  d2.forEach((d, i) => {
    const y = 1.7 + i * 1.35;
    H.card(s, 0.55, y, 7.6, 1.2, C.PANEL);
    s.addText([
      { text: d[0] + '  ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12.5, breakLine: true, paraSpaceAfter: 2 } },
      { text: d[1], options: { color: C.SLATE, fontSize: 10.8 } },
    ], { x: 0.82, y: y + 0.08, w: 7.05, h: 1.04, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.05 });
  });
  H.card(s, 8.45, 1.7, 4.3, 3.95, C.AMBER_TINT);
  s.addText([
    { text: 'What the room should notice', options: { bold: true, color: C.AMBER, fontSize: 12, breakLine: true, paraSpaceAfter: 5 } },
    { text: 'The deliverable is a tool, not a text. The spec lines that made it trustworthy: single file · offline · data embedded · nothing hard-coded · formulas on screen.\n\nCaveats to say out loud: it is a snapshot, not a live system — and share the FILE, not a public link.', options: { color: C.SLATE, fontSize: 10.8 } },
  ], { x: 8.7, y: 1.9, w: 3.8, h: 3.6, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.1 });
  H.callout(s, 0.55, 5.8, 12.2, 0.6, C.PANEL, [
    { text: 'Backup plan: ', options: { bold: true, color: C.INK, fontSize: 11 } },
    { text: 'if generation runs long, open the pre-built copy from your desktop and narrate the prompt — the room still sees prompt → working software.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'refresh', iconFill: C.SLATE, size: 11, line: C.LINE });
  H.callout(s, 0.55, 6.52, 12.2, 0.6, C.AMBER_TINT, [
    { text: 'Who can run this: ', options: { bold: true, color: C.AMBER, fontSize: 10.5 } },
    { text: 'it needs a tool that writes and packages code — Claude (Artifacts), ChatGPT (Canvas), Gemini (Canvas), typically on paid tiers; Copilot chat can’t build this today. No access? Hand the same spec to IT — or ask for the Excel version.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'key', iconFill: C.AMBER, size: 10.5 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “this time the deliverable is a tool, not a text.” This one stays a PRESENTER demo — you run it; the room watches (not everyone’s tool can build it — see the amber band).\n' +
    '2) Run the three step cards IN ORDER: paste the prepared table → run G6 → download the file, double-click it, filter something, sort something.\n' +
    '3) WHILE it generates, narrate the amber spec lines — single file, offline, data embedded, nothing hard-coded, formulas visible — those lines are what made it trustworthy.\n' +
    '4) Say the two caveats OUT LOUD: it is a snapshot, not a live system; share the FILE, not a public link.\n' +
    '5) Grey band is your safety net: pre-built copy on the desktop. Amber band answers the inevitable “can MY AI do this?” — capability, not skill: code/canvas tools (mostly paid tiers) can; Copilot chat can’t; the fallback is the spec to IT or an Excel version.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“One more daily-life play — the inbox.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'HTML = HyperText Markup Language — the single-file web-page format. KPI = Key Performance Indicator (the number tiles). G6 = the interactive-HTML template’s library code.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: capability strip added (owner asked: “this won’t be able to be created by all AIs, maybe just Claude or a paid subscription, correct?” — correct: single-file HTML needs a code/canvas-capable tool; capability verified Sep 2026: Claude Artifacts, ChatGPT Canvas, Gemini Canvas — largely paid; Copilot chat in-tenant cannot).\n' +
    'Pre-stage the data table and the G6 prompt in a text file so the demo is paste-paste-run. Budget 6–8 minutes.');

  // ---------- 40. WALKTHROUGH 2 · EMAIL — THE FIVE SHAPES ----------
  s = H.slide('PART 4 · WALKTHROUGH 2 · EMAIL', 40);
  H.title(s, 'Walkthrough · the inbox play', 'Five shapes — pick the one for the job');
  const shapes = [
    ['1 · TL;DR triage', 'One sentence, 30 words: current state or decision needed — not the history. For clearing an inbox.'],
    ['2 · The structured brief', 'OVERVIEW · DECISIONS · ACTION ITEMS · OPEN QUESTIONS. The default when filing, forwarding, or catching up.'],
    ['3 · Action-items table', 'Task | Owner | Due | Blocked by. Blank cells beat guessed ones. For moving work into your to-do system.'],
    ['4 · Decisions log', 'Decision | Decided by | Reasoning | Date — settled only, proposals flagged. For defending choices later.'],
    ['5 · “Who owes what”', 'Every unanswered question + “X owes Y: [thing]”, latest state only. For preparing your reply.'],
  ];
  shapes.forEach((r, i) => {
    const y = 1.62 + i * 0.86;
    H.card(s, 0.55, y, 6.0, 0.76, i === 1 ? C.TEAL_TINT : C.PANEL);
    s.addText([
      { text: r[0] + ' — ', options: { bold: true, color: C.TEAL_DARK, fontSize: 10.8 } },
      { text: r[1], options: { color: C.SLATE, fontSize: 9.4 } },
    ], { x: 0.82, y: y + 0.06, w: 5.5, h: 0.64, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.02 });
  });
  s.addShape('roundRect', { x: 6.75, y: 1.62, w: 6.0, h: 0.42, rectRadius: 0.07, fill: { color: C.TEAL }, line: { type: 'none' } });
  s.addText('THE PROMPT · the structured brief (shape 2)', { x: 6.95, y: 1.65, w: 5.6, h: 0.36, fontFace: F.body, fontSize: 10.5, bold: true, color: 'FFFFFF', margin: 0, valign: 'middle' });
  H.card(s, 6.75, 2.1, 6.0, 2.62, 'FFFFFF', C.LINE);
  s.addText('Summarize the email thread below under four headers, in order: 1) OVERVIEW — two sentences. 2) DECISIONS — bullets; write “None” if nothing was decided. 3) ACTION ITEMS — task — owner — due date; leave a slot blank rather than guess. 4) OPEN QUESTIONS — raised but never answered. Rules: use only facts in the thread · work oldest-first and flag anywhere a decision or date CHANGED later — show both, mark the latest · do not invent owners or dates. Thread: [paste, oldest first]', { x: 6.95, y: 2.22, w: 5.6, h: 2.4, fontFace: 'Consolas', fontSize: 8.9, color: C.TEAL_DARK, margin: 0, lineSpacingMultiple: 1.12 });
  H.card(s, 6.75, 4.9, 6.0, 1.68, C.AMBER_TINT);
  s.addText([
    { text: 'Your practice thread (in the pack): ', options: { bold: true, color: C.AMBER, fontSize: 11, breakLine: true, paraSpaceAfter: 3 } },
    { text: '“Q3 packaging change” — 10 messages, 6 people, and four planted traps: a date that MOVED mid-thread, an approval WITH a condition, a question nobody answered, and a mentioned attachment that isn’t there. A good brief catches all four.', options: { color: C.SLATE, fontSize: 10.2 } },
  ], { x: 6.98, y: 5.06, w: 5.55, h: 1.42, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.08 });
  s.addText('Why this play: thread summarization is the single most-used Copilot feature — and the easiest to trust blindly. ✂ All five shape prompts: tab EX-Email of your Course Workbook.', { x: 0.55, y: 6.1, w: 6.0, h: 0.8, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 1.05 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “the other daily play — the inbox. There isn’t ONE way to summarize a thread; there are five shapes, and picking the shape is the skill.”\n' +
    '2) Walk the five shape cards, one line each; the highlighted one — the structured brief — is the default.\n' +
    '3) Read the prompt aloud, slowly on the three rules — only facts in the thread · oldest-first, flag what CHANGED, show both values · never invent owners or dates. Those three rules are what separate this from clicking “summarize.”\n' +
    '4) Amber card: the practice thread and its four traps — run it live next slide.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Now the same play inside Copilot — buttons, limits, and the full sequence.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'TL;DR = too long; didn’t read — the one-line summary.\n' +
    '\n' +
    'CONTENT —\n' +
    'The five shapes + rules are synthesized from the 2026 practitioner literature (verbatim sources and popularity signals in notes/research/r16_email_summarization.md): AIEmaily’s prompt library (Jun 2026), Mailbird’s 2026 guide, Missive (Mar 2026), Microsoft MVP guides (van der Schyff Jan 2026, m365.fm Apr 2026), Jace template (Jan 2026).\n' +
    'Practice-thread answer key: pilot start MOVED Sep 22 → Oct 6 (Maya’s Sep 14 message — latest wins); Dan approved WITH an 18k cap (a qualifier that must survive summarization); Sofia’s customer-notification question is never answered; drop_test_v2.xlsx is referenced, not attached; Jonas’s pretzel line is noise a good brief drops.');

  // ---------- 41. WALKTHROUGH 2 · EMAIL IN COPILOT — MOCKUP + SEQUENCE ----------
  s = H.slide('PART 4 · WALKTHROUGH 2 · EMAIL', 41);
  H.title(s, 'Walkthrough · the inbox play, in Copilot', 'The button starts it — the prompts finish it');
  // — stylized Outlook strip (illustration, not a screenshot) —
  const panels = [
    ['① The thread, in Outlook', 'A'],
    ['② “Summary by Copilot” — with citations', 'B'],
    ['③ The Copilot pane — where you refine', 'C'],
  ];
  panels.forEach((p, i) => {
    const x = 0.55 + i * 4.15;
    s.addShape('roundRect', { x, y: 1.58, w: 3.95, h: 1.5, rectRadius: 0.05, fill: { color: 'FFFFFF' }, line: { color: C.SLATE, width: 1 } });
    s.addShape('roundRect', { x, y: 1.58, w: 3.95, h: 0.3, rectRadius: 0.05, fill: { color: i === 1 ? C.TEAL : C.SLATE }, line: { type: 'none' } });
    s.addText(p[0], { x: x + 0.12, y: 1.58, w: 3.75, h: 0.3, fontFace: F.body, fontSize: 8.5, bold: true, color: 'FFFFFF', margin: 0, valign: 'middle' });
    if (p[1] === 'A') {
      s.addText('Q3 packaging change', { x: x + 0.15, y: 1.94, w: 3.6, h: 0.24, fontFace: F.body, fontSize: 9, bold: true, color: C.INK, margin: 0 });
      [0, 1, 2].forEach(r => {
        s.addShape('ellipse', { x: x + 0.17, y: 2.24 + r * 0.26, w: 0.16, h: 0.16, fill: { color: [C.TEAL, C.AMBER, C.SLATE][r] }, line: { type: 'none' } });
        s.addShape('roundRect', { x: x + 0.42, y: 2.27 + r * 0.26, w: 2.4 - r * 0.4, h: 0.1, rectRadius: 0.03, fill: { color: C.LINE }, line: { type: 'none' } });
      });
      s.addText('10 messages · 6 people', { x: x + 0.15, y: 2.82, w: 3.6, h: 0.22, fontFace: F.body, fontSize: 7.5, italic: true, color: C.MUTE, margin: 0 });
    } else if (p[1] === 'B') {
      [0, 1, 2].forEach(r => {
        s.addShape('roundRect', { x: x + 0.17, y: 2.02 + r * 0.3, w: 2.9 - r * 0.5, h: 0.11, rectRadius: 0.03, fill: { color: C.LINE }, line: { type: 'none' } });
        s.addShape('roundRect', { x: x + 3.12 - r * 0.5, y: 1.99 + r * 0.3, w: 0.22, h: 0.17, rectRadius: 0.03, fill: { color: C.TEAL }, line: { type: 'none' } });
        s.addText(String(r + 1), { x: x + 3.12 - r * 0.5, y: 1.97 + r * 0.3, w: 0.22, h: 0.19, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 7, bold: true, color: 'FFFFFF', margin: 0 });
      });
      s.addText('each number is a click-through citation — your verification tool', { x: x + 0.15, y: 2.78, w: 3.65, h: 0.28, fontFace: F.body, fontSize: 7.5, italic: true, color: C.TEAL_DARK, margin: 0 });
    } else {
      s.addShape('roundRect', { x: x + 0.15, y: 1.98, w: 3.65, h: 0.4, rectRadius: 0.06, fill: { color: 'FFFFFF' }, line: { color: C.TEAL, width: 1 } });
      s.addText('“Who owes the next reply, and by when?”', { x: x + 0.25, y: 2.0, w: 3.45, h: 0.36, fontFace: 'Consolas', fontSize: 7.6, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
      s.addText('“List the action items” · “What did you base that on?”', { x: x + 0.15, y: 2.48, w: 3.65, h: 0.5, fontFace: 'Consolas', fontSize: 7.2, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.1 });
    }
  });
  s.addText('stylized illustration — not a screenshot', { x: 9.4, y: 3.1, w: 3.35, h: 0.22, align: 'right', fontFace: F.body, fontSize: 7.5, italic: true, color: C.MUTE, margin: 0 });
  H.card(s, 0.55, 3.42, 5.9, 1.95, C.PANEL);
  s.addText('Mechanics worth knowing', { x: 0.85, y: 3.55, w: 5.3, h: 0.32, fontFace: F.head, fontSize: 12.5, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.9, 3.92, 5.3, 1.4, [
    { t: 'The summary’s numbered citations jump to the source email — verify names and dates through them.', b: true },
    { t: 'Limits: attachments NOT read (use “Summarize a file”) · shared mailboxes & encrypted mail out of scope · very short threads produce nothing.' },
    { t: 'Microsoft’s own anatomy = ours: Goal · Context · Source · Expectations.' },
  ], { size: 8.8, gap: 4 });
  H.callout(s, 0.55, 5.5, 5.9, 1.5, C.RED_TINT, [
    { text: 'Where naive “summarize this” fails: ', options: { bold: true, color: C.RED, fontSize: 10, breakLine: true } },
    { text: 'the FIRST date, not the moved one · qualifiers dropped (“approved with a cap” → “approved”) · invented owners for “I’ll look into it.” Our prompt’s rules exist because of these three failures.', options: { color: C.SLATE, fontSize: 9.4 } },
  ], { iconName: 'alert', iconFill: C.RED, size: 10 });
  const eseq = [
    ['STEP 1 · The brief', 'Run the structured brief from the last slide on the practice thread (paste it, or run it on the thread in Copilot). Check it caught: the moved date, the 18k condition, the unanswered question, the missing attachment.'],
    ['STEP 2 · Reply prep', 'From the thread: List A — every question raised that was never answered. List B — WHO OWES WHAT: “X owes Y: [thing] by [date]”, latest state only. Blank beats guessed.'],
    ['STEP 3 · The reply', 'Using the brief above, draft my reply: answer the open questions, confirm the decisions with their conditions, propose next steps. Do not invent commitments — leave a [bracket] where I must decide. Under 120 words, one clear next step at the end.'],
  ];
  eseq.forEach((st, i) => {
    const y = 3.42 + i * 1.16;
    s.addShape('roundRect', { x: 6.6, y, w: 6.15, h: 0.34, rectRadius: 0.06, fill: { color: C.TEAL }, line: { type: 'none' } });
    s.addText(st[0], { x: 6.78, y: y + 0.01, w: 5.8, h: 0.32, fontFace: F.body, fontSize: 9.5, bold: true, color: 'FFFFFF', margin: 0, valign: 'middle' });
    H.card(s, 6.6, y + 0.36, 6.15, 0.72, 'FFFFFF', C.LINE);
    s.addText(st[1], { x: 6.78, y: y + 0.4, w: 5.8, h: 0.64, fontFace: 'Consolas', fontSize: 7.5, color: C.TEAL_DARK, margin: 0, lineSpacingMultiple: 0.98 });
  });
  s.addText('Same prompts in any assistant — Copilot adds the citations and the tenant boundary (Part 2: green tier). ✂ Steps 1–3: tab EX-Email of your Course Workbook.', { x: 6.6, y: 6.88, w: 6.15, h: 0.28, fontFace: F.body, fontSize: 8, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) TOP strip — walk the three panels left to right like a comic: ① the thread as Outlook shows it (10 messages, 6 people) → ② the “Summary by Copilot” button output, where every numbered chip is a CLICK-THROUGH citation back to the source email → ③ the Copilot pane, where the real work happens with your refine prompts. Say once: stylized illustration, not a screenshot — buttons move; the flow doesn’t.\n' +
    '2) LEFT mechanics card: citations are the verification tool; know the three limits (attachments, shared mailboxes, encrypted mail). And the anatomy echo: Microsoft’s Goal-Context-Source-Expectations IS our Role-Task-Context-Format wearing a trench coat.\n' +
    '3) RIGHT: run the three steps on the practice thread, live if possible. Step 1’s reveal: did it catch the Oct 6 date (not Sep 22), the 18k CONDITION on Dan’s approval, Sofia’s unanswered question, the phantom attachment?\n' +
    '4) Red card: the three classic failures, and why our prompt’s rules exist. If the room’s Copilot summary missed a trap — that’s the lesson, not a malfunction.\n' +
    '5) Footer: green-tier reminder — thread summarization belongs in the tenant, not a personal chatbot; steps 1–3 are copy-paste ready in tab EX-Email.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Two plays end to end. Here’s the menu of what we could drill next.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'GCSE (Microsoft’s) = Goal, Context, Source, Expectations — its recommended prompt structure.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: stylized 3-panel Outlook strip added (owner: pictures + do-from-Outlook); drawn in house style and labeled as illustration — no real UI screenshots, so nothing goes stale or misrepresents a tenant.\n' +
    'Copilot mechanics verified against Microsoft Support pages Sep 2026 (r16): thread summary + numbered citations; refine-in-pane prompts (Bowdoin KB examples); attachments not read by default (“Summarize a file” added Jun 2025); primary-mailbox-only scope; encrypted/IRM excluded; ~1,000-character minimum (documented for Copilot for Sales, widely reported for Outlook).\n' +
    'Advanced variants for questions (r16): scheduled daily triage (“Summarize emails from the past day that haven’t received a reply; rank importance 1–5; draft replies for 3+”) · cross-channel reconcile table (Mail/Teams/Channel | Topic | Summary | Action | Follow-up) · chunk-and-merge sequence for 30+ message threads (carry running decisions/questions forward; reconcile conflicts to the latest value, and say so).');

  // ---------- 42. FUTURE PLAYS MENU (closes Block 2) ----------
  s = H.slide('PART 4 · WHAT NEXT', 42);
  H.title(s, 'More plays we can drill next', 'Pick what we drill next — the method transfers');
  const plays = [
    ['file', 'Document interpretation & Q&A', 'Upload a contract, spec, or standard; ask clause-level questions with page-cited answers and an “it doesn’t say” rule.'],
    ['image', 'Image creation for work', 'Decks, one-pagers, training visuals — the commercially-safe lane (Firefly) vs the built-in chatbot lane, and prompt patterns for each.'],
    ['inbox', 'Inbox triage & scheduled digests', 'Beyond one thread: “summarize unanswered emails from the past day, rank 1–5, draft replies for the top ones” — on a schedule.'],
    ['mic', 'Meetings → minutes & actions', 'Transcript in; decisions, actions with owners, and a circulated summary out — same shapes as the email play.'],
    ['translate', 'Translation & tone shifts', 'Regulated-grade translation and audience rewrites: same content, five audiences, five registers.'],
    ['robot', 'Recurring data pipelines', 'This block’s data play, delegated end-to-end to an agent on a schedule — that is exactly Part 5.'],
  ];
  plays.forEach((p, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.62 + Math.floor(i / 2) * 1.5;
    H.card(s, x, y, 5.95, 1.38, C.PANEL);
    H.iconCircle(s, x + 0.2, y + 0.24, 0.46, p[0], C.TEAL);
    s.addText([
      { text: p[1], options: { bold: true, color: C.INK, fontSize: 12, breakLine: true, paraSpaceAfter: 3 } },
      { text: p[2], options: { color: C.SLATE, fontSize: 9.8 } },
    ], { x: x + 0.8, y: y + 0.1, w: 5.0, h: 1.2, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.04 });
  });
  H.callout(s, 0.55, 6.3, 12.2, 0.65, C.TEAL_TINT, [
    { text: 'Your vote decides: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5 } },
    { text: 'the next session drills the two plays this room wants most — tell me on the way out, or in the follow-up note.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'thumbsup', iconFill: C.TEAL, size: 11.5 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “every play you just saw followed one method — real file, profile first, numbered asks, verify before shipping. That method transfers; here’s the menu.”\n' +
    '2) Sweep the six cards, one line each; land on the last card — recurring pipelines — as the bridge to Part 5: “that one isn’t a future topic; it’s the next part.”\n' +
    '3) Teal band: collect votes — genuinely. The menu is real backlog, not decoration.\n' +
    '4) CLOSE BLOCK 2 from here (the old pointer slide is gone — say it, don’t slide it): name the handout pack piece by piece — prompt-library/ (all 13 templates with filled examples and pitfalls) · the Course Workbook (every exercise prompt in a named tab, the practice data, the PLAYBOOK tab) · the quotations + email-thread files · the Template Creator + Configurator · the cheat sheet, ELEMENTS guide, and Taxonomy Reference. Then the homework: run the HANDOFF move (Prompt 4/8, step 2) on your course log tonight — next block opens with it.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“The playbook so far asks the AI to answer. Part 5 asks it to WORK.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none new on this slide.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: this slide now closes Block 2 — the separate playbook-pointer slide was cut (owner: not needed); its handout-pack rundown lives in step 4 above. The eight G-template one-liners, if asked: G1 raw material in, hard word cap, “add no facts” · G2 exact columns, code-not-vibes, reconcile, stop · G3 anchored rubric, quotes as evidence · G4 README tab, formulas not values · G5 titles state findings; approve text before rendering · G6 single file, offline, auditable · G7 a question not a topic; links + dates; demand the gaps · G8 summaries serve a decision; verbatim quotes for anything load-bearing.\n' +
    'v1.5 (owner request): the future-plays menu. Image-creation lane facts are in r12 (Firefly indemnification); triage/digest prompts in r16; document-Q&A is G7/G8 grown teeth; the meetings play reuses the email shapes.\n' +
    'If a vote happens, log the winners in PROJECT_STATE for the next content cycle.');
};
