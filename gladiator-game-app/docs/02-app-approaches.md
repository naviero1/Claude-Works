# Ways to Build the Gladiator App

Goal: 2–6 people, each on their own phone, connect to one shared game of Gladiator.

The decision isn't one choice — it's four layers. Options in each layer combine
almost freely, so this doc walks the layers, then gives one recommended stack.

```
Layer 0  Rules engine        — the game logic itself (build this regardless)
Layer 1  Client platform     — what runs on each phone
Layer 2  Multiplayer backend — where the shared game state lives
Layer 3  Play modes          — how people sit around the "table"
```

---

## Layer 0 — The rules engine (not optional, and the first thing to build)

Whatever else is chosen, the game's rules should be one isolated, UI-free module:

- **Pure functions:** `(gameState, playerAction) → newState + events`. No network,
  no rendering, no timers inside it.
- **Card data as JSON** (`data/cards.draft.json` is the seed) so balance changes are
  data edits, not code edits — the creator can tune numbers without a programmer.
- **Seeded, server-side randomness** for shuffles, the d6, and the Sacred Coin —
  fair, auditable, and replayable (a full game is just `initial seed + action list`,
  which makes bug reports and disputes trivially reproducible).
- **Unit tests derived from the rulebook** — every example in the rules doc (the
  Gladius-vs-Subarmalis example, the Talaria dodge-cap example) becomes a test.

Recommended language: **TypeScript** — it runs on both server and phone browser, so
the same engine drives online play, offline hot-seat, and instant UI validation.

This module is also the cheapest way to answer "does the game even feel right on a
screen?" before spending on multiplayer infrastructure.

---

## Layer 1 — Client platform (what's on the phone)

| Option | What it is | Pros | Cons | Fits when |
|---|---|---|---|---|
| **A. Web app / PWA** ⭐ | Website; players join via link or room code in the browser; installable to home screen | Zero install friction (huge for "everyone pull out your phone"); one codebase; instant updates; cheapest; CSS handles card UI well | No app-store listing; iOS PWA limits (push notifications work since iOS 16.4 but are fiddlier) | MVP, playtesting, casual groups |
| **B. React Native (Expo) or Flutter** | Installable iOS/Android app from one codebase | Store presence & discoverability; reliable push notifications; native feel | Store fees ($99/yr Apple, $25 Google) and review cycles; players must install before playing; slower iteration | Commercial launch, async play with notifications |
| **C. Game engine (Unity / Godot)** | Full game-engine build | Best animation "juice" (3D dice, arena scenes, particles); Unity has mature netcode options | Heaviest skillset and cost; large binaries; overkill for card logic; web export is clunky | Only if the vision is a rich videogame rather than a digital board game |
| **D. Web-first, wrap later** ⭐ | Build A, then wrap the same code with **Capacitor** into store apps | A's speed now, B's distribution later; one codebase throughout | PWA constraints until wrapped | The pragmatic path when store presence is *eventually* wanted |

⭐ = recommended: **A now, D when distribution demands it.**

## Layer 2 — Multiplayer backend (where the truth lives)

The game has hidden hands, dice, and mid-attack reactions on *other* players'
phones (Aqua Vitae after damage, Flagrum's forced discard, Lorica Hephaesti's
negate). That pushes hard toward a **server-authoritative, push-based (WebSocket)**
design: the server owns state and rolls, clients only render and submit intents.

| Option | What it is | Pros | Cons |
|---|---|---|---|
| **1. Custom authoritative server — Node/TS + Colyseus (or plain Socket.IO)** ⭐ | Small server hosting "rooms"; runs the Layer-0 engine; clients connect by room code | Full control; engine shared with client; Colyseus gives rooms/state-sync/reconnect out of the box; cheap ($5–20/mo covers many concurrent games); no cheating possible by design | You run a server (deploys, monitoring) |
| **2. boardgame.io** | Open-source turn-based-game framework (turn order, phases, secret info, lobby built in) | Purpose-built for exactly this genre; least code to first game | Project maintenance has slowed; framework lock-in; customizing its turn model for reaction windows takes care |
| **3. BaaS realtime (Firebase / Supabase)** | Clients sync through a realtime database; rules run in cloud functions | No server to operate; generous free tiers; easy auth | Authoritative turn logic in functions is awkward (latency per action, cold starts); easy to accidentally trust clients; reaction timers are clunky |
| **4. Managed game backend (Nakama, Photon, Playroom) | Hosted game-server platforms with rooms/matchmaking | Scales without ops; matchmaking included | Cost and lock-in; their models target real-time action games; still must embed your rules engine |
| **5. P2P / one phone hosts (WebRTC)** | No server; a host phone owns state | No hosting cost; works on a LAN | NAT/connection pain in browsers; host-quits kills the game; cheating possible; reconnects hard. Not recommended |

⭐ = recommended: **Option 1** (Colyseus), with Option 2 worth a spike if we want to
move even faster and accept the framework.

## Layer 3 — Play modes (how people gather)

| Mode | Description | Cost to add | Verdict |
|---|---|---|---|
| **Remote rooms** ⭐ | Host creates room → shares 4–6 letter code → everyone joins from anywhere | Core build | The baseline; also works when everyone's in the same room |
| **Same room, phones only** ⭐ | Same as above, sitting together — app replaces cards/dice/coins/trackers; table talk stays human | Free (same build) | The primary intended experience per the creator's brief |
| **Shared arena screen** | A TV/laptop shows the public arena (market, VITA bars, dice animations); phones show only private hands — Jackbox style | Moderate (a spectator "board" client) | Strong later addition; great for demos and parties |
| **Pass-and-play** | One phone passed around; hands hidden between turns | Small (engine + local UI, no server) | Cheap byproduct of Layer 0 — useful as the first playable prototype |
| **Async / correspondence** | Turns over hours with push notifications | Significant (reaction windows need auto-resolve rules; needs Option B/D clients for reliable push) | Defer; see creator question Q20 |
| **Solo vs bots** | AI opponents | Moderate (simple bot policies are easy; fun bots are not) | Defer unless the creator wants a practice mode |

---

## Recommended stack and phased path

**Stack:** TypeScript everywhere. Rules engine as a pure TS package · React (or
Svelte) PWA client · Node + Colyseus authoritative server · Postgres only when
persistence is needed (accounts/stats) · deploy on Fly.io/Railway/Render.

| Phase | Deliverable | Proves |
|---|---|---|
| **0. Lock the spec** | Creator answers doc 03; `cards.draft.json` → confirmed | The rules are unambiguous enough to code |
| **1. Engine + hot-seat prototype** | Rules engine w/ tests + pass-and-play web UI (no server, no accounts) | The game is fun on a screen; adaptation choices (reaction prompts, dice moments) feel right |
| **2. Online rooms (the real MVP)** | Colyseus server + PWA: create/join by code, server dice & shuffles, reaction windows w/ timers, reconnect handling, full first-to-3-laurels sessions | 2–6 phones anywhere can play a whole game |
| **3. Polish & reach** | Animations/sound (the d6 and Sacred Coin deserve drama), shared-screen mode, Capacitor wrap → app stores, optional accounts/stats/rankings | It's a product, not a prototype |

Rough scale for one experienced full-stack TS developer: Phase 1 ≈ 2–4 weeks,
Phase 2 ≈ 4–8 weeks, Phase 3 open-ended. Running costs until stores/accounts:
domain + ~$5–20/month hosting.

### Why not start with Unity, native apps, or Firebase?

- **Unity/native first** front-loads cost and slows the loop that matters most
  right now: playtesting the *digital adaptation* of the rules.
- **Firebase-style client-sync** fights this game's needs (authoritative dice,
  hidden hands, interrupt windows) — you end up rebuilding a server in functions.
- A web MVP is discardable-cheap, and nothing is wasted: the Layer-0 engine — most
  of the real work — carries unchanged into any later client or backend.
