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
  s.addNotes('Read them slowly; this is the slide people photograph. Each maps back to a part: 1–2 anatomy, 3–5 concepts, 6–7 evidence, 8–9 agentic, 10 management.');

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
  s.addNotes('Run exercise 1 live in the session if time allows — pick a volunteer’s real prompt. Exercises 2 and 3 work as homework with a share-back next meeting.');

  // ---------- 44. GLOSSARY ----------
  s = H.slide('REFERENCE', 44);
  H.title(s, 'Reference', 'Glossary — sixteen terms that matter');
  const glossary = [
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
  ];
  glossary.forEach((g, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.58 + Math.floor(i / 2) * 0.64;
    s.addText([
      { text: g[0] + ' — ', options: { bold: true, color: C.TEAL_DARK, fontSize: 10.5 } },
      { text: g[1], options: { color: C.SLATE, fontSize: 10 } },
    ], { x, y, w: 5.95, h: 0.6, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.0 });
  });
  s.addNotes('Print-friendly reference. All sixteen were used in context during the training.');

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
  s.addNotes('The point of this slide is auditability: nothing in the deck is vibes. If someone challenges a number, the notes folder has the URL and the date it was verified.');

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
  s.addNotes('All six books are real and in print — most are in the team’s shared library already. Reading order: Mollick for mindset, Phoenix & Taylor for craft, Huyen when you’re building agents seriously.');

  // ---------- 47. THANK YOU / DARK CLOSE ----------
  s = H.slide(null, 47, { dark: true });
  s.addText('FROM PROMPTS TO AGENTS', { x: 0.55, y: 2.4, w: 12, h: 0.5, fontFace: F.body, fontSize: 15, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('Draft with AI.\nDecide with judgment.\nDelegate with a brief.', { x: 0.55, y: 2.95, w: 11.5, h: 2.4, fontFace: F.head, fontSize: 40, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.12 });
  s.addText('Templates: prompt-library/ · Research & sources: notes/ · Questions and template improvements: open an issue or bring them to the next session.', { x: 0.55, y: 5.6, w: 11.5, h: 0.6, fontFace: F.body, fontSize: 13, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes('Close by connecting to the previous training’s habit line: draft with AI, decide with judgment — now extended with: delegate with a brief.');
};
