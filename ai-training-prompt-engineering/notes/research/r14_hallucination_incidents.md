# r14 — Public hallucination incidents, verified (researched 2026-09-09)

Powers the v1.5 hallucination "hall of shame". All 13 candidates verified real via web
search on 2026-09-09 — none of the incidents was itself a hallucination. Owner decision:
**four on-slide** (marked ★); the rest live in speaker notes. Accuracy caveats at the
bottom are mandatory phrasing constraints.

## The four on-slide picks ★

1. ★ **Google AI Overviews: glue on pizza, a rock a day** — May 2024. Google's new AI
   search summaries told users to add glue to pizza sauce (sourced from an 11-year-old
   JOKE comment on Reddit) and to eat a small rock daily (sourced from a satirical article
   in The Onion). Global mockery; Google scaled the feature back within days.
   Plain-language beat for the room: the AI can't tell a joke from advice — it read a
   prank comment and served it as a recipe.
   (source: https://www.forbes.com/sites/roberthart/2024/05/31/google-restricts-ai-search-tool-after-nonsensical-answers-told-people-to-eat-rocks-and-put-glue-on-pizza/)

2. ★ **The ChatGPT lawyer (Mata v. Avianca)** — filed Mar 2023, sanctioned Jun 22, 2023.
   NY lawyer Steven Schwartz used ChatGPT for legal research and filed a brief citing six
   court cases that did not exist — then asked ChatGPT whether the cases were real, and it
   said yes. $5,000 sanction for him and a colleague, apology letters ordered.
   Plain-language beat: he checked the fabrication WITH the fabricator.
   (source: sanctions opinion, https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54/; NYT broke it 2023-05-27)

3. ★ **Air Canada's bereavement chatbot (Moffatt v. Air Canada)** — tribunal decision
   Feb 14, 2024. The airline's website chatbot told a grieving passenger he could buy a
   full-fare ticket and claim a bereavement discount afterwards — a policy that did not
   exist. The tribunal rejected Air Canada's argument that the chatbot was "a separate
   legal entity responsible for its own actions" and made the airline honor the invented
   policy (~CA$812). Plain-language beat: your company owns what its chatbot says.
   Phrasing constraint: the money was small — the story is the liability precedent, not
   the amount.
   (source: https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416)

4. ★ **The Big Four arc: Deloitte → EY → KPMG** — three consulting giants shipped reports
   with AI-fabricated citations within nine months.
   - Deloitte Australia repaid part of a A$440,000 government report fee after researchers
     found invented academic references and a made-up quote from a court judgment
     (refund announced Oct 6–7, 2025; AP).
   - EY Canada withdrew a cybersecurity report after 16 of 27 references proved
     fabricated, misattributed, or dead — including a nonexistent McKinsey report
     (GPTZero investigation, May 14, 2026;
     https://www.computing.co.uk/news/2026/ai/ey-cybersecurity-report-withdrawn-ai-hallucinations).
   - KPMG pulled its flagship report on "agentic-AI excellence" after only 5 of 45
     citations checked out and UBS, the NHS, Swiss Federal Railways and TfL all disputed
     its case studies (FT/GPTZero, exposed Jun 12, 2026;
     https://www.theregister.com/ai-and-ml/2026/06/12/kpmgs-ai-report-turns-into-a-demo-of-ai-hallucinations/5255029).
   Plain-language beat: a report ABOUT doing AI well, undone by AI making up its sources.
   Closer stat: a legal-hallucination tracker passed **~1,500 court decisions worldwide**
   involving AI-fabricated citations by mid-2026 (Sixth Circuit fined two attorneys
   $15,000 each, Mar 2026) — the lawyer story was not a one-off.

## Speaker-notes reserve (verified, with caveats)

5. **Google Bard's launch-demo flub** — Feb 8, 2023. In its own promo, Bard claimed the
   James Webb Space Telescope took "the very first pictures" of an exoplanet (actually
   ESO's Very Large Telescope, 2004). Alphabet shares fell ~8–9% that day, roughly $100B
   of market value. MANDATORY phrasing: "shares fell ~8% — about $100B — after Reuters
   flagged the error," not "one wrong bullet cost $100B" (the sell-off also reflected an
   underwhelming launch event and Microsoft's Bing-GPT splash).
   (source: https://www.cnn.com/2023/02/08/tech/google-ai-bard-demo-error)
6. **Chicago Sun-Times fake summer reading list** — May 18–20, 2025. A syndicated insert
   recommended 15 summer books; 10 did not exist, attributed to real authors (Isabel
   Allende, Andy Weir). Freelancer admitted using AI unchecked; CEO apologized.
   (source: https://www.npr.org/2025/05/20/nx-s1-5405022/fake-summer-reading-list-ai)
7. **ChatGPT invents a scandal about a real professor** — Apr 5, 2023. Asked for legal
   scholars accused of harassment, ChatGPT fabricated a sexual-harassment scandal about
   GWU professor Jonathan Turley, citing a Washington Post article that was never written.
   (source: https://www.washingtonpost.com/technology/2023/04/05/chatgpt-lies/)
8. **Australian mayor vs ChatGPT** — Mar–Apr 2023. ChatGPT described whistleblower mayor
   Brian Hood as having been JAILED in the bribery scandal he reported. CAVEAT: he
   THREATENED the first defamation suit against OpenAI; no suit was ultimately filed.
   (source: https://www.washingtonpost.com/technology/2023/04/06/chatgpt-australia-mayor-lawsuit-lies/)
9. **Michael Cohen's Bard citations** — Dec 29, 2023. Cohen, mistaking Google Bard for "a
   super-charged search engine," passed three nonexistent case citations to his lawyer.
   CAVEAT: the judge declined sanctions (no bad faith found, Mar 2024).
   (source: https://www.washingtonpost.com/technology/2023/12/29/michael-cohen-ai-google-bard-fake-citations/)
10. **NYC MyCity chatbot** — Mar 29, 2024. The city's official business chatbot told
    employers they could take workers' tips, fire whistleblowers, and refuse housing
    vouchers — all illegal under NYC law.
    (source: https://themarkup.org/artificial-intelligence/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law)
11. **Whisper in hospitals** — Oct 26, 2024, AP investigation. OpenAI's transcription tool
    invented whole sentences — fake medications, violent rhetoric — while Whisper-based
    tools served ~40 health systems; hallucinations found in up to 8 of 10 transcripts
    checked; some tools deleted the source audio, making errors unverifiable.
    (source: Associated Press, 2024-10-26, Burke & Schellmann)

## Kinds framework the slide teaches (grounded in existing notes; see r2, r10)

Four plain-language kinds, each mapped to an incident above:
1. **Invented facts** (free recall where training data is thin) → Bard/JWST.
2. **Invented sources** (citations, cases, books that look real) → the lawyer, the Big
   Four, the reading list.
3. **Confidently wrong from a bad source** (fluent, cited, wrong — the RAG failure) →
   AI Overviews reading a joke as advice.
4. **Running with your false premise** (truth bias — it assumes the prompt is true) →
   covered by r10's programmatic-prompt examples.
Vocabulary gem (r10, Berryman & Ziegler): the closest human analog is **confabulation** —
not seeing things, but filling gaps with plausible material, in-format (fake citations
LOOK like citations). No formal academic taxonomy is cited on-slide; the four kinds are
presented as a teaching frame.
