#!/usr/bin/env python3
"""Render the animated README banner (assets/img/readme-banner.gif).

    pip install playwright pillow && playwright install chromium
    python3 tools/build_banner.py

The animation lives in tools/banner/banner.html (one setFrame(n) function, 72 frames).
To change the four highlight chips, edit the `facts` array there. Keep them to
results that are already on the page.
"""
import io
import os
import sys

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "tools", "banner", "banner.html")
OUT = os.path.join(ROOT, "assets", "img", "readme-banner.gif")
FRAMES, MS = 72, 70


def main():
    frames = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 400})
        pg.goto("file://" + SRC)
        pg.wait_for_timeout(800)  # let fonts load
        for f in range(FRAMES):
            pg.evaluate(f"setFrame({f})")
            frames.append(Image.open(io.BytesIO(pg.screenshot())).convert("RGB"))
        b.close()

    # One shared palette (built from a spread of frames) keeps colors stable and the file small.
    picks = [frames[i] for i in range(0, FRAMES, 9)]
    w, h = frames[0].size
    sheet = Image.new("RGB", (w, h * len(picks)))
    for i, f in enumerate(picks):
        sheet.paste(f, (0, i * h))
    pal = sheet.quantize(colors=255, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    q = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in frames]
    q[0].save(OUT, save_all=True, append_images=q[1:], duration=[MS] * FRAMES, loop=0, disposal=1)
    print(f"wrote {OUT} ({os.path.getsize(OUT) / 1e6:.2f} MB)")


if __name__ == "__main__":
    sys.exit(main())
