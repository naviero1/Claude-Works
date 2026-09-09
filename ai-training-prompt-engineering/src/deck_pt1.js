// PART I — Primer (v1.6: R10 prompt chips, owner-audit rounds 1–2, audit fixes)
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
    'This training goes deeper than the general AI onboarding: it is specifically about prompting — the skill — across two modes.\n' +
    'Everything is dated September 2026 because this field moves monthly.');

  // ---------- 2. WELCOME + MAP ----------
  s = H.slide('WELCOME', 2);
  H.title(s, 'Welcome', 'Ask, or delegate — prompting does both');
  H.bullets(s, 0.55, 1.6, 6.1, 1.95, [
    { t: 'Prompting is the one AI skill that transfers everywhere: every assistant, every vendor, every year. Models change monthly; the craft compounds.', b: true },
    { t: 'The same skill has two modes. Generative: you ask, it writes, you act. Agentic: you brief it, it plans, uses tools, checks itself, and delivers.' },
    { t: 'Each mode needs a different kind of prompt — that distinction is the backbone of this training.' },
  ], { size: 11.5, gap: 6 });
  H.callout(s, 0.55, 3.62, 6.1, 1.2, C.TEAL_TINT, [
    { text: 'The 10-second version: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5, breakLine: true } },
    { text: 'a generative prompt describes what to write.\nAn agentic prompt describes a job to run — Part 5 teaches that mode properly.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'zap', iconFill: C.TEAL, size: 11.5 });
  H.promptChip(s, 0.55, 4.94, 6.1, 2.0, 1, [
    { type: '“Write a short farewell card for a coworker who is leaving.”', why: 'generative mode — it writes instantly, guessing every detail it doesn’t know.' },
    { type: '“Now don’t write it. Ask me everything you’d need to know to do this perfectly, then wait for my answers.”', why: 'the seed of delegate mode — the AI turns around and interviews YOU.' },
  ], { label: 'Two modes, felt — opens your course log', size: 8.6, tab: 'EX1-TwoModes' });
  H.card(s, 7.0, 1.55, 5.75, 2.95, C.PANEL);
  s.addText('The map — three blocks, six parts', { x: 7.3, y: 1.78, w: 5.2, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
  s.addText([
    { text: 'BLOCK 1 · FOUNDATIONS', options: { bold: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true, paraSpaceAfter: 2 } },
    { text: '1 · The primer — how this actually works\n2 · Models & tools — the landscape', options: { color: C.SLATE, fontSize: 10.5, breakLine: true, paraSpaceAfter: 7 } },
    { text: 'BLOCK 2 · THE CRAFT', options: { bold: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true, paraSpaceAfter: 2 } },
    { text: '3 · Prompt engineering — anatomy + techniques\n4 · The playbook — worked examples & demos', options: { color: C.SLATE, fontSize: 10.5, breakLine: true, paraSpaceAfter: 7 } },
    { text: 'BLOCK 3 · DELEGATION', options: { bold: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true, paraSpaceAfter: 2 } },
    { text: '5 · Agentic prompting — the mission brief\n6 · Prompts as assets · wrap-up', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { x: 7.3, y: 2.2, w: 5.2, h: 2.25, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.08 });
  H.callout(s, 7.0, 4.66, 5.75, 1.7, C.AMBER_TINT, [
    { text: 'You leave with: ', options: { bold: true, color: C.INK, fontSize: 11.5, breakLine: true } },
    { text: 'a working AI vocabulary · a tool map · the universal prompt anatomy + seven techniques · your Course Workbook (every exercise, copy-paste ready) · a 13-template library with the interactive Template Creator · the Prompt Element Taxonomy reference · team conventions for storing and versioning prompts.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'download', iconFill: C.AMBER, size: 11 });
  s.addText('This course teaches the text wing. Image, video and audio prompting have their own dials — same discipline, different controls; with enough interest, that becomes its own training.', { x: 7.0, y: 6.48, w: 5.75, h: 0.5, fontFace: F.body, fontSize: 9, italic: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 1.05 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Say the bold line first: “Prompting is the one AI skill that transfers everywhere.”\n' +
    '2) Walk the three left bullets; land on “two modes” as the backbone.\n' +
    '3) Teal card: read the 10-second version VERBATIM — it is the thesis.\n' +
    '4) Map card: the three block names and six parts, quickly — no clock talk.\n' +
    '5) Amber card: the take-homes; hold up the handout pack and the Course Workbook.\n' +
    '6) Footer aside, one sentence: this is the TEXT wing; image/video/audio could become their own training.\n' +
    '\n' +
    'TRY IT — PROMPT 1/8 (opens the course log; copy both steps from tab EX1-TwoModes)\n' +
    'Everyone runs both steps in ONE chat they keep all course — their course log.\n' +
    'Sequence: open your AI → paste STEP 1 → read what it invented → paste STEP 2 → watch it interview you.\n' +
    'Debrief line: step 1 ran on guesses (invented names, blanks); step 2 asked YOU.\n' +
    'Recovery (a model asks questions in step 1 too): “asking is the delegate move — step 2 just makes it happen on purpose.”\n' +
    'Do NOT use agentic vocabulary yet (checks, gates, briefs) — Part 5 owns those words.\n' +
    '\n' +
    'ACRONYMS —\n' +
    'LLM = Large Language Model — the text engine behind every assistant in this course.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: prompt rebuilt to the R10 template (TYPE THIS/WHY, no untaught concepts).\n' +
    'The multimodal aside is deliberate: the Prompt Report counts 58 text + 40 other-modality techniques — a separate training if votes call for it.\n' +
    'The eight numbered PROMPT exercises run through Parts 1–2 in the trainees’ own AI window; Parts 3–4 carry the hands-on reps and walkthrough exercises. The one course-log thread doubles as their take-home record.');

  // ---------- 3. PART I DIVIDER ----------
  s = H.slide(null, 3, { dark: true });
  H.partMarker(s, 1);
  s.addText('PART 1 · THE PRIMER', { x: 0.55, y: 2.3, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('Where this came from,\nand how it actually works', { x: 0.55, y: 2.8, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('Seventy years in two slides, then the six concepts that make you fluent: tokens, context, RAG, the escalation ladder, the token economy, hallucination.', { x: 0.55, y: 4.85, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Dividers are pacing: breathe. Read the two-line title, nothing more.\n' +
    '2) Point at the progress bar: “six parts — this is where we are.”\n' +
    '3) One sentence: “Two history slides, then six concepts — the vocabulary for everything after.”\n' +
    '4) Under 30 seconds, advance.\n' +
    '\n' +
    'ACRONYMS —\n' +
    'RAG = Retrieval-Augmented Generation (own slide shortly).');

  // ---------- 4. FOUR ERAS ----------
  s = H.slide('PART 1 · A SHORT HISTORY', 4);
  H.title(s, 'Seventy years in one slide', 'Four eras: rules → learning → generative → agentic');
  const eras = [
    ['edit', 'Rules', '1950s–1990s · symbolic AI, expert systems', 'Humans hand-code the logic: “if X then Y.” Rules shine, then crack on messy reality. Hype outruns results twice: the “AI winters.”', 'Gave us: expert systems doing real work — MYCIN diagnosing infections, XCON configuring computers.', C.PANEL],
    ['chart', 'Learning', '1990s–2010s · machine learning, neural networks', 'Stop writing rules — let the system find patterns in examples. 2012: deep nets + GPUs crush image recognition (AlexNet: 15.3% error vs 26.2%).', 'Gave us: spam filters, search ranking, recommendations, image recognition.', C.PANEL],
    ['brain', 'Generative', '2017– · transformers, LLMs', 'The Transformer (2017) lets models train on the whole internet. Predict-the-next-word at that scale writes, summarizes, codes.', 'Gave us: ChatGPT (2022), image generators — AI everyone can talk to.', C.TEAL_TINT],
    ['robot', 'Agentic', '2024– · reasoning models, tool use', 'Models get “arms”: tools, browsers, files, code. Reasoning models plan multi-step work; agents execute with limited supervision.', 'Giving us: coding agents, office agents, deep-research modes — AI you delegate to.', C.TEAL_TINT],
  ];
  eras.forEach((e, i) => {
    const x = 0.55 + i * 3.19;
    H.card(s, x, 1.7, 2.95, 3.72, e[5]);
    H.iconCircle(s, x + 0.24, 1.92, 0.5, e[0], C.TEAL);
    s.addText(e[1], { x: x + 0.86, y: 1.94, w: 2.05, h: 0.34, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
    s.addText(e[2], { x: x + 0.86, y: 2.27, w: 2.05, h: 0.42, fontFace: F.body, fontSize: 8.2, bold: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 0.98 });
    const gx = x + 0.3, gy = 2.82;
    const box = (bx, by, bw, label, tint) => {
      s.addShape('roundRect', { x: bx, y: by, w: bw, h: 0.22, rectRadius: 0.04, fill: { color: tint || 'FFFFFF' }, line: { color: C.TEAL, width: 0.75 } });
      if (label) s.addText(label, { x: bx, y: by, w: bw, h: 0.22, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 6.5, color: C.TEAL_DARK, margin: 0 });
    };
    if (i === 0) {
      box(gx + 0.78, gy, 0.8, 'if…?');
      box(gx + 0.08, gy + 0.4, 0.8, 'then A'); box(gx + 1.5, gy + 0.4, 0.8, 'else B');
      s.addShape('line', { x: gx + 1.05, y: gy + 0.22, w: -0.55, h: 0.18, line: { color: C.TEAL, width: 1 } });
      s.addShape('line', { x: gx + 1.32, y: gy + 0.22, w: 0.55, h: 0.18, line: { color: C.TEAL, width: 1 } });
    } else if (i === 1) {
      const L1 = [0, 0.22, 0.44], L2 = [0.11, 0.33];
      L1.forEach(dy => L2.forEach(dy2 => s.addShape('line', { x: gx + 0.3, y: gy + dy + 0.07, w: 0.85, h: dy2 - dy, line: { color: C.LINE, width: 0.9 } })));
      L2.forEach(dy2 => s.addShape('line', { x: gx + 1.3, y: gy + dy2 + 0.07, w: 0.75, h: 0.15 - dy2 + 0.07, line: { color: C.LINE, width: 0.9 } }));
      L1.forEach(dy => s.addShape('ellipse', { x: gx + 0.16, y: gy + dy, w: 0.15, h: 0.15, fill: { color: C.TEAL }, line: { type: 'none' } }));
      L2.forEach(dy => s.addShape('ellipse', { x: gx + 1.16, y: gy + dy, w: 0.15, h: 0.15, fill: { color: C.TEAL }, line: { type: 'none' } }));
      s.addShape('ellipse', { x: gx + 2.06, y: gy + 0.22, w: 0.15, h: 0.15, fill: { color: C.AMBER }, line: { type: 'none' } });
    } else if (i === 2) {
      box(gx, gy + 0.2, 0.55, 'The'); box(gx + 0.6, gy + 0.2, 0.6, 'audit'); box(gx + 1.25, gy + 0.2, 0.4, 'is');
      s.addShape('line', { x: gx + 1.68, y: gy + 0.31, w: 0.25, h: 0, line: { color: C.TEAL, width: 1.25, endArrowType: 'triangle' } });
      s.addShape('roundRect', { x: gx + 1.98, y: gy + 0.2, w: 0.42, h: 0.22, rectRadius: 0.04, fill: { color: C.TEAL }, line: { type: 'none' } });
      s.addText('…?', { x: gx + 1.98, y: gy + 0.2, w: 0.42, h: 0.22, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 7, bold: true, color: 'FFFFFF', margin: 0 });
    } else {
      box(gx, gy + 0.08, 0.68, 'PLAN'); box(gx + 0.86, gy + 0.08, 0.62, 'ACT'); box(gx + 1.66, gy + 0.08, 0.74, 'CHECK');
      s.addShape('line', { x: gx + 0.7, y: gy + 0.19, w: 0.14, h: 0, line: { color: C.TEAL, width: 1, endArrowType: 'triangle' } });
      s.addShape('line', { x: gx + 1.5, y: gy + 0.19, w: 0.14, h: 0, line: { color: C.TEAL, width: 1, endArrowType: 'triangle' } });
      s.addShape('line', { x: gx + 0.34, y: gy + 0.48, w: 1.72, h: 0, line: { color: C.TEAL, width: 1, beginArrowType: 'triangle' } });
    }
    s.addText(e[3], { x: x + 0.24, y: 3.52, w: 2.5, h: 1.18, fontFace: F.body, fontSize: 9.4, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.05 });
    s.addText(e[4], { x: x + 0.24, y: 4.72, w: 2.5, h: 0.66, fontFace: F.body, fontSize: 8.6, italic: true, color: C.TEAL_DARK, margin: 0, lineSpacingMultiple: 1.02 });
    if (i < 3) H.arrow(s, x + 2.97, 3.45, 0.2, C.TEAL);
  });
  H.callout(s, 0.55, 5.6, 12.2, 1.05, C.AMBER_TINT, [
    { text: 'Why the last decade exploded — scaling laws (2020): ', options: { bold: true, color: C.INK, fontSize: 12.5 } },
    { text: 'bigger model + more data + more compute = predictably better results. Progress stopped being a research gamble and became an investment roadmap.', options: { color: C.SLATE, fontSize: 12.5 } },
  ], { iconName: 'trend', iconFill: C.AMBER });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “Seventy years in one slide — as four eras.”\n' +
    '2) Per card LEFT TO RIGHT: name the era → point at the little diagram (a hand-typed rulebook · circles passing signals, tuned from examples · predict-the-next-word · plan-act-check on a loop) → one sentence of story → the italic “gave us” line, which is the era’s legacy in products.\n' +
    '3) Pause once on “AI winters”: over-promising collapsed funding twice — skepticism is historically earned.\n' +
    '4) Close on the amber band: scaling laws.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Zoom into the decade that changed work.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'GPU = Graphics Processing Unit — the graphics chip class perfect for training neural networks (AlexNet, 2012).\n' +
    'LLM = Large Language Model.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: “gave us” outcome lines added per era (owner request), verified items only — MYCIN/XCON, spam/search/recommendations/AlexNet, ChatGPT/image generation, coding & office agents (r1, r2).\n' +
    'The eras framing is a teaching synthesis — “a useful way to see 70 years,” not official taxonomy.\n' +
    'Rules era = writing the SOP yourself; learning era = deriving the SOP from a thousand examples. (SOP = Standard Operating Procedure.)');

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
    '1) Walk the timeline TOP TO BOTTOM, metronome pace — say the METHOD name in bold each time.\n' +
    '2) Slow down twice: 2022 (RLHF) and 2024 (models that think before answering).\n' +
    '3) On 2017, tell the title story: “Attention Is All You Need” — ATTENTION is the mechanism that lets the model weigh which earlier words matter most when predicting the next one; the paper’s bold claim was that attention ALONE suffices — the older machinery could be dropped. (The title is widely described as a playful nod to “All You Need Is Love.”)\n' +
    '4) Right card: ChatGPT reached 100M users in two months; TikTok ~nine; Instagram ~two and a half years.\n' +
    '\n' +
    'TRY IT (optional, spoken — not one of the eight numbered exercises) —\n' +
    'TYPE THIS → “Explain the 2017 AI paper ‘Attention Is All You Need’ like I’m new to AI: what is attention, why did the title claim it’s ALL you need, and what did it replace? Under 120 words.”\n' +
    'WHY → the definition lands in their course log, accurately, from their own tool.\n' +
    '\n' +
    'ACRONYMS —\n' +
    'GPT = Generative Pre-trained Transformer. RLHF = Reinforcement Learning from Human Feedback.\n' +
    'MoE = Mixture of Experts (defined properly in Part 2). o1 = OpenAI’s first reasoning model. R1 = DeepSeek’s open reasoning model.\n' +
    '\n' +
    'CONTENT —\n' +
    'A multi-company user-growth line is NOT buildable honestly (metrics differ: weekly vs monthly actives vs downloads) — the time-to-100M chart is the one honest shape (single source).\n' +
    'Kept for questions: 88% of organizations use AI somewhere (Stanford AI Index 2026), but agent deployment is still single-digit % — everyone chats, almost nobody delegates. That gap is this course.\n' +
    'Vendor adoption numbers are marketing until independently reproduced.');

  // ---------- 6. HOW AN LLM WORKS ----------
  s = H.slide('PART 1 · HOW LLMS WORK', 6);
  H.title(s, 'Under the hood', 'A prediction engine, sent to finishing school');
  const pipe = [
    ['database', '1 · Pretraining', 'Months, trillions of words: learn to predict the next token on internet-scale text. Language, facts, and reasoning patterns compress into billions of learned weights.'],
    ['list', '2 · Instruction tuning', 'Curated example dialogues teach it to follow instructions and answer questions — instead of just continuing your text.'],
    ['thumbsup', '3 · Human feedback (RLHF)', 'People rank outputs; the model is tuned toward helpful, honest, harmless. And it never stops: your thumbs-up today is preference data for the NEXT model.'],
  ];
  pipe.forEach((p, i) => {
    const x = 0.55 + i * 4.18;
    H.card(s, x, 1.62, 3.95, 2.42, C.PANEL);
    H.iconCircle(s, x + 0.28, 1.78, 0.46, p[0], C.TEAL);
    s.addText(p[1], { x: x + 0.28, y: 2.3, w: 3.4, h: 0.36, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
    s.addText(p[2], { x: x + 0.28, y: 2.68, w: 3.42, h: 1.3, fontFace: F.body, fontSize: 9.8, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.04 });
    if (i < 2) H.arrow(s, x + 3.97, 2.75, 0.2, C.TEAL);
  });
  H.callout(s, 0.55, 4.16, 6.0, 1.18, C.TEAL_TINT, [
    { text: 'Knowledge is frozen at the cutoff — with escape hatches. ', options: { bold: true, color: C.TEAL_DARK, fontSize: 10.8, breakLine: true } },
    { text: 'Training ends months before release. But many assistants compensate: live web search pulls today’s pages into the prompt, and RAG (concept 3) plugs in your own documents.', options: { color: C.SLATE, fontSize: 10 } },
  ], { iconName: 'clock', iconFill: C.TEAL, size: 10.8 });
  H.callout(s, 6.75, 4.16, 6.0, 1.18, C.AMBER_TINT, [
    { text: 'Why prompting exists: ', options: { bold: true, color: C.INK, fontSize: 11.5, breakLine: true } },
    { text: 'the model completes your text — the prompt is the only steering wheel you have. A complete prompt doesn’t make the model smarter: it deletes wrong guesses.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'compass', iconFill: C.AMBER, size: 11 });
  H.promptChip(s, 0.55, 5.46, 12.2, 1.6, 2, [
    { type: '“Finish this sentence 5 different ways: We should move the launch date because”', why: 'no facts yet — watch it scatter across guesses.' },
    { type: '“Now 5 more ways, knowing: B2B software firm, competitor launches May 3, our beta ends April 20.”', why: 'your facts didn’t make it smarter — they deleted wrong guesses.' },
  ], { label: 'Narrowing the guesses — two separate sends', size: 8.2, tab: 'EX2-Guesses' });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Title metaphor first: “a prediction engine, sent to finishing school.”\n' +
    '2) Three cards LEFT TO RIGHT — pretraining, instruction tuning, human feedback. On card 3, land the after-ship line: RLHF never really stops — every thumbs-up/down you click, and on personal accounts your chats themselves, become the preference data that trains the next model. (That is exactly what “trains on your data by default” means on the trust slide in Part 2.)\n' +
    '3) LEFT callout: the cutoff — AND its two escape hatches: live web search, and RAG for your own documents.\n' +
    '4) RIGHT callout, slowly — the thesis of the course: the prompt is the only steering wheel; a complete prompt DELETES WRONG GUESSES.\n' +
    '\n' +
    'TRY IT — PROMPT 2/8 (two sends; copy from tab EX2-Guesses)\n' +
    'Send 1 scatters: budget, staffing, quality. Send 2 orbits May 3 and April 20.\n' +
    'Debrief line: “Grade the directions, not the sentences.”\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Six concepts, quick — starting with what the model actually reads.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'RLHF = Reinforcement Learning from Human Feedback — card 3.\n' +
    'RAG = Retrieval-Augmented Generation — concept 3, shortly.\n' +
    '\n' +
    'CONTENT —\n' +
    'InstructGPT fact worth telling: raters preferred a well-tuned 1.3B model over raw 175B GPT-3 — tuning beat 100× scale.\n' +
    'v1.6: cutoff callout gains the web-search/RAG escape hatches; RLHF card gains the after-ship story (owner request).');

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
  H.promptChip(s, 0.55, 4.85, 6.2, 1.7, 3, [
    { type: '“Explain AI tokens to a busy office worker in under 80 words: use a LEGO-brick analogy, show one word splitting into tokens, and end with why tokens set my AI’s cost and limits.”', why: 'the definition lands in your course log — and the brick analogy is the one the best explainers use.' },
  ], { label: 'Bricks, not letters', size: 8.4, tab: 'EX3-Tokens' });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Title first: “the model reads bricks, not letters.”\n' +
    '2) Left bullets; STOP on the bold third and tell the strawberry story — models famously miscounted the r’s because they never see letters. (Tell it as a story — current models have memorized that one; don’t run it live.)\n' +
    '3) Right card: the brick strip — “this is exactly how your sentence arrives: eight bricks, eight numbers.”\n' +
    '4) Best live demo if you have two minutes: open a live tokenizer page and paste attendees’ NAMES and company jargon — common words stay whole, rare words shatter into colored chunks. Personal and reliable.\n' +
    '5) Teal card: the three daily-work consequences.\n' +
    '\n' +
    'TRY IT — PROMPT 3/8 (copy from tab EX3-Tokens)\n' +
    'One send; the AI teaches the concept into their log.\n' +
    'Recovery (answers differ across the room): “every vendor has its own brick set — the bricks are always there, the letters never are.”\n' +
    '\n' +
    'BRIDGE —\n' +
    '“If text is bricks — how many bricks fit on the desk?”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'ID = identifier — to the model each token is just a number. K = thousand.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: prompt finalized from the explainer research (r17) — LEGO validated as the dominant popular analogy; tokenizer-page demo recommended over any word trick.\n' +
    'Token math preview: tokens also explain context windows (next slide) and the bill (later this part).');

  // ---------- 8. CONTEXT WINDOW ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 8);
  H.title(s, 'Concept 2 · Context window', 'A desk, not a filing cabinet');
  H.bullets(s, 0.55, 1.62, 6.2, 2.75, [
    { t: 'The context window is working memory for one conversation: your question, the system prompt, chat history, attached files, and search results must all fit on the desk.' },
    { t: 'Close the chat and the desk is swept clean. Nothing persists unless a memory feature or a saved file re-loads it.' },
    { t: 'By 2026, ~1M tokens (≈750,000 words) is the flagship standard. Consumer apps often enforce smaller limits than the raw model.' },
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
    { text: '① long documents at the TOP, question at the END (up to ~30% better answers) · ② label multiple documents · ③ new topic → new chat · ④ long thread → run the handoff move below.', options: { color: C.SLATE, fontSize: 10.2 } },
  ], { iconName: 'check', iconFill: C.TEAL, size: 10.5 });
  H.card(s, 0.55, 4.5, 6.2, 0.94, C.AMBER_TINT);
  s.addText([
    { text: 'A desk with a filing cabinet? ', options: { bold: true, color: C.INK, fontSize: 11 } },
    { text: 'Persistent files, notes and standing instructions are exactly what agentic tools bolt onto the desk — Part 5.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { x: 0.85, y: 4.6, w: 5.7, h: 0.76, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.05 });
  H.promptChip(s, 0.55, 5.56, 12.2, 1.52, 4, [
    { type: '“Explain your context window like I’m a 5th grader: the desk, what fits on it, and what happens when I close this chat. Under 100 words.”', why: 'the AI describes its own working memory, plainly.' },
    { type: '(homework) “Summarize our chat so far in under 80 words, titled HANDOFF.”', why: 'tonight, paste it into a fresh chat, ask “where was I?” — and watch it pick up your course.' },
  ], { label: 'The desk — explained, then carried', size: 8.4, tab: 'EX4-Handoff' });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) The analogy first: “a desk, not a filing cabinet.”\n' +
    '2) Left bullets; on the bold one, draw the U-shape in the air — attention high at the start, sags in the middle, high at the end.\n' +
    '3) Right card: the four things on the desk right now.\n' +
    '4) Teal card: the four habits — habit ④ is about to be performed.\n' +
    '5) Amber card: one sentence — the filing-cabinet teaser for Part 5. Plant the seed, move on.\n' +
    '\n' +
    'TRY IT — PROMPT 4/8 (copy from tab EX4-Handoff)\n' +
    'Step 1 in class; step 2 is homework in the same thread.\n' +
    'Recovery (someone’s fresh chat knows unpasted things): “your tool has a filing cabinet bolted to the desk — hold that thought for Part 5.”\n' +
    '\n' +
    'BRIDGE —\n' +
    '“And what if what you need was never on the desk? RAG.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    '1M = one million tokens.\n' +
    '\n' +
    'CONTENT —\n' +
    '“Lost in the middle” = Liu et al. 2023 (TACL). The up-to-~30% figure is Anthropic’s own long-context guidance.\n' +
    '1M-token flagship standard verified Aug 2026 across Claude, GPT-5.x, Gemini, and the Chinese open-weight flagships.');

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
    '1) Expand the acronym ONCE, then the analogy: an open-book exam — a librarian fetches pages from YOUR documents; the student writes from those pages.\n' +
    '2) Four step cards LEFT TO RIGHT.\n' +
    '3) Green card: current, checkable, private, access-aware.\n' +
    '4) Red card, slowly: wrong page → fluent, confident, CITED, wrong. “Check the citation, not the prose.”\n' +
    '5) Teal band: “you’ve been running this loop all along” — keep it generic, no product names.\n' +
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
  H.promptChip(s, 6.75, 1.62, 6.0, 2.1, 5, [
    { type: '“Give me three everyday AI problems: one fixed by a better prompt, one by giving it the right documents, one only fixable by retraining it. One line each on why.”', why: 'the ladder, sorted live by the AI in front of you.' },
  ], { label: 'See the rungs sort themselves', size: 8.8, tab: 'EX5-Ladder' });
  H.card(s, 6.75, 3.88, 6.0, 2.72, C.PANEL);
  s.addText([
    { text: 'Want the full drill? ', options: { bold: true, color: C.INK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 4 } },
    { text: 'Tab EX5-Ladder also holds the EXTENDED triage drill: six realistic workplace AI problems — you sort each as P (prompt), R (retrieve) or F (fine-tune) BEFORE the AI grades you against the one-question diagnostic. Problem 6 is deliberately arguable — that argument is the lesson.\n\nRun it tonight, or as the room’s stretch exercise if time allows.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { x: 7.02, y: 4.08, w: 5.45, h: 2.35, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.1 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) The rule IS the title: “prompt first, retrieve second, fine-tune last.”\n' +
    '2) Three rungs TOP TO BOTTOM; the temp analogies carry it: instructions → binder → training course.\n' +
    '3) Amber card — the generic power: ONE question triages any AI disappointment. The next concept is all about the bill.\n' +
    '\n' +
    'TRY IT — PROMPT 5/8 (copy from tab EX5-Ladder)\n' +
    'One send; concept-first — nobody gets lost in an exercise.\n' +
    'The EXTENDED six-problem drill lives in the same tab (answers in your notes: 1 P · 2 R · 3 P · 4 R · 5 F · 6 defensible either way — the debrief centerpiece).\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Two concepts left — the next one is all about the bill.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'RAG = Retrieval-Augmented Generation (rung 2).\n' +
    '\n' +
    'CONTENT —\n' +
    '“Let’s fine-tune on our procedures” → first ask: knowledge problem (→RAG) or behavior problem (→prompt)? Most enterprise cases are knowledge problems.\n' +
    'Frontier flagships mostly aren’t fine-tunable (2026); open-weight models are.\n' +
    'NOTE: this is the ESCALATION ladder (capability). Part 6’s PROMOTION ladder (where prompts live) is a different ladder — name them fully.');

  // ---------- 11. FAST vs THINKING ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 11);
  H.title(s, 'Concept 5 · Fast models vs thinking models', 'Two speeds, one bill');
  H.bullets(s, 0.55, 1.66, 6.2, 2.85, [
    { t: 'Every vendor ships a fast tier — one pass, instant, cheap — and a thinking tier that drafts, checks and revises internally before answering (compute spent at answer time).' },
    { t: 'System 1 vs System 2 (Kahneman’s Thinking, Fast and Slow): fast intuition for routine asks; slow deliberation where being wrong is expensive.' },
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
  H.promptChip(s, 7.0, 1.66, 5.75, 2.15, 6, [
    { type: '“Describe your fast mode vs your thinking mode like I’m choosing between them for real work: when is each worth it, and roughly how much more does thinking cost? Under 120 words.”', why: 'the model explains its own two speeds — and its own bill.' },
  ], { label: 'Same brain, two speeds', size: 8.8, tab: 'EX6-TwoSpeeds' });
  H.card(s, 7.0, 3.95, 5.75, 2.63, C.PANEL);
  s.addText([
    { text: 'Feel the bill (extended, tab EX6): ', options: { bold: true, color: C.INK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 4 } },
    { text: 'a five-colleague scheduling puzzle you run TWICE — once as an instant one-liner, once carefully with every rule checked — then the AI estimates the word count of each and computes the multiple. Most rooms land on 10–20×: exactly how the thinking tier bills you.\n\nUnique solution (your answer key): Ben Mon · Chloe Tue · Ema Wed · Ana Thu · Dev Fri.', options: { color: C.SLATE, fontSize: 10.2 } },
  ], { x: 7.28, y: 4.15, w: 5.2, h: 2.3, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.1 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “every AI app sells you two speeds — when is the slow one worth its bill?” Name the book once: Kahneman’s Thinking, Fast and Slow — the owner-favorite narrative of this slide.\n' +
    '2) The BILL bullet is the slow-down: thinking is billed like output — 5–20× a simple ask.\n' +
    '3) Green/amber cards: on for, off for. Escalate on failure, not by default.\n' +
    '\n' +
    'TRY IT — PROMPT 6/8 (copy from tab EX6-TwoSpeeds)\n' +
    'One send, informative. The extended puzzle version lives in the same tab for stretch time or homework.\n' +
    'Recovery (a model claims one mode): “ask it what the thinking toggle in its own interface does, then — that’s tomorrow’s exercise anyway.”\n' +
    '\n' +
    'BRIDGE —\n' +
    '“That’s the two speeds. Now the whole menu — where your tokens actually go.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'MoE = Mixture of Experts — defined properly in Part 2.\n' +
    'System 1 / System 2 = Kahneman’s fast-intuition vs slow-deliberation framing.\n' +
    '\n' +
    'CONTENT —\n' +
    'Thinking tokens billed as output even when you only see a summary; output ≈ 5× input across vendors; effort adaptive/dial-able by 2026 (t4 §5, primary-sourced).\n' +
    'Honest caveat: the model isn’t literally “thinking” — it generates intermediate tokens that improve the final answer.');

  // ---------- 12. THE FEATURE MENU ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 12);
  H.title(s, 'Concept 5 · The feature menu · continued', 'Where your tokens go');
  H.card(s, 0.55, 1.62, 5.9, 3.3, C.PANEL);
  s.addText('The cost ladder — every vendor sells it', { x: 0.85, y: 1.8, w: 5.3, h: 0.38, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  const ladder2 = [
    ['Quick answer', '1×', 'one pass, instant'],
    ['Thinking / extended reasoning', '5–20×', 'drafts and checks before answering'],
    ['Web search', '+sources', 'grounds the answer in live pages'],
    ['Deep research', '100×+', 'browses for minutes, cited report'],
    ['Agent modes', 'the most', 'plans and acts across many steps'],
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
    ['claude', 'ChatGPT', 'deep research · thinking slider (paid) · “Think” button (free)'],
    ['gemini', 'Gemini', 'Deep Research (all tiers) · Deep Think = separate hard-reasoning mode (Ultra)'],
    ['openai', 'Claude', 'Research (paid plans) · extended thinking'],
    ['copilot', 'Copilot', 'Quick response · Think Deeper · Smart (GPT-5) · Researcher agent'],
    ['perplexity', 'Perplexity', 'Search · Research · Create files and apps'],
  ];
  const modeLogos = { ChatGPT: 'openai', Gemini: 'gemini', Claude: 'claude', Copilot: 'copilot', Perplexity: 'perplexity' };
  modeNames.forEach((m, i) => {
    const y = 2.3 + i * 0.52;
    H.logo(s, 6.88, y + 0.03, 0.38, modeLogos[m[1]], m[1][0]);
    s.addText(m[1], { x: 7.36, y, w: 1.05, h: 0.46, fontFace: F.body, fontSize: 10.5, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText(m[2], { x: 8.45, y, w: 4.15, h: 0.46, fontFace: F.body, fontSize: 8.8, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.98 });
  });
  s.addText('Deep research, demystified: a reasoning model given a browser and time — it plans, reads sources for minutes, and synthesizes a cited report. The MoE story in Part 2 is why that became affordable.', { x: 0.55, y: 5.02, w: 12.2, h: 0.42, fontFace: F.body, fontSize: 10.5, italic: true, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.05 });
  H.promptChip(s, 0.55, 5.5, 12.2, 1.55, 7, [
    { type: '“List the modes this app gives me — quick answer, thinking, web search, deep research, agent — one line each on what it does differently and its rough effort. Say ‘unsure’ rather than guess.”', why: 'your own product hands you its menu; ask again the day it changes.' },
  ], { label: 'Ask your own product for its menu', size: 9, tab: 'EX7-FeatureMenu' });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Left card: climb the staircase — 1× quick answer up to agent modes. The discipline: pick the SMALLEST mode that can succeed; escalate deliberately.\n' +
    '2) Right card: the same ladder under five brand logos — read one row, gesture the rest. Copilot users: your everyday menu is the fourth row. (“Smart (GPT-5)” is the CONSUMER Copilot label; M365 Copilot separately prefers GPT-5.6 — different surfaces, both true.)\n' +
    '3) Italic line: deep research demystified.\n' +
    '\n' +
    'TRY IT — PROMPT 7/8 (copy from tab EX7-FeatureMenu)\n' +
    'Self-updating — the answer regenerates the day any vendor renames a button. The extended 6-column table version lives in the tab.\n' +
    'Recovery (model misstates its own toggles): “it knows what its modes DO better than where the buttons live — keep the ladder, verify toggles with your eyes.”\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Last concept — the one everyone asks about first.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'MoE = Mixture of Experts (Part 2).\n' +
    '\n' +
    'CONTENT —\n' +
    'Mode names verified Sep 9, 2026 — full paper trail with sources: notes/research/r18_mode_names.md. Re-confirm the ChatGPT row in the live app before training day (r18 caveat). [REFRESH QUARTERLY.]\n' +
    'The 5–20× multiplier is sourced (r2); the 100×+ deep-research figure is an order-of-magnitude illustration, not a billed rate.\n' +
    'Scaling anecdote for questions: one fast prompt vs an orchestrated multi-agent research run = hundreds of quick answers’ worth of tokens.');

  // ---------- 13. HALLUCINATION — THE FOUR CHARACTERS ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 13);
  H.title(s, 'Concept 6 · Hallucination', 'Fluency is not evidence');
  H.bullets(s, 0.55, 1.66, 5.6, 4.3, [
    { t: 'The mechanism: models are optimized for the most plausible next token, not the most true one. Trouble concentrates where training data is thin: rare facts, exact citations, numbers, names.' },
    { t: 'OpenAI’s own 2025 research: benchmarks reward confident guessing over “I don’t know” — models learn to be good test-takers.', b: true },
    { t: 'The better word is confabulation: it isn’t seeing things — it fills gaps with plausible material, in-format. Fake citations LOOK like citations.' },
  ], { size: 12, gap: 10 });
  const kinds = [
    ['brain', 'THE CONFIDENT GUESS', 'Invented facts', 'Free recall where data was thin — a wrong fact, delivered with total certainty.'],
    ['file', 'THE FAKE RECEIPT', 'Invented sources', 'Citations, cases, book titles that look perfectly real — and don’t exist.'],
    ['alert', 'THE JOKE TAKEN SERIOUSLY', 'Wrong source, confident answer', 'Fluent, cited — and built on a joke, a satire, or the wrong revision.'],
    ['repeat', 'GARBAGE IN, GOSPEL OUT', 'Runs with your false premise', 'It assumes your prompt is true: feed it a wrong “fact” and it politely builds on it.'],
  ];
  kinds.forEach((k, i) => {
    const y = 1.66 + i * 1.24;
    H.card(s, 6.35, y, 6.4, 1.12, i === 2 ? C.RED_TINT : C.PANEL);
    H.iconCircle(s, 6.55, y + 0.31, 0.5, k[0], i === 2 ? C.RED : C.TEAL);
    s.addText([
      { text: k[1] + '  ', options: { bold: true, color: i === 2 ? C.RED : C.TEAL_DARK, fontSize: 13, fontFace: F.head } },
      { text: '· ' + k[2], options: { color: C.MUTE, fontSize: 9.5, breakLine: true, paraSpaceAfter: 2 } },
      { text: k[3], options: { color: C.SLATE, fontSize: 9.8 } },
    ], { x: 7.18, y: y + 0.08, w: 5.4, h: 0.98, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.03 });
  });
  s.addText('Four characters — one root: the show must go on. Next slide: what they cost in public.', { x: 0.55, y: 6.6, w: 12.2, h: 0.35, fontFace: F.body, fontSize: 10.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Open with the improv actor, spoken: “an improv actor never breaks character — the show must go on, so gaps get filled with the most plausible line. That is your AI on a thin-data day.”\n' +
    '2) Left bullets: the mechanism; the bold OpenAI 2025 finding — the vendor itself says benchmarks reward guessing; the vocabulary upgrade — CONFABULATION.\n' +
    '3) Right: meet the four CHARACTERS — say the nicknames with theater: the confident guess · the fake receipt · the joke taken seriously · garbage in, gospel out. One line each; each returns as a real incident on the next slide.\n' +
    '4) Presenter story for character 1 if you want one: Google Bard’s launch demo flubbed a telescope fact — details on the next slide’s notes.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“What do these characters look like in public? The hall of shame.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none new on this slide.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: the four kinds became named characters (owner: more engaging). Teaching frame grounded in r10/r2/r14 — not claimed as academic taxonomy.\n' +
    'OpenAI 2025 = “Why language models hallucinate” (arXiv:2509.04664).');

  // ---------- 14. HALL OF SHAME ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 14);
  H.title(s, 'Concept 6 · The hall of shame · continued', 'Real, public, verified — and all avoidable');
  const shame = [
    ['alert', 'Glue on pizza · May 2024', 'Google’s AI search told users to put glue in pizza sauce and eat a rock a day — it had read a joke forum comment and a satire article as advice. Global mockery; the feature was scaled back within days.'],
    ['gavel', 'The ChatGPT lawyer · Jun 2023', 'A New York lawyer filed six court cases that didn’t exist — then asked ChatGPT whether they were real. It said yes. $5,000 sanction, apology letters ordered (Mata v. Avianca).'],
    ['send', 'Air Canada’s chatbot · Feb 2024', 'The website bot invented a bereavement refund policy. A tribunal made the airline honor it — rejecting the claim that the bot was “a separate legal entity.” Your company owns what its chatbot says.'],
    ['chart', 'The Big Four arc · 2025–26', 'Deloitte partially refunded a government report fee over invented citations; EY pulled a report where 16 of 27 references didn’t check out; KPMG’s report on agentic-AI excellence had 5 of 45 citations check out.'],
  ];
  shame.forEach((r, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.62 + Math.floor(i / 2) * 1.68;
    H.card(s, x, y, 5.95, 1.56, C.PANEL);
    H.iconCircle(s, x + 0.2, y + 0.2, 0.44, r[0], i === 0 ? C.AMBER : C.RED);
    s.addText([
      { text: r[1], options: { bold: true, color: C.INK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 3 } },
      { text: r[2], options: { color: C.SLATE, fontSize: 9.6 } },
    ], { x: x + 0.78, y: y + 0.1, w: 5.0, h: 1.4, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.03 });
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
    '1) Walk the four cards — laugh at glue-on-pizza, then take the temperature down.\n' +
    '2) Glue on pizza, plainly: someone posted a JOKE; the AI served it as advice — “the joke taken seriously.”\n' +
    '3) The lawyer: he checked the fabrication WITH the fabricator. Verification lives OUTSIDE the tool.\n' +
    '4) Air Canada: small money (~CA$800), giant precedent.\n' +
    '5) The Big Four arc: three global consultancies, three fabricated-source scandals in nine months — the last one a report ABOUT doing AI well.\n' +
    '6) Amber → teal → red bands, in order; the house rule VERBATIM — policy, not advice.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“That closes the concepts — now, the tool landscape.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none new on this slide.\n' +
    '\n' +
    'CONTENT —\n' +
    'All incidents verified with sources, dates and MANDATORY phrasing caveats in notes/research/r14_hallucination_incidents.md.\n' +
    'Reserve incidents for questions (r14): Bard’s launch flub (phrase carefully: shares fell ~8% — about $100B — after Reuters flagged the error AND a weak launch event) · Sun-Times fake reading list · the invented Turley scandal · mayor Hood (THREATENED suit; never filed) · Cohen (NOT sanctioned) · NYC MyCity chatbot · Whisper in hospitals (AP).\n' +
    'None of the cures eliminates hallucination — they convert unverifiable claims into verifiable ones.');
};
