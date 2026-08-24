// PART I — Primer: where this came from, how it works
const { C, F } = require('./deck_lib');

module.exports = function buildPartOne(pres, H) {
  // ---------- 1. TITLE ----------
  let s = H.slide(null, null, { dark: true });
  s.addText('EMPLOYEE TRAINING · AUGUST 2026', { x: 0.55, y: 1.0, w: 8, h: 0.35, fontFace: F.body, fontSize: 13, bold: true, charSpacing: 3, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('From Prompts to Agents', { x: 0.55, y: 1.4, w: 12.2, h: 1.05, fontFace: F.head, fontSize: 54, bold: true, color: C.ON_DARK, margin: 0 });
  s.addText('A focused course on prompt engineering — for generative AI you talk to,\nand agentic AI you delegate to.', { x: 0.55, y: 2.55, w: 10.5, h: 0.85, fontFace: F.body, fontSize: 16, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  const cols = [
    ['THE PRIMER', 'History & core concepts', 'four eras of AI · tokens · context windows · RAG · reasoning models · hallucination'],
    ['THE CRAFT', 'Prompt engineering', 'the universal anatomy · seven techniques · what the evidence says · a template playbook'],
    ['THE LEAP', 'Agentic AI', 'tools & models worth knowing · mission briefs · guardrails · managing your prompt library'],
  ];
  cols.forEach((cd, i) => {
    const x = 0.55 + i * 4.18;
    H.card(s, x, 3.85, 3.95, 1.75, C.DARK_CARD);
    s.addText([
      { text: cd[0], options: { bold: true, color: C.TEAL_LIGHT, fontSize: 12, breakLine: true, paraSpaceAfter: 4 } },
      { text: cd[1], options: { bold: true, color: C.ON_DARK, fontSize: 14.5, breakLine: true, paraSpaceAfter: 4 } },
      { text: cd[2], options: { color: C.ON_DARK_MUTE, fontSize: 10 } },
    ], { x: x + 0.28, y: 4.02, w: 3.45, h: 1.45, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.05 });
  });
  s.addText('Companion to “Working Smart with AI.” All examples are generic — no internal document names or confidential data appear anywhere.', { x: 0.55, y: 6.3, w: 12.2, h: 0.4, fontFace: F.body, fontSize: 10.5, italic: true, color: C.ON_DARK_MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT — 1) Have this up as people arrive; don’t read it to them. 2) Open with the name and the one-liner: “This is a course about one skill — prompting — in two modes: generative AI you talk to, and agentic AI you delegate to.” 3) Sweep the three cards left to right as the journey: the primer, the craft, the leap. 4) Point at the footer line: every example is generic — no company data anywhere in the material. 5) Bridge: “Before the map — why this one skill is worth two hours.”\n' +
    'ACRONYMS — AI = Artificial Intelligence (defined once here; it recurs on nearly every slide). RAG = Retrieval-Augmented Generation — the model fetches passages from your documents before answering; taught properly in Part 1.\n' +
    'CONTENT — This training goes deeper than the general AI onboarding: it is specifically about prompting — the skill — across two modes: generative (AI that talks) and agentic (AI that works). Everything is dated August 2026 because this field moves monthly.');

  // ---------- 2. WELCOME + MAP (merged, v1.1) ----------
  s = H.slide('WELCOME', 2);
  H.title(s, 'Welcome', 'One skill, two modes — and a library you keep');
  H.bullets(s, 0.55, 1.62, 6.1, 2.5, [
    { t: 'Prompting is the one AI skill that transfers everywhere: every assistant, every vendor, every year. Models change monthly; the craft compounds.', b: true },
    { t: 'The same skill has two modes now. Generative: you ask, it writes, you act. Agentic: you brief it, it plans, uses tools, checks itself, and delivers.' },
    { t: 'Each mode needs a different kind of prompt — that distinction is the backbone of this training.' },
  ], { size: 12.5, gap: 8 });
  H.callout(s, 0.55, 4.4, 6.1, 1.5, C.TEAL_TINT, [
    { text: 'The 10-second version: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12.5, breakLine: true } },
    { text: 'a generative prompt describes what to write.\nAn agentic prompt describes a job to run — goal, inputs, checks, and when to stop and ask you.', options: { color: C.SLATE, fontSize: 12 } },
  ], { iconName: 'zap', iconFill: C.TEAL, size: 12 });
  H.card(s, 7.0, 1.55, 5.75, 2.95, C.PANEL);
  s.addText('The map — two one-hour sessions', { x: 7.3, y: 1.78, w: 5.2, h: 0.4, fontFace: F.head, fontSize: 15.5, bold: true, color: C.INK, margin: 0 });
  s.addText([
    { text: 'SESSION 1', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 3 } },
    { text: '1 · The primer — how LLMs actually work\n2 · Models & tools, August 2026\n3 · Prompt engineering — anatomy + techniques\n4 · The playbook — two live demos', options: { color: C.SLATE, fontSize: 11, breakLine: true, paraSpaceAfter: 8 } },
    { text: 'SESSION 2', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 3 } },
    { text: '5 · Agentic prompting — the mission brief\n6 · Managing prompts as assets · wrap-up', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 7.3, y: 2.22, w: 5.2, h: 2.2, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.12 });
  H.callout(s, 7.0, 4.7, 5.75, 1.9, C.AMBER_TINT, [
    { text: 'You leave with: ', options: { bold: true, color: C.INK, fontSize: 12, breakLine: true } },
    { text: 'a working AI vocabulary · a tool map · the universal prompt anatomy + seven techniques · a 13-template library with an interactive Template Creator · the Prompt Element Taxonomy reference (your parts catalog) · team conventions for storing and versioning prompts.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'download', iconFill: C.AMBER, size: 11.5 });
  s.addNotes(
    'HOW TO PRESENT — 1) Say the bold line first: “Prompting is the one AI skill that transfers everywhere — every assistant, every vendor, every year.” 2) Walk the three left bullets top to bottom; land on “two modes” as the backbone of the whole training. 3) Move to the map card: read the six part names quickly and show the split — parts 1–4 today, 5–6 in session two. 4) Teal card: read the 10-second version VERBATIM — it is the thesis. 5) Amber card: the take-homes; physically hold up the handout pack here (cheat sheet, ELEMENTS guide, Taxonomy Reference) so people know things are coming home with them. 6) Bridge: “Part 1 — how this thing actually works.”\n' +
    'ACRONYMS — LLM = Large Language Model — the text engine behind every assistant in this course.\n' +
    'CONTENT — Merged welcome+map (v1.1). Two-session delivery: split after Part 4. Parts 1, 3, 5, and 6 end with a skippable three-minute rep; Part 2’s rep is folded into its test-set slide, Part 4’s rep is the blind-critique homework. Set the thesis early: two modes, one craft; the library, Creator, and taxonomy are the take-home.');

  // ---------- 4. PART I DIVIDER ----------
  s = H.slide(null, 4, { dark: true });
  H.partMarker(s, 1);
  s.addText('PART 1 · THE PRIMER', { x: 0.55, y: 2.3, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('Where this came from,\nand how it actually works', { x: 0.55, y: 2.8, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('Seventy years in two slides, then the six concepts that make you fluent: tokens, context, RAG, reasoning, hallucination — and why prompting exists at all.', { x: 0.55, y: 4.85, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes(
    'HOW TO PRESENT — 1) Dividers are pacing: breathe. Read the two-line title, nothing more. 2) Point at the progress bar top-left: “six parts — this is where we are” (the bar returns on every divider). 3) Set expectations in one sentence: “Two history slides, then six concepts — the concepts are the vocabulary for everything after.” 4) Under 30 seconds, then advance.\n' +
    'ACRONYMS — RAG = Retrieval-Augmented Generation (in the subtitle; it gets its own slide shortly).');

  // ---------- 5. FOUR ERAS ----------
  s = H.slide('PART 1 · A SHORT HISTORY', 5);
  H.title(s, 'Seventy years in one slide', 'Four eras: rules → learning → generative → agentic');
  const eras = [
    ['edit', 'Rules', '1950s–1990s', 'Humans hand-code the logic: “if X then Y.” Expert systems shine, then crack — rules can’t cover messy reality. Twice, hype outruns results: the “AI winters.”', C.PANEL],
    ['chart', 'Learning', '1990s–2010s', 'The flip: stop writing rules, let the system find patterns in examples. Spam filters, search, recommendations. 2012: deep neural nets + GPUs crush image recognition (AlexNet).', C.PANEL],
    ['brain', 'Generative', '2017–', 'The Transformer (2017) lets models train on the whole internet in parallel. Predict-the-next-word at that scale writes, summarizes, codes. ChatGPT makes it a product (2022).', C.TEAL_TINT],
    ['robot', 'Agentic', '2024–', 'Models get “arms”: tools, browsers, files, code. Reasoning models plan multi-step work; agents execute it with limited supervision. Where the frontier is now.', C.TEAL_TINT],
  ];
  eras.forEach((e, i) => {
    const x = 0.55 + i * 3.19;
    H.card(s, x, 1.7, 2.95, 3.6, e[4]);
    H.iconCircle(s, x + 0.24, 1.95, 0.52, e[0], C.TEAL);
    s.addText(e[1], { x: x + 0.9, y: 1.98, w: 2.0, h: 0.35, fontFace: F.head, fontSize: 15.5, bold: true, color: C.INK, margin: 0 });
    s.addText(e[2], { x: x + 0.9, y: 2.32, w: 2.0, h: 0.28, fontFace: F.body, fontSize: 9.5, bold: true, color: C.MUTE, margin: 0 });
    s.addText(e[3], { x: x + 0.24, y: 2.75, w: 2.5, h: 2.4, fontFace: F.body, fontSize: 10.6, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.1 });
    if (i < 3) H.arrow(s, x + 2.97, 3.45, 0.2, C.TEAL);
  });
  H.callout(s, 0.55, 5.6, 12.2, 1.05, C.AMBER_TINT, [
    { text: 'Why the last decade exploded — scaling laws (2020): ', options: { bold: true, color: C.INK, fontSize: 12.5 } },
    { text: 'bigger model + more data + more compute = predictably better results. Progress stopped being a research gamble and became an investment roadmap.', options: { color: C.SLATE, fontSize: 12.5 } },
  ], { iconName: 'trend', iconFill: C.AMBER });
  s.addNotes(
    'HOW TO PRESENT — 1) Frame it: “Seventy years in one slide — as four eras.” 2) Walk the four cards LEFT TO RIGHT, one sentence each; use the arrows as the story: rules cracked on messy reality → learn from examples instead → generative scale → models get arms. 3) Pause once, on “AI winters” in card 1: over-promising collapsed funding twice — skepticism about AI is historically earned. 4) Close on the amber band: scaling laws turned progress from a research gamble into an investment roadmap. 5) Bridge: “zoom into the decade that changed work.”\n' +
    'ACRONYMS — GPU = Graphics Processing Unit — the graphics chip class that turned out to be perfect for training neural networks (AlexNet, 2012).\n' +
    'CONTENT — The eras framing is a teaching synthesis — each transition is well documented, but present it as “a useful way to see 70 years,” not official taxonomy. The rules era = writing the SOP yourself; the learning era = deriving the SOP from a thousand examples — that lands with quality engineers. Winters lesson: over-promising causes funding collapse; healthy skepticism is historically earned. (SOP = Standard Operating Procedure.)');

  // ---------- 6. THE GENERATIVE DECADE ----------
  s = H.slide('PART 1 · A SHORT HISTORY', 6);
  H.title(s, 'The decade that changed work', '2017 → 2026: from one paper to a billion users');
  const tl = [
    ['2017', 'The Transformer', '“Attention Is All You Need” (Google) — an architecture that scales with hardware'],
    ['2020', 'GPT-3: few-shot', 'show it examples in the prompt, it does the task — prompt engineering is born'],
    ['2022', 'RLHF + ChatGPT', 'instruction tuning turns a predictor into an assistant; 100M users in 2 months'],
    ['2024', 'Reasoning models', 'OpenAI o1 “thinks” before answering — pay compute at answer time, not just training'],
    ['2025', 'The agentic turn', 'DeepSeek R1 open-weights reasoning · computer & browser use · Claude Code · ChatGPT agent'],
    ['2026', 'Agents for everyone', 'Claude Cowork brings the coding-agent engine to general office work'],
  ];
  tl.forEach((t, i) => {
    const y = 1.62 + i * 0.82;
    s.addText(t[0], { x: 0.55, y, w: 0.85, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.TEAL, margin: 0 });
    s.addText([
      { text: t[1] + ' — ', options: { bold: true, color: C.INK, fontSize: 12.5 } },
      { text: t[2], options: { color: C.SLATE, fontSize: 11.5 } },
    ], { x: 1.55, y, w: 6.4, h: 0.75, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.05 });
  });
  s.addShape('line', { x: 1.42, y: 1.7, w: 0, h: 4.7, line: { color: C.LINE, width: 1.5 } });
  H.card(s, 8.3, 1.62, 4.45, 4.9, C.PANEL);
  s.addText('Adoption, in numbers', { x: 8.6, y: 1.85, w: 3.9, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 8.62, 2.35, 3.9, 4.0, [
    { t: 'ChatGPT: 100M users in 2 months (2023) — fastest consumer ramp ever recorded; 900M+ weekly users by Feb 2026' },
    { t: 'Google Gemini app: 1B monthly users (Aug 2026)' },
    { t: '88% of organizations now use AI somewhere; generative AI ~70% (Stanford AI Index 2026)' },
    { t: 'But agent deployment is still single-digit % across most business functions — the gap is the opportunity', b: true },
  ], { size: 11.5, gap: 9 });
  s.addNotes(
    'HOW TO PRESENT — 1) Walk the timeline TOP TO BOTTOM, year by year, metronome pace — one line each. 2) Slow down only twice: 2022 (RLHF turned a predictor into an assistant people could use) and 2024 (models that think before answering). 3) Then the right card: read the adoption numbers and END on the bold line — “everyone chats with AI; almost nobody has industrialized delegation to agents. That gap is why you’re in this room.” 4) Bridge: “so what IS the thing under the hood?”\n' +
    'ACRONYMS — GPT = Generative Pre-trained Transformer (OpenAI’s model family name). RLHF = Reinforcement Learning from Human Feedback — people rank the model’s answers and it is tuned toward the preferred ones. o1 = OpenAI’s first reasoning model. R1 = DeepSeek’s open reasoning model.\n' +
    'CONTENT — Two beats: (1) everything since 2017 is one architecture, scaled; (2) adoption stats end on the tension — everyone chats with AI, almost nobody has industrialized delegation to agents yet. Learning to brief agents well now is a genuine head start. Sources: Reuters/UBS 2023, TechCrunch Feb 2026, Google Aug 2026, Stanford HAI AI Index 2026.');

  // ---------- 7. HOW AN LLM WORKS ----------
  s = H.slide('PART 1 · HOW LLMS WORK', 7);
  H.title(s, 'Under the hood', 'A prediction engine, sent to finishing school');
  const pipe = [
    ['database', '1 · Pretraining', 'Months, trillions of words: learn to predict the next token on internet-scale text. Language, facts, and reasoning patterns compress into billions of learned weights.'],
    ['list', '2 · Instruction tuning', 'Curated example dialogues teach it to follow instructions and answer questions — instead of just continuing your text.'],
    ['thumbsup', '3 · Human feedback (RLHF)', 'People rank outputs; the model is tuned toward helpful, honest, harmless. This step turned raw predictors into assistants — and made ChatGPT possible.'],
  ];
  pipe.forEach((p, i) => {
    const x = 0.55 + i * 4.18;
    H.card(s, x, 1.7, 3.95, 3.0, C.PANEL);
    H.iconCircle(s, x + 0.28, 1.95, 0.55, p[0], C.TEAL);
    s.addText(p[1], { x: x + 0.28, y: 2.62, w: 3.4, h: 0.4, fontFace: F.head, fontSize: 14.5, bold: true, color: C.INK, margin: 0 });
    s.addText(p[2], { x: x + 0.28, y: 3.05, w: 3.42, h: 1.55, fontFace: F.body, fontSize: 10.8, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.08 });
    if (i < 2) H.arrow(s, x + 3.97, 3.15, 0.2, C.TEAL);
  });
  H.callout(s, 0.55, 5.0, 6.0, 1.6, C.TEAL_TINT, [
    { text: 'Knowledge is frozen at the cutoff. ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12.5, breakLine: true } },
    { text: 'Training ends months before release; the model recalls patterns, it doesn’t look things up. Anything newer needs web search or your documents in the prompt.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'clock', iconFill: C.TEAL, size: 12 });
  H.callout(s, 6.75, 5.0, 6.0, 1.6, C.AMBER_TINT, [
    { text: 'Why prompting exists: ', options: { bold: true, color: C.INK, fontSize: 12.5, breakLine: true } },
    { text: 'the model completes your text. The prompt is the only steering wheel you have — everything it knows about your task, audience, and standards must be in it.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'compass', iconFill: C.AMBER, size: 12 });
  s.addNotes(
    'HOW TO PRESENT — 1) Open with the title metaphor: “a prediction engine, sent to finishing school.” 2) Walk the three cards LEFT TO RIGHT — pretraining, instruction tuning, human feedback; the arrows are the assembly line. One plain sentence each. 3) Then the two bottom callouts, LEFT first: knowledge freezes at the cutoff — anything newer must be brought to it. 4) RIGHT callout last, read slowly: “Why prompting exists” — this is the thesis sentence of the entire course; let it sit for a beat. 5) Bridge: “six concepts, quick — starting with what the model actually reads.”\n' +
    'ACRONYMS — RLHF = Reinforcement Learning from Human Feedback — card 3 on this slide.\n' +
    'CONTENT — “Autocomplete trained on the internet; RLHF is the finishing school.” The right-hand callout is the thesis of the whole course: prompting matters because the prompt is the entire interface. InstructGPT fact worth telling: raters preferred a well-tuned 1.3B model over raw 175B GPT-3 — tuning beat 100x scale.');

  // ---------- 8. TOKENS ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 8);
  H.title(s, 'Concept 1 · Tokens', 'The model reads bricks, not letters');
  H.bullets(s, 0.55, 1.7, 6.2, 3.0, [
    { t: 'Text is chopped into tokens — word chunks from a fixed vocabulary. Common words are one token; rare ones get built from pieces (“ham·bur·ger”).' },
    { t: 'Rules of thumb (English): 1 token ≈ 4 characters ≈ ¾ of a word. A 50-page document ≈ 25–35K tokens.' },
    { t: 'The model never sees letters — “strawberry” arrives as one or two IDs. That’s why letter-counting and character-exact edits fail: it’s working from hearing, not spelling.', b: true },
    { t: 'Everything is priced and limited in tokens — input and output. Output tokens cost ~5× input, because generation is serial.' },
  ], { size: 12.5, gap: 9 });
  H.card(s, 7.0, 1.7, 5.75, 2.6, C.PANEL);
  s.addText('LEGO bricks of text', { x: 7.3, y: 1.92, w: 5.2, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
  s.addText('Common words are pre-molded bricks; unusual words get assembled from smaller pieces. You pay by the brick, not by the sentence — and the builder has never seen inside a brick.', { x: 7.3, y: 2.38, w: 5.2, h: 1.0, fontFace: F.body, fontSize: 11.5, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.1 });
  // one chip per token — the sentence as the model receives it
  const chips = [['Analyzing', 0.95], ['the', 0.45], ['supplier', 0.85], ['’s', 0.3], ['first', 0.55], ['-', 0.22], ['pass', 0.55], ['yield', 0.6]];
  let cx = 7.3;
  chips.forEach((ch, i) => {
    s.addShape('roundRect', { x: cx, y: 3.44, w: ch[1], h: 0.36, rectRadius: 0.06, fill: { color: i % 2 ? 'FFFFFF' : C.TEAL_TINT }, line: { color: C.TEAL, width: 0.75 } });
    s.addText(ch[0], { x: cx, y: 3.45, w: ch[1], h: 0.34, align: 'center', valign: 'middle', fontFace: 'Consolas', fontSize: 9.5, color: C.TEAL_DARK, margin: 0 });
    cx += ch[1] + 0.06;
  });
  s.addText('eight bricks — the model receives eight numbered IDs, not forty letters', { x: 7.3, y: 3.9, w: 5.2, h: 0.3, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0 });
  H.callout(s, 7.0, 4.55, 5.75, 2.0, C.TEAL_TINT, [
    { text: 'So what, for daily work: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12.5, breakLine: true } },
    { text: 'paste-heavy prompts burn budget and context fast · non-English and dense technical text cost more tokens · use AI for language, software for characters (counts, checksums, exact IDs).', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'layers', iconFill: C.TEAL, size: 12 });
  H.callout(s, 0.55, 5.3, 6.2, 1.25, C.PANEL, [
    { text: 'Try it once: ', options: { bold: true, color: C.INK, fontSize: 11.5 } },
    { text: 'paste a paragraph of your own text into any online tokenizer (search “OpenAI tokenizer”) and watch it break into bricks. Thirty seconds — you’ll never forget it.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'zap', iconFill: C.SLATE, size: 11.5, line: C.LINE });
  s.addNotes(
    'HOW TO PRESENT — 1) Title first: “the model reads bricks, not letters.” 2) Left bullets top to bottom; STOP on the bold third bullet and tell the strawberry story there — it cannot count the r’s because it never sees letters, only brick IDs. 3) Right card: point at the brick strip — “this is exactly how your sentence arrives: eight bricks, eight numbers.” 4) Bottom-right teal card: the three daily-work consequences. 5) Bottom-left card: the 30-second homework (tokenizer). 6) Bridge: “if text is bricks — how many bricks fit on the desk?”\n' +
    'ACRONYMS — ID = identifier — to the model each token is just a number. K = thousand (25–35K tokens).\n' +
    'CONTENT — The strawberry-letter-counting failure is famous — explain the mechanism (it never sees letters) so the audience can predict this class of failure, not just memorize one example. Token math preview: it also explains context windows (next slide) and pricing.');

  // ---------- 9. CONTEXT WINDOW ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 9);
  H.title(s, 'Concept 2 · Context window', 'A desk, not a filing cabinet');
  H.bullets(s, 0.55, 1.65, 6.2, 2.9, [
    { t: 'The context window is working memory for one conversation: your question, the system prompt, chat history, attached files, and search results must all fit on the desk.' },
    { t: 'Close the chat and the desk is swept clean. Nothing persists unless a memory feature or a saved file re-loads it.' },
    { t: 'By Aug 2026, ~1M tokens (≈1,500 pages) is the flagship standard — Claude, GPT-5.x, Gemini, and the Chinese open-weight flagships alike. Consumer apps often enforce smaller limits than the raw model.' },
    { t: '“Fits on the desk” ≠ “gets read carefully”: accuracy is highest at the start and end of a long context and sags in the middle (“lost in the middle”).', b: true },
  ], { size: 12.5, gap: 8 });
  H.card(s, 7.0, 1.65, 5.75, 2.5, C.PANEL);
  s.addText('What’s on the desk right now', { x: 7.3, y: 1.85, w: 5.2, h: 0.4, fontFace: F.head, fontSize: 14.5, bold: true, color: C.INK, margin: 0 });
  const deskItems = [['file', 'System prompt & instructions'], ['chat', 'Every prior turn — both sides'], ['paperclip', 'Attached documents'], ['search', 'Tool & search results']];
  deskItems.forEach((d, i) => {
    const x = 7.3 + (i % 2) * 2.75; const y = 2.35 + Math.floor(i / 2) * 0.85;
    H.iconCircle(s, x, y, 0.4, d[0], C.SLATE);
    s.addText(d[1], { x: x + 0.52, y: y + 0.02, w: 2.2, h: 0.75, fontFace: F.body, fontSize: 10, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.0 });
  });
  H.callout(s, 7.0, 4.35, 5.75, 2.2, C.TEAL_TINT, [
    { text: 'Habits that exploit the desk: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12.5, breakLine: true } },
    { text: '① long documents at the TOP, question at the END — Anthropic measured up to ~30% better answers · ② label multiple documents clearly · ③ new topic → new chat: stale history pollutes attention · ④ very long thread → ask for a summary, carry it into a fresh chat.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'check', iconFill: C.TEAL, size: 12 });
  s.addNotes(
    'HOW TO PRESENT — 1) The analogy first: “the context window is a desk, not a filing cabinet.” 2) Left bullets top to bottom: everything must fit; the desk is swept when the chat closes; ~1M tokens is the 2026 standard; then the bold one — “fits on the desk” is not “gets read carefully” — draw the U-shape in the air (attention high at the start, sags in the middle, high at the end). 3) Right card: the four things sitting on the desk right now. 4) Teal card: read all four numbered habits — this is the practical payoff of the slide. 5) Bridge: “and what if what you need was never on the desk? RAG.”\n' +
    'ACRONYMS — 1M = one million (tokens ≈ 1,500 pages). GPT-5.x = OpenAI’s current model family.\n' +
    'CONTENT — The desk analogy carries the course. “Lost in the middle” is Liu et al. 2023 (TACL) — U-shaped accuracy by position; still true in modern long-context models for non-literal tasks. The 30% figure is Anthropic’s own long-context guidance. 1M-token standard verified Aug 2026 across Claude Fable/Sonnet 5, GPT-5.6, Gemini 3.1 Pro, DeepSeek V4, Qwen3.8, Kimi K3.');

  // ---------- 10. RAG ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 10);
  H.title(s, 'Concept 3 · RAG', 'An open-book exam — audit the librarian');
  s.addText('The problem RAG solves: the model’s knowledge is frozen and public; your work runs on private documents it has never seen — and must never be trained on.', { x: 0.55, y: 1.42, w: 12.2, h: 0.42, fontFace: F.body, fontSize: 13, color: C.SLATE, margin: 0 });
  const rag = [
    ['chat', '1 · Ask', 'Plain question: “What does the supplier agreement say about re-inspection?”'],
    ['search', '2 · Retrieve', 'Semantic search finds the most relevant passages — by meaning, not keywords.'],
    ['layers', '3 · Augment', 'Those passages are placed on the model’s desk, behind the scenes.'],
    ['check', '4 · Generate', 'The model answers from the supplied text — and cites where it looked.'],
  ];
  rag.forEach((st, i) => {
    const x = 0.55 + i * 3.19;
    H.card(s, x, 2.0, 2.85, 2.5, C.PANEL);
    H.iconCircle(s, x + 0.24, 2.22, 0.5, st[0], C.TEAL);
    s.addText(st[1], { x: x + 0.24, y: 2.85, w: 2.4, h: 0.35, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
    s.addText(st[2], { x: x + 0.24, y: 3.22, w: 2.42, h: 1.2, fontFace: F.body, fontSize: 10.2, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.05 });
    if (i < 3) H.arrow(s, x + 2.87, 3.15, 0.3, C.TEAL);
  });
  H.card(s, 0.55, 4.75, 6.0, 1.95, C.GREEN_TINT);
  s.addText([
    { text: 'Why enterprises build on it: ', options: { bold: true, color: C.INK, fontSize: 12, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'current (re-index a doc in minutes, no retraining) · checkable (citations to the exact passage) · private (retrieval feeds one answer; it teaches the model nothing) · access-aware (you only retrieve what you’re allowed to see).', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 0.85, y: 4.95, w: 5.5, h: 1.6, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.08 });
  H.card(s, 6.75, 4.75, 6.0, 1.95, C.RED_TINT);
  s.addText([
    { text: 'The failure mode to respect: ', options: { bold: true, color: C.RED, fontSize: 12, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'if retrieval fetches the wrong page — an outdated revision, a near-miss document — the model still writes a fluent, confident, cited answer from it. Bad retrieval = confident wrong answer. So: check the citation, not just the prose.', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 7.05, y: 4.95, w: 5.5, h: 1.6, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.08 });
  s.addNotes(
    'HOW TO PRESENT — 1) Expand the acronym ONCE — Retrieval-Augmented Generation — then switch to the analogy: an open-book exam. 2) Walk the four step cards LEFT TO RIGHT: ask → retrieve → augment → generate; the librarian fetches pages, the student writes the answer. 3) Green card: why enterprises build on it — current, checkable, private, access-aware. 4) Red card, slowly: the failure mode — if the librarian pulls the wrong page, the student still writes a fluent, confident, CITED answer. Say the rule: “check the citation, not the prose.” 5) Bridge: “when do you prompt, when do you retrieve, when do you fine-tune? The ladder.”\n' +
    'ACRONYMS — RAG = Retrieval-Augmented Generation.\n' +
    'CONTENT — Open-book exam analogy: the student still writes the answer, from pages a librarian fetched — if the librarian pulls rev B instead of rev D, the student confidently cites the wrong page. This is the engine behind internal assistants and Copilot-over-SharePoint. Retrieval ≠ training is the privacy point to repeat.');

  // ---------- 11. ESCALATION LADDER ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 11);
  H.title(s, 'Concept 4 · The escalation ladder', 'Prompt first, retrieve second, fine-tune last');
  const ladder = [
    ['edit', 'Prompting', 'Instructions to a skilled temp', 'Costs nothing, changes instantly, works on every model. Handles style, format, task framing, examples. Where 90% of value lives — this course.', C.TEAL_TINT],
    ['book', 'RAG / retrieval', 'Hand the temp your binder', 'Adds knowledge: current, private, citable. The answer changes when the binder changes. For facts the model can’t know.', C.PANEL],
    ['cpu', 'Fine-tuning', 'Send them to a training course', 'Changes the model’s weights: permanent habits — a house style, a niche format, a distilled small model. Slow, per-model, high maintenance. Rarely the answer for knowledge.', C.PANEL],
  ];
  ladder.forEach((l, i) => {
    const y = 1.7 + i * 1.62;
    H.card(s, 0.55, y, 12.2, 1.45, l[4]);
    H.iconCircle(s, 0.82, y + 0.42, 0.55, l[0], C.TEAL);
    s.addText([
      { text: l[1] + ' — ', options: { bold: true, color: C.INK, fontSize: 14 } },
      { text: l[2], options: { italic: true, color: C.TEAL_DARK, fontSize: 12.5, breakLine: true, paraSpaceAfter: 3 } },
      { text: l[3], options: { color: C.SLATE, fontSize: 11 } },
    ], { x: 1.55, y: y + 0.12, w: 11.0, h: 1.25, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.06 });
  });
  s.addNotes(
    'HOW TO PRESENT — 1) The rule IS the title — say it: “prompt first, retrieve second, fine-tune last.” 2) Walk the three rungs TOP TO BOTTOM; let the temp analogies carry it: instructions to a skilled temp → hand them your binder → send them to a training course. 3) Point at rung 1’s highlight: “90% of the value lives here — that is this course.” 4) Bridge: “two concepts left: models that think, and models that make things up.”\n' +
    'ACRONYMS — RAG = Retrieval-Augmented Generation (rung 2).\n' +
    'CONTENT — v1.1: embeddings sidebar cut — if asked how retrieval finds things: every text gets a coordinate in meaning-space; nearby = similar, even with no shared words. Escalation rule: cheapest and most reversible first. When someone proposes “let’s fine-tune on our procedures,” the first question is: knowledge problem (→RAG) or behavior problem (→maybe fine-tune)? Most enterprise cases are knowledge problems. Frontier flagships mostly aren’t fine-tunable anyway (as of Aug 2026); open-weight models are.');

  // ---------- 12. REASONING MODELS ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 12);
  H.title(s, 'Concept 5 · Reasoning models', 'Buying the model time to think — when it’s worth it');
  H.bullets(s, 0.55, 1.7, 6.2, 3.4, [
    { t: 'Since OpenAI’s o1 (2024): models can draft, check, and revise internally before answering — spending extra compute at answer time on hard problems.' },
    { t: 'By 2026 it’s adaptive, not a separate product: flagships decide how long to think, and you can set effort (fast → extended thinking).' },
    { t: 'The bill: thinking tokens are charged as output tokens — the expensive kind — and add seconds to minutes. A hard question can quietly cost 5–20× a simple one.', b: true },
    { t: 'System 1 vs System 2: fast intuition for routine asks; slow deliberation for the problems where being wrong is expensive.' },
  ], { size: 12.5, gap: 9 });
  H.card(s, 7.0, 1.7, 5.75, 2.3, C.GREEN_TINT);
  s.addText([
    { text: 'Turn thinking ON for: ', options: { bold: true, color: C.INK, fontSize: 12.5, breakLine: true, paraSpaceAfter: 4 } },
    { text: 'multi-step analysis · math and anything numeric · root-cause reasoning · code · weighing tradeoffs across a long document · drafting the plan an agent will execute.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { x: 7.3, y: 1.9, w: 5.2, h: 1.95, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.1 });
  H.card(s, 7.0, 4.25, 5.75, 2.3, C.AMBER_TINT);
  s.addText([
    { text: 'Skip it for: ', options: { bold: true, color: C.INK, fontSize: 12.5, breakLine: true, paraSpaceAfter: 4 } },
    { text: 'lookups · reformatting · summaries · routine drafting. You pay in time and tokens for deliberation you don’t need — and (Part 3 preview) “think step by step” prompts are now often redundant: the model already does.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { x: 7.3, y: 4.45, w: 5.2, h: 1.95, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.1 });
  s.addNotes(
    'HOW TO PRESENT — 1) Frame: “since 2024 you can buy the model time to think — the question is when it’s worth it.” 2) Left bullets top to bottom: o1 started it; by 2026 it’s adaptive with an effort dial; then the BILL (bold) — thinking tokens are the expensive kind, a hard question quietly costs 5–20× a simple one; System 1 vs System 2 as the human parallel. 3) Right cards: green = turn it ON for this list; amber = skip it for that list. Read both lists briskly. 4) Bridge: “last concept — the one everyone asks about first.”\n' +
    'ACRONYMS — o1 = OpenAI’s first reasoning model (2024). System 1 / System 2 = Kahneman’s fast-intuition vs slow-deliberation framing (not an acronym, but say the source if asked).\n' +
    'CONTENT — Reasoning models are what make reliable agents feasible — planning quality is the bottleneck for multi-step work. Note the honest caveat: the model isn’t literally “thinking”; it generates intermediate tokens that improve the final answer. The cost asymmetry surprises people: budget reasoning like you budget an engineer’s deep-work time.');

  // ---------- 13. HALLUCINATION ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 13);
  H.title(s, 'Concept 6 · Hallucination', 'Fluency is not evidence');
  H.bullets(s, 0.55, 1.7, 6.2, 3.6, [
    { t: 'The mechanism: models are optimized for the most plausible next token, not the most true one. Fluency and truth usually coincide — except where training data is thin: rare facts, exact citations, numbers, names.' },
    { t: 'OpenAI’s own 2025 research: hallucination is a statistically expected result of standard training — benchmarks reward confident guessing over “I don’t know,” so models learn to be good test-takers.', b: true },
    { t: 'The assertive tone carries no information about reliability. An improv actor never breaks character — the show must go on, so gaps get filled with the most plausible line.' },
  ], { size: 12.5, gap: 10 });
  const cures = [
    ['book', 'Ground it', 'Give it the source: attach the document, use RAG/search — answering from supplied text beats free recall.'],
    ['eye', 'Cite it', 'Demand citations and an “I don’t know” escape hatch: “If the text doesn’t say, say so.”'],
    ['check', 'Verify it', 'Check what matters before it ships: quotes, numbers, clauses, anything regulatory. Your domain knowledge is the safety net.'],
  ];
  cures.forEach((cu, i) => {
    const y = 1.7 + i * 1.65;
    H.card(s, 7.0, y, 5.75, 1.5, i === 2 ? C.TEAL_TINT : C.PANEL);
    H.iconCircle(s, 7.25, y + 0.42, 0.5, cu[0], C.TEAL);
    s.addText([
      { text: cu[1], options: { bold: true, color: C.INK, fontSize: 13, breakLine: true, paraSpaceAfter: 2 } },
      { text: cu[2], options: { color: C.SLATE, fontSize: 10.8 } },
    ], { x: 7.9, y: y + 0.12, w: 4.65, h: 1.3, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.07 });
  });
  H.callout(s, 0.55, 5.6, 6.2, 1.0, C.RED_TINT, [
    { text: 'House rule: ', options: { bold: true, color: C.RED, fontSize: 12.5 } },
    { text: 'every uncited standard clause, date, number, or quote is a draft until verified.', options: { color: C.SLATE, fontSize: 12.5 } },
  ], { iconName: 'alert', iconFill: C.RED, size: 12 });
  s.addNotes(
    'HOW TO PRESENT — 1) The title is the sermon: “fluency is not evidence.” 2) Left bullets top to bottom: the mechanism (most PLAUSIBLE next token, not most true); the bold OpenAI 2025 finding — the vendor itself says benchmarks reward confident guessing; the improv-actor analogy (never breaks character, fills gaps with the most plausible line). 3) Right cards top to bottom: Ground it → Cite it → Verify it — one line each. 4) Red band: read the house rule VERBATIM — it is policy, not advice. 5) Bridge: “that closes the concepts — a three-minute rep, then the tool landscape.”\n' +
    'ACRONYMS — RAG = Retrieval-Augmented Generation (Ground-it card).\n' +
    'CONTENT — The OpenAI 2025 paper (“Why language models hallucinate”) is a gift for this slide: the vendor itself explains that eval incentives reward guessing. None of the three cures eliminates hallucination — they convert unverifiable claims into verifiable ones. This closes Part 1; Part 2 is the tool landscape.');

  // ---------- P1 REP (v1.1, skippable) ----------
  s = H.slide('THREE-MINUTE REP · PART 1', 14);
  H.title(s, 'Three-minute rep', 'Spot the missing elements');
  H.repTimer(s);
  H.card(s, 0.55, 1.75, 7.4, 3.4, C.PANEL);
  s.addText('The prompt on the screen:', { x: 0.85, y: 2.0, w: 6.6, h: 0.35, fontFace: F.body, fontSize: 12, bold: true, color: C.SLATE, margin: 0 });
  s.addText('“Analyze the returns data and make it look good for leadership.”', { x: 0.85, y: 2.45, w: 6.7, h: 0.7, fontFace: 'Consolas', fontSize: 15, color: C.TEAL_DARK, margin: 0, lineSpacingMultiple: 1.15 });
  H.bullets(s, 0.9, 3.35, 6.6, 1.7, [
    'One minute, on your own: what would you need to add before trusting the answer?',
    'Two minutes, together: name the missing pieces out loud.',
  ], { size: 12.5, gap: 8 });
  H.card(s, 8.25, 1.75, 4.5, 3.4, C.AMBER_TINT);
  s.addText([
    { text: 'For the debrief (presenter only)', options: { bold: true, color: C.AMBER, fontSize: 11.5, breakLine: true, paraSpaceAfter: 5 } },
    { text: 'Missing: the actual question (which metric, which period, vs what?) · the audience and their time · a length/format contract · permission to say what the data can’t answer · “compute, don’t estimate.”', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 8.52, y: 1.95, w: 3.95, h: 3.0, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.12 });
  s.addText('Skippable if running long — the same diagnosis returns in Part 3.', { x: 0.55, y: 5.45, w: 12.2, h: 0.35, fontFace: F.body, fontSize: 10.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT — 1) Point at the 3:00 badge: “three minutes, by the clock.” 2) Read the on-screen prompt aloud, deadpan — let its vagueness land. 3) One minute of silence: what would YOU need to add before trusting the answer? 4) Two minutes collecting answers out loud; the amber card is your debrief key — don’t show your hand early. 5) Do NOT teach the elements yet — say exactly this: “every gap you just named is an element with a name in Part 3,” and move on.\n' +
    'ACRONYMS — none on this slide.\n' +
    'CONTENT — Three minutes, hard cap. The point is the felt experience of a vague prompt — every gap they name is an element from Part 3. Skip freely if behind schedule.');
};