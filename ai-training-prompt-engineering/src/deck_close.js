// Closing block: ten things, exercises, glossary, sources, reading
const { C, F } = require('./deck_lib');

module.exports = function buildClose(pres, H) {
  // ---------- CONCLUSION A · REQUIREMENTS = THE SISTER SKILL (v1.6) ----------
  let s = H.slide('CONCLUSION · THE SISTER SKILL', 48);
  H.title(s, 'You already write prompts for a living — same skill, new audience', 'They’re called requirements');
  H.card(s, 0.55, 1.58, 12.2, 0.78, C.TEAL_TINT);
  s.addText([
    { text: '“Prompt engineering and requirements engineering are literally the same skill — using clarity, context, and intentionality to communicate your intent.”', options: { italic: true, color: C.TEAL_DARK, fontSize: 13 } },
    { text: '   — Andrew Stellman, O’Reilly, 2025', options: { color: C.MUTE, fontSize: 10 } },
  ], { x: 0.85, y: 1.66, w: 11.6, h: 0.62, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.05 });
  H.card(s, 0.55, 2.5, 6.9, 3.3, C.PANEL);
  s.addText('Same structure, three ways', { x: 0.85, y: 2.66, w: 6.2, h: 0.35, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
  const reqMap = [
    ['User story', '“As a [role], I want [goal], so that [benefit]”', 'ROLE + TASK — the so-that is the Task’s purpose clause'],
    ['Acceptance criteria', 'Given [state] · When [action] · Then [result]', 'Given = CONTEXT · When = TASK · Then = FORMAT + checks'],
    ['ISO 29148 standard', 'unambiguous · complete · singular · verifiable', 'TASK precision · CONTEXT · THE STOP · FORMAT + self-check'],
  ];
  reqMap.forEach((r, i) => {
    const y = 3.12 + i * 0.9;
    H.card(s, 0.8, y, 3.3, 0.8, 'FFFFFF', C.LINE);
    s.addText([
      { text: r[0], options: { bold: true, color: C.INK, fontSize: 9.5, breakLine: true } },
      { text: r[1], options: { color: C.SLATE, fontSize: 8, italic: true } },
    ], { x: 0.94, y: y + 0.05, w: 3.05, h: 0.7, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 0.98 });
    H.arrow(s, 4.16, y + 0.3, 0.22, C.TEAL);
    s.addText(r[2], { x: 4.5, y: y + 0.03, w: 2.8, h: 0.75, fontFace: F.body, fontSize: 8.4, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle', lineSpacingMultiple: 0.98 });
  });
  H.card(s, 7.6, 2.5, 5.15, 3.3, C.PANEL);
  s.addText('Why it wins', { x: 7.88, y: 2.66, w: 4.6, h: 0.35, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
  s.addText([
    { text: '41.1%', options: { bold: true, color: C.RED, fontSize: 22, fontFace: F.head } },
    { text: '  — how often a model guesses an UNSTATED requirement right. A spec deletes the guessing.', options: { color: C.SLATE, fontSize: 10 } },
  ], { x: 7.88, y: 3.06, w: 4.6, h: 0.75, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.02 });
  s.addText([
    { text: 'The software world moved first: ', options: { bold: true, color: C.INK, fontSize: 10, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'GitHub’s Spec Kit (2025) makes the written spec “the source of truth” AI agents build from — spec-driven development is requirements writing, industrialized.', options: { color: C.SLATE, fontSize: 9.6 } },
  ], { x: 7.88, y: 3.9, w: 4.6, h: 0.95, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText([
    { text: '“Whoever writes the spec… is now the programmer.”', options: { italic: true, color: C.TEAL_DARK, fontSize: 10.5, breakLine: true } },
    { text: '— Sean Grove, OpenAI, 2025', options: { color: C.MUTE, fontSize: 8.5 } },
  ], { x: 7.88, y: 4.92, w: 4.6, h: 0.75, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.04 });
  H.callout(s, 0.55, 6.0, 12.2, 0.95, C.AMBER_TINT, [
    { text: 'What this means for this room: ', options: { bold: true, color: C.INK, fontSize: 12, breakLine: true } },
    { text: 'if you can write an SOP, a test protocol, or an acceptance criterion, you already own the hardest 80% of prompt engineering — the seven elements are a requirements document in miniature.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'key', iconFill: C.AMBER, size: 11.5 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) The reveal, plainly: “you didn’t learn a NEW skill today — you learned a new audience for one you already have. Writing a prompt IS writing a requirement.” Then the Stellman quote, verbatim.\n' +
    '2) LEFT card: three requirements forms this room may already write — user stories, Given-When-Then, the ISO characteristics — and each maps ONTO the anatomy. Read one mapping aloud (Given = Context, When = Task, Then = Format + checks is the cleanest).\n' +
    '3) RIGHT card: the callback number — 41.1% — and the software world’s move: spec-driven development (GitHub Spec Kit), then Grove’s line: whoever writes the spec is now the programmer. His stronger line if the room is technical: “code is 10–20% of the value; the other 80–90% is structured communication.”\n' +
    '4) Amber band — the point of the slide: SOPs, test protocols, acceptance criteria = the hardest 80%, already owned.\n' +
    '5) One caution to respect (R7): the evidence is structural + measured on clarified PROMPTS (ClarifyGPT +7 pts; Yang +4.8%) — there is no study of requirements-trained PEOPLE prompting better; don’t claim one.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“And when you can’t fill an element in — that gap has a name too: a question.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'SOP = Standard Operating Procedure. ISO 29148 = the international requirements-engineering standard (ISO/IEC/IEEE). BDD (if asked) = Behavior-Driven Development, home of Given-When-Then. PM = product manager (in Grove’s quote).\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6 new slide (owner request). All quotes verified verbatim, all forms traced to origin — notes/research/r21_requirements_questions.md: Stellman O’Reilly Sep 2025; Grove “The New Code” June 2025 (transcript-checked); Spec Kit github.blog Sep 2025; user story Connextra 2001; Given-When-Then Dan North mid-2000s; INVEST Bill Wake 2003; ISO 29148:2018 nine characteristics; ClarifyGPT ACM FSE 2024.\n' +
    'DO NOT USE (misattributions people expect): Einstein’s “55 minutes on the problem” (apocryphal) and Voltaire’s “judge a man by his questions” (actually de Lévis, 1808).');

  // ---------- CONCLUSION B · THE CRAFT OF ASKING (v1.6) ----------
  s = H.slide('CONCLUSION · ASK BETTER QUESTIONS', 49);
  H.title(s, 'The best prompt is a question', 'Sometimes theirs — let the AI interview you');
  H.card(s, 0.55, 1.58, 6.2, 3.4, C.TEAL_TINT);
  s.addText('The flip — one line you can paste today', { x: 0.85, y: 1.74, w: 5.6, h: 0.35, fontFace: F.head, fontSize: 13.5, bold: true, color: C.TEAL_DARK, margin: 0 });
  H.card(s, 0.82, 2.16, 5.65, 0.85, 'FFFFFF', C.LINE);
  s.addText('“Before answering, ask me clarifying questions until you’re 95% confident you understand what I need.”', { x: 0.98, y: 2.24, w: 5.35, h: 0.7, fontFace: 'Consolas', fontSize: 10, color: C.TEAL_DARK, margin: 0, valign: 'middle', lineSpacingMultiple: 1.06 });
  s.addText([
    { text: 'Why it works: ', options: { bold: true, color: C.INK, fontSize: 10.5 } },
    { text: 'unstated needs get guessed right 41.1% of the time — but when the model asks FIRST, accuracy jumps ~7–14 points (ClarifyGPT, FSE 2024). Answering its questions isn’t politeness; it’s quality control.', options: { color: C.SLATE, fontSize: 10 } },
  ], { x: 0.85, y: 3.14, w: 5.6, h: 1.0, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.06 });
  s.addText('You’ve run this before — it was Prompt 1/7, step 2, on slide two. The course opened and closes on the same move.', { x: 0.85, y: 4.2, w: 5.6, h: 0.65, fontFace: F.body, fontSize: 9.5, italic: true, color: C.TEAL_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  H.card(s, 6.95, 1.58, 5.8, 3.4, C.PANEL);
  s.addText('The question toolkit — for you, not the AI', { x: 7.22, y: 1.74, w: 5.3, h: 0.35, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
  const qkit = [
    ['Five Whys', 'Ohno, Toyota: “by repeating why five times… the solution becomes clear.” Same factory as our PDCA loop.'],
    ['Open → closed funnel', 'Open questions to explore (“what’s driving this?”), closed to verify (“so the cap is 18k — yes or no?”).'],
    ['The Socratic check', 'Interrogate any AI answer: what’s assumed? what’s the evidence? what if we’re wrong?'],
  ];
  qkit.forEach((q, i) => {
    const y = 2.18 + i * 0.94;
    H.iconCircle(s, 7.22, y + 0.08, 0.4, ['refresh', 'branch', 'help'][i], C.TEAL);
    s.addText([
      { text: q[0] + ' — ', options: { bold: true, color: C.TEAL_DARK, fontSize: 10.5 } },
      { text: q[1], options: { color: C.SLATE, fontSize: 9.6 } },
    ], { x: 7.74, y, w: 4.8, h: 0.9, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.03 });
  });
  H.card(s, 0.55, 5.12, 12.2, 1.0, C.PANEL);
  s.addText([
    { text: '“Figuring out what questions to ask will be more important than figuring out the answer.”', options: { italic: true, color: C.INK, fontSize: 12.5 } },
    { text: '  — Sam Altman, 2025', options: { color: C.MUTE, fontSize: 9.5, breakLine: true, paraSpaceAfter: 3 } },
    { text: '“[Computers] are useless. They can only give you answers.”', options: { italic: true, color: C.SLATE, fontSize: 10.5 } },
    { text: '  — Pablo Picasso, 1964. Sixty years apart, same conclusion.', options: { color: C.MUTE, fontSize: 9 } },
  ], { x: 0.85, y: 5.22, w: 11.6, h: 0.82, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.08 });
  H.callout(s, 0.55, 6.28, 12.2, 0.72, C.TEAL_TINT, [
    { text: 'The two skills are one: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5 } },
    { text: 'the seven elements are a requirements spec in miniature — and the element you CAN’T fill in yet is the exact question to ask, or to let the AI ask you.', options: { color: C.SLATE, fontSize: 11.5 } },
  ], { iconName: 'zap', iconFill: C.TEAL, size: 11.5 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Open with the flip: all course long they wrote prompts; the last skill is making the AI interview THEM. Read the paste-line; note the callback — it was Prompt 1/7 step 2, the very first exercise. Full circle, on purpose.\n' +
    '2) The numbers, in one breath: 41.1% guessed right unstated → asking first recovers ~7–14 points → “answer its questions” is quality control.\n' +
    '3) RIGHT toolkit — for HUMANS: Five Whys (say the Toyota tie: same factory as the PDCA slide) · open→closed funnel · the Socratic check for interrogating any AI answer.\n' +
    '4) Quote band: Altman, then the Picasso echo — sixty years apart, same conclusion. (Picasso wording verified to the 1964 Paris Review interview; the popular “computers are useless” phrasing is a later smoothing.)\n' +
    '5) Teal band is the course’s closing thesis — read it verbatim, then advance to the ten things.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Ten things worth remembering — the photograph slide.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'FSE = the ACM Foundations of Software Engineering conference (ClarifyGPT’s venue). HBR (if cited aloud) = Harvard Business Review.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6 new slide (owner request). Sources verified in notes/research/r21_requirements_questions.md: ClarifyGPT (GPT-4 62.43→69.60 mean Pass@1; +13.87 with human answers) · CLAM 2022 (qualitative) · Ohno, Toyota Production System · Altman via ReThinking/CNBC Jan 2025 · Picasso via Quote Investigator.\n' +
    'Extra toolkit for questions, if the room wants more: HBR’s five leader questions (investigative what’s known · speculative what if · productive now what · interpretive so what · subjective what’s unsaid), May–Jun 2024.\n' +
    'DO NOT attribute: Einstein 55-minutes (apocryphal) · Voltaire judge-by-questions (de Lévis, 1808).');

  // ---------- 42. TEN THINGS ----------
  s = H.slide('WRAP-UP', 42);
  H.title(s, 'Wrap-up', 'Ten things worth remembering');
  const ten = [
    ['1', 'The prompt is the whole steering wheel — everything the model knows about your task must be in it (or in files it can read).'],
    ['2', 'Anatomy beats inspiration: Role · Task · Context · Format · Examples — plus the Out and the Stop. A prompt is a requirement with a new audience.'],
    ['3', 'The context window is a desk, not a filing cabinet: long documents at the top, question at the end, fresh chat per topic.'],
    ['4', 'Numbers come from code execution, quotes come from documents, current facts come from search — never from free recall.'],
    ['5', 'Fluency is not evidence. Uncited claims are drafts. Give the model an out and demand citations.'],
    ['6', 'Never reveal your preferred answer when asking for judgment — AI affirms you ~49% more than a human would.'],
    ['7', 'On thinking models: drop the step-by-step scripts, keep the clarity. Contradictions now cost real money.'],
    ['8', 'A generative prompt says what to write. An agentic prompt is a work order: mission, environment, checks, gates, autonomy rules.'],
    ['9', 'Gates catch errors at the cheapest point: definitions before data, reconciliation before analysis, headlines before rendering.'],
    ['10', 'Prompts that work are assets: name them, version them, store them where the team (and the agent) can find them.'],
  ];
  ten.forEach((t, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.6 + Math.floor(i / 2) * 1.02;
    H.card(s, x, y, 5.95, 0.92, C.PANEL);
    s.addText(t[0], { x: x + 0.12, y: y + 0.14, w: 0.6, h: 0.6, fontFace: F.head, fontSize: 20, bold: true, color: C.TEAL, align: 'center', margin: 0 });
    s.addText(t[1], { x: x + 0.78, y: y + 0.06, w: 5.05, h: 0.8, fontFace: F.body, fontSize: 9.8, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 1.02 });
  });
  s.addText('And if you keep only one sentence: a prompt deletes wrong guesses, binds the job, and decides what sits on the desk.', { x: 0.55, y: 6.68, w: 12.2, h: 0.32, align: 'center', fontFace: F.body, fontSize: 10.5, italic: true, color: C.TEAL_DARK, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT — 1) Announce: “this is the slide people photograph — go ahead.” 2) Read all ten SLOWLY, in order, left column then right, 1→10. No commentary between them; the compression is the point. 3) If asked where one came from, the map: 1–2 anatomy, 3–5 concepts, 6–7 evidence, 8–9 agentic, 10 management. 4) Close on the italic footer — the whole course in one sentence: a prompt deletes wrong guesses (Part 1), binds the job (Parts 3–5), and decides what sits on the desk (context — Parts 1 and 5). 5) Bridge: “three exercises to make it stick.”\n' +
    'ACRONYMS — none new on this slide.\n' +
    'CONTENT — Each maps back to a part: 1–2 anatomy, 3–5 concepts, 6–7 evidence, 8–9 agentic, 10 management. v1.8: the one-sentence wrap-up added (external-review adoption, 9B-ext) — it compresses the course’s three moves into one line.');

  // ---------- 43. EXERCISES ----------
  s = H.slide('HANDS-ON', 43);
  H.title(s, 'Hands-on · 15 minutes each', 'Three exercises that make it stick');
  const ex = [
    ['edit', 'Exercise 1 · Anatomy rebuild', 'Take a prompt you actually used last week. Rebuild it with the seven-element anatomy (G-templates as reference). Run both versions; compare outputs side by side. Then ask the model to improve your rebuilt prompt — metaprompting — and run that too.', 'You’ll see the quality jump — and how cheap it was.'],
    ['scale', 'Exercise 2 · Blind review', 'Take a document or plan you own. Paste it as “a colleague’s draft” and run G3’s critique template: case against, three weakest points, what evidence would change the verdict. Do NOT hint at your view.', 'Most people meet their first honest AI review here.'],
    ['robot', 'Exercise 3 · First mission brief', 'Pick a small recurring job with files (a folder to summarize, a tracker to update). Fill A1’s twelve blocks — placeholders and all. You don’t need an agent to run it today: writing the brief is the skill.', 'Where the checks and gates feel awkward is where your process was fuzzy all along.'],
  ];
  ex.forEach((e, i) => {
    const y = 1.65 + i * 1.68;
    H.card(s, 0.55, y, 8.9, 1.52, C.PANEL);
    H.iconCircle(s, 0.85, y + 0.44, 0.6, e[0], C.TEAL);
    s.addText([
      { text: e[1] + '  ', options: { bold: true, color: C.INK, fontSize: 12.5, breakLine: true, paraSpaceAfter: 3 } },
      { text: e[2] + '  ', options: { color: C.SLATE, fontSize: 10.2, breakLine: true, paraSpaceAfter: 2 } },
      { text: e[3], options: { color: C.TEAL_DARK, fontSize: 9.5, italic: true } },
    ], { x: 1.65, y: y + 0.08, w: 7.0, h: 1.38, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.04 });
  });
  s.addImage({ path: require('path').join(__dirname, 'assets', 'images', 'office_scene.jpg'), x: 9.65, y: 1.65, w: 3.1, h: 1.74, sizing: { type: 'cover', w: 3.1, h: 1.74 } });
  s.addShape('roundRect', { x: 9.65, y: 1.65, w: 3.1, h: 1.74, rectRadius: 0.06, fill: { type: 'none' }, line: { color: C.LINE, width: 1 } });
  s.addText('Fifteen minutes, your real work — starting now.', { x: 9.65, y: 3.43, w: 3.1, h: 0.3, align: 'center', fontFace: F.body, fontSize: 8.8, italic: true, color: C.MUTE, margin: 0 });
  H.card(s, 9.65, 3.85, 3.1, 1.15, C.TEAL_TINT);
  s.addText([
    { text: 'Share-back: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 10.2 } },
    { text: 'next team meeting, two volunteers show a before / after.', options: { color: C.SLATE, fontSize: 10 } },
  ], { x: 9.85, y: 3.97, w: 2.7, h: 0.92, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.05 });
  s.addNotes(
    'HOW TO PRESENT — 1) Three cards TOP TO BOTTOM: anatomy rebuild → blind review → first mission brief; each is 15 minutes ON THEIR REAL WORK — say that twice; toy exercises don’t transfer. 2) Read the italic payoff line inside each card — it is the motivation. 3) Set the share-back (teal card): next team meeting, two volunteers show a before/after. 4) If time allows in-session, run exercise 1 live with a volunteer’s real prompt.\n' +
    'ACRONYMS — G-templates / G3 / A1 = library codes (generative set, the critique template, the mission brief).\n' +
    'CONTENT — Exercises 2 and 3 work as homework with a share-back next meeting.\n' +
    'ART — the office scene is an owner-generated illustration (R16), placed here per the owner’s default (the closing hands-on slide): the room it depicts is the room doing the exercises.');

  // ---------- 44. GLOSSARY ----------
  s = H.slide('REFERENCE', 44);
  H.title(s, 'Reference', 'Glossary — twenty terms that matter');
  const glossary = [
    ['Escalation ladder', 'prompt first, retrieve second, fine-tune last — capability triage (Part 1)'],
    ['Promotion ladder', 'one-off → personal → team → packaged → as-code — where a prompt lives (Part 6)'],
    ['Token', 'the text chunk a model actually reads (~¾ of a word); pricing and limits count these'],
    ['Context window', 'working memory per conversation — everything must fit; cleared when the chat ends'],
    ['Knowledge cutoff', 'where training data stops; anything after needs search or your documents'],
    ['RAG', 'retrieval-augmented generation — fetch relevant passages, answer from them, with citations'],
    ['Embedding', 'a text’s coordinate in meaning-space; powers semantic search and RAG retrieval'],
    ['Hallucination', 'fluent, confident, wrong — plausibility optimized instead of truth'],
    ['Reasoning model', 'drafts and checks internally before answering; slower, costlier, better at hard problems'],
    ['Few-shot', 'teaching by 3–5 examples in the prompt'],
    ['Chain-of-thought', 'prompting visible step-by-step reasoning — now built into thinking models'],
    ['Metaprompting', 'asking the model to critique or rewrite your prompt'],
    ['Sycophancy', 'the trained tendency to agree with you; blind the review to defuse it'],
    ['Agent', 'model + tools + instructions in a loop, acting until done or stopped'],
    ['MCP', 'Model Context Protocol — the open standard for plugging tools into agents'],
    ['Mission brief', 'an agentic prompt: goal, environment, inputs, process, checks, gates, reporting'],
    ['Gate', 'a human checkpoint inside an agent’s process — approve before it proceeds'],
    ['Open weights', 'a downloadable model you can self-host — the data-privacy end of the spectrum'],
    ['Taxonomy', 'the element → attribute → option catalog behind the Template Creator — your parts list for prompts'],
    ['Context engineering', 'choosing everything on the desk — prompt, files, history, tool results; the parent discipline of agentic prompting'],
  ];
  glossary.forEach((g, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.55 + Math.floor(i / 2) * 0.54;
    s.addText([
      { text: g[0] + ' — ', options: { bold: true, color: C.TEAL_DARK, fontSize: 10.5 } },
      { text: g[1], options: { color: C.SLATE, fontSize: 10 } },
    ], { x, y, w: 5.95, h: 0.56, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.0 });
  });
  s.addNotes(
    'HOW TO PRESENT — 1) Do not read it. One sentence: “print-friendly glossary — every term on it was used in context today.” 2) Point at two entries only: sycophancy (the one that changes behavior) and gate (the one that makes agents safe). 3) Advance.\n' +
    'ACRONYMS — RAG and MCP are expanded on the slide itself; nothing else to define.\n' +
    'CONTENT — Print-friendly reference. All twenty were used in context during the training (taxonomy added in v1.2; the two ladders added in v1.5 to disambiguate them; context engineering added in v1.8 with the desk-slide line).');

  // ---------- EVIDENCE MAPS (v1.4 — why each dial matters, per criteria class) ----------
  const evTable = (s2, rows) => {
    s2.addText('Criteria class', { x: 0.75, y: 1.58, w: 2.3, h: 0.3, fontFace: F.body, fontSize: 10.5, bold: true, color: C.SLATE, margin: 0 });
    s2.addText('What it does to your output', { x: 3.15, y: 1.58, w: 6.0, h: 0.3, fontFace: F.body, fontSize: 10.5, bold: true, color: C.TEAL_DARK, margin: 0 });
    s2.addText('Evidence', { x: 9.3, y: 1.58, w: 3.25, h: 0.3, fontFace: F.body, fontSize: 10.5, bold: true, color: C.INK, margin: 0 });
    rows.forEach((r, i) => {
      const y = 1.92 + i * 0.5;
      H.card(s2, 0.55, y, 12.2, 0.44, i % 2 ? 'FFFFFF' : C.PANEL, i % 2 ? C.LINE : null);
      s2.addText(r[0], { x: 0.75, y: y + 0.02, w: 2.3, h: 0.4, fontFace: F.body, fontSize: 9.3, bold: true, color: C.INK, margin: 0, valign: 'middle', lineSpacingMultiple: 0.92 });
      s2.addText(r[1], { x: 3.15, y: y + 0.02, w: 6.0, h: 0.4, fontFace: F.body, fontSize: 8.8, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.92 });
      s2.addText(r[2], { x: 9.3, y: y + 0.02, w: 3.25, h: 0.4, fontFace: F.body, fontSize: 8.2, italic: true, color: C.MUTE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.92 });
    });
  };
  s = H.slide('REFERENCE · EVIDENCE MAP 1 OF 2', 45);
  H.title(s, 'Reference', 'Why each dial matters — the generative criteria');
  evTable(s, [
    ['Identity & role', 'Sets voice, vocabulary, and caution level — which region of training answers. Titles add no accuracy: 162-persona testing found no gain.', 'Zheng 2024 · Salewski 2023'],
    ['Behavioral rules', 'Turn “be careful” into rules checkable line-by-line in the output; grounding rules drastically cut invented content.', 'Anthropic hallucination docs'],
    ['Stance & blinding', 'Models affirm users ~49% more than humans and mirror any side you reveal — a declared neutral or critic stance pre-empts the mirror.', 'Cheng, Science 2026 · Sharma 2023'],
    ['Task verb & question', 'The verb selects the operation; a precise question carries its own completion test. Ambiguity burns thinking tokens on reconciliation.', 'Google guide · OpenAI GPT-5 guide'],
    ['Purpose — the why', 'Models generalize from reasons: an explained rule gets applied in spirit to cases you never listed.', 'Anthropic best practices'],
    ['Context & glossary', 'Replaces the model’s most-plausible guess with your facts; every unstated quirk becomes an invented “fix.”', 'OpenAI 2025, why LMs hallucinate'],
    ['Material placement', 'Documents at the top, question at the end: up to ~30% better answers; content buried mid-context sags.', 'Anthropic long-context · Liu 2023'],
    ['Format & length', 'Tiny format changes swing accuracy up to 76 points — a tested shape removes that variance. Numeric caps are enforceable; adjectives are moods.', 'Sclar, ICLR 2024'],
    ['Examples', 'The model imitates format, tone, AND edge-case behavior; exemplar choice and order alone can swing accuracy from chance to 90%+. Zero-shot first on thinking models.', 'Brown 2020 · Lu 2021 · DeepSeek-R1'],
    ['The Out & the Stop', 'Permission to say “I don’t know” drastically cuts invented answers — training rewards guessing; numbered scope plus a stop rule bound the sprawl.', 'Anthropic docs · OpenAI 2025'],
  ]);
  s.addNotes(
    'HOW TO PRESENT — 1) This is a reference slide — don’t walk all ten rows. Say what it IS: “every dial you met in Part 3, what it does to your output, and the evidence — the same notes now sit on every slot of your Taxonomy Reference.” 2) If time allows, read TWO rows aloud as proof of depth: Format & length (the 76-point swing) and Stance (the ~49% number). 3) Point them to the handout: “when you wonder whether a slot is worth filling, the why is printed next to it.”\n' +
    'ACRONYMS — ICLR = International Conference on Learning Representations (a top AI research venue).\n' +
    'CONTENT — v1.4 layer (owner request): the per-attribute “why it matters” notes. Full citations with URLs live in notes/research/ (r3_techniques.md, t1_prompt_report.md). Every row compresses the whys stamped on the taxonomy attributes; the agentic half is the next slide.');

  s = H.slide('REFERENCE · EVIDENCE MAP 2 OF 2', 46);
  H.title(s, 'Reference', 'Why each dial matters — the agentic criteria');
  evTable(s, [
    ['Posture & standing rules', 'Conduct that must survive hour three of an unsupervised run — rules live in re-read files, not in fading conversation context.', 'Anthropic harness guidance'],
    ['Done + verifiable-by', 'The loop needs an exit it can TEST: mark work complete “only after end-to-end verification — not when the code is written.”', 'Anthropic memory-tool (verbatim)'],
    ['Environment boundaries', 'Immutable inputs and versioned outputs engineer reversibility in before the first action — blast radius is a design choice.', 'Claude Code protected paths'],
    ['Least-privilege tools', 'Name what exists, forbid the rest; risk-rate each tool low/medium/high by write access, reversibility, and impact.', 'OpenAI practical guide · NCSC'],
    ['Input register & trust', 'Trust level dictates validation depth; UNKNOWN beats a plausible guess — a guessed grain propagates through the whole run.', 'pipeline/register discipline'],
    ['Plan steps & methods', 'Named inputs and outputs per step keep intermediates inspectable; boring methods re-run identically; math runs as code.', 'Anthropic chaining · Faith & Fate 2023'],
    ['Checks: anchor · hard · soft', 'Rules-based feedback is “the best form of feedback” an agent gets; one outside anchor catches whole-pipeline errors in a single comparison.', 'Anthropic Agent SDK'],
    ['Gates & autonomy', 'Approval sits where errors are cheapest — plan, pre-irreversible, failure thresholds; autonomy is a design choice named by the role YOU keep.', 'OpenAI guide · Feng et al. 2025'],
    ['Logs & reproducibility', 'Structured updates and descriptive commits make a run auditable and recoverable; same inputs → same outputs is engineered, not hoped.', 'Anthropic harness guidance'],
    ['Report shape & discipline', 'A fixed status shape reads in 30 seconds; “done” means the check it ran, the output it got, the file re-opened — evidence, not assertion.', 'SDK status enums · harness docs'],
  ]);
  s.addNotes(
    'HOW TO PRESENT — 1) Same treatment as the previous slide: name it, read TWO rows (Done + verifiable-by — the verbatim vendor rule — and Gates & autonomy), then point to the handout. 2) The line to land: “none of the twelve blocks is bureaucracy — each one exists because a documented failure taught someone to add it.”\n' +
    'ACRONYMS — SDK = Software Development Kit. NCSC = (UK) National Cyber Security Centre.\n' +
    'CONTENT — v1.4 layer, agentic half. Feng et al. 2025 = “Levels of Autonomy for AI Agents” (operator → observer). Full citations: notes/research/t6_agentic_attrs.md.');

  // ---------- 45. SOURCES ----------
  s = H.slide('REFERENCE', 45);
  H.title(s, 'Reference', 'Sources this training is built on');
  const srcCols = [
    ['Vendor guidance (fetched Aug 2026)', [
      'Anthropic — Prompting best practices; long-context tips; reduce-hallucinations; Building Effective Agents; Claude Code best practices; context engineering',
      'OpenAI — GPT-5 prompting guide; reasoning best practices; A Practical Guide to Building Agents; Model Spec',
      'Google — Gemini for Workspace prompting guides (Persona-Task-Context-Format)',
      'Microsoft — Copilot prompt guidance (Goal-Context-Source-Expectations); Copilot agents docs',
    ]],
    ['Research', [
      'Brown et al. 2020 (few-shot) · Wei et al. 2022 & Kojima et al. 2022 (chain-of-thought) · Wang et al. 2023 (self-consistency)',
      'Sclar et al. 2024 (format brittleness) · Zheng et al. 2024 (personas) · Salinas & Morstatter 2024 (tips/perturbations)',
      'Cheng et al., Science 2026 (sycophancy) · Sharma et al. 2023 (why sycophancy) · Liu et al. 2023 (lost in the middle)',
      'OpenAI 2025 (why language models hallucinate) · Sprague et al. 2025 (when CoT helps)',
    ]],
    ['Landscape & governance', [
      'Stanford HAI AI Index 2026 · LMArena / Artificial Analysis / SWE-bench (Aug 2026 snapshots)',
      'OWASP LLM Top 10 (2025) + Top 10 for Agentic Applications for 2026 · UK NCSC agentic-AI guidance · IMDA/CSA Singapore (agentic deployment) · Cisco AI Defense (skills audit) · Harmonic Security (shadow-AI prompts)',
      'Vendor launch posts & major-outlet reporting (Reuters, CNBC, TechCrunch, Bloomberg) for all product dates',
    ]],
  ];
  srcCols.forEach((col, i) => {
    const x = 0.55 + i * 4.18;
    H.card(s, x, 1.62, 3.95, 5.0, C.PANEL);
    s.addText(col[0], { x: x + 0.22, y: 1.8, w: 3.5, h: 0.55, fontFace: F.head, fontSize: 12.5, bold: true, color: C.TEAL_DARK, margin: 0 });
    H.bullets(s, x + 0.24, 2.42, 3.5, 4.0, col[1], { size: 9, gap: 7 });
  });
  s.addText('Full source list with URLs: notes/research/ in the training repo — every fact in this deck carries an “as of” date there.', { x: 0.55, y: 6.75, w: 12.2, h: 0.35, fontFace: F.body, fontSize: 10, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT — 1) One sentence, then move: “nothing in this deck is vibes — every number has a URL and an as-of date in notes/research/ in the repo.” 2) If someone challenges a number later, this is where you point them.\n' +
    'ACRONYMS — OWASP = Open Worldwide Application Security Project. NCSC = (UK) National Cyber Security Centre. HAI = Stanford Institute for Human-Centered AI. LLM = Large Language Model. SWE-bench / LMArena = benchmark and leaderboard names.\n' +
    'CONTENT — The point of this slide is auditability.');

  // ---------- 46. RECOMMENDED READING ----------
  s = H.slide('KEEP LEARNING', 46);
  H.title(s, 'Keep learning', 'Recommended reading — start practical, go deep');
  const books = [
    ['Practical start', [
      ['Mollick — Co-Intelligence (2024)', 'the working-with-AI mindset book; read first'],
      ['Kneusel — How AI Works (2024)', 'the concepts of Part 1, gently and rigorously'],
    ]],
    ['The craft', [
      ['Phoenix & Taylor — Prompt Engineering for Generative AI (O’Reilly 2024)', 'the five principles, applied — closest to Parts 3–4'],
      ['Berryman & Ziegler — Prompt Engineering for LLMs (O’Reilly 2024)', 'how prompts actually meet the model; by GitHub Copilot creators'],
    ]],
    ['Going deep', [
      ['Huyen — AI Engineering (O’Reilly 2025)', 'RAG, agents, evaluation — the engineering behind Part 5'],
      ['Alammar & Grootendorst — Hands-On Large Language Models (2024)', 'visual internals: tokens, embeddings, transformers'],
    ]],
  ];
  books.forEach((col, i) => {
    const x = 0.55 + i * 4.18;
    H.card(s, x, 1.62, 3.95, 4.4, i === 1 ? C.TEAL_TINT : C.PANEL);
    s.addText(col[0], { x: x + 0.22, y: 1.8, w: 3.5, h: 0.4, fontFace: F.head, fontSize: 13.5, bold: true, color: C.TEAL_DARK, margin: 0 });
    col[1].forEach((b, j) => {
      s.addText([
        { text: b[0], options: { bold: true, color: C.INK, fontSize: 10.5, breakLine: true, paraSpaceAfter: 2 } },
        { text: b[1], options: { color: C.SLATE, fontSize: 9.5 } },
      ], { x: x + 0.24, y: 2.3 + j * 1.8, w: 3.5, h: 1.7, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.05 });
    });
  });
  H.callout(s, 0.55, 6.25, 12.2, 0.75, C.AMBER_TINT, [
    { text: 'And the fastest teacher of all: ', options: { bold: true, color: C.INK, fontSize: 12 } },
    { text: 'the prompt library in this repo. Copy a template, run it on your real work today, improve it, commit the improvement.', options: { color: C.SLATE, fontSize: 12 } },
  ], { iconName: 'zap', iconFill: C.AMBER, size: 12 });
  s.addNotes(
    'HOW TO PRESENT — 1) Three shelves LEFT TO RIGHT: practical start → the craft → going deep; one line per book, no more. 2) Give the reading order explicitly: Mollick for mindset, Phoenix & Taylor for craft, Huyen when you’re building agents seriously. 3) End on the amber band: “the fastest teacher is the prompt library in the repo — copy a template, run it on real work today, improve it, commit the improvement.”\n' +
    'ACRONYMS — none new on this slide (O’Reilly = the technical publisher).\n' +
    'CONTENT — All six books are real and in print — most are in the team’s shared library already.');

  // ---------- 47. THANK YOU / DARK CLOSE ----------
  s = H.slide(null, 47, { dark: true });
  s.addText('FROM PROMPTS TO AGENTS', { x: 0.55, y: 2.4, w: 12, h: 0.5, fontFace: F.body, fontSize: 15, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('Draft with AI.\nDecide with judgment.\nDelegate with a brief.', { x: 0.55, y: 2.95, w: 7.6, h: 2.4, fontFace: F.head, fontSize: 40, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.12 });
  s.addImage({ path: require('path').join(__dirname, 'assets', 'images', 'question_bench.jpg'), x: 8.4, y: 2.35, w: 4.15, h: 2.33, sizing: { type: 'cover', w: 4.15, h: 2.33 } });
  s.addShape('roundRect', { x: 8.4, y: 2.35, w: 4.15, h: 2.33, rectRadius: 0.06, fill: { type: 'none' }, line: { color: C.TEAL_LIGHT, width: 1 } });
  s.addText('and the last skill of all — let it ask you', { x: 8.4, y: 4.74, w: 4.15, h: 0.3, align: 'center', fontFace: F.body, fontSize: 10, italic: true, color: C.ON_DARK_MUTE, margin: 0 });
  s.addText('Templates: prompt-library/ · Research & sources: notes/ · Questions and template improvements: open an issue or bring them to the next session.', { x: 0.55, y: 5.6, w: 11.5, h: 0.6, fontFace: F.body, fontSize: 13, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes(
    'HOW TO PRESENT — 1) Read the three lines as a cadence, with a beat between each: draft with AI — decide with judgment — delegate with a brief. 2) Connect to the previous training: the first two lines are its habit line; the third is what this course added. 3) Gesture at the painting: the person’s question is lit; the robot’s is still forming — the caption is the course’s last lesson, from the best-prompt-is-a-question slide. 4) Last sentence: where everything lives, and bring template improvements to the next session. 5) Thank them — then stop talking; resist the recap urge.\n' +
    'ACRONYMS — none on this slide.\n' +
    'CONTENT — Close by connecting to the previous training’s habit line — now extended with: delegate with a brief.\n' +
    'ART — the bench scene is an owner-generated illustration (R16). PLACEMENT NOTE (v1.8): the ledger slotted it on the best-prompt-is-a-question slide, but that slide has no room at full size without cutting the question toolkit — so it closes the deck instead, uncropped, as the final image the room sees. Flagged to the owner; easy to move if he prefers.');
};
