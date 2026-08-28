# Design plan — The Inventory Doctrine

## Read of the request
Editorial-analytical. The deliverable is a report with an audience (ops / supply
chain / finance leadership), whose single job is to make the **causal link**
legible: *this* pre-2019 doctrine created *that* vulnerability, COVID exposed it
*here*, so the measurement system changed *this way*. Craft goes into the
structural language, not decoration — the subject is serious and the reader is
technical.

## Visual world
**The freight document.** Bill of lading, dispatch manifest, engineering drawing.
Hairline rules, stencilled mono registers, a strict grid, a hazard-tape accent.
Every structural device encodes something true: the section numbers are a real
sequence (doctrine → shock → response → measurement), the two-column ledger is
literally a before/after register, and the hazard stripe is the subject's own
signage rather than ornament.

Deliberately *not*: warm cream + serif display + terracotta; near-black with one
acid pop; purple-blue gradient hero; Inter/Space Grotesk; emoji section markers.

## Color
Cool paper ground with a green-blue bias (chosen, not inherited grey).

| Role | Light | Dark |
|---|---|---|
| page | `#e9edec` | `#0b1214` |
| panel | `#f7f9f9` | `#111a1d` |
| ink | `#0f1719` | `#e9efee` |
| rule | `#cbd5d3` | `#233034` |
| **accent — hazard amber** | `#c07d00` | `#d9a01f` |
| act 1 — the efficiency era | `#1c6ea4` marine | `#3e8fc4` |
| act 2 — the shock | `#c0492c` oxide | `#d8623f` |
| act 3 — the resilience era | `#00918a` teal | `#12a99f` |

The three acts double as the chart categorical slots 1–3, so a colour means the
same thing in prose and in every figure.

## Type
Three roles, each with a job:
- **Archivo** — display and UI. A grotesque with ANSI/industrial-signage bones.
- **Source Serif 4** — running text. Report gravity, comfortable at length.
- **IBM Plex Mono** — the data register: ledger columns, formulas, labels,
  eyebrows, axis ticks. Genuine technical provenance, and it is the face that
  makes the page read as a document rather than a deck.

## Layout
One 1140px frame, running text held to ~66ch, data artefacts breaking out wider.
Sections open with a manifest register line (number · title · rule). The
recurring artefact is a **two-column ledger** — old metric on the left in marine,
new metric on the right in teal, with the failure mode COVID exposed spanning the
full width underneath in oxide. That row *is* the argument, repeated 15 times.

## Chart palette validation
Run against the dataviz skill's `validate_palette.js`, adjacent pairlist,
both modes:

```
light  #1c6ea4,#c0492c,#00918a,#c07d00,#6a5ab8,#4f7a1f   surface #f5f7f6
       lightness band PASS · chroma floor PASS · CVD adjacent worst ΔE 12.6 PASS
       normal-vision worst ΔE 21.2 PASS · contrast all ≥3:1 PASS   → ALL PASS

dark   #3e8fc4,#d8623f,#12a99f,#b98209,#8a7ce0,#6e9c37   surface #111a1d
       lightness band PASS · chroma floor PASS · CVD adjacent worst ΔE 12.8 PASS
       normal-vision worst ΔE 20.1 PASS · contrast all ≥3:1 PASS   → ALL PASS
```

Constraint carried forward: under `--pairs all` (scatter, bubble, choropleth)
marine↔teal falls to normal-vision ΔE 12.4, below the 15 floor. No all-pairs
chart form is used in this report; if one is added later it caps at two slots.

Every figure is single-series or two-series with a legend and direct endpoint
labels, so identity is never carried by colour alone, and each carries a
`Show data` table view.
