"""Sync pass 2026-09-29 — deck numbering and cross-reference sync.

Input  = the current deliverable decks (main + Reference Deck).
Output = the same paths, plus a copy of the synced main deck in "First package".
Untouched copies of the inputs are kept under SCRATCH/before/ before anything is written.

What it does (and nothing else):
  1. MAIN DECK: every 'page-number' shape prints the slide's physical position
     (position 49, the REFERENCE APPENDIX divider, stays unnumbered).
  2. Applies every exact old->new substitution from the audit's remap_plan.json
     (run-level replacement so formatting survives; each 'old' must occur exactly once
     in the named slide's body or notes).
  3. MAIN DECK notes fixes: slide 7 ("trust slide in Part 2" -> Reference Deck slide 106);
     slides 43 and 46 (owner-added dividers) get their own short facilitator notes
     instead of the notes copied from slide 36.
  4. REFERENCE DECK: three workbook/course-book pointer fixes on printed 100, 102, 103.
  5. Dumps both decks before and after, asserts that the only differences are the
     planned ones, and writes SCRATCH/diff_report.txt.
  7. (`--followup`, run after the sync pass) Verifier follow-ups: the same "trust slide"
     notes fix on main slide 50 and Reference Deck printed 74, and the slide-37 ANCHORS
     title on main slide 1; verified against the post-sync dumps, then re-copied to
     "First package". Guarded, so re-running it is a no-op that says so.
Every substitution asserts that it found its target exactly once — nothing no-ops silently.
"""
import copy
import hashlib
import json
import os
import shutil
import sys
import zipfile

from pptx import Presentation

REPO = "/home/user/Claude-Works/ai-training-prompt-engineering/"
DELIV = REPO + "deliverables/"
MAIN = DELIV + "From_Prompts_to_Agents_Facilitated_60_Minute.pptx"
REF = DELIV + "From_Prompts_to_Agents_Reference_Deck.pptx"
FIRST_PACKAGE_MAIN = DELIV + "First package/From_Prompts_to_Agents_Facilitated_Final_0918.pptx"

SCRATCH = ("/tmp/claude-0/-home-user-Claude-Works/a43332a6-06a6-532a-af4a-fdd550eb8be6/"
           "scratchpad/")
IMPL = SCRATCH + "deck-impl/"
BEFORE = IMPL + "before/"
REMAP_PLAN = SCRATCH + "deck-xref/remap_plan.json"
DIFF_REPORT = IMPL + "diff_report.txt"

UNNUMBERED_MAIN_POSITIONS = {49}  # REFERENCE APPENDIX divider — stays without a page number

# ----------------------------------------------------------------------------------------
# Extra edits beyond remap_plan.json (all exact, all asserted to occur exactly once).
# ----------------------------------------------------------------------------------------
EXTRA_SUBS = [
    # (b) main slide 7 notes: point the "trust slide" remark at the Reference Deck page.
    {"deck": "main", "pos": 7, "where": "notes",
     "old": "on the trust slide in Part 2.)",
     "new": "on Reference Deck slide 106, “The right workspace for the data”.)"},
    # Reference Deck printed 103 (pos 57): the long template is in the course book now.
    {"deck": "ref", "pos": 57, "where": "body",
     "old": "Copy-paste version: workbook tab 4-Summarize-Email",
     "new": "Full template: the course book, Reusable prompts chapter"},
    # Reference Deck printed 100 (pos 54): the dashboard vocabulary table lives in EX-Dashboard.
    {"deck": "ref", "pos": 54, "where": "notes",
     "old": "the vocabulary table in workbook tab 2-Build-Dashboard",
     "new": "the vocabulary table in workbook tab EX-Dashboard"},
    # Reference Deck printed 102 (pos 56): stale topic — the plain-language pack has no
    # supplier-quality file; its worked demonstration is inventory_replenishment.md and
    # the exercise has no live slot (workbook tab 5-Explain-Clearly agrees).
    {"deck": "ref", "pos": 56, "where": "body",
     "old": "Supplier quality (the live example)",
     "new": "Inventory replenishment (the worked demonstration)"},
]

# (c) Fresh facilitator notes for the two owner-added dividers (TIME chip unchanged: 0:40).
NEW_NOTES = {
    43: [
        "MODE: TEACH",
        "TIME: 0:40",
        "PURPOSE: Introduce the email block (slides 44–45).",
        "LAND THIS: A long thread becomes a short brief: decisions, actions, open questions.",
        "SAY: Copilot in Outlook is one way to summarize a thread. The pasted fictional thread "
        "with the same prompt is the fallback in any approved assistant. The thread is data, "
        "not instructions.",
        "DO: Nothing yet — the Outlook walkthrough is next.",
        "BRIDGE: Move to \"Organize an Email Thread in Outlook\".",
        "IF LATE: COMPRESS to the LAND THIS sentence.",
    ],
    46: [
        "MODE: TEACH",
        "TIME: 0:40",
        "PURPOSE: Introduce the quotation block (slides 47–48).",
        "LAND THIS: A document becomes data only after its values are transcribed and checked.",
        "SAY: Three fictional supplier quotes arrive as PDFs. Values are copied verbatim, each "
        "with its source file and page. Pictures and scans are read, not parsed: transcribe "
        "first, spot-check the values against the page, then compute.",
        "DO: Nothing yet — the extraction prompt is next.",
        "BRIDGE: Move to \"Extract Supplier Quotes into Excel\".",
        "IF LATE: COMPRESS to the LAND THIS sentence.",
    ],
}
NEW_NOTES_MAX_WORDS = 90

# ----------------------------------------------------------------------------------------
# 7. Follow-up fixes from the verifier (run separately: `python3 <this file> --followup`).
#    Guarded so re-running is safe: a substitution whose `old` is gone and whose `new` is
#    already present exactly once is reported as already applied; anything else that is
#    not exactly one hit fails loudly.
# ----------------------------------------------------------------------------------------
FOLLOWUP_SUBS = [
    # main pos 50 and Reference Deck pos 28 (printed 74) carry the same stale sentence that
    # EXTRA_SUBS already fixed on main slide 7 — same replacement.
    {"deck": "main", "pos": 50, "where": "notes",
     "old": "on the trust slide in Part 2.)",
     "new": "on Reference Deck slide 106, “The right workspace for the data”.)"},
    {"deck": "ref", "pos": 28, "where": "notes",
     "old": "on the trust slide in Part 2.)",
     "new": "on Reference Deck slide 106, “The right workspace for the data”.)"},
    # main pos 1 notes, ANCHORS list: use the live title of slide 37.
    {"deck": "main", "pos": 1, "where": "notes",
     "old": "37: Exercise: compare suppliers and check the result",
     "new": "37: Upload the Data File and Run These Two Prompts"},
    # Reference Deck printed 99 (pos 53) notes: the presentation demonstration is main
    # deck slide 42 (the five-slide mock-up), not 44 (the Outlook teach slide).
    {"deck": "ref", "pos": 53, "where": "notes",
     "old": "now sits at live slide 44",
     "new": "now sits at main deck slide 42"},
]
FOLLOWUP_BASELINE = {"main": IMPL + "after_main.json", "ref": IMPL + "after_ref.json"}
FOLLOWUP_REPORT = IMPL + "followup_report.txt"


# ----------------------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------------------
def die(msg):
    raise SystemExit("FAIL: " + msg)


def dump_deck(path):
    """Same shape as the audit dump: pos, printed, title, body, notes."""
    prs = Presentation(path)
    rows = []
    for i, s in enumerate(prs.slides, 1):
        title, body, pagenum = "", [], ""
        for sh in s.shapes:
            if sh.has_text_frame and sh.text_frame.text.strip():
                t = sh.text_frame.text.strip()
                if sh.name == "page-number":
                    pagenum = t
                    continue
                if not title:
                    title = t.split("\n")[0][:80]
                body.append(t)
        notes = s.notes_slide.notes_text_frame.text if s.has_notes_slide else ""
        rows.append({"pos": i, "printed": pagenum, "title": title,
                     "body": "\n".join(body), "notes": notes})
    return rows


def text_frames(slide, where):
    if where == "notes":
        if not slide.has_notes_slide:
            die("slide has no notes")
        return [slide.notes_slide.notes_text_frame]
    if where == "body":
        return [sh.text_frame for sh in slide.shapes
                if sh.has_text_frame and sh.name != "page-number"]
    die("unknown where=" + where)


def replace_once(slide, where, old, new, label):
    """Replace `old` with `new` exactly once inside the slide's body shapes or notes.

    Prefers a run-level replacement (formatting untouched). If the target spans runs,
    the paragraph is collapsed into its first run (keeping that run's formatting).
    """
    hits = []  # (paragraph, run-or-None)
    for tf in text_frames(slide, where):
        for p in tf.paragraphs:
            ptxt = "".join(r.text for r in p.runs)
            n = ptxt.count(old)
            if n == 0:
                continue
            if n > 1:
                die(f"{label}: {old!r} occurs {n}x in one paragraph")
            runs = [r for r in p.runs if old in r.text]
            hits.append((p, runs[0] if runs else None))
    if len(hits) != 1:
        die(f"{label}: {old!r} found {len(hits)} times in {where} (expected exactly 1)")
    p, run = hits[0]
    if run is not None:
        if run.text.count(old) != 1:
            die(f"{label}: {old!r} occurs more than once in the run")
        run.text = run.text.replace(old, new)
    else:  # spans runs: keep first run, its formatting, and the joined text
        first = p.runs[0]
        joined = "".join(r.text for r in p.runs)
        for r in p.runs[1:]:
            p._p.remove(r._r)
        first.text = joined.replace(old, new, 1)
    return f"{label}: {old!r} -> {new!r}"


def set_page_number(slide, pos, label):
    shapes = [sh for sh in slide.shapes if sh.name == "page-number"]
    if len(shapes) != 1:
        die(f"{label}: expected one page-number shape, found {len(shapes)}")
    tf = shapes[0].text_frame
    runs = [r for p in tf.paragraphs for r in p.runs]
    if len(runs) != 1:
        die(f"{label}: page-number shape has {len(runs)} runs (expected 1)")
    old = runs[0].text
    runs[0].text = str(pos)
    return old


def set_notes(slide, lines, label):
    """Replace the whole notes text with `lines`, reusing the first run's formatting."""
    words = sum(len(l.split()) for l in lines)
    if words >= NEW_NOTES_MAX_WORDS:
        die(f"{label}: new notes are {words} words (limit {NEW_NOTES_MAX_WORDS})")
    tf = slide.notes_slide.notes_text_frame
    if not tf.paragraphs or not tf.paragraphs[0].runs:
        die(f"{label}: notes have no run to copy formatting from")
    p0 = tf.paragraphs[0]
    rpr = copy.deepcopy(p0.runs[0]._r.get_or_add_rPr())
    ppr = copy.deepcopy(p0._p.pPr) if p0._p.pPr is not None else None
    for p in list(tf.paragraphs)[1:]:
        tf._txBody.remove(p._p)
    for child in list(p0._p):
        if child.tag.endswith("}pPr") or child.tag.endswith("}endParaRPr"):
            continue
        p0._p.remove(child)
    for i, line in enumerate(lines):
        p = p0 if i == 0 else tf.add_paragraph()
        if i and ppr is not None:
            p._p.insert(0, copy.deepcopy(ppr))
        r = p.add_run()
        r.text = line
        existing = r._r.rPr
        if existing is not None:
            r._r.remove(existing)
        r._r.insert(0, copy.deepcopy(rpr))
    return words


def zip_hashes(path):
    z = zipfile.ZipFile(path)
    return {n: hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist()}


# ----------------------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------------------
def main():
    os.makedirs(BEFORE, exist_ok=True)
    before_paths = {}
    for key, src in (("main", MAIN), ("ref", REF)):
        dst = BEFORE + os.path.basename(src)
        if not os.path.exists(dst):
            shutil.copyfile(src, dst)  # untouched input, kept for the diff
        before_paths[key] = dst

    plan = json.load(open(REMAP_PLAN, encoding="utf-8"))
    if len(plan) != 49:
        die(f"remap_plan.json has {len(plan)} items, expected 49")
    subs = plan + EXTRA_SUBS

    decks = {"main": Presentation(MAIN), "ref": Presentation(REF)}
    if len(decks["main"].slides) != 69 or len(decks["ref"].slides) != 67:
        die("unexpected slide counts")
    log = []

    # 1. page numbers (main deck)
    page_changes = []
    for i, slide in enumerate(decks["main"].slides, 1):
        if i in UNNUMBERED_MAIN_POSITIONS:
            if any(sh.name == "page-number" for sh in slide.shapes):
                die(f"main pos {i} should be unnumbered but has a page-number shape")
            continue
        old = set_page_number(slide, i, f"main pos {i}")
        if old != str(i):
            page_changes.append((i, old, str(i)))
    log.append(f"page numbers: {len(page_changes)} slides renumbered "
               f"({', '.join(f'{p}: {o}->{n}' for p, o, n in page_changes)})")

    # 2. + 3b + 4. exact substitutions
    for it in subs:
        slide = decks[it["deck"]].slides[it["pos"] - 1]
        log.append(replace_once(slide, it["where"], it["old"], it["new"],
                                f"{it['deck']} pos {it['pos']} {it['where']}"))

    # 3c. fresh notes for the owner-added dividers
    for pos, lines in NEW_NOTES.items():
        slide = decks["main"].slides[pos - 1]
        body = "\n".join(sh.text_frame.text for sh in slide.shapes if sh.has_text_frame)
        if "PART 4 · APPLICATION" not in body or "TEACH  0:40" not in body:
            die(f"main pos {pos} is not the expected owner-added divider")
        words = set_notes(slide, lines, f"main pos {pos} notes")
        log.append(f"main pos {pos} notes: replaced (copied from slide 36) with {words}-word "
                   f"facilitator notes")

    decks["main"].save(MAIN)
    decks["ref"].save(REF)

    # 5. verify: dump after, simulate expected, compare
    report = ["DECK SYNC 2026-09-29 — diff report (before -> after)", ""]
    problems = []
    for key, path in (("main", MAIN), ("ref", REF)):
        before = dump_deck(before_paths[key])
        after = dump_deck(path)
        json.dump(before, open(IMPL + f"before_{key}.json", "w"), ensure_ascii=False, indent=1)
        json.dump(after, open(IMPL + f"after_{key}.json", "w"), ensure_ascii=False, indent=1)
        if len(before) != len(after):
            die(f"{key}: slide count changed")
        # expected text = before text with the planned edits applied
        expected = copy.deepcopy(before)
        for it in subs:
            if it["deck"] != key:
                continue
            row = expected[it["pos"] - 1]
            if row[it["where"]].count(it["old"]) != 1:
                die(f"expected-model: {it} not unique in before dump")
            row[it["where"]] = row[it["where"]].replace(it["old"], it["new"])
        if key == "main":
            for row in expected:
                row["printed"] = "" if row["pos"] in UNNUMBERED_MAIN_POSITIONS else str(row["pos"])
            for pos, lines in NEW_NOTES.items():
                expected[pos - 1]["notes"] = "\n".join(lines)
        report.append(f"=== {key.upper()} DECK: {os.path.basename(path)} ===")
        changed = 0
        for b, e, a in zip(before, expected, after):
            for field in ("printed", "body", "notes"):
                if a[field] != e[field]:
                    problems.append(f"{key} pos {a['pos']} {field}: differs from the planned result")
                if a[field] != b[field]:
                    changed += 1
                    report.append(f"pos {a['pos']:>2} {field}:")
                    if field == "printed":
                        report.append(f"   {b[field] or '-'} -> {a[field] or '-'}")
                    elif field == "notes" and a["pos"] in NEW_NOTES and key == "main":
                        report.append("   (whole notes replaced)")
                        report.append("   BEFORE: " + b[field].replace("\n", " | ")[:160] + " ...")
                        report.append("   AFTER:  " + a[field].replace("\n", " | "))
                    else:
                        bl, al = b[field].split("\n"), a[field].split("\n")
                        for x, y in zip(bl, al):
                            if x != y:
                                report.append(f"   - {x}")
                                report.append(f"   + {y}")
                        if len(bl) != len(al):
                            problems.append(f"{key} pos {a['pos']} {field}: line count changed")
        if key == "main":
            for row in after:
                want = "" if row["pos"] in UNNUMBERED_MAIN_POSITIONS else str(row["pos"])
                if row["printed"] != want:
                    problems.append(f"main pos {row['pos']}: printed {row['printed']!r} != {want!r}")
        if key == "ref":
            for row in after:
                want = "" if row["pos"] == 27 else str(row["pos"] + 46)
                if row["printed"] != want:
                    problems.append(f"ref pos {row['pos']}: printed {row['printed']!r} != {want!r}")
        hb, ha = zip_hashes(before_paths[key]), zip_hashes(path)
        members = sorted(n for n in set(hb) | set(ha) if hb.get(n) != ha.get(n))
        report.append(f"-- {changed} slide fields changed; {len(members)} zip members differ:")
        report.append("   " + ", ".join(members))
        report.append("")

    report.append("=== EDIT LOG ===")
    report.extend(log)
    if problems:
        report.append("")
        report.append("=== PROBLEMS ===")
        report.extend(problems)
    open(DIFF_REPORT, "w", encoding="utf-8").write("\n".join(report) + "\n")
    if problems:
        die("verification failed — see " + DIFF_REPORT)

    # 6. First package copy
    shutil.copyfile(MAIN, FIRST_PACKAGE_MAIN)
    print("\n".join(log))
    print(f"OK — report: {DIFF_REPORT}; First package copy updated.")


def count_hits(slide, where, text):
    """Number of paragraphs (in the slide's body shapes or notes) containing `text`."""
    return sum("".join(r.text for r in p.runs).count(text)
               for tf in text_frames(slide, where) for p in tf.paragraphs)


def followup():
    """Step 7: apply FOLLOWUP_SUBS on top of the synced decks and verify against the
    post-sync dumps (after_main.json / after_ref.json). Safe to re-run."""
    for path in FOLLOWUP_BASELINE.values():
        if not os.path.exists(path):
            die("baseline dump missing: " + path + " (run the sync pass first)")
    baseline = {k: json.load(open(p, encoding="utf-8")) for k, p in FOLLOWUP_BASELINE.items()}
    decks = {"main": Presentation(MAIN), "ref": Presentation(REF)}
    if len(decks["main"].slides) != 69 or len(decks["ref"].slides) != 67:
        die("unexpected slide counts")

    log, applied = [], []
    for it in FOLLOWUP_SUBS:
        slide = decks[it["deck"]].slides[it["pos"] - 1]
        label = f"{it['deck']} pos {it['pos']} {it['where']}"
        n_old, n_new = count_hits(slide, it["where"], it["old"]), count_hits(slide, it["where"], it["new"])
        if n_old == 0 and n_new == 1:
            log.append(f"{label}: already applied ({it['new']!r} present once) — skipped")
            continue
        if n_old != 1 or n_new != 0:
            die(f"{label}: expected exactly one {it['old']!r} and no {it['new']!r}, "
                f"found {n_old} and {n_new}")
        log.append(replace_once(slide, it["where"], it["old"], it["new"], label))
        applied.append(it)

    if applied:
        decks["main"].save(MAIN)
        decks["ref"].save(REF)

    # verify: only the FOLLOWUP_SUBS fields may differ from the post-sync baseline
    report = ["DECK SYNC 2026-09-29 — follow-up report (post-sync baseline -> now)", ""]
    problems = []
    for key, path in (("main", MAIN), ("ref", REF)):
        before, after = baseline[key], dump_deck(path)
        json.dump(after, open(IMPL + f"after2_{key}.json", "w"), ensure_ascii=False, indent=1)
        if len(before) != len(after):
            die(f"{key}: slide count changed")
        expected = copy.deepcopy(before)
        for it in FOLLOWUP_SUBS:
            if it["deck"] != key:
                continue
            row = expected[it["pos"] - 1]
            if row[it["where"]].count(it["old"]) != 1:
                die(f"expected-model: {it} not unique in baseline dump")
            row[it["where"]] = row[it["where"]].replace(it["old"], it["new"])
        report.append(f"=== {key.upper()} DECK: {os.path.basename(path)} ===")
        changed = 0
        for b, e, a in zip(before, expected, after):
            for field in ("printed", "title", "body", "notes"):
                if a[field] != e[field]:
                    problems.append(f"{key} pos {a['pos']} {field}: differs from the planned result")
                if a[field] != b[field]:
                    changed += 1
                    report.append(f"pos {a['pos']:>2} {field}:")
                    bl, al = b[field].split("\n"), a[field].split("\n")
                    for x, y in zip(bl, al):
                        if x != y:
                            report.append(f"   - {x}")
                            report.append(f"   + {y}")
                    if len(bl) != len(al):
                        problems.append(f"{key} pos {a['pos']} {field}: line count changed")
        want_changed = sum(1 for it in FOLLOWUP_SUBS if it["deck"] == key)
        if changed != want_changed:
            problems.append(f"{key}: {changed} fields differ from baseline, expected {want_changed}")
        report.append(f"-- {changed} slide fields changed (expected {want_changed})")
        report.append("")
    report.append("=== EDIT LOG ===")
    report.extend(log)
    if problems:
        report.append("")
        report.append("=== PROBLEMS ===")
        report.extend(problems)
    open(FOLLOWUP_REPORT, "w", encoding="utf-8").write("\n".join(report) + "\n")
    if problems:
        die("follow-up verification failed — see " + FOLLOWUP_REPORT)

    shutil.copyfile(MAIN, FIRST_PACKAGE_MAIN)
    if hashlib.sha256(open(MAIN, "rb").read()).digest() != \
            hashlib.sha256(open(FIRST_PACKAGE_MAIN, "rb").read()).digest():
        die("First package copy is not byte-identical to the main deck")
    print("\n".join(log))
    print(f"OK — report: {FOLLOWUP_REPORT}; First package copy updated.")


if __name__ == "__main__":
    sys.exit(followup() if "--followup" in sys.argv[1:] else main())
