# Questions for the Game's Creator

Grouped in three sections: **A** — rules edge cases an app must resolve exactly
(a human table can shrug; code can't), **B** — choices about adapting the game to
phones, **C** — product decisions. Every question has a *suggested default* so a
quick "yes/no/correction" per line is enough.

---

## A. Rules clarifications

**Q1. Starting money.** Players seem to start at 0 denarii and collect their first
30 in their first Equip Phase — correct, or is there starting cash?
*Suggested default: start at 0.*

**Q2. Die-multiplier weapons (Leo ×10, Ursus ×8, Canis ×5, Cerberus ×8).** The
rules say "one die roll does it all." Does the *same* d6 that decides the hit also
set the damage (roll 4 vs dodge 2 with Leo = 40 damage; a 6 = auto-hit for 60)? Or
is damage a separate roll? And when paired with a fixed weapon (Ursus + Gladius):
total = 50 + die×8 from that same roll?
*Suggested default: same single roll for everything.*

**Q3. Damage math order.** Confirm: (total attack − total armor) → round **up** to
nearest 5 → minimum 5 on any successful hit. Does the round-up-to-5 also apply to
die-multiplier damage (e.g. Ursus roll 3 = 24 → 25)?
*Suggested default: yes to both.*

**Q4. Attack Left/Right into a dead neighbor.** Does the attack skip to the next
*living* gladiator in that direction, or is it wasted?
*Suggested default: next living gladiator in that direction.*

**Q5. Fulgur Iovis targets.** "Attacks two players simultaneously" — any two of the
attacker's choice, or specifically both neighbors? In a 2-player game does it hit
the lone opponent once or twice?
*Suggested default: any two; in 2-player it hits the opponent once.*

**Q6. Furor (+1 to the roll).** It clearly turns a 5 into an auto-hit 6. Does the +1
also count for beating dodge (a 2 becomes 3 vs dodge 2 = hit)? And with
die-multiplier weapons, does the boosted number also boost damage (5→6 ⇒ Leo 60)?
*Suggested default: yes and yes.*

**Q7. Death sequence details.** Confirm the order: VITA hits 0 → Emperor's Favor
coin (first time per round only) → if eliminated and they hadn't attacked yet this
turn, Furor Mortis coin → Hades. Two sub-questions: (a) does Furor Mortis also
trigger on a *second* death (where no Favor coin is flipped)? (b) At exactly 0
VITA, may the player heal with Aqua Vitae/Medicus *instead of* flipping, or does
the coin flip immediately? ("Cannot use if VITA goes below 0" reads like healing is
only allowed while still above 0.)
*Suggested defaults: (a) yes, Furor Mortis can trigger on any death before acting;
(b) no — at 0 the coin flips immediately.*

**Q8. Interceptio.** (a) Where does the stripped equipment go — discard pile,
removed from the round, or to the thief? (b) Can it strip Retiarius' permanent Rete?
(c) Can it strip a Legendary (e.g. Lorica Hephaesti — it's body *armor*)? (d)
Two-handed weapons are immune since it says "one-handed weapon or armor" —
intentional?
*Suggested defaults: (a) discard pile; (b) no; (c) no — legendaries are god-gifts;
(d) yes, intentional.*

**Q9. Dodge-reduction stacking.** Rete, Harena, and Hades cards each say −1 (min
1). Do multiple sources stack (dodge 3 → 1 with two nets/effects)? Does Galea negate
only the Rete, or also Harena/Hades dodge reductions?
*Suggested default: they stack, floor 1; Galea negates Rete only.*

**Q10. Bestia and dodge buffs.** Bestia "never dodges." If Bestia equips Talaria
Mercurii (+2 dodge), does it get dodge 2, or is "never" absolute?
*Suggested default: never is absolute — Bestia can't gain dodge.*

**Q11. Velox + Ensis Martis.** Ensis grants "draw and immediately play an extra
attack card" on a hit. Does Velox's "draw 2, play 1" apply to that extra draw too?
Can the extra attack chain again if it also hits?
*Suggested default: extra draw is exactly 1 card; no chaining — one bonus attack
per turn.*

**Q12. Eliminated players' Equip Phase.** Dead players draw Hades cards in the
Attack Phase — during the Equip Phase do they simply sit out entirely (no income,
no sell, no draw)?
*Suggested default: yes, they skip the Equip Phase.*

**Q13. Hades "attack hits a RANDOM player."** Random among all *living* gladiators
— can that include the cursed attacker themself? (Rolling randomly among the others,
or truly anyone?)
*Suggested default: any living gladiator except the attacker.*

**Q14. Debilis Gladiator.** 80 VITA, dodge 1, no special, 1 copy — strictly weaker
than Vulgaris. What is it for (a handicap card? unfinished design? a joke card the
unlucky player must live with)? Should the app include it in the random deal?
*Needs the creator's intent — no default.*

**Q15. The gladiator mulligan.** "Once per round, after all players have drawn, you
can send your Gladiator back and draw a new one." In what order do players
mulligan? Is the returned gladiator shuffled back in (could someone else draw it)?
*Suggested default: seating order; returned card shuffled back in.*

**Q16. Market edge cases.** Specials/legendaries flipped into the Market are
discarded and redrawn — (a) does that also apply while dealing the initial 3-card
Market? (b) A legendary discarded this way: is it gone for the whole round (so some
rounds simply won't see, say, Cerberus)?
*Suggested defaults: (a) yes; (b) yes — gone until next round's reshuffle.*

**Q17. Selling restrictions.** "Cannot sell a card you drew this phase" — do
market-*bought* cards also lock for the phase? Sold cards are "removed from the
game" — since everything reshuffles between rounds, removal really means "for the
rest of this round," right?
*Suggested defaults: bought cards also locked; removal is per-round.*

**Q18. First player & turn rotation.** Who goes first in round 1, and does the
starting player rotate each round (e.g. to the loser's left)?
*Suggested default: random first player in round 1, then rotate clockwise each
round.*

---

## B. Digital-adaptation decisions

**Q19. Reaction timers.** Cards like Aqua Vitae ("any time, after taking damage"),
Flagrum (defender chooses a discard), and Lorica Hephaesti (negate a hit) need the
app to pause and prompt another player's phone. Are short reaction windows (e.g.
10–15 s, then auto-continue) acceptable? May players toggle "never ask me" per
card?
*Suggested default: yes — configurable timer per room.*

**Q20. Live-only or also async?** Is the app strictly a live session (everyone
playing at once, 30–90 min), or should turns-over-hours play (with push
notifications) be supported eventually? Async requires auto-resolve rules for every
reaction window, so it meaningfully constrains design.
*Suggested default: live-only first; revisit async later.*

**Q21. Shared arena screen.** Interest in a Jackbox-style mode later — a TV/laptop
shows the public arena (market, VITA, dice) while phones hold private hands?
*Suggested default: yes, but a later phase.*

**Q22. Turn timers & disconnects.** OK to auto-pass a player after N seconds of
inactivity, and hold their seat for reconnection (say 2 minutes) before the group
can vote to drop them? What should happen to a dropped player's gladiator —
eliminated, or piloted by simple auto-play?
*Suggested default: 60 s soft timer, reconnect grace, then eliminated.*

**Q23. Dice & coin ceremony.** The d6 and Sacred Coin are the drama of the game.
Server generates the result, but should the *attacker* tap/shake to "roll" (and the
dying player tap to flip the coin) so the ritual survives digitally?
*Suggested default: yes — tap-to-roll animations, server-decided outcomes.*

**Q24. Match format.** App enforces full first-to-3-laurels matches — should there
also be a quick single-round mode? Should an interrupted match be resumable later
by the same group?
*Suggested default: both modes; resumable for 48 h.*

**Q25. House rules.** Which knobs should hosts get (laurels to win, income amount,
turn timer, include/exclude Debilis or legendaries…)? Or lock everything to the
rulebook?
*Suggested default: a small "house rules" panel, rulebook values preset.*

**Q26. Rules enforcement level.** Full enforcement (the app validates every action
— our strong recommendation, it's the point of an app) vs. a loose "digital table"
where players move cards freely as in Tabletop Simulator?
*Suggested default: full enforcement.*

**Q27. Player identity in a room.** Nickname + avatar picked per game is enough for
v1 (no accounts/passwords)?
*Suggested default: yes.*

---

## C. Product & business decisions

**Q28. Purpose of the app.** Playtesting/companion tool for the physical card game,
a commercial digital product in its own right, or a marketing funnel for a physical
release? (This ordering drives every priority.)

**Q29. Distribution.** Private web link for the playtest circle → public web → app
stores: how far do you want to go, and is web-first acceptable for v1?

**Q30. Art & branding.** Do finished card art / logo / visual identity exist beyond
these text-layout print sheets? Who owns the art? Any style direction for the app
(parchment-and-bronze? comic? minimalist)?

**Q31. Name & IP.** "Gladiator" is a crowded name (films, games). Is there a
distinctive full title (e.g. "Gladiator: The Arena Card Game") and has any
trademark search been done? (Matters most for app-store listing.)

**Q32. Monetization.** Free for playtesting is the obvious start — any longer-term
model (one-time purchase, cosmetics, expansions like the Hades deck as DLC)?

**Q33. Audience & rating.** Stylized arena violence with playful tone — target age
rating (likely ~10+/E10)? Any content lines not to cross in art/animations?

**Q34. Languages.** English only for v1 (keeping the Latin card names as flavor)?

**Q35. Ownership & upkeep.** Who will own the code repository, pay hosting
(~$5–20/month at MVP scale), and maintain the app after v1 — and does the creator
want the rules/balance editable by themselves (the JSON card file makes that
possible without a programmer)?
