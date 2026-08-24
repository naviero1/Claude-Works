// PART 3 (Prompt engineering) + PART 4 (Applied playbook)
const { C, F } = require('./deck_lib');

module.exports = function buildPartThree(pres, H) {
  // ---------- 21. PART 3 DIVIDER ----------
  let s = H.slide(null, 21, { dark: true });
  s.addText('PART 3 · PROMPT ENGINEERING', { x: 0.55, y: 2.3, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('The craft: getting what\nyou actually meant', { x: 0.55, y: 2.8, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('Every AI vendor publishes prompting guidance. It converges on one anatomy and a handful of techniques — this part teaches them, with the evidence for what works and what’s myth.', { x: 0.55, y: 4.85, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });

  // ---------- 22. UNIVERSAL ANATOMY ----------
  s = H.slide('PART 3 · THE ANATOMY', 22);
  H.title(s, 'The universal anatomy', 'Four vendors, one recipe: Role · Task · Context · Format · Examples');
  const rows = [
    [{ text: '', options: {} }, 'Anthropic (Claude)', 'OpenAI (ChatGPT)', 'Google (Gemini)', 'Microsoft (Copilot)'],
  ];
  const anat = [
    ['Role', '“Give Claude a role” (system prompt)', 'role / developer message', 'Persona', '(part of Context)'],
    ['Task', '“Be clear and direct”', '“simple and direct” instructions', 'Task — “the most important component”', 'Goal — the only required part'],
    ['Context', '“Add context — explain why”', 'context sections, delimiters', 'Context', 'Context + Source'],
    ['Format', 'format control, XML tags', 'format specs, verbosity', 'Format', 'Expectations'],
    ['Examples', '3–5 diverse, tagged examples', '“few-shot if needed”', '(use your documents)', '(iterate with follow-ups)'],
  ];
  // table via cards
  const colX = [0.55, 2.35, 5.0, 7.65, 10.3];
  const colW = [1.7, 2.55, 2.55, 2.55, 2.45];
  ['', 'Anthropic', 'OpenAI', 'Google', 'Microsoft'].forEach((h, i) => {
    if (i > 0) s.addText(h, { x: colX[i], y: 1.62, w: colW[i], h: 0.32, fontFace: F.body, fontSize: 11.5, bold: true, color: C.TEAL_DARK, margin: 0 });
  });
  anat.forEach((r, ri) => {
    const y = 2.0 + ri * 0.78;
    H.card(s, 0.55, y, 12.2, 0.68, ri % 2 ? 'FFFFFF' : C.PANEL, ri % 2 ? C.LINE : null);
    s.addText(r[0], { x: 0.75, y: y + 0.08, w: 1.5, h: 0.5, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0, valign: 'middle' });
    for (let i = 1; i <= 4; i++) {
      s.addText(r[i], { x: colX[i], y: y + 0.06, w: colW[i] - 0.15, h: 0.58, fontFace: F.body, fontSize: 9.3, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 1.0 });
    }
  });
  H.callout(s, 0.55, 6.05, 12.2, 0.95, C.TEAL_TINT, [
    { text: 'Google’s data point: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12 } },
    { text: 'the most fruitful prompts averaged ~21 words with context — most people type fewer than nine. A good prompt is a short briefing, not a search query.', options: { color: C.SLATE, fontSize: 12 } },
  ], { iconName: 'edit', iconFill: C.TEAL, size: 12 });
  s.addNotes('The frameworks are near-identical: Google calls it Persona-Task-Context-Format; Microsoft Goal-Context-Source-Expectations; Anthropic and OpenAI teach the same elements. The 21-words stat is from Google’s Oct 2024 Workspace guide (dropped in the newer edition — teach as directional, not gospel). Anthropic’s golden rule belongs in the room: show your prompt to a colleague with minimal context — if they’d be confused, the model will be too. Continuity hook: our own library teaches the same skeleton — the internal crash course’s “5 building blocks” (Role, Context, Task, Format, Tone) and CRISP checklist, and Phoenix & Taylor’s Five Principles (Give Direction, Specify Format, Provide Examples, Evaluate Quality, Divide Labor). One anatomy, many aliases.');

  // ---------- E1. THE FIVE ELEMENTS, DEFINED (v1.1) ----------
  s = H.slide('PART 3 · THE ELEMENTS', 23);
  H.title(s, 'The elements, defined', 'Five slots — each with a job, a mechanism, and a failure it prevents');
  const edefs = [
    ['Role', 'who is answering — behaviors, not titles', '“You are a senior analyst.”', '“You never invent numbers; you state n; you say what the data can’t answer.”'],
    ['Task', 'verb + object + audience + success criterion', '“Analyze the returns data.”', '“What is the return rate by site for Q2 vs the 2% target?”'],
    ['Context', 'what the model cannot know — material, glossary, quirks, the why', '“Use our standard definitions.”', '“Return rate = returns ÷ shipped. Quirk: the export has a totals row — exclude it and say so.”'],
    ['Format', 'the output contract — shape, numeric cap, tone', '“Keep it short and professional.”', '“≤ 120 words: the ask in sentence one, two facts with numbers, the deadline.”'],
    ['Examples', '3–5 diverse demonstrations, edge case included', 'three clones of the happy case', 'one typical + one edge + one reject case, fenced in tags'],
  ];
  edefs.forEach((r, i) => {
    const y = 1.62 + i * 1.0;
    H.card(s, 0.55, y, 12.2, 0.9, i % 2 ? 'FFFFFF' : C.PANEL, i % 2 ? C.LINE : null);
    s.addText(r[0], { x: 0.78, y: y + 0.08, w: 1.35, h: 0.74, fontFace: F.head, fontSize: 14, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText(r[1], { x: 2.2, y: y + 0.07, w: 3.6, h: 0.76, fontFace: F.body, fontSize: 10, color: C.INK, margin: 0, valign: 'middle', lineSpacingMultiple: 1.02 });
    s.addText([{ text: 'weak  ', options: { bold: true, color: C.RED, fontSize: 8.5 } }, { text: r[2], options: { color: C.SLATE, fontSize: 9 } }], { x: 5.95, y: y + 0.07, w: 3.1, h: 0.76, fontFace: F.body, margin: 0, valign: 'middle', lineSpacingMultiple: 1.0 });
    s.addText([{ text: 'strong  ', options: { bold: true, color: C.GREEN, fontSize: 8.5 } }, { text: r[3], options: { color: C.SLATE, fontSize: 9 } }], { x: 9.15, y: y + 0.07, w: 3.4, h: 0.76, fontFace: F.body, margin: 0, valign: 'middle', lineSpacingMultiple: 1.0 });
  });
  s.addText('The full field guide — mechanism, evidence, and pitfalls per element — is in your handout (ELEMENTS guide).', { x: 0.55, y: 6.68, w: 12.2, h: 0.3, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes('v1.1 addition. One row at a time: name the element, read weak vs strong aloud — the contrast teaches faster than the definition. Role: behaviors are auditable, titles aren’t. Task: a question carries its own completion test. Context: unstated quirks become invented fixes. Format: numeric caps are enforceable, adjectives aren’t. Examples: the model handles edge cases exactly as yours do.');

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
  s.addNotes('v1.1 addition. The grid is the practical payoff of the element model: when output disappoints, don’t reword at random — name the failed element and fix that one. This turns iteration from retyping into diagnosis. Same grid opens the ELEMENTS handout.');

  // ---------- 23. SEVEN TECHNIQUES ----------
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
  s.addNotes('Each technique traces to vendor docs and research: examples = Brown et al. 2020 few-shot; the out = Anthropic hallucination guidance; chaining = Anthropic 2026 (“still useful when you need to inspect intermediate outputs”); self-check needs concrete criteria (self-correction research shows “are you sure?” can make answers worse). Metaprompting is now productized: OpenAI Prompt Optimizer, Anthropic prompt improver, Google “Make this a power prompt.”');

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
  s.addNotes('Sources worth naming aloud: format brittleness = Sclar et al. ICLR 2024 (up to 76-point swings from formatting alone — the case for tested, versioned templates; think gauge R&R for prompts). Personas = Zheng et al. EMNLP 2024. Tipping = Salinas & Morstatter, ACL 2024. Sycophancy = Cheng et al., Science 2026 (arXiv 2510.01395). The lesson isn’t “AI lies” — it’s “AI mirrors you”; blind it to your preference before asking for judgment.');

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
    { text: 'clarity and specificity · relevant context and sources · output format · giving an out · grounding in documents · iteration. The anatomy from slide 22 applies to every model you will ever use — the scaffolding tricks retire, the briefing skills compound.', options: { color: C.SLATE, fontSize: 12.5 } },
  ], { iconName: 'check', iconFill: C.TEAL, size: 12.5 });
  s.addNotes('This slide inoculates against stale advice from 2023-era blog posts. Sources: OpenAI reasoning best practices (“avoid chain-of-thought prompts”, “try zero shot first”), Anthropic prompting best practices 2026 (“prefer general instructions over prescriptive steps”), GPT-5 guide (contradiction cost), DeepSeek-R1 paper (few-shot degrades). Close on the reassurance: the durable 80% is unchanged.');

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
  s.addNotes('The diagnose-by-element trick makes iteration systematic instead of random retyping. Metaprompting demo idea (live): paste a mediocre prompt, ask the assistant to critique and rewrite it, run both, compare. Bridge: Part 4 is the library of already-iterated templates.');

  // ---------- P3 REP (v1.1, skippable) ----------
  s = H.slide('THREE-MINUTE REP · PART 3', 27);
  H.title(s, 'Three-minute rep', 'Rebuild one line');
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
  s.addNotes('Three minutes. The neighbor-compare is the learning moment — different fills, same anatomy. Skip freely if behind.');

  // ---------- 27. PART 4 DIVIDER ----------
  s = H.slide(null, 27, { dark: true });
  s.addText('PART 4 · THE PLAYBOOK', { x: 0.55, y: 2.1, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('Thirteen templates,\nready to copy', { x: 0.55, y: 2.6, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('Eight generative + five agentic, shipped with this training in prompt-library/.\nEach: the template · a filled example · why it works · the pitfalls.', { x: 0.55, y: 4.6, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  const libNames = ['G1 Writing & editing', 'G2 Data analysis', 'G3 Evaluations & rubrics', 'G4 Spreadsheets', 'G5 Presentations', 'G6 Interactive HTML', 'G7 Research briefs', 'G8 Summarize & compare', 'A1 Mission brief', 'A2 ETL → presentation', 'A3 Recurring cycle', 'A4 CLAUDE.md starter', 'A5 Document pipeline'];
  libNames.forEach((n, i) => {
    const x = 0.55 + (i % 4) * 3.12;
    const y = 5.55 + Math.floor(i / 4) * 0.44;
    s.addText('▸ ' + n, { x, y, w: 3.0, h: 0.38, fontFace: F.body, fontSize: 10.5, color: i < 8 ? C.ON_DARK_MUTE : C.TEAL_LIGHT, margin: 0 });
  });
  s.addNotes('Emphasize: these are starting points to adapt, not scripts. Generative templates (G) run in any chat assistant; agentic templates (A, in teal) are for Claude Code / Cowork-class tools — Part 5 explains them.');

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
  s.addNotes('Walk one row at a time; the right column is the teaching. Evidence for code-not-vibes: GPT-4 scored ~59% on 3-digit x 3-digit multiplication, falling toward zero as digits grow (Faith and Fate, NeurIPS 2023) — code execution hands the model a calculator. All four major tools now run code for analysis. This anatomy generalizes: every template is blocks + reasons. For recurring or multi-file pipelines, the agentic sibling is A2 (Part 5).');

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
  s.addNotes('v1.1: replaces the catalog slides. Prepare a safe demo draft in advance (generic plan with 2–3 planted weaknesses). Budget 6–8 minutes. The side-by-side moment is the punchline — let the room read both answers in silence for 20 seconds before speaking.');

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
  s.addNotes('v1.1: second demo. Pre-stage the data table and the G6 prompt in a text file so the demo is paste-paste-run. If generation runs long, have a pre-built copy of the dashboard ready to open — narrate the prompt while it loads. Budget 6–8 minutes.');

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
    { text: 'Where they live: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5 } },
    { text: 'prompt-library/ in the repo — each with a filled example and pitfalls — plus the interactive Template Creator that assembles any of them from menus.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'download', iconFill: C.TEAL, size: 11.5 });
  s.addNotes('v1.1: the catalog is now a handout pointer, not four lecture slides. Walk it in 60 seconds: two templates they just saw demoed, six more that work the same way. Session 1 ends here.');

  // ---------- P3 REP note: runs inside session 1 wrap if time allows ----------
};
