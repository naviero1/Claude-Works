// PART 2 — Models & tools landscape (verified Aug 2026)
const { C, F } = require('./deck_lib');

module.exports = function buildPartTwo(pres, H) {
  // ---------- 14. PART 2 DIVIDER ----------
  let s = H.slide(null, 14, { dark: true });
  H.partMarker(s, 2);
  s.addText('PART 2 · MODELS & TOOLS', { x: 0.55, y: 2.3, w: 12, h: 0.5, fontFace: F.body, fontSize: 16, bold: true, charSpacing: 4, color: C.TEAL_LIGHT, margin: 0 });
  s.addText('The landscape,\nAugust 2026', { x: 0.55, y: 2.8, w: 11.5, h: 1.9, fontFace: F.head, fontSize: 44, bold: true, color: C.ON_DARK, margin: 0, lineSpacingMultiple: 1.05 });
  s.addText('Who makes what, what each is genuinely good at, what the Chinese open-weight wave changed — and which agentic tools are worth knowing by name. Everything on these slides is dated: this field re-ranks monthly.', { x: 0.55, y: 4.85, w: 11, h: 0.8, fontFace: F.body, fontSize: 15, color: C.ON_DARK_MUTE, margin: 0, lineSpacingMultiple: 1.15 });
  s.addNotes(
    'HOW TO PRESENT — 1) Progress bar: part 2 of 6. 2) One framing sentence: “Names and fortes, all dated August 2026 — the names churn monthly; the habits you leave with don’t.” 3) Under 30 seconds, advance.\n' +
    'ACRONYMS — none on this slide.');

  // ---------- 15. ASSISTANT LANDSCAPE ----------
  s = H.slide('PART 2 · THE ASSISTANTS', 15);
  H.title(s, 'The assistants', 'Six names cover the chat landscape — August 2026');
  const vendors = [
    ['Claude', 'Anthropic · Fable 5 / Opus 5 / Sonnet 5 / Haiku 4.5', 'Forte: agentic work & coding (top of SWE-bench), long documents (1M ctx), careful writing.', 'Caveat: premium pricing at the top tier; flagship can refuse high-risk domains by design.'],
    ['ChatGPT', 'OpenAI · GPT-5.6 family (Sol / Terra / Luna)', 'Forte: the all-rounder with the largest user base — reasoning, images, voice, Work agent mode.', 'Caveat: fast model churn and renaming; check tenant/data settings before regulated content.'],
    ['Gemini', 'Google · Gemini 3 / 3.1 Pro / 3.6 Flash + Deep Think', 'Forte: deepest multimodal stack (Veo video, Nano Banana images), Workspace integration, giant context.', 'Caveat: confusing model-name sprawl; best reasoning sits behind the Ultra tier.'],
    ['Copilot', 'Microsoft · GPT-5.6 preferred + Claude selectable', 'Forte: lives inside Word, Excel, Outlook, Teams with tenant-level governance — the sanctioned default at most enterprises.', 'Caveat: admin flags mean colleagues get different capabilities; opaque model labels.'],
    ['Perplexity', 'Perplexity · own stack + Model Council (GPT+Claude+Gemini)', 'Forte: cited web research — Pro Search reads 300+ sources; Comet agentic browser.', 'Caveat: a citation isn’t proof — click through before quoting anywhere formal.'],
    ['Grok', 'SpaceXAI · Grok 4.6', 'Forte: aggressive price-performance and speed; real-time X data; coding-agent focus.', 'Caveat: lighter enterprise governance history — apply extra review at work.'],
  ];
  vendors.forEach((v, i) => {
    const x = 0.55 + (i % 3) * 4.18;
    const y = 1.62 + Math.floor(i / 3) * 2.5;
    H.card(s, x, y, 3.95, 2.32, C.PANEL);
    s.addText(v[0], { x: x + 0.24, y: y + 0.14, w: 3.4, h: 0.38, fontFace: F.head, fontSize: 16, bold: true, color: C.TEAL_DARK, margin: 0 });
    s.addText(v[1], { x: x + 0.24, y: y + 0.52, w: 3.5, h: 0.32, fontFace: F.body, fontSize: 8.6, bold: true, charSpacing: 0.5, color: C.MUTE, margin: 0 });
    s.addText(v[2], { x: x + 0.24, y: y + 0.88, w: 3.5, h: 0.85, fontFace: F.body, fontSize: 9.6, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.04 });
    s.addText(v[3], { x: x + 0.24, y: y + 1.72, w: 3.5, h: 0.55, fontFace: F.body, fontSize: 8.8, italic: true, color: C.AMBER, margin: 0, lineSpacingMultiple: 1.0 });
  });
  s.addText('Model names verified Aug 21, 2026 — they will have moved by the time you read this. The fortes move slower; the habits in Parts 3–5 don’t move at all.', { x: 0.55, y: 6.68, w: 12.2, h: 0.35, fontFace: F.body, fontSize: 10, italic: true, color: C.MUTE, margin: 0 });
  s.addNotes(
    '[REFRESH QUARTERLY — owner: Oscar]\n' +
    'HOW TO PRESENT — 1) Frame: “six names cover the chat landscape.” 2) Walk the cards in reading order — Claude → ChatGPT → Gemini (top row), Copilot → Perplexity → Grok (bottom row) — saying ONE forte line each; let the amber caveats be read, not spoken. 3) Point at the italic footer: names verified Aug 21, 2026 — they WILL have moved; the matrix a few slides ahead does the practical work. 4) Bridge: “one force reshaped this list in 2025 — the Chinese open-weight wave.”\n' +
    'ACRONYMS — SWE-bench = Software Engineering benchmark — the standard test of coding-agent ability. ctx = context window. GPT-5.6 Sol / Terra / Luna = OpenAI’s current tier names. X = the social platform (Grok’s data source).\n' +
    'CONTENT — One line each, then move — the matrix (four slides ahead) does the practical work. Names to say: Claude Fable 5 (Jun 2026, current flagship), GPT-5.6 Sol/Terra/Luna (Jul 2026), Gemini 3 family, Copilot now lets you pick Claude inside Office (Researcher, Excel Agent Mode). Grok note: xAI was acquired by SpaceX (Feb 2026).');

  // ---------- 16. THE CHINESE WAVE ----------
  s = H.slide('PART 2 · THE CHINESE WAVE', 16);
  H.title(s, 'The DeepSeek moment — and after', 'What the Chinese labs brought to the table');
  H.card(s, 0.55, 1.62, 5.4, 2.5, C.PANEL);
  s.addText('January 2025, in three facts', { x: 0.82, y: 1.82, w: 4.9, h: 0.35, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.87, 2.25, 4.85, 1.85, [
    { t: 'DeepSeek-R1: open-weights reasoning rivaling OpenAI’s o1, MIT-licensed, ~96% cheaper per token' },
    { t: 'Nvidia lost $589B in one day (Jan 27) — the largest single-day loss in market history at the time' },
    { t: 'The “$5.6M training cost”? Final-run fuel bill, not the cost of the racing team — real efficiency, oversold headline', b: true },
  ], { size: 10.8, gap: 6 });
  H.card(s, 0.55, 4.28, 5.4, 2.35, C.TEAL_TINT);
  s.addText('The gap, measured', { x: 0.82, y: 4.46, w: 4.9, h: 0.35, fontFace: F.head, fontSize: 14, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.87, 4.88, 4.85, 1.7, [
    { t: 'US–China top-model gap: ~3% (Stanford AI Index 2026) — down from 18–32 points in 2023' },
    { t: '…achieved on ~23× less visible private AI investment ($286B US vs $12B China, 2025)' },
  ], { size: 10.8, gap: 6 });
  s.addText('What they brought', { x: 6.35, y: 1.62, w: 6, h: 0.4, fontFace: F.head, fontSize: 15, bold: true, color: C.INK, margin: 0 });
  const gifts = [
    ['package', 'Open weights, permissive licenses', 'MIT / Apache models you can download, self-host, fine-tune — data never leaves your infrastructure'],
    ['cpu', 'Efficiency as a discipline', 'Mixture-of-Experts (671B total, ~37B working per token) + distillation: frontier ability at a fraction of the cost'],
    ['dollar', 'Price pressure on everyone', 'forced US labs to respond — OpenAI shipped its first open-weight models since GPT-2 (gpt-oss, Aug 2025)'],
    ['robot', 'Open agentic models', 'Kimi K2 line: trillion-parameter open models chaining hundreds of tool calls'],
    ['globe', 'Global adoption', 'Alibaba’s Qwen: the most-downloaded open family on Hugging Face, ~150K derivative models; US firms (famously Airbnb) self-host it'],
  ];
  gifts.forEach((g, i) => H.iconRow(s, 6.35, 2.12 + i * 0.92, 6.4, g[0], C.TEAL, g[1], g[2], { d: 0.46, headSize: 12, descSize: 9.8, h: 0.88 }));
  s.addNotes(
    'HOW TO PRESENT — 1) Anchor the moment with the LEFT top card — January 2025 in three facts: R1 rivals o1 at ~96% cheaper; Nvidia’s $589B day; and keep the cost claim honest — the famous $5.6M is the final-run fuel bill, not the racing team. 2) RIGHT column: the five things they brought, top to bottom, one line each. 3) LEFT bottom card: the gap, measured — ~3% on ~23× less visible investment. 4) Bridge: “so who’s who — and what’s the one rule that keeps you safe?”\n' +
    'ACRONYMS — MoE = Mixture-of-Experts — only a fraction of the model computes per token (671B built, ~37B working). MIT / Apache = permissive open-source licenses. R1 = DeepSeek’s open reasoning model; o1 = OpenAI’s. B = billion. gpt-oss = OpenAI’s first open-weight models since GPT-2 (Aug 2025). K2 = Kimi’s trillion-parameter agentic model line.\n' +
    'CONTENT — The fuel-bill analogy keeps the cost claim honest (SemiAnalysis: total hardware spend >$500M). The Airbnb story teaches both sides: CEO praised Qwen as “fast and cheap” for customer service — then Congress asked questions, and the defense was exactly “self-hosted open weights: we send no data to China.” Which sets up the next slide.');

  // ---------- 17. CHINESE LLMS — WHO'S WHO + SAFE USE ----------
  s = H.slide('PART 2 · THE CHINESE WAVE', 17);
  H.title(s, 'Who’s who — and the rule that keeps you safe', 'The app sends data to China. The weights are just a file.');
  const cn = [
    ['DeepSeek', 'MoE pioneer; R1 reasoning; V4 line current (open weights)'],
    ['Qwen (Alibaba)', 'the open ecosystem leader; Apache 2.0; every size from laptop to trillion-class'],
    ['Kimi (Moonshot)', 'agentic specialist; 1T-param open models built for tool use'],
    ['GLM (Z.ai / Zhipu)', 'MIT-licensed agent/coding models; on the US Entity List — procurement red flag'],
    ['MiniMax · Baidu · Tencent', 'long-context leader · Ernie went open 2025 · broad open portfolio'],
  ];
  cn.forEach((cd, i) => {
    const y = 1.62 + i * 0.78;
    H.card(s, 0.55, y, 5.9, 0.68, C.PANEL);
    s.addText(cd[0], { x: 0.78, y: y + 0.06, w: 2.2, h: 0.56, fontFace: F.head, fontSize: 11.5, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    s.addText(cd[1], { x: 3.0, y: y + 0.05, w: 3.35, h: 0.58, fontFace: F.body, fontSize: 9.2, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.98 });
  });
  H.card(s, 6.75, 1.62, 6.0, 2.4, C.RED_TINT);
  s.addText('Consumer apps: not for work. Ever.', { x: 7.02, y: 1.8, w: 5.5, h: 0.35, fontFace: F.head, fontSize: 13.5, bold: true, color: C.RED, margin: 0 });
  H.bullets(s, 7.07, 2.2, 5.4, 1.75, [
    { t: 'Data goes to servers in China, under Chinese law — Italy blocked the DeepSeek app; banned on government devices in the US, Australia, South Korea, Taiwan…' },
    { t: '1 in 25 enterprise AI prompts went to a China-based app in 2025 — mostly without IT knowing (Harmonic, 22M prompts)', b: true },
  ], { size: 10.5, gap: 6 });
  H.card(s, 6.75, 4.2, 6.0, 2.4, C.GREEN_TINT);
  s.addText('Self-hosted open weights: a different question', { x: 7.02, y: 4.38, w: 5.5, h: 0.35, fontFace: F.head, fontSize: 13.5, bold: true, color: C.GREEN, margin: 0 });
  H.bullets(s, 7.07, 4.78, 5.4, 1.7, [
    { t: 'Restaurant vs cookbook: the app sees your order; the downloaded weights cook at home — nothing is sent anywhere' },
    { t: 'Still IT/governance territory: licenses, Entity-List vendors, and alignment quirks travel with the weights (a local R1 still won’t discuss Tiananmen) — evaluate like any software of unknown provenance' },
  ], { size: 10.5, gap: 6 });
  H.callout(s, 0.55, 5.7, 5.9, 0.9, C.TEAL_TINT, [
    { text: 'One question decides: ', options: { bold: true, color: C.TEAL_DARK, fontSize: 11 } },
    { text: 'does company data leave your network? Hosted app → yes: never. Self-hosted weights → no: an IT governance decision.', options: { color: C.SLATE, fontSize: 11 } },
  ], { iconName: 'key', iconFill: C.TEAL, size: 11 });
  s.addNotes(
    'HOW TO PRESENT — 1) Read the title sentence — it IS the rule: “the app sends data to China; the weights are just a file.” 2) LEFT column: five vendor rows, fast — names to recognize, not memorize. 3) RED card: consumer apps, never for work — the bans list, then the shadow-AI stat: 1 in 25 enterprise prompts went to a China-based app, mostly without IT knowing. 4) GREEN card: self-hosted weights are a different question — restaurant vs cookbook; still governed (licenses, Entity List, alignment quirks travel with the file). 5) Land on the bottom-left teal card: one question decides everything — does company data leave your network? 6) Bridge: “from models to agents — the gallery.”\n' +
    'ACRONYMS — MoE = Mixture-of-Experts. R1 / V4 = DeepSeek model lines. GLM = Zhipu’s model family. US Entity List = the federal trade-restriction list — a procurement red flag. IT = Information Technology (your technology organization). API = Application Programming Interface — the hosted service route.\n' +
    'CONTENT — The one distinction to hammer: hosted app/API (data to China; what regulators banned) vs self-hosted weights (a file on your GPUs; the Airbnb defense). Both sentences are simultaneously true: “never company data in Chinese consumer apps” AND “IT may evaluate self-hosted weights through governance review.” For this audience: treat open-weight models like SOUP — software of unknown provenance — with documented evaluation.');

  // ---------- 18. AGENTIC TOOL GALLERY ----------
  s = H.slide('PART 2 · AGENTIC TOOLS', 18);
  H.title(s, 'The agent gallery', 'Names you’ll hear — and what each is actually for');
  const gallery = [
    ['terminal', 'Claude Code', 'Anthropic', 'Agentic coding AND general file/data automation — terminal, desktop, web. Points at a real folder: reads PDFs, builds spreadsheets, writes reports. Skills make workflows repeatable.'],
    ['users', 'Claude Cowork', 'Anthropic', 'The same engine packaged for non-technical knowledge work: “describe the outcome, step away, come back to finished files.”'],
    ['zap', 'ChatGPT Work', 'OpenAI', 'Agent mode beside Chat and Codex: connects Slack/Gmail/Drive, runs scheduled tasks, produces decks, sheets, small apps.'],
    ['grid', 'Copilot agents', 'Microsoft', 'Researcher, Analyst, Excel Agent Mode, Copilot Studio — governed agents inside your tenant. The path of least resistance at most enterprises.'],
    ['code', 'Coding IDEs', 'Cursor · Devin · GitHub Copilot', 'Developer-grade agents: multi-file refactors, assign-an-issue-get-a-PR. Engineering tools, not business-user tools.'],
    ['globe', 'Browser agents', 'Comet · Claude in Chrome', 'The assistant rides in your browser, sees pages, acts on them. Powerful; injection-prone — treat every page as untrusted input.'],
    ['branch', 'Automation platforms', 'n8n · Zapier', 'Wire apps together with agent steps in the flow: n8n for technical/self-hosted, Zapier for business users, 8,000+ connectors.'],
    ['alert', 'OpenClaw', 'open source', 'DIY personal agent run from WhatsApp/Telegram; ~250K GitHub stars — and 2026’s security cautionary tale. Not for corporate use; its lessons come in Part 5.'],
  ];
  gallery.forEach((g, i) => {
    const x = 0.55 + (i % 2) * 6.2;
    const y = 1.6 + Math.floor(i / 2) * 1.28;
    H.card(s, x, y, 5.95, 1.16, i === 7 ? C.AMBER_TINT : C.PANEL);
    H.iconCircle(s, x + 0.18, y + 0.32, 0.5, g[0], i === 7 ? C.AMBER : C.TEAL);
    s.addText([
      { text: g[1] + '  ', options: { bold: true, color: C.INK, fontSize: 12 } },
      { text: g[2], options: { color: C.MUTE, fontSize: 9, breakLine: true, paraSpaceAfter: 2 } },
      { text: g[3], options: { color: C.SLATE, fontSize: 9.3 } },
    ], { x: x + 0.8, y: y + 0.06, w: 5.0, h: 1.05, fontFace: F.body, valign: 'middle', margin: 0, lineSpacingMultiple: 1.0 });
  });
  s.addNotes(
    '[REFRESH QUARTERLY — owner: Oscar]\n' +
    'HOW TO PRESENT — 1) Frame: “eight names you’ll hear — and what each is actually FOR.” 2) Walk the cards left to right, top to bottom, one line each. Slow slightly on two: Claude Code (“this very training’s materials were built with it”) and Copilot agents (“the path of least resistance inside your tenant”). 3) End on the amber OpenClaw card: 2026’s security cautionary tale — don’t tell the whole story now; its lessons return in Part 5’s guardrails. 4) Bridge: “so which one for which job? The matrix.”\n' +
    'ACRONYMS — IDE = Integrated Development Environment — a programmer’s editor. PR = Pull Request — a proposed code change on GitHub. DIY = do-it-yourself. n8n / Zapier = automation-platform product names (not acronyms).\n' +
    'CONTENT — Claude Code appears twice in this training on purpose: it is the tool this deck’s own materials were built with, and the natural home of the agentic templates in Part 5. OpenClaw: created by Peter Steinberger; renamed Clawdbot → Moltbot → OpenClaw after trademark issues; the maintainer’s own warning — “if you can’t run a command line, this is far too dangerous to use safely” — plus CVEs (Common Vulnerabilities and Exposures — publicly registered security flaws), 135K exposed instances, and a malicious #1-ranked community skill (Cisco).');

  // ---------- 19. RIGHT TOOL FOR THE TASK ----------
  s = H.slide('PART 2 · RIGHT TOOL FOR THE TASK', 19);
  H.title(s, 'The matrix', 'Right tool for the task — August 2026');
  const matrix = [
    ['Long documents & doc comparison', 'Claude or Gemini (1M-class context) · confidential material → your approved internal tool only'],
    ['Data analysis', 'Copilot Excel Agent Mode (in-tenant) · Claude / ChatGPT with code execution · agentic: Claude Code / Cowork for file crunching'],
    ['Presentations & documents', 'Copilot in PowerPoint (your templates) · Claude Cowork / ChatGPT Work build full files'],
    ['Cited web research', 'Perplexity first · deep-research modes in ChatGPT / Gemini / Claude · verify citations regardless'],
    ['Writing & editing', 'All capable; Claude for careful long-form · Copilot for in-place edits in Outlook/Word'],
    ['Coding & repo work', 'Claude Code · Cursor · GitHub Copilot · (SWE-bench leaders: Claude Opus 5 / Fable 5, ~95–96%)'],
    ['Images · video', 'ChatGPT Images 2.0 (photoreal) · Nano Banana 2 (stylized/text) · Veo 3.1 (video)'],
    ['Speed & bulk / self-hosting', 'Gemini Flash, Claude Haiku (cheap+fast) · open weights (Qwen, DeepSeek, Kimi) via approved infra'],
  ];
  matrix.forEach((m, i) => {
    const y = 1.6 + i * 0.63;
    H.card(s, 0.55, y, 12.2, 0.55, i % 2 ? 'FFFFFF' : C.PANEL, i % 2 ? C.LINE : null);
    s.addText(m[0], { x: 0.78, y: y + 0.04, w: 3.6, h: 0.47, fontFace: F.body, fontSize: 10.5, bold: true, color: C.INK, margin: 0, valign: 'middle' });
    s.addText(m[1], { x: 4.5, y: y + 0.04, w: 8.05, h: 0.47, fontFace: F.body, fontSize: 9.6, color: C.SLATE, margin: 0, valign: 'middle', lineSpacingMultiple: 0.95 });
  });
  H.callout(s, 0.55, 6.62, 12.2, 0.48, C.AMBER_TINT, [
    { text: 'Standing rule: ', options: { bold: true, color: C.INK, fontSize: 10.5 } },
    { text: 'your organization’s AI policy and approved-tool list outrank every cell of this table.', options: { color: C.SLATE, fontSize: 10.5 } },
  ], { iconName: 'shield', iconFill: C.AMBER, size: 10.5 });
  s.addNotes(
    '[REFRESH QUARTERLY — owner: Oscar]\n' +
    'HOW TO PRESENT — 1) Announce it: “screenshot slide — this map is yours to keep.” Give them five seconds to actually take the photo. 2) Walk only TWO rows in full — data analysis and presentations (the rooms’ daily work); gesture over the rest as reference. 3) Finish on the amber band and say it VERBATIM: “your organization’s AI policy and approved-tool list outrank every cell of this table.” 4) Bridge: “so how do you pick from this table when the rankings churn every month? With your own three tasks — next slide.”\n' +
    'ACRONYMS — 1M-class = roughly one-million-token context window. SWE-bench = the standard coding-agent benchmark.\n' +
    'CONTENT — This is the screenshot-and-keep slide. Walk two rows the audience cares most about (data analysis, presentations) and let the rest be reference. Reinforce the policy caveat verbally every time.');

  // ---------- 20. YOUR PRIVATE TEST SET (v1.3 — replaces the rankings-caution slide + rep 2) ----------
  s = H.slide('PART 2 · YOUR PRIVATE TEST SET', 20);
  H.title(s, 'Picking tools when rankings churn', 'Three of your real tasks beat every leaderboard');
  H.card(s, 0.55, 1.7, 5.9, 3.3, C.PANEL);
  s.addText('Why you can ignore the rankings', { x: 0.85, y: 1.94, w: 5.3, h: 0.4, fontFace: F.head, fontSize: 14.5, bold: true, color: C.INK, margin: 0 });
  H.bullets(s, 0.9, 2.45, 5.3, 2.4, [
    { t: 'Top models cluster within ~1 point and re-rank monthly; benchmarks saturate and leak.' },
    { t: 'Vendor-reported numbers are marketing until independently reproduced — read them as claims.' },
    { t: 'And none of them measure the only thing that matters: fit for YOUR documents, YOUR data, YOUR formats.', b: true },
  ], { size: 11.8, gap: 8 });
  H.card(s, 6.75, 1.7, 6.0, 3.3, C.TEAL_TINT);
  s.addText('The 60-second habit that replaces them', { x: 7.05, y: 1.94, w: 5.5, h: 0.4, fontFace: F.head, fontSize: 14.5, bold: true, color: C.TEAL_DARK, margin: 0 });
  const tsteps = [
    ['1', 'Write down three of your real tasks — one analysis, one document, one deck or tracker.'],
    ['2', 'When a new model or tool ships, run the three and judge for yourself.'],
    ['3', 'Keep the list where you will find it — it outlives every leaderboard.'],
  ];
  tsteps.forEach((t, i) => {
    const y = 2.45 + i * 0.82;
    s.addText(t[0], { x: 7.05, y, w: 0.45, h: 0.5, fontFace: F.head, fontSize: 19, bold: true, color: C.TEAL, margin: 0 });
    s.addText(t[1], { x: 7.6, y: y + 0.02, w: 4.9, h: 0.75, fontFace: F.body, fontSize: 11.8, color: C.SLATE, margin: 0, lineSpacingMultiple: 1.06 });
  });
  H.callout(s, 0.55, 5.35, 12.2, 1.1, C.AMBER_TINT, [
    { text: 'Do it now — 60 seconds: ', options: { bold: true, color: C.AMBER, fontSize: 13 } },
    { text: 'write your three tasks before the next slide. That list is your private benchmark from here on — and the skills in Parts 3–5 transfer across every tool it ever ranks.', options: { color: C.SLATE, fontSize: 13 } },
  ], { iconName: 'target', iconFill: C.AMBER, size: 13 });
  s.addNotes(
    'HOW TO PRESENT — 1) Frame in one line: “before we leave tools — how do you PICK, when the rankings reshuffle monthly?” 2) LEFT card fast: models cluster within a point; benchmarks saturate and leak; vendor numbers are claims; and none of it measures fit for YOUR work (bold). 3) RIGHT card: the habit, steps 1→3 — three real tasks, run them on anything new, keep the list findable. 4) Amber band: actually give the room 60 SECONDS of silence to write their three tasks — this replaces a full rep; don’t skip the writing moment. 5) Close: “this training teaches prompting, not products — the skills transfer across every tool on your list.” 6) Bridge: “Part 3 — the craft itself.”\n' +
    'ACRONYMS — none needing expansion on this slide.\n' +
    'CONTENT — v1.3: merges the former rankings-caution slide and the Part 2 rep into one action slide (owner feedback: two slides + a rep was one idea stretched thin). Sources for the caution, if challenged: LMArena July 2026 re-baseline; SWE-bench Verified saturation reporting; Artificial Analysis clustering. The power-tools analogy survives in your pocket if someone pushes back: four good brands, any drives a screw — you pick by fit, shop, and feel, not last month’s magazine review.');
};