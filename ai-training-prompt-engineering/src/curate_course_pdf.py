#!/usr/bin/env python3
"""Curate the extended Course PDF against the current deck (owner-directed,
2026-09-18): the exercise prompt boxes in the written course must carry the
approved wording from channel instruction 21 (the same text now on the
slides), not the pre-revision drafts. Content is edited in
src/assets/course_content.json; build_course_pdf.py renders it.

Only the seven prompt monos (and their captions where they describe the old
flow) change; all other prose stays.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "assets", "course_content.json")

sys.path.insert(0, HERE)
from build_v08 import P1, P2, P3, P4, P5, P6, P7  # approved wording, verbatim


def fmt(sends):
    lines = []
    for label, text in sends:
        lines.append((f"{label}: " if label else "") + text)
    return "\n".join(lines)


def main():
    d = json.load(open(CONTENT, encoding="utf-8"))

    # (chapter, section, block, sends, new caption or None to keep)
    targets = [
        (0, 0, 3, P1, "Tab EX1-TwoModes - run all three sends in one chat, and keep that chat: it is your course log."),
        (0, 2, 3, P2, None),
        (0, 3, 3, P3, None),
        (0, 4, 5, P4, None),
        (0, 6, 7, P6, None),
        (1, 1, 7, P7, None),
    ]
    for ci, si, bi, sends, cap in targets:
        blk = d[ci]["sections"][si]["blocks"][bi]
        assert blk.get("type") == "mono", (ci, si, bi, blk.get("type"))
        old = blk["text"]
        blk["text"] = fmt(sends)
        if cap:
            blk["caption"] = cap
        print(f"ch{ci} sec{si} blk{bi}: replaced ({len(old)} -> {len(blk['text'])} chars)")

    # EX5 (fast vs reasoning): find its mono by caption and replace
    hits = 0
    for ci, ch in enumerate(d):
        for si, sec in enumerate(ch.get("sections", [])):
            for bi, blk in enumerate(sec.get("blocks", [])):
                if blk.get("type") == "mono" and "EX5" in str(blk.get("caption", "")):
                    blk["text"] = fmt(P5)
                    hits += 1
                    print(f"ch{ci} sec{si} blk{bi}: EX5 replaced")
    print("EX5 monos replaced:", hits)

    json.dump(d, open(CONTENT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("content saved; rebuilding PDF")
    subprocess.run([sys.executable, os.path.join(HERE, "build_course_pdf.py")], check=True)


if __name__ == "__main__":
    main()
