# Game Review — Gladiator as a Digital Specification

This restates rules v5.0 in the shape an app needs: entities, state, phases, and
formulas. Anything uncertain is **not** decided here — it's listed in
[03-questions-for-creator.md](03-questions-for-creator.md).

## 1. The game in one paragraph

2–6 players each control one Gladiator. Play alternates between an **Equip Phase**
(earn 30 denarii, buy/draw/sell equipment from a 3-card Market, arrange weapons and
armor) and an **Attack Phase** (draw an Attack card that picks your target, roll 1d6
against their dodge, deal attack-minus-armor damage). At 0 VITA a coin flip decides
revival or elimination; eliminated players keep playing by drawing Hades cards that
meddle with the living. Last gladiator standing wins the round and a laurel; first to
3 laurels wins the game.

## 2. Components (all verified against print sheets)

| Deck | Cards | Breakdown |
|---|---|---|
| Gladiators | 33 | Vulgaris ×11, Velox ×9, Bestia ×8, Retiarius ×3, Invictus ×1, Debilis ×1 |
| Equipment | 117 | 50 weapons, 37 armor, 24 specials, 6 legendaries |
| Attack | 30 | Left ×9, Right ×9, Your Choice ×6, Pass ×6 |
| Hades | 30 | Watch ×15, Wrath of the Dead ×8, Whisper from Below ×7 |

Physical accessories the app must simulate: denarii (bank), health/win trackers,
six-sided die, Sacred Coin.

## 3. Game state model

```
Game
├─ laurelsToWin: 3
├─ players[2..6] (fixed seating order → "left"/"right" targeting)
│   ├─ laurels
│   └─ per-round state:
│       ├─ gladiator (type, VITA current/max, base dodge, special)
│       ├─ denarii
│       ├─ hand (max 6 at end of Equip Phase; equipment + special cards only)
│       ├─ equipped: mainHand, offHand, body, head, arm, legs, noSlot(Talaria)
│       ├─ usedEmperorsFavor: bool   (one coin flip per gladiator per round)
│       ├─ alive | eliminated (eliminated → draws Hades cards)
│       └─ hasAttackedThisTurn: bool (drives Furor Mortis)
├─ decks: equipment(+discard), attack(+discard), hades(+discard), gladiators
├─ market: 3 face-up equipment cards (specials/legendaries never sit in market —
│          discard & redraw)
└─ round/turn/phase pointers + active reaction windows
```

Per-round reset: everything except laurels (and seating). New gladiators are drawn
each round; denarii return to the bank; all decks reshuffle.

## 4. Turn structure

A **round** = repeat **turns** until one gladiator lives. A **turn** = every player
takes an Equip Phase, then every player takes an Attack Phase action, in seating
order.

### Equip Phase (per player)

1. **Income** — collect 30 denarii.
2. **Sell** (optional, any time this phase) — any hand or equipped card for its sell
   value (50% of cost, rounded up to nearest 5). Cannot sell a card drawn this phase.
   Sold cards leave the game (for the round).
3. **Market refresh** (optional, once per phase, before draw/buy) — pay 20 denarii,
   replace all 3 Market cards.
4. **Draw 1** from equipment deck **OR buy up to 2** from the Market (not both).
   Market refills immediately after purchases.
5. **Equip freely** — unlimited rearranging between hand and gladiator; locks when
   the phase ends. Hand limit 6 (equipped cards don't count) — discard down at end.

### Attack Phase (per player, seating order)

- **Living player:** draw 1 Attack card → target = card's direction (Left / Right /
  Your Choice / Pass). 2-player games skip attack cards; you always attack the
  opponent. Then resolve the attack (below). Velox instead draws 2 and plays 1.
- **Eliminated player:** draw 1 Hades card and resolve it (see §7).

### Attack resolution (one d6 roll)

| Roll | Result |
|---|---|
| ≤ target's dodge | **Miss.** No damage |
| 6 | **Auto-hit.** Damage = full attack total, armor ignored |
| otherwise | **Hit.** Damage = attack total − target's armor total |

- Attack total = sum of all equipped weapon ATK (+ gladiator modifiers, e.g. Bestia
  +10). Unarmed = 10 (fists).
- Damage rounds **up** to the nearest 5; every successful hit deals **at least 5**.
- **Dodge is capped at 4** no matter the modifiers (a 5 or 6 always has a chance to
  hit). Dodge modifiers: Rete −1, Harena −1, Hades cards −1, Talaria +2 — floor 1
  when reduced (Bestia is "never dodges").
- Die-multiplier weapons (Leo ×10, Ursus ×8, Canis ×5, Cerberus ×8) deal
  die-roll × multiplier damage — whether that uses the same to-hit die or a second
  roll is question Q2.

### Reaction cards (why the app needs interrupt windows)

- **Aqua Vitae / Medicus Scroll** — heal "at any time, including during the Attack
  Phase after taking damage."
- **Harena / Furor** — must be declared *after* an attack card is drawn, *before*
  the roll.
- **Flagrum** — on hit, the *defender* chooses a card to discard (mid-attack input
  from the non-active player).
- **Lorica Hephaesti** — once per game, negate a hit entirely (a decision made when
  hit).

These make the game more than strictly-sequential input: several moments need a
prompt on *another* player's phone before resolution can continue.

## 5. Death pipeline (per gladiator, per round)

```
VITA reaches 0
└─ first time this round? → Sacred Coin (Emperor's Favor)
     ├─ Heads → revive at 30 VITA, still in the round
     └─ Tails → eliminated ↓
        (second 0 VITA this round → eliminated directly, no coin)
└─ eliminated before they attacked this turn? → Sacred Coin (Furor Mortis)
     ├─ Heads → one final attack vs their killer (normal attack rules)
     └─ Tails → nothing
└─ eliminated → for the rest of the round, their Attack Phase turn = draw a
   Hades card and resolve it
```

## 6. Win conditions

- Round: last living gladiator → +1 laurel.
- Game: first player to 3 laurels is Champion of the Arena.

## 7. Card catalog (full data in `data/cards.draft.json`)

**Gladiators** — Vulgaris 100 VITA/dodge 1; Velox 80/2 (draw 2 attack cards, play
1); Bestia 130/never dodges (+10 all attacks); Retiarius 90/2 (permanent Rete in one
weapon slot); Invictus 120/3 (body armor only); Debilis 80/1 (no special — see Q14).

**Weapons** (main hand + off-hand slots; two-handed fills both) — Pugio 15 (doubles
vs <30 VITA), Gladius 50 (not with Tridens), Pilum 50 (ignores 5 armor), Sica 35
(ignores 20 armor), Tridens 60 (main hand only, not with Gladius), Spatha 80
(two-handed), Flagrum 25 (forces a discard on hit), Rete 0 (target dodge −1, max 1),
Leo d6×10 (two-handed, ignores armor, dodge −1), Ursus d6×8 (auto-hit damage taken
−10), Canis d6×5 (ignores armor).

**Armor** (slots: body ×1 max, head, arm, legs, off-hand for shields) — Subarmalis
20, Parma 25, Manica 25, Ocreae 25, Cassis 20, Galea 25 (negates Rete), Scutum 35,
Lorica Squamata 35 (auto-hit −10), Lorica Segmentata 45 (auto-hit −20).

**Specials** (draw-only, one use, announce & discard) — Aqua Vitae (+30 VITA),
Medicus (+20), Harena (dodge −1), Furor (+1 to roll, 5→6 auto-hits), Interceptio
(strip an opponent's one-handed weapon/armor, they get half sell value), Fortuna
(draw 2 keep 1).

**Legendaries** (draw-only, unique, max 1 per gladiator, sell 50) — Fulgur Iovis 60
(hits two players with one roll), Lorica Hephaesti 45 def (once per game negate a
hit), Ensis Martis 70 (on hit, extra attack card), Talaria Mercurii (+2 dodge, cap
4), Hasta Achillis 60 (auto-hit on 5 or 6), Cerberus d6×8 (ignores armor, dodge −1).

**Hades deck** — Watch ×15 (flavor, do nothing), Wrath ×8 (hits all living: dodge
−1, 5 damage, everyone discards, attack rolls −1, armor −10 variants), Whisper ×7
(one chosen target: dodge −1, weapon inactive, armor −10, roll −1, attack
redirected to random player, specials locked).

## 8. Consistency notes from the review

- Print sheets and rulebook agree on every count and every stat we cross-checked.
- The printed player-aid card omits the Market-refresh step that rules v5.0 added —
  the docx is the newer authority.
- The rulebook's own example ("dodge 2, roll 2 or less = dodged") confirms
  *miss on roll ≤ dodge*, i.e. dodge N = misses on N faces of the die.
- Ambiguous edge cases are collected as Q1–Q18 in doc 03 rather than guessed at here.
