# JSON Automation Model — Extended Reference

Source: `MindBloom_Automation_Asset_Library.pdf`, `MindBloom_Learn_Brand_Reference_Pack_v2.pdf`

## Minimal schema

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

## Suggested extended fields

```json
{
  "brand": "MindBloom Learn",
  "productLine": "ColorQuest",
  "mascot": "Questy",
  "topic": "July 4th Coloring",
  "age": "4-8",
  "difficulty": "easy",
  "occasion": "July4th",
  "year": 2026,
  "website": "www.mindbloomlearn.com",
  "outputs": ["worksheet", "preview", "etsy", "pinterest", "pdf"],
  "worksheet": {
    "template": "bw",
    "pages": 1
  },
  "activityBook": false,
  "lessonPack": false
}
```

## Output ? file mapping

| `outputs` value | Deliverable | Template / spec |
|-----------------|-------------|-----------------|
| `worksheet` | Printable worksheet PNG/PDF | `01` or `02` universal worksheet template |
| `preview` | Watermarked preview PDF | `03` watermarked preview template |
| `etsy` | Etsy listing cover JPG/PNG | `05` Etsy cover 2000×1600 |
| `pinterest` | Pinterest pin JPG/PNG | `04` Pinterest 1000×1500 |
| `pdf` | Paid full PDF (no watermark) | Paid PDF spec in Automation Asset Library |

## Example output paths (repo)

```
assets/occasions/{Occasion}/{ProductLine}/{ProductLine}_{Occasion}_{age}.pdf
assets/occasions/{Occasion}/{ProductLine}/{ProductLine}_{Occasion}_{age}.png
assets/occasions/{Occasion}/Etsy_Thumbnail_{Occasion}.png
```

Follow naming patterns already in `assets/occasions/fathers-day/` and `assets/occasions/July4th/`.
