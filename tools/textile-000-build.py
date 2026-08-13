#!/usr/bin/env python3
"""Render textile-000-batik.html from its template and the batik geometry."""
from batik import *  # noqa: F401,F403

def fig_unification():
    o = ['<svg viewBox="0 0 780 348" role="img" aria-label="The same isosceles '
         'triangle read twice. Upright, filled with a column of slashed noughts, it '
         'is the pucuk rebung, the bamboo-shoot border motif of the Malay '
         'archipelago. Rotated a half turn and set beneath a circle, the identical '
         'triangle becomes the shaft of a keyhole in the NoughtVault mark.">']

    o.append(txt(26, 30, "01 — PUCUK REBUNG", "#EDE6D6", 11, 1.9))
    o.append('<g transform="translate(62,62)">' + rebung(51, 74, up=True) + '</g>')
    for i, s in enumerate(("the bamboo shoot: the", "oldest border motif in",
                           "the archipelago, and the", "one that is already austere")):
        o.append(txt(26, 258 + i * 17, s))

    o.append(txt(288, 30, "02 — THE TURN", "#EDE6D6", 11, 1.9))
    o.append('<g transform="translate(324,62)">' + rebung(51, 74, noughts=False) + '</g>')
    o.append('<path d="M296 116 A 40 40 0 0 1 296 196" fill="none" stroke="#EDE6D6" '
             'stroke-width="1.2" stroke-dasharray="4 4"/>')
    o.append('<path d="M292 190 L296 200 L302 191 Z" fill="#EDE6D6"/>')
    for i, s in enumerate(("180°. Nothing else about", "the drawing changes — the",
                           "motif already contains", "its own second meaning")):
        o.append(txt(288, 258 + i * 17, s))

    o.append(txt(550, 30, "03 — THE KEYHOLE", "#EDE6D6", 11, 1.9))
    # the ghost is the turned shoot from panel 02; the solid shaft is that same
    # triangle inset 9 mm, so the keyhole is not a lookalike — it is the motif.
    o.append('<g transform="translate(586,62)" opacity=".24">'
             + rebung(51, 74, noughts=False, echoes=(0,)) + '</g>')
    xl, xr, ay = inset_tri(51, 74, 9)          # wide end at the top, tapering down
    ox, oy = 586, 62
    o.append(f'<path d="M{ox+mm(xl)} {oy+mm(9)} L{ox+mm(xr)} {oy+mm(9)} '
             f'L{ox+mm(25.5)} {oy+mm(ay)} Z" fill="#EDE6D6"/>')
    o.append(f'<circle cx="{ox+mm(25.5)}" cy="{oy+mm(9)}" r="{mm(9.6)}" fill="#EDE6D6"/>')
    for i, s in enumerate(("a circle over an inverted", "shoot. The border reads as",
                           "ornament to everyone, and", "as a keyhole to one person")):
        o.append(txt(550, 258 + i * 17, s, "#EDE6D6" if i == 3 else "#8A8C8E"))

    o.append('<line x1="26" y1="316" x2="754" y2="316" stroke="#1B1B1B"/>')
    o.append(txt(26, 338, "ONE SHAPE · TWO READINGS · NOTHING TO EXPLAIN AND NOTHING TO HIDE"))
    o.append('</svg>')
    return "\n".join(o)


def fig_square():
    w, pad = SQ * U, 26
    o = [f'<svg viewBox="0 0 {w+374} {w+2*pad+34}" role="img" aria-label="The '
         f'complete 350 millimetre batik square. A plain hem, a ruled tepi border '
         f'carrying 26 dots a side, then two kepala bands of twelve pucuk rebung '
         f'each — 24 in total, one per word of a 24-word recovery phrase — framing a '
         f'plain badan field with the slashed-nought vault medallion at its centre.">']
    o.append(txt(pad, 20, "350 × 350 mm FINISHED · PRINT 000 · KEPALA 24"))
    o.append(f'<g transform="translate({pad},{pad+18})">' + square() + '</g>')

    # elbow leaders: anchor on the cloth, label parked at a legible spacing
    gx, lx = w + pad + 30, w + pad + 66
    rows = [
        (HEM / 2, 44, "HEM", "14 mm · rolled and hand-stitched"),
        (HEM + TEPI / 2, 116, "TEPI", "8 mm · 26 cecek a side"),
        (HEM + TEPI + KEPALA / 2, 250, "KEPALA", "76 mm · 12 shoots, pointing in"),
        (SQ / 2, 400, "BADAN", "154 mm · void, and one mark"),
        (SQ - HEM - TEPI - KEPALA / 2, 560, "KEPALA", "76 mm · 12 more — 24 in all"),
    ]
    for at, ly, name, note in rows:
        ay = pad + 18 + mm(at)
        o.append(f'<path d="M{w+pad+6} {ay} L{gx} {ay} L{gx} {ly} L{lx-8} {ly}" '
                 f'fill="none" stroke="#2C2C2C" stroke-width="1"/>')
        o.append(txt(lx, ly - 3, name, "#EDE6D6"))
        o.append(txt(lx, ly + 14, note))
    o.append('</svg>')
    return "\n".join(o)


def fig_detail():
    o = ['<svg viewBox="0 0 780 452" role="img" aria-label="One pucuk rebung '
         'enlarged four times with its parts named: three nested resist outlines, a '
         'spine of three slashed noughts diminishing toward the apex, a terminal dot '
         'closing the shoot, and a row of cecek along the plinth beneath it.">']
    o.append(txt(26, 26, "ONE SHOOT AT 4:1 · 25.5 × 68 mm ACTUAL"))
    o.append('<g transform="translate(104,58) scale(2.05)">'
             + rebung(51, 68, up=True) + '</g>')
    o.append('<g transform="translate(104,338) scale(2.05)">'
             + cecek_row(0, 51, 0, 11) + '</g>')
    o.append(f'<line x1="104" y1="330" x2="313" y2="330" stroke="#EDE6D6" '
             f'stroke-width="1.1" opacity=".55"/>')

    ann = [   # callouts run apex-to-base, in the order the motif is drawn
        ("THREE ECHOES", "outline, +3 mm, +6 mm — the canting draws", 372, 104, 222, 104),
        ("TERMINAL CECEK", "a single dot closes the shoot", 372, 180, 213, 160),
        ("THE NOUGHT COLUMN", "three slashed ovals, each sized to its own", 372, 256, 272, 256),
        ("PLINTH", "61 cecek run the width of the band", 372, 344, 316, 340),
    ]
    sub2 = {0: "the contour, then echoes it twice",
            1: "", 2: "height, so it can never overflow", 3: ""}
    for i, (t, s, tx, ty, lx_, ly_) in enumerate(ann):
        o.append(f'<line x1="{lx_}" y1="{ly_}" x2="{tx-14}" y2="{ty-4}" stroke="#2C2C2C"/>')
        o.append(txt(tx, ty, t, "#EDE6D6"))
        o.append(txt(tx, ty + 16, s))
        if sub2[i]:
            o.append(txt(tx, ty + 32, sub2[i]))
    o.append('</svg>')
    return "\n".join(o)


def fig_medallion():
    o = ['<svg viewBox="0 0 780 412" role="img" aria-label="The NoughtVault mark '
         'redrawn as a batik medallion: a rounded double frame for the door, two '
         'solid hinge blocks on the left, the slashed nought standing in for the '
         'dial, and to its right a keyhole whose shaft is an inverted pucuk rebung.">']
    o.append(txt(26, 26, "THE MEDALLION AT 1.6:1 · 96 × 96 mm ACTUAL"))
    o.append('<g transform="translate(232,196) scale(1.56)">'
             + medallion(0, 0, 1.0, sw=2.3) + '</g>')
    ann = [("THE DOOR", "a double frame, 96 and 78 mm", 458, 108),
           ("THE DIAL", "an upright nought, struck through", 458, 174),
           ("THE HINGES", "the only filled mass on the cloth", 458, 240),
           ("THE KEYHOLE", "a circle over an inverted shoot —", 458, 306)]
    for t, s, tx, ty in ann:
        o.append(txt(tx, ty, t, "#EDE6D6"))
        o.append(txt(tx, ty + 16, s))
    o.append(txt(458, 338, "the same block, turned over", "#EDE6D6"))
    o.append('<line x1="26" y1="376" x2="754" y2="376" stroke="#1B1B1B"/>')
    o.append(txt(26, 398, "CENTRED IN THE BADAN · OMITTED ENTIRELY ON THE RAKING COLOURWAY"))
    o.append('</svg>')
    return "\n".join(o)


def fig_colourways():
    """True crops — the same drawing, four dye recipes, clipped to one corner."""
    ways = [
        ("00 VOID", VOID, "#EDE6D6", None, ["black ground, undyed line", "the house · Batch 001"]),
        ("01 RAKING", VOID, "#191919", None, ["black wax on black ground", "§ 11's idea, built"]),
        ("02 TITANIUM", VOID, "#FFFFFF", "#5E6367", ["three screens", "no new capability"]),
        ("03 NILA", "#16283A", "#E9E2D2", "#2F5B78", ["indigo dip, undyed line", "the Vault only"]),
    ]
    T, PITCH = 206, 234
    o = [f'<svg viewBox="0 0 {20+PITCH*4} 336" role="img" aria-label="Four '
         f'colourways shown as true crops of the same corner of the print: VOID in '
         f'undyed line on black, RAKING in black wax on black shown exaggerated, '
         f'TITANIUM adding a grey mid-tone inside each shoot, and NILA on an indigo '
         f'ground.">', '<defs>']
    for i in range(4):
        o.append(f'<clipPath id="cw{i}"><rect x="0" y="0" width="{T}" height="{T}"/></clipPath>')
    o.append('</defs>')

    for i, (name, g, line, mid, notes) in enumerate(ways):
        x = 20 + i * PITCH
        o.append(f'<g transform="translate({x},20)">')
        o.append(f'<g clip-path="url(#cw{i})">')
        o.append(f'<rect x="0" y="0" width="{T}" height="{T}" fill="{g}"/>')
        o.append(f'<g transform="translate({-mm(HEM)+6},{-mm(HEM)+6})">'
                 + square(res=line, ground=g, fill=mid, medal=False) + '</g>')
        o.append('</g>')
        o.append(f'<rect x="0" y="0" width="{T}" height="{T}" fill="none" '
                 f'stroke="#2C2C2C" stroke-width="1"/>')
        o.append('</g>')
        o.append(txt(x, 252, name, "#EDE6D6", 10.5, 1.5))
        for j, s in enumerate(notes):
            o.append(txt(x, 270 + j * 16, s, size=10, ls=1.3))
    o.append(f'<line x1="20" y1="306" x2="{20+PITCH*3+T}" y2="306" stroke="#1B1B1B"/>')
    o.append(txt(20, 328, "RAKING IS SHOWN EXAGGERATED — ON CLOTH THE DIFFERENCE IS "
                          "SHEEN, NOT VALUE, AND IT DIES IN FLAT LIGHT", size=10, ls=1.4))
    o.append('</svg>')
    return "\n".join(o)


def fig_fold():
    o = ['<svg viewBox="0 0 780 316" role="img" aria-label="The four-fold wrap: the '
         'square laid as a diamond with the plate centred face-down, the near corner '
         'folded up over it, the left and right corners folded in, and the parcel '
         'rolled to the far corner, finishing as a flat pouch closed by a single '
         'tuck with no tape or fastening.">']
    steps = [("01 — LAY", "plate face-down, centred"),
             ("02 — NEAR CORNER", "up, and over the plate"),
             ("03 — SIDES IN", "left, then right"),
             ("04 — ROLL", "to the far corner; tuck")]
    GHOST, FLAP, LINE = "#262626", "#151515", "#EDE6D6"
    for i, (t, s) in enumerate(steps):
        x = 20 + i * 190
        o.append(txt(x, 26, t, "#EDE6D6", 10, 1.5))
        o.append(f'<g transform="translate({x},40)">')
        # the original square, kept as a ghost so the parcel visibly shrinks
        o.append(f'<path d="M84 4 L164 84 L84 164 L4 84 Z" fill="none" '
                 f'stroke="{GHOST}" stroke-width="1.1" stroke-dasharray="3 4"/>')

        if i == 0:
            o.append(f'<rect x="57" y="63" width="54" height="42" fill="none" '
                     f'stroke="{LINE}" stroke-width="1.5"/>')
            o.append(txt(84, 88, "90 × 70", "#8A8C8E", 9.5, 1.2, "middle"))

        if i == 1:      # the near corner comes up over the plate
            o.append(f'<path d="M4 84 L84 4 L164 84 L136 112 L32 112 Z" fill="none" '
                     f'stroke="{LINE}" stroke-width="1.4" stroke-linejoin="round"/>')
            o.append(f'<path d="M32 112 L136 112 L84 60 Z" fill="{FLAP}" '
                     f'stroke="{LINE}" stroke-width="1.4" stroke-linejoin="round"/>')
            o.append(f'<line x1="84" y1="150" x2="84" y2="122" stroke="{LINE}" stroke-width="1"/>')
            o.append(f'<path d="M84 116 L79 128 L89 128 Z" fill="{LINE}"/>')

        if i == 2:      # then the two side corners
            o.append(f'<path d="M36 52 L84 4 L132 52 L132 112 L36 112 Z" fill="none" '
                     f'stroke="{LINE}" stroke-width="1.4" stroke-linejoin="round"/>')
            o.append(f'<path d="M36 112 L132 112 L84 64 Z" fill="{FLAP}" '
                     f'stroke="{LINE}" stroke-width="1.2" stroke-linejoin="round"/>')
            for pts in ("M36 54 L36 110 L66 82 Z", "M132 54 L132 110 L102 82 Z"):
                o.append(f'<path d="{pts}" fill="{FLAP}" stroke="{LINE}" '
                         f'stroke-width="1.4" stroke-linejoin="round"/>')

        if i == 3:      # rolled to the far corner and tucked
            o.append(f'<rect x="36" y="48" width="96" height="80" fill="{FLAP}" '
                     f'stroke="{LINE}" stroke-width="1.7"/>')
            o.append(f'<path d="M60 48 L108 48 L84 80 Z" fill="{LINE}"/>')
            o.append(f'<line x1="36" y1="88" x2="132" y2="88" stroke="{LINE}" '
                     f'stroke-width="1" opacity=".45"/>')
            o.append(txt(84, 152, "110 × 95 mm", "#8A8C8E", 9.5, 1.2, "middle"))
        o.append('</g>')
        o.append(txt(x, 240, s, size=10, ls=1.4))
    o.append('<line x1="20" y1="266" x2="760" y2="266" stroke="#1B1B1B"/>')
    o.append(txt(20, 288, "NO TAPE · NO RIBBON · NO INSTRUCTION CARD — THE LAST TUCK "
                          "IS THE ONLY THING HOLDING IT", size=10, ls=1.4))
    o.append(txt(20, 306, "UNDOING IT IS THE FIRST THING THE CUSTOMER DOES, AND IT "
                          "TAKES ONE SECOND", size=10, ls=1.4))
    o.append('</svg>')
    return "\n".join(o)


FIGS = {"UNIFICATION": fig_unification(), "SQUARE": fig_square(),
        "DETAIL": fig_detail(), "MEDALLION": fig_medallion(),
        "COLOURWAYS": fig_colourways(), "FOLD": fig_fold()}

with open("textile-000-batik.template.html", encoding="utf-8") as f:
    doc = f.read()
for k, v in FIGS.items():
    doc = doc.replace("{{" + k + "}}", v)
assert "{{" not in doc, doc[doc.index("{{"):doc.index("{{") + 60]
with open("textile-000-batik.html", "w", encoding="utf-8") as f:
    f.write(doc)
print("wrote textile-000-batik.html", len(doc), "bytes")
