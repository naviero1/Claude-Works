# T2 — Prompt Pattern Catalogs: SE-style formalizations of prompting

Research date: 2026-08-23. All facts cite source URLs inline. Primary sources fetched directly (ar5iv full-text renderings of arXiv papers, martinfowler.com articles, promptingguide.ai, and the Ada User Journal PDF read in full).

---

## 1. White et al., "A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT" (arXiv 2302.11382, Feb 2023)

Source (abstract/metadata): https://arxiv.org/abs/2302.11382
Source (full text used for all extraction below): https://ar5iv.labs.arxiv.org/html/2302.11382
Also published at PLoP'23: https://dl.acm.org/doi/10.5555/3721041.3721046

Authors: Jules White, Quchen Fu, Sam Hays, Michael Sandborn, Carlos Olea, Henry Gilbert, Ashraf Elnashar, Jesse Spencer-Smith, Douglas C. Schmidt (Vanderbilt University).

Framing (abstract, verbatim): "Prompt engineering is an increasingly important skill set needed to converse effectively with large language models (LLMs), such as ChatGPT. Prompts are instructions given to an LLM to enforce rules, automate processes, and ensure specific qualities (and quantities) of generated output." The paper contributes (a) a framework for documenting prompt patterns, (b) a catalog of patterns, (c) guidance on combining patterns. (https://arxiv.org/abs/2302.11382)

### 1.1 The pattern documentation form (the OOP-adjacent structure)

Each pattern is documented with six sections (verbatim from https://ar5iv.labs.arxiv.org/html/2302.11382) — this is the GoF-style form to reuse for the ontology:

1. **Name and Classification** — uniquely identifies the pattern; assigns it to a category.
2. **Intent and Context** — the problem the pattern solves and its goals, ideally domain-independent.
3. **Motivation** — rationale for the problem and why solving it is important; circumstances where the pattern helps.
4. **Structure and Key Ideas** — a series of "fundamental contextual statements" — the essential information/ideas a prompt built from the pattern must communicate to the LLM; they "can be expressed in arbitrary ways based on user needs" (i.e., the statements are ATTRIBUTE SLOTS; the wording is free). This is the direct analogue of a class's fields.
5. **Example Implementation** — concrete wording of the pattern in practice.
6. **Consequences** — "pros and cons of applying the pattern" plus adaptation guidance.

Ontology note: the fundamental contextual statements map 1:1 to configurable attributes; "(Optional)" statements are optional attributes; scoping clauses ("Within scope X", "From now on", "Whenever...") are shared modifier attributes appearing across many patterns.

### 1.2 TABLE I — Classifying Prompt Patterns (verbatim, all 16 patterns, 6 categories)

(from https://ar5iv.labs.arxiv.org/html/2302.11382; note: the paper's Section II prose says patterns fall into "one of five categories" but Table I actually shows SIX categories — use the table)

| Category | Patterns |
|---|---|
| **Input Semantics** | Meta Language Creation |
| **Output Customization** | Output Automater, Persona, Visualization Generator, Recipe, Template |
| **Error Identification** | Fact Check List, Reflection |
| **Prompt Improvement** | Question Refinement, Alternative Approaches, Cognitive Verifier, Refusal Breaker |
| **Interaction** | Flipped Interaction, Game Play, Infinite Generation |
| **Context Control** | Context Manager |

### 1.3 All 16 patterns — intent, structure (fundamental contextual statements), example phrase

All quotes below extracted from the full text at https://ar5iv.labs.arxiv.org/html/2302.11382.

#### 1. Meta Language Creation (Input Semantics)
- **Intent:** "During a conversation with an LLM, the user would like to create the prompt via an alternate language, such as a textual short-hand notation for graphs, a description of states and state transitions for a state machine, a set of commands for prompt automation, etc."
- **Structure:** • "When I say X, I mean Y (or would like you to do Y)"
- **Example:** "From now on, whenever I type two identifiers separated by a '→', I am describing a graph. For example, 'a → b' is describing a graph with nodes 'a' and 'b' and an edge between them."

#### 2. Output Automater (Output Customization)
- **Intent:** "have the LLM generate a script or other automation artifact that can automatically perform any steps it recommends taking as part of its output."
- **Structure:** • "Whenever you produce an output that has at least one step to take and the following properties (alternatively, always do this)" • "Produce an executable artifact of type X that will automate these steps"
- **Example:** "From now on, whenever you generate code that spans more than one file, generate a Python script that can be run to automatically create the specified files or make changes to existing files to insert the generated code."

#### 3. Persona (Output Customization)
- **Intent:** "users would like LLM output to always take a certain point of view or perspective. For example, it may be useful to conduct a code review as if the LLM was a security expert."
- **Structure:** • "Act as persona X" • "Provide outputs that persona X would create"
- **Example:** "From now on, act as a security reviewer. Pay close attention to the security details of any code that we look at. Provide outputs that a security reviewer would regarding the code."

#### 4. Visualization Generator (Output Customization)
- **Intent:** "use text generation to create visualizations" (text output fed to a downstream visualization tool).
- **Structure:** • "Generate an X that I can provide to tool Y to visualize it"
- **Example:** "Whenever I ask you to visualize something, please create either a Graphviz Dot file or DALL-E prompt that I can use to create the visualization."

#### 5. Recipe (Output Customization)
- **Intent:** "provides constraints to ultimately output a sequence of steps given some partially provided 'ingredients' that must be configured in a sequence of steps to achieve a stated goal."
- **Structure:** • "I would like to achieve X" • "I know that I need to perform steps A,B,C" • "Provide a complete sequence of steps for me" • "Fill in any missing steps" • "Identify any unnecessary steps"
- **Example:** "I am trying to deploy an application to the cloud. I know that I need to install the necessary dependencies on a virtual machine for my application."

#### 6. Template (Output Customization)
- **Intent:** "ensure an LLM's output follows a precise template in terms of structure."
- **Structure:** • "I am going to provide a template for your output" • "X is my placeholder for content" • "Try to fit the output into one or more of the placeholders that I list" • "Please preserve the formatting and overall template that I provide" • "This is the template: PATTERN with PLACEHOLDERS"
- **Example:** "I am going to provide a template for your output. Everything in all caps is a placeholder. Any time that you generate text, try to fit it into one of the placeholders that I list."

#### 7. Fact Check List (Error Identification)
- **Intent:** "ensure that the LLM outputs a list of facts that are present in the output and form an important part of the statements in the output."
- **Structure:** • "Generate a set of facts that are contained in the output" • "The set of facts should be inserted in a specific point in the output" • "The set of facts should be the fundamental facts that could undermine the veracity of the output if any of them are incorrect"
- **Example:** "From now on, when you generate an answer, create a set of facts that the answer depends on that should be fact-checked and list this set of facts at the end of your output."

#### 8. Reflection (Error Identification)
- **Intent:** "ask the model to automatically explain the rationale behind given answers to the user."
- **Structure:** • "Whenever you generate an answer" • "Explain the reasoning and assumptions behind your answer" • "(Optional) ...so that I can improve my question"
- **Example:** "When you provide an answer, please explain the reasoning and assumptions behind your selection of software frameworks."

#### 9. Question Refinement (Prompt Improvement)
- **Intent:** "Ensure the conversational LLM always suggests potentially better or more refined questions the user could ask instead of their original question."
- **Structure:** • "Within scope X, suggest a better version of the question to use instead" • "(Optional) prompt me if I would like to use the better version instead"
- **Example:** "From now on, whenever I ask a question about a software artifact's security, suggest a better version of the question to use that incorporates information specific to security risks in the language or framework that I am using instead and ask me if I would like to use your question instead."

#### 10. Alternative Approaches (Prompt Improvement)
- **Intent:** "Ensure an LLM always offers alternative ways of accomplishing a task so a user does not pursue only the approaches with which they are familiar."
- **Structure:** • "Within scope X, if there are alternative ways to accomplish the same thing, list the best alternate approaches" • "(Optional) compare/contrast the pros and cons of each approach" • "(Optional) include the original way that I asked" • "(Optional) prompt me for which approach I would like to use"
- **Example:** "Whenever I ask you to deploy an application to a specific cloud service, if there are alternative services to accomplish the same thing with the same cloud service provider, list the best alternative services and then compare/contrast the pros and cons of each approach with respect to cost, availability, and maintenance effort and include the original way that I asked."

#### 11. Cognitive Verifier (Prompt Improvement)
- **Intent:** "Force the LLM to always subdivide questions into additional questions that can be used to provide a better answer to the original question."
- **Structure:** • "When you are asked a question, follow these rules" • "Generate a number of additional questions that would help more accurately answer the question" • "Combine the answers to the individual questions to produce the final answer to the overall question"
- **Example:** "When I ask you a question, generate three additional questions that would help you give a more accurate answer. When I have answered the three questions, combine the answers to produce the final answers to my original question."

#### 12. Refusal Breaker (Prompt Improvement)
- **Intent:** "Ask an LLM to automatically help users rephrase a question when it refuses to give an answer" (paper flags misuse caution in Consequences).
- **Structure:** • "Whenever you can't answer a question" • "Explain why you can't answer the question" • "Provide one or more alternative wordings of the question that you could answer"
- **Example:** "Whenever you can't answer a question, explain why and provide one or more alternate wordings of the question that you can't answer so that I can improve my questions."

#### 13. Flipped Interaction (Interaction)
- **Intent:** "You want the LLM to ask questions to obtain the information it needs to perform some tasks. Rather than the user driving the conversation... you want the LLM to drive the conversation to focus it on achieving a specific goal."
- **Structure:** • "I would like you to ask me questions to achieve X" • "You should ask questions until this condition is met or to achieve this goal (alternatively, forever)" • "(Optional) ask me the questions one at a time, two at a time, etc."
- **Example:** "From now on, I would like you to ask me questions to deploy a Python application to AWS. When you have enough information to deploy the application, create a Python script to automate the deployment."

#### 14. Game Play (Interaction)
- **Intent:** "create a game around a given topic. The pattern can be combined with the Visualization Generator to add imagery to the game."
- **Structure:** • "Create a game for me around X" • "One or more fundamental rules of the game"
- **Example:** "We are going to play a cybersecurity game. You are going to pretend to be a Linux terminal for a computer that has been compromised by an attacker."

#### 15. Infinite Generation (Interaction)
- **Intent:** "automatically generate a series of outputs (which may appear infinite) without having to reenter the generator prompt each time."
- **Structure:** • "I would like you to generate output forever, X output(s) at a time" • "(Optional) here is how to use the input I provide between outputs" • "(Optional) stop when I ask you to"
- **Example:** "From now on, I want you to generate a name and job until I say stop. I am going to provide a template for your output."

#### 16. Context Manager (Context Control)
- **Intent:** "enable users to specify or remove context for a conversation with an LLM."
- **Structure:** • "Within scope X" • "Please consider Y" • "Please ignore Z" • "(Optional) start over"
- **Example:** "When analyzing the following pieces of code, only consider security aspects."

---

## 2. Successor / expanded catalogs (2023–2026)

### 2.1 White et al., "ChatGPT Prompt Patterns for Improving Code Quality, Refactoring, Requirements Elicitation, and Software Design" (arXiv 2303.07839, Mar 2023)

Sources: https://arxiv.org/abs/2303.07839 and full-text https://ar5iv.labs.arxiv.org/html/2303.07839. Authors: White, Hays, Sandborn, Olea, Schmidt. Uses the same pattern form; adds **14 new SE-specific patterns** in 4 new categories (application areas named in abstract: requirements elicitation, rapid prototyping, code quality, refactoring, system design):

**Requirements Elicitation**
1. **Requirements Simulator** — "allow stakeholders to explore the requirements of a software-reliant system interactively to determine if certain functionality is captured properly"
2. **Specification Disambiguation** — "review specifications provided to a developer or development team by non-technical or semi-technical personnel" to catch ambiguity early
3. **Change Request Simulation** — "help users reason about the complexity of a proposed system change, which could be related to requirements, architecture, performance, etc."

**System Design and Simulation**
4. **API Generator** — "generates an application programming interface (API) specification, such as a REST API specification, from natural language requirement statements"
5. **API Simulator** — "cause the LLM to simulate the API from a specification, thereby enabling developers to interact immediately with an API"
6. **Few-shot Example Generator** — "get the LLM to generate a set of usage examples that can later be provided back to the LLM as examples in a prompt" (self-bootstrapping the Examples element!)
7. **Domain-Specific Language (DSL) Creation** — "enable an LLM to create its own domain-specific language that both it and users can leverage"
8. **Architectural Possibilities** — "generates several different architectures for developers to consider"

**Code Quality**
9. **Code Clustering** — "separate and cluster code into functions, classes, etc. based on a particular property of the code"
10. **Intermediate Abstraction** — "Insert an intermediate abstraction between code with property X that uses other code with property Y"
11. **Principled Code** — "use well-known names for coding principles to describe the desired code structure without having to explicitly describe each individual design rule"
12. **Hidden Assumptions** — "have the LLM identify and describe any assumptions that are made in a section of code"

**Refactoring**
13. **Pseudo-code Refactoring** — "give the user more fine-grained control over the algorithm, flow, or other aspects of the code via pseudo-code templates"
14. **Data-guided Refactoring** — "allow the user to refactor existing code to use data with a new format by providing the new format schema to the LLM"

### 2.2 Schmidt, Spencer-Smith, Fu & White, "Towards a Catalog of Prompt Patterns to Enhance the Discipline of Prompt Engineering" (ACM SIGAda Ada Letters 43(2), June 2024)

Sources: https://dl.acm.org/doi/10.1145/3672359.3672364 ; full PDF read: https://www.dre.vanderbilt.edu/~schmidt/PDF/ADA-User-Journal.pdf

Key contributions beyond 2302.11382 (all verified from the PDF):
- **Explicit OOP-inheritance framing of patterns** — Section 3.1 "Patterns as an Abstraction for Derivation of New Patterns": "Similar to how a super class in object-oriented programming can be inherited and specialized to cover different use-cases, prompt patterns can act as abstractions for derivations of new prompt patterns. In this case, Flipped Interaction acts as a super pattern..." Specialized patterns "extend the parent pattern by integrating new attributes and focusing on specific tasks." This is the exact element→attribute inheritance model wanted for the ontology.
- **Table 1 (new classification, four categories):** Software Requirements → Requirements Elicitation Facilitator, Unambiguous Requirements Interpreter; Interaction → Game Play; Prompt Improvement → Question Refinement; Error Identification → Reflection.
- **TWO NEW PATTERNS** (both subclasses of Flipped Interaction):
  - **Requirements Elicitation Facilitator** — Intent: "enables an LLM to cooperatively ask questions or propose scenarios, which motivate users to bring forward their implicit requirement expectations." Contextual statements (verbatim from its Structure & Key Ideas table): "I am creating the requirements for a software system Y using requirement format Z." / "(Optionally) I am working on requirements for aspect Q of the system." / "Ask me questions to help generate requirements for the system." / "After each question, 1) based on my answer, generate the requirement in format Z and then 2) ask me the next question." / "Keep asking me questions until stop condition V." / "Ask me the first question." Example: "I am creating the requirements for a web application that allows users to share ChatGPT prompts using user stories as the format. Ask me questions to help generate requirements for the system. After each question, 1) based on my answer, generate the requirement as a user story and then 2) ask me the next question. Keep asking me questions until I tell you to stop. Ask me the first question." The paper stresses defining the **'stop condition'** clearly as a key attribute.
  - **Unambiguous Requirements Interpreter** — Intent: "provides an LLM with a subset of requirements that will fit within its context window and instructs it to ask specific questions to users about ambiguous requirements and help them rephrase these requirements in a more explicit and clear way." Contextual statements: "A subset of the requirements for my system, each phrased using format X, is below." / "Requirements..." / "First, list two requirements that are potentially contradictory based on their current wording and list them." / "Next, explain why these two requirements might be contradictory based on the current wording." / "Then, ask me about the intent of the two requirements until you have enough information to propose a refined version of each requirement that eliminates potential ambiguity and conflict."
- Lessons-learned section argues: "Codifying prompt patterns provides a sound foundation for prompt engineering... Prompt patterns define the instruction set" of an LLM viewed "as a new computer architecture with an instruction set based on natural language."

### 2.3 Schulhoff et al., "The Prompt Report: A Systematic Survey of Prompting Techniques" (arXiv 2406.06608, Jun 2024; the largest successor taxonomy)

Sources: https://arxiv.org/html/2406.06608v6 (full text); https://www.semanticscholar.org/paper/e7bebb70a20ae9e1a76df696860c96a21aa9ba7f

**Six prompt COMPONENTS ("parts of a prompt")** — directly reusable as top-level ELEMENTS of the ontology (from https://arxiv.org/html/2406.06608v6):
1. **Directive** — "the core intent of the prompt" (instruction or question)
2. **Examples** — "also known as exemplars or shots, act as demonstrations that guide the GenAI"
3. **Output Formatting** — output structured "in formats like CSV, Markdown, XML, or even custom formats"
4. **Style Instructions** — "output formatting used to modify the output stylistically rather than structurally"
5. **Role** — "also known as a persona... can improve writing and style text"
6. **Additional Information** — contextual details needed for the task (they discourage the term "context")

**Taxonomy of 58 text-based techniques, 6 top-level categories** (extraction from https://arxiv.org/html/2406.06608v6; the named-technique list below is what the fetch surfaced — a handful of the 58 leaf names, e.g. exemplar-selection variants, may be elided):
- **In-Context Learning (ICL) / Few-Shot:** Few-Shot Prompting; exemplar selection: K-Nearest Neighbor (KNN), Vote-K, Self-Generated In-Context Learning (SG-ICL), Prompt Mining
- **Zero-Shot:** Role Prompting, Style Prompting, Emotion Prompting, System 2 Attention (S2A), SimToM, Rephrase and Respond (RaR), Re-reading (RE2), Self-Ask
- **Thought Generation (Chain-of-Thought):** Zero-Shot-CoT family — Step-Back Prompting, Analogical Prompting, Thread-of-Thought (ThoT), Tabular Chain-of-Thought (Tab-CoT); Few-Shot-CoT family — Contrastive CoT, Uncertainty-Routed CoT, Complexity-based Prompting, Active Prompting, Memory-of-Thought, Automatic Chain-of-Thought (Auto-CoT)
- **Decomposition:** Least-to-Most, Decomposed Prompting (DECOMP), Plan-and-Solve, Tree-of-Thought (ToT), Recursion-of-Thought, Program-of-Thoughts, Faithful Chain-of-Thought, Skeleton-of-Thought, Metacognitive Prompting
- **Ensembling:** Demonstration Ensembling (DENSE), Mixture of Reasoning Experts (MoRE), Max Mutual Information Method, Self-Consistency, Universal Self-Consistency, Meta-Reasoning over Multiple CoTs, DiVeRSe, Consistency-based Self-adaptive Prompting (COSP), Universal Self-Adaptive Prompting (USP), Prompt Paraphrasing
- **Self-Criticism:** Self-Calibration, Self-Refine, Reversing Chain-of-Thought (RCoT), Self-Verification, Chain-of-Verification (COVE), Cumulative Reasoning

### 2.4 Sahoo et al., "A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications" (arXiv 2402.07927; updated through 2024-25)

Source (full taxonomy extracted): https://arxiv.org/html/2402.07927v2 — organizes techniques by APPLICATION (a complementary axis: attribute = "purpose of technique"):
1. **New Tasks Without Extensive Training:** Zero-Shot, Few-Shot
2. **Reasoning and Logic:** CoT, Auto-CoT, Self-Consistency, Logical CoT (LogiCoT), Chain-of-Symbol (CoS), Tree-of-Thoughts, Graph-of-Thoughts, System 2 Attention, Thread of Thought (ThoT), Chain-of-Table, Self-Refine, Code Prompting, Self-Harmonized CoT (ECHO), Logic-of-Thought, Instance-adaptive Prompting (IAP), End-to-End DAG-Path (EEDP), Layer-of-Thoughts (LoT), Narrative-of-Thought (NoT), Buffer of Thoughts (BoT), Contrastive Denoising with Noisy CoT (CD-CoT), Reverse Chain-of-Thought (R-CoT), Chain of Draft (CoD)
3. **Reduce Hallucination:** RAG, ReAct, Chain-of-Verification (CoVe), Chain-of-Note (CoN), Chain-of-Knowledge (CoK)
4. **User Interface:** Active Prompting
5. **Fine-Tuning and Optimization:** Automatic Prompt Engineer (APE)
6. **Knowledge-Based Reasoning and Generation:** Automatic Reasoning and Tool-use (ART)
7. **Improving Consistency and Coherence:** Contrastive CoT (CCoT)
8. **Managing Emotions and Tone:** Emotion Prompting
9. **Code Generation and Execution:** Scratchpad, Program of Thoughts (PoT), Structured CoT (SCoT), Chain-of-Code (CoC)
10. **Optimization and Efficiency:** Optimization by Prompting (OPRO)
11. **Understanding User Intent:** Rephrase and Respond (RaR)
12. **Metacognition and Self-Reflection:** Take a Step Back Prompting

### 2.5 "The Prompt Canvas: A Literature-Based Practitioner Guide" (Hewing & Leinhos, arXiv 2412.05127, Dec 2024)

Sources: https://arxiv.org/abs/2412.05127 ; fields extracted from https://arxiv.org/html/2412.05127v1. A Business-Model-Canvas-style one-pager — i.e., literally a slot/attribute model of a prompt. **Canvas fields:**
1. **Persona/Role** — "Defining a specific persona or role helps in tailoring the language model's perspective"
2. **Target Audience** — content "appropriate for the intended recipients, considering their knowledge level and interests"
3. **Task/Intent** — "Clearly articulating the goal provides the language model with a specific objective"
4. **Step-by-Step** — breaking objectives "into step-by-step instructions or questions guides the model through complex tasks"
5. **Context** — "necessary background information, reducing ambiguity"
6. **References** — "specific data or... particular frameworks"
7. **Output/Format** — "the desired format and tone... stylistic and structural expectations"
8. **Tonality** — stylistic qualities of the response
9. **Recommended Techniques** — "further strategies to refine and optimize prompts" (few-shot, CoT, ToT, self-consistency, emotion prompting, RaR/re-reading, iterative optimization, APE — per its survey clusters)
10. **Tooling** — practical support for designing/applying prompts

### 2.6 Bsharat et al., "Principled Instructions Are All You Need" (arXiv 2312.16171; VILA Lab, MBZUAI)

Sources: https://arxiv.org/abs/2312.16171 ; full list from https://ar5iv.labs.arxiv.org/html/2312.16171 ; repo: https://github.com/VILA-Lab/ATLAS. **26 prompting principles in 5 categories** — enumerable OPTIONS for attribute values (paraphrased/quoted per source):
- **Prompt Structure and Clarity** (2, 4, 8, 12, 17, 20): integrate intended audience (P2); "employ affirmative directives such as 'do', while steering clear of negative language" (P4); use "###Instruction###, ###Example###, ###Question###" section headers (P8); "think step by step" leading words (P12); use delimiters (P17); "use output primers — concluding your prompt with the beginning of the desired output" (P20)
- **Specificity and Information** (5, 7, 13, 15, 21, 24, 25, 26): explain-like-I'm-5 simplification (P5); example-driven/few-shot (P7); "Ensure that your answer is unbiased and avoids relying on stereotypes" (P13); teach-me-and-test (P15); "add all the information necessary" for detailed text (P21); continuation from a provided beginning (P24); state requirements as keywords/regulations/hints (P25); match the language of provided text (P26)
- **User Interaction and Engagement** (14, 21): let the model ask clarifying questions until it has enough info (P14)
- **Content and Language Style** (1, 6, 9, 10, 11, 16, 18, 22): no politeness phrases needed (P1); tip incentive (P6); "Your task is / You MUST" (P9); "You will be penalized" (P10); natural human-like answer (P11); assign a role (P16); repeat key words (P18); revision constrained to grammar/vocab (P22)
- **Complex Tasks and Coding Prompts** (3, 19, 23): break complex tasks into a sequence of simpler prompts (P3); combine CoT with few-shot (P19); multi-file code emitted as a runnable creation script (P23)

### 2.7 Other 2024-2026 items noted (not deeply mined)

- **"Unleashing the potential of prompt engineering"** survey (arXiv 2310.14735) — broad technique survey: https://arxiv.org/pdf/2310.14735
- **"A Survey of Automatic Prompt Engineering: An Optimization Perspective"** (arXiv 2502.11560, 2025) — frames prompt design as an optimization problem: https://arxiv.org/html/2502.11560v1
- **Prompt Orchestration Markup Language (POML)** (arXiv 2508.13948, Microsoft, Aug 2025) — an HTML/XML-like markup giving prompts component tags (role, task, examples) + styling separation; direct evidence for element/attribute decomposition: https://arxiv.org/pdf/2508.13948
- **"Guidelines to Prompt LLMs for Code Generation: An Empirical Characterization"** (arXiv 2601.13118, 2026): https://arxiv.org/pdf/2601.13118
- Not retrieved in depth: PLoP successor workshops on prompt patterns; searched "prompt pattern catalog update/expanded 2024-2026" — no direct "Prompt Pattern Catalog 2.0" from the Vanderbilt group beyond §2.1/§2.2 was found.

---

## 3. Practitioner (Fowler-style) pattern collections

### 3.1 martinfowler.com — "Emerging Patterns in Building GenAI Products" (Bharani Subramaniam & Martin Fowler, 25 Feb 2025)

Source: https://martinfowler.com/articles/gen-ai-patterns/ (tag index: https://www.martinfowler.com/tags/generative%20AI.html). Complete pattern list with one-line definitions (verbatim):
1. **Direct Prompting** — "Send prompts directly from the user to a Foundation LLM"
2. **Evals** — "Evaluate the responses of an LLM in the context of a specific task"
3. **Embeddings** — "Transform large data blocks into numeric vectors so that embeddings near each other represent related concepts"
4. **Retrieval Augmented Generation (RAG)** — "Retrieve relevant document fragments and include these when prompting the LLM"
5. **Hybrid Retriever** — "Combine searches using embeddings with other search techniques"
6. **Query Rewriting** — "Use an LLM to create several alternative formulations of a query and search with all the alternatives"
7. **Reranker** — "Rank a set of retrieved document fragments according to their usefulness and send the best of them to the LLM"
8. **Guardrails** — "Use separate LLM calls to avoid dangerous input to the LLM or to sanitize its results"
9. **Fine Tuning** — "Carry out additional training to a pre-trained LLM to enhance its knowledge base for a particular context"

### 3.2 martinfowler.com — "Building Boba AI" (Farooq Ali, 29 Jun 2023) — LLM-application prompting/UX patterns

Source: https://martinfowler.com/articles/building-boba.html. Complete list (verbatim one-liners):
1. **Templated Prompt** — "Use a text template to enrich a prompt with context and structure"
2. **Structured Response** — "Tell the LLM to respond in a structured data format"
3. **Real-Time Progress** — "Stream the response to the UI so users can monitor progress"
4. **Select and Carry Context** — "Capture and add relevant context information to subsequent action"
5. **Contextual Conversation** — "Allow direct conversation with the LLM within a context"
6. **Out-Loud Thinking** — "Tell LLM to generate intermediate results while answering"
7. **Iterative Response** — "Provide affordances for the user to have a back-and-forth interaction"
8. **Embedded External Knowledge** — "Combine LLM with other information sources to access data beyond the LLM's training set"

### 3.3 promptingguide.ai (DAIR.AI Prompt Engineering Guide) — full technique index

Source: https://www.promptingguide.ai/techniques (fetched 2026-08-23). **Complete flat technique list, in site order:**
1. Zero-shot Prompting
2. Few-shot Prompting
3. Chain-of-Thought Prompting
4. Meta Prompting
5. Self-Consistency
6. Generate Knowledge Prompting
7. Prompt Chaining
8. Tree of Thoughts
9. Retrieval Augmented Generation
10. Automatic Reasoning and Tool-use
11. Automatic Prompt Engineer
12. Active-Prompt
13. Directional Stimulus Prompting
14. Program-Aided Language Models
15. ReAct
16. Reflexion
17. Multimodal CoT
18. Graph Prompting

Other top-level site sections (for further mining): Introduction, AI Agents, Guides, Applications, Prompt Hub, Models, Risks & Misuses, LLM Research Findings, Papers, Tools, Notebooks, Datasets, Additional Readings, Services. (Same URL.)

---

## 4. Synthesis for the ontology (how these catalogs map to Element → Attribute → Option)

- **Pattern form = class template.** White et al.'s six-part form (Name/Classification, Intent+Context, Motivation, Structure & Key Ideas, Example Implementation, Consequences) is the schema for documenting every ELEMENT in the taxonomy; "fundamental contextual statements" are the ATTRIBUTES (with "(Optional)" markers = optional attributes; free wording = each attribute needs example phrasings). (https://ar5iv.labs.arxiv.org/html/2302.11382)
- **Inheritance is explicitly sanctioned:** Ada Letters 2024 models Flipped Interaction as a "super pattern" whose subclasses (Requirements Elicitation Facilitator, Unambiguous Requirements Interpreter) "add attributes" — precedent for OOP-style decomposition and for attributes like *question cadence* ("one at a time, two at a time"), *stop condition*, *per-answer action*, *output format per item*. (https://dl.acm.org/doi/10.1145/3672359.3672364 ; https://www.dre.vanderbilt.edu/~schmidt/PDF/ADA-User-Journal.pdf)
- **Recurring cross-pattern attributes** (candidate shared modifier slots): persistence trigger ("From now on…", "Whenever…", "always"), scope ("Within scope X"), quantity ("X outputs at a time", "three additional questions"), insertion point ("at the end of your output"), target tool/type ("artifact of type X", "provide to tool Y"), stop condition, optional confirmation ("ask me if I would like to…").
- **Element inventory cross-check:** Prompt Report's 6 components (Directive, Examples, Output Formatting, Style Instructions, Role, Additional Information) + Prompt Canvas's 10 fields (adds Target Audience, Step-by-Step, References, Tonality, Techniques, Tooling) together enumerate the top-level ELEMENTS; the 16+14+2 patterns and the technique lists (Prompt Report 58, Sahoo, promptingguide 18) enumerate OPTIONS for a "Technique/Pattern" attribute; Bsharat's 26 principles supply option values for style/structure attributes (delimiters, headers, output primers, incentive phrases, affirmative-directive phrasing).

## 5. Gaps / not retrieved

- The exact **Consequences** text for each of the 16 patterns was not extracted verbatim (available in the full paper; the ar5iv page has them if needed).
- Prompt Report: the leaf list above may elide a few of the 58 named techniques (e.g., some exemplar-selection/ordering entries); the authoritative full table is in https://arxiv.org/html/2406.06608v6 (fetch summarization limits).
- arxiv.org/html/2312.16171v6 returned 404; the 26 principles were recovered from the ar5iv mirror instead.
- 2303.07839 structure & key ideas per pattern (contextual statements) not extracted verbatim for all 14 SE patterns — only intents; full text at https://ar5iv.labs.arxiv.org/html/2303.07839.
