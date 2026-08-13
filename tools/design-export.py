#!/usr/bin/env python3
"""Emit the NoughtVault batik work as a Claude Design system bundle.

Writes dist/design-system/**, one standalone preview per component. Each file
carries a first-line @dsCard marker, which is what the Design System pane reads
to build its card index — so the bundle can be pushed with DesignSync without
any explicit asset registration.

Every specimen is drawn by tools/batik.py, the same code that draws the figures
in textile-000-batik.html, so the design system and the specification cannot
drift apart.
"""
import os
import shutil

from batik import (BASE, INNER, KEPALA, N, PLINTH, SHOOT, SQ, TEPI, HEM, VOID,
                   RESIST, cecek_row, counter, inset_tri, medallion, mm,
                   rebung, square, txt)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "dist", "design-system")

TOKENS = [
    ("--void", "#000000", "the ground. Every document, every colourway."),
    ("--resist", "#EDE6D6", "raw undyed cotton — where the wax was. The accent."),
    ("--nila", "#2F5B78", "the indigo dip. Vault tier only."),
    ("--titanium", "#8A8C8E", "labels, dimensions, secondary prose."),
    ("--prose", "#C4BDB2", "running text. Warm, against the cold accent."),
    ("--rule", "#1B1B1B", "hairlines and section divisions."),
    ("--panel", "#070707", "raised surfaces, one step off the void."),
]

COLOURWAYS = [
    ("00 VOID", VOID, "#EDE6D6", None, "black ground, undyed line", "the house · Batch 001"),
    ("01 RAKING", VOID, "#191919", None, "black wax on black ground", "held for year two"),
    ("02 TITANIUM", VOID, "#FFFFFF", "#5E6367", "three screens", "no new capability"),
    ("03 NILA", "#16283A", "#E9E2D2", "#2F5B78", "indigo dip, undyed line", "the Vault only"),
]

CSS = """
:root{
  --void:#000; --panel:#070707; --rule:#1B1B1B; --rule-hi:#2C2C2C;
  --titanium:#8A8C8E; --white:#fff; --prose:#C4BDB2; --resist:#EDE6D6;
  --mono: ui-monospace,"Cascadia Mono",Consolas,"SFMono-Regular",Menlo,monospace;
  --serif: "Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
}
*{box-sizing:border-box}
html{background:var(--void);color-scheme:dark}
body{margin:0;background:var(--void);color:var(--prose);font-family:var(--serif);
     font-size:16px;line-height:1.7;-webkit-font-smoothing:antialiased}
.wrap{padding:40px 44px 52px;display:flex;flex-direction:column;gap:30px}
.head{display:flex;flex-direction:column;gap:8px;border-bottom:1px solid var(--rule);
      padding-bottom:20px}
.eyebrow{font-family:var(--mono);font-size:10.5px;letter-spacing:.38em;
         text-transform:uppercase;color:var(--titanium)}
.eyebrow b{color:var(--white);font-weight:400}
h1{font-family:var(--mono);font-weight:400;font-size:19px;letter-spacing:.16em;
   text-transform:uppercase;color:var(--white);margin:0;text-wrap:balance}
.note{max-width:70ch;color:var(--titanium);font-size:15px;margin:0}
.row{display:flex;flex-wrap:wrap;gap:34px;align-items:flex-end}
.row.top{align-items:flex-start}
.sw{width:150px}
.cell{display:flex;flex-direction:column;gap:10px}
.cap{font-family:var(--mono);font-size:10px;letter-spacing:.16em;
     text-transform:uppercase;color:var(--titanium)}
.cap b{color:var(--resist);font-weight:400;display:block}
svg{display:block;overflow:visible}
.scroll{overflow-x:auto}
.sw{display:flex;flex-direction:column;gap:9px}
.chip{width:150px;height:76px;border:1px solid var(--rule-hi)}
.hex{font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--white)}
.tok{font-family:var(--mono);font-size:10px;letter-spacing:.14em;color:var(--titanium)}
.desc{font-size:13.5px;color:var(--titanium);max-width:22ch;line-height:1.5}
.rule{border:0;border-top:1px solid var(--rule);margin:0}
"""


def shell(title, eyebrow, heading, note, body, card):
    return (f'<!-- @dsCard group="{card["group"]}" name="{card["name"]}" '
            f'subtitle="{card["subtitle"]}" -->\n'
            f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            f'<title>{title}</title>\n<style>{CSS}</style>\n</head>\n<body>\n'
            f'<div class="wrap">\n  <div class="head">\n'
            f'    <div class="eyebrow">NOUGHT<b>VAULT</b> &nbsp;//&nbsp; {eyebrow}</div>\n'
            f'    <h1>{heading}</h1>\n  </div>\n'
            f'  <p class="note">{note}</p>\n{body}\n</div>\n</body></html>\n')


def cell(label, sub, svg):
    return (f'    <div class="cell">{svg}\n'
            f'      <div class="cap"><b>{label}</b>{sub}</div>\n    </div>')


def svg_(w, h, inner, scale=1.0):
    return (f'<svg viewBox="0 0 {w} {h}" width="{round(w*scale)}" '
            f'height="{round(h*scale)}" role="img">{inner}</svg>')


# ------------------------------------------------------------------- cards --
def card_pucuk_rebung():
    W, H = 110, 144
    specimens = [
        ("Upright", "the shoot · canonical", rebung(51, 68, up=True)),
        ("Inverted", "the keyhole reading", rebung(51, 68)),
        ("Outline only", "no isian · for cap tooling", rebung(51, 68, up=True, noughts=False)),
        ("Single echo", "small scale, under 15 mm", rebung(51, 68, up=True, noughts=False, echoes=(0,))),
    ]
    row = "\n".join(cell(a, b, svg_(W, H, f'<g transform="translate(4,4)">{s}</g>', 1.55))
                    for a, b, s in specimens)
    return shell(
        "Pucuk rebung", "MOTIF · PUCUK REBUNG", "Pucuk rebung",
        "The bamboo shoot — the border motif of the Malay archipelago, and the only "
        "traditional one that is already austere enough for a void-black brand. "
        "25.5 × 68 mm on the 350 mm print. Three nested outlines are the canting "
        "convention; the spine of slashed noughts is ours. Each nought is sized from "
        "the shoot&rsquo;s own half-width at its height, so it can never overflow the outline.",
        f'  <div class="row">\n{row}\n  </div>',
        {"group": "Motifs", "name": "Pucuk rebung",
         "subtitle": "Upright / inverted, with and without isian"})


def card_counter_shoot():
    W, H = 300, 150
    band = "".join(f'<g transform="translate({mm(BASE*k)},0)">'
                   + rebung(BASE, SHOOT, sw=1.4) + '</g>' for k in range(3))
    ctr = "".join(f'<g transform="translate({mm(BASE*(k+0.5))},0)">'
                  + counter(BASE, SHOOT, up=True) + '</g>' for k in range(2))
    specimens = [
        ("Alone", "inset 2.5 mm", svg_(70, 150, f'<g transform="translate(4,2)">'
                                       + counter(BASE, SHOOT, up=True) + '</g>', 1.3)),
        ("Interlocked", "how it actually sits", svg_(W, H, f'<g transform="translate(4,2)">'
                                                    + band + ctr + '</g>', 1.3)),
    ]
    row = "\n".join(cell(a, b, s) for a, b, s in specimens)
    return shell(
        "Counter-shoot", "MOTIF · COUNTER-SHOOT", "The counter-shoot",
        "The negative space between two pucuk rebung, drawn at the true height of the "
        "gap and inset 2.5 mm so a clear band of ground survives on either side. It is "
        "also the tolerance budget: a hand-drawn or cap-stamped band drifts, and the "
        "counter-shoot is sized to absorb ±1 mm of it without the border looking wrong.",
        f'  <div class="row">\n{row}\n  </div>',
        {"group": "Motifs", "name": "Counter-shoot",
         "subtitle": "Negative motif, and the drift budget"})


def card_unification():
    xl, xr, ay = inset_tri(51, 74, 9)
    key = (f'<path d="M{mm(xl)} {mm(9)} L{mm(xr)} {mm(9)} L{mm(25.5)} {mm(ay)} Z" '
           f'fill="{RESIST}"/><circle cx="{mm(25.5)}" cy="{mm(9)}" r="{mm(9.6)}" fill="{RESIST}"/>')
    specimens = [
        ("Pucuk rebung", "ornament, to everyone", svg_(110, 160,
            f'<g transform="translate(4,4)">{rebung(51, 74, up=True)}</g>', 1.5)),
        ("Turned 180°", "nothing else changes", svg_(110, 160,
            f'<g transform="translate(4,4)">{rebung(51, 74, noughts=False)}</g>', 1.5)),
        ("The keyhole", "to one person", svg_(110, 160,
            f'<g transform="translate(4,4)" opacity=".24">'
            f'{rebung(51, 74, noughts=False, echoes=(0,))}</g>'
            f'<g transform="translate(4,4)">{key}</g>', 1.5)),
    ]
    row = "\n".join(cell(a, b, s) for a, b, s in specimens)
    return shell(
        "The unification", "MOTIF · THE UNIFICATION", "One shape, two readings",
        "The load-bearing idea in the whole textile programme. An inverted pucuk rebung "
        "under a circle is the keyhole in the NoughtVault mark — the border motif and "
        "the logo are the same triangle. The solid shaft is that triangle inset 9 mm, "
        "not a lookalike drawn to match. Nothing has to be explained and nothing has to "
        "be hidden, which is the only kind of concealment that survives being looked at.",
        f'  <div class="row">\n{row}\n  </div>',
        {"group": "Motifs", "name": "The unification",
         "subtitle": "Shoot → turn → keyhole"})


def card_mark():
    nought = (f'<ellipse cx="{mm(30)}" cy="{mm(30)}" rx="{mm(15)}" ry="{mm(20.5)}" '
              f'fill="none" stroke="{RESIST}" stroke-width="2.9"/>'
              f'<line x1="{mm(18.5)}" y1="{mm(47)}" x2="{mm(41.5)}" y2="{mm(13)}" '
              f'stroke="{RESIST}" stroke-width="2.9" stroke-linecap="round"/>')
    kx, ky = 16, 12
    keyhole = (f'<circle cx="{mm(kx)}" cy="{mm(ky)}" r="{mm(7.6)}" fill="{RESIST}"/>'
               f'<path d="M{mm(kx-4)} {mm(ky+5.4)} L{mm(kx+4)} {mm(ky+5.4)} '
               f'L{mm(kx)} {mm(ky+24)} Z" fill="{RESIST}"/>')
    specimens = [
        ("The medallion", "96 × 96 mm · badan centre",
         svg_(210, 210, f'<g transform="translate(105,105)">{medallion(0, 0, 1.0)}</g>', 1.35)),
        ("The nought", "the dial, alone",
         svg_(124, 124, f'<g transform="translate(2,2)">{nought}</g>', 1.2)),
        ("The keyhole", "circle over inverted shoot",
         svg_(70, 84, f'<g transform="translate(2,2)">{keyhole}</g>', 1.2)),
    ]
    row = "\n".join(cell(a, b, s) for a, b, s in specimens)
    return shell(
        "The mark", "BRAND · THE MARK", "The mark, in batik language",
        "The vault door redrawn for wax: a rounded double frame, two solid hinge blocks, "
        "the slashed nought standing in for the dial, and the keyhole to its right. The "
        "hinges are the only filled mass on the cloth, which gives the eye somewhere to "
        "land in a design that is otherwise all contour. Supply this to the shop as line "
        "art at final size — batik shops improvise beautifully, and this is the one "
        "element that must not be improvised. Omitted entirely on the RAKING colourway.",
        f'  <div class="row">\n{row}\n  </div>',
        {"group": "Brand", "name": "The mark",
         "subtitle": "Medallion, nought, keyhole"})


def card_kepala_band():
    band = "".join(f'<g transform="translate({mm(BASE*k)},{mm(PLINTH)})">'
                   + rebung(BASE, SHOOT) + '</g>' for k in range(N))
    ctr = "".join(f'<g transform="translate({mm(BASE*(k+0.5))},{mm(PLINTH)})">'
                  + counter(BASE, SHOOT, up=True) + '</g>' for k in range(N - 1))
    plinth = (cecek_row(0, INNER, PLINTH / 2, 61)
              + f'<line x1="0" y1="{mm(PLINTH)}" x2="{mm(INNER)}" y2="{mm(PLINTH)}" '
                f'stroke="{RESIST}" stroke-width="1.1" opacity=".55"/>')
    inner = f'<g transform="translate(4,4)">{plinth}{band}{ctr}</g>'
    return shell(
        "Kepala band", "PATTERN · KEPALA BAND", "The kepala band",
        f"Twelve pucuk rebung across {INNER} mm — one band. The print carries two, "
        f"facing each other across the badan, so the border counts to twenty-four: one "
        f"per word of a 24-word recovery phrase. It counts to 24; it does not store 24, "
        f"and no copy may ever imply otherwise. Band depth {KEPALA} mm including an "
        f"{PLINTH} mm plinth of 61 cecek.",
        f'  <div class="scroll">{svg_(mm(INNER)+8, mm(KEPALA)+10, inner, 1.0)}</div>\n'
        f'  <div class="cap"><b>12 shoots · {BASE} mm each</b>apexes point into the field</div>',
        {"group": "Patterns", "name": "Kepala band",
         "subtitle": "12 shoots, 306 mm — two bands make 24"})


def card_tepi():
    L = 300
    a, b = 0, 24
    o = [f'<rect x="0" y="0" width="{mm(L)}" height="{mm(b)}" fill="none" '
         f'stroke="{RESIST}" stroke-width="1.7"/>',
         f'<rect x="{mm(TEPI)}" y="{mm(TEPI)}" width="{mm(L-2*TEPI)}" '
         f'height="{mm(b-2*TEPI)}" fill="none" stroke="{RESIST}" stroke-width="1.7"/>']
    for k in range(26):
        t = TEPI + (L - 2 * TEPI) * (k + 0.5) / 26
        o.append(f'<circle cx="{mm(t)}" cy="{mm(TEPI/2)}" r="{mm(0.85)}" fill="{RESIST}"/>')
    inner = f'<g transform="translate(4,4)">{"".join(o)}</g>'
    return shell(
        "Tepi", "PATTERN · TEPI", "The tepi",
        f"The {TEPI} mm ruled border, inside a {HEM} mm plain hem. It carries 26 cecek a "
        f"side — one per punch in the DC53 alphabet. Like the 24 shoots, it is ornament "
        f"that happens to count: it costs one instruction to the shop, it is never "
        f"mentioned in a listing, and it is the detail that makes the object read as "
        f"designed rather than sourced.",
        f'  <div class="scroll">{svg_(mm(L)+8, mm(b)+10, inner, 1.0)}</div>\n'
        f'  <div class="cap"><b>26 cecek a side</b>shown at 300 mm of a 306 mm run</div>',
        {"group": "Patterns", "name": "Tepi",
         "subtitle": "Ruled border, 26 cecek a side"})


def card_kepala_24():
    inner = f'<g transform="translate(6,6)">{square()}</g>'
    return shell(
        "Print 000 · Kepala 24", "PRINT 000 · KEPALA 24", "Print 000 — Kepala 24",
        f"{SQ} × {SQ} mm finished from a 355 mm cut with a 2.5 mm rolled hem — the "
        f"vendor&rsquo;s stock napkin, unmodified. A sarong compressed into a square: two "
        f"kepala bands facing each other across a plain badan, framed by a ruled tepi, "
        f"with the mark alone in the field. Hand-drawn for Batch 001; copper cap tooling "
        f"does not amortise below roughly 250 pieces.",
        f'  <div class="scroll">{svg_(mm(SQ)+12, mm(SQ)+12, inner, 0.86)}</div>',
        {"group": "Prints", "name": "Print 000 · Kepala 24",
         "subtitle": "The 350 mm square, complete"})


def card_colourways():
    T = 214
    cells = []
    for name, g, line, mid, n1, n2 in COLOURWAYS:
        cid = name.split()[0]
        svg = (f'<svg viewBox="0 0 {T} {T}" width="{T}" height="{T}" role="img">'
               f'<defs><clipPath id="c{cid}"><rect width="{T}" height="{T}"/></clipPath></defs>'
               f'<g clip-path="url(#c{cid})"><rect width="{T}" height="{T}" fill="{g}"/>'
               f'<g transform="translate({-mm(HEM)+6},{-mm(HEM)+6})">'
               f'{square(res=line, ground=g, fill=mid, medal=False)}</g></g>'
               f'<rect width="{T}" height="{T}" fill="none" stroke="#2C2C2C"/></svg>')
        cells.append(cell(name, f"{n1}<br>{n2}", svg))
    return shell(
        "Colourways", "PRINT 000 · COLOURWAYS", "Four ways to dye one drawing",
        "True crops of the same corner. TITANIUM needs no new vendor capability — it is "
        "the black, grey and white sample already in hand, three screens the shop runs "
        "every day. RAKING is shown exaggerated: on cloth the difference is sheen rather "
        "than value, and it dies in flat light, which is why it is held back from a batch "
        "that still needs photographs.",
        '  <div class="row">\n' + "\n".join(cells) + '\n  </div>',
        {"group": "Prints", "name": "Colourways",
         "subtitle": "VOID / RAKING / TITANIUM / NILA"})


def card_colour():
    sw = []
    for tok, hexv, desc in TOKENS:
        border = ";border-color:#2C2C2C" if hexv in (VOID, "#070707") else ""
        sw.append(f'    <div class="sw"><div class="chip" style="background:{hexv}{border}">'
                  f'</div><div class="hex">{hexv}</div><div class="tok">{tok}</div>'
                  f'<div class="desc">{desc}</div></div>')
    return shell(
        "Colour", "FOUNDATIONS · COLOUR", "Colour",
        "The house is void-black and single-theme by commitment, in every document. What "
        "changes per document is the accent, and for the textile it is raw undyed cotton "
        "— because in a resist process the accent is the absence of dye. Wax is laid so "
        "the dye cannot reach what is underneath, and what you see is the negative of "
        "what was protected. Semantic colours are kept strictly separate from the accent.",
        '  <div class="row top">\n' + "\n".join(sw) + '\n  </div>',
        {"group": "Foundations", "name": "Colour",
         "subtitle": "Void ground, undyed accent, 7 tokens"})


def card_type():
    rows = [
        ("Masthead", "mono · clamp(27–42px) / .02em", 'font-family:var(--mono);font-size:34px;color:#fff;letter-spacing:.02em;line-height:1.14',
         "The oldest border motif is a keyhole upside down."),
        ("Section", "mono · 15px / .24em / caps", 'font-family:var(--mono);font-size:15px;color:#fff;letter-spacing:.24em;text-transform:uppercase',
         "The motif, and the turn"),
        ("Eyebrow", "mono · 10.5px / .42em / caps", 'font-family:var(--mono);font-size:10.5px;color:var(--titanium);letter-spacing:.42em;text-transform:uppercase',
         "Textile 000 · the batik prints"),
        ("Prose", "serif · 17px / 1.72 / 68ch", 'font-family:var(--serif);font-size:17px;color:var(--prose);line-height:1.72;max-width:68ch',
         "Batik is a resist process: hot wax laid down so the dye cannot reach what is "
         "underneath, and what you see is the negative of what was protected."),
        ("Caption", "mono · 11px / .06em", 'font-family:var(--mono);font-size:11px;color:var(--titanium);letter-spacing:.06em',
         "350 × 350 mm finished · print 000 · kepala 24"),
    ]
    body = []
    for name, spec, style, sample in rows:
        body.append(f'  <div class="cell" style="gap:6px">'
                    f'<div class="cap"><b>{name}</b>{spec}</div>'
                    f'<div style="{style}">{sample}</div><hr class="rule"></div>')
    return shell(
        "Type", "FOUNDATIONS · TYPE", "Type",
        "Two faces doing opposite jobs. A monospace carries every piece of structural "
        "chrome — mastheads, section labels, captions, dimensions, tables — so anything "
        "that is machinery looks like machinery. A Palatino-class serif carries the "
        "prose, warm against the cold accent. No webfonts anywhere: the pages are read "
        "behind a strict CSP, and a silent fallback would be worse than a system stack "
        "chosen on purpose.",
        "\n".join(body),
        {"group": "Foundations", "name": "Type",
         "subtitle": "Mono chrome, serif prose, 5 roles"})


def card_wrap():
    GHOST, FLAP, LINE = "#262626", "#151515", RESIST
    panels = []
    steps = [("01 — LAY", "plate face-down, centred"),
             ("02 — NEAR CORNER", "up, and over the plate"),
             ("03 — SIDES IN", "left, then right"),
             ("04 — ROLL", "to the far corner; tuck")]
    for i, (t, s) in enumerate(steps):
        o = [f'<path d="M84 4 L164 84 L84 164 L4 84 Z" fill="none" stroke="{GHOST}" '
             f'stroke-width="1.1" stroke-dasharray="3 4"/>']
        if i == 0:
            o.append(f'<rect x="57" y="63" width="54" height="42" fill="none" '
                     f'stroke="{LINE}" stroke-width="1.5"/>')
        if i == 1:
            o.append(f'<path d="M4 84 L84 4 L164 84 L136 112 L32 112 Z" fill="none" '
                     f'stroke="{LINE}" stroke-width="1.4" stroke-linejoin="round"/>')
            o.append(f'<path d="M32 112 L136 112 L84 60 Z" fill="{FLAP}" stroke="{LINE}" '
                     f'stroke-width="1.4" stroke-linejoin="round"/>')
        if i == 2:
            o.append(f'<path d="M36 52 L84 4 L132 52 L132 112 L36 112 Z" fill="none" '
                     f'stroke="{LINE}" stroke-width="1.4" stroke-linejoin="round"/>')
            o.append(f'<path d="M36 112 L132 112 L84 64 Z" fill="{FLAP}" stroke="{LINE}" '
                     f'stroke-width="1.2" stroke-linejoin="round"/>')
            for pts in ("M36 54 L36 110 L66 82 Z", "M132 54 L132 110 L102 82 Z"):
                o.append(f'<path d="{pts}" fill="{FLAP}" stroke="{LINE}" '
                         f'stroke-width="1.4" stroke-linejoin="round"/>')
        if i == 3:
            o.append(f'<rect x="36" y="48" width="96" height="80" fill="{FLAP}" '
                     f'stroke="{LINE}" stroke-width="1.7"/>')
            o.append(f'<path d="M60 48 L108 48 L84 80 Z" fill="{LINE}"/>')
            o.append(f'<line x1="36" y1="88" x2="132" y2="88" stroke="{LINE}" '
                     f'stroke-width="1" opacity=".45"/>')
        panels.append(cell(t, s, svg_(168, 168, "".join(o), 1.15)))
    return shell(
        "The wrap", "PACKAGING · THE WRAP", "The wrap",
        "A furoshiki fold sized to the 90 × 70 mm plate, finishing at roughly "
        "110 × 95 mm — flat enough for the letter tier, and closed by nothing but its own "
        "last corner. The absence of a fastening is the design: there is no moment where "
        "the customer looks for scissors. Do not close it with a VOID seal — transfer is "
        "already unreliable on titanium and will not happen at all on woven cotton, and a "
        "seal that visibly fails on the wrapper teaches the customer it is decorative "
        "minutes before they use one on the plate.",
        '  <div class="row">\n' + "\n".join(panels) + '\n  </div>',
        {"group": "Packaging", "name": "The wrap",
         "subtitle": "Four folds and a tuck, no fastening"})


CARDS = {
    "foundations/colour.html": card_colour,
    "foundations/type.html": card_type,
    "brand/mark.html": card_mark,
    "motifs/pucuk-rebung.html": card_pucuk_rebung,
    "motifs/counter-shoot.html": card_counter_shoot,
    "motifs/unification.html": card_unification,
    "patterns/kepala-band.html": card_kepala_band,
    "patterns/tepi.html": card_tepi,
    "prints/kepala-24.html": card_kepala_24,
    "prints/colourways.html": card_colourways,
    "packaging/wrap-fold.html": card_wrap,
}

README = """# NoughtVault — Batik (Textile 000)

Design-system bundle for the NoughtVault batik programme, generated from
`tools/batik.py` — the same geometry that draws the figures in
`textile-000-batik.html`, so the system and the specification cannot drift.

Every preview is standalone and self-contained: no external CSS, no webfonts,
no scripts. Each carries a first-line `@dsCard` marker, so the Design System
pane builds its card index without explicit asset registration.

| Group | Card | What it fixes |
| --- | --- | --- |
| Foundations | Colour | Void ground; the accent is undyed cotton, not a hue |
| Foundations | Type | Mono for chrome, serif for prose, no webfonts |
| Brand | The mark | The vault door in wax; supply as line art, never improvised |
| Motifs | Pucuk rebung | The shoot, 25.5 × 68 mm, and its isian |
| Motifs | Counter-shoot | The negative motif, and the ±1 mm drift budget |
| Motifs | The unification | Shoot → turn → keyhole; the load-bearing idea |
| Patterns | Kepala band | 12 shoots per band, 24 per print |
| Patterns | Tepi | Ruled border, 26 cecek a side |
| Prints | Print 000 · Kepala 24 | The complete 350 mm square |
| Prints | Colourways | VOID / RAKING / TITANIUM / NILA |
| Packaging | The wrap | Four folds and a tuck, no fastening |

## Rules that travel with the artwork

- Never in the listing, never in What's Included, never in an alt tag. The
  square is a surprise, and a surprise that gets listed stops being one.
- The cloth counts to 24. It does not store 24, and no copy may imply it does.
- Only wax-resist work may be called batik. A screen-printed square is a
  batik-*motif* print and the copy has to say so.
- The vendor brief reads `napkin batik 14 × 14, corak tempahan` and nothing
  else. No brand name in artwork filenames.

Regenerate with `cd tools && python3 design-export.py`.
"""


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    for path, fn in CARDS.items():
        full = os.path.join(OUT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(fn())
    with open(os.path.join(OUT, "README.md"), "w", encoding="utf-8") as f:
        f.write(README)
    print(f"wrote {len(CARDS) + 1} files to dist/design-system/")
    for p in sorted(CARDS):
        print("  ", p)


if __name__ == "__main__":
    main()
