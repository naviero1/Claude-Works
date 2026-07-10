# CLI — `six_hats.py`

A standalone runner that takes any topic and runs it through the Six Thinking
Hats framework, one hat per model call, then synthesizes the result.

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
# optional: pick a current model id from https://docs.claude.com/en/docs/about-claude/models
export SIX_HATS_MODEL=claude-sonnet-4-5
```

## Use

```bash
# auto-detect the task type, run all hats, print a Markdown report
python six_hats.py "Should we rewrite the billing service in Go?"

# force a modality and save to a file
python six_hats.py "Is now a good time to switch careers?" \
    --modality decisions -o career.md

# feed a long topic from a file, or via stdin
python six_hats.py --topic-file design_doc.md --modality technical
cat notes.md | python six_hats.py --modality research

# custom hat order (blue open/close are always added)
python six_hats.py "..." --modality decisions \
    --sequence white,green,black,yellow,red

# cheap single-call version (isolation left to the model)
python six_hats.py "..." --single-pass

# inspect the exact prompts with NO api key and NO network call
python six_hats.py "test topic" --modality research --dry-run
```

## What it does

1. **Blue (open)** frames the session and, in `auto` mode, classifies the
   modality (`decisions` / `research` / `creative` / `technical`).
2. **White** produces the shared facts + gaps. Its output — and only its
   output — is fed forward to every hat that runs after it.
3. Each remaining hat runs as its **own call, blind to the other hats**. That
   isolation is the whole point (see `../spec/framework.md`).
4. **Blue (close)** reads every pass and synthesizes a bottom line, the key
   tensions, and next actions.

Because each hat is a separate call, the six hats map directly onto six
single-purpose agents — this script is a reference for what an agent
orchestration would do.

## Flags

| Flag | Meaning |
|------|---------|
| `topic` / `--topic-file` / stdin | where the topic comes from (pick one) |
| `--modality` | `auto` (default), `decisions`, `research`, `creative`, `technical` |
| `--sequence` | comma-separated middle-hat order override |
| `--model` | model id (default from `SIX_HATS_MODEL` or `claude-sonnet-4-5`) |
| `--max-tokens` | per-hat token cap (default 2000) |
| `--single-pass` | one call instead of one-per-hat (cheaper, lower fidelity) |
| `--dry-run` | print assembled prompts; no key or network needed |
| `-o/--output` | write the report to a file instead of stdout |

Progress is written to **stderr**, the report to **stdout**, so you can pipe the
report cleanly: `python six_hats.py "..." > out.md`.
