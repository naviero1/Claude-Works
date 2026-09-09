# r12 — Agent & tool landscape expansion (researched 2026-09-09)

Powers the v1.5 expansion of the Part 2 agent gallery into two slides. Audience filter:
non-technical office workers (documents, spreadsheets, decks, meetings, quality/regulatory
work). Every fact dated with a source URL; UNVERIFIED items at the bottom.

## General autonomous agents

**Manus** (the owner's "ManuAI") — general-purpose agent: plain-language goal → autonomous
multi-step execution in a cloud sandbox (browsing, analysis, spreadsheets, decks, reports,
web apps) (https://en.wikipedia.org/wiki/Manus_(AI_agent)).
- Ownership saga (verified, teachable): Meta acquired it for ~$2B in Dec 2025; China's NDRC
  ordered the deal unwound Apr 2026 (Fortune 2026-04-28); Meta unwound and halted data
  sharing Jun 2026 (TechCrunch 2026-06-13); now independent, Singapore-HQ (CNBC 2026-08-11).
- Desktop app with "My Computer" mode since 2026-03-18 (CNBC); full web apps from one
  prompt since Manus 1.5 (Oct 2025).
- Caveat: founded in China, Singapore HQ, fresh forced-divestiture history — "try
  personally, don't put company data in."

## Workspace agents

**Notion AI / Notion Agents** — Notion 3.0 Agents (2025-09-18) do "everything a human can
do in Notion"; Notion 3.3 **Custom Agents** (2026-02-24) run 24/7 on triggers (schedules,
Slack, email, database changes), scoped permissions, team-shareable
(https://www.notion.com/releases/2026-02-24). Caveat: Business/Enterprise plans only; usage
billed in Notion Credits ($10/1,000) since 2026-05-04. Notion crossed 100M users Aug 2024.

## Research & document assistants

**NotebookLM → renamed "Gemini Notebook" on 2026-07-16** (slide must carry both names) —
grounded assistant over YOUR sources: cited answers, Audio/Video Overviews, mind maps,
slide decks; each notebook now has a secure cloud computer that can run code
(https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html).
Auto Drive-sync since May 2026; Deep Research source-gathering since Nov 2025. Enterprise
flavor with VPC Service Controls via Google Cloud. Best single new tool for this audience:
grounded in your documents = low hallucination risk, free tier.

## Meeting assistants (one slot)

Framing: **"check your native tool first, Granola if you want best-in-class."**
- Teams Facilitator agent (needs M365 Copilot license; Aug 2026 update) — in-tenant.
- Zoom AI Companion 3.0 (Dec 2025) — cross-platform, can take notes in Teams/Meet ($12/mo
  add-on).
- **Granola** — bot-free desktop notepad (records system audio locally, no bot joins);
  $125M Series C at $1.5B valuation 2026-03-25 (TechCrunch); customers Vanta, Gusto, Asana.
  Caveat for the slide: bot-less recording can bypass visible-notice norms — flag the
  recording-consent policy.
- Otter.ai: $100M ARR, 35M+ users, AI Meeting Agents (Businesswire 2025-12-22) — runner-up.

## Slides & visual docs (one shared slot)

**Gamma** — decks from a prompt; $100M ARR, 70M users, $2.1B valuation, profitable
(TechCrunch 2025-11-10); Gamma 3.0 Agent (Sept 2025) researches and restyles whole decks.
Caveat: .pptx export workable, not perfect for strict corporate-template shops.
**Canva AI 2.0** (2026-04-16) + 100 Visual Suite features (2026-09-04) incl.
spreadsheet-data-to-charts — the design suite marketing already licenses.

## Image generation (one slide row, three lanes)

- **Adobe Firefly — the corporate-safe headline pick**: trained only on licensed Adobe
  Stock / public-domain / openly licensed content; paid plans include IP indemnification
  (https://business.adobe.com/products/firefly-business.html). Firefly AI Assistant
  (agentic) since 2026-04-27; hosts 30+ third-party models in one workspace.
- ChatGPT Images 2.0 (2026-04-21) and Google Nano Banana 2 (2026-02-26, Lite at ~4s
  generations since Jun 2026) — "already inside your chatbot" one-liners.
- **Midjourney: no slot** — V8.1 default since 2026-06-10, but Disney/Universal/WBD
  copyright suit in active discovery (Variety Jul 2026) → one-line legal-risk caveat only.
- **Stable Diffusion: no slot for this audience** (owner suggestion, demoted with
  rationale): still the leading open-weight image ecosystem, but that is an IT/developer
  use case — local installs/GPUs, no indemnification; Stability AI has pivoted to B2B
  media deals (EA partnership; $76M raise 2026-08-25 backed by Sony/Universal/Warner
  Music, EA, AMD — TechCrunch). One line at most: "the open-source option your IT
  department might run privately."

## App builders for non-coders (one slot)

**Lovable** — describe an app → working web app with database/login/hosting; 60M+ projects;
enterprise customers incl. Adidas, NVIDIA, Deutsche Telekom; ~$12B valuation talks
(Forbes 2026-06-05). Caveat: generated apps need security review before real company data.
Replit Agent 3 = runner-up; v0 is for front-end developers — skip.

## Voice & language (one shared slot)

**ElevenLabs** — $500M Series D at $11B (CNBC 2026-02-04); ~$600M ARR; used by 41% of the
Fortune 500 (Sacra). Office uses: narrated training modules, dubbing. Caveat: voice cloning
requires consent governance.
**DeepL** — Voice-to-Voice real-time spoken translation (2026-04-16, DeepL press); DeepL
Agent deployed by 2,000 customers for report analysis and legal work. Directly relevant to
regulated/multilingual document work.

## Video (one line)

Veo 3.1 (Oct 2025) remains Google's production flagship; Gemini Omni/Omni Flash announced
at I/O 2026-05-19. **Sora: OpenAI shut the standalone app 2026-04-26; API sunsets
2026-09-24; survives only inside ChatGPT** — the teachable line: tools die fast; don't
build processes on consumer apps. Runway Gen-4.5 = the pro-control choice.

## Checked, not recommended

- Vertical compliance/GRC AI (Drata, Vanta, Spellbook): too role-specific — spoken aside
  for the quality subgroup only.
- Browser agents: no change — ChatGPT Atlas shut down 2026-08-09 (validates existing
  Comet / Claude-in-Chrome picks).
- Enterprise agent platforms: covered by the Copilot entry. Context stat if wanted:
  Gartner — 40% of enterprise apps will embed task-specific agents by end-2026, up from
  <5% in 2025 (via Rasa blog).

## Find-more pointer (owner asked for "a link or prompt, without being overbearing")

**Recommended: a meta-prompt footer line, not a directory link** —
"Tools change monthly — ask your approved AI assistant: 'Search the web: what are the
current best tools for [my task], and which are enterprise-safe?'"
Rationale: reinforces the course's own skill; never goes stale (this research alone found
three headline tools renamed or killed within 12 months: NotebookLM → Gemini Notebook,
Sora shut down, Atlas shut down); directories (There's An AI For That ~50,000+ tools,
Futurepedia) are reputable but volume-driven, pay-to-submit marketing channels —
overwhelming for non-technical staff. Backup single link if the owner insists: There's An
AI For That, captioned "browse by task, verify with IT before use."

## UNVERIFIED (do not use without re-checking)

Lovable $400M Series C close at $13.3B (only June talks at ~$12B are Forbes-confirmed) ·
ElevenLabs $22B tender valuation · Zoom "ZoomMate" rebrand · TAAFT exact tool count (use
"50,000+") · Notion "21,000 custom agents in beta" · Perplexity $450M ARR (stats blog) ·
Manus GAIA scores · NotebookLM "Lecture" format · Sora $1M/day shutdown economics.
