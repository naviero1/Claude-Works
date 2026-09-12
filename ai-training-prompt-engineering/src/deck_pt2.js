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
    ['openai', 'ChatGPT', 'OpenAI · GPT-5.6 (Sol / Terra / Luna)', 'The everything assistant', 'Largest user base; fastest at drafts, options and marketing copy; images, voice, agent mode.', 'Fast model churn and renaming; check data settings before regulated content.'],
    ['gemini', 'Gemini', 'Google · Gemini 3 / 3.1 Pro / 3.6 Flash', 'Everywhere Google is', 'Multimodal breadth + the deepest Workspace integration — 1B+ monthly users; default AI in Gmail, Docs, Meet.', 'Model-name sprawl; the best reasoning (Deep Think) sits behind the Ultra tier.'],
    ['copilot', 'Copilot', 'Microsoft · GPT-5.6 + Claude selectable', 'The governed one — inside your tenant', '30M+ paid seats inside the M365 compliance boundary IT already audits; its Cowork agent runs on Claude technology.', 'Licenses others’ models; admin flags mean colleagues get different capabilities.'],
    ['claude', 'Claude', 'Anthropic · Fable/Opus/Sonnet 5 + Haiku', 'Best-in-class coding & agentic work', 'Tops SWE-bench AND OpenAI’s own real-work eval (GDPval); 2026 writing evals rank its prose #1; 1M-token documents.', 'Premium pricing at the top; the flagship can refuse high-risk domains by design.'],
    ['perplexity', 'Perplexity', 'Perplexity · own stack + Model Council', 'Research with receipts', 'Inline citations by default; the lowest citation-error rate in CJR’s AI-search testing — 37%, vs 67% for ChatGPT Search.', 'A citation isn’t proof — click through before quoting anywhere formal.'],
    ['grok', 'Grok', 'xAI (SpaceX) · Grok 4.6', 'Blunt on purpose', '“Unhinged” is a literal voice mode; real-time X data; aggressive price-performance.', 'Fewer guardrails, real incidents (Jul 2025 apology) — mind brand-sensitive work.'],
  ];
  vendors.forEach((v, i) => {
    const x = 0.55 + (i % 3) * 4.18;
    const y = 1.58 + Math.floor(i / 3) * 2.56;
    H.card(s, x, y, 3.95, 2.42, C.PANEL);
    s.addShape('roundRect', { x, y, w: 3.95, h: 0.62, rectRadius: 0.06, fill: { color: 'FFFFFF' }, line: { color: C.LINE, width: 0.75 } });
    H.logo(s, x + 0.14, y + 0.11, 0.4, v[0], v[1][0]);
    s.addText(v[1], { x: x + 0.64, y: y + 0.05, w: 2.1, h: 0.34, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
    s.addText(v[2], { x: x + 0.64, y: y + 0.36, w: 3.26, h: 0.24, fontFace: F.body, fontSize: 9, bold: true, charSpacing: 0.3, color: C.MUTE, margin: 0 });
    s.addText(v[3], { x: x + 0.2, y: y + 0.7, w: 3.55, h: 0.52, fontFace: F.head, fontSize: 13.5, bold: true, color: C.TEAL_DARK, margin: 0, lineSpacingMultiple: 0.96 });
    s.addText(v[4], { x: x + 0.2, y: y + 1.24, w: 3.58, h: 0.76, fontFace: F.body, fontSize: 11, color: C.SLATE, margin: 0, lineSpacingMultiple: 0.98 });
    s.addText(v[5], { x: x + 0.2, y: y + 2.02, w: 3.58, h: 0.38, fontFace: F.body, fontSize: 10.5, italic: true, color: C.AMBER, margin: 0, lineSpacingMultiple: 0.92 });
  });
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
    'v1.12 (owner edits, ported): evidence lines enlarged (his 14pt did not fit the fixed cards — set to the max that does, 11pt; caveats 10.5) and the “Fortes verified Sep 9, 2026 — they will move” footer removed from the slide: say it from point 5 instead.\n' +
    'v1.6: rebuilt as identity trading cards (assertion-evidence layout, r19) with real product logos; Perplexity’s known-for now leads with the CJR error-rate comparison (the ~94%-with-citations figure was less meaningful — audit H3).\n' +
    'Every claim evidence-backed in notes/research/r13_reputations_r1.md:\n' +
    'Writing: owner’s hunch was “ChatGPT writes better” — 2026 evals say otherwise (LMArena creative-writing June 2026: Anthropic six of top ten, #1; EQ-Bench Aug 2026 agrees). ChatGPT’s honest forte is speed, options, marketing copy.\n' +
    'Claude: SWE-bench ~96% (Sept 2026); GDPval winner (OpenAI’s own eval, Sept 2025); GDPval-AA v2 leader Sept 2026.\n' +
    'Copilot: 30M+ paid seats (Microsoft FY26 Q4, Jul 2026); Copilot Cowork licenses Claude Cowork technology (Mar 2026).\n' +
    'Vendor benchmark numbers are marketing until independently reproduced — read them as claims.\n' +
    'Grok note: xAI was acquired by SpaceX (Feb 2026).\n' +
    'Logos: official site favicons (assets/logos/) — referential brand use inside an internal training deck.\n' +
    'USAGE KEEPERS (from the cut “What people actually use” slide; all sourced in r24, mid-2026 — speak if useful): 52% of US employees use AI at work, 15% daily (Gallup May ’26) · top jobs writing 51% / research 49% · 86% treat AI output as a FIRST DRAFT, not a final product (Microsoft WTI 2026) · usage ≠ preference — people default to whatever is inside Gmail/Office/WhatsApp · STANDING RULE, always said aloud: your organization’s AI policy and approved-tool list outrank every name in this part.\n' +
    'R14 type pass: sub-labels trimmed to fit 9pt — Perplexity’s Model Council = GPT+Claude+Gemini; footer teaser (“whose servers? two slides ahead — the account tier decides, not the logo”) now spoken from point 5, not printed.');

  // ---------- 17. THE DEEPSEEK MOMENT ----------
  s = H.slide('PART 2 · THE CHINESE WAVE', 17);
  H.title(s, 'The DeepSeek moment', 'January 2025: frontier ability, ~27× cheaper');
  H.card(s, 0.55, 1.58, 5.6, 1.62, C.PANEL);
  H.logo(s, 0.8, 1.72, 0.36, 'deepseek', 'D');
  s.addText('What happened, in three facts', { x: 1.26, y: 1.72, w: 4.7, h: 0.32, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.85, 2.08, 5.05, 1.1, [
    { t: 'DeepSeek-R1: open-weights reasoning rivaling OpenAI’s o1 — MIT-licensed, free' },
    { t: 'Nvidia lost $589B in one day (Jan 27) — then the largest single-day market loss ever' },
    { t: '“$5.6M training cost”? Fuel for the final race — not the racing team. Real efficiency, oversold headline.', b: true },
  ], { size: 10, gap: 3 });
  H.card(s, 0.55, 3.3, 5.6, 2.52, C.TEAL_TINT);
  s.addText('The trick has a name: MoE — Mixture of Experts', { x: 0.82, y: 3.44, w: 5.1, h: 0.32, fontFace: F.head, fontSize: 13, bold: true, color: C.TEAL_DARK, margin: 0 });
  // — the specialist hospital (owner-generated illustration, v1.8) —
  s.addImage({ path: require('path').join(__dirname, 'assets', 'images', 'hospital_night.jpg'), x: 0.9, y: 3.86, w: 1.55, h: 1.9, sizing: { type: 'cover', w: 1.55, h: 1.9 } });
  s.addShape('roundRect', { x: 0.9, y: 3.86, w: 1.55, h: 1.9, rectRadius: 0.05, fill: { type: 'none' }, line: { color: C.TEAL_DARK, width: 1.25 } });
  s.addText('Built like a huge specialist hospital at night: 671 billion parameters on the books, but only ~37 billion — the lit windows, the relevant departments — wake up per question. You pay for the specialists consulted, not the whole building. Distillation (big models teaching small ones) finishes the job.', { x: 2.62, y: 3.86, w: 3.38, h: 1.9, fontFace: F.body, fontSize: 10.5, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.08 });
  // — the bill, hero —
  H.card(s, 6.35, 1.58, 6.4, 2.15, C.PANEL);
  s.addText('The bill, per million output tokens', { x: 6.62, y: 1.72, w: 5.9, h: 0.32, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
  s.addText('OpenAI o1', { x: 6.62, y: 2.14, w: 1.35, h: 0.3, fontFace: F.body, fontSize: 10, color: C.SLATE, margin: 0, valign: 'middle' });
  s.addShape('roundRect', { x: 8.05, y: 2.16, w: 3.3, h: 0.26, rectRadius: 0.04, fill: { color: C.SLATE }, line: { type: 'none' } });
  s.addText('$60', { x: 8.05, y: 2.14, w: 3.25, h: 0.3, align: 'right', valign: 'middle', fontFace: F.head, fontSize: 12, bold: true, color: 'FFFFFF', margin: 0 });
  s.addText('DeepSeek-R1', { x: 6.62, y: 2.56, w: 1.35, h: 0.3, fontFace: F.body, fontSize: 10, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
  s.addShape('roundRect', { x: 8.05, y: 2.58, w: 0.14, h: 0.26, rectRadius: 0.02, fill: { color: C.TEAL }, line: { type: 'none' } });
  s.addText('$2.19', { x: 8.24, y: 2.44, w: 1.6, h: 0.52, fontFace: F.head, fontSize: 24, bold: true, color: C.TEAL, margin: 0, valign: 'middle' });
  s.addShape('ellipse', { x: 11.55, y: 2.08, w: 1.0, h: 1.0, fill: { color: C.AMBER }, line: { type: 'none' } });
  s.addText([
    { text: '27×', options: { fontSize: 19, bold: true, breakLine: true } },
    { text: 'cheaper', options: { fontSize: 8.5, bold: true } },
  ], { x: 11.55, y: 2.08, w: 1.0, h: 1.0, align: 'center', valign: 'middle', fontFace: F.head, color: 'FFFFFF', margin: 0, lineSpacingMultiple: 0.9 });
  s.addText('A $100 o1 workload cost ~$3.60 on R1 — this is why the thinking and deep-research modes from Part 1 didn’t stay luxury-priced.', { x: 6.62, y: 3.14, w: 4.8, h: 0.55, fontFace: F.body, fontSize: 10.5, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.03 });
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
    s.addText(b[0], { x: 6.62, y, w: 2.35, h: 0.32, fontFace: F.body, fontSize: 10, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.95 });
    const barMax = 2.5;
    s.addShape('roundRect', { x: 9.05, y: y + 0.03, w: barMax * (b[1] / 100), h: 0.11, rectRadius: 0.02, fill: { color: C.TEAL }, line: { type: 'none' } });
    s.addText(String(b[1]), { x: 9.08 + barMax * (b[1] / 100), y: y - 0.02, w: 0.5, h: 0.2, fontFace: F.body, fontSize: 8.5, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addShape('roundRect', { x: 9.05, y: y + 0.17, w: barMax * (b[2] / 100), h: 0.11, rectRadius: 0.02, fill: { color: C.SLATE }, line: { type: 'none' } });
    s.addText(String(b[2]), { x: 9.08 + barMax * (b[2] / 100), y: y + 0.12, w: 0.5, h: 0.2, fontFace: F.body, fontSize: 8.5, color: C.SLATE, margin: 0, valign: 'middle' });
  });
  s.addText([
    { text: '■', options: { color: C.TEAL, fontSize: 9, bold: true } }, { text: ' DeepSeek-R1  ', options: { color: C.SLATE, fontSize: 9 } },
    { text: '■', options: { color: C.SLATE, fontSize: 9, bold: true } }, { text: ' OpenAI o1 — matched on math & coding, behind on PhD science: not a clean sweep.', options: { color: C.MUTE, fontSize: 9 } },
  ], { x: 6.62, y: 5.32, w: 5.9, h: 0.34, fontFace: F.body, margin: 0 });
  H.promptChip(s, 0.55, 5.7, 12.2, 1.38, 7, [
    { type: '“Explain Mixture of Experts like a colleague: a specialist hospital where only the relevant departments wake up per question — and why that made AI dramatically cheaper in 2025. Under 120 words.”', why: 'the MoE cheat-note lands in your course log.' },
  ], { label: 'The specialist hospital, explained', size: 10, tab: 'EX7-MoE' });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Anchor the moment, LEFT top card: January 2025 — an open model rivals o1; Nvidia’s $589B day; and keep the cost claim honest — the famous $5.6M is the fuel bill for the final winning race, not the cost of the racing team (total hardware spend was estimated well over $500M).\n' +
    '2) LEFT teal card — POINT AT THE HOSPITAL IMAGE: the whole building is 671 billion parameters; the three lit windows are the ~37 billion that wake up for your question. You pay for the specialists consulted, not the whole building. Distillation = big models teaching small ones.\n' +
    '3) RIGHT top — the star of the slide: $60 against $2.19, and the bars are TRUE proportion (the R1 bar really is 27× shorter). A $100 o1 workload for $3.60.\n' +
    '4) RIGHT bottom: three benchmark pairs — matched on math and coding, behind on PhD science (be honest: not a clean sweep).\n' +
    '5) Close the loop to Part 1: THIS is why thinking modes and deep research became affordable for everyone.\n' +
    '\n' +
    'TRY IT — PROMPT 7/7 (copy from tab EX7-MoE)\n' +
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
    'v1.8 ART — the drawn hospital is replaced by the owner-generated night-hospital illustration (R16): three windows lit, exactly the ~37B-of-671B story. Point at the lit windows.\n' +
    'Chart data verified against the R1 paper (arXiv:2501.12948) — see notes/research/r13_reputations_r1.md.\n' +
    'Pricing: R1 $0.55/$2.19 vs o1 $15/$60 per M tokens (Jan 2025) = 27.3–27.4×.\n' +
    'Since then (if asked): DeepSeek stayed the open-weight value leader but slipped off the leading edge — NIST’s CAISI evaluation (May 2026) put it ~8 months behind the frontier.\n' +
    'What the wave brought beyond DeepSeek (spoken if useful): open weights with permissive licenses to self-host (Qwen the most-downloaded family; famously self-hosted by Airbnb) · price pressure that pushed OpenAI to ship its first open-weight models since GPT-2 (gpt-oss, Aug 2025) · trillion-parameter open agentic models (Kimi).\n' +
    'US–China top-model gap: ~3% (Stanford AI Index 2026), down from 18–32 points in 2023.');

  // ---------- 18. SERVERS — THE GEOGRAPHY (v1.7: matrix removed at owner request) ----------
  s = H.slide('PART 2 · TRUST & DATA', 18);
  H.title(s, 'Where your words go', 'Whose servers, in which country — Sep 2026');
  // — owner-generated world-map backdrop (R16; src/assets/images/map_world.jpg) —
  s.addImage({ path: require('path').join(__dirname, 'assets', 'images', 'map_world.jpg'), x: 0.55, y: 1.58, w: 12.2, h: 4.15, sizing: { type: 'cover', w: 12.2, h: 4.15 } });
  s.addShape('roundRect', { x: 0.55, y: 1.58, w: 12.2, h: 4.15, rectRadius: 0.02, fill: { type: 'none' }, line: { color: C.LINE, width: 1 } });
  const regions = [
    ['UNITED STATES', C.TEAL_DARK, 0.85, [
      ['claude', 'Anthropic', 'stored in the US'],
      ['openai', 'OpenAI', 'US by default'],
      ['grok', 'xAI', 'own Memphis data centers'],
      ['perplexity', 'Perplexity', 'AWS cloud, worldwide'],
    ]],
    ['EUROPE — residency on business tiers', C.TEAL_DARK, 4.85, [
      ['openai', 'OpenAI', 'EU residency (2025) + in-region processing (2026)'],
      ['microsoft', 'Microsoft', 'EU Data Boundary — Claude-in-Copilot sits outside it'],
      ['google', 'Google', 'enterprise residency by region'],
      ['claude', 'Anthropic', 'EU via cloud partners (Bedrock · Vertex · Foundry)'],
    ]],
    ['CHINA & ASIA', C.RED, 8.85, [
      ['deepseek', 'DeepSeek', '“stored in the People’s Republic of China” — its own policy'],
      ['kimi', 'Kimi (Moonshot)', 'PRC storage'],
      [null, 'Z.ai (Zhipu)', 'Singapore processing · US Entity-List parent'],
    ]],
  ];
  regions.forEach(rg => {
    const x = rg[2];
    s.addShape('roundRect', { x, y: 1.82, w: 3.72, h: 3.7, rectRadius: 0.08, fill: { color: 'FFFFFF' }, line: { color: rg[1], width: 1, dashType: 'dash' } });
    s.addText(rg[0], { x: x + 0.18, y: 1.94, w: 3.4, h: 0.3, fontFace: F.body, fontSize: 10.5, bold: true, charSpacing: 0.8, color: rg[1], margin: 0 });
    rg[3].forEach((r, i) => {
      const y = 2.36 + i * 0.79;
      H.logo(s, x + 0.18, y + 0.02, 0.36, r[0], r[1][0]);
      s.addText([
        { text: r[1], options: { bold: true, color: C.INK, fontSize: 10.5, breakLine: true } },
        { text: r[2], options: { color: C.SLATE, fontSize: 10.5 } },
      ], { x: x + 0.64, y, w: 3.0, h: 0.76, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 0.98 });
    });
  });
  H.card(s, 0.55, 5.95, 6.0, 1.15, C.TEAL_TINT);
  s.addText([
    { text: 'Residency = choosing where it lives. ', options: { bold: true, color: C.TEAL_DARK, fontSize: 12, breakLine: true } },
    { text: 'An enterprise feature: the same vendor can host your company tenant in the EU while its consumer app stores chats in the US.', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 0.85, y: 6.06, w: 5.5, h: 0.95, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.05 });
  H.card(s, 6.75, 5.95, 6.0, 1.15, C.AMBER_TINT);
  s.addText([
    { text: 'The one question that settles it: ', options: { bold: true, color: C.INK, fontSize: 12, breakLine: true } },
    { text: 'ask IT which region and tier YOUR account runs on — your organization’s AI policy has the answer for everything else.', options: { color: C.SLATE, fontSize: 11 } },
  ], { x: 7.05, y: 6.06, w: 5.5, h: 0.95, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.05 });
  s.addNotes(
    '[REFRESH QUARTERLY — owner: Oscar]\n' +
    '\n' +
    'HOW TO PRESENT —\n' +
    '1) Frame: “one geography question — whose servers, in which country — and one account question. That’s the whole trust topic at our level.”\n' +
    '2) Walk the three region panels LEFT TO RIGHT. US: where the consumer apps live by default. EUROPE: the residency panel — these are BUSINESS-TIER features; slow on Microsoft (EU Data Boundary — but the Claude models inside Copilot sit OUTSIDE it; your IT team cares). CHINA & ASIA: read DeepSeek’s line verbatim — its own privacy policy says data is “stored in the People’s Republic of China”; Italy blocked the app over it (Jan 2025, not lifted).\n' +
    '3) The italic map line: SAME LOGO, DIFFERENT HOMES — the account tier decides which one yours is. That is the entire lesson.\n' +
    '4) Teal card: residency, defined once.\n' +
    '5) Amber card: the handoff — which region and tier YOUR account runs on is an IT question; the org’s AI policy answers everything else. (Deliberately NOT on this slide: any what-data-goes-where guidance — that is company policy’s territory, not this training’s.)\n' +
    '6) The restaurant-vs-cookbook aside if China comes up: using the app is eating at their restaurant (they see your order); downloaded open-weight MODELS are a cookbook IT can cook from at home — the app, not the model, is the risk.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“That’s the landscape. Part 3 — the craft itself.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'PRC = People’s Republic of China. EU Data Boundary = Microsoft’s commitment to process EU data inside the EU.\n' +
    'AWS = Amazon Web Services. Entity List = the US federal trade-restriction list — a procurement red flag.\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.12 (owner edits, ported): the centered “same logo, different homes — the ACCOUNT TIER decides” line was removed from the slide — say it aloud instead when sweeping the panels; it remains the slide’s one-line lesson.\n' +
    'v1.7: rebuilt as the server-geography map (owner: focus on where servers are; no data-type guidance — that belongs to company policy). Swap the schematic band for the owner’s generated world-map backdrop when it lands in notes/intake/ (R16).\n' +
    'Presenter background (kept OFF-slide by design, from r11, researched Sep 9 2026): the major Western vendors train on CONSUMER chats by default and none train on enterprise-tier data · the famous 2025 leaks were all personal-account: ~300K+ Grok chats indexed by Google; “deleted” ChatGPT chats preserved for court (enterprise excluded) · Google consumer: reviewed chats kept up to 3 yrs · Kimi PRC storage; Z.ai Singapore processing, Entity-List parent · EchoLeak (CVE-2025-32711, Jun 2025): even enterprise Copilot had a zero-click exfiltration hole — patched.\n' +
    'Defaults drift (Anthropic flipped consumer training Aug 2025; Microsoft Oct 2024) — re-verify quarterly.\n' +
    'Standing rule, always said aloud: your organization’s AI policy and approved-tool list outrank everything on this slide.');

};
