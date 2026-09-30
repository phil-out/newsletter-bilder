#!/usr/bin/env python3
"""Macht aus svg/*.svg transparente png/*.png (für die Mails) — mit Google Chrome (headless).

    python3 zeichnungen.py && python3 render.py

Die Pixelgrösse steht in width/height jeder SVG-Datei (mind. 500 px breit, weil Chrome
kleinere Fenster nicht zuverlässig rendert).
"""
import re
import subprocess
import sys
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASIS = Path(__file__).parent


def main():
    ziel = BASIS / "png"
    ziel.mkdir(exist_ok=True)
    fehler = 0
    for quelle in sorted((BASIS / "svg").glob("*.svg")):
        kopf = quelle.read_text(encoding="utf-8")[:400]
        b, h = (int(x) for x in re.search(r'width="(\d+)" height="(\d+)"', kopf).groups())
        aus = ziel / f"{quelle.stem}.png"
        r = subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", f"--window-size={b},{h}",
            "--default-background-color=00000000", "--virtual-time-budget=5000",
            f"--screenshot={aus}", quelle.resolve().as_uri(),
        ], capture_output=True, text=True, timeout=60)
        if r.returncode or not aus.exists():
            fehler += 1
            print(f"FEHLER {quelle.name}: {r.stderr[-300:]}")
        else:
            print(f"{aus.name:28} {b}×{h}  {aus.stat().st_size // 1024} KB")
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main()
