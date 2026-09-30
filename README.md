# Newsletter-Bilder

Illustrationen für einen privaten Familien-Newsletter. Dieses Repo ist nur öffentlich,
damit Mail-Programme die Bilder laden können — es enthält **keine** Inhalte oder
persönlichen Daten, nur Zeichnungen.

- `zeichnungen.py` — alle Illustrationen als Code (flach, geometrisch, mit Gesichtern)
- `svg/` — daraus erzeugte SVG-Quellen
- `png/` — daraus gerenderte Bilder, die die Mails verwenden

```bash
python3 zeichnungen.py && python3 render.py   # braucht Google Chrome (macOS)
```
