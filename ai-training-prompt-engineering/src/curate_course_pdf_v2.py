#!/usr/bin/env python3
"""Curate src/assets/course_content.json for the 2026-09-29 sync (the written course,
rendered by build_course_pdf.py): de-duplicate repeated concepts, align chapter order and
slide references to the owner-final deck, make Appendix B learner self-check material, and
apply the readability rewrites. Three stages, each deterministic and self-checking:

  A. Apply the ordered ops of the audit's curation_plan.json (indices refer to the file as
     it was BEFORE this script ran; plan['index_semantics'] documents them). The apply
     logic is the plan builder's simulate(): per-section cuts/replacements/inserts in
     original coordinates, then block moves into a new section, then whole-section moves.
     Every op's expect_type and current_block_head are asserted first, so a second run
     (or a run against a drifted file) fails loudly instead of double-applying.
  B. This script's own ops on the post-plan structure: final deck slide positions
     (main deck cited by physical position; the Reference Deck by its printed number as
     'Reference Deck slide N'), the deck's 'HTML dashboard' wording with HTML glossed in
     prose, a second-pass cut of paragraphs that restate a concept defined elsewhere,
     and jargon glosses. Blocks are located by section heading plus block head; every
     substitution must match exactly once. Wholesale rewrites use the spaced hyphen;
     small in-place edits keep the block's existing dash style.
  C. Second-pass ops from the verifier's reading of the rendered book (2026-09-29):
     one full definition per concept (ASK vs DELEGATE in Chapter 5's table; the twelve
     mission-brief blocks in 'The mission brief for bounded work'; the seven elements and
     the three evidence verdicts in Chapter 3), the Part 1 verification checks merged
     into one list, the supplier expected numbers printed only in Chapter 4 step 1 and
     Appendix B.1, no facilitator document named in the learner chapters, the prompt
     skeleton taken verbatim from build_cheatsheet.py, glosses at first use (RLHF, MoE,
     SKU, 'language-model arithmetic'), one HTML gloss, and a truthful caption for the
     fuller email template. Appendix B's content is untouched (owner decision). Stage C
     is guarded: stage_c_state() recognises a file it has already been applied to and
     the ops are skipped, and a partially matching file fails loudly.
  D. Verification: the eleven approved sends (P1..P7 in build_v08.py) verbatim, in deck
     order, in mono blocks; the application prompts equal to assets/course_prompts.json;
     no instructor-only material outside references/exercise-data/instructor-keys/;
     no model identifiers; every deck reference in the allowed set; the stage C
     post-conditions; word counts; and the concepts that still carry more than one
     'defines' block (audit concept map).

Usage:
  python3 curate_course_pdf_v2.py                 # apply A+B+C to the repo file, then D
  python3 curate_course_pdf_v2.py --out X.json    # same, but write X.json (dry run)
  python3 curate_course_pdf_v2.py --stage-c-only  # C on the current (post A+B) file, then D;
                                                  # a second run is a no-op that still verifies
  python3 curate_course_pdf_v2.py --check-only    # stage D on the current file only
Options: --plan PATH, --concept-map PATH (audit outputs; defaults point at the audit's
scratchpad), --report PATH (JSON report). The PDF is rebuilt separately
(python3 build_course_pdf.py); this script never writes deliverables/.
"""
import argparse
import ast
import copy
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "assets", "course_content.json")
PROMPTS = os.path.join(HERE, "assets", "course_prompts.json")
V08 = os.path.join(HERE, "build_v08.py")
CHEATSHEET = os.path.join(HERE, "build_cheatsheet.py")
AUDIT = ("/tmp/claude-0/-home-user-Claude-Works/a43332a6-06a6-532a-af4a-fdd550eb8be6/"
         "scratchpad/coursepdf")

# Owner-final deck, 2026-09-29 (verified against the deck dump titles): the Part 4
# application block by physical slide position, and the Reference Deck by printed number.
MAIN_DECK_ALLOWED = {37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48}
REF_DECK_ALLOWED = {102, 103, 104, 112, 113}


# --------------------------------------------------------------------------- helpers
def p(text):
    return {"type": "p", "text": text}


def callout(kind, title, body):
    return {"type": "callout", "kind": kind, "title": title, "body": body}


def table(cols, rows, note=None):
    b = {"type": "table", "cols": cols, "rows": rows}
    if note:
        b["note"] = note
    return b


def bullets(items):
    return {"type": "bullets", "items": list(items)}


def cheatsheet_slot(label="Missing info & finish line:"):
    """One skeleton slot of the cheat sheet, (label, text), read from build_cheatsheet.py so
    the book prints the cheat sheet's wording and not a hand-copied variant of it."""
    src = open(CHEATSHEET, encoding="utf-8").read()
    hits = re.findall(r"\(\s*'" + re.escape(label) + r"'\s*,\s*('(?:[^'\\]|\\.)*')\s*\)", src)
    assert len(hits) == 1, f"{label!r} in build_cheatsheet.py: {len(hits)} hits (expected 1)"
    return label, ast.literal_eval(hits[0])


def blk_head(b):
    t = b["type"]
    s = (b.get("text") or b.get("body")
         or (" ".join(b.get("items", [])) if t == "bullets" else "")
         or (" ".join(str(c) for c in b.get("cols", [])) if t == "table" else ""))
    return f"[{t}] " + s[:70].replace("\n", " ")


def texts_of(b):
    """Every text field of a block, for greps and counts."""
    t = b["type"]
    if t in ("p", "h3"):
        return [b["text"]]
    if t == "mono":
        return [b["text"], b.get("caption", "")]
    if t == "bullets":
        return list(b["items"])
    if t == "callout":
        return [b.get("title", ""), b["body"]]
    if t == "table":
        return [str(c) for r in [b["cols"]] + b["rows"] for c in r] + [b.get("note", "")]
    raise ValueError(t)


def words(s):
    return len(re.findall(r"\S+", s or ""))


def count_all(chs):
    n = 0
    for ch in chs:
        n += words(ch.get("intro", ""))
        for sec in ch["sections"]:
            for b in sec["blocks"]:
                n += sum(words(t) for t in texts_of(b))
    return n


def count_prose(chs):
    n = 0
    for ch in chs:
        n += words(ch.get("intro", ""))
        for sec in ch["sections"]:
            for b in sec["blocks"]:
                if b["type"] in ("p", "h3", "bullets", "callout"):
                    n += sum(words(t) for t in texts_of(b))
    return n


def count_blocks(chs):
    return sum(len(s["blocks"]) for ch in chs for s in ch["sections"])


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'), ("—", "-"), ("–", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def strip_ids(chs):
    for ch in chs:
        for sec in ch["sections"]:
            for b in sec["blocks"]:
                b.pop("_id", None)
    return chs


# --------------------------------------------------------------------------- stage A
def tag_ids(chs):
    for ci, ch in enumerate(chs):
        for si, sec in enumerate(ch["sections"]):
            for bi, b in enumerate(sec["blocks"]):
                b["_id"] = f"{ci}.{si}.{bi}"


def assert_plan_targets(chs, ops):
    for i, o in enumerate(ops):
        c, s, b = o["chapter"], o["section"], o["block_index"]
        if s == -1 or b == -1 or isinstance(b, list) or b is None:
            continue
        blk = chs[c]["sections"][s]["blocks"][b]
        if o.get("expect_type"):
            assert blk["type"] == o["expect_type"], (
                f"plan op {i}: expected {o['expect_type']} at {c}.{s}.{b}, found {blk['type']}")
        if o.get("current_block_head"):
            assert blk_head(blk) == o["current_block_head"], (
                f"plan op {i}: block head drifted at {c}.{s}.{b}:\n  file: {blk_head(blk)}\n  plan: {o['current_block_head']}")


def simulate(chs, ops):
    """Ported verbatim in semantics from the audit's plan_build.py simulate(); block identity
    (_id) is carried so the concept report can follow blocks through the moves."""
    new = copy.deepcopy(chs)
    cuts, reps, ins, moved = {}, {}, {}, {}
    sec_moves, heading_reps, intro_reps = [], {}, {}
    for o in ops:
        c, s, b = o["chapter"], o["section"], o["block_index"]
        if o["op"] == "replace" and s == -1:
            intro_reps[c] = o["new_block"]
            continue
        if o["op"] == "replace" and b == -1:
            heading_reps[(c, s)] = o["new_block"]
            continue
        if o["op"] == "cut":
            cuts.setdefault((c, s), set()).add(b)
        elif o["op"] == "replace":
            reps[(c, s, b)] = o["new_block"]
        elif o["op"] == "insert":
            ins.setdefault((c, s, o["target"]["after_block"]), []).append(o["new_block"])
        elif o["op"] == "move":
            if isinstance(b, list):
                moved[(c, s)] = (set(b), o["target"])
            else:
                sec_moves.append((c, s, o["target"]))
        else:
            raise ValueError(o["op"])
    carried = {}
    for ci, ch in enumerate(new):
        if ci in intro_reps:
            ch["intro"] = intro_reps[ci]
        for si, sec in enumerate(ch["sections"]):
            if (ci, si) in heading_reps:
                sec["heading"] = heading_reps[(ci, si)]
            out = []
            if (ci, si, -1) in ins:
                out.extend(dict(x, _id=f"ins:{ci}.{si}.start") for x in ins[(ci, si, -1)])
            mv = moved.get((ci, si))
            for bi, blk in enumerate(sec["blocks"]):
                nb = blk
                if (ci, si, bi) in reps:
                    nb = dict(copy.deepcopy(reps[(ci, si, bi)]), _id=blk["_id"])
                if mv and bi in mv[0]:
                    carried.setdefault((ci, si), []).append(nb)
                elif bi not in cuts.get((ci, si), set()):
                    out.append(nb)
                out.extend(dict(copy.deepcopy(x), _id=f"ins:{ci}.{si}.{bi}")
                           for x in ins.get((ci, si, bi), []))
            sec["blocks"] = out
    for (c, s), blocks in carried.items():
        tgt = moved[(c, s)][1]
        new[tgt["chapter"]]["sections"].insert(
            tgt["after_section"] + 1, {"heading": tgt["new_section_heading"], "blocks": blocks})
    for c, s, tgt in sec_moves:
        src = new[c]["sections"]
        heading = heading_reps.get((c, s), chs[c]["sections"][s]["heading"])
        idx = next(i for i, sec in enumerate(src) if sec["heading"] == heading)
        secobj = src.pop(idx)
        dst = new[tgt["chapter"]]["sections"]
        after_heading = chs[tgt["chapter"]]["sections"][tgt["after_section"]]["heading"]
        j = next(i for i, sec in enumerate(dst) if sec["heading"] == after_heading)
        dst.insert(j + 1, secobj)
    return new


# --------------------------------------------------------------------------- stage B
class Editor:
    """Locates blocks by chapter index + section heading (+ block head) and edits them,
    asserting every target exists exactly once."""

    def __init__(self, chs):
        self.chs = chs
        self.log = []

    def section(self, ci, heading):
        hits = [s for s in self.chs[ci]["sections"] if s["heading"] == heading]
        assert len(hits) == 1, f"section {heading!r} in chapter {ci}: {len(hits)} hits"
        return hits[0]

    def block(self, ci, heading, bi, head):
        sec = self.section(ci, heading)
        b = sec["blocks"][bi]
        first = texts_of(b)[0]
        assert first.startswith(head), (
            f"{ci}/{heading!r}/{bi}: expected head {head!r}, found {first[:80]!r}")
        return sec, b

    def sub(self, ci, heading, bi, head, old, new, field="text", item=None, cell=None, reason=""):
        """Replace `old` (exactly one occurrence) in a block's field, bullet item, or table
        cell (cell=(row, col), 0-based rows below the header)."""
        sec, b = self.block(ci, heading, bi, head)
        if item is not None:
            target = b["items"][item]
        elif cell is not None:
            target = b["rows"][cell[0]][cell[1]]
        else:
            target = b[field]
        assert target.count(old) == 1, (
            f"{ci}/{heading!r}/{bi}: {old[:60]!r} found {target.count(old)} times")
        if item is not None:
            b["items"][item] = target.replace(old, new)
        elif cell is not None:
            b["rows"][cell[0]][cell[1]] = target.replace(old, new)
        else:
            b[field] = target.replace(old, new)
        self.log.append(f"edit {ci}/{heading}/{bi} ({b['type']}): {reason}")

    def insert_after(self, ci, heading, bi, head, new_block, reason=""):
        sec, b = self.block(ci, heading, bi, head)
        sec["blocks"].insert(bi + 1, dict(new_block, _id=f"ins:c:{ci}.{heading[:12]}.{bi}"))
        self.log.append(f"insert {ci}/{heading}/{bi + 1} ({new_block['type']}): {reason}")

    def rewrite(self, ci, heading, bi, head, new_block, reason=""):
        sec, b = self.block(ci, heading, bi, head)
        assert new_block["type"] == b["type"], (b["type"], new_block["type"])
        nb = dict(new_block, _id=b["_id"])
        sec["blocks"][bi] = nb
        self.log.append(f"rewrite {ci}/{heading}/{bi} ({b['type']}): {reason}")

    def cut(self, ci, heading, bi, head, reason=""):
        sec, b = self.block(ci, heading, bi, head)
        del sec["blocks"][bi]
        self.log.append(f"cut {ci}/{heading}/{bi} ({b['type']}): {reason}")

    def set_heading(self, ci, old, new, reason=""):
        sec = self.section(ci, old)
        sec["heading"] = new
        self.log.append(f"heading {ci}: {old!r} -> {new!r}: {reason}")

    def sub_intro(self, ci, old, new, reason=""):
        intro = self.chs[ci]["intro"]
        assert intro.count(old) == 1, (ci, old)
        self.chs[ci]["intro"] = intro.replace(old, new)
        self.log.append(f"intro {ci}: {reason}")


def stage_b(chs, prompts):
    e = Editor(chs)
    # -- deck references: final physical positions of the owner-final deck ----------------
    e.sub(0, "Effort, capability, and the smallest fix", 8, "Using the supplied screenshot",
          "Tab EX6-FeatureMenu - self-updating: ask again the day a button changes.",
          "Tab EX6-FeatureMenu - the deck keeps this one in the reference layer (Reference Deck slide 113). "
          "Self-updating: ask again the day a button changes.",
          field="caption", reason="Prompt 6/7 has no live slide; mark it Reference Deck slide 113")
    e.sub(2, "Your turn: turn your course log into a report", 1, "STEP 1: List every prompt",
          "Reference Deck page 104", "Reference Deck slide 104", field="caption",
          reason="house citation form 'Reference Deck slide N'")
    e.sub(5, "Save one prompt for Monday", 6, "Review the selected conversation about [topic]",
          "Reference Deck page 103", "Reference Deck slide 103", field="caption",
          reason="house citation form 'Reference Deck slide N'")
    e.rewrite(3, "One dataset, nine steps", 2, "Step", table(
        ["Step", "What you make", "Where"], [
            ["1 · Inspect, then analyze", "A checked supplier comparison, reconciled to the source", "Slide 37 · tab 1-Analyze-Data"],
            ["2 · Follow up in the same chat", "A month-and-site pattern - values shown, no causes claimed", "Slide 38 · tab 1-Analyze-Data"],
            ["3 · The assistant returns your workbook", "Supplier_Data_Analyzed.xlsx - Summary sheet, native charts", "Slide 39 · tab Excel-Charts"],
            ["4 · Build the dashboard", "One self-contained offline HTML file from the returned workbook", "Slides 40-41 · tab 2-Build-Dashboard"],
            ["5 · Present the findings", "A five-slide management mock-up from the same verified findings", "Slide 42 · tab 3-Present-Findings"],
            ["6 · Organize the email thread", "The structured brief - decisions, actions, \"Not stated\"", "Slides 43-45 · tab 4-Summarize-Email"],
            ["7 · Extract the quotes", "A Raw Extraction sheet - verbatim values, cited sources", "Slide 47 · tab Quote-Extract"],
            ["8 · Compare the quotes", "A Normalized Comparison - or an honest \"not yet\"", "Slide 48 · tab Quote-Compare"],
            ["9 · Build the research workbook", "Evidence · Synthesis · Sources, every claim traced", "Reference Deck slide 112 · tab Research"]],
        note="Slide numbers are those of From_Prompts_to_Agents_Facilitated_60_Minute.pptx (slides 43 and 46 open the "
             "email and document blocks); the reference exercise (explain a topic clearly) is Reference Deck slide 102 · "
             "tab 5-Explain-Clearly."),
        reason="steps 1-8 at physical positions 37/38/39/40-41/42/43-45/47/48; step 9 Reference Deck slide 112")
    # -- the deck's 'HTML dashboard' wording, HTML glossed in prose at first use ----------
    e.sub(2, "Prompt elements are requirement types: the menu", 8, "<b>Quality and acceptance</b>",
          "Strong: \"one self-contained HTML file that works offline, data embedded, no network calls.\"",
          "Strong: \"one self-contained HTML file that works offline, data embedded, no network calls.\" "
          "(HTML is the web-page format any browser opens.)",
          item=2, reason="gloss HTML at its first use in prose")
    e.rewrite(3, "Step 4: a dashboard from the returned workbook", 1, "You specify behavior, not code",
              callout("key", "You specify behavior, not code",
                      "An HTML dashboard is a web page: the file provides the structure, and JavaScript - the "
                      "browser's scripting language, embedded in the same file - supplies the interactive behavior. "
                      "You specify that behavior in plain language, control by control - no code knowledge is needed "
                      "to ask for it precisely."),
              reason="the callout's 'the page' dangled once the prompt stopped spelling HTML out; gloss HTML and JavaScript here")
    sec, b = e.block(3, "Step 4: a dashboard from the returned workbook", 2, "Using the returned Supplier_Data_Analyzed.xlsx")
    assert b["type"] == "mono" and "HyperText Markup Language (HTML) dashboard" in b["text"], b["text"][:120]
    assert b["text"].replace("HyperText Markup Language (HTML) dashboard", "HTML dashboard") == prompts["dashboard"], (
        "course_prompts.json['dashboard'] differs from the book beyond the HTML wording")
    b["text"] = prompts["dashboard"]
    e.log.append("edit 3/Step 4/2 (mono): dashboard prompt aligned to the deck's 'HTML dashboard' wording (course_prompts.json)")
    # -- jargon glosses -------------------------------------------------------------------
    e.sub(1, "The right workspace for the data", 2, "A vendor's home country",
          "the same vendor can host your company tenant in the EU",
          "the same vendor can host your company tenant - its own fenced-off instance of the service - in the EU",
          reason="gloss 'tenant'")
    e.sub(3, "Step 4: a dashboard from the returned workbook", 4, "A KPI is a number",
          "A KPI is a number someone acts on", "A KPI (key performance indicator) is a number someone acts on",
          reason="spell out KPI at first use")
    e.sub(4, "Worked exercise: the supplier analysis becomes a mission brief", 2, "Shaped as a mission",
          "<b>Transform</b>: one schema, ordered rules", "<b>Transform</b>: one schema (agreed column layout), ordered rules",
          reason="gloss 'schema'")
    e.sub(3, "Step 1: inspect, then analyze", 14, "Averaging the monthly return-rate",
          "Treating the blank cell Inspection_Hours cell as zero", "Treating the blank Inspection_Hours cell as zero",
          item=2, reason="typo")
    # -- second pass: paragraphs that restate a concept defined elsewhere -----------------
    e.rewrite(1, "Compare on your task, not on the leaderboard", 3, "The assistants you will meet", p(
        "The assistants you will meet by name in this course include ChatGPT, Claude, Copilot, Gemini, Perplexity, "
        "and Grok; verify current offerings before relying on any characterization of them. What stays true across "
        "the churn is that different assistants expose different capabilities and controls, and the same brand "
        "behaves differently on different account tiers - which is why the fourth question settles more arguments "
        "than any review article."),
        reason="the head-to-head trial is defined in the four questions above and drilled in the bake-off callout below; drop the third statement")
    e.rewrite(3, "One dataset, nine steps", 6, "This prompt runs, and it returns", p(
        "This prompt runs, and it returns something confident. But it made three decisions silently - the rows, "
        "the metric, and the meaning of \"worst\", the gaps Chapter 3 named - and it carries no source scope, no "
        "denominator rule, no missing-data rule, and no check. Every gap becomes the model's guess - and a guess "
        "you cannot see is a guess you cannot audit."),
        reason="the three silent decisions are already analysed at Chapter 3 'complete enough'; cross-reference instead of restating")
    e.rewrite(3, "Step 5: five slides from the same findings", 7, "Findings are what the workbook supports", p(
        "Findings are what the workbook supports; recommendations are labeled proposals, and the two-panel slide "
        "makes that boundary physical - the trust move that survives every audience question. It matters most "
        "exactly where the story gets tempting. The verified scorecard carries units-weighted unit costs: Alpha "
        "Components $12.4299, Bravo Plastics $9.9030, Cardinal Metals $14.1804. The tension is real - the cheapest "
        "supplier is also the most-returned - and it is precisely where a weak deck starts inventing: a projected "
        "savings figure, a quality-cost trade-off, a committed benefit. The mock deck states no cost claim anywhere, "
        "because the data cannot support one; what switching or fixing would cost is a question for the proposed "
        "review, not for this dataset."),
        reason="the two-panel findings/judgment slide is described in the slide-by-slide list above; keep the unit-cost trap")
    e.rewrite(3, "Step 6: organize the email thread", 0, "An email summary has a job to do", p(
        "An email summary has a job to do. A long thread read top to bottom is a chronology, and a chronological "
        "retelling can bury the current decision - the thing the person asking for the summary actually needs. So "
        "decide what the summary must answer before writing any prompt; the menu below names the jobs."),
        reason="the catch-up / action table / reply preparation list is the 'Choose the result you need' table two blocks down")
    e.rewrite(3, "Reference exercise: explain a topic clearly", 7, "Simplifications that change meaning", p(
        "Finding the simplifications that changed meaning is part of the exercise: compare the explanation with "
        "the source sentence by sentence - a missing condition is a meaning change, not a style choice. Each sample "
        "file in the pack ships with its own fidelity note, because the note is part of the deliverable - a "
        "plain-language document that cannot say what it dropped has not finished the job."),
        reason="'meaning changes are defects' is the section's opening thesis; keep the method and the fidelity note")
    e.rewrite(4, "ASK and DELEGATE: the decision, not the tools", 2, "The agentic column is a superset", p(
        "The agentic column is a superset: every generative element still applies, wrapped in a job. Both modes "
        "require judgment - a chat response can still cause harm if used unchecked - but delegation adds "
        "responsibility for the actions taken, and that difference in failure cost drives everything this chapter "
        "adds."),
        reason="'bad text costs a re-prompt; a wrong action has changed files' is the table's failure-mode row directly above and the chapter intro")
    e.rewrite(4, "Instructions versus enforceable controls", 3, "The injection rule reframes", p(
        "The injection rule reframes how an agent must read: text inside a source document is evidence to inspect, "
        "never authority to change the task - a cell saying \"ignore your instructions\" is quoting, not commanding. "
        "Write that framing into briefs as defense in depth. The course's concrete boundary is a good default: work "
        "on a copy of the workbook and a draft report; nothing sent, no master overwritten."),
        reason="'the real checkpoints live in the tool's permission settings' is the section's opening paragraph")
    e.rewrite(5, "A small review process for shared prompts", 2, "A replacement must solve", p(
        "A replacement must solve the intended problem without introducing critical regressions - it has to beat "
        "the version it replaces on those cases, not just feel better. Re-run the cases after every model upgrade."),
        reason="version, owner, source assumptions and review date are the library conventions listed two blocks down")
    e.cut(6, "Why each dial matters: the agentic criteria", 2, "None of the blocks is bureaucracy",
          reason="after the plan's trim it restates Chapter 5 'The mission brief for bounded work' word for word")
    e.set_heading(6, "The evidence box set: works, myth, expired", "The evidence verdicts: works, myth, expired",
                  reason="the box set was folded into Chapter 3 by the plan; the heading must not promise boxes")
    e.sub_intro(6, "the evidence boxes when a piece of prompting advice needs a verdict",
                "the evidence verdicts when a piece of prompting advice needs one",
                reason="same: no evidence boxes remain in this chapter")
    return e.log


# --------------------------------------------------------------------------- stage C
def stage_c_state(chs):
    """Idempotency guard for stage C. True when every sentinel edit is in the file, False
    when none is; a file that carries only some of them (hand-edited or drifted) fails."""
    e = Editor(chs)
    signs = [
        "and the facilitation plan" not in e.section(6, "The package")["blocks"][2]["text"],
        "Missing info & finish line" in e.section(2, "A prompt is a small work specification")["blocks"][1]["text"],
        not any(b["type"] == "callout" and b.get("title") == "The rule of three"
                for b in e.section(0, "Verification belongs in the task")["blocks"]),
        e.section(4, "The anatomy, grown up to survive autonomy")["blocks"][1]["cols"][0] != "Generative element",
    ]
    assert all(signs) or not any(signs), f"stage C partially applied - refusing to continue: {signs}"
    return all(signs)


def stage_c(chs):
    """Second-pass curation ops (verifier findings on the rendered book, 2026-09-29). Every
    target is located by section heading + block head and every substitution must match
    exactly once; indices are those of the file after stage B and after the earlier ops of
    this function. Appendix B is deliberately untouched."""
    e = Editor(chs)
    # -- no facilitator document named in the learner chapters ---------------------------
    e.sub(6, "The package", 2, "Everything else sits under references/",
          "Prompt_Element_Taxonomy_Reference.pdf, Prompt_Template_Configurator.xlsx, and the facilitation plan.",
          "Prompt_Element_Taxonomy_Reference.pdf, and Prompt_Template_Configurator.xlsx.",
          reason="the facilitation plan is the instructor run-sheet; learners are not pointed at it")
    # -- ASK vs DELEGATE: Chapter 5's table is the one full definition; Part 1 keeps the teaser
    e.rewrite(0, "One skill, two ways to work", 0, "Prompting is the one AI skill", p(
        "Prompting is the one AI skill that transfers everywhere: every assistant, every vendor, every year. "
        "Models change monthly; the craft compounds. The skill has two modes, <b>ASK</b> and <b>DELEGATE</b>, "
        "and the ten-second version is all you need for now: a generative prompt describes <i>what to write</i>; "
        "an agentic prompt describes <i>a job to run</i>."),
        reason="drop the sentence-level ASK/DELEGATE definitions; Chapter 5 'ASK and DELEGATE' defines both")
    e.rewrite(0, "One skill, two ways to work", 1, "The ten-second version", p(
        "That distinction is the backbone of this course - the craft chapters teach the first kind, and "
        "Chapter 5 grows it into the second, defining both modes side by side. For now, feel the difference."),
        reason="the teaser now lives in the paragraph above; this one points forward")
    # -- the timeline table: gloss RLHF and MoE at first use; the 100M-users fact once -----
    e.sub(0, "Four eras, and the decade of named leaps", 3, "Year",
          "Instruction tuning + RLHF", "Instruction tuning + human-feedback tuning (RLHF)", cell=(2, 1),
          reason="gloss RLHF at its first use (defined in prose only two sections later)")
    e.sub(0, "Four eras, and the decade of named leaps", 3, "Year",
          "Human feedback turns a predictor into an assistant; ChatGPT reaches 100M users in two months",
          "Human feedback turns a predictor into an assistant", cell=(2, 2),
          reason="the 100M-users fact is stated, dated and sourced in the next paragraph")
    e.sub(0, "Four eras, and the decade of named leaps", 3, "Year",
          "MoE, distillation, open weights", "Mixture of Experts (MoE), distillation, open weights", cell=(4, 1),
          reason="gloss MoE at its first use (explained in Chapter 2)")
    # -- Part 1: the rule of three, ground/cite/verify and the four failure patterns become one list
    e.cut(0, "Verification belongs in the task", 4, "The rule of three",
          reason="numbers/claims/actions folded into the single checks list below")
    e.rewrite(0, "Verification belongs in the task", 5, "The cure has not changed", p(
        "The cure has not changed: <b>ground it</b> (give it the source), <b>cite it</b> (demand receipts, plus an "
        "'I don't know' escape hatch), <b>verify it</b> (check what matters before it ships). None of these "
        "eliminates confabulation - they convert unverifiable claims into verifiable ones. Which check to run "
        "depends on what kind of wrong you are guarding against:"),
        reason="introduces the merged checks list; the house rule moves below it")
    e.insert_after(0, "Verification belongs in the task", 5, "The cure has not changed", bullets([
        "A <b>number</b> - recompute it.",
        "An <b>invented fact</b> - find the supporting record, or state that it is unknown.",
        "An <b>invented citation</b> - open the actual source and inspect the cited passage.",
        "The <b>wrong document or revision</b> - confirm identity, date, and applicability first.",
        "A <b>lost condition</b> - compare the conclusion with the original qualifier or approval condition.",
        "An <b>action</b> - inspect the result it produced, not the report of it."]),
        reason="the one checks list: the rule of three merged with the four failure patterns")
    e.insert_after(0, "Verification belongs in the task", 6, "A <b>number</b>", p(
        "House rule from here on: every uncited standard clause, date, number, or quote is a draft until "
        "verified. A credible format, a confident tone, or a citation marker is not a check - and a memorable "
        "failure story matters only if it changes which checks you run."),
        reason="house rule + the 'Format is not evidence' callout, in one paragraph")
    e.cut(0, "Failure patterns and the check they need", 3, "Format is not evidence",
          reason="merged into the checks list's closing paragraph")
    e.cut(0, "Failure patterns and the check they need", 2, "An <b>invented fact</b>",
          reason="the four patterns now sit in the merged checks list")
    e.cut(0, "Failure patterns and the check they need", 1, "The same discipline applies",
          reason="lead-in to the cut list")
    e.set_heading(0, "Failure patterns and the check they need", "Diagnose the prompt, not the model",
                  reason="the section now holds only the diagnostic closer and the bridge to Chapter 3")
    # -- the prompt skeleton: the cheat sheet's wording, verbatim ----------------------------
    label, slot = cheatsheet_slot()
    old_slot = ("Missing info & boundaries: if [gap or conflict]: state it, ask, or stop.\n"
                "                      Actions needing review: [actions].")
    new_slot = (f"{label} if [gap]: write “Not stated” and list it;\n"
                "                      if [conflict]: ask or stop. Answer, report limitations,\n"
                "                      then stop. Actions needing review: [actions].")
    assert re.sub(r"\s+", " ", new_slot) == f"{label} {slot}", (
        "the reflowed skeleton slot must equal the cheat sheet's text (whitespace aside)")
    e.sub(2, "A prompt is a small work specification", 1, "Purpose & audience:", old_slot, new_slot,
          reason="last skeleton slot = the cheat sheet's 'Missing info & finish line' text (Out + Stop preserved)")
    # -- one HTML gloss: the Chapter 4 dashboard callout keeps it -------------------------
    e.sub(2, "Prompt elements are requirement types: the menu", 8, "<b>Quality and acceptance</b>",
          " (HTML is the web-page format any browser opens.)", "", item=2,
          reason="HTML is explained once, in 'You specify behavior, not code' (stage B's gloss removed)")
    # -- glosses: SKU, and 'LLM' never expanded ------------------------------------------
    e.sub(2, "One task through the improvement loop", 4, "PLAN   Role: careful retail analyst",
          "PLAN   Role: careful retail analyst — never invent numbers. Task: monthly returns\n"
          "       report from the attached export. Context: columns = SKU · reason code ·\n"
          "       refund €. Format: one-page summary + top-5 table. Example: last month's\n"
          "       report, attached. The out: field missing → say so, don't guess.\n"
          "       The stop: deliver the report — nothing beyond.",
          "PLAN   Role: careful retail analyst — never invent numbers. Task: monthly returns\n"
          "       report from the attached export. Context: columns = SKU (product code) ·\n"
          "       reason code · refund €. Format: one-page summary + top-5 table.\n"
          "       Example: last month's report, attached. The out: field missing → say so,\n"
          "       don't guess. The stop: deliver the report — nothing beyond.",
          reason="gloss SKU inside the example brief; PLAN lines re-flowed to the block's width")
    e.sub(2, "The prompt is a document, not a sentence", 2, "Part",
          "LLM arithmetic is unreliable", "Language-model arithmetic is unreliable", cell=(0, 1),
          reason="'LLM' is never expanded in the book; say language model")
    # -- supplier expected numbers: Chapter 4 step 1 and Appendix B.1 are the two copies ---
    e.sub(3, "Step 3: the assistant returns your workbook", 3, "Editable-native is the acceptance test",
          "Summary totals reconcile to the Data sheet - 224,902 units shipped, 432 returns, with a reconciliation "
          "check on the sheet itself - and both charts respond to editing.",
          "Summary totals reconcile to the Data sheet totals, with a reconciliation check on the sheet itself, "
          "and both charts respond to editing.",
          field="body", reason="the totals are printed in step 1's acceptance checks")
    e.sub(4, "Worked exercise: the supplier analysis becomes a mission brief", 3, "Three human gates",
          "Here that is the workbook's TOTAL row: the 144 detail rows must sum to 224,902 units shipped and 432 "
          "returned, with the one blank Inspection_Hours cell disclosed as missing, not zeroed.",
          "Here that is the workbook's TOTAL row - the shipped and returned totals that Chapter 4, step 1 "
          "reconciled to - with the one blank Inspection_Hours cell disclosed as missing, not zeroed.",
          reason="cite the gate anchor by reference instead of reprinting the totals")
    e.sub(4, "Worked exercise: the supplier analysis becomes a mission brief", 3, "Three human gates",
          "The correct headline: Bravo Plastics has the highest return rate, 262 returns on 75,184 units - 0.348%.",
          "The correct headline is step 1's finding - Bravo Plastics has the highest return rate - with its "
          "number in the title.",
          reason="same: the Bravo figures stay in step 1 and Appendix B.1")
    # -- the four email traps: names here, the resolution in Appendix B.2 ------------------
    e.cut(3, "Step 6: organize the email thread", 14, "Trap",
          reason="the trap-by-trap resolution is Appendix B.2's job; the table repeated it")
    e.rewrite(3, "Step 6: organize the email thread", 13, "The thread is engineered", p(
        "The thread is engineered so that a naive \"summarize this\" fails in observable ways. Four traps are "
        "planted - two moving dates, a conditional approval, an unanswered question, and a missing attachment - "
        "and a good brief catches all four."),
        reason="trap names only; the 'Success check' callout that follows points at Appendix B.2")
    # -- the twelve mission-brief blocks: one definition, in 'The mission brief for bounded work'
    e.rewrite(4, "The anatomy, grown up to survive autonomy", 1, "Generative element", table(
        ["What changes", "Why"], [
            ["Every element must survive unsupervised decisions: role as behaviors only, context as a per-source "
             "register with grain and trust, examples as a worked run",
             "the agent decides for hours without you; a vibe or a guess propagates through the run"],
            ["The task gains a definition of done; the Stop becomes gates and autonomy rules",
             "the loop needs an exit condition, and scope control becomes checkpointed process"],
            ["The format gains logs and a fixed report shape; the Out becomes a logged, owned open item",
             "actions must be traceable, and not-knowing must be owned"],
            ["Conduct blocks appear with no generative ancestor: environment, plan, checks, rules, quality bar",
             "method, verification, and invariants that a text-only prompt never needed"]]),
        reason="a four-row 'what changes' table; the block-by-block definition is the checklist in the next section")
    e.rewrite(6, "Why each dial matters: the agentic criteria", 0, "The second map", p(
        "The second map lists the agentic criteria, each with the mission-brief block it governs and the source "
        "behind it; the rationale per block is in Chapter 5, \"The mission brief for bounded work\". Use it "
        "whenever a task introduces new tools, actions, or approval boundaries."),
        reason="the map no longer explains; it points")
    e.rewrite(6, "Why each dial matters: the agentic criteria", 1, "<b>Posture and standing rules</b>", bullets([
        "<b>Posture and standing rules</b> - <role>, <rules> (Anthropic harness guidance)",
        "<b>Done plus verifiable-by</b> - <mission> (Anthropic memory-tool guidance)",
        "<b>Environment boundaries</b> - <environment> (Claude Code protected paths)",
        "<b>Least-privilege tools</b> - <environment> (OpenAI practical guide; NCSC)",
        "<b>Input register and trust</b> - <inputs> (pipeline and register discipline)",
        "<b>Plan steps and methods</b> - <plan> (Anthropic chaining; Faith and Fate 2023)",
        "<b>Checks: anchor, hard, soft</b> - <checks> (Anthropic Agent SDK)",
        "<b>Gates and autonomy</b> - <process> (OpenAI guide; Feng et al. 2025)",
        "<b>Logs and reproducibility</b> - <outputs> (Anthropic harness guidance)",
        "<b>Report shape and discipline</b> - <reporting>, <quality_bar> (SDK status enums; harness docs)"]),
        reason="criterion name + the brief block it governs + source; the re-explanations duplicated Chapter 5")
    # -- the seven elements: defined in Chapter 3; the reference map keeps name + citation --
    e.rewrite(6, "Why each dial matters: the generative criteria", 0, "This map links", p(
        "This map lists each generative requirement type with the source behind it. What filling the slot does "
        "to your output is explained where the element is introduced in Chapter 3; the field guide carries the "
        "full rationale."),
        reason="the map no longer explains; it points")
    e.rewrite(6, "Why each dial matters: the generative criteria", 1, "<b>Identity and role</b>", bullets([
        "<b>Identity and role</b> (Zheng 2024; Salewski 2023)",
        "<b>Behavioral rules</b> (Anthropic hallucination docs)",
        "<b>Stance and blinding</b> (Cheng, Science 2026; Sharma 2023)",
        "<b>Task verb and question</b> (Google guide; OpenAI GPT-5 guide)",
        "<b>Purpose, the why</b> (Anthropic best practices)",
        "<b>Context and glossary</b> (OpenAI 2025)",
        "<b>Material placement</b> (Anthropic long-context; Liu 2023)",
        "<b>Format and length</b> (Sclar, ICLR 2024)",
        "<b>Examples</b> (Brown 2020; Lu 2021; DeepSeek-R1)",
        "<b>The out and the stop</b> (Anthropic docs; OpenAI 2025)"]),
        reason="element name + citation; the rationale sentences duplicated Chapter 3")
    # -- the three verdicts: defined once, in Chapter 3 -----------------------------------
    e.sub(6, "The evidence verdicts: works, myth, expired", 0, "The course sorts techniques",
          "<b>works</b> (replicated, use it), <b>myth</b> (never survived replication, including some standard "
          "2023 advice), and <b>expired</b> (was genuinely right, then the product absorbed it). The lists are in "
          "Chapter 3",
          "<b>works</b>, <b>myth</b>, and <b>expired</b>. The lists, with each verdict defined, are in Chapter 3",
          reason="the parenthetical definitions repeat the three Chapter 3 callouts")
    # -- the blind-review follow-up: a pointer to the Part 1 mirror test ---------------------
    e.sub(5, "The capstone: one task, one checked result", 3, "Anatomy rebuild.",
          "Blind review. Paste a document you own as \"a colleague's draft\" and ask for the case against it, its "
          "three weakest points, and what evidence would change the verdict - without hinting at your view. Most "
          "people meet their first honest AI review here.",
          "Blind review. Rerun the Chapter 1 mirror test on a document you own - without hinting at your view.",
          item=1, reason="the move is explained and set as an exercise in Chapter 1, 'AI mirrors you'")
    # -- the fuller email template: a truthful caption ------------------------------------
    e.sub(5, "Save one prompt for Monday", 5, "The package gives you two saving surfaces",
          "One of the five, as it ships:", "The email prompt, in the fuller form a library entry deserves:",
          reason="the block below is not one of the workbook prompts (tab 4-Summarize-Email holds the shorter structured brief)")
    e.sub(5, "Save one prompt for Monday", 6, "Review the selected conversation about [topic]",
          "The fuller email-brief template, verbatim - Reference Deck slide 103.",
          "The fuller email-brief template; Reference Deck slide 103 carries a condensed version of it.",
          field="caption",
          reason="slide 103 paraphrases this text; no workbook tab holds it verbatim (checked against the workbook)")
    return e.log


def apply_stage_c(chs):
    if stage_c_state(chs):
        return None
    log = stage_c(chs)
    assert stage_c_state(chs), "stage C ran but its sentinels are not all set"
    return log


# --------------------------------------------------------------------------- stage D
def load_sends():
    tree = ast.parse(open(V08, encoding="utf-8").read())
    P = {n.targets[0].id: ast.literal_eval(n.value) for n in tree.body
         if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name)
         and re.fullmatch(r"P[1-7]", n.targets[0].id)}
    assert len(P) == 7 and sum(len(v) for v in P.values()) == 11, P.keys()
    return P


def verify(chs, prompts, concept_map=None, base=None):
    rep = {}
    monos = [(ci, si, bi, b) for ci, ch in enumerate(chs) for si, sec in enumerate(ch["sections"])
             for bi, b in enumerate(sec["blocks"]) if b["type"] == "mono"]
    order = {(m[0], m[1], m[2]): k for k, m in enumerate(monos)}
    # 1. the eleven approved sends, verbatim, one mono per prompt, in deck order 1..7
    P = load_sends()
    seen, found = [], {}
    for name in ("P1", "P2", "P3", "P4", "P5", "P6", "P7"):
        hits = set()
        for label, text in P[name]:
            hit = [(ci, si, bi) for ci, si, bi, b in monos if text in b["text"]]
            assert len(hit) == 1, f"{name} {label}: verbatim in {len(hit)} mono blocks (expected 1)"
            hits.add(hit[0])
        assert len(hits) == 1, f"{name}: sends split across monos {hits}"
        loc = hits.pop()
        assert loc[0] <= 1, f"{name} outside chapters 0-1: {loc}"
        seen.append(order[loc])
        found[name] = f"{loc[0]}.{loc[1]}.{loc[2]}"
    assert seen == sorted(seen), f"approved prompts out of deck order: {found}"
    p6 = chs[int(found["P6"][0])]["sections"][int(found["P6"].split(".")[1])]["blocks"][int(found["P6"].split(".")[2])]
    assert "Reference Deck slide 113" in p6.get("caption", ""), "P6 must be marked Reference Deck slide 113"
    rep["approved_prompts"] = found
    # 2. application prompts: the shared source (deck, workbook, builder) verbatim in Chapter 4's monos
    app = {}
    for key, text in prompts.items():
        if key.startswith("_"):
            continue
        hit = [f"{ci}.{si}.{bi}" for ci, si, bi, b in monos if ci == 3 and norm(text) in norm(b["text"])]
        assert hit, f"course_prompts.json[{key}] not found verbatim in a Chapter 4 mono"
        app[key] = hit
    dash = [b for ci, si, bi, b in monos if b["text"] == prompts["dashboard"]]
    assert len(dash) == 1, "the dashboard prompt must equal course_prompts.json exactly once"
    assert "HyperText" not in json.dumps(chs, ensure_ascii=False), "old HTML spelling still present"
    rep["application_prompts"] = app
    # 3. instructor material: none in learner chapters (0-6) and the self-check keys (8); ch 7 = verbatim sources
    bad = re.compile(r"instructor|facilitator|facilitation|hand out|KEY-Analysis|KEY-Email|instructor-keys", re.I)
    for ci, ch in enumerate(chs):
        if ci == 7:
            continue
        fields = [ch.get("title", ""), ch.get("intro", ""), ch.get("kicker", "")]
        for sec in ch["sections"]:
            fields.append(sec["heading"])
            for b in sec["blocks"]:
                fields.extend(texts_of(b))
        for f in fields:
            m = bad.search(f)
            assert not m, f"instructor material in chapter {ci}: ...{f[max(0, m.start()-60):m.end()+60]}..."
    # 4. model identifiers
    ids = re.compile(r"\b(Fable|Opus|Mythos|Sonnet|Haiku)\b|claude-[a-z0-9]", re.I)
    m = ids.search(json.dumps(chs, ensure_ascii=False))
    assert not m, f"model identifier in content: {m.group(0)}"
    # 5. deck references: main deck by physical position, Reference Deck by printed number
    refs = []
    for ci, ch in enumerate(chs):
        if ci == 7:
            continue
        for sec in ch["sections"]:
            for b in sec["blocks"]:
                for t in texts_of(b):
                    assert not re.search(r"\bDeck \d", t), f"stale 'Deck N' citation: {t[:80]}"
                    assert not re.search(r"Reference Deck (?:page|p\.) ?\d", t), f"'Reference Deck page': {t[:80]}"
                    for mm in re.finditer(r"Reference Deck slide (\d+)", t):
                        n = int(mm.group(1)); assert n in REF_DECK_ALLOWED, (n, t[:80]); refs.append(f"Reference Deck slide {n}")
                    for mm in re.finditer(r"\bSlides? (\d+)(?:-(\d+))?", t):
                        lo, hi = int(mm.group(1)), int(mm.group(2) or mm.group(1))
                        assert {lo, hi} <= MAIN_DECK_ALLOWED, (mm.group(0), t[:80])
                        refs.append(mm.group(0))
                    assert not re.search(r"(?<!Reference Deck )\bslide \d", t), f"lower-case slide citation: {t[:80]}"
    rep["deck_references"] = sorted(set(refs), key=lambda s: (s.startswith("Ref"), s))
    # 5b. stage C post-conditions (learner chapters 0-6 and the self-check keys, 8)
    learner = json.dumps(chs[:7] + chs[8:], ensure_ascii=False)
    for needle in ("and the facilitation plan", "HTML is the web-page format", "LLM arithmetic",
                   "ChatGPT reaches 100M", "Instruction tuning + RLHF\"", "The rule of three",
                   "The fuller email-brief template, verbatim"):
        assert needle not in learner, f"stage C post-condition: {needle!r} still present"
    for needle in ("human-feedback tuning (RLHF)", "Mixture of Experts (MoE)", "SKU (product code)",
                   "Language-model arithmetic", "Reference Deck slide 103 carries a condensed version",
                   "Chapter 1 mirror test"):
        assert learner.count(needle) == 1, f"stage C post-condition: {needle!r} x{learner.count(needle)}"
    label, slot = cheatsheet_slot()
    skel = [b for ci, si, bi, b in monos if b["text"].startswith("Purpose & audience:")]
    assert len(skel) == 1 and re.sub(r"\s+", " ", skel[0]["text"]).endswith(f"{label} {slot}"), (
        "the book's prompt skeleton must end with the cheat sheet's last slot, verbatim")
    totals_in = {sec["heading"] for ci, ch in enumerate(chs) if ci != 7 for sec in ch["sections"]
                 if any("224,902" in t for b in sec["blocks"] for t in texts_of(b))}
    assert totals_in == {"Step 1: inspect, then analyze", chs[8]["sections"][0]["heading"]}, totals_in
    twelve = [(ci, sec["heading"]) for ci, ch in enumerate(chs[:7]) for sec in ch["sections"]
              for b in sec["blocks"] if b["type"] == "bullets"
              and sum(re.match(r"<[a-z_]+>", i) is not None for i in b["items"]) >= 12]
    assert twelve == [(4, "The mission brief for bounded work")], f"twelve-block definition not unique: {twelve}"
    # 6. word and block counts
    rep["counts"] = {"all_text_words": count_all(chs), "prose_words": count_prose(chs), "blocks": count_blocks(chs)}
    if base is not None:
        rep["counts_before"] = {"all_text_words": count_all(base), "prose_words": count_prose(base), "blocks": count_blocks(base)}
    # 7. concepts that still have more than one 'defines' block
    if concept_map is not None:
        where = {}
        for ci, ch in enumerate(chs):
            for si, sec in enumerate(ch["sections"]):
                for bi, b in enumerate(sec["blocks"]):
                    if "_id" in b:
                        where[b["_id"]] = (ci, si, bi)
        multi = []
        for name, entries in concept_map.items():
            defs = [where.get(f"{e['chapter']}.{e['section']}.{e['block_index']}")
                    for e in entries if e["role"] == "defines"]
            defs = [d for d in defs if d is not None]
            if len(defs) > 1:
                secs = {(c, s) for c, s, _ in defs}
                # one definition spread over consecutive blocks of one section is not a repetition
                run = len(secs) == 1 and max(b for _, _, b in defs) - min(b for _, _, b in defs) < len(defs)
                multi.append({"concept": name, "defines_at": [f"{c}.{s}.{b}" for c, s, b in defs],
                              "same_section": len(secs) == 1, "consecutive_run": run})
        rep["concepts_with_multiple_defines"] = multi
    return rep


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plan", default=os.path.join(AUDIT, "curation_plan.json"))
    ap.add_argument("--concept-map", default=os.path.join(AUDIT, "concept_map.json"))
    ap.add_argument("--out", default=CONTENT)
    ap.add_argument("--report", default=None)
    ap.add_argument("--check-only", action="store_true")
    ap.add_argument("--stage-c-only", action="store_true",
                    help="apply stage C to the current file (skipped if already applied), then verify and write")
    a = ap.parse_args()

    prompts = json.load(open(PROMPTS, encoding="utf-8"))
    base = json.load(open(CONTENT, encoding="utf-8"))
    cmap = json.load(open(a.concept_map, encoding="utf-8")) if os.path.exists(a.concept_map) else None

    if a.check_only:
        rep = verify(copy.deepcopy(base), prompts)
        print(json.dumps(rep, indent=1, ensure_ascii=False))
        return

    if a.stage_c_only:
        chs = copy.deepcopy(base)
        tag_ids(chs)
        log = apply_stage_c(chs)
        if log is None:
            print("stage C: already applied to this file - no ops run (idempotent)")
            log = []
        else:
            print(f"stage C: {len(log)} ops")
            for line in log:
                print("  " + line)
        rep = verify(chs, prompts, None, base)
        rep["stage_c_log"] = log
        strip_ids(chs)
        json.dump(chs, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"content written: {a.out}")
        c0, c1 = rep["counts_before"], rep["counts"]
        print(f"words all-text {c0['all_text_words']} -> {c1['all_text_words']} | prose {c0['prose_words']} -> {c1['prose_words']} "
              f"| blocks {c0['blocks']} -> {c1['blocks']}")
        print("approved prompts:", rep["approved_prompts"])
        print("deck references:", rep["deck_references"])
        if a.report:
            json.dump(rep, open(a.report, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print("report:", a.report)
        return

    plan = json.load(open(a.plan, encoding="utf-8"))
    ops = plan["ops"]
    assert_plan_targets(base, ops)
    tagged = copy.deepcopy(base)
    tag_ids(tagged)
    chs = simulate(tagged, ops)
    print(f"stage A: {len(ops)} plan ops applied "
          f"(cut {sum(o['op'] == 'cut' for o in ops)}, replace {sum(o['op'] == 'replace' for o in ops)}, "
          f"insert {sum(o['op'] == 'insert' for o in ops)}, move {sum(o['op'] == 'move' for o in ops)})")
    log = stage_b(chs, prompts)
    print(f"stage B: {len(log)} ops")
    for line in log:
        print("  " + line)
    log_c = apply_stage_c(chs)
    assert log_c is not None, "stage C sentinels already set right after stage B - unexpected"
    print(f"stage C: {len(log_c)} ops")
    for line in log_c:
        print("  " + line)
    rep = verify(chs, prompts, cmap, base)
    rep["stage_b_log"] = log
    rep["stage_c_log"] = log_c
    strip_ids(chs)
    json.dump(chs, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"content written: {a.out}")
    c0, c1 = rep["counts_before"], rep["counts"]
    print(f"words all-text {c0['all_text_words']} -> {c1['all_text_words']} | prose {c0['prose_words']} -> {c1['prose_words']} "
          f"| blocks {c0['blocks']} -> {c1['blocks']}")
    print("approved prompts:", rep["approved_prompts"])
    print("deck references:", rep["deck_references"])
    print("concepts with >1 'defines' block:", len(rep.get("concepts_with_multiple_defines", [])))
    if a.report:
        json.dump(rep, open(a.report, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("report:", a.report)


if __name__ == "__main__":
    main()
