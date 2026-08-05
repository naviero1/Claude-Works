# CA Glue Filling Station — PLC Program & Learning Guide

Ladder logic for a benchtop cyanoacrylate (CA) glue filling station that fills
**squeeze bottles** or **syringes** from a pressure pot, plus a PDF guide that
explains every principle and algorithm used, written for learning and
troubleshooting.

**Target platform:** CODESYS 3.5 (IEC 61131-3), program language LD.

## Contents

| Path | What it is |
|---|---|
| `docs/CA_Filling_Station_Ladder_Guide.pdf` | **The guide** — system overview, safety architecture, I/O reference, ladder fundamentals, all 58 networks drawn and explained, fault-code troubleshooting tables, commissioning checklist, variable cross-reference |
| `plc/GVL_IO.txt` | Global variable list (paste into a CODESYS GVL named `GVL_IO`) — all I/O with wiring conventions, tunable timing parameters, diagnostics |
| `plc/PLC_PRG_Ladder.txt` | The canonical rung-by-rung ladder listing (58 networks, sections A–J) with the `VAR` block for `PLC_PRG` |
| `plc/PLC_PRG.st` | Structured Text 1:1 mirror of the ladder — paste into an ST POU to simulate/commission before transcribing to LD |
| `tools/` | Python scripts that generate the PDF (`build_pdf.py`, ladder renderer, network data, teaching notes) |
| `tools/sim_test.py` | Scan-accurate Python simulation of the program — 14 scenarios (normal fills, E-stop, tie-down, watchdogs, spill, plausibility…), 58 assertions. Run with `python3 tools/sim_test.py` |

## Design at a glance

- **Two-hand start** (0.5 s synchronism, anti-tie-down, anti-repeat) → door
  locks → fill valve opens → **auto-stop on the high-level / plunger-high
  sensor** → done lamp → remove package.
- **State machine:** IDLE → LOCKING → FILLING → COMPLETE, with a FAULT overlay
  reachable from anywhere; first-out fault code (1–8) preserved for
  troubleshooting.
- **False-positive defence:** debounced presence sensors plus plausibility
  cross-checks (physically impossible sensor combinations raise an error).
- **Pressure-pot low level** blocks new fills only; **spill detector** latches
  a fault whose reset is refused while the tray reads wet.
- **Fault reset:** hold both opto buttons 3 s (no dedicated reset button in the
  I/O list).
- Added output `Q_DoorLock` (the input list names a door lock; a lock needs a
  command signal) — see the design note in chapter 3 of the guide.

## Safety boundary (important)

The E-stop, two-hand control and guard-lock logic in this program are
**sequence control and indication only**. The protective functions must be
implemented in safety-rated hardware (safety relay / safety PLC per an
ISO 13849-1 risk assessment) that removes valve power independently of this
program. Chapter 2 of the guide explains the boundary in detail.

## Regenerating the PDF

```bash
pip install reportlab
python3 tools/build_pdf.py            # writes docs/CA_Filling_Station_Ladder_Guide.pdf
```
