# Sequences — Hat Ordering per Modality

The order of hats is not fixed; de Bono designed it to flex to the task. Blue
always bookends. White comes early because its facts feed everyone. Beyond that,
the ordering shifts the *character* of the session — leading with Green makes it
divergent, leading with Black makes it a stress test.

Below are the defaults this repo ships. Override any of them via the CLI
(`--sequence blue,white,green,...`) or by editing the modality file.

## Canonical default (de Bono's common sequence)

```
Blue → White → Green → Yellow → Black → Red → Blue
```

Set the agenda, get the facts, generate options, find the upside, then the
downside, gut-check, wrap up. This is the sensible default when in doubt.

## `decisions`

```
Blue → White → Green → Yellow → Black → Red → Blue
```

The canonical order. Options generated before judgment; upside before downside
so Black doesn't smother the option set; Red gut-check right before synthesis
when the tradeoffs are fresh.

## `research`

```
Blue → White → Green → Black → Yellow → Red → Blue
```

White is the centerpiece. Green opens hypotheses and angles, then Black
stress-tests the *evidence* early (weak studies, thin consensus), Yellow
consolidates what's genuinely solid, Red flags what still feels shaky.

## `creative`

```
Blue → Green → Yellow → Red → White → Black → Blue
```

Diverge first: Green leads, Yellow amplifies what's working, Red checks
emotional truth. White then grounds intent vs. execution, and Black does the
editorial pass (holes, clichés, sag) last so critique doesn't choke early
generation.

## `technical`

```
Blue → White → Black → Green → Yellow → Red → Blue
```

Pin down real constraints (White), then run Black early and hard because missed
failure modes are expensive. Green proposes alternatives in response to the
risks, Yellow names real strengths, Red gives the fragility smell-test.

## Notes

- **Blue is implicit at both ends.** In the CLI you list only the middle hats if
  you like; opening/closing Blue are always added.
- **White is force-fed forward.** Wherever White sits, its facts are shared with
  every later hat. Put it early.
- **Red near the end** tends to work best — feelings are most informative once
  the substance is on the table — except in `creative`, where an early Red read
  is part of the material.
- You can repeat a hat (e.g. a second Green pass after Black surfaces
  constraints) — just list it twice in the sequence.
