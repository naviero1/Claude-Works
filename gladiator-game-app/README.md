# Gladiator — Companion App Project

Foundation for turning **GLADIATOR — A Card Game** (2–6 players, rules v5.0) into a
multiplayer app where each player joins and plays from their own phone.

## Source material reviewed

| File | Contents |
|---|---|
| `gladiatorrules_v50.docx` | Full rulebook v5.0 (turn structure, combat, economy, death rules) |
| `gladiatorcards.pdf` | Print sheets for all 216 cards + player aids |
| `gladiatorhadesdeck.pdf` | The 30-card Hades (Underworld) deck |

Card counts in the print sheets were verified against the rulebook's component list —
they match exactly (33 gladiators, 117 equipment, 30 attack, 30 Hades).

## What's in this folder

| File | Purpose |
|---|---|
| [`docs/01-game-review.md`](docs/01-game-review.md) | The game restated as a digital specification: state, phases, combat formula, death flow — the seed for a rules engine |
| [`docs/02-app-approaches.md`](docs/02-app-approaches.md) | The ways the app can be built: client platform, multiplayer architecture, play modes — with trade-offs and a recommended phased path |
| [`docs/03-questions-for-creator.md`](docs/03-questions-for-creator.md) | Numbered questions for the game's creator: rules edge cases, digital-adaptation decisions, product decisions. Each has a suggested default so answering can be quick |
| [`data/cards.draft.json`](data/cards.draft.json) | **Draft** machine-readable database of all 216 cards (stats, costs, copy counts, rules text). Becomes the app's card data once the creator confirms it |

## Status

- [x] Game materials reviewed, card inventory verified
- [x] App approach options documented
- [x] Open questions compiled for the creator
- [ ] Creator answers questions → lock rules spec v1
- [ ] Choose approach (recommendation: web-first PWA + authoritative server, see doc 02)
- [ ] Build rules engine + hot-seat prototype
- [ ] Online rooms (join by code from any phone)
