#!/usr/bin/env python3
"""
six_hats.py — run any topic through Edward de Bono's Six Thinking Hats.

This is the reference runner for the framework in this repo. It implements the
orchestration contract described in ../spec/framework.md:

  * Blue always opens and closes the session.
  * White produces shared facts; those facts (and only those) are fed forward to
    every hat that runs after it.
  * Every other hat runs BLIND to its siblings — it sees the topic, its own hat
    prompt, the modality focus, and White's facts. Nothing else. Isolation is
    the feature: it stops optimism from taxing criticism and criticism from
    taxing creativity.
  * The closing Blue pass is the only one that reads every other pass, and it
    synthesizes them.

Each hat is a separate model call, which is exactly why this maps cleanly onto a
multi-agent setup: one hat == one single-purpose agent.

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    python six_hats.py "Should we migrate our monolith to microservices?" \
        --modality technical

    # classify the task automatically:
    python six_hats.py "Is now a good time to switch careers?" --modality auto

    # read the topic from a file or stdin:
    python six_hats.py --topic-file design_doc.md --modality technical
    echo "my topic" | python six_hats.py --modality decisions

    # see exactly what would be sent, without an API key or any network call:
    python six_hats.py "test topic" --modality research --dry-run

    # cheaper single-prompt version (one call, isolation left to the model):
    python six_hats.py "..." --single-pass

Run `python six_hats.py --help` for all options.
"""

import argparse
import os
import sys
import textwrap
from pathlib import Path

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

# Directory layout is resolved relative to this file so the CLI works no matter
# where it's invoked from.
ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts"
HATS_DIR = PROMPTS / "hats"
MODALITIES_DIR = PROMPTS / "modalities"

MODALITIES = ["decisions", "research", "creative", "technical"]

# Default hat order per modality (the MIDDLE hats — Blue open/close are always
# added automatically). Mirrors spec/sequences.md. White is force-fed forward:
# any hat listed after White receives White's facts; hats before White work
# from the topic directly (used deliberately in `creative` to diverge first).
DEFAULT_SEQUENCES = {
    "decisions": ["white", "green", "yellow", "black", "red"],
    "research":  ["white", "green", "black", "yellow", "red"],
    "creative":  ["green", "yellow", "red", "white", "black"],
    "technical": ["white", "black", "green", "yellow", "red"],
}

HAT_LABELS = {
    "blue-open":  "🔵 Blue — Framing",
    "white":      "⚪ White — Facts & Information",
    "red":        "🔴 Red — Emotion & Intuition",
    "black":      "⚫ Black — Caution & Critique",
    "yellow":     "🟡 Yellow — Optimism & Value",
    "green":      "🟢 Green — Creativity",
    "blue-close": "🔵 Blue — Synthesis",
}

DEFAULT_MODEL = os.environ.get("SIX_HATS_MODEL", "claude-sonnet-4-5")
DEFAULT_MAX_TOKENS = int(os.environ.get("SIX_HATS_MAX_TOKENS", "2000"))

NO_FACTS_YET = (
    "(The White hat has not run yet in this sequence — work directly from the "
    "topic. This is intentional for a diverge-first sequence.)"
)


# --------------------------------------------------------------------------- #
# Prompt loading & assembly
# --------------------------------------------------------------------------- #

def read_prompt(path: Path) -> str:
    if not path.exists():
        sys.exit(f"error: expected prompt file not found: {path}")
    return path.read_text(encoding="utf-8")


def fill(template: str, **kw) -> str:
    """Replace {{KEY}} placeholders. Leaves unknown placeholders untouched."""
    out = template
    for key, val in kw.items():
        out = out.replace("{{" + key + "}}", val)
    return out


def load_modality_focus(modality: str) -> str:
    return read_prompt(MODALITIES_DIR / f"{modality}.md")


def hat_prompt_file(hat: str) -> Path:
    return HATS_DIR / f"{hat}.md"


def resolve_sequence(modality: str, override: str | None) -> list[str]:
    """Return the full ordered list of hats including Blue open/close."""
    if override:
        middle = [h.strip() for h in override.split(",") if h.strip()]
        # allow the user to include or omit the blue bookends
        middle = [h for h in middle if h not in ("blue", "blue-open", "blue-close")]
    else:
        middle = list(DEFAULT_SEQUENCES[modality])
    return ["blue-open"] + middle + ["blue-close"]


# --------------------------------------------------------------------------- #
# Model client
# --------------------------------------------------------------------------- #

class Runner:
    def __init__(self, model: str, max_tokens: int, dry_run: bool):
        self.model = model
        self.max_tokens = max_tokens
        self.dry_run = dry_run
        self.system = read_prompt(PROMPTS / "system.md")
        self._client = None
        if not dry_run:
            try:
                import anthropic  # noqa: F401
            except ImportError:
                sys.exit(
                    "error: the 'anthropic' package is required for live runs.\n"
                    "       pip install -r requirements.txt   (or add --dry-run)"
                )
            import anthropic
            if not os.environ.get("ANTHROPIC_API_KEY"):
                sys.exit(
                    "error: ANTHROPIC_API_KEY is not set.\n"
                    "       export ANTHROPIC_API_KEY=sk-ant-...   (or add --dry-run)"
                )
            self._client = anthropic.Anthropic()

    def call(self, system: str, user: str) -> str:
        if self.dry_run:
            bar = "─" * 70
            return (
                f"[DRY RUN — no API call made]\n{bar}\nSYSTEM:\n{system}\n{bar}\n"
                f"USER:\n{user}\n{bar}"
            )
        resp = self._client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return "".join(
            block.text for block in resp.content if getattr(block, "type", "") == "text"
        ).strip()


# --------------------------------------------------------------------------- #
# Modality auto-classification
# --------------------------------------------------------------------------- #

def classify_modality(runner: Runner, topic: str) -> str:
    if runner.dry_run:
        return "decisions"  # deterministic default for dry runs
    instruction = (
        "Classify the following task into exactly one category and reply with "
        "ONLY that single lowercase word, nothing else.\n\n"
        f"Categories: {', '.join(MODALITIES)}\n\n"
        "Guidance: 'decisions' = choosing among options / go-no-go / strategy; "
        "'research' = understanding or investigating a topic; "
        "'creative' = drafting or critiquing creative or written work; "
        "'technical' = code, architecture, debugging, technical design.\n\n"
        f"Task:\n{topic}"
    )
    answer = runner.call("You are a precise text classifier.", instruction).lower()
    for m in MODALITIES:
        if m in answer:
            return m
    return "decisions"


# --------------------------------------------------------------------------- #
# The session
# --------------------------------------------------------------------------- #

def run_session(runner: Runner, topic: str, modality: str, sequence: list[str]) -> dict:
    focus = load_modality_focus(modality)
    system = fill(runner.system, MODALITY=modality)
    passes: dict[str, str] = {}
    facts = NO_FACTS_YET

    for hat in sequence:
        template = read_prompt(hat_prompt_file(hat))

        if hat == "blue-close":
            all_passes = "\n\n".join(
                f"## {HAT_LABELS.get(h, h)}\n\n{passes[h]}" for h in sequence if h in passes
            )
            user = fill(
                template, TOPIC=topic, MODALITY=modality,
                MODALITY_FOCUS=focus, ALL_PASSES=all_passes,
            )
        elif hat == "blue-open":
            user = fill(template, TOPIC=topic, MODALITY=modality, MODALITY_FOCUS=focus)
        elif hat == "white":
            user = fill(
                template, TOPIC=topic, MODALITY=modality,
                MODALITY_FOCUS=focus, AGENDA=passes.get("blue-open", ""),
            )
        else:
            user = fill(
                template, TOPIC=topic, MODALITY=modality,
                MODALITY_FOCUS=focus, FACTS=facts,
            )

        sys.stderr.write(f"  · {HAT_LABELS.get(hat, hat)} …\n")
        sys.stderr.flush()
        result = runner.call(system, user)
        passes[hat] = result

        if hat == "white":
            facts = result  # force-feed forward to every subsequent hat

    return passes


def single_pass_prompt(topic: str, modality: str, sequence: list[str]) -> str:
    focus = load_modality_focus(modality)
    order = " → ".join(HAT_LABELS.get(h, h) for h in sequence)
    return textwrap.dedent(f"""\
        Run the following topic through a full Six Thinking Hats analysis, one
        hat at a time, in this order:

        {order}

        For each hat, write a clearly-headed section and think ONLY in that
        hat's mode. Keep the modes uncontaminated: Black = reasoned critique,
        Yellow = reasoned value, Green = ideas with judgment suspended, Red =
        gut feeling with NO justification, White = neutral facts and gaps, Blue
        = framing (open) and synthesis (close). The closing Blue section must
        synthesize the others into a bottom line, key tensions, and next
        actions.

        Task modality: {modality}
        {focus}

        Topic:
        {topic}
        """)


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #

def build_report(topic: str, modality: str, sequence: list[str],
                 passes: dict, model: str) -> str:
    lines = [
        "# Six Thinking Hats — Analysis",
        "",
        f"**Topic:** {topic.strip()}",
        "",
        f"**Modality:** `{modality}`  ·  **Sequence:** "
        + " → ".join(h.replace("blue-open", "blue").replace("blue-close", "blue")
                     for h in sequence),
        "",
        f"*Generated by the Six Hats framework (model: `{model}`).*",
        "",
        "---",
        "",
    ]
    for hat in sequence:
        if hat not in passes:
            continue
        lines += [f"## {HAT_LABELS.get(hat, hat)}", "", passes[hat].strip(), "", "---", ""]
    return "\n".join(lines).rstrip() + "\n"


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def get_topic(args) -> str:
    if args.topic_file:
        return Path(args.topic_file).read_text(encoding="utf-8").strip()
    if args.topic:
        return args.topic.strip()
    if not sys.stdin.isatty():
        data = sys.stdin.read().strip()
        if data:
            return data
    sys.exit("error: no topic given. Pass it as an argument, --topic-file, or via stdin.")


def main():
    p = argparse.ArgumentParser(
        prog="six_hats.py",
        description="Run any topic through the Six Thinking Hats framework.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("topic", nargs="?", help="the topic to analyze (or use --topic-file/stdin)")
    p.add_argument("--topic-file", help="read the topic from a file")
    p.add_argument("--modality", default="auto",
                   choices=["auto"] + MODALITIES,
                   help="task type; 'auto' classifies it first (default: auto)")
    p.add_argument("--sequence",
                   help="comma-separated middle-hat order override, "
                        "e.g. 'white,green,yellow,black,red' (blue is always added)")
    p.add_argument("--model", default=DEFAULT_MODEL,
                   help=f"model id (default: {DEFAULT_MODEL}; or set SIX_HATS_MODEL)")
    p.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS,
                   help=f"max tokens per hat (default: {DEFAULT_MAX_TOKENS})")
    p.add_argument("--single-pass", action="store_true",
                   help="one cheaper call instead of one call per hat")
    p.add_argument("--dry-run", action="store_true",
                   help="assemble and print prompts without calling the API")
    p.add_argument("-o", "--output", help="write the report to this file")
    args = p.parse_args()

    topic = get_topic(args)
    runner = Runner(args.model, args.max_tokens, args.dry_run)

    modality = args.modality
    if modality == "auto":
        sys.stderr.write("· classifying modality …\n")
        modality = classify_modality(runner, topic)
        sys.stderr.write(f"· modality → {modality}\n")

    sequence = resolve_sequence(modality, args.sequence)

    if args.single_pass:
        prompt = single_pass_prompt(topic, modality, sequence)
        sys.stderr.write("· running single-pass analysis …\n")
        body = runner.call(fill(runner.system, MODALITY=modality), prompt)
        report = (
            f"# Six Thinking Hats — Analysis (single-pass)\n\n"
            f"**Topic:** {topic.strip()}\n\n**Modality:** `{modality}`\n\n---\n\n{body}\n"
        )
    else:
        sys.stderr.write(f"· running {len(sequence)} hats ({modality}) …\n")
        passes = run_session(runner, topic, modality, sequence)
        report = build_report(topic, modality, sequence, passes, args.model)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        sys.stderr.write(f"· wrote {args.output}\n")
    else:
        sys.stdout.write(report)


if __name__ == "__main__":
    main()
