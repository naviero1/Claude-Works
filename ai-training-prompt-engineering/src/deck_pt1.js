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
      { text: cd[2], options: { color: C.ON_DARK_MUTE, fontSize: 10.5 } },
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
  H.callout(s, 0.55, 3.62, 6.1, 1.0, C.TEAL_TINT, [
    { text: 'The 10-second version: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5, breakLine: true } },
    { text: 'a generative prompt describes what to write.\nAn agentic prompt describes a job to run — Part 5 teaches that mode properly.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'zap', iconFill: C.TEAL, size: 11.5 });
  H.promptChip(s, 0.55, 4.7, 6.1, 2.38, 1, [
    { type: '“This chat is my course log for a prompting course. Remember every prompt I run — at the end I’ll ask for a report.”', why: 'the log becomes the final exercise.' },
    { type: '“First job: write a farewell card for a coworker.”', why: 'generative mode — instant, guessing every unknown.' },
    { type: '“Now don’t write it — interview me first, then wait.”', why: 'delegate mode’s seed — the questions come to YOU.' },
  ], { label: 'Two modes, felt — opens your course log', size: 9.5, tab: 'EX1-TwoModes' });
  H.card(s, 7.0, 1.55, 5.75, 2.95, C.PANEL);
  s.addText('The map — three blocks, six parts', { x: 7.3, y: 1.78, w: 5.2, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
  s.addText([
    { text: 'BLOCK 1 · FOUNDATIONS', options: { bold: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true, paraSpaceAfter: 2 } },
    { text: '1 · The primer — how this actually works\n2 · Models & tools — the landscape', options: { color: C.SLATE, fontSize: 11, breakLine: true, paraSpaceAfter: 7 } },
    { text: 'BLOCK 2 · THE CRAFT', options: { bold: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true, paraSpaceAfter: 2 } },
    { text: '3 · Prompt engineering — anatomy + techniques\n4 · The playbook — worked examples & demos', options: { color: C.SLATE, fontSize: 11, breakLine: true, paraSpaceAfter: 7 } },
    { text: 'BLOCK 3 · DELEGATION', options: { bold: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true, paraSpaceAfter: 2 } },
    { text: '5 · Agentic prompting — the mission brief\n6 · Prompts as assets · wrap-up', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 7.3, y: 2.2, w: 5.2, h: 2.25, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.08 });
  H.card(s, 7.0, 4.66, 5.75, 1.78, C.AMBER_TINT);
  H.iconCircle(s, 7.2, 4.8, 0.4, 'download', C.AMBER);
  s.addText('You leave with:', { x: 7.72, y: 4.8, w: 4.8, h: 0.34, fontFace: F.head, fontSize: 12.5, bold: true, color: C.INK, margin: 0, valign: 'middle' });
  s.addText([
    { text: '•  Course Workbook — every exercise, copy-paste ready', options: { breakLine: true } },
    { text: '•  13-template prompt library + Template Creator', options: { breakLine: true } },
    { text: '•  Taxonomy reference + one-page cheat sheet', options: { breakLine: true } },
    { text: '•  The Do / Don’t / Expired playbook one-pager', options: { breakLine: true } },
    { text: '•  Team conventions for storing & versioning prompts', options: {} },
  ], { x: 7.28, y: 5.18, w: 5.3, h: 1.2, fontFace: F.body, fontSize: 10.5, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.1 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Say the bold line first: “Prompting is the one AI skill that transfers everywhere.”\n' +
    '2) Walk the three left bullets; land on “two modes” as the backbone.\n' +
    '3) Teal card: read the 10-second version VERBATIM — it is the thesis.\n' +
    '4) Map card: the three block names and six parts, quickly — no clock talk.\n' +
    '5) Amber card: the take-homes; hold up the handout pack and the Course Workbook.\n' +
    '6) Footer aside, one sentence: this is the TEXT wing; image/video/audio could become their own training.\n' +
    '\n' +
    'TRY IT — PROMPT 1/7 (opens the course log; copy all three steps from tab EX1-TwoModes)\n' +
    'v1.12 (owner request): STEP 1 is new — it tells the AI this chat IS the course log and to remember every prompt, so the final Part 3 rep (“turn my log into a report”) works without setup. Say: “this one sentence is what makes your last exercise possible.”\n' +
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
    'The eight numbered PROMPT exercises run through Parts 1–2 in the trainees’ own AI window; Parts 3–4 carry the hands-on reps and walkthrough exercises. The one course-log thread doubles as their take-home record.\n' +
    'IF RUNNING LATE — the kill-order (owner-approved, v1.8): compress live in this order, never delete from the deck — ① hardware-slide detail (keep the ×45M punchline) → ② the logo walk on the feature menu (read one row, gesture the rest) → ③ book-list mentions → ④ DeepSeek benchmark detail (keep the bill + hospital). The rebuild rep in Part 3 is PROTECTED — landscape trims first, practice never.\n' +
    'R14: the multimodal aside now lives only in these notes — the slide footer was removed (step 6 above: speak it, nothing to point at).');

  // ---------- 3. PART I DIVIDER ----------
  s = H.slide(null, 3, { dark: true });
  H.partMarker(s, 1);
  s.addText('PART 1 · THE PRIMER', { x: 0.55, y: 2.3, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('Where this came from,\nand how it actually works', { x: 0.55, y: 2.8, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('A short history — the eras, the decade, the hardware — then the six concepts that make you fluent: tokens, context, RAG, the escalation ladder, the token economy, hallucination.', { x: 0.55, y: 4.85, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Dividers are pacing: breathe. Read the two-line title, nothing more.\n' +
    '2) Point at the progress bar: “six parts — this is where we are.”\n' +
    '3) One sentence: “Three history slides — the eras, the decade, the hardware — then six concepts: the vocabulary for everything after.”\n' +
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
    s.addText(e[2], { x: x + 0.86, y: 2.27, w: 2.05, h: 0.42, fontFace: F.body, fontSize: 9, bold: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 0.98 });
    const gx = x + 0.3, gy = 2.82;
    const box = (bx, by, bw, label, tint) => {
      s.addShape('roundRect', { x: bx, y: by, w: bw, h: 0.22, rectRadius: 0.04, fill: { color: tint || 'FFFFFF' }, line: { color: C.TEAL, width: 0.75 } });
      if (label) s.addText(label, { x: bx, y: by, w: bw, h: 0.22, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 8, color: C.TEAL_DARK, margin: 0 });
    };
    if (i === 0) {
      box(gx + 0.78, gy, 0.8, 'if…?');
      box(gx + 0.08, gy + 0.4, 0.8, 'then A'); box(gx + 1.5, gy + 0.4, 0.8, 'else B');
      s.addShape('line', { x: gx + 0.5, y: gy + 0.22, w: 0.55, h: 0.18, line: { color: C.TEAL, width: 1 }, flipH: true });
      s.addShape('line', { x: gx + 1.32, y: gy + 0.22, w: 0.55, h: 0.18, line: { color: C.TEAL, width: 1 } });
    } else if (i === 1) {
      const L1 = [0, 0.22, 0.44], L2 = [0.11, 0.33];
      const seg = (sx, sy, sw, sh) => s.addShape('line', { x: sw < 0 ? sx + sw : sx, y: sh < 0 ? sy + sh : sy, w: Math.abs(sw), h: Math.abs(sh), line: { color: C.LINE, width: 0.9 }, flipH: sw < 0, flipV: sh < 0 });
      L1.forEach(dy => L2.forEach(dy2 => seg(gx + 0.3, gy + dy + 0.07, 0.85, dy2 - dy)));
      L2.forEach(dy2 => seg(gx + 1.3, gy + dy2 + 0.07, 0.75, 0.15 - dy2 + 0.07));
      L1.forEach(dy => s.addShape('ellipse', { x: gx + 0.16, y: gy + dy, w: 0.15, h: 0.15, fill: { color: C.TEAL }, line: { type: 'none' } }));
      L2.forEach(dy => s.addShape('ellipse', { x: gx + 1.16, y: gy + dy, w: 0.15, h: 0.15, fill: { color: C.TEAL }, line: { type: 'none' } }));
      s.addShape('ellipse', { x: gx + 2.06, y: gy + 0.22, w: 0.15, h: 0.15, fill: { color: C.AMBER }, line: { type: 'none' } });
    } else if (i === 2) {
      box(gx, gy + 0.2, 0.55, 'The'); box(gx + 0.6, gy + 0.2, 0.6, 'audit'); box(gx + 1.25, gy + 0.2, 0.4, 'is');
      s.addShape('line', { x: gx + 1.68, y: gy + 0.31, w: 0.25, h: 0, line: { color: C.TEAL, width: 1.25, endArrowType: 'triangle' } });
      s.addShape('roundRect', { x: gx + 1.98, y: gy + 0.2, w: 0.42, h: 0.22, rectRadius: 0.04, fill: { color: C.TEAL }, line: { type: 'none' } });
      s.addText('…?', { x: gx + 1.98, y: gy + 0.2, w: 0.42, h: 0.22, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 8, bold: true, color: 'FFFFFF', margin: 0 });
    } else {
      box(gx, gy + 0.08, 0.68, 'PLAN'); box(gx + 0.86, gy + 0.08, 0.62, 'ACT'); box(gx + 1.66, gy + 0.08, 0.74, 'CHECK');
      s.addShape('line', { x: gx + 0.7, y: gy + 0.19, w: 0.14, h: 0, line: { color: C.TEAL, width: 1, endArrowType: 'triangle' } });
      s.addShape('line', { x: gx + 1.5, y: gy + 0.19, w: 0.14, h: 0, line: { color: C.TEAL, width: 1, endArrowType: 'triangle' } });
      s.addShape('line', { x: gx + 0.34, y: gy + 0.48, w: 1.72, h: 0, line: { color: C.TEAL, width: 1, beginArrowType: 'triangle' } });
    }
    s.addText(e[3], { x: x + 0.24, y: 3.52, w: 2.5, h: 1.18, fontFace: F.body, fontSize: 10.5, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.05 });
    s.addText(e[4], { x: x + 0.24, y: 4.72, w: 2.5, h: 0.66, fontFace: F.body, fontSize: 9.5, italic: true, color: C.TEAL_DARK, margin: 0, lineSpacingMultiple: 1.02 });
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
  s.addText('Months to reach 100 million users — shorter bar = faster', { x: 8.6, y: 2.28, w: 3.9, h: 0.5, fontFace: F.body, fontSize: 10.5, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.05 });
  H.hbar(s, 8.6, 3.0, 3.9, 'ChatGPT', 2 / 30, '2 mo', C.TEAL, { labW: 1.15, b: true });
  H.hbar(s, 8.6, 3.5, 3.9, 'TikTok', 9 / 30, '~9 mo', C.SLATE, { labW: 1.15 });
  H.hbar(s, 8.6, 4.0, 3.9, 'Instagram', 30 / 30, '~30 mo', C.SLATE, { labW: 1.15 });
  s.addText('Fastest consumer ramp on record (UBS/Reuters, 2023).', { x: 8.6, y: 4.55, w: 3.9, h: 0.55, fontFace: F.body, fontSize: 10, italic: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('The methods on the left are the vocabulary for the whole course — each returns on a later slide.', { x: 8.6, y: 5.35, w: 3.9, h: 0.95, fontFace: F.body, fontSize: 10.5, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.1 });
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

  // ---------- 5b. THE HARDWARE STORY (v1.7, r22) ----------
  s = H.slide('PART 1 · A SHORT HISTORY', 6);
  H.title(s, 'Why AI happened now', 'The hardware story — chips, Nvidia, data centers');
  H.card(s, 0.55, 1.62, 3.6, 2.28, C.PANEL);
  s.addText('① A 60-year tailwind', { x: 0.8, y: 1.76, w: 3.1, h: 0.32, fontFace: F.head, fontSize: 13.5, bold: true, color: C.TEAL_DARK, margin: 0 });
  s.addText([
    { text: 'Moore’s law (1965): ', options: { bold: true, color: C.INK, fontSize: 11 } },
    { text: 'chips double their transistors every ~2 years.', options: { color: C.SLATE, fontSize: 11, breakLine: true, paraSpaceAfter: 4 } },
    { text: '1971: 2,300 → 2024: 208 billion', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 4 } },
    { text: '2026 status: slowing to ~3-year doublings — not dead, no longer enough alone.', options: { color: C.SLATE, fontSize: 10, italic: true } },
  ], { x: 0.8, y: 2.12, w: 3.1, h: 1.7, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.06 });
  H.card(s, 0.55, 4.02, 3.6, 2.28, C.TEAL_TINT);
  s.addText('② The accident', { x: 0.8, y: 4.16, w: 3.1, h: 0.32, fontFace: F.head, fontSize: 13.5, bold: true, color: C.TEAL_DARK, margin: 0 });
  s.addText([
    { text: 'Gaming chips WERE AI chips: ', options: { bold: true, color: C.INK, fontSize: 11 } },
    { text: 'both need millions of tiny calculations at once.', options: { color: C.SLATE, fontSize: 11, breakLine: true, paraSpaceAfter: 4 } },
    { text: '2006 — Nvidia’s CUDA lets anyone program a graphics card.', options: { color: C.SLATE, fontSize: 10.5, breakLine: true, paraSpaceAfter: 4 } },
    { text: '2012 — AlexNet: two consumer gaming cards, six days, beats 30 years of hand-built AI.', options: { bold: true, color: C.INK, fontSize: 10.5 } },
  ], { x: 0.8, y: 4.52, w: 3.1, h: 1.7, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.06 });
  // — chart: Moore's pace vs AI's appetite (log scale; Epoch AI data, r22) —
  H.card(s, 4.3, 1.62, 4.55, 4.68, C.PANEL);
  s.addText('③ Moore’s pace vs AI’s appetite', { x: 4.55, y: 1.76, w: 4.1, h: 0.32, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  s.addText('Y axis: training compute per model, in FLOP (one FLOP = one arithmetic operation) — log scale', { x: 4.55, y: 2.08, w: 4.15, h: 0.42, fontFace: F.body, fontSize: 10, color: C.SLATE, margin: 0, lineSpacingMultiple: 0.98 });
  const hwPts = [[2012, 17.67, 'AlexNet'], [2019, 21.28, 'GPT-2'], [2020, 23.49, 'GPT-3'], [2023, 25.32, 'GPT-4 (est.)']];
  [[18, '10\u00b9\u2078'], [21, '10\u00b2\u00b9'], [24, '10\u00b2\u2074']].forEach(tk => {
    const ty = 5.42 - (tk[0] - 17) / 9 * 2.85;
    s.addShape('line', { x: 4.74, y: ty, w: 0.06, h: 0, line: { color: C.MUTE, width: 1 } });
    s.addText(tk[1], { x: 4.3, y: ty - 0.1, w: 0.42, h: 0.2, align: 'right', fontFace: F.body, fontSize: 8.5, color: C.MUTE, margin: 0 });
  });
  const hwX = yr => 4.78 + (yr - 2012) / 11 * 3.5;
  const hwY = lg => 5.42 - (lg - 17) / 9 * 2.85;
  s.addShape('line', { x: hwX(2012), y: hwY(19.33), w: hwX(2023) - hwX(2012), h: hwY(17.67) - hwY(19.33), line: { color: C.MUTE, width: 1.5, dashType: 'dash' }, flipV: true });
  for (let i = 0; i < hwPts.length - 1; i++) {
    const [x1, y1] = [hwX(hwPts[i][0]), hwY(hwPts[i][1])];
    const [x2, y2] = [hwX(hwPts[i + 1][0]), hwY(hwPts[i + 1][1])];
    s.addShape('line', { x: x1, y: y2, w: x2 - x1, h: y1 - y2, line: { color: C.TEAL, width: 2 }, flipV: true });
  }
  hwPts.forEach((p, pi) => {
    s.addShape('ellipse', { x: hwX(p[0]) - 0.06, y: hwY(p[1]) - 0.06, w: 0.12, h: 0.12, fill: { color: C.TEAL_DARK }, line: { type: 'none' } });
    if (pi === 0) s.addText(p[2], { x: hwX(p[0]) + 0.1, y: hwY(p[1]) - 0.28, w: 1.0, h: 0.22, fontFace: F.body, fontSize: 8.5, bold: true, color: C.TEAL_DARK, margin: 0 });
    else s.addText(p[2], { x: hwX(p[0]) - 0.95, y: hwY(p[1]) - 0.3, w: 1.0, h: 0.22, align: 'right', fontFace: F.body, fontSize: 8.5, bold: true, color: C.TEAL_DARK, margin: 0 });
  });
  s.addText('Moore’s pace', { x: hwX(2023) - 1.0, y: hwY(19.33) + 0.05, w: 1.1, h: 0.2, align: 'right', fontFace: F.body, fontSize: 8.5, italic: true, color: C.MUTE, margin: 0 });
  s.addText('2012', { x: hwX(2012) - 0.2, y: 5.5, w: 0.5, h: 0.2, fontFace: F.body, fontSize: 8.5, color: C.MUTE, margin: 0 });
  s.addText('2023', { x: hwX(2023) - 0.25, y: 5.5, w: 0.5, h: 0.2, fontFace: F.body, fontSize: 8.5, color: C.MUTE, margin: 0 });
  s.addText([
    { text: 'At Moore’s pace since 2012: ×45.  ', options: { color: C.SLATE, fontSize: 10 } },
    { text: 'Actual: ×45,000,000.', options: { bold: true, color: C.RED, fontSize: 11.5, breakLine: true } },
    { text: 'GPT-4 ≈ 2×10²⁵ FLOP: ~200,000 years on AlexNet’s two cards — a ~25,000-GPU data-center hall: ~3 months.', options: { color: C.SLATE, fontSize: 9.5 } },
  ], { x: 4.55, y: 5.68, w: 4.15, h: 0.6, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.02 });
  H.card(s, 9.1, 1.62, 3.65, 4.68, C.PANEL);
  s.addText('④ Why the data centers', { x: 9.35, y: 1.76, w: 3.2, h: 0.32, fontFace: F.head, fontSize: 13.5, bold: true, color: C.TEAL_DARK, margin: 0 });
  const dcTiles = [
    ['cpu', 'TRAIN', 'One frontier model: 16,000+ GPUs running for months (Llama 3.1, 2024).'],
    ['users', 'SERVE', 'Then a billion people use it — around the clock, every day.'],
    ['zap', 'POWER', 'One large AI data center ≈ the electricity of 100,000 homes; the biggest under construction ≈ 2 million (IEA).'],
  ];
  dcTiles.forEach((t, i) => {
    const y = 2.2 + i * 1.28;
    H.iconCircle(s, 9.35, y, 0.46, t[0], C.TEAL);
    s.addText([
      { text: t[1] + ' — ', options: { bold: true, color: C.INK, fontSize: 11 } },
      { text: t[2], options: { color: C.SLATE, fontSize: 10.5 } },
    ], { x: 9.93, y: y - 0.1, w: 2.7, h: 1.2, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.04 });
  });
  s.addText('~$700B of build-out planned for 2026 — much announced, not yet built.', { x: 9.35, y: 5.9, w: 3.2, h: 0.5, fontFace: F.body, fontSize: 10, italic: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 1.02 });
  H.card(s, 0.55, 6.42, 12.2, 0.68, C.AMBER_TINT);
  H.logo(s, 0.72, 6.55, 0.42, 'nvidia', 'N');
  s.addText([
    { text: 'The shovel-seller: ', options: { bold: true, color: C.INK, fontSize: 11.5 } },
    { text: 'Nvidia — first reached $1T May 2023 · $4T Jul 2025 · $5T Oct 2025 · ~$5.6T today: the world’s most valuable company, and 92% of its revenue is now AI data centers.', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 1.28, y: 6.5, w: 11.3, h: 0.52, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.02 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “software got the headlines — hardware made it possible. Four beats, left to right.”\n' +
    '2) ① Moore’s law in one sentence: chips doubled their transistors every ~2 years for 50 years — 1971: 2,300; 2024: 208 billion, ~90 million times more. Status 2026: slowing to ~3-year doublings, not dead.\n' +
    '3) ② The accident story, told plainly: in 2012 three university researchers couldn’t afford a supercomputer, so they trained their network on TWO consumer gaming cards. Six days later it beat 30 years of hand-built AI. Every AI company today is still scaling up that trick. (CUDA, 2006, is why it was even possible — Nvidia had let anyone program a graphics card, and had a five-year head start when AI came calling.)\n' +
    '4) ③ The chart — the punchline of the slide: if AI compute had grown at Moore’s pace since 2012 it would be ~45× bigger. It is ~45 MILLION times bigger. The gap was bought with chips, clusters, and electricity — that gap IS the data-center boom.\n' +
    '5) ④ Train / serve / power — and the honest caveat aloud: a lot of what you read about is ANNOUNCED, not built.\n' +
    '6) Amber band — the shovel-seller: the most valuable company on Earth makes no chatbot, no phone, no search engine. It sells the shovels. Ten years ago it was “the video-game graphics company.” (This tees up Part 2: when one cheap Chinese model made investors doubt how many shovels are needed, Nvidia lost $589B in a day.)\n' +
    '\n' +
    'BRIDGE —\n' +
    '“That’s the machinery. Now — what is the model itself actually doing? Under the hood.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'GPU = Graphics Processing Unit — thousands of simple cores doing the same math at once (a CPU: a few smart cores, one task at a time).\n' +
    'CUDA = Nvidia’s software for running ANY computation on its graphics chips (2006) — the moat is the software, not just the chips.\n' +
    'IEA = International Energy Agency. FLOP = floating-point operation (the compute unit behind the chart).\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.7 new slide (owner request: Moore’s law, Nvidia’s role, chips⇄AI, why data centers — intro level). Every fact sourced in notes/research/r22_hardware_story.md: Moore 1965/1975 · Intel-CEO 3-year cadence · Blackwell 208B transistors (Mar 2024) · CUDA 2006 · AlexNet two GTX 580s (NeurIPS 2012 paper) · chart = Epoch AI database (GPT-4 point is an ESTIMATE — labeled) · Llama 3.1 16,000+ H100s (Meta, Jul 2024) · IEA Apr 2025 (415 TWh 2024 → ~945 TWh 2030; 100K-homes comparison) · capex ~$700B+ 2026 (CNBC Feb 2026, analyst tallies vary) · Nvidia milestones $1T–$5T with dates + ~$5.56T and 92% data-center revenue (Q2 FY2027, Aug 2026).\n' +
    'If asked about “Huang’s law” (AI chips beating Moore’s law): Nvidia’s claim for whole SYSTEMS; independent measurement (Epoch) puts GPU price-performance doubling at ~2.5 years — say “the marketing outruns the measurement.”\n' +
    'Stargate, if asked: announced Jan 2025 at “up to $500B”; by mid-2026 ~7 GW PLANNED across 7 US sites, first campus (Abilene, TX) partially live — announced ≠ built.\n' +
    'US–China chip angle, one line if asked: US export restrictions since Oct 2022; an Apr 2025 license rule forced Nvidia to write down $5.5B on its China-market chip.\n' +
    'v1.12 Y-AXIS, made explicit (owner request): the axis is TRAINING COMPUTE in FLOP — floating-point operations, one FLOP = one arithmetic operation (a single multiply or add) — on a log scale from 10^17 to 10^26; ticks at 10^18 / 10^21 / 10^24. Say it as one variable: “everything on this chart is counted in the same unit — how many little arithmetic operations it took to train the model.” The data-center equivalence under the chart: GPT-4 ≈ 2.1×10^25 FLOP (Epoch estimate). On AlexNet’s two GTX 580s (~3.2×10^12 FLOP/s combined, perfect efficiency) that is ~2×10^5 years — the “~200,000 years” line, an arithmetic illustration, not a measured fact. The “~25,000-GPU hall, ~3 months” figure is the widely reported industry estimate for GPT-4’s training cluster (SemiAnalysis-derived; vendor-unconfirmed — say “reported estimate” if pressed). One more anchor if useful: Llama 3.1 on the TRAIN tile used 16,000+ GPUs — that IS a data-center hall; the chart is why those halls exist.');

  // ---------- 6. HOW AN LLM WORKS ----------
  s = H.slide('PART 1 · HOW LLMS WORK', 6);
  H.title(s, 'Under the hood', 'A prediction engine, sent to finishing school');
  s.addImage({ path: require('path').join(__dirname, 'assets', 'images', 'robot_graduate.jpg'), x: 11.5, y: 0.3, w: 1.12, h: 1.12, sizing: { type: 'cover', w: 1.12, h: 1.12 } });
  s.addShape('roundRect', { x: 11.5, y: 0.3, w: 1.12, h: 1.12, rectRadius: 0.06, fill: { type: 'none' }, line: { color: C.LINE, width: 1 } });
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
    s.addText(p[2], { x: x + 0.28, y: 2.68, w: 3.42, h: 1.3, fontFace: F.body, fontSize: 10.5, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.04 });
    if (i < 2) H.arrow(s, x + 3.97, 2.75, 0.2, C.TEAL);
  });
  H.callout(s, 0.55, 4.16, 6.0, 1.12, C.TEAL_TINT, [
    { text: 'Knowledge is frozen at the cutoff — with escape hatches. ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true } },
    { text: 'Training ends months before release. Many assistants compensate: live web search pulls today’s pages into the prompt; RAG (concept 3) plugs in your own documents.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'clock', iconFill: C.TEAL, size: 11 });
  H.callout(s, 6.75, 4.16, 6.0, 1.12, C.AMBER_TINT, [
    { text: 'Why prompting exists: ', options: { bold: true, color: C.INK, fontSize: 11.5, breakLine: true } },
    { text: 'the model completes your text — the prompt is the only steering wheel you have. A complete prompt doesn’t make the model smarter: it deletes wrong guesses.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'compass', iconFill: C.AMBER, size: 11 });
  H.promptChip(s, 0.55, 5.34, 12.2, 1.74, 2, [
    { type: '“Finish this sentence 5 different ways: We should move the launch date because”', why: 'no facts yet — watch it scatter across guesses.' },
    { type: '“Now 5 more ways, knowing: B2B software firm, competitor launches May 3, our beta ends April 20.”', why: 'your facts didn’t make it smarter — they deleted wrong guesses.' },
  ], { label: 'Narrowing the guesses — two separate sends', size: 10, tab: 'EX2-Guesses' });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Title metaphor first: “a prediction engine, sent to finishing school.”\n' +
    '2) Three cards LEFT TO RIGHT — pretraining, instruction tuning, human feedback. On card 3, land the after-ship line: RLHF never really stops — every thumbs-up/down you click, and on personal accounts your chats themselves, become the preference data that trains the next model. (That is exactly what “trains on your data by default” means on the trust slide in Part 2.)\n' +
    '3) LEFT callout: the cutoff — AND its two escape hatches: live web search, and RAG for your own documents.\n' +
    '4) RIGHT callout, slowly — the thesis of the course: the prompt is the only steering wheel; a complete prompt DELETES WRONG GUESSES.\n' +
    '\n' +
    'TRY IT — PROMPT 2/7 (two sends; copy from tab EX2-Guesses)\n' +
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
    'v1.6: cutoff callout gains the web-search/RAG escape hatches; RLHF card gains the after-ship story (owner request).\n' +
    'ART — the corner graduation robot is an owner-generated illustration (R16): the “finishing school” of the subtitle, literally.');

  // ---------- 7. TOKENS ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 7);
  H.title(s, 'Concept 1 · Tokens', 'The model reads bricks, not letters');
  H.bullets(s, 0.55, 1.66, 6.2, 2.95, [
    { t: 'Text is chopped into tokens — word chunks from a fixed vocabulary. Common words are one token; rare ones get built from pieces (“ham·bur·ger”).' },
    { t: 'Rules of thumb (English): 1 token ≈ 4 characters ≈ ¾ of a word. A 50-page document ≈ 25–35K tokens.' },
    { t: 'The model never sees letters — “strawberry” arrives as one or two IDs. The famous letter-counting fails of 2024 are patched now; what still breaks: exact word counts and “count your own tokens” (every tier), character-precise edits (free/fast tiers).', b: true },
    { t: 'Everything is priced and limited in tokens — input and output. Output tokens cost ~5× input, because generation is serial.' },
  ], { size: 11.8, gap: 8 });
  H.card(s, 7.0, 1.66, 5.75, 2.72, C.PANEL);
  s.addText('LEGO bricks of text', { x: 7.3, y: 1.82, w: 5.2, h: 0.32, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
  s.addImage({ path: require('path').join(__dirname, 'assets', 'images', 'lego_tokens.jpg'), x: 7.3, y: 2.18, w: 2.9, h: 1.63, sizing: { type: 'cover', w: 2.9, h: 1.63 } });
  s.addShape('roundRect', { x: 7.3, y: 2.18, w: 2.9, h: 1.63, rectRadius: 0.04, fill: { type: 'none' }, line: { color: C.LINE, width: 0.75 } });
  s.addText('Common words are pre-molded bricks; rare words get built from pieces. You pay by the brick.', { x: 10.32, y: 2.18, w: 2.15, h: 1.63, fontFace: F.body, fontSize: 11, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 1.06 });
  const chips = [['Analyzing', 0.95], ['the', 0.45], ['supplier', 0.85], ['’s', 0.3], ['first', 0.55], ['-', 0.22], ['pass', 0.55], ['yield', 0.6]];
  let cx = 7.3;
  chips.forEach((ch, i) => {
    const fillCol = i % 2 ? 'FFFFFF' : C.TEAL_TINT;
    const nStuds = ch[1] > 0.5 ? 2 : 1;
    for (let st = 0; st < nStuds; st++) {
      const sx = cx + (ch[1] / (nStuds + 1)) * (st + 1) - 0.05;
      s.addShape('roundRect', { x: sx, y: 3.9, w: 0.1, h: 0.1, rectRadius: 0.02, fill: { color: fillCol }, line: { color: C.TEAL, width: 0.75 } });
    }
    s.addShape('roundRect', { x: cx, y: 3.98, w: ch[1], h: 0.36, rectRadius: 0.04, fill: { color: fillCol }, line: { color: C.TEAL, width: 0.75 } });
    s.addText(ch[0], { x: cx, y: 3.99, w: ch[1], h: 0.34, align: 'center', valign: 'middle', fontFace: 'Consolas', fontSize: 9.5, color: C.TEAL_DARK, margin: 0 });
    cx += ch[1] + 0.06;
  });
  H.callout(s, 7.0, 4.46, 5.75, 1.44, C.TEAL_TINT, [
    { text: 'So what, for daily work: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5, breakLine: true } },
    { text: 'paste-heavy prompts burn budget and context fast · non-English and dense technical text cost more tokens · use AI for language, software for characters (counts, checksums, exact IDs).', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'layers', iconFill: C.TEAL, size: 11 });
  H.promptChip(s, 0.55, 4.78, 6.2, 2.3, 3, [
    { type: '“Explain AI tokens to a high-school student in under 80 words: use a LEGO-brick analogy, show one word splitting into tokens, and end with why tokens set my AI’s cost and limits.”', why: 'the definition lands in your course log — the analogy the best explainers use.' },
  ], { label: 'Bricks, not letters', size: 10, tab: 'EX3-Tokens' });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Title first: “the model reads bricks, not letters.”\n' +
    '2) Left bullets; STOP on the bold third and tell the story ARC: 2024 — models famously miscounted the r’s in “strawberry” and the internet laughed; 2025 — vendors patched it (partly memorization: days after GPT-5 launched, its FAST path insisted “blueberry” has three b’s while its thinking path got it right); 2026 — the lesson that never changed: it reads bricks, not letters. NEVER run strawberry or blueberry live — both are famous now.\n' +
    '3) Right card: the brick strip — “this is exactly how your sentence arrives: eight bricks, eight numbers.”\n' +
    '4) THE live demo (safe — it shows the bricks, it can’t “get it right”): open platform.openai.com/tokenizer (PRELOAD it; backup: tiktokenizer.vercel.app) and paste attendees’ NAMES and company jargon — common words stay whole, rare words shatter into colored chunks.\n' +
    '5) Near-safe live model variant if the room wants proof from the AI itself: ask “how many tokens is this paragraph?” then show the real count on the tokenizer page — models cannot count their own tokens, on ANY tier, and the reveal is exactly the lesson.\n' +
    '6) Teal card: the three daily-work consequences.\n' +
    '\n' +
    'TRY IT — PROMPT 3/7 (copy from tab EX3-Tokens)\n' +
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
    'v1.7: capability claim re-verified 2026-09-10 (r23_tokens_grok_hallucination.md, owner challenge): strawberry-class counting is fixed on current frontier models (partly memorized — the Aug-2025 blueberry incident); still failing with evidence: character-position edits ~33–44% accuracy on non-reasoning tiers (CharBench 2025/26) · paragraph-scale letter counts on fast tiers · exact word counts on ALL tiers · counting own tokens on ALL tiers (arXiv:2502.06258). Reasoning modes pass letter tasks by spelling out — a paid, token-burning workaround, not letter-vision. Re-verify at every refresh; this claim ages fast.\n' +
    'v1.6: prompt finalized from the explainer research (r17) — LEGO validated as the dominant popular analogy; tokenizer-page demo recommended over any word trick.\n' +
    'Token math preview: tokens also explain context windows (next slide) and the bill (later this part).\n' +
    'ART — the LEGO wall + robot hand at the top of the right card is an owner-generated illustration (R16).');

  // ---------- 8. CONTEXT WINDOW ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 8);
  H.title(s, 'Concept 2 · Context window', 'A desk, not a filing cabinet');
  H.bullets(s, 0.55, 1.62, 6.2, 2.6, [
    { t: 'The context window is working memory for one conversation: your question, the system prompt, chat history, attached files, and search results must all fit on the desk.' },
    { t: 'Close the chat and the desk is swept clean. Nothing persists unless a memory feature or a saved file re-loads it.' },
    { t: 'By 2026, ~1M tokens (≈750,000 words) is the flagship standard. Consumer apps often enforce smaller limits than the raw model.' },
    { t: 'In very long chats the middle gets skimmed — accuracy is highest at the start and the end (“lost in the middle”).', b: true },
  ], { size: 12, gap: 7 });
  H.card(s, 7.0, 1.62, 5.75, 2.46, C.PANEL);
  s.addText('What’s on the desk right now', { x: 7.3, y: 1.76, w: 5.2, h: 0.3, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
  s.addImage({ path: require('path').join(__dirname, 'assets', 'images', 'desk_cabinet.jpg'), x: 7.3, y: 2.12, w: 2.6, h: 1.46, sizing: { type: 'cover', w: 2.6, h: 1.46 } });
  s.addShape('roundRect', { x: 7.3, y: 2.12, w: 2.6, h: 1.46, rectRadius: 0.04, fill: { type: 'none' }, line: { color: C.LINE, width: 0.75 } });
  const deskItems = [['file', 'System prompt & instructions'], ['chat', 'Every prior turn — both sides'], ['paperclip', 'Attached documents'], ['search', 'Tool & search results']];
  deskItems.forEach((d, i) => {
    const y = 2.12 + i * 0.48;
    H.iconCircle(s, 10.04, y + 0.07, 0.32, d[0], C.SLATE);
    s.addText(d[1], { x: 10.46, y, w: 2.2, h: 0.46, fontFace: F.body, fontSize: 11, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.95 });
  });
  H.callout(s, 7.0, 4.12, 5.75, 1.1, C.TEAL_TINT, [
    { text: 'Habits that exploit the desk: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11, breakLine: true } },
    { text: '① long documents at the TOP, question at the END (up to ~30% better answers) · ② label multiple documents · ③ new topic → new chat · ④ long thread → run the handoff move below.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'check', iconFill: C.TEAL, size: 11 });
  H.card(s, 0.55, 4.26, 6.2, 0.94, C.AMBER_TINT);
  s.addText([
    { text: 'A desk with a filing cabinet? ', options: { bold: true, color: C.INK, fontSize: 11 } },
    { text: 'Persistent files, notes and standing instructions are what agentic tools bolt onto the desk — Part 5. Pros call this CONTEXT ENGINEERING: the prompt is the briefing; context is everything on the desk — even what nobody typed.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { x: 0.85, y: 4.3, w: 5.7, h: 0.86, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.03 });
  H.promptChip(s, 0.55, 5.28, 12.2, 1.8, 4, [
    { type: '“Explain your context window like I’m a 5th grader: the desk, what fits on it, and what happens when I close this chat. Under 100 words.”', why: 'the AI describes its own working memory, plainly.' },
    { type: '(homework) “Summarize our chat so far in under 80 words, titled HANDOFF.”', why: 'tonight, paste into a fresh chat, ask “where was I?” — it picks up your course.' },
  ], { label: 'The desk — explained, then carried', size: 10, tab: 'EX4-Handoff' });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) The analogy first: “a desk, not a filing cabinet.”\n' +
    '2) Left bullets; on the bold one, draw the U-shape in the air — attention high at the start, sags in the middle, high at the end.\n' +
    '3) Right card: the four things on the desk right now.\n' +
    '4) Teal card: the four habits — habit ④ is about to be performed.\n' +
    '5) Amber card: one sentence — the filing-cabinet teaser for Part 5. Plant the seed, move on.\n' +
    '\n' +
    'TRY IT — PROMPT 4/7 (copy from tab EX4-Handoff)\n' +
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
    '1M-token flagship standard verified Aug 2026 across Claude, GPT-5.x, Gemini, and the Chinese open-weight flagships.\n' +
    'v1.8: CONTEXT ENGINEERING named on the amber card (external-review adoption, 9B-2): the prompt is the briefing; context is everything on the desk — files, history, tool results, memory. Part 5 returns to it as the parent discipline of agentic prompting. Glossary entry added.\n' +
    'ART — the desk + filing-cabinet header in the right card is an owner-generated illustration (R16).');

  // ---------- 9. RAG ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 9);
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
    H.card(s, x, 1.98, 2.85, 2.3, C.PANEL);
    H.iconCircle(s, x + 0.24, 2.18, 0.48, st[0], C.TEAL);
    s.addText(st[1], { x: x + 0.24, y: 2.76, w: 2.4, h: 0.35, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
    s.addText(st[2], { x: x + 0.24, y: 3.12, w: 2.42, h: 1.1, fontFace: F.body, fontSize: 11, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.04 });
    if (i < 3) H.arrow(s, x + 2.87, 3.0, 0.3, C.TEAL);
  });
  H.card(s, 0.55, 4.48, 4.3, 1.8, C.GREEN_TINT);
  s.addText([
    { text: 'Why enterprises build on it: ', options: { bold: true, color: C.INK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'current (re-index in minutes, no retraining) · checkable (citations to the exact passage) · private (retrieval feeds one answer, teaches the model nothing) · access-aware.', options: { color: C.SLATE, fontSize: 10.8 } },
  ], { x: 0.82, y: 4.62, w: 3.8, h: 1.54, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.05 });
  H.card(s, 4.99, 4.48, 4.3, 1.8, C.RED_TINT);
  s.addText([
    { text: 'The failure mode to respect: ', options: { bold: true, color: C.RED, fontSize: 11.5, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'fetch the wrong page — an outdated revision, a near-miss document — and the model still writes a fluent, confident, CITED answer from it. Check the citation, not just the prose.', options: { color: C.SLATE, fontSize: 10.8 } },
  ], { x: 5.26, y: 4.62, w: 3.8, h: 1.54, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.05 });
  s.addImage({ path: require('path').join(__dirname, 'assets', 'images', 'open_book.jpg'), x: 9.43, y: 4.48, w: 3.32, h: 1.8, sizing: { type: 'cover', w: 3.32, h: 1.8 } });
  s.addShape('roundRect', { x: 9.43, y: 4.48, w: 3.32, h: 1.8, rectRadius: 0.06, fill: { type: 'none' }, line: { color: C.LINE, width: 1 } });
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
    'This is the engine behind internal document assistants and Copilot-over-SharePoint.\n' +
    'ART — the open-book-exam scene (robot writing from the book, librarian delivering a glowing page) is an owner-generated illustration (R16); gesture at it when you say the analogy.');

  // ---------- 10. ESCALATION LADDER — THREE STEPS, ONE WORKED TOPIC ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 10);
  H.title(s, 'Concept 4 · The escalation ladder', 'Prompt it → feed it documents → retrain it');
  const ladder = [
    ['edit', '1 · PROMPT IT', 'instructions to a skilled temp', 'Fixes BEHAVIOR — tone, format, focus, approach.', 'Free · instant · every model. 90% of the value — this course.'],
    ['book', '2 · FEED IT DOCUMENTS', 'hand the temp your binder (RAG)', 'Fixes MISSING KNOWLEDGE — your policies, your data, current facts.', 'Minutes to set up · citable · private. Most real cases end here.'],
    ['cpu', '3 · RETRAIN IT', 'send it back to school (fine-tuning)', 'Changes deep HABITS — permanently.', 'Slow · expensive · per-model. Rare: an IT project, not a prompt.'],
  ];
  ladder.forEach((l, i) => {
    const x = 0.55 + i * 4.18;
    H.card(s, x, 1.62, 3.95, 2.55, i === 0 ? C.TEAL_TINT : C.PANEL);
    H.iconCircle(s, x + 0.26, 1.84, 0.6, l[0], C.TEAL);
    s.addText(l[1], { x: x + 1.0, y: 1.92, w: 2.85, h: 0.42, fontFace: F.head, fontSize: 15.5, bold: true, color: C.TEAL_DARK, margin: 0 });
    s.addText(l[2], { x: x + 0.26, y: 2.56, w: 3.45, h: 0.34, fontFace: F.body, fontSize: 11, italic: true, color: C.RED, margin: 0 });
    s.addText(l[3], { x: x + 0.26, y: 2.94, w: 3.45, h: 0.6, fontFace: F.body, fontSize: 11.5, bold: true, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.04 });
    s.addText(l[4], { x: x + 0.26, y: 3.58, w: 3.45, h: 0.52, fontFace: F.body, fontSize: 10.5, color: C.MUTE, margin: 0, lineSpacingMultiple: 1.02 });
    if (i < 2) H.arrow(s, x + 3.97, 2.75, 0.2, C.TEAL);
  });
  H.card(s, 0.55, 4.42, 12.2, 1.78, C.PANEL);
  s.addText('One topic, up the ladder — “answer customer questions about our warranty policy”', { x: 0.85, y: 4.56, w: 11.6, h: 0.35, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
  const rungEx = [
    ['①', '“Answer in plain language and quote the exact clause.” Answers get clear and consistent — but it doesn’t KNOW our policy, so the details are guesses.'],
    ['②', 'Upload the warranty documents (or use the company assistant). Now: current, cited answers from the real text. This is where you stop.'],
    ['③', 'Retrain — only if millions of chats must carry a deep habit with no room for instructions. An IT decision, not a prompt.'],
  ];
  rungEx.forEach((r, i) => {
    const x = 0.85 + i * 4.0;
    s.addText([
      { text: r[0] + '  ', options: { bold: true, color: C.TEAL, fontSize: 15 } },
      { text: r[1], options: { color: C.SLATE, fontSize: 11 } },
    ], { x, y: 4.98, w: 3.8, h: 1.15, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.06 });
  });
  H.callout(s, 0.55, 6.4, 12.2, 0.68, C.AMBER_TINT, [
    { text: 'One question picks the rung: ', options: { bold: true, color: C.INK, fontSize: 12.5 } },
    { text: 'is the AI missing knowledge → feed it documents. Misbehaving with knowledge it has → prompt it. Retraining stays rare.', options: { color: C.SLATE, fontSize: 12.5 } },
  ], { iconName: 'help', iconFill: C.AMBER, size: 12.5 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) The three big cards LEFT TO RIGHT — say the verbs: prompt it, feed it documents, retrain it. The temp analogies carry it: instructions → binder → back to school.\n' +
    '2) Then the worked topic, ① → ② → ③, warranty questions: prompting fixes the HOW, documents fix the WHAT, and step ② is where almost every real workplace case ends. Step ③ exists so the room knows what it is — and that it isn’t their job.\n' +
    '3) Amber band — the takeaway question, verbatim: missing knowledge → documents; misbehaving → prompt.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Two concepts left — the next one is all about the bill.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'RAG = Retrieval-Augmented Generation (rung 2 — the open-book exam from the previous slide).\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.7: rebuilt as three big sequential steps + one worked topic (owner request); the guided-prompt chip and on-slide drill were cut — the six-problem triage drill survives in workbook tab BONUS-Ladder for self-study (answers: 1 P · 2 R · 3 P · 4 R · 5 F · 6 defensible either way).\n' +
    '“Let’s fine-tune on our procedures” → first ask: knowledge problem (→documents) or behavior problem (→prompt)? Most enterprise cases are knowledge problems.\n' +
    'Frontier flagships mostly aren’t fine-tunable (2026); open-weight models are.\n' +
    'NOTE: this is the ESCALATION ladder (capability). Part 6’s PROMOTION ladder (where prompts live) is a different ladder — name them fully.');

  // ---------- 11. FAST vs THINKING ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 11);
  H.title(s, 'Concept 5 · Fast models vs thinking models', 'Two speeds, one bill');
  H.bullets(s, 0.55, 1.66, 6.2, 2.9, [
    { t: 'Every vendor ships a fast tier — one pass, instant, cheap — and a thinking tier that drafts, checks and revises internally before answering.' },
    { t: 'System 1 vs System 2 (Kahneman’s Thinking, Fast and Slow): fast intuition for routine asks; slow deliberation where being wrong is expensive.' },
    { t: 'The bill: thinking is charged as output tokens — the expensive kind. A hard question can quietly cost 5–20× a simple one.', b: true },
    { t: 'Why the fast tier got so good: MoE (Part 2 tells that story) and big models teaching small ones (distillation).' },
  ], { size: 14, gap: 7 });
  H.card(s, 0.55, 4.75, 6.2, 0.88, C.GREEN_TINT);
  s.addText([
    { text: 'Think ON: ', options: { bold: true, color: C.INK, fontSize: 12 } },
    { text: 'multi-step analysis · math · root-cause work · code · tradeoffs across a long document.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { x: 0.85, y: 4.85, w: 5.7, h: 0.7, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.04 });
  H.card(s, 0.55, 5.75, 6.2, 0.88, C.AMBER_TINT);
  s.addText([
    { text: 'Think OFF: ', options: { bold: true, color: C.INK, fontSize: 12 } },
    { text: 'lookups · reformatting · summaries · routine drafting — deliberation you don’t need.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { x: 0.85, y: 5.85, w: 5.7, h: 0.7, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.04 });
  H.promptChip(s, 7.0, 1.66, 5.75, 2.3, 5, [
    { type: '“Describe your fast mode vs your thinking mode like I’m choosing between them for real work: when is each worth it, and roughly how much more does thinking cost? Under 120 words.”', why: 'the model explains its own two speeds — and its own bill.' },
  ], { label: 'Same brain, two speeds', size: 10.5, tab: 'EX5-TwoSpeeds' });
  H.card(s, 7.0, 4.12, 5.75, 2.5, C.PANEL);
  s.addText('The two speeds, side by side', { x: 7.28, y: 4.26, w: 5.2, h: 0.34, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
  s.addImage({ path: require('path').join(__dirname, 'assets', 'images', 'hare_tortoise.jpg'), x: 7.28, y: 4.68, w: 2.74, h: 1.54, sizing: { type: 'cover', w: 2.74, h: 1.54 } });
  s.addShape('roundRect', { x: 7.28, y: 4.68, w: 2.74, h: 1.54, rectRadius: 0.05, fill: { type: 'none' }, line: { color: C.LINE, width: 0.75 } });
  s.addText([
    { text: 'FAST ', options: { bold: true, color: C.GREEN, fontSize: 11 } },
    { text: '— one pass, instant, cheap. Great until the question has traps.', options: { color: C.SLATE, fontSize: 11, breakLine: true, paraSpaceAfter: 5 } },
    { text: 'THINKING ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11 } },
    { text: '— drafts, checks, revises. 5–20× the cost.', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 10.14, y: 4.68, w: 2.45, h: 1.54, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.04 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Frame: “every AI app sells you two speeds — when is the slow one worth its bill?” Name the book once: Kahneman’s Thinking, Fast and Slow — the owner-favorite narrative of this slide.\n' +
    '2) The BILL bullet is the slow-down: thinking is billed like output — 5–20× a simple ask.\n' +
    '3) Green/amber cards: on for, off for. Escalate on failure, not by default.\n' +
    '\n' +
    'TRY IT — PROMPT 5/7 (copy from tab EX5-TwoSpeeds)\n' +
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
    'v1.7: the on-slide extended-puzzle card was cut (owner: too much); the puzzle survives in the workbook tab’s EXTENDED rows for self-study (answer key: Ben Mon · Chloe Tue · Ema Wed · Ana Thu · Dev Fri).\n' +
    'Thinking tokens billed as output even when you only see a summary; output ≈ 5× input across vendors; effort adaptive/dial-able by 2026 (t4 §5, primary-sourced).\n' +
    'Honest caveat: the model isn’t literally “thinking” — it generates intermediate tokens that improve the final answer.\n' +
    'ART — the sprinting-hare / studying-tortoise panel is an owner-generated illustration (R16): hare = fast tier, tortoise = thinking tier. Name the fable, point at the panel.');

  // ---------- 12. THE FEATURE MENU ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 12);
  H.title(s, 'Concept 5 · The feature menu · continued', 'Where your tokens go');
  H.card(s, 0.55, 1.62, 5.9, 3.5, C.PANEL);
  s.addText('The cost ladder — every vendor sells it', { x: 0.85, y: 1.8, w: 5.3, h: 0.38, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  const ladder2 = [
    ['Quick answer', '1×', 'one pass, instant'],
    ['Thinking / extended reasoning', '5–20×', 'drafts and checks before answering'],
    ['Web search', '+sources', 'grounds the answer in live pages'],
    ['Deep research', '100×+', 'browses for minutes, cited report'],
    ['Agent modes', 'the most', 'plans and acts across many steps'],
  ];
  ladder2.forEach((r, i) => {
    const y = 2.28 + i * 0.56;
    s.addShape('roundRect', { x: 0.85 + i * 0.14, y, w: 2.55, h: 0.46, rectRadius: 0.06, fill: { color: i >= 3 ? C.TEAL : C.TEAL_TINT }, line: { color: C.TEAL, width: 0.75 } });
    s.addText(r[0], { x: 0.9 + i * 0.14, y: y + 0.01, w: 2.45, h: 0.44, fontFace: F.body, fontSize: 9.5, bold: true, color: i >= 3 ? 'FFFFFF' : C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText([
      { text: r[1] + '  ', options: { bold: true, color: C.AMBER, fontSize: 10.5 } },
      { text: r[2], options: { color: C.SLATE, fontSize: 9.5 } },
    ], { x: 4.08, y: y + 0.01, w: 2.3, h: 0.44, fontFace: F.body, margin: 0, valign: 'middle' });
  });
  H.card(s, 6.6, 1.62, 6.15, 3.5, C.PANEL);
  s.addText('What it’s called where you are (Sep 2026)', { x: 6.88, y: 1.8, w: 5.6, h: 0.38, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  const modeNames = [
    ['openai', 'ChatGPT', 'deep research · thinking slider (paid) · “Think” button (free)'],
    ['gemini', 'Gemini', 'Deep Research (all tiers) · Deep Think = separate hard-reasoning mode (Ultra)'],
    ['claude', 'Claude', 'Research (paid plans) · extended thinking'],
    ['copilot', 'Copilot', 'Quick response · Think Deeper · Smart (GPT-5) · Researcher agent'],
    ['perplexity', 'Perplexity', 'Search · Research · Create files and apps'],
    ['grok', 'Grok', 'Auto · Fast · Expert · Heavy (multi-agent, $300 tier) — Think/DeepSearch retired'],
  ];
  modeNames.forEach((m, i) => {
    const y = 2.22 + i * 0.46;
    H.logo(s, 6.88, y + 0.03, 0.36, m[0], m[1][0]);
    s.addText(m[1], { x: 7.34, y, w: 1.07, h: 0.44, fontFace: F.body, fontSize: 11, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText(m[2], { x: 8.45, y, w: 4.15, h: 0.44, fontFace: F.body, fontSize: 9.5, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.95 });
  });
  s.addText('Deep research, demystified: a reasoning model given a browser and time — it plans, reads sources for minutes, and synthesizes a cited report. The MoE story in Part 2 is why that became affordable.', { x: 0.55, y: 5.16, w: 12.2, h: 0.4, fontFace: F.body, fontSize: 11, italic: true, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.05 });
  H.promptChip(s, 0.55, 5.54, 12.2, 1.54, 6, [
    { type: '“List the modes this app gives me — quick answer, thinking, web search, deep research, agent — one line each on what it does differently and its rough effort. Say ‘unsure’ rather than guess.”', why: 'your own product hands you its menu; ask again the day it changes.' },
  ], { label: 'Ask your own product for its menu', size: 10.5, tab: 'EX6-FeatureMenu' });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Left card: climb the staircase — 1× quick answer up to agent modes. The discipline: pick the SMALLEST mode that can succeed; escalate deliberately.\n' +
    '2) Right card: the same ladder under six brand logos — read one row, gesture the rest. Copilot users: your everyday menu is the fourth row. (“Smart (GPT-5)” is the CONSUMER Copilot label; M365 Copilot separately prefers GPT-5.6 — different surfaces, both true.)\n' +
    '3) Italic line: deep research demystified.\n' +
    '\n' +
    'TRY IT — PROMPT 6/7 (copy from tab EX6-FeatureMenu)\n' +
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
    'Mode names verified Sep 9, 2026 — full paper trail with sources: notes/research/r18_mode_names.md. Grok row verified Sep 10, 2026 (r23): Auto · Fast · Expert · Heavy; tiers Free / SuperGrok $30 / Heavy $300 (+X Premium bundles); nothing first-party (x.ai blocks fetch) and default-mode/Expert-gating ambiguous — re-confirm Grok AND the ChatGPT row in the live apps before training day. [REFRESH QUARTERLY.]\n' +
    'The 5–20× multiplier is sourced (r2); the 100×+ deep-research figure is an order-of-magnitude illustration, not a billed rate.\n' +
    'Scaling anecdote for questions: one fast prompt vs an orchestrated multi-agent research run = hundreds of quick answers’ worth of tokens.');

  // ---------- 13. HALLUCINATION — THE FOUR CHARACTERS ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 13);
  H.title(s, 'Concept 6 · Hallucination', 'Fluency is not evidence');
  H.bullets(s, 0.55, 1.62, 5.6, 2.55, [
    { t: 'The mechanism: models are optimized for the most plausible next token, not the most true one. Trouble concentrates where training data is thin: rare facts, citations, numbers, names.' },
    { t: 'OpenAI’s own 2025 research: benchmarks reward confident guessing over “I don’t know” — models learn to be good test-takers.', b: true },
    { t: 'The better word is confabulation: it fills gaps with plausible material, in-format — fake citations LOOK like citations.' },
  ], { size: 14, gap: 6 });
  // — the confident guess, measured (r23: arXiv:2509.04664 + GPT-5 system card) —
  H.card(s, 0.55, 4.32, 5.6, 2.44, C.PANEL);
  s.addText('The confident guess, measured', { x: 0.82, y: 4.46, w: 5.1, h: 0.32, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  const hbars = [
    ['Older reasoning model (o4-mini)', [[24, C.TEAL], [75, C.RED], [1, C.SLATE]]],
    ['Newer, trained to say “I don’t know”', [[22, C.TEAL], [26, C.RED], [52, C.SLATE]]],
  ];
  hbars.forEach((r, i) => {
    const y = 4.9 + i * 0.62;
    s.addText(r[0], { x: 0.82, y: y - 0.08, w: 5.0, h: 0.24, fontFace: F.body, fontSize: 9.5, bold: true, color: C.SLATE, margin: 0 });
    let bx = 0.82;
    r[1].forEach(seg => {
      const w = 4.55 * seg[0] / 100;
      s.addShape('rect', { x: bx, y: y + 0.16, w, h: 0.2, fill: { color: seg[1] }, line: { color: 'FFFFFF', width: 0.5 } });
      if (seg[0] >= 10) s.addText(`${seg[0]}%`, { x: bx, y: y + 0.14, w, h: 0.24, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 8.5, bold: true, color: 'FFFFFF', margin: 0 });
      bx += w;
    });
  });
  s.addText([
    { text: '■', options: { color: C.TEAL, fontSize: 9 } }, { text: ' right  ', options: { color: C.SLATE, fontSize: 9 } },
    { text: '■', options: { color: C.RED, fontSize: 9 } }, { text: ' wrong  ', options: { color: C.SLATE, fontSize: 9 } },
    { text: '■', options: { color: C.SLATE, fontSize: 9 } }, { text: ' “I don’t know” — ~3× fewer false claims.', options: { color: C.SLATE, fontSize: 9, bold: true } },
  ], { x: 0.82, y: 6.06, w: 5.1, h: 0.34, fontFace: F.body, margin: 0 });
  s.addText('OpenAI’s own models & benchmark (2025) — the mechanism, not a vendor ranking.', { x: 0.82, y: 6.4, w: 5.1, h: 0.34, fontFace: F.body, fontSize: 10, italic: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 1.0 });
  const kinds = [
    ['emblem_cue_card', 'THE CONFIDENT GUESS', 'Invented facts', 'Free recall where data was thin — a wrong fact, delivered with total certainty.'],
    ['emblem_fake_receipt', 'THE FAKE RECEIPT', 'Invented sources', 'Citations, cases, book titles that look perfectly real — and don’t exist.'],
    ['emblem_rubber_chicken', 'THE JOKE TAKEN SERIOUSLY', 'Wrong source, confident answer', 'Fluent, cited — and built on a joke, a satire, or the wrong revision.'],
    ['emblem_gilded_frame', 'GARBAGE IN, GOSPEL OUT', 'Runs with your false premise', 'It assumes your prompt is true: feed it a wrong “fact” and it politely builds on it.'],
  ];
  kinds.forEach((k, i) => {
    const y = 1.66 + i * 1.24;
    H.card(s, 6.35, y, 6.4, 1.12, i === 2 ? C.RED_TINT : C.PANEL);
    s.addImage({ path: require('path').join(__dirname, 'assets', 'images', k[0] + '.jpg'), x: 6.51, y: y + 0.09, w: 0.94, h: 0.94, sizing: { type: 'cover', w: 0.94, h: 0.94 } });
    s.addShape('roundRect', { x: 6.51, y: y + 0.09, w: 0.94, h: 0.94, rectRadius: 0.05, fill: { type: 'none' }, line: { color: C.LINE, width: 0.75 } });
    s.addText([
      { text: k[1] + '  ', options: { bold: true, color: i === 2 ? C.RED : C.TEAL_DARK, fontSize: 13, fontFace: F.head } },
      { text: '· ' + k[2], options: { color: C.MUTE, fontSize: 10, breakLine: true, paraSpaceAfter: 2 } },
      { text: k[3], options: { color: C.SLATE, fontSize: 10.5 } },
    ], { x: 7.6, y: y + 0.08, w: 5.02, h: 0.98, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.03 });
  });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Open with the improv actor, spoken: “an improv actor never breaks character — the show must go on, so gaps get filled with the most plausible line. That is your AI on a thin-data day.”\n' +
    '2) Left bullets: the mechanism; the bold OpenAI 2025 finding — the vendor itself says benchmarks reward guessing; the vocabulary upgrade — CONFABULATION.\n' +
    '3) Right: meet the four CHARACTERS — say the nicknames with theater: the confident guess · the fake receipt · the joke taken seriously · garbage in, gospel out. One line each; each returns as a real incident on the next slide.\n' +
    '4) The chart, bottom-left — read it in one breath: “same questions, two models, nearly the same amount RIGHT — but the older one GUESSED whenever it didn’t know (75% wrong), and the newer one was allowed to say I-don’t-know (wrong drops to 26%).” That is the confident guess, measured — and it is why Part 3 teaches you to give the model an out.\n' +
    '5) Presenter story for character 1 if you want one: Google Bard’s launch demo flubbed a telescope fact — details on the next slide’s notes.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“What do these characters look like in public? The hall of shame.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none new on this slide.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.7: abstain-vs-guess chart added (r23: SimpleQA numbers from arXiv:2509.04664 + the GPT-5 system card — o4-mini 24/75/1 vs gpt-5-thinking-mini 22/26/52; the on-slide caveat is mandatory).\n' +
    'v1.8 ART — the four character cards now carry the owner-generated object emblems (R16): blank cue card in a spotlight · sealed receipt dissolving into pixels · rubber chicken on a specimen tray · crumpled paper in a gilded frame. Point at each emblem as you name its character.\n' +
    'v1.6: the four kinds became named characters (owner: more engaging). Teaching frame grounded in r10/r2/r14 — not claimed as academic taxonomy.\n' +
    'OpenAI 2025 = “Why language models hallucinate” (arXiv:2509.04664).\n' +
    'R14: the italic footer (“Four characters — one root: the show must go on. Next slide: what they cost in public.”) was removed from the slide — speak it as the closing line before advancing.');

  // ---------- 14. HALL OF SHAME ----------
  s = H.slide('PART 1 · CORE CONCEPTS', 14);
  H.title(s, 'Concept 6 · The hall of shame · continued', 'Real, public, verified — and all avoidable');
  const shame = [
    ['alert', 'Glue on pizza · May 2024', 'Google’s AI search told users to put glue in pizza sauce and eat a rock a day — it had read a joke forum comment and satire as advice. Global mockery; scaled back within days.'],
    ['gavel', 'The ChatGPT lawyer · Jun 2023', 'A New York lawyer filed six cases that didn’t exist — then asked ChatGPT if they were real. It said yes. $5,000 sanction, apology letters ordered (Mata v. Avianca).'],
    ['send', 'Air Canada’s chatbot · Feb 2024', 'The website bot invented a bereavement refund policy. A tribunal made the airline honor it — rejecting “the bot is a separate legal entity.” Your company owns what its chatbot says.'],
    ['chart', 'The Big Four arc · 2025–26', 'Deloitte partially refunded a government report over invented citations; EY pulled one where 16 of 27 references failed; KPMG’s agentic-AI-excellence report: 5 of 45 citations checked out.'],
  ];
  shame.forEach((r, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.62 + Math.floor(i / 2) * 1.68;
    H.card(s, x, y, 5.95, 1.62, C.PANEL);
    H.iconCircle(s, x + 0.2, y + 0.2, 0.44, r[0], i === 0 ? C.AMBER : C.RED);
    s.addText([
      { text: r[1], options: { bold: true, color: C.INK, fontSize: 14, breakLine: true, paraSpaceAfter: 3 } },
      { text: r[2], options: { color: C.SLATE, fontSize: 14 } },
    ], { x: x + 0.78, y: y + 0.08, w: 5.0, h: 1.48, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 0.98 });
  });
  H.callout(s, 0.55, 5.04, 12.2, 0.6, C.AMBER_TINT, [
    { text: 'Not one-offs: ', options: { bold: true, color: C.INK, fontSize: 14 } },
    { text: 'a legal tracker counted ~1,500 court decisions worldwide involving AI-fabricated citations by mid-2026.', options: { color: C.SLATE, fontSize: 14 } },
  ], { iconName: 'scale', iconFill: C.AMBER, size: 14 });
  H.callout(s, 0.55, 5.7, 12.2, 0.64, C.TEAL_TINT, [
    { text: 'The cure hasn’t changed: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12 } },
    { text: 'Ground it (give it the source) · Cite it (demand receipts + an “I don’t know” escape hatch) · Verify it (check what matters before it ships).', options: { color: C.SLATE, fontSize: 12 } },
  ], { iconName: 'check', iconFill: C.TEAL, size: 12 });
  H.callout(s, 0.55, 6.4, 12.2, 0.6, C.RED_TINT, [
    { text: 'House rule: ', options: { bold: true, color: C.RED, fontSize: 14 } },
    { text: 'every uncited standard clause, date, number, or quote is a draft until verified.', options: { color: C.SLATE, fontSize: 14 } },
  ], { iconName: 'alert', iconFill: C.RED, size: 14 });
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
