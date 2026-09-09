// PART 2 — Models & tools landscape (v1.6: trading cards, big bill + MoE hospital, data matrix, brand logos; verified Sep 9, 2026)
const { C, F } = require('./deck_lib');

module.exports = function buildPartTwo(pres, H) {
  // ---------- 15. PART 2 DIVIDER ----------
  let s = H.slide(null, 15, { dark: true });
  H.partMarker(s, 2);
  s.addText('PART 2 · MODELS & TOOLS', { x: 0.55, y: 2.3, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('The landscape,\nSeptember 2026', { x: 0.55, y: 2.8, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('Who makes what, what each is genuinely known for, whom to trust with which data, what the Chinese open-weight wave changed — and the tools worth knowing by name. Everything dated: this field re-ranks monthly.', { x: 0.55, y: 4.85, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Progress bar: part 2 of 6.\n' +
    '2) One framing sentence: “Names, fortes and trust, all dated September 2026 — the names churn monthly; the habits you leave with don’t.”\n' +
    '3) Under 30 seconds, advance.\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none on this slide.');

  // ---------- 16. ASSISTANT TRADING CARDS ----------
  s = H.slide('PART 2 · THE ASSISTANTS', 16);
  H.title(s, 'Six assistants, six different jobs', 'Pick by task, not habit — September 2026');
  const vendors = [
    ['openai', 'ChatGPT', 'OpenAI · GPT-5.6 family (Sol / Terra / Luna)', 'The everything assistant', 'Largest user base; fastest at drafts, options and marketing copy; images, voice, agent mode.', 'Fast model churn and renaming; check data settings before regulated content.'],
    ['gemini', 'Gemini', 'Google · Gemini 3 / 3.1 Pro / 3.6 Flash', 'Everywhere Google is', 'Multimodal breadth (video, images, audio) + the deepest Workspace integration — 1B+ monthly users; default AI in Gmail, Docs, Meet.', 'Model-name sprawl; the best reasoning (Deep Think) sits behind the Ultra tier.'],
    ['copilot', 'Copilot', 'Microsoft · GPT-5.6 preferred + Claude selectable', 'The governed one — inside your tenant', '30M+ paid seats inside the M365 compliance boundary IT already audits; its Cowork agent runs on Claude technology.', 'Licenses others’ models; admin flags mean colleagues get different capabilities.'],
    ['claude', 'Claude', 'Anthropic · Fable 5 / Opus 5 / Sonnet 5 / Haiku 4.5', 'Best-in-class coding & agentic work', 'Tops SWE-bench AND OpenAI’s own real-work eval (GDPval); 2026 writing evals rank its prose #1; 1M-token documents.', 'Premium pricing at the top tier; the flagship can refuse high-risk domains by design.'],
    ['perplexity', 'Perplexity', 'Perplexity · own stack + Model Council (GPT+Claude+Gemini)', 'Research with receipts', 'Inline citations by default; the lowest citation-error rate in CJR’s AI-search testing — 37%, vs 67% for ChatGPT Search.', 'A citation isn’t proof — click through before quoting anywhere formal.'],
    ['grok', 'Grok', 'xAI (SpaceX) · Grok 4.6', 'Blunt on purpose', '“Unhinged” is a literal voice mode; real-time X data; aggressive price-performance.', 'Fewer guardrails has meant real incidents (Jul 2025 public apology) — care for brand-sensitive work.'],
  ];
  vendors.forEach((v, i) => {
    const x = 0.55 + (i % 3) * 4.18;
    const y = 1.58 + Math.floor(i / 3) * 2.56;
    H.card(s, x, y, 3.95, 2.42, C.PANEL);
    s.addShape('roundRect', { x, y, w: 3.95, h: 0.62, rectRadius: 0.06, fill: { color: 'FFFFFF' }, line: { color: C.LINE, width: 0.75 } });
    H.logo(s, x + 0.14, y + 0.11, 0.4, v[0], v[1][0]);
    s.addText(v[1], { x: x + 0.64, y: y + 0.05, w: 2.1, h: 0.34, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
    s.addText(v[2], { x: x + 0.64, y: y + 0.36, w: 3.2, h: 0.24, fontFace: F.body, fontSize: 7.4, bold: true, charSpacing: 0.3, color: C.MUTE, margin: 0 });
    s.addText(v[3], { x: x + 0.2, y: y + 0.7, w: 3.55, h: 0.52, fontFace: F.head, fontSize: 12.5, bold: true, color: C.TEAL_DARK, margin: 0, lineSpacingMultiple: 0.98 });
    s.addText(v[4], { x: x + 0.2, y: y + 1.24, w: 3.58, h: 0.78, fontFace: F.body, fontSize: 8.8, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.0 });
    s.addText(v[5], { x: x + 0.2, y: y + 2.0, w: 3.58, h: 0.4, fontFace: F.body, fontSize: 7.8, italic: true, color: C.AMBER, margin: 0, lineSpacingMultiple: 0.95 });
  });
  s.addText('Which of these can see company data? Two slides ahead — trust is about the account tier, not the logo. Fortes verified Sep 9, 2026 — they will have moved; the habits in Parts 3–5 don’t move at all.', { x: 0.55, y: 6.72, w: 12.2, h: 0.4, fontFace: F.body, fontSize: 10, italic: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 1.02 });
  s.addNotes(
    '[REFRESH QUARTERLY — owner: Oscar]\n' +
    '\n' +
    'HOW TO PRESENT —\n' +
    '1) Frame: “six trading cards — the big bold line on each is what that assistant is genuinely KNOWN FOR. Pick by task, not habit.”\n' +
    '2) Walk the Z: ChatGPT → Gemini → Copilot (the three everyone already has), then Claude → Perplexity → Grok. Say the bold line, one evidence beat, move on; let the amber caveats be read, not spoken.\n' +
    '3) On Grok, the plain version: “Unhinged” is not a nickname — it is an actual personality setting in its voice app, by that name; and in July 2025 a bad update had it praising Hitler for sixteen hours before an apology. That is the trade-off of a deliberately less-filtered assistant.\n' +
    '4) On Copilot, land the licensing fact: Microsoft’s Cowork agent runs on Claude technology — tiers matter more than brand wars.\n' +
    '5) Footer: the trust question is TWO SLIDES AHEAD; fortes verified Sep 9, 2026 and they WILL move.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“One force reshaped this list — the Chinese open-weight wave.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'SWE-bench = Software Engineering benchmark — the standard test of coding-agent ability.\n' +
    'GDPval = OpenAI’s benchmark of 220 real knowledge-work tasks across 44 occupations.\n' +
    'CJR = Columbia Journalism Review (its Tow Center tested AI search citation accuracy).\n' +
    'X = the social platform (Grok’s data source).\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: rebuilt as identity trading cards (assertion-evidence layout, r19) with real product logos; Perplexity’s known-for now leads with the CJR error-rate comparison (the ~94%-with-citations figure was less meaningful — audit H3).\n' +
    'Every claim evidence-backed in notes/research/r13_reputations_r1.md:\n' +
    'Writing: owner’s hunch was “ChatGPT writes better” — 2026 evals say otherwise (LMArena creative-writing June 2026: Anthropic six of top ten, #1; EQ-Bench Aug 2026 agrees). ChatGPT’s honest forte is speed, options, marketing copy.\n' +
    'Claude: SWE-bench ~96% (Sept 2026); GDPval winner (OpenAI’s own eval, Sept 2025); GDPval-AA v2 leader Sept 2026.\n' +
    'Copilot: 30M+ paid seats (Microsoft FY26 Q4, Jul 2026); Copilot Cowork licenses Claude Cowork technology (Mar 2026).\n' +
    'Vendor benchmark numbers are marketing until independently reproduced — read them as claims.\n' +
    'Grok note: xAI was acquired by SpaceX (Feb 2026).\n' +
    'Logos: official site favicons (assets/logos/) — referential brand use inside an internal training deck.');

  // ---------- 17. THE DEEPSEEK MOMENT ----------
  s = H.slide('PART 2 · THE CHINESE WAVE', 17);
  H.title(s, 'The DeepSeek moment', 'January 2025: frontier ability, ~27× cheaper');
  H.card(s, 0.55, 1.58, 5.6, 1.62, C.PANEL);
  H.logo(s, 0.8, 1.72, 0.36, 'deepseek', 'D');
  s.addText('What happened, in three facts', { x: 1.26, y: 1.72, w: 4.7, h: 0.32, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.85, 2.12, 5.05, 1.05, [
    { t: 'DeepSeek-R1: open-weights reasoning rivaling OpenAI’s o1 — MIT-licensed, free to download' },
    { t: 'Nvidia lost $589B in one day (Jan 27) — the largest single-day market loss in history at the time' },
    { t: 'The “$5.6M training cost”? Fuel for the final winning race — not the racing team. Real efficiency, oversold headline.', b: true },
  ], { size: 8.9, gap: 3 });
  H.card(s, 0.55, 3.3, 5.6, 2.52, C.TEAL_TINT);
  s.addText('The trick has a name: MoE — Mixture of Experts', { x: 0.82, y: 3.44, w: 5.1, h: 0.32, fontFace: F.head, fontSize: 13, bold: true, color: C.TEAL_DARK, margin: 0 });
  // — the specialist hospital, drawn —
  const hx = 0.85, hy = 3.92, hw = 1.95, hh = 1.5;
  s.addShape('roundRect', { x: hx, y: hy, w: hw, h: hh, rectRadius: 0.05, fill: { color: 'FFFFFF' }, line: { color: C.TEAL_DARK, width: 1.5 } });
  s.addShape('roundRect', { x: hx + hw / 2 - 0.14, y: hy - 0.26, w: 0.28, h: 0.26, rectRadius: 0.03, fill: { color: C.RED }, line: { type: 'none' } });
  s.addText('+', { x: hx + hw / 2 - 0.14, y: hy - 0.28, w: 0.28, h: 0.26, align: 'center', valign: 'middle', fontFace: F.head, fontSize: 12, bold: true, color: 'FFFFFF', margin: 0 });
  const litWin = [1, 6, 11];
  for (let wi = 0; wi < 16; wi++) {
    const wx = hx + 0.16 + (wi % 4) * 0.45;
    const wy = hy + 0.14 + Math.floor(wi / 4) * 0.3;
    const lit = litWin.includes(wi);
    s.addShape('rect', { x: wx, y: wy, w: 0.3, h: 0.2, fill: { color: lit ? C.AMBER : C.PANEL }, line: { color: lit ? C.AMBER : C.LINE, width: lit ? 1.25 : 0.75 } });
  }
  s.addShape('roundRect', { x: hx + hw / 2 - 0.13, y: hy + hh - 0.32, w: 0.26, h: 0.32, rectRadius: 0.02, fill: { color: C.TEAL_DARK }, line: { type: 'none' } });
  s.addText('671B params — the building · ~37B — the lit departments', { x: hx - 0.05, y: hy + hh + 0.03, w: 2.25, h: 0.34, fontFace: F.body, fontSize: 7.2, italic: true, color: C.TEAL_DARK, margin: 0, align: 'center', lineSpacingMultiple: 0.95 });
  s.addText('Built like a huge specialist hospital: 671 billion parameters on the books, but only ~37 billion — the relevant departments — wake up for any one question. You pay for the specialists consulted, not the whole building. Add distillation (big models teaching small ones) and frontier ability stops being luxury-priced.', { x: 3.0, y: 3.88, w: 3.0, h: 1.85, fontFace: F.body, fontSize: 9.4, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.06 });
  // — the bill, hero —
  H.card(s, 6.35, 1.58, 6.4, 2.15, C.PANEL);
  s.addText('The bill, per million output tokens', { x: 6.62, y: 1.72, w: 5.9, h: 0.32, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
  s.addText('OpenAI o1', { x: 6.62, y: 2.14, w: 1.35, h: 0.3, fontFace: F.body, fontSize: 9.5, color: C.SLATE, margin: 0, valign: 'middle' });
  s.addShape('roundRect', { x: 8.05, y: 2.16, w: 3.3, h: 0.26, rectRadius: 0.04, fill: { color: C.SLATE }, line: { type: 'none' } });
  s.addText('$60', { x: 8.05, y: 2.14, w: 3.25, h: 0.3, align: 'right', valign: 'middle', fontFace: F.head, fontSize: 12, bold: true, color: 'FFFFFF', margin: 0 });
  s.addText('DeepSeek-R1', { x: 6.62, y: 2.56, w: 1.35, h: 0.3, fontFace: F.body, fontSize: 9.5, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
  s.addShape('roundRect', { x: 8.05, y: 2.58, w: 0.14, h: 0.26, rectRadius: 0.02, fill: { color: C.TEAL }, line: { type: 'none' } });
  s.addText('$2.19', { x: 8.24, y: 2.44, w: 1.6, h: 0.52, fontFace: F.head, fontSize: 24, bold: true, color: C.TEAL, margin: 0, valign: 'middle' });
  s.addShape('ellipse', { x: 11.55, y: 2.08, w: 1.0, h: 1.0, fill: { color: C.AMBER }, line: { type: 'none' } });
  s.addText([
    { text: '27×', options: { fontSize: 19, bold: true, breakLine: true } },
    { text: 'cheaper', options: { fontSize: 7.5, bold: true } },
  ], { x: 11.55, y: 2.08, w: 1.0, h: 1.0, align: 'center', valign: 'middle', fontFace: F.head, color: 'FFFFFF', margin: 0, lineSpacingMultiple: 0.9 });
  s.addText('A $100 o1 workload cost ~$3.60 on R1 — this is why the thinking and deep-research modes from Part 1 didn’t stay luxury-priced.', { x: 6.62, y: 3.14, w: 4.8, h: 0.55, fontFace: F.body, fontSize: 9.6, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.03 });
  // — benchmarks, compressed —
  H.card(s, 6.35, 3.82, 6.4, 1.86, C.PANEL);
  s.addText('Same league on the hard benchmarks — R1 paper, Jan 2025', { x: 6.62, y: 3.94, w: 5.9, h: 0.3, fontFace: F.head, fontSize: 12, bold: true, color: C.INK, margin: 0 });
  const bench = [
    ['Math olympiad (AIME 2024)', 79.8, 79.2],
    ['Coding agent (SWE-bench)', 49.2, 48.9],
    ['Science PhD (GPQA)', 71.5, 75.7],
  ];
  bench.forEach((b, i) => {
    const y = 4.28 + i * 0.34;
    s.addText(b[0], { x: 6.62, y, w: 2.35, h: 0.32, fontFace: F.body, fontSize: 8.6, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.95 });
    const barMax = 2.5;
    s.addShape('roundRect', { x: 9.05, y: y + 0.03, w: barMax * (b[1] / 100), h: 0.11, rectRadius: 0.02, fill: { color: C.TEAL }, line: { type: 'none' } });
    s.addText(String(b[1]), { x: 9.08 + barMax * (b[1] / 100), y: y - 0.02, w: 0.5, h: 0.2, fontFace: F.body, fontSize: 7.5, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addShape('roundRect', { x: 9.05, y: y + 0.17, w: barMax * (b[2] / 100), h: 0.11, rectRadius: 0.02, fill: { color: C.SLATE }, line: { type: 'none' } });
    s.addText(String(b[2]), { x: 9.08 + barMax * (b[2] / 100), y: y + 0.12, w: 0.5, h: 0.2, fontFace: F.body, fontSize: 7.5, color: C.SLATE, margin: 0, valign: 'middle' });
  });
  s.addText([
    { text: '■', options: { color: C.TEAL, fontSize: 8, bold: true } }, { text: ' DeepSeek-R1  ', options: { color: C.SLATE, fontSize: 7.8 } },
    { text: '■', options: { color: C.SLATE, fontSize: 8, bold: true } }, { text: ' OpenAI o1 — matched on math & coding, behind on PhD science: not a clean sweep, and that’s the honest story.', options: { color: C.MUTE, fontSize: 7.8 } },
  ], { x: 6.62, y: 5.32, w: 5.9, h: 0.3, fontFace: F.body, margin: 0 });
  H.promptChip(s, 0.55, 5.8, 12.2, 1.32, 8, [
    { type: '“Explain Mixture of Experts like a colleague: a specialist hospital where only the relevant departments wake up per question — and why that made AI dramatically cheaper in 2025. Under 120 words.”', why: 'the MoE cheat-note lands in your course log, told by your own assistant.' },
  ], { label: 'The specialist hospital, explained', size: 8.6, tab: 'EX8-MoE' });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Anchor the moment, LEFT top card: January 2025 — an open model rivals o1; Nvidia’s $589B day; and keep the cost claim honest — the famous $5.6M is the fuel bill for the final winning race, not the cost of the racing team (total hardware spend was estimated well over $500M).\n' +
    '2) LEFT teal card — POINT AT THE DRAWING: the whole hospital is 671 billion parameters; the three lit windows are the ~37 billion that wake up for your question. You pay for the specialists consulted, not the whole building. Distillation = big models teaching small ones.\n' +
    '3) RIGHT top — the star of the slide: $60 against $2.19, and the bars are TRUE proportion (the R1 bar really is 27× shorter). A $100 o1 workload for $3.60.\n' +
    '4) RIGHT bottom: three benchmark pairs — matched on math and coding, behind on PhD science (be honest: not a clean sweep).\n' +
    '5) Close the loop to Part 1: THIS is why thinking modes and deep research became affordable for everyone.\n' +
    '\n' +
    'TRY IT — PROMPT 8/8 (copy from tab EX8-MoE)\n' +
    'Optional if time is tight; the answer doubles as their MoE cheat-note in the log.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“So whose servers is your data on? The trust map.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'MoE = Mixture of Experts — only a fraction of the model computes per token (671B built, ~37B working).\n' +
    'MIT license = a permissive open-source license. R1 = DeepSeek’s open reasoning model; o1 = OpenAI’s.\n' +
    'AIME / GPQA / SWE-bench = math-olympiad, PhD-science and coding-agent benchmarks.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: bill promoted to hero position with true-proportion bars + 27× badge; MoE hospital drawn (owner request); benchmark chart compressed to three rows — MATH-500 (97.3 vs 96.4) and Codeforces (96.3 vs 96.6 percentile) cut for space, quote if asked.\n' +
    'Chart data verified against the R1 paper (arXiv:2501.12948) — see notes/research/r13_reputations_r1.md.\n' +
    'Pricing: R1 $0.55/$2.19 vs o1 $15/$60 per M tokens (Jan 2025) = 27.3–27.4×.\n' +
    'Since then (if asked): DeepSeek stayed the open-weight value leader but slipped off the leading edge — NIST’s CAISI evaluation (May 2026) put it ~8 months behind the frontier.\n' +
    'What the wave brought beyond DeepSeek (spoken if useful): open weights with permissive licenses to self-host (Qwen the most-downloaded family; famously self-hosted by Airbnb) · price pressure that pushed OpenAI to ship its first open-weight models since GPT-2 (gpt-oss, Aug 2025) · trillion-parameter open agentic models (Kimi).\n' +
    'US–China top-model gap: ~3% (Stanford AI Index 2026), down from 18–32 points in 2023.');

  // ---------- 18. SERVERS, TIERS, TRUST ----------
  s = H.slide('PART 2 · TRUST & DATA', 18);
  H.title(s, 'Where your words go', 'Trust the tier, not the logo — Sep 2026');
  const servers = [
    ['claude', 'Anthropic', 'stored in the US · EU via cloud partners (Bedrock / Vertex / Foundry)'],
    ['openai', 'OpenAI', 'EU residency (2025) + in-region processing (2026) — business tiers only'],
    ['google', 'Google', 'enterprise: residency by region · consumer: reviewed chats kept up to 3 yrs'],
    ['microsoft', 'Microsoft', 'EU Data Boundary — but Claude models inside Copilot sit outside it'],
    ['grok', 'xAI', 'own US data centers (Memphis) · no residency options published'],
    ['perplexity', 'Perplexity', 'AWS, worldwide · no residency options published'],
    ['deepseek', 'DeepSeek', '“stored in the People’s Republic of China” — its own privacy policy'],
    ['kimi', 'Kimi (Moonshot)', 'PRC storage · training opt-out only via customer service'],
    [null, 'Z.ai (Zhipu)', 'Singapore processing · parent on the US Entity List'],
  ];
  s.addText('Whose servers, where', { x: 0.55, y: 1.5, w: 5.9, h: 0.32, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
  servers.forEach((r, i) => {
    const y = 1.9 + i * 0.47;
    H.card(s, 0.55, y, 5.9, 0.42, i % 2 ? 'FFFFFF' : C.PANEL, i % 2 ? C.LINE : null);
    H.logo(s, 0.64, y + 0.05, 0.32, r[0], r[1][0]);
    s.addText(r[1], { x: 1.05, y: y + 0.01, w: 1.4, h: 0.4, fontFace: F.body, fontSize: 9.2, bold: true, color: i > 5 ? C.RED : C.TEAL_DARK, margin: 0, valign: 'middle', lineSpacingMultiple: 0.9 });
    s.addText(r[2], { x: 2.48, y: y + 0.01, w: 3.9, h: 0.4, fontFace: F.body, fontSize: 8.2, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.95 });
  });
  // — data-type × tier matrix —
  H.card(s, 6.65, 1.5, 6.1, 4.62, C.PANEL);
  s.addText('What data can go where?', { x: 6.92, y: 1.62, w: 5.6, h: 0.32, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
  s.addText('Company tenants: the major vendors don’t train on your data by default. Personal accounts: they do.', { x: 6.92, y: 1.94, w: 5.6, h: 0.3, fontFace: F.body, fontSize: 8.6, italic: true, color: C.SLATE, margin: 0 });
  const colX = [9.15, 10.45, 11.75], colW = 1.22;
  const heads = [['GREEN', 'Company tenant', C.GREEN], ['YELLOW', 'Personal account', C.AMBER], ['RED', 'China-hosted app', C.RED]];
  heads.forEach((hd, i) => {
    s.addText([
      { text: hd[0], options: { bold: true, color: hd[2], fontSize: 8.5, breakLine: true } },
      { text: hd[1], options: { color: C.SLATE, fontSize: 7 } },
    ], { x: colX[i], y: 2.28, w: colW, h: 0.44, align: 'center', fontFace: F.body, margin: 0, lineSpacingMultiple: 0.92 });
  });
  const rows = [
    ['Public material (already on the internet)', '✓', '✓', '✓'],
    ['Internal, non-confidential', '✓', '✗', '✗'],
    ['Confidential business data', '✓*', '✗', '✗'],
    ['Personal data (PII)', '✓*', '✗', '✗'],
    ['Client & regulated data', '✓*', '✗', '✗'],
  ];
  rows.forEach((r, i) => {
    const y = 2.76 + i * 0.44;
    if (i % 2 === 0) s.addShape('roundRect', { x: 6.85, y, w: 5.75, h: 0.4, rectRadius: 0.04, fill: { color: 'FFFFFF' }, line: { color: C.LINE, width: 0.5 } });
    s.addText(r[0], { x: 6.98, y, w: 2.1, h: 0.4, fontFace: F.body, fontSize: 8.4, bold: true, color: C.INK, margin: 0, valign: 'middle', lineSpacingMultiple: 0.9 });
    [1, 2, 3].forEach(ci => {
      const mark = r[ci];
      const col = mark[0] === '✓' ? (mark.length > 1 ? C.AMBER : C.GREEN) : C.RED;
      s.addText(mark, { x: colX[ci - 1], y, w: colW, h: 0.4, align: 'center', valign: 'middle', fontFace: F.body, fontSize: mark[0] === '✓' ? 12 : 11, bold: true, color: col, margin: 0 });
    });
  });
  s.addText([
    { text: '✓* = only where your AI policy explicitly allows it — and only the minimum needed. ', options: { color: C.SLATE, fontSize: 8.2, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'The 2025 leaks all happened in the YELLOW column: ~300K+ Grok chats indexed by Google; “deleted” ChatGPT chats preserved for court. ', options: { color: C.AMBER, fontSize: 8.2, breakLine: true, paraSpaceAfter: 3 } },
    { text: 'RED = the APP sends data to China, under Chinese law (Italy blocked DeepSeek). The open-weight MODELS, self-hosted by IT on approved servers, are a different object — the app, not the model, is the risk.', options: { color: C.SLATE, fontSize: 8.2 } },
  ], { x: 6.92, y: 5.02, w: 5.6, h: 1.05, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.02 });
  H.callout(s, 0.55, 6.5, 12.2, 0.6, C.TEAL_TINT, [
    { text: 'One question decides: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5 } },
    { text: 'does company data leave your network — and whose account is it on? Company tenant → work, within policy. Personal → public material only. China-hosted app → never.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'key', iconFill: C.TEAL, size: 11 });
  s.addNotes(
    '[REFRESH QUARTERLY — owner: Oscar]\n' +
    '\n' +
    'HOW TO PRESENT —\n' +
    '1) Open with the finding that organizes this slide: the major Western vendors train on CONSUMER chats by default, and none of them trains on enterprise-tier data — so trust tracks the account tier, not the company logo. The same logo appears in green and yellow.\n' +
    '2) LEFT table, fast: whose servers, where. Two rows to slow on: Microsoft (EU Data Boundary — but the Claude models inside Copilot sit OUTSIDE it; your IT team cares) and DeepSeek (its own policy says data is stored in the People’s Republic of China).\n' +
    '3) RIGHT matrix — the new heart of the slide. Read it BY ROW: public material goes anywhere; everything below that line goes only into the company tenant; and the starred rows — confidential, personal data, client data — need the policy to say yes explicitly, minimum necessary. PII = personally identifiable information: names, emails, IDs, anything that points at a person.\n' +
    '4) The amber footnote line: every famous 2025 leak happened in the yellow column — personal accounts.\n' +
    '5) The red story, plainly: using the app is eating at their restaurant (they see your order); downloaded open weights are a cookbook IT can cook from at home (nothing is sent anywhere).\n' +
    '6) Teal band: the one deciding question, verbatim.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“From models to the tools that DO things — the gallery.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'PII = Personally Identifiable Information — data that identifies a person (names, emails, ID numbers).\n' +
    'PRC = People’s Republic of China. EU Data Boundary = Microsoft’s commitment to process EU data inside the EU.\n' +
    'AWS = Amazon Web Services. Entity List = the US federal trade-restriction list — a procurement red flag.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: right side rebuilt as a data-type × tier matrix (owner request); Grok leak count stated as ~300K+ (reported figures vary 300–370K — audit L2).\n' +
    'Every row and tier claim sourced in notes/research/r11_vendor_trust.md (researched Sep 9, 2026), incl.: consumer-training defaults; OpenAI court-ordered retention of “deleted” chats (2025, enterprise excluded); Italy’s DeepSeek block (Jan 2025, not lifted); DeepSeek’s exposed chat-log database (Jan 2025); Kimi PRC storage; Z.ai Entity-List parent.\n' +
    'Green ≠ invulnerable: EchoLeak (CVE-2025-32711, Jun 2025) was a zero-click prompt-injection exfiltration hole in enterprise Copilot — patched, but proof that novel attack surface exists even in green.\n' +
    'Defaults drift (Anthropic flipped consumer training Aug 2025; Microsoft Oct 2024) — re-verify quarterly.\n' +
    'Standing rule, always said aloud: your organization’s AI policy and approved-tool list outrank everything on this slide.');

  // ---------- 19. AGENT GALLERY — THE DOERS ----------
  s = H.slide('PART 2 · AGENTIC TOOLS', 19);
  H.title(s, 'The agent gallery · the doers', 'Agents that run jobs — names you’ll hear');
  const gallery = [
    ['claude', 'C', 'Claude Code', 'Anthropic', 'Agentic coding AND general file/data automation — points at a real folder: reads PDFs, builds spreadsheets, writes reports. Built this training’s materials.'],
    ['claude', 'C', 'Claude Cowork', 'Anthropic', 'The same engine for non-technical knowledge work: “describe the outcome, step away, come back to finished files.” Licensed by Microsoft as Copilot Cowork.'],
    ['openai', 'C', 'ChatGPT Work', 'OpenAI', 'Agent mode beside Chat: connects Slack/Gmail/Drive, runs scheduled tasks, produces decks, sheets, small apps.'],
    ['copilot', 'C', 'Copilot agents', 'Microsoft', 'Researcher, Analyst, Excel Agent Mode, Copilot Studio — governed agents inside your tenant. The path of least resistance at most enterprises.'],
    ['manus', 'M', 'Manus', 'independent (Singapore)', 'The famous general agent: goal in, finished multi-step work out. So famous Meta paid ~$2B for it (Dec 2025) — and Beijing forced the deal apart (Apr 2026). Try it personally; don’t feed it company data.'],
    ['notion', 'N', 'Notion Agents', 'Notion', 'Agents living inside the workspace you may already use: run 24/7 on triggers (schedules, Slack, email), build docs and databases, shareable with the team.'],
    ['zapier', 'Z', 'Automation platforms', 'n8n · Zapier', 'Wire apps together with agent steps in the flow: n8n for technical/self-hosted, Zapier for business users, 8,000+ connectors.'],
    [null, 'O', 'OpenClaw', 'open source', 'DIY personal agent run from WhatsApp/Telegram — and 2026’s security cautionary tale. Not for corporate use; its lessons come in Part 5.'],
  ];
  gallery.forEach((g, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.6 + Math.floor(i / 2) * 1.28;
    H.card(s, x, y, 5.95, 1.16, i === 7 ? C.AMBER_TINT : C.PANEL);
    if (i === 7) H.iconCircle(s, x + 0.18, y + 0.32, 0.5, 'alert', C.AMBER);
    else H.logo(s, x + 0.18, y + 0.32, 0.5, g[0], g[1]);
    s.addText([
      { text: g[2] + '  ', options: { bold: true, color: C.INK, fontSize: 12 } },
      { text: g[3], options: { color: C.MUTE, fontSize: 9, breakLine: true, paraSpaceAfter: 2 } },
      { text: g[4], options: { color: C.SLATE, fontSize: 9.2 } },
    ], { x: x + 0.8, y: y + 0.06, w: 5.0, h: 1.05, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.0 });
  });
  s.addText('Coding IDEs (Cursor · GitHub Copilot · Devin) and browser agents (Comet · Claude in Chrome) exist too — engineering and power-user tools; ask IT before either.', { x: 0.55, y: 6.75, w: 12.2, h: 0.35, fontFace: F.body, fontSize: 9.5, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    '[REFRESH QUARTERLY — owner: Oscar]\n' +
    '\n' +
    'HOW TO PRESENT —\n' +
    '1) Frame: “eight doers — agents that run jobs. One line each; two get a story.”\n' +
    '2) Story 1 — Claude Code: “this very training’s materials were built with it.”\n' +
    '3) Story 2 — Manus, plainly: an agent so famous Meta bought it for two billion dollars — and the Chinese government forced the deal to be unwound; it now runs independently from Singapore. That whole saga is a one-line governance lesson: know who owns your tools.\n' +
    '4) End on the amber OpenClaw card: 2026’s security cautionary tale — don’t tell the whole story now; its lessons return in Part 5’s guardrails.\n' +
    '5) Footer: IDEs and browser agents exist — engineering/power-user territory, and browser agents are injection-prone (treat every page as untrusted input).\n' +
    '\n' +
    'BRIDGE —\n' +
    '“Agents that DO. Now the specialists that MAKE — next slide.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'IDE = Integrated Development Environment — a programmer’s editor.\n' +
    'DIY = do-it-yourself. n8n / Zapier = product names (not acronyms).\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: brand logos on cards (assets/logos/); Manus saga dates now on the card (audit L13).\n' +
    'Evidence per tool: notes/research/r12_tool_landscape.md.\n' +
    'Manus: Meta acquisition ~$2B Dec 2025; Beijing (NDRC) ordered unwind Apr 2026; independent Singapore company Aug 2026; desktop “My Computer” mode Mar 2026.\n' +
    'Notion: Custom Agents (Feb 2026) run on triggers with scoped permissions; Business/Enterprise plans; usage billed in credits.\n' +
    'OpenClaw: maintainer’s own warning, verbatim — “if you can’t run a command line, this is far too dangerous to use safely”; CVE-2026-25253 (1-click RCE); a malicious #1-ranked community skill (Cisco).');

  // ---------- 20. SPECIALIST SHELF — THE MAKERS ----------
  s = H.slide('PART 2 · AGENTIC TOOLS', 20);
  H.title(s, 'The specialist shelf · the makers', 'One great tool per job — September 2026');
  const shelf = [
    ['google', 'G', 'Gemini Notebook (was NotebookLM)', 'Google', 'Upload YOUR documents, get cited answers, audio overviews, mind maps. Grounded in your sources = low hallucination. The most useful new tool for this room.'],
    [null, null, 'Meeting notes', 'Teams / Zoom native · Granola', 'Check your native tool first (IT-sanctioned). Granola is the bot-free best-in-class — but recording consent policy applies either way.'],
    ['gamma', 'G', 'Decks & design', 'Gamma · Canva AI', 'Gamma: a full deck from a prompt (70M users). Canva: the design suite marketing already licenses, now with conversational AI.'],
    ['adobe', 'A', 'Images — the safe lane', 'Adobe Firefly', 'Trained only on licensed content; paid plans include legal indemnification — the corporate pick. ChatGPT Images 2.0 / Nano Banana 2 are already in your chatbot for internal drafts.'],
    ['lovable', 'L', 'Apps without code', 'Lovable', 'Describe an app in plain language → working web app with database and login (Adidas, NVIDIA use it). Security review before real company data.'],
    ['deepl', 'D', 'Voice & language', 'ElevenLabs · DeepL', 'ElevenLabs: narrated training modules, dubbing (consent rules for voice cloning). DeepL: real-time spoken translation + document-grade language work.'],
    ['gemini', 'V', 'Video', 'Veo 3.1 (in Google tools)', 'Good enough for internal video today. Cautionary tale: OpenAI’s famous Sora app was shut down (Apr 2026) — never build a process on a consumer app.'],
    [null, null, 'Find more, forever', 'your own assistant', 'Tools change monthly. Ask your approved AI: “Search the web: what are the best current tools for [my task], and which are enterprise-safe?” That answer never goes stale.'],
  ];
  shelf.forEach((g, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.6 + Math.floor(i / 2) * 1.24;
    H.card(s, x, y, 5.95, 1.12, i === 7 ? C.TEAL_TINT : C.PANEL);
    if (g[0] === null) H.iconCircle(s, x + 0.18, y + 0.3, 0.5, i === 1 ? 'mic' : 'search', C.TEAL);
    else H.logo(s, x + 0.18, y + 0.3, 0.5, g[0], g[1]);
    s.addText([
      { text: g[2] + '  ', options: { bold: true, color: C.INK, fontSize: 11.5 } },
      { text: g[3], options: { color: C.MUTE, fontSize: 8.8, breakLine: true, paraSpaceAfter: 2 } },
      { text: g[4], options: { color: C.SLATE, fontSize: 9 } },
    ], { x: x + 0.8, y: y + 0.05, w: 5.0, h: 1.02, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.0 });
  });
  H.callout(s, 0.55, 6.6, 12.2, 0.52, C.AMBER_TINT, [
    { text: 'Standing rule: ', options: { bold: true, color: C.INK, fontSize: 10.5 } },
    { text: 'your organization’s AI policy and approved-tool list outrank every name on these two slides.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'shield', iconFill: C.AMBER, size: 10.5 });
  s.addNotes(
    '[REFRESH QUARTERLY — owner: Oscar]\n' +
    '\n' +
    'HOW TO PRESENT —\n' +
    '1) Frame: “the makers — one great tool per job. Sweep, don’t dwell: this slide is a reference card.”\n' +
    '2) Slow on two: Gemini Notebook (say the rename out loud — it was NotebookLM until July 2026, people know the old name; grounded in YOUR documents = the anti-hallucination tool) and Firefly (trained only on licensed content, and paid plans include legal indemnification — the one your legal team will like).\n' +
    '3) The Sora line, plainly: a world-famous video app, shut down in April 2026 — the lesson is never to build a business process on a consumer app.\n' +
    '4) Teal card (bottom right): the find-more move — don’t bookmark tool lists; ask your own assistant, fresh, when you need one.\n' +
    '5) Amber band VERBATIM: org policy and the approved-tool list outrank everything here.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“That’s the landscape. Part 3 — the craft itself.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'none needing expansion on this slide (product names throughout).\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.6: brand logos on cards; Firefly indemnification scoped to paid plans (audit L9); Sora line carries the date and no duration claim (audit M1/L21).\n' +
    'Evidence per tool in notes/research/r12_tool_landscape.md, incl.: NotebookLM→Gemini Notebook rename (Jul 16, 2026); Granola $1.5B valuation (Mar 2026) + the consent caveat; Gamma $100M ARR/70M users (Nov 2025); Firefly licensed-training + paid-plan indemnification (Adobe business terms); Lovable enterprise users; DeepL Voice-to-Voice (Apr 2026); Sora app shutdown (Apr 2026).\n' +
    'Deliberately NOT on the slide: Stable Diffusion (open-source image generation — now an IT/developer tool: local installs, no indemnification; say “the open-source option IT might run privately” if asked) and Midjourney (artists’ favorite; active studio copyright litigation — legal-risk caveat).\n' +
    'If someone wants a directory anyway: There’s An AI For That — browse by task, verify with IT before use.');
};
