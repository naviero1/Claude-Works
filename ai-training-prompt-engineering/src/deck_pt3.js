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
    { text: 'Retired to the bench — today’s models reason by default. The 2026 version is slide 25.', options: { color: C.SLATE, fontSize: 11.5 } },
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

  // ---------- 29. WRITING & DOCUMENTS ----------
  s = H.slide('PART 4 · WRITING & DOCUMENTS', 29);
  H.title(s, 'Templates G1 + G8', 'Writing and long documents: edit beats draft');
  H.card(s, 0.55, 1.65, 6.0, 4.95, C.PANEL);
  s.addText('G1 · Writing & editing', { x: 0.85, y: 1.88, w: 5.3, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.TEAL_DARK, margin: 0 });
  H.bullets(s, 0.9, 2.4, 5.4, 4.0, [
    { t: 'Most workplace writing requests are edits of text you supply — feed raw material, don’t ask for blank-page magic', b: true },
    'Frame the job of the message: “the reader should know / decide / do X” — a success criterion, not a topic',
    'Hard length caps (“≤ 120 words — cut content before quality”): uncapped AI runs 2–3× too long',
    '“Do not add facts beyond the material” — the highest-value line in the template',
    'Voice: build a STYLE CARD once from 2–3 writing samples; reuse it forever',
    'Edit mode returns a change list — you accept or reject each change, so you stay the author',
  ], { size: 11.5, gap: 7 });
  H.card(s, 6.75, 1.65, 6.0, 4.95, C.PANEL);
  s.addText('G8 · Summarize & compare', { x: 7.05, y: 1.88, w: 5.3, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.TEAL_DARK, margin: 0 });
  H.bullets(s, 7.1, 2.4, 5.4, 4.0, [
    'Summaries serve a decision: “for [audience] who must [decide X]” — otherwise the model keeps the wrong 10%',
    { t: 'Always ask: “what does this document NOT cover that the reader will assume it does?” — kills the completeness illusion', b: true },
    'Verbatim quotes with location for anything contractual, regulatory, or numeric — paraphrase is where obligations drift',
    'Version compare: substantive diffs in a table, conflicts flagged, both sides quoted',
    'Meeting notes → action table with owner, due date, and the source sentence; unassigned stays UNASSIGNED',
  ], { size: 11.5, gap: 7 });
  s.addNotes('The edits-beat-drafts point is backed by OpenAI/NBER usage data: writing ≈ 40% of work messages, and about two-thirds of those are edits of user text, not new drafting. Length caps and the no-new-facts rule address the two most common AI-writing complaints.');

  // ---------- 30. EVALUATIONS ----------
  s = H.slide('PART 4 · EVALUATIONS', 30);
  H.title(s, 'Template G3', 'AI as reviewer: rubric first, judgment second — yours last');
  const evals = [
    ['list', 'Rubric grading', 'Anchored 1–5 scale per criterion · “quotes as evidence” · “not addressed = 1, no credit for what you assume” · then: gaps + the questions to ask the author.'],
    ['scale', 'Pairwise comparison', 'Score each option independently first, then head-to-head per criterion. Substance over polish, explicitly — and re-check imagining reverse reading order.'],
    ['shield', 'Critique my work', 'Steelman the opposite position · three weakest points · “what evidence would prove this wrong?” · overall read only at the end. Never say which option you prefer.'],
  ];
  evals.forEach((e, i) => {
    const y = 1.65 + i * 1.55;
    H.card(s, 0.55, y, 7.5, 1.4, C.PANEL);
    H.iconCircle(s, 0.82, y + 0.4, 0.55, e[0], C.TEAL);
    s.addText([
      { text: e[1], options: { bold: true, color: C.INK, fontSize: 13.5, breakLine: true, paraSpaceAfter: 3 } },
      { text: e[2], options: { color: C.SLATE, fontSize: 10.8 } },
    ], { x: 1.6, y: y + 0.1, w: 6.25, h: 1.2, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.06 });
  });
  H.card(s, 8.35, 1.65, 4.4, 4.65, C.AMBER_TINT);
  s.addText('Judge biases to design around', { x: 8.62, y: 1.88, w: 3.9, h: 0.4, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 8.65, 2.38, 3.85, 3.8, [
    { t: 'Position bias — favors the first/last option read' },
    { t: 'Verbosity bias — longer reads as better' },
    { t: 'Self-preference — models rate their own style highly' },
    { t: 'Sycophancy — mirrors any preference you leak' },
    { t: 'Countered by: rubrics, quotes-as-evidence, independent-then-compare, blind authorship, two runs', b: true },
  ], { size: 11, gap: 7 });
  H.callout(s, 0.55, 6.45, 12.2, 0.62, C.RED_TINT, [
    { text: 'Boundary: ', options: { bold: true, color: C.RED, fontSize: 11.5 } },
    { text: 'consequential calls — people, money, compliance — get a human owner. AI narrows the field and sharpens questions; it doesn’t sign.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'hand', iconFill: C.RED, size: 11.5 });
  s.addNotes('LLM-as-judge research: GPT-4-class judges reached >80% agreement with human preferences — the same as human-human agreement (Zheng et al., MT-Bench, NeurIPS 2023); biases (position, verbosity, self-preference) are from the same paper. 2026 caution: a judge can be highly repeatable and still biased — a consistent judge is not necessarily a fair judge. G3 mitigates mechanically: rubric anchors, quotes as evidence, independent-then-compare, blinding. Use cases in the room: supplier proposals, SOP drafts, report QC. Screening inspection, not final release.');

  // ---------- 31. SPREADSHEETS & DECKS ----------
  s = H.slide('PART 4 · FILES THAT DO WORK', 31);
  H.title(s, 'Templates G4 + G5', 'Spreadsheets and decks: specify like an engineer');
  H.card(s, 0.55, 1.65, 6.0, 4.95, C.PANEL);
  s.addText('G4 · Spreadsheets', { x: 0.85, y: 1.88, w: 5.3, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.TEAL_DARK, margin: 0 });
  H.bullets(s, 0.9, 2.4, 5.4, 4.0, [
    { t: 'Name exact columns (“C = Ship Date, F = Qty”) — the single highest-leverage habit; it’s Microsoft’s own #1 tip', b: true },
    'Every workbook ships a README tab: sources, as-of date, metric definitions, assumptions, change log',
    'Formulas, not pasted values — the file must survive a data update',
    'Cleaning: values unchanged, every rule logged with rows affected, oddities listed for review — never silently “fixed”',
    'Formula help: explained piece by piece before insertion + a 3-row hand check',
  ], { size: 11.5, gap: 7 });
  H.card(s, 6.75, 1.65, 6.0, 4.95, C.PANEL);
  s.addText('G5 · Presentations', { x: 7.05, y: 1.88, w: 5.3, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.TEAL_DARK, margin: 0 });
  H.bullets(s, 7.1, 2.4, 5.4, 4.0, [
    'Flow: content → outline → approval → deck. Never “make me a presentation about X”',
    { t: 'Titles state findings with the number (“Scrap fell 40% after the fixture change”), never topics (“Scrap update”)', b: true },
    'Audience + minutes-of-their-time in the prompt sets the altitude',
    'Gate: titles + bullets as plain text for approval BEFORE rendering — re-rendering is cheap, re-thinking a circulated deck is not',
    'Speaker notes + source/as-of footer on every data slide',
  ], { size: 11.5, gap: 7 });
  s.addNotes('Both templates encode the same philosophy: specification beats hope. Message titles are evidence-backed: assertion-evidence slides (sentence headline + visual evidence) measurably beat topic-title + bullets for comprehension and recall (Penn State, Alley et al., p<.01). Trust calibration for sheets: Microsoft itself reports Excel Agent Mode at 57.2% vs a ~71% human baseline on real spreadsheet tasks — a strong intern, not a signed-off spreadsheet. The text-before-render gate bridges to agentic gates in Part 5.');

  // ---------- 32. HTML + RESEARCH ----------
  s = H.slide('PART 4 · BEYOND OFFICE FILES', 32);
  H.title(s, 'Templates G6 + G7', 'Interactive HTML — and research that cites its sources');
  H.card(s, 0.55, 1.65, 6.0, 4.95, C.TEAL_TINT);
  s.addText('G6 · Interactive HTML', { x: 0.85, y: 1.88, w: 5.3, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.TEAL_DARK, margin: 0 });
  H.bullets(s, 0.9, 2.4, 5.4, 4.0, [
    { t: 'When the audience will explore — filter, sort, what-if — one HTML file beats a deck or spreadsheet', b: true },
    'Ask for: single file, data embedded, works offline from disk on a locked-down laptop — email it or drop it on SharePoint',
    'Shapes: KPI dashboard with filters · what-if calculator (formulas shown on screen, auditable) · searchable team tracker / reference',
    'All numbers computed from embedded data — no hard-coded results you can’t trace',
    'Treat the file like the data inside it: same confidentiality class · give it an owner + as-of banner, or it goes stale-but-credible',
  ], { size: 11.5, gap: 7 });
  H.card(s, 6.75, 1.65, 6.0, 4.95, C.PANEL);
  s.addText('G7 · Research briefs', { x: 7.05, y: 1.88, w: 5.3, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.TEAL_DARK, margin: 0 });
  H.bullets(s, 7.1, 2.4, 5.4, 4.0, [
    'A research question, not a topic — plus the decision it feeds',
    'Use tools that actually search and cite; never trust from-memory citations',
    { t: 'Every bullet ends with a link and a date; no link → labeled “unsourced — verify”', b: true },
    'Demand the gaps section: “what the sources do NOT establish” — where honesty lives',
    'Spot-check 2–3 load-bearing links before you forward; for big calls, run the question in a second tool and mind the disagreements',
  ], { size: 11.5, gap: 7 });
  s.addNotes('G6 is the sleeper hit for engineers: a self-contained dashboard or calculator colleagues can open anywhere, no install, no server, auditable formulas. The constraint “single file, offline” is what makes it safe and shareable. G7 formalizes the verification habit for research outputs.');
};
