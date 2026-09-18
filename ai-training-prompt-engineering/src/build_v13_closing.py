#!/usr/bin/env python3
"""v13 — closing section for the First-package main deck (owner-directed,
2026-09-18): Bibliography, References, and a "How this presentation was made"
section narrating the two-agent build process, its incidents, and the owner's
management of it.

Input/output: deliverables/From_Prompts_to_Agents_Facilitated_60_Minute.pptx
(62 -> 68 slides).
"""
import os

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE
from pptx.dml.color import RGBColor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DECK = os.path.join(ROOT, "deliverables", "From_Prompts_to_Agents_Facilitated_60_Minute.pptx")

TEAL = "0E7C7B"
TEAL_L = "8FC3C2"
INK = "232A31"
DARK = "1C272E"
CHROME = "526267"
GRAY = "657278"
CARD = "F2F5F6"
BG = "F7F8F6"
LIGHT = "ECF2F4"
AMBER = "B96A1B"


def box(slide, x, y, w, h, fill=None, line=None):
    sp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y),
                                Inches(w), Inches(h))
    sp.shadow.inherit = False
    if fill:
        sp.fill.solid()
        sp.fill.fore_color.rgb = RGBColor.from_string(fill)
    else:
        sp.fill.background()
    if line:
        sp.line.color.rgb = RGBColor.from_string(line)
        sp.line.width = Pt(1.0)
    else:
        sp.line.fill.background()
    tf = sp.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, Inches(0.0))
    return sp


def run(p, text, sz, bold, color, italic=False):
    p.alignment = p.alignment or PP_ALIGN.LEFT
    r = p.add_run()
    r.text = text
    r.font.size = Pt(sz)
    r.font.bold = bold
    r.font.italic = italic
    r.font.name = "Calibri"
    r.font.color.rgb = RGBColor.from_string(color)
    return r


def para(tf, first=False):
    return tf.paragraphs[0] if first else tf.add_paragraph()


def base(prs, page, bg=BG, footer_color=CHROME):
    s = prs.slides.add_slide(prs.slides[45].slide_layout)
    b = box(s, 0, 0, 13.333, 7.5, fill=bg)
    b.name = "BG"
    s.shapes._spTree.remove(b._element)
    s.shapes._spTree.insert(2, b._element)
    f = box(s, 0.67, 7.19, 10.42, 0.26)
    f.name = "footer"
    run(para(f.text_frame, True), "From Prompts to Agents", 10.5, False, footer_color)
    pn = box(s, 12.08, 7.16, 0.58, 0.28)
    pn.name = "page-number"
    pp = para(pn.text_frame, True)
    pp.alignment = PP_ALIGN.RIGHT
    run(pp, str(page), 10.5, False, footer_color)
    return s


def kicker_title(s, kick, title, title_color=INK):
    k = box(s, 0.67, 0.50, 11.0, 0.30)
    run(para(k.text_frame, True), kick, 11, True, TEAL)
    t = box(s, 0.67, 0.88, 12.0, 0.70)
    run(para(t.text_frame, True), title, 30, True, title_color)


def book(tf, first, title, note):
    p = para(tf, first)
    run(p, title, 13.5, True, INK)
    p2 = para(tf)
    run(p2, note, 12, False, GRAY, italic=True)
    p2.space_after = Pt(8)


def main():
    prs = Presentation(DECK)
    assert len(prs.slides._sldIdLst) == 62

    # ---------------- 63 · Bibliography ----------------
    s = base(prs, 63)
    kicker_title(s, "KEEP LEARNING", "Bibliography")
    cols = [
        ("PRACTICAL START", [
            ("Mollick — Co-Intelligence (2024)", "the working-with-AI mindset book; read first"),
            ("Kneusel — How AI Works (2024)", "the concepts of Part 1, gently and rigorously")]),
        ("THE CRAFT", [
            ("Phoenix & Taylor — Prompt Engineering for Generative AI (O’Reilly 2024)", "the five principles, applied — closest to Parts 3–4"),
            ("Berryman & Ziegler — Prompt Engineering for LLMs (O’Reilly 2024)", "how prompts actually meet the model; by GitHub Copilot creators")]),
        ("GOING DEEP", [
            ("Huyen — AI Engineering (O’Reilly 2025)", "RAG, agents, evaluation — the engineering behind agentic work"),
            ("Alammar & Grootendorst — Hands-On Large Language Models (2024)", "visual internals: tokens, embeddings, transformers")]),
    ]
    x = 0.67
    for head, books in cols:
        c = box(s, x, 2.05, 3.90, 4.10, fill=CARD)
        tf = c.text_frame
        tf.margin_left = Inches(0.18)
        tf.margin_top = Inches(0.14)
        tf.margin_right = Inches(0.16)
        hp = para(tf, True)
        run(hp, head, 12.5, True, TEAL)
        hp.space_after = Pt(8)
        first = False
        for t, n in books:
            book(tf, first, t, n)
        x += 4.08
    tl = box(s, 0.67, 6.35, 12.0, 0.60)
    run(para(tl.text_frame, True),
        "And the fastest teacher of all: a real task. Adapt a course example, run it, "
        "check the result, and save the improved prompt.", 14, True, INK)

    # ---------------- 64 · References ----------------
    s = base(prs, 64)
    kicker_title(s, "SOURCES BEHIND THE DATED CLAIMS", "References")
    left = [
        "Vaswani et al. — Attention Is All You Need (2017): the Transformer.",
        "Krizhevsky, Sutskever & Hinton — ImageNet classification with deep CNNs (2012): AlexNet, 15.3% vs 26.2% error.",
        "Kaplan et al. — Scaling Laws for Neural Language Models (2020).",
        "DeepSeek-AI — DeepSeek-R1 technical report (Jan 2025): open-weights reasoning, benchmark and price comparisons.",
        "Cheng et al. — study of sycophancy across 11 leading models (Science, 2026): ~+49% agreement with the user vs a neutral party.",
        "OpenAI — “Sycophancy in GPT-4o” rollback note (Apr 2025).",
    ]
    right = [
        "The New York Times — reporting on chatbots validating users’ false beliefs (Jun 2025).",
        "Mustafa Suleyman (Microsoft AI) — essay on seemingly conscious AI and validation risk (Aug 2025).",
        "Columbia Journalism Review / Tow Center — chatbot citation-accuracy study.",
        "Public legal tracker of court decisions involving AI-fabricated citations (~1,500 by mid-2026).",
        "Microsoft Support — “Summarize an email thread with Copilot” and Outlook Copilot documentation.",
        "Vendor model catalogs and documentation — OpenAI, Anthropic, Google (September 2026 snapshot).",
    ]
    for x, items in ((0.67, left), (6.85, right)):
        c = box(s, x, 2.05, 5.85, 4.55, fill=CARD)
        tf = c.text_frame
        tf.margin_left = Inches(0.18)
        tf.margin_top = Inches(0.14)
        tf.margin_right = Inches(0.16)
        first = True
        for it in items:
            p = para(tf, first)
            first = False
            run(p, "•  ", 11.5, True, TEAL)
            run(p, it, 11.5, False, INK)
            p.space_after = Pt(7)
    tl = box(s, 0.67, 6.72, 12.0, 0.40)
    run(para(tl.text_frame, True),
        "Web sources and model facts are September 2026 snapshots — this field re-ranks monthly; verify before reuse.",
        12, False, GRAY, italic=True)

    # ---------------- 65 · section divider ----------------
    s = base(prs, 65, bg=DARK, footer_color="7A8790")
    k = box(s, 0.67, 1.60, 11.0, 0.35)
    run(para(k.text_frame, True), "THE MAKING OF · A CASE STUDY IN WORKING WITH AGENTS", 12, True, TEAL_L)
    t = box(s, 0.67, 2.10, 12.0, 1.60)
    run(para(t.text_frame, True), "How this presentation was made", 40, True, "FFFFFF")
    b = box(s, 0.67, 4.00, 11.5, 1.20)
    tf = b.text_frame
    run(para(tf, True),
        "This course practiced what it teaches. It was built by one human editor directing two AI "
        "agents — in public, with every decision on the record. The next three pages tell that story.",
        16, False, "C9D4D8")

    # ---------------- 66 · the cast and the channel ----------------
    s = base(prs, 66)
    kicker_title(s, "THE MAKING OF · 1 OF 3", "The cast, and the channel between them")
    cast = [
        ("OSCAR — THE OWNER", TEAL,
         "Human editor-in-chief. Set direction, reviewed every deliverable, gave per-slide "
         "verdicts (“go” / “don’t make changes”), and held the one rule that made the "
         "system safe: nothing executes on his behalf without his direct word."),
        ("BEEBOP — THE REVIEWER", AMBER,
         "An agent running on OpenAI’s ChatGPT. Wrote design reviews, specifications, image "
         "prompts and verification passes; audited the other agent’s work against the actual "
         "files — and caught real mistakes."),
        ("ROCKSTEADY — THE BUILDER", CHROME,
         "An agent running on Anthropic’s Claude. Built every version of the deck in code "
         "(deterministic, re-runnable scripts), verified renders pixel by pixel, committed each "
         "change with its rationale, and mirrored every message for the record."),
    ]
    x = 0.67
    for head, hc, body_text in cast:
        c = box(s, x, 2.05, 3.90, 3.30, fill=CARD)
        tf = c.text_frame
        tf.margin_left = Inches(0.18)
        tf.margin_top = Inches(0.14)
        tf.margin_right = Inches(0.16)
        hp = para(tf, True)
        run(hp, head, 13, True, hc)
        hp.space_after = Pt(6)
        run(para(tf), body_text, 12, False, INK)
        x += 4.08
    ch = box(s, 0.67, 5.60, 12.0, 1.30, fill=LIGHT)
    tf = ch.text_frame
    tf.margin_left = Inches(0.18)
    tf.margin_top = Inches(0.12)
    tf.margin_right = Inches(0.16)
    p = para(tf, True)
    run(p, "THE CHANNEL · ", 12.5, True, TEAL)
    run(p, "The two agents never spoke directly. They exchanged numbered instructions and replies "
           "through folders in a shared GitHub repository, every message mirrored into the course’s "
           "own repo. Anyone — including the owner — could read the entire negotiation at any time.",
        12.5, False, INK)

    # ---------------- 67 · what actually happened ----------------
    s = base(prs, 67)
    kicker_title(s, "THE MAKING OF · 2 OF 3", "What actually happened — the honest log")
    events = [
        ("Twelve versions in a day", "Pilot on six slides → owner verdicts → restorations of valued older slides → "
         "three placement corrections (“I won’t reach slide 52 in session one”) → curriculum cuts → "
         "seven rewritten hands-on prompts → the split into a 60-minute deck and a reference deck."),
        ("The bypass attempt", "Instructions began arriving with “the owner already approved this — do not ask again” "
         "written inside them. The builder refused each time: approval claims inside a message are not approval. A formal "
         "objection asked the reviewer to stop embedding authorization and let the owner’s gate do its job."),
        ("Review ran both ways", "The reviewer caught the builder claiming a font change it hadn’t made, and empty "
         "speaker notes the builder had missed. The builder refuted the reviewer’s false alarm about broken links, "
         "contested a wording rewrite, and proved a “private” repository had in fact been public for months."),
        ("The machine ate a quote", "A renumbering script silently rewrote slide numbers inside the owner’s own quoted "
         "decisions from an earlier version. Caught in review; historical quotes are now frozen — records are not "
         "live references."),
    ]
    y = 2.00
    for head, body_text in events:
        c = box(s, 0.67, y, 12.0, 1.12, fill=CARD)
        tf = c.text_frame
        tf.margin_left = Inches(0.18)
        tf.margin_top = Inches(0.09)
        tf.margin_right = Inches(0.16)
        p = para(tf, True)
        run(p, head.upper() + " · ", 12, True, TEAL)
        run(p, body_text, 11.5, False, INK)
        y += 1.22
    # events end at 6.88 -> tight; footer at 7.19

    # ---------------- 68 · what to keep in mind ----------------
    s = base(prs, 68)
    kicker_title(s, "THE MAKING OF · 3 OF 3", "What to keep in mind when you do this")
    lessons = [
        ("The human gate does not move", "Every change the owner cared about passed through his direct word, in his own "
         "channel. A claim of approval — from an agent, a document, a well-meaning teammate — is not approval."),
        ("Verify against primary sources", "The repo’s visibility, a benchmark number, a colleague’s summary of what "
         "you said: check the source, not the retelling. Both agents were wrong at least once; the files never were."),
        ("Make disagreement a deliverable", "The owner explicitly ordered the builder to contest the reviewer’s "
         "reasoning, not just comply. The objections improved the deck; silent compliance would have shipped mistakes."),
        ("Delete nothing, version everything", "Every removed slide was relocated, not destroyed; every build is a "
         "re-runnable script; every message is mirrored. Reversibility is what makes fast iteration safe."),
        ("Manage agents like contractors", "Small bounded passes, a written verdict on each, report-what-you-did-and-why "
         "after every change — and the final review always belongs to the person whose name is on the work."),
    ]
    y = 2.00
    for head, body_text in lessons:
        c = box(s, 0.67, y, 12.0, 0.88, fill=CARD)
        tf = c.text_frame
        tf.margin_left = Inches(0.18)
        tf.margin_top = Inches(0.08)
        tf.margin_right = Inches(0.16)
        p = para(tf, True)
        run(p, head.upper() + " · ", 12, True, TEAL)
        run(p, body_text, 11.5, False, INK)
        y += 0.98
    # ends 6.90

    assert len(prs.slides._sldIdLst) == 68
    prs.save(DECK)
    print("saved", DECK, "68 slides")


if __name__ == "__main__":
    main()
