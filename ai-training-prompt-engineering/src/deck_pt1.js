// PART I — Primer: where this came from, how it works (v1.5)
const { C, F } = require('./deck_lib');

module.exports = function buildPartOne(pres, H) {
  // ---------- 1. TITLE ----------
  let s = H.slide(null, null, { dark: true });
  s.addText('EMPLOYEE TRAINING · SEPTEMBER 2026', { x: 0.55, y: 1.0, w: 8, h: 0.35, fontFace: F.body, fontSize: 13, bold: true, charSpacing: 3, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('From Prompts to Agents', { x: 0.55, y: 1.4, w: 12.2, h: 1.05, fontFace: F.head, fontSize: 54, bold: true, color: C.ON_DARK, margin: 0 });
  s.addText('A focused course on prompt engineering — for generative AI you talk to,\nand agentic AI you delegate to.', { x: 0.55, y: 2.55, w: 10.5, h: 0.85, fontFace: F.body, fontSize: 16, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  const cols = [
    ['THE PRIMER', 'History & core concepts', 'four eras of AI · tokens · context windows · RAG · the token economy · hallucination'],
    ['THE CRAFT', 'Prompt engineering', 'the universal anatomy · seven elements · seven techniques · what the evidence says'],
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
    'HOW TO PRESENT —\n' +
    '1) Have this up as people arrive; don’t read it to them.\n' +
    '2) Open with the name and the one-liner: “This is a course about one skill — prompting — in two modes: generative AI you talk to, and agentic AI you delegate to.”\n' +
    '3) Sweep the three cards left to right as the journey: the primer, the craft, the leap.\n' +
    '4) Point at the footer line: every example is generic — no company data anywhere in the material.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Before the map — why this one skill is worth your time.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'AI = Artificial Intelligence (defined once here; it recurs on nearly every slide).\n' +
    'RAG = Retrieval-Augmented Generation — the model fetches passages from your documents before answering; taught properly in Part 1.\n' +
    '\n' +
    'CONTENT —\n' +
    'This training goes deeper than the general AI onboarding: it is specifically about prompting — the skill — across two modes: generative (AI that talks) and agentic (AI that works).\n' +
    'Everything is dated September 2026 because this field moves monthly.');

  // ---------- 2. WELCOME + MAP ----------
  s = H.slide('WELCOME', 2);
  H.title(s, 'Welcome', 'Ask, or delegate — prompting does both');
  H.bullets(s, 0.55, 1.6, 6.1, 2.1, [
    { t: 'Prompting is the one AI skill that transfers everywhere: every assistant, every vendor, every year. Models change monthly; the craft compounds.', b: true },
    { t: 'The same skill has two modes. Generative: you ask, it writes, you act. Agentic: you brief it, it plans, uses tools, checks itself, and delivers.' },
    { t: 'Each mode needs a different kind of prompt — that distinction is the backbone of this training.' },
  ], { size: 12, gap: 7 });
  H.callout(s, 0.55, 3.82, 6.1, 1.28, C.TEAL_TINT, [
    { text: 'The 10-second version: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12, breakLine: true } },
    { text: 'a generative prompt describes what to write.\nAn agentic prompt describes a job to run — goal, inputs, checks, and when to stop and ask you.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'zap', iconFill: C.TEAL, size: 11.5 });
  H.promptChip(s, 0.55, 5.25, 6.1, 1.62, 1,
    'This chat is my course log. Entry 1, same request two ways: a farewell card for a coworker. First, just write it. Then don’t write it — draft the job brief instead: goal, inputs you need from me, checks, when to stop and ask.',
    { label: 'Two modes, felt — opens your course log', size: 9 });
  H.card(s, 7.0, 1.55, 5.75, 2.95, C.PANEL);
  s.addText('The map — three blocks, six parts', { x: 7.3, y: 1.78, w: 5.2, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
  s.addText([
    { text: 'BLOCK 1 · FOUNDATIONS', options: { bold: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true, paraSpaceAfter: 2 } },
    { text: '1 · The primer — how this actually works\n2 · Models & tools — the landscape', options: { color: C.SLATE, fontSize: 10.5, breakLine: true, paraSpaceAfter: 7 } },
    { text: 'BLOCK 2 · THE CRAFT', options: { bold: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true, paraSpaceAfter: 2 } },
    { text: '3 · Prompt engineering — anatomy + techniques\n4 · The playbook — live demos & templates', options: { color: C.SLATE, fontSize: 10.5, breakLine: true, paraSpaceAfter: 7 } },
    { text: 'BLOCK 3 · DELEGATION', options: { bold: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true, paraSpaceAfter: 2 } },
    { text: '5 · Agentic prompting — the mission brief\n6 · Prompts as assets · wrap-up', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { x: 7.3, y: 2.2, w: 5.2, h: 2.25, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.08 });
  H.callout(s, 7.0, 4.66, 5.75, 1.7, C.AMBER_TINT, [
    { text: 'You leave with: ', options: { bold: true, color: C.INK, fontSize: 11.5, breakLine: true } },
    { text: 'a working AI vocabulary · a tool map · the universal prompt anatomy + seven techniques · a 13-template library with an interactive Template Creator · the Prompt Element Taxonomy reference (your parts catalog) · team conventions for storing and versioning prompts.', options: { color: C.SLATE, fontSize: 10.8 } },
  ], { iconName: 'download', iconFill: C.AMBER, size: 11 });
  s.addText('This course teaches the text wing. Image, video and audio prompting have their own dials — same discipline, different controls; with enough interest, that becomes its own training.', { x: 7.0, y: 6.48, w: 5.75, h: 0.5, fontFace: F.body, fontSize: 9, italic: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 1.05 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Say the bold line first: “Prompting is the one AI skill that transfers everywhere — every assistant, every vendor, every year.”\n' +
    '2) Walk the three left bullets top to bottom; land on “two modes” as the backbone of the whole training.\n' +
    '3) Teal card: read the 10-second version VERBATIM — it is the thesis.\n' +
    '4) Map card: read the three block names and six parts quickly — no clock talk.\n' +
    '5) Amber card: the take-homes; physically hold up the handout pack here so people know things are coming home with them.\n' +
    '6) Footer aside, one sentence: this is the TEXT wing of prompting; image/video/audio have their own dials — a possible future training.\n' +
    '\n' +
    'TRY IT — PROMPT 1/8 (opens the course log)\n' +
    'Everyone runs the chip prompt in whatever AI window they have open, in ONE chat they will keep all course — their course log.\n' +
    'Debrief line: the card ran on guesses (invented names, bracketed blanks); the brief asked YOU questions.\n' +
    'Recovery (a model asks questions both times): “guessing and bracketing are generative mode; asking is the agentic move — the brief just makes it happen on purpose.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'LLM = Large Language Model — the text engine behind every assistant in this course.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.5: title simplified to the ask-or-delegate example; durations removed from the map (three blocks, expandable — timing lives in the presenter plan, not on slides).\n' +
    'The multimodal aside is deliberate and brief: the Prompt Report counts 58 text techniques plus 40 for other modalities — a separate training if votes call for it.\n' +
    'Parts 3, 5 and 6 carry the hands-on moments; the eight numbered PROMPT exercises run in the trainees’ own AI window throughout — the thread doubles as their take-home course log.');

  // ---------- 3. PART I DIVIDER ----------
  s = H.slide(null, 3, { dark: true });
  H.partMarker(s, 1);
  s.addText('PART 1 · THE PRIMER', { x: 0.55, y: 2.3, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('Where this came from,\nand how it actually works', { x: 0.55, y: 2.8, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('Seventy years in two slides, then the six concepts that make you fluent: tokens, context, RAG, the escalation ladder, the token economy, hallucination.', { x: 0.55, y: 4.85, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Dividers are pacing: breathe. Read the two-line title, nothing more.\n' +
    '2) Point at the progress bar top-left: “six parts — this is where we are” (the bar returns on every divider).\n' +
    '3) Set expectations in one sentence: “Two history slides, then six concepts — the concepts are the vocabulary for everything after.”\n' +
    '4) Under 30 seconds, then advance.\n' +
    '\n' +
    'ACRONYMS —\n' +
    'RAG = Retrieval-Augmented Generation (in the subtitle; it gets its own slide shortly).');

  // ---------- 4. FOUR ERAS ----------
  s = H.slide('PART 1 · A SHORT HISTORY', 4);
  H.title(s, 'Seventy years in one slide', 'Four eras: rules → learning → generative → agentic');
  const eras = [
    ['edit', 'Rules', '1950s–1990s · symbolic AI, expert systems', 'Humans hand-code the logic: “if X then Y.” Expert systems (MYCIN, XCON) shine, then crack — rules can’t cover messy reality. Hype outruns results twice: the “AI winters.”', C.PANEL],
    ['chart', 'Learning', '1990s–2010s · machine learning, neural networks', 'Stop writing rules — let the system find patterns in examples. Spam filters, search, recommendations. 2012: deep nets + GPUs crush image recognition (AlexNet: 15.3% error vs 26.2%).', C.PANEL],
    ['brain', 'Generative', '2017– · transformers, LLMs', 'The Transformer (2017) lets models train on the whole internet. Predict-the-next-word at that scale writes, summarizes, codes. ChatGPT makes it a product (2022).', C.TEAL_TINT],
    ['robot', 'Agentic', '2024– · reasoning models, tool use', 'Models get “arms”: tools, browsers, files, code. Reasoning models plan multi-step work; agents execute it with limited supervision. The frontier now.', C.TEAL_TINT],
  ];
  eras.forEach((e, i) => {
    const x = 0.55 + i * 3.19;
    H.card(s, x, 1.7, 2.95, 3.72, e[4]);
    H.iconCircle(s, x + 0.24, 1.92, 0.5, e[0], C.TEAL);
    s.addText(e[1], { x: x + 0.86, y: 1.94, w: 2.05, h: 0.34, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
    s.addText(e[2], { x: x + 0.86, y: 2.27, w: 2.05, h: 0.42, fontFace: F.body, fontSize: 8.2, bold: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 0.98 });
    // schematic mini-diagram strip
    const gx = x + 0.3, gy = 2.82;
    const box = (bx, by, bw, label, tint) => {
      s.addShape('roundRect', { x: bx, y: by, w: bw, h: 0.22, rectRadius: 0.04, fill: { color: tint || 'FFFFFF' }, line: { color: C.TEAL, width: 0.75 } });
      if (label) s.addText(label, { x: bx, y: by, w: bw, h: 0.22, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 6.5, color: C.TEAL_DARK, margin: 0 });
    };
    if (i === 0) { // decision tree
      box(gx + 0.78, gy, 0.8, 'if…?');
      box(gx + 0.08, gy + 0.4, 0.8, 'then A'); box(gx + 1.5, gy + 0.4, 0.8, 'else B');
      s.addShape('line', { x: gx + 1.05, y: gy + 0.22, w: -0.55, h: 0.18, line: { color: C.TEAL, width: 1 } });
      s.addShape('line', { x: gx + 1.32, y: gy + 0.22, w: 0.55, h: 0.18, line: { color: C.TEAL, width: 1 } });
    } else if (i === 1) { // tiny neural net
      const L1 = [0, 0.22, 0.44], L2 = [0.11, 0.33];
      L1.forEach(dy => L2.forEach(dy2 => s.addShape('line', { x: gx + 0.3, y: gy + dy + 0.07, w: 0.85, h: dy2 - dy, line: { color: C.LINE, width: 0.9 } })));
      L2.forEach(dy2 => s.addShape('line', { x: gx + 1.3, y: gy + dy2 + 0.07, w: 0.75, h: 0.15 - dy2 + 0.07, line: { color: C.LINE, width: 0.9 } }));
      L1.forEach(dy => s.addShape('ellipse', { x: gx + 0.16, y: gy + dy, w: 0.15, h: 0.15, fill: { color: C.TEAL }, line: { type: 'none' } }));
      L2.forEach(dy => s.addShape('ellipse', { x: gx + 1.16, y: gy + dy, w: 0.15, h: 0.15, fill: { color: C.TEAL }, line: { type: 'none' } }));
      s.addShape('ellipse', { x: gx + 2.06, y: gy + 0.22, w: 0.15, h: 0.15, fill: { color: C.AMBER }, line: { type: 'none' } });
    } else if (i === 2) { // next-word prediction
      box(gx, gy + 0.2, 0.55, 'The'); box(gx + 0.6, gy + 0.2, 0.6, 'audit'); box(gx + 1.25, gy + 0.2, 0.4, 'is');
      s.addShape('line', { x: gx + 1.68, y: gy + 0.31, w: 0.25, h: 0, line: { color: C.TEAL, width: 1.25, endArrowType: 'triangle' } });
      s.addShape('roundRect', { x: gx + 1.98, y: gy + 0.2, w: 0.42, h: 0.22, rectRadius: 0.04, fill: { color: C.TEAL }, line: { type: 'none' } });
      s.addText('…?', { x: gx + 1.98, y: gy + 0.2, w: 0.42, h: 0.22, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 7, bold: true, color: 'FFFFFF', margin: 0 });
    } else { // agent loop
      box(gx, gy + 0.08, 0.68, 'PLAN'); box(gx + 0.86, gy + 0.08, 0.62, 'ACT'); box(gx + 1.66, gy + 0.08, 0.74, 'CHECK');
      s.addShape('line', { x: gx + 0.7, y: gy + 0.19, w: 0.14, h: 0, line: { color: C.TEAL, width: 1, endArrowType: 'triangle' } });
      s.addShape('line', { x: gx + 1.5, y: gy + 0.19, w: 0.14, h: 0, line: { color: C.TEAL, width: 1, endArrowType: 'triangle' } });
      s.addShape('line', { x: gx + 0.34, y: gy + 0.48, w: 1.72, h: 0, line: { color: C.TEAL, width: 1, beginArrowType: 'triangle' } });
    }
    s.addText(e[3], { x: x + 0.24, y: 3.52, w: 2.5, h: 1.82, fontFace: F.body, fontSize: 9.9, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.07 });
    if (i < 3) H.arrow(s, x + 2.97, 3.45, 0.2, C.TEAL);
  });
  H.callout(s, 0.55, 5.6, 12.2, 1.05, C.AMBER_TINT, [
    { text: 'Why the last decade exploded — scaling laws (2020): ', options: { bold: true, color: C.INK, fontSize: 12.5 } },
    { text: 'bigger model + more data + more compute = predictably better results. Progress stopped being a research gamble and became an investment roadmap.', options: { color: C.SLATE, fontSize: 12.5 } },
  ], { iconName: 'trend', iconFill: C.AMBER });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame it: “Seventy years in one slide — as four eras.”\n' +
    '2) Walk the four cards LEFT TO RIGHT. For each: name the era, point at the little diagram (a hand-written rulebook → a net that learns from examples → a machine that predicts the next word → a loop that plans, acts and checks itself), then one sentence of story.\n' +
    '3) Pause once, on “AI winters” in card 1: over-promising collapsed funding twice — skepticism about AI is historically earned.\n' +
    '4) Close on the amber band: scaling laws turned progress from a research gamble into an investment roadmap.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Zoom into the decade that changed work.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'GPU = Graphics Processing Unit — the graphics chip class that turned out to be perfect for training neural networks (AlexNet, 2012).\n' +
    'LLM = Large Language Model.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.5: each era card now names its technologies (owner request) and carries a schematic mini-diagram — mechanism sketches, not data charts (owner choice).\n' +
    'Say the diagrams plainly: rules = a decision tree someone typed; learning = little circles passing signals, tuned from examples; generative = predict the next word-brick; agentic = plan → act → check, then loop.\n' +
    'The eras framing is a teaching synthesis — present it as “a useful way to see 70 years,” not official taxonomy.\n' +
    'The rules era = writing the SOP yourself; the learning era = deriving the SOP from a thousand examples. (SOP = Standard Operating Procedure.)');

  // ---------- 5. THE GENERATIVE DECADE ----------
  s = H.slide('PART 1 · A SHORT HISTORY', 5);
  H.title(s, 'The decade that changed work', 'Each leap has a name — 2017 → 2026');
  const tl = [
    ['2017', 'The Transformer', '“Attention Is All You Need” (Google) — the architecture behind every model since'],
    ['2020', 'Scaling laws + few-shot', 'GPT-3: show examples in the prompt, it does the task — prompt engineering is born'],
    ['2022', 'Instruction tuning + RLHF', 'human feedback turns a predictor into an assistant; ChatGPT hits 100M users in 2 months'],
    ['2024', 'Reasoning models', 'OpenAI o1 “thinks” before answering — compute spent at answer time, not just training'],
    ['2025', 'MoE + distillation + open weights', 'DeepSeek R1: frontier ability gets radically cheaper; big models teach small ones'],
    ['2026', 'Agentic harnesses', 'Claude Code · Cowork-class agents bring delegation to general office work'],
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
  s.addText('The speed of adoption', { x: 8.6, y: 1.85, w: 3.9, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
  s.addText('Months to reach 100 million users — shorter bar = faster', { x: 8.6, y: 2.28, w: 3.9, h: 0.5, fontFace: F.body, fontSize: 10, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.05 });
  H.hbar(s, 8.6, 3.0, 3.9, 'ChatGPT', 2 / 30, '2 mo', C.TEAL, { labW: 1.15, b: true });
  H.hbar(s, 8.6, 3.5, 3.9, 'TikTok', 9 / 30, '~9 mo', C.SLATE, { labW: 1.15 });
  H.hbar(s, 8.6, 4.0, 3.9, 'Instagram', 30 / 30, '~30 mo', C.SLATE, { labW: 1.15 });
  s.addText('Fastest consumer ramp ever recorded at launch (UBS/Reuters, 2023).', { x: 8.6, y: 4.55, w: 3.9, h: 0.55, fontFace: F.body, fontSize: 9, italic: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('The methods on the left are the vocabulary for the whole course — each returns on a later slide.', { x: 8.6, y: 5.35, w: 3.9, h: 0.95, fontFace: F.body, fontSize: 10, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.1 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Walk the timeline TOP TO BOTTOM, year by year, metronome pace — say the METHOD name in bold each time; these six names are course vocabulary.\n' +
    '2) Slow down twice: 2022 (RLHF — people ranked the model’s answers until a predictor became an assistant) and 2024 (models that think before answering).\n' +
    '3) Right card: one beat — ChatGPT reached 100 million users in two months; TikTok took nine, Instagram two and a half years.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“So what IS the thing under the hood?”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'GPT = Generative Pre-trained Transformer (OpenAI’s model family name).\n' +
    'RLHF = Reinforcement Learning from Human Feedback — people rank the model’s answers and it is tuned toward the preferred ones.\n' +
    'MoE = Mixture of Experts — a model built huge but waking only a fraction per question (defined properly in Part 2).\n' +
    'o1 = OpenAI’s first reasoning model. R1 = DeepSeek’s open reasoning model.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.5: adoption card replaced with the single honest chart (time-to-100M, one source: UBS/Reuters 2023). A multi-company user-growth line is NOT buildable honestly — vendors report different metrics (weekly vs monthly actives vs downloads).\n' +
    'Kept for you, not the slide: 88% of organizations now use AI somewhere (Stanford AI Index 2026) — but agent deployment is still single-digit % across most business functions. Everyone chats with AI; almost nobody has industrialized delegation. That gap is why this room matters.\n' +
    'Vendor benchmark and adoption numbers are marketing until independently reproduced — treat them as claims.');

  // ---------- 6. HOW AN LLM WORKS ----------
  s = H.slide('PART 1 · HOW LLMS WORK', 6);
  H.title(s, 'Under the hood', 'A prediction engine, sent to finishing school');
  const pipe = [
    ['database', '1 · Pretraining', 'Months, trillions of words: learn to predict the next token on internet-scale text. Language, facts, and reasoning patterns compress into billions of learned weights.'],
    ['list', '2 · Instruction tuning', 'Curated example dialogues teach it to follow instructions and answer questions — instead of just continuing your text.'],
    ['thumbsup', '3 · Human feedback (RLHF)', 'People rank outputs; the model is tuned toward helpful, honest, harmless. This step turned raw predictors into assistants — and made ChatGPT possible.'],
  ];
  pipe.forEach((p, i) => {
    const x = 0.55 + i * 4.18;
    H.card(s, x, 1.62, 3.95, 2.75, C.PANEL);
    H.iconCircle(s, x + 0.28, 1.84, 0.52, p[0], C.TEAL);
    s.addText(p[1], { x: x + 0.28, y: 2.46, w: 3.4, h: 0.38, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
    s.addText(p[2], { x: x + 0.28, y: 2.86, w: 3.42, h: 1.42, fontFace: F.body, fontSize: 10.3, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.06 });
    if (i < 2) H.arrow(s, x + 3.97, 3.0, 0.2, C.TEAL);
  });
  H.callout(s, 0.55, 4.52, 6.0, 1.32, C.TEAL_TINT, [
    { text: 'Knowledge is frozen at the cutoff. ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12, breakLine: true } },
    { text: 'Training ends months before release; the model recalls patterns, it doesn’t look things up. Anything newer needs web search or your documents in the prompt.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'clock', iconFill: C.TEAL, size: 11.5 });
  H.callout(s, 6.75, 4.52, 6.0, 1.32, C.AMBER_TINT, [
    { text: 'Why prompting exists: ', options: { bold: true, color: C.INK, fontSize: 12, breakLine: true } },
    { text: 'the model completes your text — the prompt is the only steering wheel you have. A complete prompt doesn’t make the model smarter: it deletes wrong guesses.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'compass', iconFill: C.AMBER, size: 11.5 });
  H.promptChip(s, 0.55, 6.0, 12.2, 1.05, 2,
    'Send 1: Finish this sentence 5 different ways: “We should move the launch date because”   ·   Send 2: Now 5 more ways, knowing: B2B software firm, competitor launches May 3, our beta ends April 20. What changed?',
    { label: 'Narrowing the guesses — two separate sends', size: 9 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Open with the title metaphor: “a prediction engine, sent to finishing school.”\n' +
    '2) Walk the three cards LEFT TO RIGHT — pretraining, instruction tuning, human feedback; the arrows are the assembly line. One plain sentence each.\n' +
    '3) LEFT callout: knowledge freezes at the cutoff — anything newer must be brought to it.\n' +
    '4) RIGHT callout, read slowly — it is the thesis of the entire course: the prompt is the only steering wheel, and a complete prompt doesn’t make the model smarter — it DELETES WRONG GUESSES. Let that sit for a beat.\n' +
    '\n' +
    'TRY IT — PROMPT 2/8 (two sends, in the course log)\n' +
    'Send 1 scatters: budget, staffing, quality, weather. Send 2 orbits May 3 and April 20.\n' +
    'Debrief line: “Grade the directions, not the sentences — your facts didn’t add intelligence, they deleted wrong guesses.”\n' +
    'That is the invisible probability distribution, made countable on their own screen.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Six concepts, quick — starting with what the model actually reads.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'RLHF = Reinforcement Learning from Human Feedback — card 3 on this slide.\n' +
    '\n' +
    'CONTENT —\n' +
    '“Autocomplete trained on the internet; RLHF is the finishing school.”\n' +
    'InstructGPT fact worth telling: raters preferred a well-tuned 1.3B model over raw 175B GPT-3 — tuning beat 100x scale.');

  // ---------- 7. TOKENS ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 7);
  H.title(s, 'Concept 1 · Tokens', 'The model reads bricks, not letters');
  H.bullets(s, 0.55, 1.66, 6.2, 2.95, [
    { t: 'Text is chopped into tokens — word chunks from a fixed vocabulary. Common words are one token; rare ones get built from pieces (“ham·bur·ger”).' },
    { t: 'Rules of thumb (English): 1 token ≈ 4 characters ≈ ¾ of a word. A 50-page document ≈ 25–35K tokens.' },
    { t: 'The model never sees letters — “strawberry” arrives as one or two IDs. That’s why letter-counting and character-exact edits fail: it’s working from hearing, not spelling.', b: true },
    { t: 'Everything is priced and limited in tokens — input and output. Output tokens cost ~5× input, because generation is serial.' },
  ], { size: 11.8, gap: 8 });
  H.card(s, 7.0, 1.66, 5.75, 2.55, C.PANEL);
  s.addText('LEGO bricks of text', { x: 7.3, y: 1.88, w: 5.2, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
  s.addText('Common words are pre-molded bricks; unusual words get assembled from smaller pieces. You pay by the brick — and the builder has never seen inside a brick.', { x: 7.3, y: 2.34, w: 5.2, h: 0.85, fontFace: F.body, fontSize: 11, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.08 });
  const chips = [['Analyzing', 0.95], ['the', 0.45], ['supplier', 0.85], ['’s', 0.3], ['first', 0.55], ['-', 0.22], ['pass', 0.55], ['yield', 0.6]];
  let cx = 7.3;
  chips.forEach((ch, i) => {
    const fillCol = i % 2 ? 'FFFFFF' : C.TEAL_TINT;
    // LEGO studs on top of each brick
    const nStuds = ch[1] > 0.5 ? 2 : 1;
    for (let st = 0; st < nStuds; st++) {
      const sx = cx + (ch[1] / (nStuds + 1)) * (st + 1) - 0.05;
      s.addShape('roundRect', { x: sx, y: 3.32, w: 0.1, h: 0.1, rectRadius: 0.02, fill: { color: fillCol }, line: { color: C.TEAL, width: 0.75 } });
    }
    s.addShape('roundRect', { x: cx, y: 3.4, w: ch[1], h: 0.36, rectRadius: 0.04, fill: { color: fillCol }, line: { color: C.TEAL, width: 0.75 } });
    s.addText(ch[0], { x: cx, y: 3.41, w: ch[1], h: 0.34, align: 'center', valign: 'middle', fontFace: 'Consolas', fontSize: 9.5, color: C.TEAL_DARK, margin: 0 });
    cx += ch[1] + 0.06;
  });
  s.addText('eight bricks — the model receives eight numbered IDs, not forty letters', { x: 7.3, y: 3.85, w: 5.2, h: 0.3, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0 });
  H.callout(s, 7.0, 4.35, 5.75, 1.55, C.TEAL_TINT, [
    { text: 'So what, for daily work: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5, breakLine: true } },
    { text: 'paste-heavy prompts burn budget and context fast · non-English and dense technical text cost more tokens · use AI for language, software for characters (counts, checksums, exact IDs).', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'layers', iconFill: C.TEAL, size: 11 });
  H.promptChip(s, 0.55, 4.85, 6.2, 2.0, 3,
    'You don’t read letters — you read tokens: chunks of text, like LEGO bricks. Teach me this in under 150 words, like I’m a new office colleague. 1) Chop this sentence into token-style chunks, putting | between chunks (a rough split is fine): “Our quarterly onboarding checklist is ready.” 2) One short sentence each: (a) why letter-counting can go wrong for you; (b) what to ask you FIRST when I need letter-perfect work; (c) why tokens are what I pay for and what fills your memory of our chat. Plain language.',
    { label: 'Bricks, not letters', size: 8.6 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Title first: “the model reads bricks, not letters.”\n' +
    '2) Left bullets top to bottom; STOP on the bold third bullet and tell the strawberry story there — models famously miscounted the r’s in “strawberry” because they never see letters, only brick IDs. (Tell it as a story — current models have memorized that one, so don’t run it live.)\n' +
    '3) Right card: point at the brick strip — “this is exactly how your sentence arrives: eight bricks, eight numbers.” The studs are decoration; the chunk boundaries are the point.\n' +
    '4) Teal card: the three daily-work consequences.\n' +
    '\n' +
    'TRY IT — PROMPT 3/8 (course log)\n' +
    'Everyone runs the chip prompt. Point at the | marks on a few screens: that is what the AI actually sees.\n' +
    'Recovery (splits differ across the room, or the model hedges that its split is approximate): “that IS the lesson — every vendor has its own brick set; the bricks are always there, the letters never are.”\n' +
    'Bonus: the prompt itself models good form — structured request, word cap, plain-language constraint.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“If text is bricks — how many bricks fit on the desk?”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'ID = identifier — to the model each token is just a number.\n' +
    'K = thousand (25–35K tokens).\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.5: the tokenizer homework card became PROMPT 3/8 — teach-first: the model explains the concept with one worked example; no capability stunt that a 2026 model would pass and thereby teach the opposite.\n' +
    'Token math preview: it also explains context windows (next slide) and pricing (two slides ahead).');

  // ---------- 8. CONTEXT WINDOW ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 8);
  H.title(s, 'Concept 2 · Context window', 'A desk, not a filing cabinet');
  H.bullets(s, 0.55, 1.62, 6.2, 2.75, [
    { t: 'The context window is working memory for one conversation: your question, the system prompt, chat history, attached files, and search results must all fit on the desk.' },
    { t: 'Close the chat and the desk is swept clean. Nothing persists unless a memory feature or a saved file re-loads it.' },
    { t: 'By 2026, ~1M tokens (≈1,500 pages) is the flagship standard. Consumer apps often enforce smaller limits than the raw model.' },
    { t: '“Fits on the desk” ≠ “gets read carefully”: accuracy is highest at the start and end of a long context and sags in the middle (“lost in the middle”).', b: true },
  ], { size: 11.5, gap: 7 });
  H.card(s, 7.0, 1.62, 5.75, 2.4, C.PANEL);
  s.addText('What’s on the desk right now', { x: 7.3, y: 1.8, w: 5.2, h: 0.4, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
  const deskItems = [['file', 'System prompt & instructions'], ['chat', 'Every prior turn — both sides'], ['paperclip', 'Attached documents'], ['search', 'Tool & search results']];
  deskItems.forEach((d, i) => {
    const x = 7.3 + (i % 2) * 2.75; const y = 2.28 + Math.floor(i / 2) * 0.82;
    H.iconCircle(s, x, y, 0.38, d[0], C.SLATE);
    s.addText(d[1], { x: x + 0.5, y: y + 0.01, w: 2.2, h: 0.72, fontFace: F.body, fontSize: 9.8, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.0 });
  });
  H.callout(s, 7.0, 4.16, 5.75, 1.28, C.TEAL_TINT, [
    { text: 'Habits that exploit the desk: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true } },
    { text: '① long documents at the TOP, question at the END (~30% better answers) · ② label multiple documents · ③ new topic → new chat · ④ long thread → run the handoff move below.', options: { color: C.SLATE, fontSize: 10.2 } },
  ], { iconName: 'check', iconFill: C.TEAL, size: 10.5 });
  H.card(s, 0.55, 4.5, 6.2, 0.94, C.AMBER_TINT);
  s.addText([
    { text: 'A desk with a filing cabinet? ', options: { bold: true, color: C.INK, fontSize: 11 } },
    { text: 'Persistent files, notes and standing instructions are exactly what agentic tools bolt onto the desk — Part 5.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { x: 0.85, y: 4.6, w: 5.7, h: 0.76, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.05 });
  H.promptChip(s, 0.55, 5.58, 12.2, 1.5, 4,
    'One day this chat gets too long, or I close it — and your desk is swept clean. Boil our course thread so far into a handoff note titled HANDOFF 4/8, under 80 words (shorter is fine): everything a brand-new chat would need to continue my training — what course this is, which numbered exercises I’ve done, what comes next. Under the note, two plain sentences: what happens to everything here the moment this chat closes? Last line: what would you need to remember me across chats? Just name it — we get there in Part 5.',
    { label: 'The handoff note — the habit, performed', size: 8.8 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) The analogy first: “the context window is a desk, not a filing cabinet.”\n' +
    '2) Left bullets top to bottom; on the bold one, draw the U-shape in the air — attention high at the start, sags in the middle, high at the end.\n' +
    '3) Right card: the four things sitting on the desk right now.\n' +
    '4) Teal card: the four numbered habits — habit ④ is about to be performed, not described.\n' +
    '5) Amber card: one sentence only — the filing-cabinet teaser for Part 5. Plant the seed, move on.\n' +
    '\n' +
    'TRY IT — PROMPT 4/8 (course log)\n' +
    'Everyone runs the handoff prompt in the same thread — one send, one window.\n' +
    'Homework line: “tonight, paste your HANDOFF into a brand-new chat, ask ‘Where was I?’, and watch it pick up your course mid-stream.”\n' +
    'Recovery (note runs long or skips an exercise): “you just watched a long thread sag in the middle — the very reason we write handoff notes before we need them; reply ‘add Exercise X and trim to 80 words’.”\n' +
    'If someone’s fresh chat knows things they never pasted: “your tool has a filing cabinet bolted to the desk — hold that thought for Part 5.”\n' +
    '\n' +
    'BRIDGE —\n' +
    '“And what if what you need was never on the desk? RAG.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    '1M = one million (tokens ≈ 1,500 pages).\n' +
    '\n' +
    'CONTENT —\n' +
    '“Lost in the middle” = Liu et al. 2023 (TACL) — U-shaped accuracy by position. The ~30% figure is Anthropic’s own long-context guidance (docs at top, query at end).\n' +
    '1M-token flagship standard verified Aug 2026 across Claude, GPT-5.x, Gemini, and the Chinese open-weight flagships.\n' +
    'v1.5: the old two-window version of this exercise was cut — one send, one window; the felt proof moved to homework.');

  // ---------- 9. RAG ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 9);
  H.title(s, 'Concept 3 · RAG', 'An open-book exam — audit the librarian');
  s.addText('The problem RAG solves: the model’s knowledge is frozen and public; your work runs on private documents it has never seen — and must never be trained on.', { x: 0.55, y: 1.42, w: 12.2, h: 0.42, fontFace: F.body, fontSize: 12.5, color: C.SLATE, margin: 0 });
  const rag = [
    ['chat', '1 · Ask', 'Plain question: “What does the supplier agreement say about re-inspection?”'],
    ['search', '2 · Retrieve', 'Semantic search finds the most relevant passages — by meaning, not keywords.'],
    ['layers', '3 · Augment', 'Those passages are placed on the model’s desk, behind the scenes.'],
    ['check', '4 · Generate', 'The model answers from the supplied text — and cites where it looked.'],
  ];
  rag.forEach((st, i) => {
    const x = 0.55 + i * 3.19;
    H.card(s, x, 1.98, 2.85, 2.3, C.PANEL);
    H.iconCircle(s, x + 0.24, 2.18, 0.48, st[0], C.TEAL);
    s.addText(st[1], { x: x + 0.24, y: 2.76, w: 2.4, h: 0.35, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
    s.addText(st[2], { x: x + 0.24, y: 3.12, w: 2.42, h: 1.1, fontFace: F.body, fontSize: 9.8, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.04 });
    if (i < 3) H.arrow(s, x + 2.87, 3.0, 0.3, C.TEAL);
  });
  H.card(s, 0.55, 4.48, 6.0, 1.8, C.GREEN_TINT);
  s.addText([
    { text: 'Why enterprises build on it: ', options: { bold: true, color: C.INK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'current (re-index a doc in minutes, no retraining) · checkable (citations to the exact passage) · private (retrieval feeds one answer; it teaches the model nothing) · access-aware (you only retrieve what you’re allowed to see).', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { x: 0.85, y: 4.66, w: 5.5, h: 1.5, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.06 });
  H.card(s, 6.75, 4.48, 6.0, 1.8, C.RED_TINT);
  s.addText([
    { text: 'The failure mode to respect: ', options: { bold: true, color: C.RED, fontSize: 11.5, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'if retrieval fetches the wrong page — an outdated revision, a near-miss document — the model still writes a fluent, confident, cited answer from it. Bad retrieval = confident wrong answer. So: check the citation, not just the prose.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { x: 7.05, y: 4.66, w: 5.5, h: 1.5, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.06 });
  H.callout(s, 0.55, 6.42, 12.2, 0.62, C.TEAL_TINT, [
    { text: 'You already use this. ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5 } },
    { text: 'Our internal company assistant — the one where you upload documentation and “talk” to it — is RAG in production. Every step on this slide happens each time you ask it a question.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'home', iconFill: C.TEAL, size: 11 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Expand the acronym ONCE — Retrieval-Augmented Generation — then switch to the analogy: an open-book exam. A librarian fetches pages from YOUR documents; the student writes the answer from those pages.\n' +
    '2) Walk the four step cards LEFT TO RIGHT: ask → retrieve → augment → generate.\n' +
    '3) Green card: why enterprises build on it — current, checkable, private, access-aware.\n' +
    '4) Red card, slowly: the failure mode — if the librarian pulls the wrong page, the student still writes a fluent, confident, CITED answer. Say the rule: “check the citation, not the prose.”\n' +
    '5) Teal band: point at the room — “you’ve been running this loop all along”: the internal assistant where you upload documentation and talk to it IS this slide. (Keep it generic — no product or vendor names.)\n' +
    '\n' +
    'BRIDGE —\n' +
    '“When do you prompt, when do you retrieve, when do you fine-tune? The escalation ladder.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'RAG = Retrieval-Augmented Generation.\n' +
    '\n' +
    'CONTENT —\n' +
    'Retrieval ≠ training is the privacy point to repeat.\n' +
    'This is the engine behind internal document assistants and Copilot-over-SharePoint.');

  // ---------- 10. ESCALATION LADDER ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 10);
  H.title(s, 'Concept 4 · The escalation ladder', 'Prompt first, retrieve second, fine-tune last');
  const ladder = [
    ['edit', 'Prompting', 'instructions to a skilled temp', 'Free, instant, works on every model. Style, format, framing, examples. 90% of the value — this course.', C.TEAL_TINT],
    ['book', 'RAG / retrieval', 'hand the temp your binder', 'Adds knowledge: current, private, citable. For facts the model can’t know.', C.PANEL],
    ['cpu', 'Fine-tuning', 'send them to a training course', 'Changes the model’s habits permanently. Slow, per-model, high maintenance. Rarely the answer.', C.PANEL],
  ];
  ladder.forEach((l, i) => {
    const y = 1.62 + i * 1.08;
    H.card(s, 0.55, y, 6.0, 0.96, l[4]);
    H.iconCircle(s, 0.78, y + 0.24, 0.48, l[0], C.TEAL);
    s.addText([
      { text: l[1] + ' — ', options: { bold: true, color: C.INK, fontSize: 12.5 } },
      { text: l[2], options: { italic: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true, paraSpaceAfter: 2 } },
      { text: l[3], options: { color: C.SLATE, fontSize: 9.8 } },
    ], { x: 1.42, y: y + 0.08, w: 5.0, h: 0.82, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.03 });
  });
  H.callout(s, 0.55, 5.0, 6.0, 1.6, C.AMBER_TINT, [
    { text: 'One question triages everything: ', options: { bold: true, color: C.INK, fontSize: 12, breakLine: true } },
    { text: 'is the AI missing knowledge, or misbehaving with knowledge it already has? Missing → retrieve. Misbehaving → prompt. A deep habit that must hold at huge volume, with no room to paste instructions → fine-tune (rare).', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'help', iconFill: C.AMBER, size: 11.5 });
  H.promptChip(s, 6.75, 1.62, 6.0, 4.98, 5,
    'Course log — Escalation Ladder triage drill. Show me the six problems below as a numbered list, then STOP and wait. I’ll answer each with P (better prompt), R (retrieval) or F (fine-tune). Then grade me in under 150 words — rule: missing or outdated knowledge → R · has what it needs but acts wrong → P · deep habit at huge volume → F. Count defensible answers correct. End with my score and the one question to ask before choosing a rung.\n1 Product descriptions never match our three-bullet brand-voice guide.\n2 Confidently answers vacation-policy questions — with last year’s rules.\n3 Support replies are accurate but twice as long as anyone reads.\n4 Can’t answer “what did we decide in the March pricing review?” — it’s all in our meeting notes.\n5 A dictation tool garbles a specialty’s spoken shorthand thousands of times a day; no pasted document changes how it hears.\n6 Our review AI must apply a 40-page internal rubric to every contract — pasting it crowds out the contract itself.',
    { label: 'The triage drill — you sort, it grades', size: 8.8 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) The rule IS the title — say it: “prompt first, retrieve second, fine-tune last.”\n' +
    '2) Walk the three rungs TOP TO BOTTOM; let the temp analogies carry it: instructions to a skilled temp → hand them your binder → send them to a training course.\n' +
    '3) Amber card — the generic power of the ladder: ONE question triages any AI disappointment: missing knowledge, or misbehaving with knowledge it has? Cheapest and most reversible fix first.\n' +
    '\n' +
    'TRY IT — PROMPT 5/8 (course log; the trainees commit BEFORE the model grades — the learning is model-proof)\n' +
    'Answers: 1 P (behavior trap that looks like training) · 2 R (stale knowledge) · 3 P · 4 R (private knowledge) · 5 F (legitimate) · 6 defensible either way — the debrief centerpiece.\n' +
    'Debrief line: “Who put F on number 6? Defend it — notice every argument comes down to the one question on the amber card. That question is the whole ladder.”\n' +
    'Recovery (model blurts answers past the STOP): “cover the screen, sort the six on paper, then scroll back and argue with it — a grader that can’t wait for your diagnosis is exactly why the diagnosis has to live in your head.”\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Two concepts left — and they’re both about the bill.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'RAG = Retrieval-Augmented Generation (rung 2).\n' +
    '\n' +
    'CONTENT —\n' +
    'When someone proposes “let’s fine-tune on our procedures,” the first question is: knowledge problem (→RAG) or behavior problem (→maybe fine-tune)? Most enterprise cases are knowledge problems.\n' +
    'Frontier flagships mostly aren’t fine-tunable anyway (as of 2026); open-weight models are.\n' +
    'If asked how retrieval finds things: every text gets a coordinate in meaning-space; nearby = similar, even with no shared words.\n' +
    'NOTE: this is the ESCALATION ladder (capability). Part 6 has a different ladder — the PROMOTION ladder (where prompts live). Name them fully to avoid collision.');

  // ---------- 11. FAST vs THINKING (Concept 5 · 1 of 2) ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 11);
  H.title(s, 'Concept 5 · Fast models vs thinking models', 'Two speeds, one bill (1 of 2)');
  H.bullets(s, 0.55, 1.66, 6.2, 2.85, [
    { t: 'Every vendor ships a fast tier — one pass, instant, cheap — and a thinking tier that drafts, checks and revises internally before answering (compute spent at answer time).' },
    { t: 'System 1 vs System 2: fast intuition for routine asks; slow deliberation where being wrong is expensive.' },
    { t: 'The bill: thinking tokens are charged as output tokens — the expensive kind. A hard question can quietly cost 5–20× a simple one.', b: true },
    { t: 'Why the fast tier got so good: models built huge but waking only a fraction per question (MoE — Part 2 tells that story), and big models teaching small ones (distillation).' },
  ], { size: 11.5, gap: 7 });
  H.card(s, 0.55, 4.68, 6.2, 0.9, C.GREEN_TINT);
  s.addText([
    { text: 'Think ON: ', options: { bold: true, color: C.INK, fontSize: 11 } },
    { text: 'multi-step analysis · math · root-cause work · code · tradeoffs across a long document · planning an agent’s job.', options: { color: C.SLATE, fontSize: 10.2 } },
  ], { x: 0.85, y: 4.78, w: 5.7, h: 0.72, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.04 });
  H.card(s, 0.55, 5.68, 6.2, 0.9, C.AMBER_TINT);
  s.addText([
    { text: 'Think OFF: ', options: { bold: true, color: C.INK, fontSize: 11 } },
    { text: 'lookups · reformatting · summaries · routine drafting — you’d pay time and tokens for deliberation you don’t need.', options: { color: C.SLATE, fontSize: 10.2 } },
  ], { x: 0.85, y: 5.78, w: 5.7, h: 0.72, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.04 });
  H.promptChip(s, 7.0, 1.66, 5.75, 4.95, 6,
    'Course log — Fast answers vs careful answers. Five colleagues — Ana, Ben, Chloe, Dev, Ema — present Monday–Friday, one per day. Rules: Ana not Monday · Dev the day right after Ana · Ema on Tuesday or Wednesday · Ben earlier in the week than Chloe · Chloe the day right before Ema.\nPART 1 — FAST: your instant answer — five names with days, one line, nothing else.\nPART 2 — CAREFUL: now solve it as if it really mattered — step by step, check every rule, state your final answer. Under 250 words.\nPART 3 — THE BILL: estimate the word count of each part. If every word cost the same, how many times more expensive was the careful version? Did your two answers agree? One sentence: when is fast enough — and when is it not?',
    { label: 'Same brain, two speeds', size: 9 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “every AI app sells you two speeds — the question is when the slow one is worth its bill.”\n' +
    '2) Left bullets top to bottom; the BILL bullet is the one to slow on: thinking is billed like output — the expensive kind — and a hard question quietly costs 5–20× a simple one.\n' +
    '3) Green/amber cards: when to switch thinking on, when to skip it. Escalate on failure, not by default.\n' +
    '\n' +
    'TRY IT — PROMPT 6/8 (course log; unique solution: Ben Mon · Chloe Tue · Ema Wed · Ana Thu · Dev Fri — check screens at a glance)\n' +
    'Debrief line: “Shout your multiple — most of you paid 10–20× for the careful pass; that is exactly how the thinking tier bills you.”\n' +
    'Recovery (fast answer already right): “you didn’t beat the exercise — you caught the pricing: modern models often deliberate quietly even before the ‘instant’ line.”\n' +
    'The exercise is designed NOT to need the fast answer to be wrong — either outcome teaches.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“That’s the two speeds. Now the whole menu — where your tokens actually go.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'MoE = Mixture of Experts — defined properly in Part 2 (the DeepSeek slide).\n' +
    'System 1 / System 2 = Kahneman’s fast-intuition vs slow-deliberation framing.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.5: replaces “Concept 5 · Reasoning models” — reframed from one vendor’s spending story to the generic token economy (owner request). Split into two slides; this is mechanics + cost.\n' +
    'Facts: thinking tokens billed as output even when you only see a summary; output ≈ 5× input across vendors; effort is adaptive/dial-able by 2026 (vendor effort settings are primary-sourced in notes/research/t4_choice_enums.md §5).\n' +
    'Honest caveat: the model isn’t literally “thinking” — it generates intermediate tokens that improve the final answer.');

  // ---------- 12. THE FEATURE MENU (Concept 5 · 2 of 2) ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 12);
  H.title(s, 'Concept 5 · The feature menu', 'Where your tokens go (2 of 2)');
  H.card(s, 0.55, 1.62, 5.9, 3.3, C.PANEL);
  s.addText('The cost ladder — every vendor sells it', { x: 0.85, y: 1.8, w: 5.3, h: 0.38, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  const ladder2 = [
    ['Quick answer', '1×', 'one pass, instant'],
    ['Thinking / extended reasoning', '5–20×', 'drafts and checks before answering'],
    ['Web search', '+sources', 'grounds the answer in live pages'],
    ['Deep research', '100×+', 'browses for minutes, returns a cited report'],
    ['Agent modes', 'the most', 'plans and acts across many steps for you'],
  ];
  ladder2.forEach((r, i) => {
    const y = 2.28 + i * 0.52;
    s.addShape('roundRect', { x: 0.85 + i * 0.14, y, w: 2.55, h: 0.42, rectRadius: 0.06, fill: { color: i >= 3 ? C.TEAL : C.TEAL_TINT }, line: { color: C.TEAL, width: 0.75 } });
    s.addText(r[0], { x: 0.9 + i * 0.14, y: y + 0.01, w: 2.45, h: 0.4, fontFace: F.body, fontSize: 8.6, bold: true, color: i >= 3 ? 'FFFFFF' : C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText([
      { text: r[1] + '  ', options: { bold: true, color: C.AMBER, fontSize: 10 } },
      { text: r[2], options: { color: C.SLATE, fontSize: 9 } },
    ], { x: 4.08, y: y + 0.01, w: 2.3, h: 0.4, fontFace: F.body, margin: 0, valign: 'middle' });
  });
  H.card(s, 6.6, 1.62, 6.15, 3.3, C.PANEL);
  s.addText('What it’s called where you are (Sep 2026)', { x: 6.88, y: 1.8, w: 5.6, h: 0.38, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  const modeNames = [
    ['ChatGPT', 'deep research · thinking slider (paid) · “Think” button (free)'],
    ['Gemini', 'Deep Research (all tiers) · Deep Think = separate hard-reasoning mode (Ultra)'],
    ['Claude', 'Research (paid plans) · extended thinking'],
    ['Copilot', 'Quick response · Think Deeper · Smart (GPT-5) · Researcher agent'],
    ['Perplexity', 'Search · Research · Create files and apps'],
  ];
  modeNames.forEach((m, i) => {
    const y = 2.3 + i * 0.52;
    s.addText(m[0], { x: 6.88, y, w: 1.3, h: 0.46, fontFace: F.body, fontSize: 10.5, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText(m[1], { x: 8.25, y, w: 4.35, h: 0.46, fontFace: F.body, fontSize: 9, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.98 });
  });
  s.addText('Deep research, demystified: a reasoning model given a browser and time — it plans, reads sources for minutes, and synthesizes a cited report. The MoE story in Part 2 is why that became affordable.', { x: 0.55, y: 5.02, w: 12.2, h: 0.42, fontFace: F.body, fontSize: 10.5, italic: true, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.05 });
  H.promptChip(s, 0.55, 5.5, 12.2, 1.55, 7,
    'Course log — The feature menu. You are the product I’m typing into right now. List the answer modes and major features this product offers me — quick answer, deeper-thinking mode, web search, a deep-research mode that browses for minutes, any agent mode. Only what really exists today. A tight table, max 6 rows: what it’s called here · what it does differently behind the scenes · rough effort vs a quick answer (1×, 5–20×, 100×+) · one task where it’s the smallest mode that succeeds · one task where it’s overkill · where I switch it on — say “unsure” rather than guess. End with a one-sentence rule for picking the smallest mode that can succeed.',
    { label: 'Ask your own product for its menu', size: 8.8 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Left card: climb the staircase bottom-left to top-right — 1× quick answer, 5–20× thinking, search adds sources, 100×+ deep research, agent modes most of all. The discipline in the subtitle: pick the SMALLEST mode that can succeed; escalate deliberately.\n' +
    '2) Right card: the same ladder under five brand names — read one row, gesture over the rest. Copilot users: your everyday menu is the fourth row.\n' +
    '3) Italic line: deep research demystified — a reasoning model with a browser and time. Cited report out; big token bill in.\n' +
    '\n' +
    'TRY IT — PROMPT 7/8 (course log; self-updating — the answer regenerates the day any vendor renames a button)\n' +
    'Debrief line: “Read your column 1 aloud around the room — four different menus, one identical 1×/20×/100× ladder. You didn’t memorize this chart; you asked for it.”\n' +
    'Recovery (model misstates its own toggles/plans): “meta-prompting’s fine print — it knows what its modes DO far better than where the buttons live; keep the ladder, verify the toggles with your own eyes.”\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Last concept — the one everyone asks about first.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'MoE = Mixture of Experts (Part 2).\n' +
    '\n' +
    'CONTENT —\n' +
    'Mode names verified Sep 9, 2026 (notes/research/ + vendor help pages): ChatGPT deep research + thinking-effort slider (Sol) / Think button (Luna); Gemini Deep Research all tiers (free ~5 reports/mo) vs Deep Think (Ultra reasoning mode — a different thing); claude.ai Research (paid); Copilot Quick response / Think Deeper / Smart (GPT-5) + Researcher agent (consumer Deep Research retired); Perplexity Search / Research / Create files and apps. [REFRESH QUARTERLY — names churn.]\n' +
    'Scaling anecdote for questions: one prompt to a fast model vs an orchestrated multi-agent research run = hundreds of quick answers’ worth of tokens — the sessions that built this course are a live example.\n' +
    '(Part 3 preview) “think step by step” is now often redundant — the expired-advice slide in Part 3 handles it.');

  // ---------- 13. HALLUCINATION — WHAT & KINDS (Concept 6 · 1 of 2) ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 13);
  H.title(s, 'Concept 6 · Hallucination', 'Fluency is not evidence (1 of 2)');
  H.bullets(s, 0.55, 1.66, 6.1, 4.6, [
    { t: 'The mechanism: models are optimized for the most plausible next token, not the most true one. Fluency and truth usually coincide — except where training data is thin: rare facts, exact citations, numbers, names.' },
    { t: 'OpenAI’s own 2025 research: hallucination is a statistically expected result of standard training — benchmarks reward confident guessing over “I don’t know,” so models learn to be good test-takers.', b: true },
    { t: 'The better word is confabulation: the model isn’t seeing things — it fills gaps with plausible material, in-format. Fake citations LOOK like citations; fake URLs look like URLs.' },
    { t: 'Think of an improv actor who never breaks character: the show must go on, so gaps get filled with the most plausible line — delivered with total confidence.' },
  ], { size: 11.8, gap: 9 });
  const kinds = [
    ['1 · Invented facts', 'Free recall where data was thin — a confident wrong fact. (The Bard telescope flub, next slide.)'],
    ['2 · Invented sources', 'Citations, cases, book titles that look perfectly real — and don’t exist. (The ChatGPT lawyer.)'],
    ['3 · Confidently wrong from a bad source', 'Fluent, cited — and built on a joke or the wrong revision. (Glue on pizza.)'],
    ['4 · Runs with your false premise', 'It assumes your prompt is true: feed it a wrong “fact” and it builds on it politely.'],
  ];
  kinds.forEach((k, i) => {
    const y = 1.66 + i * 1.24;
    H.card(s, 6.85, y, 5.9, 1.12, i === 2 ? C.RED_TINT : C.PANEL);
    s.addText([
      { text: k[0], options: { bold: true, color: i === 2 ? C.RED : C.TEAL_DARK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 2 } },
      { text: k[1], options: { color: C.SLATE, fontSize: 10 } },
    ], { x: 7.12, y: y + 0.08, w: 5.4, h: 0.98, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.04 });
  });
  s.addText('Four kinds — one root: the show must go on. The next slide is what that cost in public.', { x: 0.55, y: 6.6, w: 12.2, h: 0.35, fontFace: F.body, fontSize: 10.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) The title is the sermon: “fluency is not evidence.”\n' +
    '2) Left bullets top to bottom: the mechanism (most PLAUSIBLE next token, not most true); the bold OpenAI 2025 finding — the vendor itself says benchmarks reward confident guessing; the vocabulary upgrade — CONFABULATION: filling gaps with plausible material, in-format; the improv-actor analogy, said plainly: an improv actor never breaks character — gaps get filled with the most plausible line.\n' +
    '3) Right cards top to bottom: the four kinds, one line each — each names the public incident that’s coming on the next slide.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“What does that look like in public? The hall of shame.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none new on this slide.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.5: expanded to two slides (owner request: define hallucination more, name the kinds, then the public examples).\n' +
    'The four kinds are a teaching frame grounded in the research notes (self-delusion/snowballing, in-format guessing, bad-retrieval, truth bias — r10_library_b.md, r2_concepts.md, r14) — not claimed as an academic taxonomy.\n' +
    'OpenAI 2025 = “Why language models hallucinate” (arXiv:2509.04664) — eval incentives reward guessing over abstaining.');

  // ---------- 14. HALLUCINATION — HALL OF SHAME (Concept 6 · 2 of 2) ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 14);
  H.title(s, 'Concept 6 · The hall of shame', 'Real, public, verified — and all avoidable (2 of 2)');
  const shame = [
    ['alert', 'Glue on pizza · May 2024', 'Google’s AI search told users to put glue in pizza sauce and eat a rock a day — it had read a joke forum comment and a satire article as advice. Global mockery; the feature was scaled back within days.'],
    ['gavel', 'The ChatGPT lawyer · Jun 2023', 'A New York lawyer filed six court cases that didn’t exist — then asked ChatGPT whether they were real. It said yes. $5,000 sanction, apology letters ordered (Mata v. Avianca).'],
    ['send', 'Air Canada’s chatbot · Feb 2024', 'The website bot invented a bereavement refund policy. A tribunal made the airline honor it — rejecting the claim that the bot was “a separate legal entity.” Your company owns what its chatbot says.'],
    ['chart', 'The Big Four arc · 2025–26', 'Deloitte refunded a government report over invented citations; EY pulled a report with 16 of 27 references fake; KPMG’s report on agentic-AI excellence had 5 of 45 citations check out.'],
  ];
  shame.forEach((r, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.62 + Math.floor(i / 2) * 1.68;
    H.card(s, x, y, 5.95, 1.56, C.PANEL);
    H.iconCircle(s, x + 0.2, y + 0.2, 0.44, r[0], i === 0 ? C.AMBER : C.RED);
    s.addText([
      { text: r[1], options: { bold: true, color: C.INK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 3 } },
      { text: r[2], options: { color: C.SLATE, fontSize: 9.7 } },
    ], { x: x + 0.78, y: y + 0.1, w: 5.0, h: 1.4, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.04 });
  });
  H.callout(s, 0.55, 5.12, 12.2, 0.55, C.AMBER_TINT, [
    { text: 'Not one-offs: ', options: { bold: true, color: C.INK, fontSize: 11 } },
    { text: 'a legal tracker counted ~1,500 court decisions worldwide involving AI-fabricated citations by mid-2026.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'scale', iconFill: C.AMBER, size: 11 });
  H.callout(s, 0.55, 5.8, 12.2, 0.55, C.TEAL_TINT, [
    { text: 'The cure hasn’t changed: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11 } },
    { text: 'Ground it (give it the source) · Cite it (demand receipts + an “I don’t know” escape hatch) · Verify it (check what matters before it ships).', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'check', iconFill: C.TEAL, size: 11 });
  H.callout(s, 0.55, 6.48, 12.2, 0.55, C.RED_TINT, [
    { text: 'House rule: ', options: { bold: true, color: C.RED, fontSize: 11 } },
    { text: 'every uncited standard clause, date, number, or quote is a draft until verified.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'alert', iconFill: C.RED, size: 11 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Walk the four cards — let the room laugh at glue-on-pizza, then take the temperature down card by card.\n' +
    '2) Glue on pizza, said plainly: someone posted a JOKE on a forum; the AI read the joke as advice and served it as a real answer — kind 3 from the last slide.\n' +
    '3) The lawyer: he checked the fabrication WITH the fabricator — “are these real?” — “yes.” That is why verification must be OUTSIDE the tool.\n' +
    '4) Air Canada: small money (~CA$800), giant precedent — your company owns what its chatbot says.\n' +
    '5) The Big Four arc lands hardest in a corporate room: three global consultancies, three AI-fabricated-source scandals in nine months — the last one a report ABOUT doing AI well.\n' +
    '6) Amber band: ~1,500 court decisions — the lawyer was not a one-off. Then teal: the cure — Ground it, Cite it, Verify it. Then the red house rule VERBATIM — it is policy, not advice.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“That closes the concepts — now, the tool landscape.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none new on this slide.\n' +
    '\n' +
    'CONTENT —\n' +
    'All incidents verified with sources and dates in notes/research/r14_hallucination_incidents.md — including phrasing caveats.\n' +
    'Reserve incidents for questions (also in r14): Bard’s launch flub (~$100B market drop that day — phrase carefully: the error PLUS a weak launch event drove it) · Chicago Sun-Times fake summer reading list (10 of 15 books didn’t exist) · the invented Turley scandal · mayor Brian Hood (THREATENED the first defamation suit; never filed) · Michael Cohen’s fake Bard citations (NOT sanctioned — no bad faith) · NYC MyCity chatbot advising law-breaking · Whisper inventing sentences in hospital transcription (AP).\n' +
    'None of the three cures eliminates hallucination — they convert unverifiable claims into verifiable ones.');
};
