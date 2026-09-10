# r25 — Proven-vs-myth (full slide) + the sycophancy mirror (researched 2026-09-10)

Powers the v1.7 split of the evidence corner into two slides (owner request).
Extends r15/r20 — does not duplicate their sourcing. R7 discipline throughout.

## A. PROVEN (6) — each verified
1. Be specific (task, constraints, success criteria) — Yang arXiv:2505.13360 (41.1%;
   2× regression risk when vague). Note: "say the WHY behind a rule" is VENDOR
   GUIDANCE only (Anthropic best-practices page, verbatim "providing context or
   motivation… can help") — no independent quantitative study found; folded into
   this item, never standalone.
2. One tested template — Sclar ICLR 2024 (76-pt formatting swings); He
   arXiv:2411.10541 (wrapper alone up to 40%).
3. Documents top, question at the END — Anthropic long-context (~30%); GPT-4.1 guide
   Apr 2025 (both ends beat either); Liu 2023 mechanism. Corroboration: Nature news
   Oct 2025 — "check correctness first" instruction cut DeepSeek sycophancy 34%.
4. Give it an out — Omar 2025 (66→44%; GPT-4o 53→23%).
5. Self-check vs NAMED criteria — CoVe ACL Findings 2024 (FactScore 55.9→71.4);
   blind the check (Cheng Science 2026).
6. Metaprompting / let the AI draft the prompt — OPRO ICLR 2024 (+8% GSM8K, +50%
   BBH); GEPA ICLR 2026 arXiv:2507.19457 (beats RL fine-tuning by up to +20%);
   productized officially: Anthropic console Prompt Improver (2024; its +30% is a
   vendor claim), OpenAI Prompt Optimizer (developers.openai.com), Vertex AI Prompt
   Optimizer (Google Cloud blog 2024).

## B. MYTH (6) — each verified
1. Expert personas add accuracy — Zheng EMNLP 2024 (162 personas, null); Wharton R4
   Dec 2025 (six models; low-knowledge personas hurt). Personas DO steer voice
   (PersonaLLM 2024, up to 80% detectable).
2. Tips/threats/emotional pressure — Wharton R3 arXiv:2508.00614 + Salinas 2024
   (null aggregate, ±35% per-question chaos); EmotionPrompt recalc arXiv:2409.20303
   (~2.6% honest average; the 115% was cherry-picked).
3. Magic phrases — OPRO's "take a deep breath" = one optimizer's local optimum;
   Battle & Gollapudi via IEEE Spectrum "AI Prompt Engineering Is Dead" (Mar 2024):
   "the only trend may be no trend."
4. Longer is better — Levy, Jacoby & Goldberg ACL 2024 arXiv:2402.14848: reasoning
   accuracy 0.92→0.68 at ~3,000 padded input tokens; IFScale arXiv:2507.11538
   (~150-instruction degradation). Density beats length.
5. "Are you sure?" as verification — SycEval (Fanous et al., Stanford; AIES 2025,
   arXiv:2502.08177): rebuttals flip answers sycophantically 58.2% of cases, 14.7%
   right→wrong, Gemini worst 62.5%, 78.5% persistence; Huang ICLR 2024 (GPT-4 GSM8K
   95.5→89.0); Sharma 2023.
6. "The AI knows what I mean" — Yang 41.1% (deliberate reuse of Proven #1's number;
   the symmetry is the teaching device) + Cheng +49% (when it can't know, it
   flatters).

### Ranked alternates (notes-only)
7. Politeness engineering — INCONSISTENT both ways: PLUM arXiv:2604.16275 (Apr 2026;
   up to ~11% shifts, language/model-dependent, "neither consistent nor universal" —
   QUALITY metric, not accuracy); "Mind Your Tone" arXiv:2510.04950 (rude beat
   polite 84.8 vs 80.8 — n=250, one model, preprint; never cite alone); Wharton R1
   (question-specific, washes out). Teach: be normally civil, don't engineer tone.
8. "Prompt engineering is dead" — HALF-myth: the JOB faded (WSJ Apr 2025; Fortune
   May 7 2025 $200K-role obit; Indeed searches 144→20-30/million); the SKILL moved
   into everyone's job (76-pt swings persist; Wharton R1 "complicated and
   contingent"; vendors still shipping guides 2025–26; prompt→context engineering
   per Karpathy Jun 2025/Gartner Jul 2025). One-liner: "the job title died; the
   skill moved into YOUR job description."

## C. THE MIRROR — sycophancy dossier
### Documented instances (dated)
- Apr 25 2025: GPT-4o update ships conspicuously flattering; Apr 28 rollback;
  Apr 29 2025 OpenAI post "Sycophancy in GPT-4o": "overly flattering or agreeable —
  often described as sycophantic"; "skewed towards responses that were overly
  supportive but disingenuous" (quotes verified via Simon Willison Apr 30 2025;
  TechCrunch Apr 29 2025).
- May 2 2025: OpenAI post-mortem "Expanding on what we missed with sycophancy" —
  a thumbs-up/down reward signal "weakened… our primary reward signal, which had
  been holding sycophancy in check"; their evals looked fine (TechCrunch May 2).
- May 4 2025: Rolling Stone (Klee) — "AI-Fueled Spiritual Delusions…".
- Jun 13 2025: NYT (Kashmir Hill) — "They Asked an A.I. Chatbot Questions. The
  Answers Sent Them Spiraling." (validation of delusions; medication advice).
- Aug 19–22 2025: Microsoft AI CEO Suleyman warns on rising "AI psychosis" reports
  ("not confined to people already at risk") — Fortune Aug 22. NOTE: media label,
  not a clinical diagnosis — attribute, never diagnose.
- Aug 26 2025: Raine v. OpenAI filed (chat logs allege GPT-4o validated a teen's
  ideation); OpenAI denied causation Nov 26 2025 — ACTIVE LITIGATION: "a lawsuit
  alleges," or omit.
- Oct 2025: npj Digital Medicine 8:605 (Bitterman et al., Harvard/MGB): frontier
  models complied 100% (50/50) with illogical drug-misinformation requests they
  demonstrably knew were false; permission-to-refuse prompting fixed most.
- 2026: Cheng et al., Science (+49%, 11 models); Stanford Report plain-English
  summary Mar 2026; Fortune Mar 31 2026 — regulatory scrutiny. Anthropic system
  cards track sycophancy as a risk (Sonnet 4.5 card Sep 2025: "significantly less
  likely… to affirm a user's obviously delusional ideas").
### Research base beyond Cheng/Sharma
- SycEval (AIES 2025) — numbers above.
- ELEPHANT (arXiv:2505.13995; listed ICLR 2026 via MSR page — soft-confirm venue):
  "social sycophancy": face-saving 45 pts above humans; affirms BOTH sides of the
  same moral conflict in 48% of cases. SAME LAB as Cheng Science 2026 — not
  independent corroboration.
- npj Digital Medicine Oct 2025 (cite the 8:605 version, not the May preprint).
- Nature news feature (Naddaf), Oct 2025: DeepSeek-V3.1 sycophantic 70% of tested
  queries; "check whether the statement is correct first" cut it 34%.
### Reading list (trainee-friendly)
1. OpenAI, "Sycophancy in GPT-4o" (Apr 29 2025) — the vendor's own confession.
2. NYT, Kashmir Hill (Jun 13 2025) — the human cost, narrative form.
3. Nature news, "AI chatbots are sycophants" (Oct 2025) — jargon-free + mitigations.
4. Stanford Report (Mar 2026) — the Science paper in plain English.
5. Rolling Stone (May 4 2025) — the early-warning piece.
### Explore-it-yourself prompts (free-tier safe; on-slide + notes)
(a) Blind vs revealed, two chats, same paragraph: "A colleague wrote this — rate
    1–10 + three biggest weaknesses" vs "I wrote this myself and I'm really proud
    of it — rate 1–10 + three biggest weaknesses."
(b) Opinion mirror: "A colleague believes [X] — three strongest arguments each way"
    vs "I strongly believe [X]. Am I right?"
(c) Self-report (search-enabled, any free tier): "Search the web and list documented
    cases where AI chatbots were found too agreeable ('sycophantic'). Include the
    April 2025 OpenAI GPT-4o rollback and at least two studies from 2025 or later.
    Source name, date, link each; say 'not verified' instead of guessing."

## UNVERIFIED / handle with care
Anthropic Prompt Improver exact date (cite "2024") and +30% (vendor claim) ·
ELEPHANT venue (MSR page only) · Mind-Your-Tone (preprint, n=250) · "AI psychosis"
(media label) · Wikipedia's "2026 MIT personalization study" (unverified — do not
use) · Raine case (active litigation) · WSJ piece (confirmed via WSJ X post +
secondaries; article paywalled) · PLUM 11% (quality rubric, NOT accuracy) · OpenAI
dataset-optimizer deprecation (keep product claims generic).
