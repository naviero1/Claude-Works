"""Teaching text for the PDF guide: one principle intro per program section,
one troubleshooting-oriented note per network."""

SECTION_INTROS = {
    "A": (
        "Principle: <b>the two-timer oscillator</b>. Two on-delay timers reset each other in a loop, "
        "producing a free-running square wave (Blink) with period 2 × cfgBlinkHalfPeriod = 1 s. Building "
        "the flasher once, at the very top of the program, means every 'flashing' indication is one AND "
        "away — and all flashing lamps blink in phase, which operators read as one coherent machine "
        "rather than several random blinkers."),
    "B": (
        "Principle: <b>debounce and signal qualification</b>. Real sensors chatter: a bottle dropped "
        "into the nest bounces, an opto sensor flickers as a syringe slides past. Each raw input feeding "
        "a decision is therefore passed through a TON: the signal must hold TRUE for the debounce time "
        "before the program believes it. Note the deliberate asymmetry — trust is built slowly (100 ms) "
        "but withdrawn instantly, because for a permissive signal the safe direction of doubt is OFF. "
        "The db* variables, not the raw I_* inputs, are what the rest of the program consumes for "
        "presence decisions; the only raw uses are the fill-stop sensors (speed matters more than noise "
        "immunity) and the hard interlocks repeated in the valve rungs."),
    "C": (
        "Principle: <b>a two-hand START gesture modelled on ISO 13851 concepts</b> — not a two-hand "
        "protective function (the fill deliberately continues after release, because during the fill "
        "the LOCKED GUARD protects the operator, not the buttons; the hardware two-hand relay in the "
        "safety layer provides the actual hand protection). Four properties are enforced: "
        "<b>synchronism</b> — both buttons within 0.5 s of each other; <b>anti-tie-down</b> — taping "
        "one button down and pressing the other is caught by the discordance timers and latched as a "
        "lockout that only full release clears; <b>full-release re-initiation</b> — if the two-hand "
        "condition drops with a button still pressed, the same lockout latches, so re-pressing one "
        "button can never re-form the condition; <b>anti-repeat</b> — the start signal is a rising "
        "EDGE. The same station doubles as the fault-reset input via a release-then-hold-3-s gesture, "
        "saving a dedicated reset button."),
    "D": (
        "Principle: <b>trip latching</b>. A safety event must be remembered, not merely mirrored: if a "
        "momentary E-stop tap or one droplet across the spill probe merely paused the machine, it would "
        "resume by itself the moment the signal cleared — the operator would never know, and an "
        "intermittent fault would never be investigated. Both latches use the seal-in idiom, and both "
        "refuse to release until the reset gesture arrives AND their own cause is verifiably gone."),
    "E": (
        "Principle: <b>plausibility checking</b> — the program's answer to 'how do I ensure a presence "
        "sensor isn't giving a false positive?'. One sensor can lie; a physically impossible "
        "COMBINATION of sensors cannot happen on a healthy machine. Glue rises bottom-up, so HIGH "
        "without LOW is impossible; a level reading with no bottle present is impossible; a plunger "
        "cannot be at both ends; a clamp cannot be locked on a syringe that is not there. Any such "
        "combination, held for 0.5 s, raises SensorErr — which blocks new starts, flashes the attention "
        "lamp, and (if it appears mid-cycle) aborts as fault 5. CA-specific tip: cyanoacrylate vapour "
        "fogs optical sensors; when SensorErr appears, clean lenses first."),
    "F": (
        "Principle: <b>the permissive chain</b>. Every condition required for a safe, sensible start is "
        "a contact in series — the rung is a checklist the machine walks every scan. The payoff is "
        "diagnostic: online, the first cold contact in the chain IS the reason the machine refuses to "
        "start; no cross-referencing needed. Requirements are split by package type (ReadyBottle / "
        "ReadySyringe), common safety (SafetyOK), and cycle context (door, pot level, idle) so each "
        "rung stays short enough to read at a glance."),
    "G": (
        "Principle: <b>the state machine</b>. Four mutually exclusive states carry the cycle: "
        "LOCKING → FILLING → COMPLETE, with IDLE derived as 'none of the above and no trip'. Each "
        "transition is one rung that SETs the next state and RESETs the current one, so the machine can "
        "never be in two cycle states at once, and every transition has exactly one place to put a "
        "breakpoint. A second idea rides along: <b>cycle registration</b> — the package type is captured "
        "into CycBottle/CycSyringe at the start edge, so a fixture sensor glitching mid-fill can never "
        "swap which valve is open (it aborts as fault 6 instead)."),
    "H": (
        "Principle: <b>first-out fault capture</b>. When something breaks, several symptoms usually "
        "follow within milliseconds — the door pops, the level drops, the watchdog expires. What the "
        "troubleshooter needs is the FIRST domino. Each fault rung writes its code only if FaultCode is "
        "still 0 (the EQ-then-MOVE chain), so the register preserves the original cause until reset. "
        "Section order inside H is deliberate: E-stop and spill first — if the E-stop caused the door "
        "signal to drop, code 1 wins the race in the same scan. Network 43 sits AFTER every "
        "transition rung of section G so that on any trip, its R coils win the scan and the cycle dies "
        "immediately."),
    "I": (
        "Principle: <b>defence in depth at the outputs</b>. The valve rungs re-check the entire safety "
        "chain (SafetyOK = raw E-stop input AND no latched E-stop/spill/fault trip), door closed, door "
        "locked and the high-level sensor in series with the state machine's own permission. Logically "
        "redundant — the state machine already guarantees them — but if any rung above is ever edited "
        "carelessly, the output rung still cannot energise a valve with the door open, a trip latched, "
        "or the package already full. Cheap insurance at the only place where software touches "
        "something hazardous. The lamp rungs then simply publish internal state, and the filling lamp "
        "deliberately mirrors the actual valve COMMANDS, not the state bit, so lamp and solenoid can "
        "never disagree."),
    "J": (
        "Principle: <b>counting events, not conditions</b> — via a producer/consumer handshake. "
        "Network 32 latches MDoneEvent the instant a fill completes; the counters consume it here and "
        "network 57 clears it, so it lives exactly one scan and each completion counts exactly once — "
        "even if a same-scan trip immediately knocks StComplete back out (the glue is in the package "
        "either way). Aborted cycles never fire the event and are deliberately not counted. PV is set "
        "to 65535 because the CODESYS CTU stops counting when CV reaches PV — a classic surprise."),
}

NET_NOTES = {
    1: "Half of the oscillator: tBlinkA times only while tBlinkB.Q is FALSE. If Blink ever freezes, watch both timers' ET online — one of them is being held in reset.",
    2: "The other half, plus the Blink coil. Period = 2 × cfgBlinkHalfPeriod. All flashing indications derive from this one bit, so they blink in phase.",
    3: "A bottle must sit still for 100 ms before dbBottlePresent is believed; removal is believed instantly. If starts are refused with a bottle loaded, watch this bit — chattering here means nest vibration or a marginal sensor gap.",
    4: "Same pattern for the syringe body sensor.",
    5: "Same pattern for the clamp feedback. A clamp that is 'almost' over-centre gives a flickering I_SyrLocked — the debounce hides the flicker, the plausibility check (network 20) catches the contradiction if it drops mid-fill.",
    6: "Same pattern for the fill-tip sensor.",
    7: "Mode = bottle only after the fixture signal holds for 200 ms.",
    8: "Mode = syringe is a separately debounced NOT of the same input — so during a fixture swap BOTH modes are FALSE and the station simply cannot start. 'Both mode lamps off' therefore means: signal changing, or sensor not seeing its target.",
    9: "PotLow needs the level to read low for a full 2 s — sloshing from a bottle being slammed in cannot flash the refill warning. PotLow blocks NEW starts only (network 25); a fill in progress finishes on the glue in the line.",
    10: "Times how long the LEFT button is held alone. Reaching 0.5 s means the press was discordant.",
    11: "Mirror image for the right button.",
    12: "The lockout latch, with three ways in and one way out: either discordance timer (button held alone &gt; 0.5 s), or the falling edge of TwoHandOK while a button is still pressed (F_TRIG — this is what forces a FULL release before re-initiation; F_TRIG reads last scan's TwoHandOK because network 13 runs after this one). The seal holds while any button is pressed, so ONLY releasing both clears it. Symptom: operator swears the buttons are dead — they are holding one down from the last attempt.",
    13: "The two-hand condition itself: both pressed AND no lockout. Note this is a LEVEL — network 14 turns it into an event.",
    14: "R_TRIG makes the start a one-scan pulse: anti-repeat for free. Combined with network 12's full-release rule, every StartPulse provably comes from both buttons freshly applied within 0.5 s.",
    15: "The reset gesture, in two steps that both matter: ResetArmed latches only when BOTH buttons are seen released while a trip is latched — hands resting on the buttons when a fault occurs can never auto-acknowledge it. Then holding both for 3 s fires the one-scan ResetPulse. Reading FaultLatched here uses last scan's value (it is computed in section H) — irrelevant across a 3 s hold.",
    16: "Seal-in latch, the textbook rung for the idiom: trigger branch (E-stop circuit open), seal branch (EStopTrip itself), and the seal-break term NOT(ResetPulse AND I_EStopOK), drawn by De Morgan as two parallel NC contacts. The latch survives everything except a reset gesture delivered while the circuit is healthy — and it trips even on a momentary tap.",
    17: "50 ms qualification for the spill probe — fast enough for a real leak, deaf to a single splash droplet bouncing past.",
    18: "Same latch idiom as 16, one subtlety different: the seal-break requires the tray to read DRY, so the reset gesture is REFUSED while I_SpillDetect is still TRUE. Clean first, then reset. Note the spill input's own limitation (see GVL): a dead probe reads 'dry' forever — proof-test it at shift start.",
    19: "Three impossible bottle situations: HIGH without LOW (glue rises bottom-up), and either level signal with no bottle in the nest. Held 0.5 s → BottleSensErr. When it fires, the offending branch is highlighted online — it points at the exact lying sensor.",
    20: "Five impossible syringe situations: plunger at both ends; either plunger signal with no syringe in the nest (catches a stuck-ON plunger sensor); clamp locked with no syringe; fill tip seen with no syringe. Same 0.5 s confirmation as network 19.",
    21: "The OR of both checkers, consumed by the ready rungs (22–23), the attention lamp (53) and the mid-cycle fault (40).",
    22: "The bottle checklist: bottle mode, bottle present (debounced), NOT already full, sensors plausible. NOT I_BottleHigh is what refuses an already-full bottle; a partly-filled one (I_BottleLow TRUE) passes — that is a legal top-off, which network 27 records in CycTopOff.",
    23: "The syringe checklist adds the clamp and the fill tip — a syringe that is present but not locked, or missing its tip, never starts.",
    24: "Common safety summary used by network 25: E-stop healthy AND no latched trip of any kind.",
    25: "THE start permissive. Online, walk left to right: the first cold contact is the reason the machine refuses to start. PotLow appears here — and only here — so low glue blocks new fills without aborting a running one.",
    26: "The only rung that starts a cycle: the one-scan StartPulse gated by the full permissive. SET coil — from here the state machine owns the bit.",
    27: "Cycle registration: which package type this cycle fills is CAPTURED now, from the same gated pulse — everything downstream consults CycBottle/CycSyringe, never the live mode sensor. CycTopOff additionally records that the package already held glue at start (bottle low level made / plunger off its empty stop): a top-off legitimately finishes much sooner than a full fill, and this bit says so on the HMI.",
    28: "Watchdog on the locking step: StLocking may last at most 2 s. IN drops when the state advances, so the timer self-cancels on success.",
    29: "The Locking→Filling transition: door still closed AND the lock bolt confirmed. SET the next state, RESET the current — the transition idiom used by every rung in this section.",
    30: "Bottle fill watchdog: 30 s of StFilling without reaching high level is declared stuck (fault 4, network 39).",
    31: "Syringe fill watchdog, 20 s.",
    32: "Fill complete — the one place raw, un-debounced level sensors are used on purpose: the state follows the very scan the sensor trips, and the valve rungs (45/46) cut off on the same raw signal. The debounced PRESENCE contact in each branch stops a sensor glint during a mid-fill removal from masquerading as success (presence drops instantly; fault 7 wins instead). MDoneEvent hands the completion to the counters even if a trip clears StComplete this same scan.",
    33: "Cycle closure: buttons released (anti-repeat across cycles) AND the filled package actually removed; the cycle registration bits clear with it. If the done lamp never clears, one of these contacts is the reason — usually a presence sensor still seeing residue.",
    34: "IDLE is derived, not stored: 'no cycle state and no trip'. It cannot get out of sync, because it is recomputed from the truth every scan.",
    35: "First-out capture, E-stop: if FaultCode is still 0, write 1. E-stop is checked FIRST in section H so that when one root cause knocks over several signals in the same scan, code 1 wins the race.",
    36: "Spill is second in the pecking order.",
    37: "Door integrity during a cycle: open at any cycle stage, or unlocked while actually filling. The three branches distinguish which combination occurred — online you can see which one carried power.",
    38: "Lock watchdog expiry → code 8. Distinct from code 2 (door opened) because the remedy is different: 8 is 'lock never engaged' (solenoid/bolt/feedback), 2 is 'door integrity lost afterwards'.",
    39: "Either fill watchdog → code 4. See the fault table in chapter 6 for the cause list — supply, clog, valve, or a blind level sensor.",
    40: "A plausibility error DURING a cycle is promoted from warning to fault: mid-fill the sensors are load-bearing; the machine must not keep pouring on data it cannot trust.",
    41: "The registered cycle type disagrees with the live mode sensor → the fixture signal was lost mid-cycle. Because the valves follow Cyc* (registration), the wrong valve can never open — the cycle just aborts cleanly.",
    42: "Package integrity during the cycle: bottle gone, or syringe gone/unclamped/tip lost. Debounced bits drop instantly on removal (network 03 note), so the abort is immediate.",
    43: "The abort rung — placed AFTER every set/transition rung of section G, so when an S and an R coil fire in the same scan, this R executes last and wins. One rung guarantees: any trip, cycle dead, this very scan.",
    44: "The common reset: the release-then-hold gesture (network 15) plus proof the E-stop is healthy and the tray is dry. Clears the flag, the cycle registration and the stored code. The E-stop/spill latches ALSO check their own cause (16/18) — belt and braces. Other causes (door, timeout…) may be acknowledged before the cause is fixed; PermStart blocks any restart until it actually is.",
    45: "The bottle valve: state machine permission AND the full safety chain (SafetyOK re-checks the raw E-stop input and every latched trip) AND the door/level interlocks re-read raw. Even a corrupted state bit cannot open this valve with the door unlocked or a trip latched.",
    46: "Syringe valve, same construction.",
    47: "Door locked exactly while a cycle needs it (LOCKING + FILLING). Idle, Complete and Fault states leave the door free — an operator is never locked out of a faulted machine. Energise-to-lock: power loss unlocks the guard, acceptable only because the valves are spring-return closed (see GVL note).",
    48: "Mode lamp, bottle. Both mode lamps off = mode signal absent/settling (see network 08 note).",
    49: "Mode lamp, syringe.",
    50: "The filling lamp mirrors the valve COMMANDS, not StFilling — so during the brief LOCKING step the lamp is off, and lamp/solenoid can never contradict each other. Lamp off + glue flowing = valve mechanically stuck: hardware.",
    51: "Done lamp = StComplete, held until the package is removed (network 33).",
    52: "E-stop lamp is STEADY (distinct from the flashing attention lamp): on while pressed OR while the trip awaits reset. Lamp on with the button released = reset gesture still owed.",
    53: "Everything that needs a human collects here: latched faults, spill, low pot, sensor errors, two-hand lockout, and 'E-stop released but not reset'. One variable to test when asking 'why is the attention lamp flashing?' — check its six branches online.",
    54: "AND with Blink turns the steady condition into the specified flashing lamp. If it is ON steady, Blink froze — see network 01.",
    55: "Counts bottle cycles from the one-scan MDoneEvent (latched by network 32, consumed by network 57). PV=65535 because the CODESYS CTU stops counting at PV — with the default 0 it would never count at all. CV is copied (WORD-&gt;UINT) to the HMI-visible counter.",
    56: "Syringe twin of 55.",
    57: "Consumes the completion event: MDoneEvent lives exactly one scan — set by 32, read by 55/56, cleared here. The same handshake pattern as network 58.",
    58: "Handshake: the HMI sets cmdCounterReset; the program consumes it (both counters saw it this scan in 55–56) and clears it, so the command acts exactly once.",
}
