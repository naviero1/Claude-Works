// PART 2 — Models & tools landscape (v1.5, verified Sep 9, 2026)
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

  // ---------- 16. ASSISTANT LANDSCAPE ----------
  s = H.slide('PART 2 · THE ASSISTANTS', 16);
  H.title(s, 'The assistants', 'Six names — and what each is genuinely known for');
  const vendors = [
    ['Claude', 'Anthropic · Fable 5 / Opus 5 / Sonnet 5 / Haiku 4.5', 'Known for: best-in-class coding & agentic work — tops SWE-bench AND OpenAI’s own real-work eval (GDPval); 1M-token documents; 2026 writing evals rank it #1 for careful prose.', 'Caveat: premium pricing at the top tier; flagship can refuse high-risk domains by design.'],
    ['ChatGPT', 'OpenAI · GPT-5.6 family (Sol / Terra / Luna)', 'Known for: the everything assistant — fastest at drafts, options and marketing copy; largest user base; images, voice, agent mode.', 'Caveat: fast model churn and renaming; check data settings before regulated content.'],
    ['Gemini', 'Google · Gemini 3 / 3.1 Pro / 3.6 Flash + Deep Think', 'Known for: multimodal breadth (video, images, audio) and the deepest Workspace integration — 1B+ monthly users; default AI in Gmail/Docs/Meet.', 'Caveat: model-name sprawl; best reasoning sits behind the Ultra tier.'],
    ['Copilot', 'Microsoft · GPT-5.6 preferred + Claude selectable', 'Known for: ubiquity and governance — 30M+ paid seats inside the M365 compliance boundary IT already audits. Its Cowork agent runs on Claude technology.', 'Caveat: licenses others’ models; admin flags mean colleagues get different capabilities.'],
    ['Perplexity', 'Perplexity · own stack + Model Council (GPT+Claude+Gemini)', 'Known for: research with receipts — ~94% of answers carry inline citations; lowest citation-error rate in CJR’s AI-search testing; Comet browser.', 'Caveat: a citation isn’t proof — click through before quoting anywhere formal.'],
    ['Grok', 'xAI (SpaceX) · Grok 4.6', 'Known for: blunt on purpose — “Unhinged” is a literal voice mode; real-time X data; aggressive price-performance.', 'Caveat: fewer guardrails has meant real incidents (Jul 2025 public apology) — care for brand-sensitive work.'],
  ];
  vendors.forEach((v, i) => {
    const x = 0.55 + (i % 3) * 4.18;
    const y = 1.62 + Math.floor(i / 3) * 2.5;
    H.card(s, x, y, 3.95, 2.32, C.PANEL);
    s.addText(v[0], { x: x + 0.24, y: y + 0.12, w: 3.4, h: 0.36, fontFace: F.head, fontSize: 15.5, bold: true, color: C.TEAL_DARK, margin: 0 });
    s.addText(v[1], { x: x + 0.24, y: y + 0.48, w: 3.5, h: 0.3, fontFace: F.body, fontSize: 8.2, bold: true, charSpacing: 0.4, color: C.MUTE, margin: 0 });
    s.addText(v[2], { x: x + 0.24, y: y + 0.82, w: 3.5, h: 0.95, fontFace: F.body, fontSize: 9.2, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.02 });
    s.addText(v[3], { x: x + 0.24, y: y + 1.78, w: 3.5, h: 0.5, fontFace: F.body, fontSize: 8.4, italic: true, color: C.AMBER, margin: 0, lineSpacingMultiple: 0.98 });
  });
  s.addText('Which of these can see company data? Two slides ahead — trust is about the account tier, not the logo. Names and fortes verified Sep 9, 2026 — they will have moved; the habits in Parts 3–5 don’t move at all.', { x: 0.55, y: 6.68, w: 12.2, h: 0.4, fontFace: F.body, fontSize: 10, italic: true, color: C.MUTE, margin: 0, lineSpacingMultiple: 1.02 });
  s.addNotes(
    '[REFRESH QUARTERLY — owner: Oscar]\n' +
    '\n' +
    'HOW TO PRESENT —\n' +
    '1) Frame: “six names cover the chat landscape — and each is genuinely known for something different.”\n' +
    '2) Walk the cards in reading order — Claude → ChatGPT → Gemini (top row), Copilot → Perplexity → Grok (bottom row) — ONE known-for line each; let the amber caveats be read, not spoken.\n' +
    '3) On Grok, say the plain version: “Unhinged” is not a nickname — it is an actual personality setting in its voice app, by that name; and in July 2025 a bad update had it praising Hitler for sixteen hours before an apology. That is the trade-off of a deliberately less-filtered assistant.\n' +
    '4) On Copilot, land the licensing fact: Microsoft’s Cowork agent runs on Claude technology — the tiers matter more than the brand wars.\n' +
    '5) Footer: the trust question is TWO SLIDES AHEAD; names verified Sep 9, 2026 and they WILL move.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“One force reshaped this list — the Chinese open-weight wave.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'SWE-bench = Software Engineering benchmark — the standard test of coding-agent ability.\n' +
    'GDPval = OpenAI’s benchmark of real knowledge-work tasks across 44 occupations.\n' +
    'CJR = Columbia Journalism Review (its Tow Center tested AI search citation accuracy).\n' +
    'X = the social platform (Grok’s data source).\n' +
    '\n' +
    'CONTENT —\n' +
    'v1.5 “known for” layer — every claim evidence-backed in notes/research/r13_reputations_r1.md:\n' +
    'Writing: owner’s hunch was “ChatGPT writes better” — 2026 evals say otherwise (LMArena creative-writing June 2026: Anthropic six of top ten, #1; EQ-Bench Aug 2026 agrees). ChatGPT’s honest forte is speed, options, marketing copy.\n' +
    'Claude: SWE-bench ~96% (Sept 2026); GDPval winner (OpenAI’s own eval, Sept 2025); GDPval-AA v2 leader Sept 2026.\n' +
    'Copilot: 30M+ paid seats (Microsoft FY26 Q4, Jul 2026); Copilot Cowork licenses Claude Cowork technology (Mar 2026).\n' +
    'Perplexity: ~94% answers with inline citations; CJR/Tow lowest citation-error rate (37% vs 67% ChatGPT Search).\n' +
    'Vendor benchmark numbers are marketing until independently reproduced — read them as claims.\n' +
    'Grok note: xAI was acquired by SpaceX (Feb 2026).');

  // ---------- 17. THE DEEPSEEK MOMENT ----------
  s = H.slide('PART 2 · THE CHINESE WAVE', 17);
  H.title(s, 'The DeepSeek moment', 'January 2025: frontier ability, ~27× cheaper');
  H.card(s, 0.55, 1.62, 5.4, 1.78, C.PANEL);
  s.addText('What happened, in three facts', { x: 0.82, y: 1.78, w: 4.9, h: 0.32, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.87, 2.16, 4.85, 1.2, [
    { t: 'DeepSeek-R1: open-weights reasoning rivaling OpenAI’s o1 — MIT-licensed, free to download' },
    { t: 'Nvidia lost $589B in one day (Jan 27) — the largest single-day loss in market history at the time' },
    { t: 'The “$5.6M training cost”? The fuel for the final winning race — not the racing team. Real efficiency, oversold headline.', b: true },
  ], { size: 9.6, gap: 4 });
  H.card(s, 0.55, 3.52, 5.4, 1.95, C.TEAL_TINT);
  s.addText('The trick has a name: MoE — Mixture of Experts', { x: 0.82, y: 3.68, w: 4.9, h: 0.32, fontFace: F.head, fontSize: 13, bold: true, color: C.TEAL_DARK, margin: 0 });
  s.addText('The model is built like a huge specialist hospital: 671 billion parameters on the books, but only ~37 billion — the relevant departments — wake up for any one question. You pay for the specialists consulted, not the whole building. Add distillation (big models teaching small ones) and frontier ability stops being luxury-priced.', { x: 0.85, y: 4.04, w: 4.85, h: 1.35, fontFace: F.body, fontSize: 10.2, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.08 });
  H.card(s, 6.15, 1.62, 6.6, 3.85, C.PANEL);
  s.addText('R1 vs o1 — matched on most, ~27× cheaper', { x: 6.42, y: 1.78, w: 6.1, h: 0.32, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
  const bench = [
    ['Math olympiad (AIME 2024)', 79.8, 79.2],
    ['MATH-500', 97.3, 96.4],
    ['Coding agent (SWE-bench)', 49.2, 48.9],
    ['Science PhD (GPQA)', 71.5, 75.7],
    ['Codeforces (percentile)', 96.3, 96.6],
  ];
  bench.forEach((b, i) => {
    const y = 2.22 + i * 0.56;
    s.addText(b[0], { x: 6.42, y, w: 2.5, h: 0.5, fontFace: F.body, fontSize: 9, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.95 });
    const barMax = 2.55;
    s.addShape('roundRect', { x: 9.0, y: y + 0.03, w: barMax * (b[1] / 100), h: 0.18, rectRadius: 0.03, fill: { color: C.TEAL }, line: { type: 'none' } });
    s.addText(String(b[1]), { x: 9.02 + barMax * (b[1] / 100), y: y - 0.01, w: 0.55, h: 0.24, fontFace: F.body, fontSize: 8, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addShape('roundRect', { x: 9.0, y: y + 0.25, w: barMax * (b[2] / 100), h: 0.18, rectRadius: 0.03, fill: { color: C.SLATE }, line: { type: 'none' } });
    s.addText(String(b[2]), { x: 9.02 + barMax * (b[2] / 100), y: y + 0.21, w: 0.55, h: 0.24, fontFace: F.body, fontSize: 8, color: C.SLATE, margin: 0, valign: 'middle' });
  });
  s.addText([
    { text: '■', options: { color: C.TEAL, fontSize: 8.5, bold: true } }, { text: ' DeepSeek-R1  ', options: { color: C.SLATE, fontSize: 8 } },
    { text: '■', options: { color: C.SLATE, fontSize: 8.5, bold: true } }, { text: ' OpenAI o1 · Codeforces = human percentile · R1 paper, Jan 2025', options: { color: C.MUTE, fontSize: 8 } },
  ], { x: 6.42, y: 5.04, w: 6.1, h: 0.24, fontFace: F.body, margin: 0 });
  s.addText([
    { text: 'The bill: ', options: { bold: true, color: C.AMBER, fontSize: 10.5 } },
    { text: '$2.19 vs $60 per million output tokens — a $100 o1 workload cost ~$3.60 on R1. This is why the thinking and deep-research modes from Part 1 didn’t stay luxury-priced.', options: { color: C.SLATE, fontSize: 10 } },
  ], { x: 6.42, y: 5.3, w: 6.1, h: 0.5, fontFace: F.body, margin: 0, lineSpacingMultiple: 1.02 });
  H.promptChip(s, 0.55, 5.95, 12.2, 1.12, 8,
    'Course log — the specialist hospital. Explain Mixture of Experts to me like a colleague: a model built as a huge specialist hospital where only a few departments wake up for each question. Then, plainly: why did this make powerful AI dramatically cheaper in 2025 — and what does it have to do with the deep-research and thinking modes in my own AI app? Under 120 words.',
    { label: 'MoE, explained by your own assistant', size: 8.8 });
  s.addNotes(
    'HOW TO PRESENT —\n' +
    '1) Anchor the moment, LEFT top card: January 2025 — an open model rivals o1; Nvidia’s $589B day; and keep the cost claim honest — the famous $5.6M is the fuel bill for the final winning race, not the cost of the racing team (total hardware spend was estimated well over $500M).\n' +
    '2) LEFT teal card — define MoE with the hospital, plainly: built like a huge specialist hospital; 671 billion parameters exist, ~37 billion wake up per question; you pay for the specialists consulted, not the whole building. Distillation = big models teaching small ones.\n' +
    '3) RIGHT chart: five benchmark pairs — matched or ahead on three, behind on two (be honest: not a clean sweep) — then the bill line: 27× cheaper output; $100 of o1 work for $3.60.\n' +
    '4) Close the loop to Part 1: THIS is why thinking modes and deep research became affordable for everyone.\n' +
    '\n' +
    'TRY IT — PROMPT 8/8 (course log)\n' +
    'Optional if time is tight; the answer doubles as their MoE cheat-note in the log.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“So whose servers is your data on? The trust map.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'MoE = Mixture of Experts — only a fraction of the model computes per token (671B built, ~37B working).\n' +
    'MIT license = a permissive open-source license. R1 = DeepSeek’s open reasoning model; o1 = OpenAI’s.\n' +
    'AIME / MATH-500 / GPQA / SWE-bench / Codeforces = math-olympiad, math, PhD-science, coding-agent and competitive-programming benchmarks.\n' +
    '\n' +
    'CONTENT —\n' +
    'Chart data verified against the R1 paper (arXiv:2501.12948) — see notes/research/r13_reputations_r1.md. Codeforces bars are human percentiles, not accuracy — the legend says so.\n' +
    'Pricing: R1 $0.55/$2.19 vs o1 $15/$60 per M tokens (Jan 2025) = 27.3–27.4×.\n' +
    'Since then (if asked): DeepSeek stayed the open-weight value leader but slipped off the leading edge — NIST’s CAISI evaluation (May 2026) put it ~8 months behind the frontier.\n' +
    'What the wave brought beyond DeepSeek (former on-slide list, now spoken if useful): open weights with permissive licenses to self-host (Qwen the most-downloaded family; famously self-hosted by Airbnb) · price pressure that pushed OpenAI to ship its first open-weight models since GPT-2 (gpt-oss, Aug 2025) · trillion-parameter open agentic models (Kimi).\n' +
    'US–China top-model gap: ~3% (Stanford AI Index 2026), down from 18–32 points in 2023.');

  // ---------- 18. SERVERS, TIERS, TRUST ----------
  s = H.slide('PART 2 · TRUST & DATA', 18);
  H.title(s, 'Where your words go', 'Trust the tier, not the logo — Sep 2026');
  const servers = [
    ['Anthropic', 'stored in the US · EU via cloud partners (Bedrock / Vertex / Foundry)'],
    ['OpenAI', 'EU residency (2025) + in-region processing (2026) — business tiers only'],
    ['Google', 'enterprise: residency by region · consumer: reviewed chats kept up to 3 yrs'],
    ['Microsoft', 'EU Data Boundary — but Claude models inside Copilot sit outside it'],
    ['xAI', 'own US data centers (Memphis) · no residency options published'],
    ['Perplexity', 'AWS, worldwide · no residency options published'],
    ['DeepSeek', '“stored in the People’s Republic of China” — its own privacy policy'],
    ['Kimi (Moonshot)', 'PRC storage · training opt-out only via customer service'],
    ['Z.ai (Zhipu)', 'Singapore processing · parent on the US Entity List'],
  ];
  s.addText('Whose servers, where', { x: 0.55, y: 1.5, w: 5.9, h: 0.32, fontFace: F.head, fontSize: 13, bold: true, color: C.INK, margin: 0 });
  servers.forEach((r, i) => {
    const y = 1.9 + i * 0.5;
    H.card(s, 0.55, y, 5.9, 0.44, i % 2 ? 'FFFFFF' : C.PANEL, i % 2 ? C.LINE : null);
    s.addText(r[0], { x: 0.75, y: y + 0.02, w: 1.55, h: 0.4, fontFace: F.body, fontSize: 9.5, bold: true, color: i > 5 ? C.RED : C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText(r[1], { x: 2.35, y: y + 0.02, w: 4.0, h: 0.4, fontFace: F.body, fontSize: 8.4, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.95 });
  });
  const tiers = [
    [C.GREEN_TINT, C.GREEN, 'GREEN · Company tenant — approved for work data, within policy', 'Enterprise/business accounts: no training on your data by default (every major vendor), audit controls, contracts. This is where company work belongs.'],
    [C.AMBER_TINT, C.AMBER, 'YELLOW · Personal account — public material only', 'Every vendor trains on consumer chats by default. The 2025 leaks all happened here: 370K Grok chats indexed by Google; “deleted” chats preserved for court cases. Never client or regulated data.'],
    [C.RED_TINT, C.RED, 'RED · China-hosted consumer apps — no company data, ever', 'The app sends data to China, under Chinese law (Italy blocked DeepSeek). The open-weight MODELS are a different object: run by IT on approved US/EU servers, they send nothing anywhere. The app, not the model, is the risk.'],
  ];
  tiers.forEach((t, i) => {
    const y = 1.5 + i * 1.65;
    H.card(s, 6.65, y, 6.1, 1.52, t[0]);
    s.addText([
      { text: t[2], options: { bold: true, color: t[1], fontSize: 10.8, breakLine: true, paraSpaceAfter: 3 } },
      { text: t[3], options: { color: C.SLATE, fontSize: 9.4 } },
    ], { x: 6.92, y: y + 0.1, w: 5.6, h: 1.34, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.05 });
  });
  H.callout(s, 0.55, 6.5, 12.2, 0.6, C.TEAL_TINT, [
    { text: 'One question decides: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11.5 } },
    { text: 'does company data leave your network — and whose account is it on? Company tenant → work. Personal → public material only. China-hosted app → never.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'key', iconFill: C.TEAL, size: 11 });
  s.addNotes(
    '[REFRESH QUARTERLY — owner: Oscar]\n' +
    '\n' +
    'HOW TO PRESENT —\n' +
    '1) Open with the finding that reorganized this slide: every Western vendor trains on CONSUMER chats by default, and NONE trains on enterprise-tier data — so trust tracks the account tier, not the company logo. The same logo appears in green and yellow.\n' +
    '2) LEFT table, fast: whose servers, where. Two rows to slow on: Microsoft (EU Data Boundary — but the Claude models inside Copilot sit OUTSIDE it; your IT team cares) and DeepSeek (its own policy says data is stored in the People’s Republic of China).\n' +
    '3) RIGHT tiers top to bottom: green = company tenant, where work belongs · yellow = personal accounts, where all the 2025 leaks happened · red = China-hosted consumer apps, never — and say the restaurant-vs-cookbook line plainly: using the app is eating at their restaurant (they see your order); downloaded open weights are a cookbook IT can cook from at home (nothing is sent anywhere).\n' +
    '4) Teal band: the one deciding question, verbatim.\n' +
    '\n' +
    'BRIDGE —\n' +
    '“From models to the tools that DO things — the gallery.”\n' +
    '\n' +
    'ACRONYMS —\n' +
    'PRC = People’s Republic of China. EU Data Boundary = Microsoft’s commitment to process EU data inside the EU.\n' +
    'AWS = Amazon Web Services. Entity List = the US federal trade-restriction list — a procurement red flag.\n' +
    '\n' +
    'CONTENT —\n' +
    'Every row and tier claim sourced in notes/research/r11_vendor_trust.md (researched Sep 9, 2026), incl.: consumer-training defaults all-vendors; Grok’s ~370K indexed chats (Aug 2025); OpenAI court-ordered retention of “deleted” chats (2025, enterprise excluded); Italy’s DeepSeek block (Jan 2025, not lifted); DeepSeek’s exposed chat-log database (Jan 2025); Kimi PRC storage; Z.ai Entity-List parent.\n' +
    'Green ≠ invulnerable: EchoLeak (CVE-2025-32711, Jun 2025) was a zero-click prompt-injection exfiltration hole in enterprise Copilot — patched, but proof that novel attack surface exists even in green.\n' +
    'Defaults drift (Anthropic flipped consumer training Aug 2025; Microsoft Oct 2024) — re-verify quarterly.\n' +
    'Standing rule, always said aloud: your organization’s AI policy and approved-tool list outrank everything on this slide.');

  // ---------- 19. AGENT GALLERY — THE DOERS ----------
  s = H.slide('PART 2 · AGENTIC TOOLS', 19);
  H.title(s, 'The agent gallery · the doers', 'Agents that run jobs — names you’ll hear');
  const gallery = [
    ['terminal', 'Claude Code', 'Anthropic', 'Agentic coding AND general file/data automation — points at a real folder: reads PDFs, builds spreadsheets, writes reports. Built this training’s materials.'],
    ['users', 'Claude Cowork', 'Anthropic', 'The same engine for non-technical knowledge work: “describe the outcome, step away, come back to finished files.” Licensed by Microsoft as Copilot Cowork.'],
    ['zap', 'ChatGPT Work', 'OpenAI', 'Agent mode beside Chat: connects Slack/Gmail/Drive, runs scheduled tasks, produces decks, sheets, small apps.'],
    ['grid', 'Copilot agents', 'Microsoft', 'Researcher, Analyst, Excel Agent Mode, Copilot Studio — governed agents inside your tenant. The path of least resistance at most enterprises.'],
    ['robot', 'Manus', 'independent (Singapore)', 'The famous general agent: goal in, finished multi-step work out. So famous Meta paid ~$2B for it — and Beijing forced the deal apart. Try it personally; don’t feed it company data.'],
    ['sitemap', 'Notion Agents', 'Notion', 'Agents living inside the workspace you may already use: run 24/7 on triggers (schedules, Slack, email), build docs and databases, shareable with the team.'],
    ['branch', 'Automation platforms', 'n8n · Zapier', 'Wire apps together with agent steps in the flow: n8n for technical/self-hosted, Zapier for business users, 8,000+ connectors.'],
    ['alert', 'OpenClaw', 'open source', 'DIY personal agent run from WhatsApp/Telegram — and 2026’s security cautionary tale. Not for corporate use; its lessons come in Part 5.'],
  ];
  gallery.forEach((g, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.6 + Math.floor(i / 2) * 1.28;
    H.card(s, x, y, 5.95, 1.16, i === 7 ? C.AMBER_TINT : C.PANEL);
    H.iconCircle(s, x + 0.18, y + 0.32, 0.5, g[0], i === 7 ? C.AMBER : C.TEAL);
    s.addText([
      { text: g[1] + '  ', options: { bold: true, color: C.INK, fontSize: 12 } },
      { text: g[2], options: { color: C.MUTE, fontSize: 9, breakLine: true, paraSpaceAfter: 2 } },
      { text: g[3], options: { color: C.SLATE, fontSize: 9.2 } },
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
    'v1.5: gallery split into doers/makers; Manus and Notion Agents added (evidence: notes/research/r12_tool_landscape.md).\n' +
    'Manus: Meta acquisition ~$2B Dec 2025; Beijing (NDRC) ordered unwind Apr 2026; independent Singapore company Aug 2026; desktop “My Computer” mode Mar 2026.\n' +
    'Notion: Custom Agents (Feb 2026) run on triggers with scoped permissions; Business/Enterprise plans; usage billed in credits.\n' +
    'OpenClaw: maintainer’s own warning — “if you can’t run a command line, this is far too dangerous to use safely”; CVE-2026-25253 (1-click RCE); a malicious #1-ranked community skill (Cisco).');

  // ---------- 20. SPECIALIST SHELF — THE MAKERS ----------
  s = H.slide('PART 2 · AGENTIC TOOLS', 20);
  H.title(s, 'The specialist shelf · the makers', 'One great tool per job — September 2026');
  const shelf = [
    ['book', 'Gemini Notebook (was NotebookLM)', 'Google', 'Upload YOUR documents, get cited answers, audio overviews, mind maps. Grounded in your sources = low hallucination. The most useful new tool for this room.'],
    ['mic', 'Meeting notes', 'Teams / Zoom native · Granola', 'Check your native tool first (IT-sanctioned). Granola is the bot-free best-in-class — but recording consent policy applies either way.'],
    ['layout', 'Decks & design', 'Gamma · Canva AI', 'Gamma: a full deck from a prompt (70M users). Canva: the design suite marketing already licenses, now with conversational AI.'],
    ['image', 'Images — the safe lane', 'Adobe Firefly', 'Trained only on licensed content and ships with legal indemnification — the corporate pick. ChatGPT Images 2.0 / Nano Banana 2 are already in your chatbot for internal drafts.'],
    ['html', 'Apps without code', 'Lovable', 'Describe an app in plain language → working web app with database and login (Adidas, NVIDIA use it). Security review before real company data.'],
    ['translate', 'Voice & language', 'ElevenLabs · DeepL', 'ElevenLabs: narrated training modules, dubbing (consent rules for voice cloning). DeepL: real-time spoken translation + document-grade language work.'],
    ['video', 'Video', 'Veo 3.1 (in Google tools)', 'Good enough for internal video today. Cautionary tale: OpenAI’s famous Sora app shut down 14 months after launch — never build a process on a consumer app.'],
    ['search', 'Find more, forever', 'your own assistant', 'Tools change monthly. Ask your approved AI: “Search the web: what are the best current tools for [my task], and which are enterprise-safe?” That answer never goes stale.'],
  ];
  shelf.forEach((g, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.6 + Math.floor(i / 2) * 1.24;
    H.card(s, x, y, 5.95, 1.12, i === 7 ? C.TEAL_TINT : C.PANEL);
    H.iconCircle(s, x + 0.18, y + 0.3, 0.5, g[0], C.TEAL);
    s.addText([
      { text: g[1] + '  ', options: { bold: true, color: C.INK, fontSize: 11.5 } },
      { text: g[2], options: { color: C.MUTE, fontSize: 8.8, breakLine: true, paraSpaceAfter: 2 } },
      { text: g[3], options: { color: C.SLATE, fontSize: 9 } },
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
    '2) Slow on two: Gemini Notebook (say the rename out loud — it was NotebookLM until July 2026, people know the old name; grounded in YOUR documents = the anti-hallucination tool) and Firefly (the image tool trained only on licensed content, with legal indemnification — the one your legal team will like).\n' +
    '3) The Sora line, plainly: a world-famous video app shut down fourteen months after launch — the lesson is never to build a business process on a consumer app.\n' +
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
    'v1.5: replaces the former task-matrix and rankings slides (owner: redundant). Their two salvage lines live on: the policy band here, and “vendor numbers are marketing” in the assistants notes.\n' +
    'Evidence per tool in notes/research/r12_tool_landscape.md, incl.: NotebookLM→Gemini Notebook rename (Jul 16, 2026); Granola $1.5B valuation (Mar 2026) + the consent caveat; Gamma $100M ARR/70M users (Nov 2025); Firefly licensed-training + indemnification (Adobe business terms); Lovable enterprise users; DeepL Voice-to-Voice (Apr 2026); Sora app shutdown (Apr 2026).\n' +
    'Deliberately NOT on the slide: Stable Diffusion (open-source image generation — now an IT/developer tool: local installs, no indemnification; say “the open-source option IT might run privately” if asked) and Midjourney (artists’ favorite; active studio copyright litigation — legal-risk caveat).\n' +
    'If someone wants a directory anyway: There’s An AI For That — browse by task, verify with IT before use.');
};
