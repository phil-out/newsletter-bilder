#!/usr/bin/env python3
"""Alle Illustrationen des Newsletters als SVG-Quellen.

    python3 zeichnungen.py      # schreibt svg/*.svg
    zsh render.sh               # macht daraus png/*.png (für die Mails)

Stil: flach, geometrisch, Punkt-Augen + Lächeln, wenige Farben (siehe FARBEN).
"""
from pathlib import Path

INK, ROT, BLAU, GELB, ROSA = "#23203A", "#F0522E", "#2E6BE6", "#FFC53D", "#F6B7C3"
WOLKE, WEISS, CREME, DUNKEL = "#DCE6FA", "#FFFDF8", "#FBF5EA", "#2B3553"

ORDNER = Path(__file__).parent / "svg"


def gesicht(cx, cy, abstand=10, r=3.6, laecheln=True, backen=True, farbe=INK, strich=3):
    """Augen, Lächeln und Bäckchen um (cx, cy)."""
    s = (f'<circle cx="{cx - abstand}" cy="{cy}" r="{r}" fill="{farbe}"/>'
         f'<circle cx="{cx + abstand}" cy="{cy}" r="{r}" fill="{farbe}"/>')
    if laecheln:
        b = abstand * 0.9
        s += (f'<path d="M{cx - b} {cy + 10} q{b} {b * 0.8} {2 * b} 0" stroke="{farbe}" '
              f'stroke-width="{strich}" fill="none" stroke-linecap="round"/>')
    if backen:
        s += (f'<circle cx="{cx - abstand * 1.8}" cy="{cy + 9}" r="{r * 1.25}" fill="{ROSA}"/>'
              f'<circle cx="{cx + abstand * 1.8}" cy="{cy + 9}" r="{r * 1.25}" fill="{ROSA}"/>')
    return s


def funkeln(x, y, r=6):
    return (f'<path d="M{x} {y - r}l{r * .4} {r * .6} {r * .6} {r * .4}-{r * .6} {r * .4}'
            f'-{r * .4} {r * .6}-{r * .4}-{r * .6}-{r * .6}-{r * .4} {r * .6}-{r * .4}z" fill="{GELB}"/>')


def svg(vb, breite, hoehe, inhalt, stil=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{breite}" height="{hoehe}">'
            f'{stil}{inhalt}</svg>\n')


# ---------------------------------------------------------------- Rubriken (120 × 120)

RUBRIKEN = {
    "wochenende": (  # Sonne
        f'<g stroke="{GELB}" stroke-width="8" stroke-linecap="round"><path d="M60 8v12M60 100v12M8 60h12M100 60h12'
        f'M23 23l8.5 8.5M88.5 88.5L97 97M23 97l8.5-8.5M88.5 31.5L97 23"/></g>'
        f'<circle cx="60" cy="60" r="30" fill="{GELB}"/>' + gesicht(60, 56)),
    "planb": (  # Schirm
        f'<path d="M16 62A44 44 0 0 1 104 62Q93 53 82 62Q71 53 60 62Q49 53 38 62Q27 53 16 62Z" fill="{ROT}"/>'
        f'<path d="M60 62V98Q60 108 50 108Q43 108 43 101" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>'
        + gesicht(60, 40, abstand=9, r=3.4, backen=False) +
        f'<g fill="{BLAU}"><path d="M18 80q5 7 0 12q-5-5 0-12z"/><path d="M98 76q5 7 0 12q-5-5 0-12z"/>'
        f'<path d="M84 98q5 7 0 12q-5-5 0-12z"/></g>'),
    "events": (  # Ballone
        f'<g stroke="{INK}" stroke-width="2" fill="none"><path d="M42 70Q48 92 60 110"/><path d="M80 64Q72 90 60 110"/>'
        f'<path d="M60 82V110"/></g>'
        f'<circle cx="42" cy="46" r="23" fill="{ROT}"/><path d="M38 68h8l-4 5z" fill="{ROT}"/>'
        f'<circle cx="80" cy="40" r="22" fill="{BLAU}"/><path d="M76 61h8l-4 5z" fill="{BLAU}"/>'
        f'<circle cx="60" cy="60" r="21" fill="{GELB}"/><path d="M56 80h8l-4 5z" fill="{GELB}"/>'
        + gesicht(60, 57, abstand=7, r=3, backen=False, strich=2.6)),
    "kultur": (  # Billett
        f'<g transform="rotate(-10 60 60)"><path d="M16 36H104V52A8 8 0 0 0 104 68V84H16V68A8 8 0 0 0 16 52Z" fill="{ROT}"/>'
        f'<path d="M40 41V79" stroke="{CREME}" stroke-width="3" stroke-dasharray="5 5"/>'
        + gesicht(73, 56, abstand=9, r=3.4, backen=False) + '</g>' + funkeln(18, 22, 7) + funkeln(104, 100, 6)),
    "ausflug": (  # Berg mit Gesicht
        f'<circle cx="94" cy="28" r="12" fill="{GELB}"/>'
        f'<path d="M8 106C20 70 38 32 60 32C82 32 100 70 112 106Z" fill="{BLAU}"/>'
        + gesicht(60, 62) +
        f'<g fill="{WEISS}"><circle cx="26" cy="96" r="12"/><circle cx="42" cy="90" r="15"/><circle cx="58" cy="98" r="10"/>'
        f'<rect x="14" y="96" width="54" height="12" rx="6"/></g>'),
    "spielplatz": (  # Rutschbahn
        f'<path d="M28 104V40M46 104V40M28 56h18M28 72h18M28 88h18" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/>'
        f'<rect x="22" y="32" width="40" height="10" rx="5" fill="{BLAU}"/>'
        f'<path d="M58 38C84 40 80 92 110 96" stroke="{ROT}" stroke-width="13" fill="none" stroke-linecap="round"/>'
        f'<circle cx="96" cy="46" r="13" fill="{GELB}"/>' + gesicht(96, 44, abstand=5, r=2.6, backen=False, strich=2.4)),
    "kulinarik": (  # Schüssel
        f'<path d="M72 60L96 18" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
        f'<circle cx="44" cy="58" r="11" fill="{GELB}"/><circle cx="62" cy="54" r="12" fill="{ROT}"/><circle cx="80" cy="59" r="9" fill="{GELB}"/>'
        f'<path d="M14 62H106C106 90 88 106 60 106C32 106 14 90 14 62Z" fill="{BLAU}"/>'
        + gesicht(60, 78, backen=True)),
    "rezept": (  # Kochtopf
        f'<g stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round" opacity=".35">'
        f'<path d="M46 20q-6 6 0 12t0 12M60 14q-6 6 0 12t0 12M74 20q-6 6 0 12t0 12"/></g>'
        f'<path d="M30 52Q60 30 90 52Z" fill="{BLAU}"/><circle cx="60" cy="38" r="5" fill="{INK}"/>'
        f'<rect x="12" y="62" width="16" height="9" rx="4.5" fill="{ROT}"/><rect x="92" y="62" width="16" height="9" rx="4.5" fill="{ROT}"/>'
        f'<rect x="24" y="52" width="72" height="54" rx="16" fill="{ROT}"/>' + gesicht(60, 76)),
    "basteln": (  # Farbstift
        f'<path d="M14 104q10-10 20 0t20 0t20 0" stroke="{ROT}" stroke-width="4" fill="none" stroke-linecap="round"/>'
        f'<g transform="rotate(-35 60 56)"><rect x="10" y="44" width="16" height="24" rx="6" fill="{ROSA}"/>'
        f'<rect x="22" y="44" width="62" height="24" fill="{GELB}"/><rect x="22" y="44" width="7" height="24" fill="{BLAU}"/>'
        f'<path d="M84 44L108 56L84 68Z" fill="#F4D6AE"/><path d="M100 52L108 56L100 60Z" fill="{INK}"/>'
        + gesicht(56, 52, abstand=7, r=3, laecheln=True, backen=False, strich=2.4) + '</g>'),
    "entwicklung": (  # Bauklötze
        f'<path d="M16 60L39 22L62 60Z" fill="{BLAU}" stroke="{BLAU}" stroke-width="4" stroke-linejoin="round"/>'
        f'<rect x="16" y="62" width="46" height="44" rx="5" fill="{ROT}"/>' + gesicht(39, 80, abstand=8, r=3.2, backen=False) +
        f'<circle cx="86" cy="88" r="18" fill="{GELB}"/><rect x="72" y="54" width="28" height="16" rx="8" fill="{ROSA}"/>'),
    "alltag": (  # Wecker
        f'<path d="M40 94L31 106M80 94L89 106" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
        f'<circle cx="34" cy="30" r="11" fill="{BLAU}"/><circle cx="86" cy="30" r="11" fill="{BLAU}"/>'
        f'<rect x="55" y="20" width="10" height="10" rx="3" fill="{INK}"/>'
        f'<circle cx="60" cy="64" r="36" fill="{ROT}"/><circle cx="60" cy="64" r="27" fill="{WEISS}"/>'
        f'<path d="M60 64V46M60 64H73" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
        f'<circle cx="60" cy="64" r="3.5" fill="{INK}"/>'
        f'<circle cx="49" cy="74" r="2.8" fill="{INK}"/><circle cx="71" cy="74" r="2.8" fill="{INK}"/>'
        f'<path d="M54 81q6 5 12 0" stroke="{INK}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'),
    "brauchtum": (  # Räbeliechtli
        f'<path d="M18 16H102" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
        f'<path d="M60 16V36" stroke="{INK}" stroke-width="2.5"/>'
        f'<rect x="44" y="34" width="32" height="10" rx="5" fill="{BLAU}"/>'
        f'<circle cx="60" cy="74" r="32" fill="{ROT}"/>'
        f'<circle cx="49" cy="66" r="5" fill="{GELB}"/><circle cx="71" cy="66" r="5" fill="{GELB}"/>'
        f'<path d="M46 80Q60 96 74 80Q60 88 46 80Z" fill="{GELB}"/>' + funkeln(102, 58, 7) + funkeln(18, 88, 6)),
    "surprise": (  # Geschenk
        funkeln(16, 24, 7) + funkeln(104, 20, 6) +
        f'<ellipse cx="48" cy="34" rx="13" ry="8" transform="rotate(-25 48 34)" fill="{ROT}"/>'
        f'<ellipse cx="72" cy="34" rx="13" ry="8" transform="rotate(25 72 34)" fill="{ROT}"/>'
        f'<rect x="24" y="56" width="72" height="50" rx="7" fill="{BLAU}"/>'
        f'<rect x="18" y="42" width="84" height="18" rx="6" fill="{BLAU}"/>'
        f'<rect x="54" y="42" width="12" height="64" fill="{ROT}"/><circle cx="60" cy="40" r="6" fill="{ROT}"/>'
        f'<circle cx="41" cy="77" r="3.4" fill="{INK}"/><circle cx="79" cy="77" r="3.4" fill="{INK}"/>'
        f'<path d="M45 89q15 10 30 0" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>'),
    "news": (  # Megafon
        f'<path d="M92 44q10 16 0 32M101 34q16 26 0 52" stroke="{BLAU}" stroke-width="4.5" fill="none" stroke-linecap="round"/>'
        f'<path d="M46 74L52 98" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
        f'<path d="M34 46L84 24V96L34 74Z" fill="{ROT}" stroke="{ROT}" stroke-width="4" stroke-linejoin="round"/>'
        f'<rect x="18" y="44" width="20" height="32" rx="7" fill="{BLAU}"/>'
        + gesicht(62, 56, abstand=8, r=3.2, backen=False, strich=2.6)),
    "comingup": (  # Rakete
        f'<path d="M48 96q12 22 24 0z" fill="{GELB}"/>'
        f'<path d="M60 10C84 30 84 72 76 94H44C36 72 36 30 60 10z" fill="{ROT}"/>'
        f'<path d="M44 70L26 92L44 92zM76 70L94 92L76 92z" fill="{BLAU}"/>'
        f'<circle cx="60" cy="48" r="13" fill="{WEISS}"/><circle cx="60" cy="48" r="8" fill="{BLAU}"/>'
        + funkeln(22, 36, 7) + funkeln(98, 50, 5.5)),
    "vorgemerkt": (  # Merkzettel mit Pin
        f'<g transform="rotate(-6 60 62)"><path d="M22 26H98V82L76 104H22Z" fill="{GELB}"/>'
        f'<path d="M76 104V82H98Z" fill="#E8A92A"/>'
        + gesicht(56, 62, abstand=10, r=3.6) +
        f'<path d="M36 88H64" stroke="{INK}" stroke-width="3" stroke-linecap="round" opacity=".25"/></g>'
        f'<circle cx="60" cy="24" r="9" fill="{ROT}"/><circle cx="57" cy="21" r="3" fill="#FFFFFF" opacity=".6"/>'),
    "wochentags": (  # Kindergarten-Täschli
        f'<path d="M44 30Q44 14 60 14Q76 14 76 30" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>'
        f'<rect x="24" y="28" width="72" height="80" rx="20" fill="{BLAU}"/>'
        f'<rect x="34" y="70" width="52" height="30" rx="10" fill="{ROT}"/>'
        f'<rect x="54" y="66" width="12" height="9" rx="3" fill="{GELB}"/>'
        + gesicht(60, 46, abstand=10, r=3.6)),
    "monat": (  # Kalenderblatt (Quartals-News)
        f'<rect x="20" y="24" width="80" height="82" rx="12" fill="{WEISS}"/>'
        f'<path d="M20 36A12 12 0 0 1 32 24H88A12 12 0 0 1 100 36V48H20Z" fill="{ROT}"/>'
        f'<rect x="37" y="14" width="7" height="18" rx="3.5" fill="{INK}"/><rect x="76" y="14" width="7" height="18" rx="3.5" fill="{INK}"/>'
        + gesicht(60, 70)),
}

# ---------------------------------------------------------------- Wetter (60 × 60)

def wolke(y):
    return f'<path d="M11 {y}a10 10 0 0 1 2-19.6A14 14 0 0 1 39.5 {y - 21} 10 10 0 0 1 48 {y}z" fill="{WOLKE}"/>'


def w_augen(y, laecheln=False):
    s = f'<circle cx="25" cy="{y}" r="2" fill="{INK}"/><circle cx="35" cy="{y}" r="2" fill="{INK}"/>'
    if laecheln:
        s += f'<path d="M26 {y + 5.5}q4 2.6 8 0" stroke="{INK}" stroke-width="1.8" fill="none" stroke-linecap="round"/>'
    return s


WETTER = {
    "sonne": (f'<g stroke="{GELB}" stroke-width="4.5" stroke-linecap="round"><path d="M30 5v7M30 48v7M5 30h7M48 30h7'
              f'M12.3 12.3l5 5M42.7 42.7l5 5M12.3 47.7l5-5M42.7 17.3l5-5"/></g><circle cx="30" cy="30" r="14" fill="{GELB}"/>'
              f'<circle cx="25" cy="28" r="2" fill="{INK}"/><circle cx="35" cy="28" r="2" fill="{INK}"/>'
              f'<path d="M25.5 34q4.5 4 9 0" stroke="{INK}" stroke-width="2" fill="none" stroke-linecap="round"/>'),
    "teils": (f'<circle cx="37" cy="21" r="12" fill="{GELB}"/>'
              f'<path d="M13 46a9 9 0 0 1 2-17.6A12 12 0 0 1 37.5 31 8 8 0 0 1 45 46z" fill="{WOLKE}"/>'
              f'<circle cx="24" cy="38" r="1.9" fill="{INK}"/><circle cx="33" cy="38" r="1.9" fill="{INK}"/>'),
    "wolke": wolke(44) + w_augen(33, laecheln=True),
    "regen": wolke(36) + w_augen(26) +
             f'<g fill="{BLAU}"><path d="M19 42q3 4 0 7q-3-3 0-7z"/><path d="M30 44q3 4 0 7q-3-3 0-7z"/><path d="M41 42q3 4 0 7q-3-3 0-7z"/></g>',
    "nebel": wolke(34) + w_augen(24) +
             '<g stroke="#C9D3E8" stroke-width="4" stroke-linecap="round"><path d="M10 42h30M20 50h30"/></g>',
    "schnee": wolke(36) + w_augen(26) +
              f'<g fill="{BLAU}"><circle cx="19" cy="45" r="2.6"/><circle cx="30" cy="49" r="2.6"/><circle cx="41" cy="45" r="2.6"/>'
              f'<circle cx="24" cy="54" r="2.2"/><circle cx="36" cy="54" r="2.2"/></g>',
    "gewitter": wolke(36) + w_augen(26) + f'<path d="M31 38L24 50H31L27 59L39 45H32L36 38Z" fill="{GELB}"/>',
}

# ---------------------------------------------------------------- Kopf, Fuss, Linien

SCHRIFT = ('<style>@import url("https://fonts.googleapis.com/css2?family=Fredoka:wght@700&amp;display=block");'
           'text{font-family:Fredoka,Arial,sans-serif;font-weight:700}</style>')

HELD_TRAM = (  # Zürcher Cobra-Tram, Linie 13 (Höngg)
    f'<defs><clipPath id="cobra"><path d="M116 106H418C452 106 474 124 482 156L486 176C488 188 481 196 470 196H112'
    f'C102 196 96 189 96 180V124C96 113 104 106 116 106Z"/></clipPath></defs>'
    f'<ellipse cx="292" cy="146" rx="250" ry="84" fill="{WOLKE}"/>'
    f'<ellipse cx="300" cy="300" rx="420" ry="112" fill="{GELB}"/>'
    f'<circle cx="530" cy="80" r="28" fill="{ROT}"/>'
    f'<circle cx="521" cy="76" r="3" fill="{INK}"/><circle cx="539" cy="76" r="3" fill="{INK}"/>'
    f'<path d="M521 86q9 7 18 0" stroke="{INK}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
    f'<path d="M446 54q7-7 14 0q7-7 14 0M480 80q5-5 10 0q5-5 10 0" stroke="{BLAU}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
    f'<g fill="{WEISS}"><circle cx="48" cy="84" r="18"/><circle cx="72" cy="76" r="24"/><circle cx="98" cy="86" r="16"/>'
    f'<rect x="32" y="84" width="80" height="18" rx="9"/><circle cx="556" cy="156" r="14"/><circle cx="578" cy="150" r="20"/>'
    f'<rect x="544" y="154" width="60" height="15" rx="7.5"/></g>'
    f'<g fill="{INK}"><circle cx="150" cy="197" r="10"/><circle cx="292" cy="197" r="10"/><circle cx="432" cy="197" r="10"/></g>'
    f'<g fill="#C9D3E8"><rect x="130" y="99" width="46" height="10" rx="5"/><rect x="368" y="99" width="40" height="10" rx="5"/></g>'
    f'<path d="M226 106L246 80L232 68M246 80L266 106M216 68H250" stroke="{INK}" stroke-width="3" fill="none" '
    f'stroke-linejoin="round" stroke-linecap="round"/>'
    f'<path d="M116 106H418C452 106 474 124 482 156L486 176C488 188 481 196 470 196H112C102 196 96 189 96 180V124'
    f'C96 113 104 106 116 106Z" fill="#FFFFFF"/>'
    f'<rect x="90" y="152" width="400" height="50" fill="{BLAU}" clip-path="url(#cobra)"/>'
    f'<g fill="{DUNKEL}"><rect x="110" y="118" width="36" height="28" rx="7"/><rect x="152" y="118" width="36" height="28" rx="7"/>'
    f'<rect x="204" y="118" width="36" height="28" rx="7"/><rect x="246" y="118" width="36" height="28" rx="7"/>'
    f'<rect x="300" y="118" width="36" height="28" rx="7"/><rect x="384" y="118" width="30" height="28" rx="7"/>'
    f'<path d="M422 116H440C458 118 470 130 476 148H422Z"/></g>'
    f'<path d="M196 106v90M292 106v90" stroke="#DCE2EE" stroke-width="3"/>'
    f'<rect x="342" y="118" width="36" height="28" rx="7" fill="{GELB}"/>'
    f'<text x="360" y="140" text-anchor="middle" font-size="21" fill="{INK}">13</text>'
    f'<circle cx="440" cy="130" r="6" fill="{WEISS}"/><circle cx="458" cy="130" r="6" fill="{WEISS}"/>'
    f'<circle cx="442" cy="131" r="3" fill="{INK}"/><circle cx="460" cy="131" r="3" fill="{INK}"/>'
    f'<path d="M444 168q12 8 24 0" stroke="{WEISS}" stroke-width="3.2" fill="none" stroke-linecap="round"/>'
    f'<circle cx="436" cy="166" r="4.5" fill="{ROSA}"/><circle cx="479" cy="184" r="3.5" fill="{GELB}"/>'
)

FUSS_DINO = (
    f'<path d="M30 86Q10 90 4 70Q22 80 38 74z" fill="{BLAU}"/><ellipse cx="72" cy="80" rx="40" ry="24" fill="{BLAU}"/>'
    f'<path d="M96 70Q104 40 118 34" stroke="{BLAU}" stroke-width="18" fill="none" stroke-linecap="round"/>'
    f'<circle cx="124" cy="32" r="16" fill="{BLAU}"/>'
    f'<g fill="{ROT}"><path d="M46 58l7-12 7 12z"/><path d="M62 56l7-13 7 13z"/><path d="M78 58l7-12 7 12z"/></g>'
    f'<rect x="50" y="96" width="10" height="18" rx="5" fill="{BLAU}"/><rect x="80" y="96" width="10" height="18" rx="5" fill="{BLAU}"/>'
    f'<circle cx="128" cy="28" r="3.4" fill="{WEISS}"/><circle cx="129" cy="28" r="1.8" fill="{INK}"/>'
    f'<path d="M124 39q5 3 10-1" stroke="{WEISS}" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
    f'<path d="M8 116H152" stroke="{GELB}" stroke-width="5" stroke-linecap="round"/>'
)


def welle(breite, farbe, strich):
    p, x = "M2 8 Q17 1 32 8", 32
    while x + 30 <= breite - 2:
        x += 30
        p += f" T{x} 8"
    return f'<path d="{p}" stroke="{farbe}" stroke-width="{strich}" fill="none" stroke-linecap="round"/>'


def main():
    ORDNER.mkdir(exist_ok=True)
    dateien = {}
    for name, inhalt in RUBRIKEN.items():
        dateien[f"rubrik-{name}"] = svg("0 0 120 120", 512, 512, inhalt)
    for name, inhalt in WETTER.items():
        dateien[f"wetter-{name}"] = svg("0 0 60 60", 512, 512, inhalt)
    dateien["held-tram"] = svg("0 30 600 200", 1800, 600, HELD_TRAM, stil=SCHRIFT)
    dateien["fuss-dino"] = svg("0 0 160 120", 640, 480, FUSS_DINO)
    dateien["welle"] = svg("0 0 544 14", 1632, 42, welle(544, BLAU, 3.5))
    dateien["schnoerkel"] = svg("0 0 190 14", 570, 42, welle(190, ROT, 4))
    for name, inhalt in dateien.items():
        (ORDNER / f"{name}.svg").write_text(inhalt, encoding="utf-8")
    print(f"{len(dateien)} SVG-Dateien geschrieben.")


if __name__ == "__main__":
    main()
