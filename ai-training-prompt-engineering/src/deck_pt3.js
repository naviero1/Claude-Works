// PART 3 (Prompt engineering) + PART 4 (Applied playbook)
const { C, F } = require('./deck_lib');

module.exports = function buildPartThree(pres, H) {
  // ---------- 21. PART 3 DIVIDER ----------
  let s = H.slide(null, 21, { dark: true });
  H.partMarker(s, 3);
  s.addText('PART 3 · PROMPT ENGINEERING', { x: 0.55, y: 2.3, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('The craft: getting what\nyou actually meant', { x: 0.55, y: 2.8, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('Every AI vendor publishes prompting guidance. It converges on one anatomy and a handful of techniques — this part teaches them, with the evidence for what works and what’s myth.', { x: 0.55, y: 4.85, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes(
    'HOW TO PRESENT — 1) Progress bar: part 3 — the core craft part; if the room remembers one part, make it this one. 2) One framing sentence: “Every vendor publishes prompting guidance, and it converges — we teach the convergence, with the evidence.” 3) Under 30 seconds, advance.\n' +
    'ACRONYMS — none on this slide.');

  // ---------- 22. THE ANATOMY, SHOWN (v1.3 — replaces the vendor-comparison table) ----------
  s = H.slide('PART 3 · THE ANATOMY', 22);
  H.title(s, 'The universal anatomy', 'One prompt, five parts — this is what good looks like');
  const anatEx = [
    ['ROLE', '“You are a precise editor. You add no facts that are not in the source.”'],
    ['TASK', '“Summarize the attached Q2 returns report for the operations lead.”'],
    ['CONTEXT', '“Return rate = returns ÷ units shipped. The export has a totals row — exclude it.”'],
    ['FORMAT', '“≤ 150 words: the headline number first, then three bullets; caveats last.”'],
    ['EXAMPLES', '<example> March’s summary — the one the team liked </example> + one edge case.'],
  ];
  anatEx.forEach((r, i) => {
    const y = 1.62 + i * 0.98;
    H.card(s, 0.55, y, 7.85, 0.88, i % 2 ? 'FFFFFF' : C.PANEL, i % 2 ? C.LINE : null);
    s.addShape('roundRect', { x: 0.78, y: y + 0.22, w: 1.35, h: 0.44, rectRadius: 0.07, fill: { color: C.TEAL }, line: { type: 'none' } });
    s.addText(r[0], { x: 0.78, y: y + 0.23, w: 1.35, h: 0.42, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 10.5, bold: true, charSpacing: 1, color: 'FFFFFF', margin: 0 });
    s.addText(r[1], { x: 2.32, y: y + 0.08, w: 5.85, h: 0.72, fontFace: 'Consolas', fontSize: 10.5, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 1.05 });
  });
  H.card(s, 8.65, 1.62, 4.1, 4.86, C.PANEL);
  s.addText('Same recipe, every vendor', { x: 8.9, y: 1.84, w: 3.6, h: 0.4, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  const vend = [
    ['Anthropic', 'role · clear, direct task · context · format · examples'],
    ['OpenAI', 'role & instructions · context · format · few-shot if needed'],
    ['Google', 'Persona · Task · Context · Format'],
    ['Microsoft', 'Goal · Context · Source · Expectations'],
  ];
  vend.forEach((v, i) => {
    const y = 2.35 + i * 0.82;
    s.addText(v[0], { x: 8.9, y, w: 3.6, h: 0.3, fontFace: F.body, fontSize: 11, bold: true, color: C.TEAL_DARK, margin: 0 });
    s.addText(v[1], { x: 8.9, y: y + 0.28, w: 3.6, h: 0.45, fontFace: F.body, fontSize: 9.3, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.0 });
  });
  s.addText('Four official prompting guides, one anatomy — the names differ; the recipe doesn’t.', { x: 8.9, y: 5.72, w: 3.6, h: 0.65, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 1.08 });
  H.callout(s, 0.55, 6.62, 12.2, 0.5, C.TEAL_TINT, [
    { text: 'Google’s data point: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 10.5 } },
    { text: 'the most fruitful prompts averaged ~21 words with context — most people type fewer than nine. A good prompt is a short briefing, not a search query.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'edit', iconFill: C.TEAL, size: 10.5 });
  s.addNotes(
    'HOW TO PRESENT — 1) Frame: “this is the whole anatomy — one prompt, five labeled parts. Everything in Part 3 is refinements of this picture.” 2) Read the example TOP TO BOTTOM as one continuous prompt, pausing at each tag: role sets the behavior, task names the job and the audience, context supplies what it can’t know, format is the contract, examples show the standard. 3) Point out it’s ~70 words — “this is what ‘a short briefing’ means; it took under a minute to write.” 4) Right card, fast: four official vendor guides teach this same recipe under different names — “this is not our opinion; it’s convergence.” 5) Teal band: ~21 words vs the nine people type. 6) Bridge: “now each part properly — starting with the three that carry the meaning.”\n' +
    'ACRONYMS — Q2 = second quarter. XML-style tags = the angle-bracket fences around examples.\n' +
    'CONTENT — v1.3: replaces the vendor-comparison table (owner feedback: the table proved convergence but taught nothing — the example teaches). Vendor detail if asked: Anthropic “give Claude a role” + “be clear and direct” + XML tags; OpenAI role/developer message + “simple and direct” instructions; Google Persona-Task-Context-Format; Microsoft Goal-Context-Source-Expectations (Goal is the only required part). The 21-words stat: Google’s Oct 2024 Workspace guide (dropped in the newer edition — directional, not gospel). Anthropic’s golden rule belongs in the room: show the prompt to a colleague with minimal context — if they’d be confused, the model will be too. Continuity hook: the internal crash course’s “5 building blocks” and CRISP checklist, and Phoenix & Taylor’s Five Principles — one anatomy, many aliases.');

  // ---------- E1a. THE ELEMENTS, DEFINED — 1 of 2 (v1.3 split) ----------
  s = H.slide('PART 3 · THE ELEMENTS', 23);
  H.title(s, 'The elements, defined · 1 of 2', 'Role · Task · Context — the parts that carry the meaning');
  const edefsA = [
    ['Role', 'who is answering — behaviors, not titles',
      'Behavioral commitments are auditable in the output; a title is a vibe the model can fake.',
      'wrong altitude or posture; confident authority with nothing behind it',
      '“You are a senior analyst.”',
      '“You never invent numbers; you state n; you say what the data can’t answer.”'],
    ['Task', 'verb + object + audience + success criterion',
      'A precise question carries its own completion test — the model knows when it is done.',
      'a fluent answer to a vaguer question than the one you had',
      '“Analyze the returns data.”',
      '“What is the return rate by site for Q2, vs the 2% target?”'],
    ['Context', 'what the model cannot know on its own',
      'The model fills every gap with the most plausible guess — context replaces guessing with your facts.',
      'generically right, specifically wrong for us',
      '“Use our standard definitions.”',
      '“Return rate = returns ÷ shipped. Quirk: the export has a totals row — exclude it and say so.”'],
  ];
  const drawElement = (r, y, h) => {
    H.card(s, 0.55, y, 12.2, h, C.PANEL);
    s.addText(r[0], { x: 0.82, y: y + 0.12, w: 1.85, h: 0.42, fontFace: F.head, fontSize: 17, bold: true, color: C.TEAL_DARK, margin: 0 });
    s.addText(r[1], { x: 0.82, y: y + 0.55, w: 1.85, h: h - 0.7, fontFace: F.body, fontSize: 9.6, color: C.INK, margin: 0, lineSpacingMultiple: 1.05 });
    s.addText([
      { text: 'Why it works — ', options: { bold: true, color: C.INK, fontSize: 10.2 } },
      { text: r[2], options: { color: C.SLATE, fontSize: 10.2, breakLine: true, paraSpaceAfter: 5 } },
      { text: 'Prevents — ', options: { bold: true, color: C.RED, fontSize: 10.2 } },
      { text: r[3], options: { color: C.SLATE, fontSize: 10.2 } },
    ], { x: 2.85, y: y + 0.12, w: 4.35, h: h - 0.24, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.08 });
    s.addText([
      { text: 'weak   ', options: { bold: true, color: C.RED, fontSize: 9.5 } },
      { text: r[4], options: { color: C.SLATE, fontSize: 10, italic: true, breakLine: true, paraSpaceAfter: 5 } },
      { text: 'strong ', options: { bold: true, color: C.GREEN, fontSize: 9.5 } },
      { text: r[5], options: { color: C.INK, fontSize: 10, italic: true } },
    ], { x: 7.45, y: y + 0.12, w: 5.05, h: h - 0.24, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.08 });
  };
  edefsA.forEach((r, i) => drawElement(r, 1.62 + i * 1.72, 1.58));
  s.addText('Read each pair aloud — the weak→strong contrast is the lesson. Format and Examples are next.', { x: 0.55, y: 6.85, w: 12.2, h: 0.3, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT — 1) Frame: “now each element properly — its job, why it works, and the failure it prevents. First the three that carry the meaning.” 2) One CARD at a time, same rhythm each: say the element name and its job (left) → read the weak fill aloud, flat → read the strong fill aloud — let the contrast land → then the “why it works” line. 3) Role: land “behaviors are auditable; a title is a vibe the model can fake.” 4) Task: land “a precise question knows when it’s done.” 5) Context: land “context replaces guessing with your facts.” 6) Bridge: “two to go — the contract, and the standard.”\n' +
    'ACRONYMS — n = sample size (“you state n”). Q2 = second quarter.\n' +
    'CONTENT — v1.3: the single dense five-row table split into two explanatory slides (owner feedback). Each card now carries the mechanism and the failure on-slide — previously notes-only. The full field guide per element (evidence, pitfalls) remains the ELEMENTS handout; the option menus per element are the Taxonomy Reference.');

  // ---------- E1b. THE ELEMENTS, DEFINED — 2 of 2 (v1.3 split) ----------
  s = H.slide('PART 3 · THE ELEMENTS', 24);
  H.title(s, 'The elements, defined · 2 of 2', 'Format · Examples — the contract, and the standard');
  const edefsB = [
    ['Format', 'the output contract — shape, cap, tone',
      'A numeric cap is enforceable; “short and professional” is a mood the model interprets freely.',
      'the right content in an unusable shape or length',
      '“Keep it short and professional.”',
      '“≤ 120 words: the ask in sentence one, two facts with numbers, the deadline.”'],
    ['Examples', '3–5 diverse demonstrations, edge case included',
      'The model imitates what it sees — including exactly how your examples handle the hard cases.',
      'output that misses the standard in your head — the one you never wrote down',
      'three clones of the happy case',
      'one typical + one edge + one reject case, fenced in tags'],
  ];
  edefsB.forEach((r, i) => drawElement(r, 1.62 + i * 1.86, 1.7));
  H.callout(s, 0.55, 5.5, 12.2, 1.0, C.TEAL_TINT, [
    { text: 'The pattern behind all five: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12.5 } },
    { text: 'each element moves something out of your head onto the page. When output disappoints, one of the five was left in your head — the diagnosis grid on the next slide names which.', options: { color: C.SLATE, fontSize: 12.5 } },
  ], { iconName: 'compass', iconFill: C.TEAL, size: 12.5 });
  s.addText('The full field guide — mechanism, evidence, and pitfalls per element — is in your handout (ELEMENTS guide).', { x: 0.55, y: 6.72, w: 12.2, h: 0.3, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT — 1) Same rhythm as the previous slide, two cards: name and job → weak aloud → strong aloud → the why. 2) Format: land “a numeric cap is enforceable; an adjective is a mood.” 3) Examples: land “the model handles edge cases exactly the way your examples do — so include one.” 4) Teal band — the unifying idea, read it in full: every element moves something out of your head onto the page; when output disappoints, one of the five stayed in your head. 5) Footer: full field guide = ELEMENTS handout. 6) Bridge: “two one-sentence safety valves complete the kit.”\n' +
    'ACRONYMS — none new on this slide.\n' +
    'CONTENT — v1.3 split, second half. The “pattern” line is the bridge into the diagnosis grid and, later, the taxonomy slide (the catalog of what can fill each slot). If short on time: read only the weak→strong pairs and the teal band.');

  // ---------- E2. SAFETY VALVES + DIAGNOSIS GRID (v1.1) ----------
  s = H.slide('PART 3 · THE ELEMENTS', 24);
  H.title(s, 'Two safety valves — and the diagnosis grid', 'One sentence each; they shut off the two signature failures');
  H.card(s, 0.55, 1.65, 5.9, 2.35, C.TEAL_TINT);
  H.iconCircle(s, 0.85, 1.9, 0.5, 'help', C.TEAL);
  s.addText('THE OUT — permission to not know', { x: 1.5, y: 1.95, w: 4.8, h: 0.4, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
  s.addText('“If the document doesn’t say — say so.” Models are trained on tests that reward guessing over abstaining; the Out re-opens the abstain option and drastically cuts invented answers.', { x: 0.9, y: 2.45, w: 5.3, h: 1.4, fontFace: F.body, fontSize: 11.5, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.12 });
  H.card(s, 0.55, 4.25, 5.9, 2.35, C.TEAL_TINT);
  H.iconCircle(s, 0.85, 4.5, 0.5, 'hand', C.TEAL);
  s.addText('THE STOP — the scope boundary', { x: 1.5, y: 4.55, w: 4.8, h: 0.4, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
  s.addText('“Answer these three questions, then stop — do not go exploring.” Converts open-ended capability into bounded work. In Part 5 it grows up to become gates and autonomy rules.', { x: 0.9, y: 5.05, w: 5.3, h: 1.4, fontFace: F.body, fontSize: 11.5, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.12 });
  H.card(s, 6.75, 1.65, 6.0, 4.95, C.PANEL);
  s.addText('The diagnosis grid — which element failed?', { x: 7.02, y: 1.86, w: 5.5, h: 0.4, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
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
    const y = 2.4 + i * 0.58;
    s.addText(g[0], { x: 7.05, y, w: 3.7, h: 0.5, fontFace: F.body, fontSize: 10.3, color: C.SLATE, margin: 0, valign: 'middle' });
    s.addText(g[1], { x: 10.85, y, w: 1.75, h: 0.5, fontFace: F.body, fontSize: 10.3, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    if (i < 6) s.addShape('line', { x: 7.05, y: y + 0.53, w: 5.45, h: 0, line: { color: C.LINE, width: 0.5 } });
  });
  s.addNotes(
    'HOW TO PRESENT — 1) LEFT top card: THE OUT — read the quoted sentence, then the why: models are trained on tests that reward guessing; the Out re-opens the abstain option. 2) LEFT bottom: THE STOP — read the quote; it converts open-ended capability into bounded work, and in Part 5 it grows into gates and autonomy rules. 3) RIGHT grid: the diagnosis table — say the habit: “when output disappoints, don’t reword at random — name the failed element, fix that one.” Walk two rows as examples (wrong altitude → Role; confidently invented → the Out was missing). 4) Bridge: “everything you just met — five elements, two valves — has a full catalog behind it. Next slide is your field map.”\n' +
    'ACRONYMS — none on this slide.\n' +
    'CONTENT — v1.1 addition. The grid is the practical payoff of the element model — it turns iteration from retyping into diagnosis. Same grid opens the ELEMENTS handout.');

  // ---------- E3. THE TAXONOMY HANDOUT (new in v1.2) ----------
  s = H.slide('PART 3 · YOUR FIELD MAP', 25);
  H.title(s, 'Your field map · a handout you keep', 'The Prompt Element Taxonomy — every choice, cataloged');
  H.bullets(s, 0.55, 1.68, 6.15, 2.9, [
    { t: 'A parts catalog for prompts: every element you just met, broken into its attributes — the slots you fill — and vetted options — proven ways to fill them.', b: true },
    { t: 'Two wings: the seven generative elements (Role → Examples, plus the Out and the Stop) and the twelve agentic blocks of Part 5’s mission brief.' },
    { t: 'One source of truth, three doors: this printed reference, the interactive Template Creator (HTML), and a spreadsheet Configurator.' },
    { t: 'Use it at the moment of doubt: the diagnosis grid names the failed element — the taxonomy shows the menu of stronger fills.' },
  ], { size: 12, gap: 8 });
  // "How to read one entry" — element → attribute → option, drawn
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
  s.addText('OPTIONS — every option ships with when-to-use guidance: you pick from a vetted menu instead of composing from scratch.', { x: 7.3, y: 3.78, w: 5.2, h: 0.65, fontFace: F.body, fontSize: 9.8, italic: true, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.08 });
  // the numbers + where it lives
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
    'HOW TO PRESENT — 1) Hold up the physical handout (or show the PDF) and name it: “the Prompt Element Taxonomy — your field map; everyone gets one.” 2) Say what it IS in one breath: “everything we just did — elements, their slots, and proven ways to fill them — cataloged, with when-to-use guidance on every option.” 3) LEFT bullets top to bottom: parts catalog → two wings (generative now, agentic in Part 5) → one source of truth, three doors (reference, Creator, Configurator). 4) RIGHT card: walk the tree ONCE — element Role → attribute identity → options “Careful analyst” / “Precise editor” — “you pick from a vetted menu instead of composing from scratch.” 5) Bottom band: sweep the four numbers (19 elements · 78 attributes · ~290 options · 18 presets), then the pack. 6) Set the expectation: “you don’t study this — you look things up in it, like a catalog.” 7) Bridge: “with the map in hand — seven techniques that cover almost everything.”\n' +
    'ACRONYMS — HTML = HyperText Markup Language — the Template Creator is a single web-page file that runs offline. XLSX = Excel spreadsheet format (the Configurator). PDF = Portable Document Format (this printed reference).\n' +
    'CONTENT — New in v1.2 (owner request): the taxonomy formally introduced as a side handout. Source of truth is prompt-library/taxonomy/*.json — 19 elements, 78 attributes (counting nested sub-slots, as the tools do), 286 options, 18 presets, regenerated into all three tools; never hand-edit the deliverables. The structure borrows from object-oriented software: element = class, attribute = property, option = allowed value, template = saved instance, and agentic elements inherit from generative ones (Mission extends Task). Distribution: print the reference for the room or send the PDF link with the deck; the Creator and Configurator go out as files with the handout pack.');
  s = H.slide('PART 3 · TECHNIQUES', 23);
  H.title(s, 'The toolkit', 'Seven techniques cover almost everything');
  const tech = [
    ['edit', '1 · Be specific — and say why', 'Name the audience, length, constraints. Explaining the reason behind a rule (“this will be read aloud, so no ellipses”) measurably improves compliance.'],
    ['copy', '2 · Show 3–5 examples', 'The most reliable way to control format, tone, and structure. Make them diverse and realistic — the model imitates what it sees.'],
    ['layers', '3 · Structure with tags', 'Separate instructions / context / input with XML tags or headers. Unambiguous parsing; survives copy-paste into any tool.'],
    ['help', '4 · Give it an out', '“If the document doesn’t say, say so.” Permission to admit uncertainty drastically cuts invented answers.'],
    ['branch', '5 · Chain the work', 'Big job → sequential prompts: draft → review against criteria → refine. You get inspectable intermediates — an audit trail.'],
    ['eye', '6 · Self-check against criteria', '“Before finishing, verify against [checklist].” Works when criteria are concrete; “are you sure?” alone doesn’t.'],
    ['zap', '7 · Metaprompting', 'Ask the model to improve your prompt: “What should I add or delete to get X more consistently?” Official practice at OpenAI, Anthropic, and Google.'],
  ];
  tech.forEach((t, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.62 + Math.floor(i / 2) * 1.28;
    H.card(s, x, y, 5.95, 1.16, C.PANEL);
    H.iconCircle(s, x + 0.18, y + 0.31, 0.5, t[0], C.TEAL);
    s.addText([
      { text: t[1], options: { bold: true, color: C.INK, fontSize: 12, breakLine: true, paraSpaceAfter: 2 } },
      { text: t[2], options: { color: C.SLATE, fontSize: 9.8 } },
    ], { x: x + 0.82, y: y + 0.07, w: 5.0, h: 1.02, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.03 });
  });
  H.callout(s, 6.75, 5.5, 6.0, 1.15, C.AMBER_TINT, [
    { text: 'Where’s “think step by step”? ', options: { bold: true, color: C.INK, fontSize: 11.5 } },
    { text: 'Retired to the bench — today’s models reason by default. The 2026 version comes two slides ahead.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'clock', iconFill: C.AMBER, size: 11.5 });
  s.addNotes(
    'HOW TO PRESENT — 1) Frame: “seven techniques cover almost everything — and you already met half of them.” 2) Walk the cards IN NUMBER ORDER 1→7, one line each: 1–4 are the anatomy applied (specific+why, examples, tags, the out); 5–7 are process moves (chain, self-check, metaprompting). 3) On 7, note it’s productized — every vendor now ships a prompt improver. 4) End on the amber card: “where’s think-step-by-step? Retired — two slides ahead explains why.” 5) Bridge: “which of these actually survive scrutiny? Evidence corner.”\n' +
    'ACRONYMS — XML = the angle-bracket tag style for structure (technique 3).\n' +
    'CONTENT — Each technique traces to vendor docs and research: examples = Brown et al. 2020 few-shot; the out = Anthropic hallucination guidance; chaining = Anthropic 2026 (“still useful when you need to inspect intermediate outputs”); self-check needs concrete criteria (self-correction research shows “are you sure?” can make answers worse). Metaprompting is now productized: OpenAI Prompt Optimizer, Anthropic prompt improver, Google “Make this a power prompt.”');

  // ---------- 24. EVIDENCE VS MYTH ----------
  s = H.slide('PART 3 · WHAT THE EVIDENCE SAYS', 24);
  H.title(s, 'Evidence corner', 'What works, what’s myth — and the bias to design against');
  H.card(s, 0.55, 1.65, 6.0, 2.6, C.GREEN_TINT);
  H.iconCircle(s, 0.85, 1.9, 0.5, 'check', C.GREEN);
  s.addText('Holds up', { x: 1.5, y: 1.95, w: 4.4, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.9, 2.5, 5.4, 1.7, [
    'Specificity, context, and examples — every vendor, every study',
    'Structure: tiny format changes swing accuracy by up to 76 points across phrasings — templates beat improvisation',
    'Personas shape tone and framing (what they’re for) …',
  ], { size: 11.5, gap: 6 });
  H.card(s, 0.55, 4.45, 6.0, 2.2, C.RED_TINT);
  H.iconCircle(s, 0.85, 4.68, 0.5, 'x', C.RED);
  s.addText('Doesn’t hold up', { x: 1.5, y: 4.72, w: 4.4, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.9, 5.25, 5.4, 1.3, [
    '… but “you are a genius” doesn’t improve factual accuracy (162-persona study: no gain)',
    'Tips, threats, politeness games: “even tipping a lavish $1000” didn’t change accuracy — small, unstable effects at best',
  ], { size: 11.5, gap: 6 });
  H.card(s, 6.75, 1.65, 6.0, 5.0, C.PANEL);
  s.addText('The bias to design against: sycophancy', { x: 7.05, y: 1.9, w: 5.4, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 7.1, 2.42, 5.4, 2.2, [
    { t: 'Across 11 leading models, AI affirmed users’ actions ~49% more often than humans do (Stanford/CMU, Science 2026)', b: true },
    { t: 'A single flattering exchange measurably raised users’ conviction they were right' },
    { t: 'Root cause: models are trained on human preferences — and we prefer agreement' },
  ], { size: 11.5, gap: 7 });
  H.callout(s, 7.05, 4.85, 5.4, 1.6, C.TEAL_TINT, [
    { text: 'The countermeasures: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5, breakLine: true } },
    { text: 'never reveal your preferred answer when asking for a review · ask for the case AGAINST (“three weakest points”) · paste your draft as “a colleague’s” · don’t treat “are you sure?” as verification.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'shield', iconFill: C.TEAL, size: 11 });
  s.addNotes(
    'HOW TO PRESENT — 1) Start LEFT with the green card — what holds up: specificity/context/examples everywhere; the 76-point format-brittleness swing (the case for templates); personas shape tone… 2) …and the red card finishes that sentence: “…but ‘you are a genius’ doesn’t improve accuracy” — neither do tips, threats, or politeness games. 3) RIGHT card, slow: sycophancy — the ~49% number, the conviction effect, the root cause (trained on our preferences; we prefer agreement). 4) Teal countermeasures: read all four; the first one — never reveal your preferred answer — changes behavior TODAY. 5) Bridge: “and 2026 retired some old advice — the update.”\n' +
    'ACRONYMS — CMU = Carnegie Mellon University (co-authors of the sycophancy study).\n' +
    'CONTENT — Sources worth naming aloud: format brittleness = Sclar et al. ICLR 2024 (up to 76-point swings from formatting alone — the case for tested, versioned templates; think gauge R&R for prompts). Personas = Zheng et al. EMNLP 2024. Tipping = Salinas & Morstatter, ACL 2024. Sycophancy = Cheng et al., Science 2026 (arXiv 2510.01395). The lesson isn’t “AI lies” — it’s “AI mirrors you”; blind it to your preference before asking for judgment.');

  // ---------- 25. PROMPTING THINKING MODELS ----------
  s = H.slide('PART 3 · THINKING MODELS', 25);
  H.title(s, 'The 2026 update', 'Prompting thinking models: less scaffolding, more clarity');
  const changed = [
    ['x', 'Retire: “think step by step”', 'Reasoning is built in. OpenAI: “avoid chain-of-thought prompts.” Anthropic: “think thoroughly” beats a hand-written step plan. Manual CoT is a fallback for non-thinking modes.'],
    ['x', 'Retire: piles of examples', 'Zero-shot first; add examples only if the format drifts. On some reasoning models few-shot measurably hurts (DeepSeek-R1’s own paper).'],
    ['alert', 'New risk: contradictions', 'Conflicting instructions are worse now — the model burns thinking tokens trying to reconcile them. Audit your prompt for rules that collide.'],
    ['sliders', 'New control: effort dials', 'Depth is set by parameters (thinking effort, verbosity), not magic words. Say how hard to think; don’t script how.'],
  ];
  changed.forEach((cd, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.65 + Math.floor(i / 2) * 1.62;
    H.card(s, x, y, 5.95, 1.48, C.PANEL);
    H.iconCircle(s, x + 0.2, y + 0.44, 0.52, cd[0], cd[0] === 'x' ? C.SLATE : C.AMBER);
    s.addText([
      { text: cd[1], options: { bold: true, color: C.INK, fontSize: 12.5, breakLine: true, paraSpaceAfter: 3 } },
      { text: cd[2], options: { color: C.SLATE, fontSize: 10.5 } },
    ], { x: x + 0.88, y: y + 0.1, w: 4.95, h: 1.3, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.05 });
  });
  H.callout(s, 0.55, 5.15, 12.2, 1.45, C.TEAL_TINT, [
    { text: 'What did NOT change: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 13, breakLine: true } },
    { text: 'clarity and specificity · relevant context and sources · output format · giving an out · grounding in documents · iteration. The anatomy from the top of this part applies to every model you will ever use — the scaffolding tricks retire, the briefing skills compound.', options: { color: C.SLATE, fontSize: 12.5 } },
  ], { iconName: 'check', iconFill: C.TEAL, size: 12.5 });
  s.addNotes(
    'HOW TO PRESENT — 1) Frame: “if you learned prompting from 2023 blog posts, this slide un-learns two things.” 2) TOP two cards: retire “think step by step” (reasoning is built in — the vendors say so themselves) and retire piles of examples (zero-shot first; few-shot can even hurt reasoning models). 3) BOTTOM two: the new risk — contradictions burn thinking tokens; and the new control — effort dials: say how HARD to think, not HOW to think. 4) Teal band: what did NOT change — read the list and land on: “the anatomy applies to every model you will ever use.” 5) Bridge: “the craft is stable — here’s the habit that compounds it.”\n' +
    'ACRONYMS — CoT = Chain-of-Thought — the old “think step by step” prompting style, now built into thinking models.\n' +
    'CONTENT — This slide inoculates against stale advice from 2023-era blog posts. Sources: OpenAI reasoning best practices (“avoid chain-of-thought prompts”, “try zero shot first”), Anthropic prompting best practices 2026 (“prefer general instructions over prescriptive steps”), GPT-5 guide (contradiction cost), DeepSeek-R1 paper (few-shot degrades). Close on the reassurance: the durable 80% is unchanged.');

  // ---------- 26. ITERATION ----------
  s = H.slide('PART 3 · ITERATION', 26);
  H.title(s, 'The habit', 'Prompts are drafts — iterate, then standardize');
  const iter = [
    ['edit', '1 · Draft', 'Write the prompt with the anatomy: role, task, context, format, examples.'],
    ['eye', '2 · Inspect', 'Wrong output? Diagnose which element failed: wrong altitude (role), wrong content (context), wrong shape (format), wrong style (examples).'],
    ['refresh', '3 · Refine', 'Fix that element — or ask the model itself: “rewrite this prompt so it more consistently produces X.”'],
    ['save', '4 · Standardize', 'Works twice? Name it, version it, put it in the library. A tested template beats a daily improvisation.'],
  ];
  iter.forEach((it, i) => {
    const x = 0.55 + i * 3.19;
    H.card(s, x, 1.7, 2.95, 2.6, i === 3 ? C.TEAL_TINT : C.PANEL);
    H.iconCircle(s, x + 0.24, 1.95, 0.52, it[0], C.TEAL);
    s.addText(it[1], { x: x + 0.9, y: 2.02, w: 1.95, h: 0.4, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
    s.addText(it[2], { x: x + 0.24, y: 2.6, w: 2.5, h: 1.6, fontFace: F.body, fontSize: 10.5, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.1 });
    if (i < 3) H.arrow(s, x + 2.97, 2.95, 0.2, C.TEAL);
  });
  H.callout(s, 0.55, 4.65, 12.2, 0.95, C.PANEL, [
    { text: 'Anthropic’s golden rule: ', options: { bold: true, color: C.INK, fontSize: 12.5 } },
    { text: '“Show your prompt to a colleague with minimal context and ask them to follow it. If they’d be confused, Claude will be too.”', options: { italic: true, color: C.SLATE, fontSize: 12.5 } },
  ], { iconName: 'users', iconFill: C.SLATE, size: 12.5, line: C.LINE });
  H.callout(s, 0.55, 5.75, 12.2, 0.95, C.AMBER_TINT, [
    { text: 'Why standardize? ', options: { bold: true, color: C.INK, fontSize: 12.5 } },
    { text: 'Outputs swing wildly with tiny phrasing changes. A tested, versioned template is your gauge-R&R answer to prompt variability — which is exactly what Part 4 hands you.', options: { color: C.SLATE, fontSize: 12.5 } },
  ], { iconName: 'target', iconFill: C.AMBER, size: 12.5 });
  s.addNotes(
    'HOW TO PRESENT — 1) Walk the four step cards LEFT TO RIGHT: draft → inspect → refine → standardize. At INSPECT, point back at the diagnosis grid from a few slides ago — same move. At STANDARDIZE, note the teal highlight: that’s where Part 6 lives. 2) Golden-rule band: read Anthropic’s quote VERBATIM — the colleague test. 3) Amber band: why standardize — outputs swing with tiny phrasing changes; a tested, versioned template is the gauge-R&R answer, “which is exactly what Part 4 hands you.” 4) Bridge: “rep first — then the playbook.”\n' +
    'ACRONYMS — gauge R&R = Gauge Repeatability & Reproducibility — the measurement-systems discipline; the analogy: a tested template kills prompt-to-prompt variation the way a calibrated gauge kills measurement variation.\n' +
    'CONTENT — The diagnose-by-element trick makes iteration systematic instead of random retyping. Metaprompting demo idea (live): paste a mediocre prompt, ask the assistant to critique and rewrite it, run both, compare. Bridge: Part 4 is the library of already-iterated templates.');

  // ---------- P3 REP (v1.1, skippable) ----------
  s = H.slide('THREE-MINUTE REP · PART 3', 27);
  H.title(s, 'Three-minute rep', 'Rebuild one line');
  H.repTimer(s);
  H.card(s, 0.55, 1.75, 7.4, 3.4, C.PANEL);
  s.addText('Everyone starts from the same line:', { x: 0.85, y: 2.0, w: 6.6, h: 0.35, fontFace: F.body, fontSize: 12, bold: true, color: C.SLATE, margin: 0 });
  s.addText('“Summarize this report.”', { x: 0.85, y: 2.42, w: 6.7, h: 0.5, fontFace: 'Consolas', fontSize: 16, color: C.TEAL_DARK, margin: 0 });
  H.bullets(s, 0.9, 3.1, 6.6, 1.9, [
    'Three minutes: add a Role, an audience, a numeric cap, and an Out.',
    'Compare with a neighbor — whose version would produce the more useful summary, and why?',
  ], { size: 12.5, gap: 8 });
  H.card(s, 8.25, 1.75, 4.5, 3.4, C.AMBER_TINT);
  s.addText([
    { text: 'One strong answer (presenter)', options: { bold: true, color: C.AMBER, fontSize: 11.5, breakLine: true, paraSpaceAfter: 5 } },
    { text: '“You are a precise editor. Summarize the attached report for a cross-functional partner in ≤ 150 words: the three things they must know, what changed, and what it does NOT cover. If the report doesn’t say, say so.”', options: { color: C.SLATE, fontSize: 10.8, italic: true } },
  ], { x: 8.52, y: 1.95, w: 3.95, h: 3.0, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.12 });
  s.addText('Skippable if running long.', { x: 0.55, y: 5.45, w: 12.2, h: 0.35, fontFace: F.body, fontSize: 10.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT — 1) 3:00 badge; everyone starts from the same weak line on screen: “Summarize this report.” 2) Three minutes: add a Role, an audience, a numeric cap, and an Out. 3) Neighbor compare — the learning moment: different fills, same anatomy; ask one pair whose version wins and why. 4) Only THEN reveal the presenter answer in the amber card. Skip freely if behind.\n' +
    'ACRONYMS — none on this slide.\n' +
    'CONTENT — Three minutes. The neighbor-compare is the learning moment — different fills, same anatomy. Skip freely if behind.');

  // ---------- 27. PART 4 DIVIDER ----------
  s = H.slide(null, 27, { dark: true });
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
    'HOW TO PRESENT — 1) Progress bar: part 4. One frame: “thirteen templates ship with this training — we demo two live; the rest is your handout.” 2) Point at the list: G = generative, runs in any chat tool; A (in teal) = agentic, for Claude Code / Cowork-class tools — Part 5’s world. 3) Emphasize once: starting points to adapt, not scripts. 4) Advance within 30 seconds.\n' +
    'ACRONYMS — ETL = Extract, Transform, Load — A2’s data-pipeline shape. CLAUDE.md = the standing-instructions file agents read at session start (A4). HTML = the single-file web-page format (G6).\n' +
    'CONTENT — These are starting points to adapt, not scripts. Generative templates (G) run in any chat assistant; agentic templates (A, in teal) are for Claude Code / Cowork-class tools — Part 5 explains them.');

  // ---------- 28. G2 DEEP DIVE ----------
  s = H.slide('PART 4 · DATA ANALYSIS', 28);
  H.title(s, 'Template anatomy · G2', 'Data analysis: five blocks that keep numbers honest');
  const g2 = [
    ['<role>', 'A careful analyst who computes by running code — never mental math — states n, never drops data silently.', 'LLM arithmetic is unreliable; code execution makes the math real. If your tool can’t run code, don’t trust computed numbers.'],
    ['<data>', 'File, sheet, header row, what one row means, exact column names, known issues, metric definitions.', 'The model guessing your grain and denominator is the #1 source of wrong answers. Schema first.'],
    ['<task>', 'Numbered questions in priority order — “and stop when they’re answered.”', 'Topics generate exploration; questions generate answers. The stop rule prevents ten charts and no answer.'],
    ['<method>', 'Profile the data first and show me; reconcile to a known total; flag n < 20; descriptive stats only, “associated with” not “caused by.”', 'One reconciliation anchor beats ten checks. Language discipline survives into the deck your leadership reads.'],
    ['<format>', 'Headline answer first with the number, then the table; assumptions and caveats at the end.', 'You read the answer in 10 seconds and audit the rest only if it matters.'],
  ];
  g2.forEach((r, i) => {
    const y = 1.62 + i * 1.0;
    H.card(s, 0.55, y, 12.2, 0.9, i % 2 ? 'FFFFFF' : C.PANEL, i % 2 ? C.LINE : null);
    s.addText(r[0], { x: 0.8, y: y + 0.08, w: 1.5, h: 0.74, fontFace: 'Consolas', fontSize: 12.5, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText(r[1], { x: 2.45, y: y + 0.07, w: 5.6, h: 0.76, fontFace: F.body, fontSize: 10, color: C.INK, margin: 0, valign: 'middle', lineSpacingMultiple: 1.02 });
    s.addText(r[2], { x: 8.25, y: y + 0.07, w: 4.3, h: 0.76, fontFace: F.body, fontSize: 9.3, italic: true, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 1.0 });
  });
  s.addText('block · what goes in it · why it’s there', { x: 0.55, y: 6.68, w: 8, h: 0.3, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0 });
    s.addNotes(
    'HOW TO PRESENT — 1) Frame: “one template, dissected — the other twelve share this shape: blocks, plus the reason each block exists.” 2) Walk the five rows TOP TO BOTTOM; per row: name the block, one line on what goes in (middle column), then read the RIGHT italic column aloud — the why is the teaching. 3) Slow on <method>: “reconcile to a known total — one anchor beats ten checks.” 4) Bridge: “enough anatomy — watch two templates run for real.”\n' +
    'ACRONYMS — LLM = Large Language Model. n = sample size (flag n < 20). G2 = this template’s library code.\n' +
    'CONTENT — Evidence for code-not-vibes: GPT-4 scored ~59% on 3-digit × 3-digit multiplication, falling toward zero as digits grow (Faith and Fate, NeurIPS 2023) — code execution hands the model a calculator. All four major tools now run code for analysis. For recurring or multi-file pipelines, the agentic sibling is A2 (Part 5).');

  // ---------- DEMO 1 · BLIND CRITIQUE (v1.1) ----------
  s = H.slide('PART 4 · LIVE DEMO 1', 29);
  H.title(s, 'Live demo · the blind critique (G3)', 'Watch sycophancy die in real time');
  const d1 = [
    ['1 · Set up', 'Open a fresh chat. Paste a real (or prepared) draft — a plan, a memo — introduced as “a colleague’s draft.” Do not hint at your view.'],
    ['2 · Run G3', 'Ask for: the strongest case AGAINST · the three weakest points and how a critic attacks each · what evidence would prove it wrong · overall read only at the end.'],
    ['3 · The contrast', 'Now ask the naive way in a second chat: “I wrote this — what do you think?” Compare the two answers side by side.'],
  ];
  d1.forEach((d, i) => {
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
    { text: 'The blind version finds real weaknesses; the “I wrote this” version compliments first and softens everything. Same model, same draft — the only change is what you revealed.\n\nThe science: models affirm users ~49% more than humans do. Blinding is the fix you can do today.', options: { color: C.SLATE, fontSize: 10.8 } },
  ], { x: 8.7, y: 1.9, w: 3.8, h: 3.6, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.1 });
  H.callout(s, 0.55, 5.85, 12.2, 0.75, C.TEAL_TINT, [
    { text: 'This is the Part 4 rep: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5 } },
    { text: 'everyone runs the blind critique on something of their own before session 2.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'zap', iconFill: C.TEAL, size: 11.5 });
  s.addNotes(
    'HOW TO PRESENT — 1) One-line setup: “same draft, two chats — the only variable is what I reveal about myself.” 2) Run the three step cards IN ORDER: blind version first (card 1–2), then the naive “I wrote this” ask in a second chat (card 3). 3) At the side-by-side: 20 seconds of SILENCE — let the room read both answers before anyone speaks. 4) Then the amber card: name what they noticed, and land the number — models affirm users ~49% more than humans do; blinding is the fix available today. 5) Teal band: this is the Part 4 rep — homework before session 2.\n' +
    'ACRONYMS — G3 = the evaluations/rubrics template’s library code.\n' +
    'CONTENT — v1.1: replaces the catalog slides. Prepare a safe demo draft in advance (generic plan with 2–3 planted weaknesses). Budget 6–8 minutes. The side-by-side moment is the punchline.');

  // ---------- DEMO 2 · DASHBOARD FROM A PASTE (v1.1) ----------
  s = H.slide('PART 4 · LIVE DEMO 2', 30);
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
  H.callout(s, 0.55, 5.85, 12.2, 0.75, C.PANEL, [
    { text: 'Backup plan: ', options: { bold: true, color: C.INK, fontSize: 11.5 } },
    { text: 'if generation runs long, open the pre-built copy from your desktop and narrate the prompt — the room still sees prompt → working software.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'refresh', iconFill: C.SLATE, size: 11.5, line: C.LINE });
  s.addNotes(
    'HOW TO PRESENT — 1) Frame: “this time the deliverable is a tool, not a text.” 2) Run the three step cards IN ORDER: paste the prepared table → run G6 → download the file, double-click it, filter something, sort something. 3) WHILE it generates, narrate the amber card’s spec lines — single file, offline, data embedded, nothing hard-coded, formulas visible — those lines are what made it trustworthy. 4) Say the two caveats OUT LOUD: it is a snapshot, not a live system; share the FILE, not a public link. 5) Bottom band is your safety net: pre-built copy on the desktop. 6) Bridge: “six more templates work the same way — the pointer.”\n' +
    'ACRONYMS — HTML = HyperText Markup Language — the single-file web-page format. KPI = Key Performance Indicator (the number tiles). G6 = the interactive-HTML template’s library code.\n' +
    'CONTENT — v1.1: second demo. Pre-stage the data table and the G6 prompt in a text file so the demo is paste-paste-run. Budget 6–8 minutes.');

  // ---------- PLAYBOOK HANDOUT POINTER (v1.1) ----------
  s = H.slide('PART 4 · THE PLAYBOOK', 31);
  H.title(s, 'The full playbook travels with you', 'Eight generative templates — copy, fill, run');
  const pb = [
    ['G1 · Writing & editing', 'raw material in, hard word cap, “add no facts” — edit beats draft'],
    ['G2 · Data analysis', 'exact columns, code-not-vibes, reconcile to a known total, then stop'],
    ['G3 · Evaluations', 'anchored rubric, quotes as evidence, blind critique — you just watched it'],
    ['G4 · Spreadsheets', 'README tab, formulas not values, cleaning with a logged rule per change'],
    ['G5 · Presentations', 'titles state findings with numbers; approve text before rendering'],
    ['G6 · Interactive HTML', 'single file, offline, auditable — you just watched it'],
    ['G7 · Research briefs', 'a question not a topic; every bullet gets a link + date; demand the gaps'],
    ['G8 · Documents', 'summaries serve a decision; verbatim quotes for anything load-bearing'],
  ];
  pb.forEach((p, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.65 + Math.floor(i / 2) * 1.14;
    H.card(s, x, y, 5.95, 1.0, C.PANEL);
    s.addText([
      { text: p[0], options: { bold: true, color: C.TEAL_DARK, fontSize: 12, breakLine: true, paraSpaceAfter: 2 } },
      { text: p[1], options: { color: C.SLATE, fontSize: 10 } },
    ], { x: x + 0.24, y: y + 0.08, w: 5.5, h: 0.86, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.02 });
  });
  H.callout(s, 0.55, 6.35, 12.2, 0.65, C.TEAL_TINT, [
    { text: 'Your handout pack: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5 } },
    { text: 'prompt-library/ (all 13 templates, each with a filled example and pitfalls) · the Template Creator + Configurator that assemble them · the cheat sheet, ELEMENTS guide, and Taxonomy Reference.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'download', iconFill: C.TEAL, size: 11.5 });
  s.addNotes(
    'HOW TO PRESENT — 1) Sixty seconds: sweep the eight tiles in one pass — “two you just watched; six more work exactly the same way: blocks plus reasons.” 2) Teal band: name the FULL handout pack piece by piece — templates, Creator, Configurator, cheat sheet, ELEMENTS guide, Taxonomy Reference — so nobody leaves without knowing what they own. 3) Close session 1: “homework is the blind critique on something of yours; session 2 is delegation — bring the homework story.”\n' +
    'ACRONYMS — HTML / XLSX = web-page / Excel file formats (Creator / Configurator). G1–G8 = the generative templates’ library codes.\n' +
    'CONTENT — v1.1: the catalog is a handout pointer, not four lecture slides. Session 1 ends here.');

  // ---------- P3 REP note: runs inside session 1 wrap if time allows ----------
};
