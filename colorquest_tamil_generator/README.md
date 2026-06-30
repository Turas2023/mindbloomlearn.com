# ColorQuest Tamil Adventures Generator

Template-driven worksheet generator for MindBloom Learn / ColorQuest Tamil Adventures.

Run:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python generate.py
```

Outputs:
output/*.png and output/*.pdf

Replace placeholder assets in assets/ with official:
questy.png, logo_colorquest.png, logo_mindbloom.png, vocabulary images.

The current generator draws its own page layout. It does not import PSD
templates. Missing image assets are rendered as labeled placeholders.
