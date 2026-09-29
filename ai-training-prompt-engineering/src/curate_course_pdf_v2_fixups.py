#!/usr/bin/env python3
"""Post-verification fix-ups to the course book content (2026-09-29 sync pass).

Three residuals the second verification round found, applied with asserted,
content-located edits so the script is safe to re-run (each edit is skipped
when its target text is already gone):

1. The 'states' prompt box claims to be the workbook tab verbatim but carries
   an extra leading sentence: drop it so the box equals the tab cell.
2. The acceptance-check box claims the same and differs by a few words:
   set its text to the workbook cell exactly.
3. The 'artifact decides the requirement types' principle is defined in
   Chapter 3 and restated in the Chapter 4 closing callout: keep only the
   closing callout's new content.
"""
import json
import os

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "assets", "course_content.json")
WORKBOOK = os.path.join(HERE, "..", "deliverables", "Course_Workbook.xlsx")


def cell_text(ws, label):
    for row in ws.iter_rows(values_only=True):
        if row and row[0] == label:
            return row[1]
    raise SystemExit(f"workbook row {label!r} not found")


def main():
    d = json.load(open(CONTENT, encoding="utf-8"))
    ws = openpyxl.load_workbook(WORKBOOK)["2-Build-Dashboard"]
    states = cell_text(ws, "STATES")
    check = cell_text(ws, "THE CHECK")
    done = []

    for ch in d:
        for sec in ch["sections"]:
            for blk in sec["blocks"]:
                if blk.get("type") != "mono":
                    continue
                cap = blk.get("caption") or ""
                if "states requirement, verbatim" in cap and blk["text"] != states:
                    assert blk["text"].endswith(states), "states box diverges beyond the leading sentence"
                    blk["text"] = states
                    done.append("states box = workbook STATES cell")
                if "2-Build-Dashboard" in cap and "Filter to Site = Berlin" in blk["text"] and blk["text"] != check:
                    blk["text"] = check
                    done.append("acceptance-check box = workbook THE CHECK cell")

    old = ("The artifact you choose determines which requirement types matter - and a requirement "
           "is only as good as the acceptance evidence attached to it. For every type you select, "
           "write: requirement, example, evidence.")
    new = ("A requirement is only as good as the acceptance evidence attached to it. "
           "For every type you select, write: requirement, example, evidence.")
    hits = [b for ch in d for s in ch["sections"] for b in s["blocks"] if b.get("type") == "callout" and b.get("body") == old]
    assert len(hits) <= 1, "closing callout matched more than once"
    if hits:
        hits[0]["body"] = new
        done.append("Chapter 4 closing callout trimmed to its new content")

    json.dump(d, open(CONTENT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("applied:", done if done else "nothing (already applied)")

    # post-conditions
    monos = [b for ch in d for s in ch["sections"] for b in s["blocks"] if b.get("type") == "mono"]
    assert any(b["text"] == states for b in monos) and any(b["text"] == check for b in monos)
    assert not any(b.get("body") == old for ch in d for s in ch["sections"] for b in s["blocks"])
    print("post-conditions ok")


if __name__ == "__main__":
    main()
