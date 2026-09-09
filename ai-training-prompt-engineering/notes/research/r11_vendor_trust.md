# r11 — Vendor trust, servers & data handling (researched 2026-09-09)

Powers the v1.5 redesign of the Part 2 security slide ("Who's who — and the rule that keeps
you safe") and the trust layer referenced from the assistants slide. Every fact carries a
source URL and a date. Facts in the UNVERIFIED section must not appear on a slide until
re-checked.

**Headline finding (confirmed across all seven Western vendors): trust tracks the TIER, not
the vendor.** Every vendor trains on consumer-tier conversations by default (opt-out
available) and none trains on business/enterprise-tier data by default. Every major 2025
privacy incident (indexed share links, court-ordered retention) hit consumer accounts.
Badge the tier the person is using, never the company logo.

## Anthropic (Claude)

1. Servers: traffic may route through the US, Europe, Asia, Australia; data ultimately
   **stored in the US**; no EU model hosting first-party
   (https://privacy.claude.com/en/articles/7996890, accessed 2026-09-09).
2. API data residency: per-request `inference_geo` = "us" (1.1x price) or "global";
   workspace storage geo currently US-only
   (https://platform.claude.com/docs/en/manage-claude/data-residency, accessed 2026-09-09).
3. EU/regional residency via cloud partners: AWS Bedrock, Google Vertex AI, Microsoft
   Foundry (https://claude.com/regional-compliance, accessed 2026-09-09).
4. Consumer training default flipped 2025-08-28: Free/Pro/Max chats used for training
   **unless the user opts out**; opted-in retention up to 5 years. Commercial terms
   (Work/Gov/Edu/API) excluded (https://www.anthropic.com/news/updates-to-our-consumer-terms).
5. Since 2026-06-09, frontier "covered models" carry a 30-day safety retention on every
   platform — including former zero-data-retention customers (retention, not training)
   (https://support.claude.com/en/articles/15425996). Enterprise-held-window rollout planned
   from fall 2026 (Bloomberg, 2026-08-20).
6. Certifications: SOC 2 Type I & II, ISO 27001:2022, ISO/IEC 42001:2023, HIPAA-ready
   configs with BAA (https://privacy.claude.com/en/articles/10015870; trust.anthropic.com).
7. FedRAMP High / DoD IL4-IL5 via Amazon Bedrock in AWS GovCloud (May 2025)
   (https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-bedrock-models-fedramp-high-dod-il-4-5-govcloud/).
8. No major user-data breach found 2025–26; trust events are policy-side (items 4–5).

## OpenAI (ChatGPT)

1. EU data residency for Enterprise/Edu/API since Feb 2025
   (https://openai.com/index/introducing-data-residency-in-europe/).
2. Residency worldwide for eligible business customers + **in-region GPU inference**
   (US or Europe) since Jan 2026
   (https://openai.com/index/expanding-data-residency-access-to-business-customers-worldwide/).
3. Consumer tiers: **no residency choice**; trained on by default, opt out via Settings →
   Data Controls (https://help.openai.com/en/articles/5722486). Business/Enterprise/Edu/API
   not trained on by default (https://openai.com/enterprise-privacy/).
4. Certifications: SOC 2 Type 2; ISO 27001/27017/27018/27701; HIPAA BAA on request
   (https://openai.com/security-and-privacy/). FedRAMP 20x Moderate for Enterprise + API,
   Apr 2026 (https://openai.com/index/openai-available-at-fedramp-moderate/). ChatGPT Gov
   since Jan 2025.
5. Incidents: Italy €15M GDPR fine (Dec 2024) **annulled on jurisdictional grounds
   2026-03-18 — cite both or neither** (https://www.wsgr.com/en/insights/openai-prevails-in-landmark-italian-ai-and-gdpr-enforcement-case.html).
   NYT-litigation preservation order (2025-05-13) retained even user-deleted consumer/API
   chats; lifted 2025-10-09; enterprise/ZDR excluded. ~4,500 "discoverable" shared chats
   surfaced in Google Search Jul–Aug 2025; feature killed. Mixpanel vendor breach Nov 2025
   (names/emails, no chats) (https://openai.com/index/mixpanel-incident/).

## Google (Gemini)

1. Consumer app: no residency; reviewed chats retained **up to 3 years**; even with
   activity off, 72-hour retention (https://support.google.com/gemini/answer/13594961).
   Consumer default: subset of chats may be human-reviewed and used for training; opt-out
   not retroactive.
2. Enterprise: Gemini Enterprise offers region-of-choice residency
   (https://docs.cloud.google.com/gemini/enterprise/docs/locations); Workspace-with-Gemini
   covered at rest and in processing (processing control needs Enterprise Plus / Data
   Regions add-on). Enterprise data not trained on, not human-reviewed
   (https://cloud.google.com/gemini-enterprise/faq).
3. Certifications: SOC 1/2/3, ISO 27001/27017/27018, ISO/IEC 42001; FedRAMP High for Gemini
   in Workspace (Oct 2024) and Vertex AI generative AI; HIPAA support announced Dec 2024
   (Workspace updates blog posts, Oct–Dec 2024).
4. No major Gemini-specific breach found 2025–26; the caveat is the consumer human-review /
   3-year default.

## Microsoft (Copilot / M365)

1. M365 Copilot honors M365 residency commitments and the **EU Data Boundary** (covered
   workload since 2024-03-01). **Caveat: Anthropic models offered inside Copilot are
   excluded from the EU Data Boundary**
   (https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy).
2. Enterprise: prompts/responses/Graph data not used to train foundation models; Entra ID
   sign-ins excluded from consumer training. Consumer Copilot (personal MSA): **trained on
   by default** since Oct 2024, opt-out in settings; six countries excluded
   (https://support.microsoft.com/en-us/microsoft-copilot/privacy-faq-for-microsoft-copilot).
3. Certifications: inherits M365 ISO 27001/17/18/701 + SOC 1/2/3; HIPAA BAA in scope (web
   queries to Bing fall outside); ISO/IEC 42001 certified for M365 Copilot (via Service
   Trust Portal compilation — re-verify on microsoft.com before slide use). GCC High GA
   Dec 2025 (FedRAMP High baseline).
4. Incident: **EchoLeak, CVE-2025-32711, CVSS 9.3** — zero-click prompt-injection
   exfiltration via a crafted email, patched server-side June 2025, no known exploitation
   (https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html). Teaching
   value: even green-tier enterprise AI carries novel attack surface.

## xAI (Grok)

1. Served from xAI's own **Colossus** data centers (Memphis TN / Southaven MS) — US infra;
   no published residency options (https://en.wikipedia.org/wiki/Colossus_(data_center)).
2. Consumer: X posts + Grok interactions used for training **by default** (opt-out in X
   privacy settings, TechCrunch 2024-07-26); app has "Private Chat" mode (30-day delete).
   API/business: not trained on; SOC 2 Type 2 (https://docs.x.ai/developers/faq/security).
3. Grok Business ($30/user/mo) + Enterprise since 2025-12-30 (SSO/SCIM, audit logs,
   Enterprise Vault) (https://x.ai/news/grok-business). No ISO/HIPAA/FedRAMP found.
4. Incidents (all verified): Feb 2025 system-prompt censorship episode; May 2025 "white
   genocide" insertions (rogue-employee explanation; system prompts now published on
   GitHub); **Jul 2025 "MechaHitler"** — ~16 hours of antisemitic output after a bad
   prompt update, public apology (https://www.cnbc.com/2025/05/15/,
   https://www.mediapost.com/publications/article/407435/); **Aug 2025: ~300–370K shared
   Grok chats indexed by Google** incl. personal details and at least one password
   (Forbes, 2025-08-20); Ireland DPC GDPR inquiry into EU-data training, Apr 2025.

## Perplexity

1. Hosted on AWS "in various locations worldwide"; no residency options published
   (https://www.perplexity.ai/hub/security). Aggregator note: answers may come from
   OpenAI/Anthropic models; Perplexity states providers may not train on its user data.
2. Consumer: training on queries **on by default**, opt-out toggle; Enterprise Pro: never
   trained on, ~7-day file retention; API: zero retention
   (https://docs.perplexity.ai/guides/privacy-security, accessed 2026-09-09).
3. SOC 2 Type II; "2025 HIPAA gap assessment" (NOT the same as a signable BAA — unconfirmed);
   no ISO 27001 or FedRAMP found.
4. Incident (reputation, not user data): Cloudflare accused Perplexity of stealth crawling
   evading no-crawl directives, de-listed it as a verified bot (Aug 2025); disputed.

## Chinese labs

1. Legal frame: PRC National Intelligence Law (2017) Art. 7 obliges any organization or
   citizen to assist state intelligence work
   (https://www.chinalawtranslate.com/en/national-intelligence-law-of-the-p-r-c-2017/).
2. Crucial nuance: the **open weights are a separate trust object from the China-hosted
   apps** — DeepSeek-R1 runs fully managed on Amazon Bedrock US regions and Azure AI
   Foundry with no data to China (AWS what's-new, Mar 2025). "The app, not the model, is
   the risk."
3. **DeepSeek**: privacy policy (updated 2026-02-10) states data is collected, processed
   and **stored in the People's Republic of China**; used to train unless you opt out by
   email (https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html). Italy's
   Garante blocked it 2025-01-30 (not reported lifted); South Korea pulled the app Feb 2025
   (returned ~2 months later); US Navy/NASA/Australia/Taiwan government bans. Jan 2025 Wiz
   Research found exposed databases with 1M+ log entries incl. plaintext chats and API keys
   (https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak). No
   enterprise tier or Western certifications found.
4. **Alibaba/Qwen**: enterprise route via Alibaba Cloud Model Studio — regions incl.
   Singapore, US (Virginia), Frankfurt, Tokyo; "never uses your data for model training";
   SOC 2 report (https://www.alibabacloud.com/help/en/model-studio/privacy-notice).
   Consumer Qwen Chat: broad content-use terms, no documented in-product opt-out.
5. **Moonshot/Kimi**: policy states storage "within the People's Republic of China";
   content may be used to optimize models; opt-out only via customer service
   (https://www.kimi.com/user/agreement/userPrivacy?version=v2, accessed 2026-09-09).
6. **Zhipu/Z.ai**: international service operated from Singapore; API prompts/outputs "not
   stored"; parent added to the **US Entity List 2025-01-16**
   (https://docs.z.ai/legal-agreement/privacy-policy; SCMP 2025-01-16).

## Recommended 3-tier trust framing (badge the tier, not the vendor)

- **TIER 1 — Company tenant (green)**: approved for work data within policy. M365 Copilot /
  EDP, ChatGPT Enterprise/Business, Claude for Work, Gemini Workspace/Enterprise, Grok
  Business/Enterprise, Perplexity Enterprise Pro. Common floor: no training by default,
  SOC 2 Type II (all seven), DPAs, admin controls. Residency strength varies: strong
  (OpenAI/Google/Microsoft), US-first-party-only (Anthropic — EU via cloud partners), none
  published (xAI, Perplexity).
- **TIER 2 — Personal account, reputable vendor (yellow)**: public/non-sensitive material
  only. Default training on chats (all vendors), possible human review (Google), long
  retention (Anthropic 5y opted-in, Google 3y reviewed), share-link leak history (OpenAI,
  xAI), litigation holds can outlive the delete button (OpenAI/NYT).
- **TIER 3 — China-hosted consumer apps (red)**: no company data, ever. DeepSeek app/API,
  Kimi, consumer Qwen; Z.ai borderline (Singapore processing, Entity-List parent).

Pitfalls to state: residency ≠ sovereignty (US orders reach EU-resident data; Copilot's
Claude option sits outside the EU boundary) · certifications ≠ your compliance (mis-scoped
deployments) · green ≠ invulnerable (EchoLeak) · defaults drift (Anthropic flipped Aug
2025; Microsoft Oct 2024; DeepSeek re-dated Feb 2026) — date-stamp and refresh quarterly.

## UNVERIFIED (do not use without re-checking)

- Anthropic first-party FedRAMP High listing (only Bedrock GovCloud route is solid).
- OpenAI ISO 42001. xAI ISO 27001/42001/HIPAA/FedRAMP (none found). Perplexity signable
  HIPAA BAA. Perplexity/xAI residency (absence-of-evidence only).
- Qwen consumer-app operating entity / exact server location (enterprise Model Studio facts
  are solid). Moonshot international API platform data handling.
- Microsoft ISO 42001 for M365 Copilot (consultancy compilation, not microsoft.com direct).
- DeepSeek in-app opt-out toggle (email right is verified; toggle is not).
