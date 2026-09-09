// Closing block: ten things, exercises, glossary, sources, reading
const { C, F } = require('./deck_lib');

module.exports = function buildClose(pres, H) {
  // ---------- 42. TEN THINGS ----------
  let s = H.slide('WRAP-UP', 42);
  H.title(s, 'Wrap-up', 'Ten things worth remembering');
  const ten = [
    ['1', 'The prompt is the whole steering wheel — everything the model knows about your task must be in it (or in files it can read).'],
    ['2', 'Anatomy beats inspiration: Role · Task · Context · Format · Examples. Every vendor teaches the same recipe.'],
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
  s.addNotes(
    'HOW TO PRESENT — 1) Announce: “this is the slide people photograph — go ahead.” 2) Read all ten SLOWLY, in order, left column then right, 1→10. No commentary between them; the compression is the point. 3) If asked where one came from, the map: 1–2 anatomy, 3–5 concepts, 6–7 evidence, 8–9 agentic, 10 management. 4) Bridge: “three exercises to make it stick.”\n' +
    'ACRONYMS — none new on this slide.\n' +
    'CONTENT — Each maps back to a part: 1–2 anatomy, 3–5 concepts, 6–7 evidence, 8–9 agentic, 10 management.');

  // ---------- 43. EXERCISES ----------
  s = H.slide('HANDS-ON', 43);
  H.title(s, 'Hands-on · 15 minutes each', 'Three exercises that make it stick');
  const ex = [
    ['edit', 'Exercise 1 · Anatomy rebuild', 'Take a prompt you actually used last week. Rebuild it with the five-block anatomy (G-templates as reference). Run both versions; compare outputs side by side. Then ask the model to improve your rebuilt prompt — metaprompting — and run that too.', 'You’ll see the quality jump — and how cheap it was.'],
    ['scale', 'Exercise 2 · Blind review', 'Take a document or plan you own. Paste it as “a colleague’s draft” and run G3’s critique template: case against, three weakest points, what evidence would change the verdict. Do NOT hint at your view.', 'Most people meet their first honest AI review here.'],
    ['robot', 'Exercise 3 · First mission brief', 'Pick a small recurring job with files (a folder to summarize, a tracker to update). Fill A1’s twelve blocks — placeholders and all. You don’t need an agent to run it today: writing the brief is the skill.', 'Where the checks and gates feel awkward is where your process was fuzzy all along.'],
  ];
  ex.forEach((e, i) => {
    const y = 1.65 + i * 1.68;
    H.card(s, 0.55, y, 12.2, 1.52, C.PANEL);
    H.iconCircle(s, 0.85, y + 0.44, 0.6, e[0], C.TEAL);
    s.addText([
      { text: e[1] + '  ', options: { bold: true, color: C.INK, fontSize: 13.5, breakLine: true, paraSpaceAfter: 3 } },
      { text: e[2], options: { color: C.SLATE, fontSize: 11 } },
    ], { x: 1.65, y: y + 0.12, w: 8.1, h: 1.3, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.07 });
    s.addText(e[3], { x: 9.9, y: y + 0.12, w: 2.7, h: 1.3, fontFace: F.body, fontSize: 10, italic: true, color: C.TEAL_DARK, margin: 0, valign: 'middle', lineSpacingMultiple: 1.08 });
  });
  s.addNotes(
    'HOW TO PRESENT — 1) Three cards TOP TO BOTTOM: anatomy rebuild → blind review → first mission brief; each is 15 minutes ON THEIR REAL WORK — say that twice; toy exercises don’t transfer. 2) Read the italic payoff line on the right of each card — it is the motivation. 3) Set the share-back: next team meeting, two volunteers show a before/after. 4) If time allows in-session, run exercise 1 live with a volunteer’s real prompt.\n' +
    'ACRONYMS — G-templates / G3 / A1 = library codes (generative set, the critique template, the mission brief).\n' +
    'CONTENT — Exercises 2 and 3 work as homework with a share-back next meeting.');

  // ---------- 44. GLOSSARY ----------
  s = H.slide('REFERENCE', 44);
  H.title(s, 'Reference', 'Glossary — nineteen terms that matter');
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
    'CONTENT — Print-friendly reference. All nineteen were used in context during the training (taxonomy added in v1.2; the two ladders added in v1.5 to disambiguate them).');

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
      'OWASP LLM Top 10 (2025) · UK NCSC agentic-AI guidance · Cisco AI Defense (skills audit) · Harmonic Security (shadow-AI prompts)',
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
  s.addText('Draft with AI.\nDecide with judgment.\nDelegate with a brief.', { x: 0.55, y: 2.95, w: 11.5, h: 2.4, fontFace: F.head, fontSize: 40, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.12 });
  s.addText('Templates: prompt-library/ · Research & sources: notes/ · Questions and template improvements: open an issue or bring them to the next session.', { x: 0.55, y: 5.6, w: 11.5, h: 0.6, fontFace: F.body, fontSize: 13, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes(
    'HOW TO PRESENT — 1) Read the three lines as a cadence, with a beat between each: draft with AI — decide with judgment — delegate with a brief. 2) Connect to the previous training: the first two lines are its habit line; the third is what this course added. 3) Last sentence: where everything lives, and bring template improvements to the next session. 4) Thank them — then stop talking; resist the recap urge.\n' +
    'ACRONYMS — none on this slide.\n' +
    'CONTENT — Close by connecting to the previous training’s habit line — now extended with: delegate with a brief.');
};
