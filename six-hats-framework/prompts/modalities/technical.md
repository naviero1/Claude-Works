# Modality: Technical / Code

This is a **technical** task: architecture, debugging, code review, or a
technical design tradeoff. Apply your hat with this focus:

- **White:** what the system actually does; the real constraints (scale,
  latency, dependencies, team, deadlines); what is *measured* vs. merely
  assumed.
- **Black:** bugs, security holes, race conditions, failure modes, edge cases,
  operational burden, and tech debt. Runs early and thorough here — missed
  failure modes are expensive.
- **Green:** alternative designs, simpler approaches, different tools or
  libraries, and ways to sidestep the hard part entirely.
- **Yellow:** where the approach is genuinely strong — maintainability,
  performance, testability, and fit to the existing team and stack.
- **Red:** the smell test — what feels fragile, over-engineered, or "you'll
  regret this in six months," even before you can prove it.

Cross-cutting emphasis for this modality: pin down the **real constraints**
(White) before anyone judges, and don't let Yellow excuse a design that Black
has shown to be unsafe — correctness and failure modes dominate.
