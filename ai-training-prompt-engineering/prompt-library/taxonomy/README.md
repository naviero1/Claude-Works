# Prompt Element Taxonomy — source of truth

**Version 1.0 · August 2026 · Owner: Oscar Penny**

The machine-readable ontology behind the prompt-engineering tools. OOP reading: **element = class · attribute = property · option = allowed value · technique = method · template/preset = instance**. Agentic elements inherit from their generative ancestors (`Mission extends Task`, adding a definition of done).

| File | Contains |
|---|---|
| `meta.json` | version, OOP legend, the two modes |
| `generative.json` | 7 elements (Role, Task, Context, Format, Examples, The Out, The Stop) — attributes, options, techniques, anti-patterns |
| `agentic.json` | 12 mission-brief blocks (role → reporting) — same structure |
| `presets.json` | 14 instances — the G/A library templates as saved configurations |

**Current size:** 19 elements · 78 attributes (children included) · 286 options · 14 presets.

## The three generated tools

Edit the JSON here, then regenerate — never edit the artifacts directly:

```bash
cd ../../src
python3 build_builder.py            # -> deliverables/Prompt_Template_Creator.html
python3 build_taxonomy_pdf.py       # -> deliverables/Prompt_Element_Taxonomy_Reference.pdf
python3 build_configurator_xlsx.py  # -> deliverables/Prompt_Template_Configurator.xlsx
#   then: python3 <xlsx-skill>/scripts/recalc.py ../deliverables/Prompt_Template_Configurator.xlsx
```

`build_builder.py` validates everything (unique ids, preset paths and labels resolve) — a broken edit fails the build, not the user.

## Editing rules

- **Options**: `label` (short, unique within its attribute), `phrase` (the exact text emitted into the prompt — `{{slots}}` welcome; the tools flag unfilled ones), `when` (one line of guidance), optional `"tier": "extended"`.
- **Attributes**: `pick` is `one` / `many` / `text`; `emit_label` prefixes the emitted block; `children` nest one level (the grandchildren).
- Phrases must not contain literal spreadsheet error tokens (`#VALUE!` etc.) — the xlsx recalc scanner flags them.
- Bump `meta.json` version + note the change in the library README when you materially change the ontology.

## Grounding

The structure is validated against the research in `../../notes/research/` (t1–t6): The Prompt Report's component anatomy and 58-technique taxonomy, White et al.'s pattern catalog (whose "fundamental contextual statements" are this file's attributes), the 30-framework slot inventory (CO-STAR, CRISPE, RTF, PTCF, GCSE…), shipped product pickers (tone, reading level, verbosity, reasoning effort), DSPy/LangChain/API decompositions, and vendor agentic guidance (autonomy levels, permission modes, check types).
