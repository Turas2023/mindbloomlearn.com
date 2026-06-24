---
name: mindbloom-product-pipeline
description: >-
  Orchestrates MindBloom Learn product asset generation from JSON input through
  worksheets, watermarked previews, Etsy covers, Pinterest pins, and paid PDFs.
  Use when generating a full product bundle, automating the asset pipeline,
  creating JSON-driven outputs, or when the user mentions product automation,
  asset pipeline, or multi-format deliverables for MindBloom Learn.
---

# MindBloom Product Pipeline

End-to-end workflow from the Automation-Pack specification. Read the pack docs before generating assets.

## Pack location

```
/Users/kash/Documents/MiraSolutionsllc/mindbloomlearn.com/Assets/Automation-Pack/
```

Key references:
- `MindBloom_Automation_Asset_Library.pdf` — central automation spec
- `MindBloom_Learn_Brand_Reference_Pack_v2.pdf` — brand + workflow (prefer v2; v1 has color hex values)
- `MindBloom_Universal_Template_Library/README_Template_Library.txt` — template rules

Repo canonical assets (use during generation):
- Logo: `assets/logo/mindbloomlearn.png`
- Mascots: `assets/mascots/Mindbloomlearn_{Questy|Nova|Riley|DrKai|Bloom|Hugo}.png`
- Existing patterns: `assets/occasions/`, `assets/wellness/`

## JSON input model

From `MindBloom_Automation_Asset_Library.pdf`:

```json
{
  "brand": "MindBloom Learn",
  "mascot": "Questy",
  "topic": "July 4th Coloring",
  "age": "4-8",
  "difficulty": "easy",
  "outputs": ["worksheet", "pdf", "pinterest", "etsy", "preview"]
}
```

| Field | Values |
|-------|--------|
| `mascot` | Questy, Nova, Riley, DrKai, Bloom, Hugo |
| `outputs` | `worksheet`, `pdf`, `preview`, `etsy`, `pinterest` |

See [json-model.md](json-model.md) for extended field notes and output folder layout.

## Workflow (in order)

```
JSON Input ? Worksheet ? Preview (watermarked) ? Etsy Cover ? Pinterest Pin ? Paid PDF
```

Copy this checklist and track progress:

```
- [ ] 1. Parse JSON input; confirm mascot + product line mapping
- [ ] 2. Generate worksheet(s) from universal template
- [ ] 3. Create watermarked preview PDF (free/lead-gen only)
- [ ] 4. Create Etsy cover (2000×1600)
- [ ] 5. Create Pinterest pin (1000×1500)
- [ ] 6. Export paid PDF (no watermark, high resolution)
- [ ] 7. Run brand consistency checklist
```

## Output folder structure

From `MindBloom_Automation_Asset_Library.pdf`:

```
/Mascots
/Etsy
/Pinterest
/Worksheets
/Previews
/PDFs
/JSON_Inputs
/Brand_References
```

When generating into the GitHub repo, mirror under `assets/` by product line and occasion (e.g. `assets/occasions/July4th/ColorQuest/`).

## Product line ? mascot mapping

| Mascot | Product line |
|--------|--------------|
| Questy | ColorQuest™ |
| Nova | STEMQuest™ |
| Riley | Every Mind Colors™ |
| DrKai | CareerQuest Kids™ |
| Bloom | Preschool Learning™ |
| Hugo | Homeschool Resources™ |

## Related skills

| Task | Skill |
|------|-------|
| Worksheets, activity books, lesson packs | `mindbloom-worksheet-templates` |
| Etsy covers, Pinterest pins, previews, paid PDFs | `mindbloom-marketing-assets` |
| Brand colors, mascot standards, poses | `mindbloom-brand-mascots` |

## Brand rules (always)

- Free previews: **watermarked**. Paid downloads: **no watermark**.
- Use official mascot PNGs — never redesign mascots.
- Logo: `assets/logo/mindbloomlearn.png` with full flower + lightbulb visible.
- Footer on printables: `© [YEAR] MindBloom Learn™ | A Mira Solutions LLC Brand | www.mindbloomlearn.com`
