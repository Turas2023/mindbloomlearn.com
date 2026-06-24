---
name: mindbloom-worksheet-templates
description: >-
  Creates MindBloom Learn printable worksheets, activity books, and lesson packs
  using Universal Template Library PDFs/PNGs. Use when building worksheets,
  activity books, lesson packs, 8.5x11 printables, or student/teacher PDFs
  for MindBloom Learn products.
---

# MindBloom Worksheet Templates

## Pack location

```
/Users/kash/Documents/MiraSolutionsllc/mindbloomlearn.com/Assets/Automation-Pack/MindBloom_Universal_Template_Library/
```

## Templates

| # | File | Use case | Size |
|---|------|----------|------|
| 01 | `01_Universal_Worksheet_Template_BW.pdf` / `.png` | Black & white printable worksheet | 2550×3300 (8.5×11 @ 300 DPI) |
| 02 | `02_Universal_Worksheet_Template_Color_Neutral.pdf` / `.png` | Color-neutral worksheet | 2550×3300 |
| 06 | `06_Universal_Activity_Book_Template.pdf` | Multi-page activity book | 8.5×11 portrait |
| 07 | `07_Universal_Lesson_Pack_Template.pdf` | Teacher/parent lesson pack | 8.5×11 portrait |

PNG previews exist for templates 01–05; use PNGs as layout reference when compositing.

## Worksheet layout (templates 01–02)

From `MindBloom_Automation_Asset_Library.pdf`:
- 8.5×11 portrait
- Header with logo + product line
- Mascot callout area
- Activity content blocks
- Footer copyright: `© [YEAR] MindBloom Learn™ | A Mira Solutions LLC Brand | [WEBSITE]`

## Activity book pages (template 06)

Placeholder structure per page type:

| Page | Placeholder tokens |
|------|-------------------|
| Cover | `[PRODUCT LINE]`, `[TOPIC]`, `[AGE RANGE]`, `[COVER PAGE PLACEHOLDER]` |
| Table of Contents | `[TABLE OF CONTENTS PLACEHOLDER]` |
| Activity | `[ACTIVITY PAGE PLACEHOLDER]` |
| Answer Key | `[ANSWER KEY PLACEHOLDER]` |
| Certificate | `[CERTIFICATE PLACEHOLDER]` |

## Lesson pack pages (template 07)

One PDF section per page type; each uses:
- `[PRODUCT LINE]`, `[LESSON TITLE]`, `[GRADE / AGE]`, `[MASCOT]`
- `[SECTION TITLE]`, `[CONTENT / INSTRUCTIONS]`, `[NOTES / DIFFERENTIATION]`

Page types: Lesson Overview, Learning Objectives, Materials Needed, Teacher/Parent Guide, Student Worksheet, Reflection, Answer Key.

## Workflow

1. **Choose template** — BW for coloring-heavy; color-neutral for mixed activities; 06 for books; 07 for lesson packs.
2. **Load canonical assets** — logo from `assets/logo/mindbloomlearn.png`; mascot from `assets/mascots/` or Automation-Pack transparent lineup (see `mindbloom-brand-mascots`).
3. **Replace placeholders** — product line, topic, age range, year, website.
4. **Compose activity content** — match existing repo examples under `assets/occasions/`.
5. **Export** — 300 DPI PNG/PDF for paid deliverables; no watermark on paid worksheets.

## Template selection

```
Single printable page?     ? 01 (BW) or 02 (color-neutral)
Multi-page book?           ? 06 (cover + TOC + activities + answers + certificate)
Teacher lesson bundle?     ? 07 (overview through answer key)
```

## Rules (from README_Template_Library.txt)

- Free previews should be watermarked (use `mindbloom-marketing-assets` for preview PDFs).
- Paid downloads must not contain watermarks.
- Use official mascot references; do not redesign mascots.

## Existing repo patterns

Study before creating new assets:
- `assets/occasions/fathers-day/` — multi-product-line occasion set
- `assets/occasions/July4th/ColorQuest/` — age-banded PDFs + PNGs
- `assets/wellness/` — brain fitness card layouts
