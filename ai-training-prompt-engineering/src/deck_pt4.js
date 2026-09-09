// PART 5 (Agentic prompting) + PART 6 (Prompt management) + close
const { C, F } = require('./deck_lib');

module.exports = function buildPartFour(pres, H) {
  // ---------- SESSION 2 OPENER (v1.1) ----------
  let s0 = H.slide('SESSION 2 · WHERE WE LEFT OFF', 33);
  H.title(s0, 'Session 2', 'Sixty seconds of where we left off');
  const rc = [
    ['layers', 'The anatomy', 'Role · Task · Context · Format · Examples — plus the Out and the Stop. Every vendor teaches the same recipe.'],
    ['zap', 'Seven techniques', 'specificity-with-why, examples, tags, the out, chaining, self-check, metaprompting.'],
    ['shield', 'The evidence rules', 'numbers via code · citations or it didn’t happen · never reveal your preference when asking for judgment.'],
    ['download', 'The take-home', 'eight templates + the Template Creator — the blind critique was homework; who ran it?'],
  ];
  rc.forEach((r, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.7 + Math.floor(i / 2) * 1.6;
    H.card(s0, x, y, 5.95, 1.45, C.PANEL);
    H.iconCircle(s0, x + 0.2, y + 0.42, 0.55, r[0], C.TEAL);
    s0.addText([
      { text: r[1], options: { bold: true, color: C.INK, fontSize: 13, breakLine: true, paraSpaceAfter: 2 } },
      { text: r[2], options: { color: C.SLATE, fontSize: 10.8 } },
    ], { x: x + 0.9, y: y + 0.1, w: 4.9, h: 1.25, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.06 });
  });
  H.callout(s0, 0.55, 5.15, 12.2, 1.0, C.TEAL_TINT, [
    { text: 'Today: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 13 } },
    { text: 'the leap from asking to delegating — the mission brief, gates and guardrails — then how a team keeps its prompts as assets.', options: { color: C.SLATE, fontSize: 13 } },
  ], { iconName: 'robot', iconFill: C.TEAL, size: 13 });
  s0.addNotes(
    'HOW TO PRESENT — 1) Two minutes MAXIMUM. Walk the four cards in reading order: anatomy → techniques → evidence rules → take-home. One line each — this is re-entry, not re-teaching. 2) At the take-home card, ask the homework question: “who ran the blind critique?” Take ONE volunteer story — it beats any recap. 3) Teal band: frame today — the leap from asking to delegating, then prompts as assets. 4) Advance.\n' +
    'ACRONYMS — none new on this slide.\n' +
    'CONTENT — v1.1: session-2 opener. One volunteer story beats any recap. Keep to 2 minutes total.');

  // ---------- 33. PART 5 DIVIDER ----------
  let s = H.slide(null, 33, { dark: true });
  H.partMarker(s, 5);
  s.addText('PART 5 · AGENTIC AI', { x: 0.55, y: 2.3, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('From asking\nto delegating', { x: 0.55, y: 2.8, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('Chat prompts ask for text. Agentic prompts hand over a job — which changes what a prompt must contain: environment, process, checks, and when to stop and ask you.', { x: 0.55, y: 4.85, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes(
    'HOW TO PRESENT — 1) Progress bar: part 5 — the leap the course is named for. 2) Read the two-line title, one beat of silence. 3) The subtitle names exactly what changes in the prompt: environment, process, checks, and when to stop and ask you. 4) Under 30 seconds, advance.\n' +
    'ACRONYMS — none on this slide.');

  // ---------- 34. WHAT AN AGENT IS ----------
  s = H.slide('PART 5 · WHAT AN AGENT IS', 34);
  H.title(s, 'The mechanics', 'An agent = model + tools + instructions, run in a loop');
  const loop = [['Gather', 'read files, search, look at state'], ['Act', 'one step: edit, run, query, write'], ['Verify', 'check the result against the goal'], ['Repeat', 'adjust and continue — or stop']];
  loop.forEach((st, i) => {
    const x = 0.55 + i * 1.62;
    H.card(s, x, 1.75, 1.45, 1.15, C.TEAL_TINT);
    s.addText(st[0], { x, y: 1.88, w: 1.45, h: 0.4, align: 'center', fontFace: F.head, fontSize: 13, bold: true, color: C.TEAL_DARK, margin: 0 });
    s.addText(st[1], { x: x + 0.06, y: 2.26, w: 1.33, h: 0.6, align: 'center', fontFace: F.body, fontSize: 8.3, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.0 });
    if (i < 3) H.arrow(s, x + 1.46, 2.32, 0.16, C.TEAL);
  });
  s.addShape('line', { x: 6.72, y: 2.9, w: 0, h: 0.4, line: { color: C.MUTE, width: 1.5 } });
  s.addShape('line', { x: 1.27, y: 3.3, w: 5.45, h: 0, line: { color: C.MUTE, width: 1.5 } });
  s.addShape('line', { x: 1.27, y: 2.92, w: 0, h: 0.38, line: { color: C.MUTE, width: 1.5, endArrowType: 'triangle' } });
  s.addText('…until the goal is met, a check fails, or a guardrail says “ask the human”', { x: 1.5, y: 3.36, w: 5.5, h: 0.3, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0 });
  H.card(s, 7.4, 1.75, 5.35, 1.95, C.PANEL);
  s.addText('In the vendors’ words', { x: 7.65, y: 1.92, w: 4.9, h: 0.35, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
  s.addText('“Systems that independently accomplish tasks on your behalf” (OpenAI) · models that “dynamically direct their own processes and tool usage” (Anthropic) — a chatbot that answers and waits is not an agent.', { x: 7.65, y: 2.32, w: 4.85, h: 1.3, fontFace: F.body, fontSize: 10.8, italic: true, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.1 });
  const blocks = [
    ['tool', 'Tools — the arms', 'files, shell, browsers, spreadsheets, email, code. The model requests; the harness executes.'],
    ['branch', 'MCP — the standard port', '“USB-C of AI”: one open protocol to plug tools into any agent. Linux Foundation-governed since Dec 2025; ~half a billion SDK downloads/month by mid-2026.'],
    ['memory', 'Memory = files', 'Context window is short-term memory; notes, logs, and git are long-term. Nothing survives a session unless written down.'],
    ['shield', 'Guardrails', 'permissions, sandboxes, approval gates for consequential actions — covered later this part.'],
  ];
  blocks.forEach((b, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 3.95 + Math.floor(i / 2) * 1.35;
    H.card(s, x, y, 5.95, 1.2, C.PANEL);
    H.iconCircle(s, x + 0.2, y + 0.34, 0.5, b[0], C.SLATE);
    s.addText([
      { text: b[1], options: { bold: true, color: C.INK, fontSize: 12.5, breakLine: true, paraSpaceAfter: 2 } },
      { text: b[2], options: { color: C.SLATE, fontSize: 10.3 } },
    ], { x: x + 0.85, y: y + 0.08, w: 5.0, h: 1.05, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.04 });
  });
  s.addNotes(
    'HOW TO PRESENT — 1) Say the equation in the title: “an agent is a model, plus tools, plus instructions — run in a loop.” 2) Trace the loop cards with your finger, INCLUDING the return arrow: gather → act → verify → repeat, “…until the goal is met, a check fails, or a guardrail says ask the human.” 3) Right card: the vendors’ own words — land the contrast: “a chatbot that answers and waits is not an agent.” 4) The four blocks below, one line each: tools (the arms), MCP (the standard port), memory = files, guardrails (own slide later this part). 5) Distinguish from scripts: scripts break when reality varies; agents read the result and adjust. 6) Bridge: “what does that change about the PROMPT? Everything — next slide is the heart of the training.”\n' +
    'ACRONYMS — MCP = Model Context Protocol — the open standard for plugging tools into any agent (“USB-C of AI”). SDK = Software Development Kit. USB-C = the universal connector standard (the analogy).\n' +
    'CONTENT — Loop framing is vendor-verbatim (Anthropic Agent SDK: gather context → take action → verify work → repeat). MCP numbers as of Jul 2026 per the MCP project blog.');

  // ---------- 35. THE DISTINCTION ----------
  s = H.slide('PART 5 · THE KEY DISTINCTION', 35);
  H.title(s, 'The heart of this training', 'A generative prompt writes. An agentic prompt commissions.');
  const cmp = [
    ['Specifies', 'WHAT TO WRITE', 'A JOB TO RUN'],
    ['Contains', 'role · task · context · format · examples', 'all of that, PLUS: mission & definition of done · environment & file boundaries · allowed tools · process phases & gates · autonomy rules · self-checks · deliverables & logs'],
    ['Produces', 'one response you read', 'actions + artifacts + a report with evidence'],
    ['Failure mode', 'bad text — just re-prompt', 'wrong ACTIONS: files changed, emails sent. Hence gates, sandboxes, verification'],
    ['Your role', 'reader and editor', 'delegator and reviewer at checkpoints'],
    ['Think of it as', 'briefing a ghost-writer', 'a work order for a contractor'],
  ];
  s.addText('Generative (chat)', { x: 2.6, y: 1.62, w: 4.4, h: 0.35, fontFace: F.head, fontSize: 13.5, bold: true, color: C.SLATE, margin: 0 });
  s.addText('Agentic', { x: 7.35, y: 1.62, w: 5.0, h: 0.35, fontFace: F.head, fontSize: 13.5, bold: true, color: C.TEAL_DARK, margin: 0 });
  cmp.forEach((r, i) => {
    const y = 2.02 + i * 0.78;
    H.card(s, 0.55, y, 12.2, 0.68, i % 2 ? 'FFFFFF' : C.PANEL, i % 2 ? C.LINE : null);
    s.addText(r[0], { x: 0.75, y: y + 0.06, w: 1.75, h: 0.56, fontFace: F.body, fontSize: 10.5, bold: true, color: C.INK, margin: 0, valign: 'middle' });
    s.addText(r[1], { x: 2.6, y: y + 0.05, w: 4.5, h: 0.58, fontFace: F.body, fontSize: 9.6, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 1.0 });
    s.addText(r[2], { x: 7.35, y: y + 0.05, w: 5.2, h: 0.58, fontFace: F.body, fontSize: 9.6, color: i === 1 ? C.TEAL_DARK : C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 1.0 });
  });
  s.addNotes(
    'HOW TO PRESENT — 1) Announce it: “if you remember one slide from today, make it this one.” 2) Walk the rows TOP TO BOTTOM; per row read the LEFT cell, then the RIGHT: what to write vs a job to run; one response vs actions-plus-evidence. 3) SLOW on two rows: “Contains” — the agentic column is a superset, everything from Part 3 plus the job wrapper; and “Failure mode” — bad text costs a re-prompt, wrong ACTIONS change files and send emails — hence gates, sandboxes, verification. 4) Close on the last row: briefing a ghost-writer vs a work order for a contractor. 5) Bridge: “that superset isn’t arbitrary — it’s inherited. The map.”\n' +
    'ACRONYMS — none new on this slide.\n' +
    'CONTENT — The contractor analogy is our framing, but rests directly on OpenAI’s “on your behalf” definition and Anthropic’s guidance that specs name files, scope, and end-to-end verification.');

  // ---------- INHERITANCE MAP (v1.1) ----------
  s = H.slide('PART 5 · THE INHERITANCE MAP', 36);
  H.title(s, 'The inheritance map', 'The agentic brief is the anatomy, grown up to survive autonomy');
  const inh = [
    ['Role', '<role>', 'persists across unsupervised decisions → behaviors only'],
    ['Task', '<mission>', '+ a definition of done — the loop needs an exit condition'],
    ['Context', '<context> + <inputs>', '+ a per-source register with grain & trust — agents touch every source repeatedly'],
    ['Format', '<outputs> + <reporting>', '+ audit logs and a fixed status shape — actions must be traceable'],
    ['Examples', 'the filled brief', 'a worked run is the agentic few-shot'],
    ['The Out', 'UNKNOWN → open items', 'not-knowing becomes a logged, owned item'],
    ['The Stop', 'gates + autonomy rules', 'scope control becomes checkpointed process'],
    ['(new in kind)', '<environment> <plan> <checks> <rules> <quality_bar>', 'conduct, method, verification, invariants, completeness — text-only prompts never needed them'],
  ];
  s.addText('Generative element', { x: 0.75, y: 1.6, w: 2.2, h: 0.32, fontFace: F.body, fontSize: 11, bold: true, color: C.SLATE, margin: 0 });
  s.addText('Agentic descendant', { x: 3.1, y: 1.6, w: 3.4, h: 0.32, fontFace: F.body, fontSize: 11, bold: true, color: C.TEAL_DARK, margin: 0 });
  s.addText('What was added — and why', { x: 6.7, y: 1.6, w: 5.5, h: 0.32, fontFace: F.body, fontSize: 11, bold: true, color: C.INK, margin: 0 });
  inh.forEach((r, i) => {
    const y = 1.98 + i * 0.56;
    H.card(s, 0.55, y, 12.2, 0.48, i % 2 ? 'FFFFFF' : C.PANEL, i % 2 ? C.LINE : null);
    s.addText(r[0], { x: 0.75, y: y + 0.03, w: 2.2, h: 0.42, fontFace: F.body, fontSize: 10.5, bold: true, color: C.INK, margin: 0, valign: 'middle' });
    s.addText(r[1], { x: 3.1, y: y + 0.03, w: 3.45, h: 0.42, fontFace: 'Consolas', fontSize: 9.5, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText(r[2], { x: 6.7, y: y + 0.03, w: 5.85, h: 0.42, fontFace: F.body, fontSize: 9.5, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.95 });
  });
  H.callout(s, 0.55, 6.6, 12.2, 0.52, C.AMBER_TINT, [
    { text: 'Why the superset exists: ', options: { bold: true, color: C.INK, fontSize: 10.5 } },
    { text: 'text that fails costs a re-prompt; actions that fail change the world. The new blocks govern conduct.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'branch', iconFill: C.AMBER, size: 10.5 });
  s.addNotes(
    'HOW TO PRESENT — 1) Frame: “every agentic block is a generative element, grown up to survive autonomy.” 2) Read exactly TWO rows aloud, fully: Task → <mission> (+ a definition of done — the loop needs an exit) and The Stop → gates + autonomy rules (scope control becomes checkpointed process). The pattern lands; SWEEP the remaining rows. 3) Bottom row “(new in kind)”: five conduct blocks text-only prompts never needed. 4) Amber band: why the superset exists — text fails cheap; actions fail expensive. 5) Bridge: “so the twelve blocks on the next slide are inevitable, not arbitrary.”\n' +
    'ACRONYMS — UNKNOWN → open items = the logging convention: not-knowing becomes a written, owned item instead of a silent guess.\n' +
    'CONTENT — v1.1 addition — the deepest idea in the training, promoted from the handout. This mapping is also the spine of the Taxonomy Reference handout (agentic elements inherit from generative ones — Mission extends Task).');

  // ---------- 36. MISSION BRIEF ----------
  s = H.slide('PART 5 · THE MISSION BRIEF', 36);
  H.title(s, 'Template A1', 'The mission brief: twelve blocks, each preventing a failure');
  const briefBlocks = [
    ['<role>', 'behaviours, not titles — “never invents numbers” beats “senior analyst”'],
    ['<mission>', 'one goal, one audience, one deadline, “done looks like…”'],
    ['<context>', 'glossary, quirks, targets — the tribal knowledge it can’t infer'],
    ['<environment>', 'where to read, where to write, what’s forbidden. Inputs are read-only'],
    ['<inputs>', 'each source: location, format, what one row means, trust level'],
    ['<plan>', 'the steps in order · methods allowed · methods needing permission'],
    ['<checks>', 'HARD (stop the run) vs SOFT (flag) — written so the agent can evaluate them'],
    ['<outputs>', 'exact deliverable names + the three logs: CHANGES · FINDINGS · OPEN_ITEMS'],
    ['<process>', 'phases with human gates: definitions → mid-run review → pre-render approval'],
    ['<rules>', 'the non-negotiables: never invent data, versioned outputs, assumptions logged'],
    ['<quality_bar>', 'definition of done as a checklist the agent must satisfy — and you can audit'],
    ['<reporting>', 'the exact shape of the final message: status, headline, evidence, open items'],
  ];
  briefBlocks.forEach((b, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.62 + Math.floor(i / 2) * 0.82;
    H.card(s, x, y, 5.95, 0.72, C.PANEL);
    s.addText(b[0], { x: x + 0.18, y: y + 0.06, w: 1.75, h: 0.6, fontFace: 'Consolas', fontSize: 10.5, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText(b[1], { x: x + 1.98, y: y + 0.05, w: 3.85, h: 0.62, fontFace: F.body, fontSize: 9.3, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.98 });
  });
  H.callout(s, 0.55, 6.5, 12.2, 0.55, C.TEAL_TINT, [
    { text: 'Grounding: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 10.5 } },
    { text: 'every block maps to vendor guidance — verifiable done-criteria, file boundaries, least-privilege tools, phased plans with approval, ask-before-irreversible, evidence over assertions.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'check', iconFill: C.TEAL, size: 10.5 });
  s.addNotes(
    'HOW TO PRESENT — 1) Do NOT read twelve blocks. Frame: “each block exists because a specific failure taught someone to add it.” 2) Pick THREE and tell their failure stories: <checks> — the run can fail loudly instead of finishing wrong; <process> — gates catch errors at the cheap end; <reporting> — a status you read in 30 seconds. 3) Gesture over the rest: “the annotated template with a fill-in guide is A1 in your library — and every block is in the Taxonomy Reference with its options.” 4) Teal band: every block maps to published vendor guidance. 5) Bridge: “here’s A1 running a real job.”\n' +
    'ACRONYMS — HARD / SOFT = check severities — HARD stops the run, SOFT flags and continues. CHANGES · FINDINGS · OPEN_ITEMS = the three log files the agent keeps. A1 = the mission-brief template’s library code.\n' +
    'CONTENT — The full annotated template with a fill-in guide is prompt-library/agentic/A1; A2 is the complete worked version.');

  // ---------- 37. WORKED EXAMPLE ----------
  s = H.slide('PART 5 · WORKED EXAMPLE', 37);
  H.title(s, 'Template A2', 'One prompt, five links: data in, defensible slide out');
  const chain = [
    ['inbox', 'Extract', 'read-only; hash and profile every input; parse with explicit types; fix nothing yet'],
    ['tool', 'Transform', 'one schema, ordered rules — each logged with rows affected; metrics defined as cards'],
    ['check', 'Validate', 'reconcile to a known total; identities hold; HARD fail = STOP and report'],
    ['chart', 'Analyze', 'answer the numbered questions, then stop; “associated with,” never “caused by”'],
    ['layout', 'Present', 'headline titles with the number; n on every proportion; source + as-of footer'],
  ];
  chain.forEach((cd, i) => {
    const x = 0.55 + i * 2.5;
    H.card(s, x, 1.7, 2.3, 2.5, C.PANEL);
    H.iconCircle(s, x + 0.2, 1.92, 0.5, cd[0], C.TEAL);
    s.addText(cd[1], { x: x + 0.2, y: 2.52, w: 1.9, h: 0.35, fontFace: F.head, fontSize: 13.5, bold: true, color: C.INK, margin: 0 });
    s.addText(cd[2], { x: x + 0.2, y: 2.9, w: 1.95, h: 1.2, fontFace: F.body, fontSize: 9.3, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.05 });
    if (i < 4) H.arrow(s, x + 2.32, 2.9, 0.16, C.TEAL);
  });
  const gates = [
    ['GATE 1 · Definitions', 'before any data is touched: the agent restates metrics, schema, assumptions — you confirm. Catches the wrong denominator for pennies.'],
    ['GATE 2 · Reconciliation', 'after transform: totals tie to a number you already trust. Any HARD check fails → the run stops, with the offending rows.'],
    ['GATE 3 · Headlines', 'before rendering: slide titles + bullets as plain text. Re-rendering is cheap; re-thinking a circulated deck is not.'],
  ];
  gates.forEach((g, i) => {
    const x = 0.55 + i * 4.18;
    H.card(s, x, 4.5, 3.95, 1.45, C.AMBER_TINT);
    s.addText([
      { text: '▶ ' + g[0], options: { bold: true, color: C.AMBER, fontSize: 12, breakLine: true, paraSpaceAfter: 3 } },
      { text: g[1], options: { color: C.SLATE, fontSize: 10 } },
    ], { x: x + 0.22, y: 4.62, w: 3.55, h: 1.25, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.05 });
  });
  H.callout(s, 0.55, 6.2, 12.2, 0.75, C.TEAL_TINT, [
    { text: 'Between gates: full autonomy. ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12 } },
    { text: 'Ask only if: a HARD check fails · an input isn’t as described · a definition is ambiguous · a published number would change. Otherwise, proceed.', options: { color: C.SLATE, fontSize: 12 } },
  ], { iconName: 'zap', iconFill: C.TEAL, size: 12 });
  s.addNotes(
    'HOW TO PRESENT — 1) Frame: “one prompt, five links — data in, defensible slide out.” 2) Walk the five phase cards LEFT TO RIGHT, one line each: extract (read-only) → transform (logged rules) → validate (reconcile) → analyze (numbered questions, then stop) → present (headline titles). 3) Then the three amber GATES in order — tell it as ascending cost: definitions caught for pennies → reconciliation before analysis → headlines before rendering (“re-rendering is cheap; re-thinking a circulated deck is not”). 4) Teal band: between gates, full autonomy — read the four ask-only-if conditions; they stop the agent from asking about everything or nothing. 5) Bridge: “arms need supervision — five rules.”\n' +
    'ACRONYMS — ETL = Extract, Transform, Load — the classic data-pipeline shape. HARD = run-stopping check. n = sample size (n on every proportion). as-of = the data-cutoff date stamped on the output. A2 = this template’s library code.\n' +
    'CONTENT — This is the ETL→Presentation template (A2) in the library — a real, reusable prompt for any “take data, make it trustworthy, put the answer in front of people” job.');

  // ---------- 38. GUARDRAILS ----------
  s = H.slide('PART 5 · GUARDRAILS', 38);
  H.title(s, 'Working safely', 'Arms need supervision: five rules for delegating');
  const guard = [
    ['hand', 'Reversible? proceed. Irreversible? ask.', 'Edits in a scratch folder are reversible. Deleting, sending, publishing, overwriting a master — the prompt must say: stop and ask first.'],
    ['key', 'Least privilege', 'Give the minimum access for the shortest time. UK NCSC: “If you cannot understand, monitor or contain an agent’s actions, it is not ready for deployment.”'],
    ['alert', 'Prompt injection is real', 'Anything the agent reads — a web page, an emailed doc, a spreadsheet — can carry hostile instructions. Danger peaks when private data + untrusted content + outbound channels combine: break one leg of that trifecta.'],
    ['package', 'Vet third-party “skills”', 'Community plugins are unsigned code + instructions. The #1-ranked community skill for one popular open agent was silently exfiltrating data (Cisco, Jan 2026). Treat skills like unqualified suppliers: inspect before install.'],
    ['eye', 'Demand evidence, not assertions', '“Done” means: the check it ran, the output it got, the file re-opened and verified. Spot-check agent work like any new hire’s — trust grows with track record.'],
  ];
  guard.forEach((g, i) => {
    const y = 1.62 + i * 1.02;
    H.iconRow(s, 0.55, y, 12.2, g[0], i === 2 || i === 3 ? C.RED : C.TEAL, g[1], g[2], { d: 0.5, headSize: 13, descSize: 10.8, h: 0.98 });
  });
  s.addNotes(
    'HOW TO PRESENT — 1) Five rules TOP TO BOTTOM; rule 1 is the keystone, say it as the sentence: “reversible? proceed. Irreversible? ask.” 2) On the red injection rule: the lethal trifecta — private data + untrusted content + an outbound channel; break any one leg and exfiltration paths close. 3) On the red skills rule: the Cisco story — the #1-ranked community skill for a popular open agent was silently exfiltrating data; treat skills like unqualified suppliers. 4) Rule 5 closes the loop: demand evidence, not assertions — spot-check agent work like a new hire’s. 5) Bridge: “supervision costs effort — next slide is where agentic prompting pays it back.”\n' +
    'ACRONYMS — NCSC = (UK) National Cyber Security Centre. CVE = Common Vulnerabilities and Exposures — the public registry of security flaws.\n' +
    'CONTENT — “Lethal trifecta” = Willison, 2025. NCSC’s memorable point: under the hood there is no data/instruction distinction, “only ever next token” — injection gets mitigated, not solved (browser red-teaming: 23.6% → 11.2% attack success with safeguards; honest residual number). Skills story: Cisco found the top ClawHub skill malicious; supplier-qualification mindset applies.');

  // ---------- 39. STANDING MEMORY ----------
  s = H.slide('PART 5 · STANDING MEMORY', 39);
  H.title(s, 'Templates A3 + A4', 'Write the brief once — the workspace remembers');
  H.card(s, 0.55, 1.65, 6.0, 4.95, C.PANEL);
  s.addText('A4 · CLAUDE.md / project instructions', { x: 0.85, y: 1.88, w: 5.3, h: 0.4, fontFace: F.head, fontSize: 14.5, bold: true, color: C.TEAL_DARK, margin: 0 });
  H.bullets(s, 0.9, 2.4, 5.4, 4.0, [
    'A file the agent reads at the start of every session — the onboarding packet for your workspace',
    { t: 'Include: folder layout & read/write boundaries · conventions · standing rules & ask-first list · known data quirks', b: true },
    'Exclude: anything it can infer by reading the files, tutorials, stale details',
    'Keep it ≤ ~60 lines. Per line ask: “would removing this cause mistakes?” If not, cut — bloat drowns your real instructions',
    'Never: credentials, personal data. It’s read every session and lives in history',
  ], { size: 11.5, gap: 7 });
  H.card(s, 6.75, 1.65, 6.0, 4.95, C.TEAL_TINT);
  s.addText('A3 · Reuse by diff', { x: 7.05, y: 1.88, w: 5.3, h: 0.4, fontFace: F.head, fontSize: 14.5, bold: true, color: C.TEAL_DARK, margin: 0 });
  H.bullets(s, 7.1, 2.4, 5.4, 4.0, [
    'The economics of agentic prompting: the full mission brief is written once, stored in the workspace',
    { t: 'Each cycle’s prompt is then ten lines: new input paths, the as-of date, deltas to watch, this cycle’s extra gate', b: true },
    'Delta reporting: compare every headline metric to last cycle; moves beyond threshold get one-line explanations',
    'When a definition changes at a gate — update the standing brief in the same session, log it in CHANGES.md',
    'After two “just this once” exceptions, fold them into the brief',
  ], { size: 11.5, gap: 7 });
  s.addNotes(
    'HOW TO PRESENT — 1) LEFT card first (A4): CLAUDE.md is the onboarding packet the agent reads every session. Walk its bullets: include / exclude / keep it ≤ ~60 lines (“would removing this cause mistakes? If not, cut”) / never credentials. 2) RIGHT card (A3): reuse by diff — the brief is written ONCE; each cycle’s prompt is then ten lines; deltas beyond threshold get one-line explanations; after two “just this once” exceptions, fold them in. 3) Say the economics sentence: “this is where briefs stop being prompts and start being investments.” 4) Bridge: “a standing brief IS a managed prompt — Part 6 is management.”\n' +
    'ACRONYMS — CLAUDE.md / AGENTS.md = standing-instruction files (Anthropic’s name / the cross-vendor standard). CHANGES.md = the change-log file. .md = Markdown, a plain-text document format. A3 / A4 = these templates’ library codes.\n' +
    'CONTENT — This is where agentic prompting pays compound interest. AGENTS.md: 60k+ open-source projects use it; governed by the Linux Foundation’s Agentic AI Foundation.');

  // ---------- P5 REP (v1.1, skippable) ----------
  s = H.slide('THREE-MINUTE REP · PART 5', 40);
  H.title(s, 'Three-minute rep', 'Write one gate');
  H.repTimer(s);
  H.card(s, 0.55, 1.75, 7.4, 3.4, C.TEAL_TINT);
  H.bullets(s, 0.9, 2.05, 6.6, 2.9, [
    { t: 'Think of one job you would delegate to an agent — a recurring report, a folder to process.', b: true },
    { t: 'Write its GATE 1 line: what must you confirm before it touches anything?' },
    { t: 'Write one HARD check: an equality the agent can actually evaluate, anchored to a number you already trust.' },
  ], { size: 13, gap: 10 });
  H.card(s, 8.25, 1.75, 4.5, 3.4, C.PANEL);
  s.addText([
    { text: 'Shape to aim for (presenter)', options: { bold: true, color: C.INK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 5 } },
    { text: '“GATE 1: restate the metric definitions and the file layout; wait for my OK.”\n\n“HARD: computed totals must equal last cycle’s published total exactly.”', options: { color: C.SLATE, fontSize: 11, italic: true } },
  ], { x: 8.52, y: 1.95, w: 3.95, h: 3.0, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.12 });
  s.addText('Skippable if running long — the A1 template carries the full scaffold.', { x: 0.55, y: 5.45, w: 12.2, h: 0.35, fontFace: F.body, fontSize: 10.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT — 1) 3:00 badge. Everyone picks one job they would delegate — a recurring report, a folder to process. 2) Write its GATE 1 line: what must be confirmed before the agent touches anything. 3) Write one HARD check: an equality the agent can actually evaluate, anchored to a number already trusted. 4) Debrief with the line: “where the gate felt hard to write, your process was fuzzy all along.” 5) Reveal the presenter shapes in the right card only at the end.\n' +
    'ACRONYMS — GATE = a human checkpoint the agent must stop at. HARD = a run-stopping check.\n' +
    'CONTENT — Three minutes. Skippable — the A1 template carries the full scaffold.');

  // ---------- 40. PART 6 DIVIDER ----------
  s = H.slide(null, 40, { dark: true });
  H.partMarker(s, 6);
  s.addText('PART 6 · PROMPT MANAGEMENT', { x: 0.55, y: 2.3, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('Prompts are assets.\nManage them like it.', { x: 0.55, y: 2.8, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('A good prompt took an hour of iteration to earn. Re-typing it from memory throws that hour away — and gives your teammate a worse version than yours.', { x: 0.55, y: 4.85, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes(
    'HOW TO PRESENT — 1) Progress bar: final part. 2) Read the two lines; the subtitle IS the argument — an hour of iteration, thrown away by retyping. 3) Under 30 seconds, advance.\n' +
    'ACRONYMS — none on this slide.');

  // ---------- 41. THE LADDER ----------
  s = H.slide('PART 6 · THE PROMOTION LADDER', 41);
  H.title(s, 'From retyping to asset', 'The promotion ladder — and when to climb it');
  const ladder = [
    ['edit', '1 · One-off prompt', 'Typed, used, gone. Fine for genuinely one-time asks.'],
    ['save', '2 · Personal library', 'A saved-prompts doc or text-expander snippets. Zero infrastructure; start today.'],
    ['users', '3 · Team library', 'A shared database — Notion, SharePoint list, Copilot Prompt Gallery. One tested template, everyone’s baseline.'],
    ['package', '4 · Packaged & auto-applied', 'Project instructions, Claude Skills, Gems, Copilot agents: the prompt loads itself when the context matches.'],
    ['branch', '5 · Prompts as code', 'CLAUDE.md / AGENTS.md / briefs in the repo, versioned in git, reviewed like code. Where agentic briefs live.'],
  ];
  ladder.forEach((l, i) => {
    const y = 1.62 + i * 0.99;
    H.iconRow(s, 0.55, y, 6.9, l[0], C.TEAL, l[1], l[2], { d: 0.48, headSize: 12.5, descSize: 10.2, h: 0.95 });
  });
  H.card(s, 7.75, 1.62, 5.0, 3.1, C.TEAL_TINT);
  s.addText('The promotion trigger', { x: 8.02, y: 1.82, w: 4.5, h: 0.4, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
  s.addText('Anthropic’s rule of thumb: the moment you’ve explained the same task more than once, it’s time to package it.\n\nRefined an approach you want repeated? Package it. Quality depends on reference material? Package it with the material.', { x: 8.02, y: 2.3, w: 4.5, h: 2.3, fontFace: F.body, fontSize: 11.5, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.12 });
  H.card(s, 7.75, 4.9, 5.0, 1.7, C.PANEL);
  s.addText([
    { text: 'A familiar discipline: ', options: { bold: true, color: C.INK, fontSize: 11.5, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'a prompt library is run like controlled work instructions — a name, an owner, a revision, a review date. Same muscle, lighter weight.', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 8.02, y: 5.08, w: 4.5, h: 1.4, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.1 });
  s.addNotes(
    'HOW TO PRESENT — 1) Walk the rungs 1→5 down the left side: one line on what each is, one on when to climb. 2) Right top card: the promotion trigger — say Anthropic’s rule: “explained the same task more than once? Package it.” 3) Right bottom card: the familiar discipline — controlled work instructions, lighter weight. 4) Land the expectation: “most of you should live at rungs 2–3 within a month; rung 5 is where Part 5’s briefs live.” 5) Bridge: “so WHERE exactly do these live, tool by tool?”\n' +
    'ACRONYMS — CLAUDE.md / AGENTS.md = standing-instruction files (rung 5). SOP (notes only) = Standard Operating Procedure.\n' +
    'CONTENT — The promotion ladder maps effort to value (a different ladder from Part 1’s escalation ladder — name them fully if anyone conflates them). Rung 4 is where consistency stops depending on people remembering. The SOP analogy is a process analogy — don’t imply regulatory equivalence.');

  // ---------- 42. WHERE TO STORE ----------
  s = H.slide('PART 6 · WHERE THINGS LIVE', 42);
  H.title(s, 'The storage map', 'Every tool has a home for reusable prompts — Aug 2026');
  const stores = [
    ['ChatGPT', 'Projects (files + project instructions) · custom GPTs — transitioning to workspace agents on business plans'],
    ['Claude', 'Projects (instructions + knowledge) · Styles (tone) · Skills — a folder with SKILL.md that loads itself when relevant'],
    ['Gemini', 'Gems (instructions + knowledge files, shareable via Drive permissions) · saved prompt “skills” in Chrome'],
    ['Copilot', 'Prompt Gallery — save, share to a Team, admin-auditable, stays inside your tenant · Agent Builder for packaged agents'],
    ['Any tool', 'The team library database: name · purpose · template · owner · version + change note · models tested · last tested · example output · status'],
    ['Agentic (repo)', 'CLAUDE.md / AGENTS.md at the root · briefs and skills in versioned folders · reviewed like code — this training’s repo is the worked example'],
  ];
  stores.forEach((st, i) => {
    const y = 1.62 + i * 0.82;
    H.card(s, 0.55, y, 12.2, 0.72, i >= 4 ? C.TEAL_TINT : C.PANEL);
    s.addText(st[0], { x: 0.8, y: y + 0.07, w: 1.9, h: 0.58, fontFace: F.head, fontSize: 12.5, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText(st[1], { x: 2.8, y: y + 0.06, w: 9.7, h: 0.6, fontFace: F.body, fontSize: 10.3, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 1.0 });
  });
  H.callout(s, 0.55, 6.65, 12.2, 0.5, C.PANEL, [
    { text: 'Naming collision warning: ', options: { bold: true, color: C.INK, fontSize: 10.5 } },
    { text: '“Skills” means a packaged folder at Anthropic but a saved prompt in Chrome’s Gemini — check which one a colleague means.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'help', iconFill: C.SLATE, size: 10.5, line: C.LINE });
  s.addNotes(
    '[REFRESH QUARTERLY — owner: Oscar]\n' +
    'HOW TO PRESENT — 1) Frame: “wherever you already work, there’s a home for reusable prompts.” 2) Walk the six rows fast, top to bottom — one breath each for the four vendor rows. 3) SLOW on the two teal rows: “Any tool” — the team-library field list is the takeaway for teams with none of these products; and “Agentic (repo)” — this training’s own repo is the worked example. 4) Bottom callout: the naming collision — “Skills” means different things at Anthropic and in Chrome’s Gemini; check which one a colleague means. 5) Bridge: “a live library needs house rules — last content slide.”\n' +
    'ACRONYMS — GPT (custom GPTs) = OpenAI’s packaged assistants. SKILL.md = the file that defines a Claude Skill. Gems = Gemini’s packaged prompt bundles (a product name).\n' +
    'CONTENT — Vendor features verified Aug 2026: OpenAI announced workspace agents (Apr 2026) as the custom-GPT successor for orgs; Claude Skills use progressive disclosure (metadata always loaded, body on trigger); Copilot Prompt Gallery prompts stay in the tenant boundary and are admin-exportable; Gem sharing rides Drive permissions.');

  // ---------- 43. CONVENTIONS + GOVERNANCE ----------
  s = H.slide('PART 6 · CONVENTIONS & GOVERNANCE', 43);
  H.title(s, 'House rules', 'Conventions that keep a library alive — and safe');
  H.card(s, 0.55, 1.65, 6.0, 4.95, C.PANEL);
  s.addText('Conventions (this library uses them)', { x: 0.85, y: 1.88, w: 5.3, h: 0.4, fontFace: F.head, fontSize: 14, bold: true, color: C.TEAL_DARK, margin: 0 });
  H.bullets(s, 0.9, 2.38, 5.4, 4.1, [
    { t: '{{placeholders}} for everything that changes per run — mail-merge fields for prompts; search for “{{” before running' },
    { t: '[optional] blocks you delete when unused' },
    { t: 'Version + one-line change note — Rev A/B/C discipline, lighter weight; note which model it was tested on' },
    { t: 'A filled example next to every blank template — the gold standard that shows what “good” looks like' },
    { t: 'Test on 3–5 real cases (one edge case) before marking approved; re-test after model changes', b: true },
    { t: 'Every approved prompt has a named owner and a review cadence' },
  ], { size: 11, gap: 7 });
  H.card(s, 6.75, 1.65, 6.0, 3.1, C.RED_TINT);
  s.addText('Governance: prompts contain data', { x: 7.05, y: 1.88, w: 5.3, h: 0.4, fontFace: F.head, fontSize: 14, bold: true, color: C.RED, margin: 0 });
  H.bullets(s, 7.1, 2.38, 5.4, 2.3, [
    { t: 'A stored prompt often carries supplier names, pricing, findings, draft language — classify the library like the documents it quotes', b: true },
    { t: 'Never store credentials, personal data, or patient-adjacent examples in a template — {{placeholders}} supply them at run time' },
    { t: 'Shared = distributed. Owner approval before team-wide sharing; treat third-party skills like installing software — audit first' },
  ], { size: 11, gap: 7 });
  H.card(s, 6.75, 4.95, 6.0, 1.65, C.TEAL_TINT);
  s.addText([
    { text: 'Tools change; the practice doesn’t. ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'Prompt-tooling startups get acquired and shut down yearly. Version it, test it, own it — that discipline outlives every platform.', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 7.05, y: 5.13, w: 5.45, h: 1.4, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.1 });
  s.addNotes(
    'HOW TO PRESENT — 1) LEFT card: six conventions this very library uses; read the BOLD one in full — test on 3–5 real cases including an edge case, re-test after model changes. 2) RIGHT red card SLOWLY — it matters most in this room: stored prompts CONTAIN data (supplier names, pricing, findings) — classify the library like the documents it quotes; placeholders keep secrets out of stored text; shared = distributed. 3) Teal card: tools change, the practice doesn’t — version it, test it, own it. 4) Bridge: “last rep — the whole training cashes out.”\n' +
    'ACRONYMS — Rev A/B/C = revision-letter discipline from document control. {{placeholders}} = fill-in-at-run-time fields (mail-merge for prompts).\n' +
    'CONTENT — The {{placeholder}} rule is doing double duty — reuse AND keeping sensitive values out of stored text. Market-churn example if asked: Humanloop (early leader) shut down Sept 2025 when Anthropic hired the team; the practice survived the product.');

  // ---------- P6 REP (v1.1, skippable) ----------
  s = H.slide('THREE-MINUTE REP · PART 6', 45);
  H.title(s, 'Three-minute rep', 'Pick your rung, pick your prompt');
  H.repTimer(s);
  H.card(s, 0.55, 1.75, 12.2, 3.2, C.TEAL_TINT);
  H.bullets(s, 0.9, 2.1, 11.4, 2.2, [
    { t: 'Which rung of the promotion ladder are you on today — one-off typing, personal doc, team library, packaged, as-code?', b: true },
    { t: 'Name the ONE prompt you already reuse from memory. That is your first library entry.' },
    { t: 'Write where it will live and its v1.0 line — you have just started your prompt library.' },
  ], { size: 13.5, gap: 11 });
  const rungPills = ['1 · one-off', '2 · personal doc', '3 · team library', '4 · packaged', '5 · as-code'];
  rungPills.forEach((p, i) => {
    const x = 0.9 + i * 2.28;
    s.addShape('roundRect', { x, y: 4.18, w: 2.12, h: 0.5, rectRadius: 0.1, fill: { color: 'FFFFFF' }, line: { color: C.TEAL, width: 1 } });
    s.addText(p, { x, y: 4.19, w: 2.12, h: 0.48, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 11, bold: true, color: C.TEAL_DARK, margin: 0 });
    if (i < 4) H.arrow(s, x + 2.13, 4.43, 0.14, C.TEAL);
  });
  s.addText('This one is not skippable — it is the whole training cashing out.', { x: 0.55, y: 5.3, w: 12.2, h: 0.35, fontFace: F.body, fontSize: 10.5, italic: true, color: C.AMBER, margin: 0 });
  s.addNotes(
    'HOW TO PRESENT — 1) 3:00 badge — but this one is PROTECTED: never cut it, even if everything else ran long. 2) Three prompts on screen: pick your rung (use the pill row as the picker) → name the ONE prompt you already reuse from memory → write where it will live and its v1.0 line. 3) Walk the room while they write; get two people to say their entry out loud — public commitment sticks. 4) Close: “you have just started your prompt library.”\n' +
    'ACRONYMS — v1.0 = first-version label.\n' +
    'CONTENT — Final rep — a named prompt with a home and a version number is the behavior change the training exists for.');
};