#!/usr/bin/env python3
"""Builds the first-pass report PDF for the GLADIATOR app project.

Output: gladiator-game-app/Gladiator-App-First-Pass-Report.pdf

The report is a decision workbook for the game's creator:
  Part 1 - the game as we understood it (for correction)
  Part 2 - how the app could be built (options + recommended path)
  Part 3 - 35 numbered decisions, each with ready-made lettered options
  Quick answer sheet + next steps

Content rules: stick to WinAnsi-safe characters (no arrows, no check marks,
no angle brackets or ampersands inside Paragraph markup).
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable, NextPageTemplate,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "Gladiator-App-First-Pass-Report.pdf")

ACCENT = colors.HexColor("#8B2F2F")   # arena brick red
INK = colors.HexColor("#26231E")
FAINT = colors.HexColor("#7C7466")
PARCH = colors.HexColor("#F4EDDF")    # parchment fill
LINE = colors.HexColor("#D8CDB8")

PAGE_W, PAGE_H = letter
M = 52  # margin

# ---------------------------------------------------------------- styles
def st(name, **kw):
    base = dict(fontName="Helvetica", fontSize=9.5, leading=13.5, textColor=INK)
    base.update(kw)
    return ParagraphStyle(name, **base)

S = {
    "cover_kicker": st("cover_kicker", fontSize=13, leading=16, textColor=FAINT,
                       alignment=1, fontName="Helvetica"),
    "cover_title": st("cover_title", fontName="Helvetica-Bold", fontSize=44,
                      leading=48, textColor=ACCENT, alignment=1),
    "cover_sub": st("cover_sub", fontSize=14, leading=19, alignment=1),
    "cover_meta": st("cover_meta", fontSize=10, leading=15, textColor=FAINT, alignment=1),
    "h1": st("h1", fontName="Helvetica-Bold", fontSize=17, leading=21,
             textColor=ACCENT, spaceBefore=6, spaceAfter=4),
    "h2": st("h2", fontName="Helvetica-Bold", fontSize=12, leading=15,
             spaceBefore=10, spaceAfter=3),
    "body": st("body", spaceAfter=5),
    "lead": st("lead", fontSize=10.5, leading=15, spaceAfter=6),
    "bullet": st("bullet", leftIndent=14, spaceAfter=3),
    "qtitle": st("qtitle", fontName="Helvetica-Bold", fontSize=10.5, leading=14,
                 textColor=ACCENT, spaceBefore=2),
    "qtext": st("qtext", spaceAfter=3),
    "opt": st("opt", leftIndent=16, spaceAfter=2.5),
    "write": st("write", leftIndent=16, textColor=FAINT, spaceAfter=2),
    "note": st("note", fontSize=8.5, leading=11.5, textColor=FAINT, leftIndent=16),
    "tcell": st("tcell", fontSize=8.8, leading=11.5),
    "tcell_b": st("tcell_b", fontSize=8.8, leading=11.5, fontName="Helvetica-Bold"),
    "small": st("small", fontSize=8.5, leading=11.5, textColor=FAINT),
}

def P(text, style="body"):
    return Paragraph(text, S[style])

def rule(space_before=4, space_after=8, color=LINE, thick=0.8):
    return HRFlowable(width="100%", thickness=thick, color=color,
                      spaceBefore=space_before, spaceAfter=space_after)

def blank_line(label="Notes"):
    if label is None:
        return P("_" * 86, "write")
    return P(f"{label}: " + "_" * 80, "write")

def table(data, widths, header=True, pad=4):
    rows = [[P(c, "tcell_b") if header and r == 0 else P(c, "tcell")
             for c in row] for r, row in enumerate(data)]
    t = Table(rows, colWidths=widths, repeatRows=1 if header else 0)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.6, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), pad + 1),
        ("RIGHTPADDING", (0, 0), (-1, -1), pad + 1),
        ("TOPPADDING", (0, 0), (-1, -1), pad),
        ("BOTTOMPADDING", (0, 0), (-1, -1), pad),
    ]
    if header:
        style.append(("BACKGROUND", (0, 0), (-1, 0), PARCH))
    t.setStyle(TableStyle(style))
    return t

SUG = f' <font color="#8B2F2F"><b>[suggested]</b></font>'

def question_block(num, title, qtext, options, note=None, freetext=True,
                   other_label="Other / your ruling"):
    flow = [P(f"Q{num} · {title}", "qtitle")]
    if qtext:
        flow.append(P(qtext, "qtext"))
    if note:
        flow.append(P(note, "note"))
        flow.append(Spacer(1, 2))
    for letter_, text, sug in options:
        mark = SUG if sug else ""
        flow.append(P(f"(&nbsp;&nbsp;)&nbsp; <b>{letter_}.</b> {text}{mark}", "opt"))
    if freetext:
        flow.append(P(f"(&nbsp;&nbsp;)&nbsp; <b>{other_label}:</b> " + "_" * 58, "opt"))
        flow.append(blank_line())
    flow.append(Spacer(1, 7))
    return KeepTogether(flow)

# ---------------------------------------------------------------- page furniture
def draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.6)
    canvas.line(M, 40, PAGE_W - M, 40)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(FAINT)
    canvas.drawString(M, 28, "GLADIATOR — First-Pass App Report and Decision Workbook")
    canvas.drawRightString(PAGE_W - M, 28, f"Page {doc.page}")
    canvas.restoreState()

def draw_cover(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(2)
    canvas.line(M, PAGE_H - 130, PAGE_W - M, PAGE_H - 130)
    canvas.line(M, 118, PAGE_W - M, 118)
    canvas.restoreState()

# ---------------------------------------------------------------- document
doc = BaseDocTemplate(os.path.abspath(OUT), pagesize=letter,
                      leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=56,
                      title="Gladiator — First-Pass App Report",
                      author="Gladiator app project")
frame = Frame(M, 56, PAGE_W - 2 * M, PAGE_H - M - 56, id="main")
cover_frame = Frame(M, 56, PAGE_W - 2 * M, PAGE_H - M - 56, id="cover")
doc.addPageTemplates([
    PageTemplate(id="cover", frames=[cover_frame], onPage=draw_cover),
    PageTemplate(id="content", frames=[frame], onPage=draw_footer),
])

E = []  # elements

# ================================================================ COVER
E.append(Spacer(1, 130))
E.append(P("From the table to the phone", "cover_kicker"))
E.append(Spacer(1, 10))
E.append(P("GLADIATOR", "cover_title"))
E.append(Spacer(1, 6))
E.append(P("First-Pass App Report — and a Decision Workbook for the Creator", "cover_sub"))
E.append(Spacer(1, 26))
E.append(P("Based on a full review of: rulebook v5.0 · all 216 print-sheet cards · the Hades deck",
           "cover_meta"))
E.append(P("July 2026", "cover_meta"))
E.append(Spacer(1, 46))
E.append(P("<b>How to use this document</b>", "cover_sub"))
E.append(Spacer(1, 6))
for line in [
    "<b>Part 1</b> — the game as we understood it. Please check us.",
    "<b>Part 2</b> — the ways the app could be built, and the path we recommend.",
    "<b>Part 3</b> — 35 decisions. Each comes with ready-made options:",
    "mark a circle, or write your own ruling. Options tagged",
    '<font color="#8B2F2F"><b>[suggested]</b></font> are our proposed defaults — '
    '"all suggested defaults except..." is a perfect reply.',
]:
    E.append(Paragraph(line, ParagraphStyle("c", parent=S["cover_meta"], textColor=INK)))
E.append(NextPageTemplate("content"))
E.append(PageBreak())

# ================================================================ PART 1
E.append(P("Part 1 — The game as we understood it", "h1"))
E.append(rule())
E.append(P(
    "We reviewed the v5.0 rulebook, the complete card print sheets, and the Hades deck, "
    "with the goal of turning Gladiator into an app where 2–6 players connect and play "
    "from their own phones. Everything below is our reading of your game. <b>If anything "
    "here is wrong, correct it directly on the page — the app will follow this spec.</b>", "lead"))

E.append(P("The materials are in excellent shape", "h2"))
E.append(P(
    "We counted every card in the print sheets against the rulebook's component list and "
    "they match exactly: 33 gladiator cards, 117 equipment cards (50 weapons, 37 armor, "
    "24 specials, 6 legendaries), 30 attack cards, 30 Hades cards — 210 playable cards "
    "plus 6 player aids. Stats on the cards match the rulebook tables everywhere we "
    "cross-checked. That internal consistency makes the game very codeable.", "body"))

E.append(P("The game loop", "h2"))
for b in [
    "<b>1.</b> Each player commands one Gladiator (drawn at random; one exchange allowed per round).",
    "<b>2.</b> Each turn has two phases for every player: an <b>Equip Phase</b> — collect 30 denarii, "
    "optionally sell (half cost) or refresh the Market for 20, then draw 1 card <b>or</b> buy up to 2 "
    "from the 3-card Market, and arrange equipment freely (hand limit 6) — then an <b>Attack Phase</b>.",
    "<b>3.</b> In the Attack Phase you draw an Attack card (Left / Right / Your Choice / Pass; skipped "
    "in 2-player games) and roll one d6 against the target's dodge: a roll of the dodge value or less "
    "misses; a 6 is an auto-hit that ignores armor; anything else hits for total attack minus total "
    "armor. Damage rounds up to the nearest 5; every hit deals at least 5. Unarmed fists attack at 10. "
    "Dodge is hard-capped at 4.",
    "<b>4.</b> At 0 VITA, the Sacred Coin decides: heads — the Emperor revives you at 30 VITA (once "
    "per round); tails — eliminated. If you die before acting in a turn, a second flip may grant a "
    "dying blow against your killer (Furor Mortis).",
    "<b>5.</b> Eliminated players are not out: each Attack Phase they draw a Hades card — sometimes "
    "just watching from the underworld, sometimes cursing all living gladiators (Wrath) or one chosen "
    "target (Whisper).",
    "<b>6.</b> Last gladiator standing wins the round and a laurel; the first to 3 laurels is Champion "
    "of the Arena. Everything but laurels resets between rounds.",
]:
    E.append(P(b, "bullet"))

E.append(P("What makes the digital version interesting", "h2"))
E.append(P(
    "Several cards interrupt the normal flow: Aqua Vitae and the Medicus Scroll heal “at any "
    "time, including after taking damage”; the Flagrum forces the <i>defender</i> to choose a "
    "discard mid-attack; Lorica Hephaesti can negate a hit as it lands; Harena and Furor are "
    "declared between the attack-card draw and the die roll. On phones this means short "
    "<b>reaction prompts</b> that pop up on another player's screen before the attack resolves — "
    "a solved problem in digital card games, but one that shapes the technology choice in Part 2 "
    "and questions Q19 and Q22.", "body"))
E.append(Spacer(1, 4))
E.append(P("Corrections to Part 1 (if any):", "qtitle"))
E.append(Spacer(1, 4))
E.append(blank_line(None))
E.append(Spacer(1, 6))
E.append(blank_line(None))
E.append(PageBreak())

# ================================================================ PART 2
E.append(P("Part 2 — The ways the app could be built", "h1"))
E.append(rule())
E.append(P(
    "Building this is four stacked choices, not one. For each layer we list the realistic "
    "options and mark the one we recommend. You do not need to be technical to decide here — "
    "the trade-offs are about <b>how players reach the game</b> and <b>how much it costs to "
    "iterate</b>; we handle the engineering either way.", "lead"))

E.append(P("Layer 0 — The rules engine (needed in every scenario)", "h2"))
E.append(P(
    "The heart of the app is your rulebook translated into one strict, isolated piece of "
    "software with every card's data in a simple editable file. It is written once and reused "
    "by every option below. Two properties matter to you directly: <b>(a)</b> card stats and "
    "counts live in a data file you can tune without a programmer — a balance patch is a number "
    "edit; <b>(b)</b> all dice, coin flips, and shuffles happen on the server with a reproducible "
    "seed — fair, cheat-proof, and every game can be replayed for dispute or bug reports.", "body"))

E.append(KeepTogether([P("Layer 1 — What runs on each phone", "h2"), table([
    ["Option", "The case for it", "The case against it"],
    ["<b>1A. Web app (PWA)</b> — players open a link, "
     "no install<br/><font color='#8B2F2F'><b>[recommended first]</b></font>",
     "Zero friction (everyone's phone already has it); one codebase; updates are instant; "
     "cheapest; perfect for playtesting",
     "No app-store listing; iPhone notifications are weaker than a real app"],
    ["<b>1B. Store app</b> (React Native or Flutter)",
     "App Store and Google Play presence; reliable notifications; native feel",
     "Store fees and review delays; players must install before playing; slower iteration"],
    ["<b>1C. Game engine</b> (Unity or Godot)",
     "The most spectacular animations (3D arena, physics dice)",
     "Heaviest cost and skill set; overkill for a card game's logic; slow to test rules"],
    ["<b>1D. Web first, wrap later</b><br/><font color='#8B2F2F'><b>[recommended path]</b></font>",
     "Start as 1A; when store presence matters, the same code is wrapped (Capacitor) and "
     "shipped to both stores",
     "Until wrapped, lives with 1A's limits"],
], [150, 178, 180])]))

E.append(KeepTogether([P("Layer 2 — Where the shared game lives", "h2"), table([
    ["Option", "Verdict for this game"],
    ["<b>2A. Our own small game server</b> (rooms with join codes; the server owns all state, "
     "dice, and hidden hands)<br/><font color='#8B2F2F'><b>[recommended]</b></font>",
     "Best fit. Hidden hands stay genuinely hidden, cheating is impossible by design, and the "
     "mid-attack reaction prompts are instant. Costs roughly 5–20 USD per month at playtest scale."],
    ["<b>2B. Turn-based-game framework</b> (boardgame.io)",
     "Fast start, purpose-built for card games — worth a short trial — but the project's "
     "maintenance has slowed and its turn model needs bending for reaction windows."],
    ["<b>2C. App-database sync</b> (Firebase / Supabase)",
     "Quick demos, but authoritative rules end up bolted on awkwardly; easy to end up trusting "
     "players' phones with secrets. Not recommended for this design."],
    ["<b>2D. Hosted game platforms</b> (Photon, Nakama)",
     "Adds cost and lock-in aimed at real-time action games; our rules engine must be embedded "
     "anyway. Unnecessary at this scale."],
    ["<b>2E. Phone-to-phone, no server</b>",
     "Fragile connections, the game dies if the host's phone sleeps, and cheating is possible. "
     "Not recommended."],
], [220, 288])]))

E.append(KeepTogether([P("Layer 3 — How people gather", "h2"), table([
    ["Mode", "Notes"],
    ["<b>Room codes</b> — host shares a short code; everyone joins from anywhere"
     "<br/><font color='#8B2F2F'><b>[the v1 core]</b></font>",
     "Covers both remote play and everyone-around-the-table play (the app replaces cards, "
     "dice, coins, and health trackers; the table talk stays human)."],
    ["<b>Pass-and-play</b> — one phone passed around",
     "Nearly free to build once the engine exists; our first playable prototype."],
    ["<b>Shared arena screen</b> — a TV or laptop shows the public arena; phones hold "
     "private hands (Jackbox style)",
     "A crowd-pleaser for demos and game nights; a natural later phase."],
    ["<b>Async play</b> — turns over hours with notifications",
     "Possible later; every reaction window needs an auto-resolve rule first (see Q20)."],
    ["<b>Practice vs. bots</b>",
     "Optional later; simple opponents are easy, clever ones are a project of their own."],
], [220, 288])]))

E.append(KeepTogether([P("The recommended path, in phases", "h2"), table([
    ["Phase", "What exists at the end", "Rough scale"],
    ["<b>0. Lock the spec</b>", "Your answers to Part 3 folded in; the card data file "
     "confirmed as the single source of truth", "days"],
    ["<b>1. Engine + hot-seat</b>", "The full rules playable on one phone passed around — "
     "proves the game feels right on a screen before any network work", "2–4 weeks"],
    ["<b>2. Online rooms (real MVP)</b>", "Create or join by code from any phone; server "
     "dice; reaction prompts; reconnects; full first-to-3-laurels matches", "4–8 weeks"],
    ["<b>3. Polish and reach</b>", "Animation and sound for the die and Sacred Coin, shared "
     "arena screen, app-store wrap, optional accounts and stats", "open-ended"],
], [118, 310, 80])]))
E.append(P(
    "Scale assumes one experienced developer. Running costs until stores/accounts: a domain "
    "plus roughly 5–20 USD per month of hosting.", "small"))
E.append(Spacer(1, 8))
E.append(KeepTogether([
    P("Your call on Part 2:", "qtitle"),
    P("(&nbsp;&nbsp;)&nbsp; <b>Approve</b> the recommended path (web-first, room codes, phased)" + SUG, "opt"),
    P("(&nbsp;&nbsp;)&nbsp; <b>Discuss alternatives first</b> — flag what you want to talk through", "opt"),
    blank_line(),
]))
E.append(PageBreak())

# ================================================================ PART 3
E.append(P("Part 3 — The 35 decisions", "h1"))
E.append(rule())
E.append(P(
    "Section A settles rules edge cases (a human table shrugs; software cannot). Section B "
    "shapes how the paper game behaves on phones. Section C sets product direction. Numbering "
    "matches our project files, so “Q7: option B” is all we need.", "lead"))

E.append(P("Section A — Rules of the arena", "h2"))

E.append(question_block(1, "Starting money",
    "The rulebook doesn't state starting cash; income is 30 denarii each Equip Phase.",
    [("A", "Start at 0 — the first 30 arrive in your first Equip Phase.", True),
     ("B", "Start with 30 denarii.", False),
     ("C", "Start with 50 denarii.", False)]))

E.append(question_block(2, "Beast weapons: one roll or two?",
    "Leo (die x 10), Ursus (x 8), Canis (x 5) and Cerberus (x 8) deal die-based damage, and "
    "the rulebook says “one die roll does it all.”",
    [("A", "One roll: the same d6 both decides the hit and sets the damage. Leo on a 4 against "
      "dodge 2 = 40 damage; a 6 is an auto-hit dealing 60. Paired with a fixed weapon, that one "
      "roll prices the beast (Ursus + Gladius on a 4 = 32 + 50).", True),
     ("B", "Two rolls: first d6 to hit, then a separate d6 for the beast's damage.", False)]))

E.append(question_block(3, "Damage arithmetic, in order",
    "Confirm the exact math the app performs on a normal hit.",
    [("A", "Total attack minus total armor, round UP to the nearest 5, minimum 5 on any "
      "successful hit — and die-based damage rounds the same way (Ursus rolling 3 = 24, "
      "becomes 25).", True),
     ("B", "As A, but die-based damage is used raw (24 stays 24).", False)]))

E.append(question_block(4, "Attack Left / Right into an eliminated neighbor",
    "The card points at a dead player's seat. What happens?",
    [("A", "The attack passes along to the next LIVING gladiator in that direction.", True),
     ("B", "The attack is wasted — nothing happens this phase.", False),
     ("C", "The attacker may choose any target instead (treat as Attack Your Choice).", False)]))

E.append(question_block(5, "Fulgur Iovis — which two players?",
    "The legendary lightning “attacks two players simultaneously” with one roll.",
    [("A", "Any two opponents of the attacker's choice; in a 2-player game it strikes the "
      "lone opponent once.", True),
     ("B", "Specifically the two adjacent players (left and right neighbors).", False),
     ("C", "As A, but in 2-player it strikes the lone opponent twice (two separate dodges).",
      False)]))

E.append(question_block(6, "Furor — how far does the +1 go?",
    "Furor adds 1 to your attack roll (“a 5 becomes 6, triggering an auto-hit”).",
    [("A", "The +1 applies to everything the roll does: beating dodge, reaching the auto-hit 6, "
      "and beast damage (a 5 with Leo becomes a 6: auto-hit, 60 damage).", True),
     ("B", "The +1 only converts a natural 5 into an auto-hit; dodge comparison and beast "
      "damage use the natural roll.", False)]))

E.append(question_block(7, "The exact death sequence at 0 VITA",
    "Order of operations when a gladiator drops to 0.",
    [("A", "As written, strictly: at 0 the Sacred Coin flips immediately — healing potions "
      "cannot be played at 0 (they only work while above 0). First death of the round: "
      "Emperor's Favor coin (heads = revive at 30). If eliminated before having acted this "
      "turn: Furor Mortis coin (heads = one dying attack on the killer) — and this applies on "
      "ANY death, including the second. Then to Hades.", True),
     ("B", "As A, but a player MAY play Aqua Vitae / Medicus at exactly 0 to avoid the flip.",
      False),
     ("C", "As A, but Furor Mortis can only trigger on the first death of the round.", False)]))

E.append(question_block(8, "Interceptio — the stolen gear",
    "Interceptio removes one equipped one-handed weapon or armor from an opponent, who "
    "receives half its sell value.",
    [("A", "The stripped card goes to the discard pile. It cannot take Retiarius' bound Rete, "
      "cannot take Legendaries, and two-handed weapons are immune (the card says one-handed).",
      True),
     ("B", "As A, but the saboteur KEEPS the stripped card in hand.", False),
     ("C", "As A, but Legendaries CAN be stripped.", False)]))

E.append(question_block(9, "Stacking dodge penalties",
    "Rete, Harena, and several Hades cards each reduce dodge by 1 (minimum 1).",
    [("A", "They stack — two sources take dodge 3 to 1 — never below 1. Galea cancels only "
      "the Rete's penalty, as printed.", True),
     ("B", "They stack, and Galea cancels ALL dodge penalties, not just the net's.", False),
     ("C", "They do not stack — only the single strongest penalty applies.", False)]))

E.append(question_block(10, "Bestia and dodge gifts",
    "Bestia “never dodges.” What if it equips Talaria Mercurii (+2 dodge)?",
    [("A", "Never means never — Bestia cannot gain dodge from any source.", True),
     ("B", "Bestia counts as dodge 0, so Talaria raises it to 2.", False)]))

E.append(question_block(11, "Ensis Martis' bonus attack (and Velox)",
    "On a successful hit the Blade of Mars grants “draw and immediately play an extra "
    "attack card.”",
    [("A", "The bonus is exactly one extra attack card, played at once. Velox's draw-2-pick-1 "
      "does NOT apply to it, and a bonus attack can never chain into another bonus.", True),
     ("B", "Velox's speed applies to the bonus draw too (draw 2, pick 1).", False),
     ("C", "Chaining is allowed — every successful bonus hit draws again.", False)]))

E.append(question_block(12, "Do the dead have an Equip Phase?",
    "Eliminated players draw Hades cards in the Attack Phase.",
    [("A", "They skip the Equip Phase entirely — no income, no selling, no drawing. Their "
      "whole game is the Hades deck.", True),
     ("B", "They still collect income and may sell cards.", False)]))

E.append(question_block(13, "“Attack hits a RANDOM player”",
    "A Whisper card redirects a chosen gladiator's attack to a random player.",
    [("A", "Random among living gladiators EXCLUDING the cursed attacker.", True),
     ("B", "Random among ALL living gladiators — self-hits possible (crueler, funnier).",
      False)]))

E.append(question_block(14, "Debilis, the mystery gladiator",
    "80 VITA, dodge 1, no ability, a single copy — strictly weaker than Vulgaris. What is "
    "the intent?",
    [("A", "An intentional bad-luck draw — keep it in the random deal exactly as is.", False),
     ("B", "Leave it out of the app.", False),
     ("C", "It should have an ability — write it below.", False)],
    note="No suggested default here — this one is genuinely yours.",
    other_label="Its ability / your intent"))

E.append(question_block(15, "The gladiator exchange at setup",
    "“Once per round, after all players have drawn, you can send your Gladiator back and "
    "draw a new one.”",
    [("A", "Players decide in seating order; returned gladiators are shuffled back in, so "
      "another player might draw them.", True),
     ("B", "Everyone decides secretly and simultaneously, then redraws in seating order.",
      False),
     ("C", "Returned gladiators are out of the round entirely.", False)]))

E.append(question_block(16, "Specials and Legendaries flipped into the Market",
    "They are “discarded and redrawn” since they can only be obtained from the deck.",
    [("A", "That applies during the initial 3-card Market deal too, and a Legendary discarded "
      "this way stays out for the rest of the round (some rounds simply won't see Cerberus).",
      True),
     ("B", "Shuffle them back into the deck instead — Legendaries are never lost to a Market "
      "flip.", False)]))

E.append(question_block(17, "Selling restrictions",
    "“You cannot sell a card you drew this phase,” and sold cards are “removed "
    "from the game.”",
    [("A", "Cards drawn OR bought this phase are locked until your next turn, and removal "
      "means for the rest of the round (everything returns at the round reset).", True),
     ("B", "Only drawn cards are locked — a card bought from the Market may be resold the "
      "same phase.", False)]))

E.append(question_block(18, "Who goes first?",
    "The rulebook doesn't say who starts, or whether the start seat moves between rounds.",
    [("A", "Random first player in round 1; the starting seat rotates one place clockwise "
      "each new round.", True),
     ("B", "The previous round's winner goes first.", False),
     ("C", "The previous round's winner goes last.", False)]))

E.append(P("Section B — The game on phones", "h2"))

E.append(question_block(19, "Reaction prompts",
    "Heals played after damage, the Flagrum discard, and Hephaesti's negate all need a quick "
    "prompt on another player's phone before the attack resolves.",
    [("A", "Timed prompts of 10–15 seconds that auto-continue sensibly if ignored; each player "
      "can set “stop asking me” per card.", True),
     ("B", "No timers — the game waits as long as it takes.", False),
     ("C", "No prompts at all — the app auto-plays reactions by simple logic.", False)]))

E.append(question_block(20, "Live sessions only, or async too?",
    "Live means everyone plays at once (a 30–90 minute session). Async means turns over "
    "hours with notifications — which requires an auto-resolve rule for every reaction window.",
    [("A", "Live-only in v1, engineered so async can be added later without a rebuild.", True),
     ("B", "Async matters from day one — design for it now.", False),
     ("C", "Live only, permanently — keep it simple.", False)]))

E.append(question_block(21, "Shared arena screen",
    "A TV or laptop shows the public arena — market, health bars, the die tumbling — while "
    "phones hold private hands (Jackbox style).",
    [("A", "Yes — as a later phase, after the phones-only game is solid.", True),
     ("B", "Important enough to build into v1.", False),
     ("C", "Not interested.", False)]))

E.append(question_block(22, "Slow players and dropped connections",
    "Phones lock, players wander off, elevators eat signals.",
    [("A", "A soft 60-second turn timer that auto-passes, about 2 minutes of reconnect grace, "
      "then the room may drop the player (their gladiator is eliminated).", True),
     ("B", "No timers at all — this is a friends-only tool.", False),
     ("C", "An auto-pilot plays for the disconnected player instead of elimination.", False)]))

E.append(question_block(23, "The die and the Sacred Coin",
    "The rolls are the drama of the game — worth preserving as a ritual.",
    [("A", "The roller taps or shakes their phone to throw, with a real animation; the result "
      "itself comes from the server so it's provably fair.", True),
     ("B", "Instant results with minimal ceremony — speed over drama.", False)]))

E.append(question_block(24, "Match format",
    "The rulebook's full game is first to 3 laurels — several rounds, one sitting.",
    [("A", "Both: full matches AND a quick single-round mode; an interrupted match can be "
      "resumed by the same group for about 48 hours.", True),
     ("B", "Single rounds only in v1.", False),
     ("C", "Full matches only — that's the game.", False)]))

E.append(question_block(25, "House rules",
    "How much may a room's host bend the rulebook?",
    [("A", "A small panel: laurels to win, income per turn, timers on/off, include Debilis, "
      "include Legendaries — preset to rulebook values.", True),
     ("B", "Nothing configurable in v1 — the rulebook is the rulebook.", False)]))

E.append(question_block(26, "How strict is the app?",
    "This decides what the app fundamentally is.",
    [("A", "Full referee: the app validates every action, does all math and rolls, and makes "
      "illegal moves impossible. Nobody needs to know the rules to play.", True),
     ("B", "A loose digital table: players move cards freely as in a sandbox; the app merely "
      "displays.", False)]))

E.append(question_block(27, "Who are players, to the app?",
    "Accounts create friction but enable history.",
    [("A", "A nickname and avatar chosen per room — no accounts, no passwords in v1.", True),
     ("B", "Real accounts from day one, with persistent stats and rankings.", False)]))

E.append(P("Section C — Product direction", "h2"))

E.append(question_block(28, "What is this app, primarily?",
    "This single answer orders every other priority.",
    [("A", "A playtest and companion tool for the physical card game — grow it further only "
      "if it takes off.", True),
     ("B", "A commercial digital product in its own right.", False),
     ("C", "A marketing piece for a physical release (demo for a crowdfunding page, etc.).",
      False)]))

E.append(question_block(29, "How far do we distribute?",
    None,
    [("A", "Private web link for your circle first; public web when ready; app stores only "
      "if demand shows.", True),
     ("B", "App stores as soon as possible.", False),
     ("C", "Web only — never the stores.", False)]))

E.append(question_block(30, "Art and look",
    "The print sheets are clean text layouts. For the app's first version:",
    [("A", "Finished art / a logo exist or are coming — you'll supply files.", False),
     ("B", "No art yet — v1 ships a handsome text-first card design in the spirit of the "
      "print sheets.", True),
     ("C", "Commissioning art should be part of this project.", False)],
    other_label="Style direction (e.g. parchment and bronze, comic, minimal)"))

E.append(question_block(31, "The name",
    "“Gladiator” alone is a crowded name (a famous film, several games) — mostly a "
    "concern for app-store listings.",
    [("A", "Add a distinctive subtitle for the digital release (“Gladiator: ...” — "
      "write your favorite below).", True),
     ("B", "Keep plain “Gladiator” and deal with it if we reach the stores.", False),
     ("C", "A different or expanded name already exists — write it below.", False)]))

E.append(question_block(32, "Money",
    None,
    [("A", "Free while playtesting; decide monetization only if the game takes off.", True),
     ("B", "One-time purchase.", False),
     ("C", "Free core game plus paid cosmetics or expansions (the Hades deck points the way).",
      False)]))

E.append(question_block(33, "Tone and age rating",
    "Arena combat, but the writing is playful.",
    [("A", "Stylized and bloodless — aim for roughly Everyone 10+ / PEGI 7-12.", True),
     ("B", "A grittier presentation is fine — note any limits below.", False)]))

E.append(question_block(34, "Languages",
    None,
    [("A", "English only for v1 — the Latin card names stay as flavor everywhere.", True),
     ("B", "More languages in v1 — list them below.", False)]))

E.append(question_block(35, "Ownership and upkeep",
    "The unglamorous essentials.",
    [("A", "You own the code, the app listings, and the art; hosting (about 5–20 USD per "
      "month at playtest scale) bills to you; the card data file stays editable by you "
      "without a programmer.", True),
     ("B", "A different split — describe below.", False)]))

E.append(PageBreak())

# ================================================================ ANSWER SHEET
E.append(P("Quick answer sheet", "h1"))
E.append(rule())
E.append(P(
    "If marking pages isn't convenient: fill this grid (choice letter per question), "
    "photograph it, and send it back. “All suggested defaults except...” also works.",
    "lead"))

topics = {
    1: "Starting money", 2: "Beast weapons: one roll?", 3: "Damage math order",
    4: "Attack into dead neighbor", 5: "Fulgur Iovis targets", 6: "Furor's +1 scope",
    7: "Death sequence", 8: "Interceptio details", 9: "Dodge penalty stacking",
    10: "Bestia and dodge gifts", 11: "Ensis Martis bonus", 12: "Dead players' Equip Phase",
    13: "Random redirect", 14: "Debilis intent", 15: "Setup exchange",
    16: "Specials in Market", 17: "Selling locks", 18: "First player",
    19: "Reaction prompts", 20: "Live vs async", 21: "Shared screen",
    22: "Timers and disconnects", 23: "Dice ritual", 24: "Match format",
    25: "House rules", 26: "Strictness", 27: "Accounts",
    28: "App's purpose", 29: "Distribution", 30: "Art", 31: "Name",
    32: "Money model", 33: "Tone / rating", 34: "Languages", 35: "Ownership",
}
sheet = [["Q", "Topic", "Choice", "Q", "Topic", "Choice"]]
for i in range(1, 19):
    j = i + 18
    left = [f"Q{i}", topics[i], ""]
    right = [f"Q{j}", topics[j], ""] if j <= 35 else ["", "", ""]
    sheet.append(left + right)
t = Table([[P(c, "tcell_b") if r == 0 else P(c, "tcell") for c in row] for r, row in enumerate(sheet)],
          colWidths=[34, 136, 48, 34, 136, 48], repeatRows=1)
t.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.6, LINE),
    ("BACKGROUND", (0, 0), (-1, 0), PARCH),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 4.5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
    ("LEFTPADDING", (0, 0), (-1, -1), 5),
]))
E.append(t)
E.append(Spacer(1, 10))
E.append(P("Part 2 path: (  ) approved   (  ) discuss first", "body"))
E.append(Spacer(1, 12))

E.append(KeepTogether([
    P("What happens next", "h2"),
    P("<b>1.</b> Your answers get folded into the specification and the card data file — "
      "they become the single source of truth the software follows.", "bullet"),
    P("<b>2.</b> We build the rules engine and a pass-and-play prototype you can hold in "
      "your hand within weeks — the fastest honest test of how Gladiator feels on a screen.",
      "bullet"),
    P("<b>3.</b> Then online rooms: your playtesters join with a code, each on their own "
      "phone, anywhere.", "bullet"),
    Spacer(1, 6),
    P("Nothing in this document commits you to a technology or a budget — it locks the "
      "rules and the direction so that everything built next is built once.", "body"),
]))

doc.build(E)
print("wrote", os.path.abspath(OUT))
