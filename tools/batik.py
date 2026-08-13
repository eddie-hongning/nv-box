"""Batik motif geometry for the NoughtVault textile prints.

Shared by textile-000-build.py (the specification document) and
design-export.py (the Claude Design bundle). Authored at 2 SVG units per
millimetre, so every emitted drawing is dimensionally true to the cloth.

Nothing is eyeballed: the nested resist outlines and the noughts that sit
inside them are both derived from the same triangle-inset solve, so a motif
can never overflow its own edge when a dimension changes.
"""
import math

U = 2.0                                  # units per mm
SQ = 350                                 # finished square, mm
HEM, TEPI, KEPALA = 14, 8, 76
BADAN = SQ - 2 * (HEM + TEPI + KEPALA)
assert BADAN == 154, BADAN

INNER = SQ - 2 * (HEM + TEPI)            # 306 mm
N = 12                                    # pucuk rebung per kepala band
BASE = INNER / N                          # 25.5 mm
SHOOT = 68                                # mm, triangle height
PLINTH = KEPALA - SHOOT                   # 8 mm

VOID, RESIST = "#000000", "#EDE6D6"
MONO = 'font-family="ui-monospace,monospace"'


def mm(v):
    return round(v * U, 2)


def inset_tri(b, h, d):
    """Inward offset of an isosceles triangle. Returns (x_left, x_right, apex_y)."""
    L = math.hypot(b / 2, h)
    nx, ny = h / L, -(b / 2) / L
    ax, ay = d * nx, d * ny
    dx, dy = (b / 2) / L, h / L
    t = ((b / 2) - ax) / dx
    apex_y = ay + t * dy
    t2 = (d - ay) / dy
    return ax + t2 * dx, b - (ax + t2 * dx), apex_y


# ---------------------------------------------------------------- the motif --
def rebung(b, h, res=RESIST, sw=1.6, up=False, noughts=True,
           echoes=(0, 3, 6), fill=None):
    """One pucuk rebung. Base spans x = 0..b; apex at y = h (or y = 0 if up).

    Every nought is sized from the half-width of the innermost outline at its
    own height, so the column physically cannot escape the triangle.
    """
    def Y(v):
        return h - v if up else v

    o = []
    for i, d in enumerate(echoes):
        xl, xr, ay = inset_tri(b, h, d)
        f = fill if (fill and i == len(echoes) - 1) else "none"
        o.append(
            f'<path d="M{mm(xl)} {mm(Y(d))} L{mm(xr)} {mm(Y(d))} '
            f'L{mm(b/2)} {mm(Y(ay))} Z" fill="{f}" stroke="{res}" '
            f'stroke-width="{sw:.2f}" stroke-linejoin="round"/>'
        )
    if not noughts:
        return "\n".join(o)

    # The column is stacked from the base upward in weights 3 : 2 : 1.2, so the
    # noughts diminish toward the apex. Each radius is then clipped to whichever
    # is tighter — the room left above the base, or the shoot's own half-width
    # at that height — which is what stops a nought crossing its own outline.
    d = echoes[-1]
    xl, xr, ay = inset_tri(b, h, d)
    half, span = (xr - xl) / 2, ay - d
    weights = (3.0, 2.0, 1.2)
    gap = 0.03 * span
    avail = 0.68 * span
    cursor = d + 0.06 * span
    for w in weights:
        ry = avail * w / sum(weights) / 2
        cy = cursor + ry
        hw = half * (ay - cy) / span               # half-width of the shoot here
        rx = min(ry * 0.72, hw * 0.80)
        o.append(
            f'<ellipse cx="{mm(b/2)}" cy="{mm(Y(cy))}" rx="{mm(rx)}" ry="{mm(ry)}" '
            f'fill="none" stroke="{res}" stroke-width="{sw*0.72:.2f}"/>'
        )
        o.append(                                  # the slash, lower-left → upper-right
            f'<line x1="{mm(b/2-rx*1.05)}" y1="{mm(Y(cy))+mm(ry*0.95)}" '
            f'x2="{mm(b/2+rx*1.05)}" y2="{mm(Y(cy))-mm(ry*0.95)}" stroke="{res}" '
            f'stroke-width="{sw*0.72:.2f}" stroke-linecap="round"/>'
        )
        cursor = cy + ry + gap
    cy = min(cursor + 0.04 * span, d + span * 0.93)
    o.append(f'<circle cx="{mm(b/2)}" cy="{mm(Y(cy))}" '
             f'r="{mm(min(half*(ay-cy)/span*0.55, 0.02*span+0.4))}" fill="{res}"/>')
    return "\n".join(o)


def counter(b, h, res=RESIST, sw=1.2, up=False, inset=2.5):
    """The negative shoot between two rebung: apex at the band edge, opening in.

    Drawn at the true height of the gap and inset, so it nests inside the
    negative space with a clear ground gap instead of crossing its neighbours.
    """
    def Y(v):
        return h - v if up else v

    xl, xr, ay = inset_tri(b, h, inset)
    return (f'<path d="M{mm(b/2)} {mm(Y(ay))} L{mm(xl)} {mm(Y(inset))} '
            f'L{mm(xr)} {mm(Y(inset))} Z" fill="none" stroke="{res}" '
            f'stroke-width="{sw:.2f}" stroke-linejoin="round" opacity=".5"/>')


def cecek_row(x0, x1, y, n, res=RESIST, r=0.55):
    step = (x1 - x0) / n
    return "\n".join(
        f'<circle cx="{mm(x0+step*(i+0.5))}" cy="{mm(y)}" r="{mm(r)}" fill="{res}"/>'
        for i in range(n))


def medallion(cx, cy, s=1.0, res=RESIST, sw=1.9):
    """The vault door in batik language. s scales about (cx, cy). mm."""
    o = []

    def R(w, h, r, k, op=1.0):
        o.append(f'<rect x="{mm(cx-w/2*s)}" y="{mm(cy-h/2*s)}" width="{mm(w*s)}" '
                 f'height="{mm(h*s)}" rx="{mm(r*s)}" fill="none" stroke="{res}" '
                 f'stroke-width="{sw*k:.2f}" opacity="{op}"/>')

    R(96, 96, 14, 1.0)
    R(78, 78, 10, 0.72)
    R(70, 70, 8, 0.40, 0.5)

    for dy in (-19, 19):                                   # hinges
        o.append(f'<rect x="{mm(cx-53*s)}" y="{mm(cy+(dy-6.5)*s)}" '
                 f'width="{mm(11*s)}" height="{mm(13*s)}" rx="{mm(1.5*s)}" fill="{res}"/>')

    o.append(f'<ellipse cx="{mm(cx-11*s)}" cy="{mm(cy)}" rx="{mm(15*s)}" '
             f'ry="{mm(20.5*s)}" fill="none" stroke="{res}" stroke-width="{sw*1.5:.2f}"/>')
    o.append(f'<line x1="{mm(cx-22.5*s)}" y1="{mm(cy+17*s)}" x2="{mm(cx+0.5*s)}" '
             f'y2="{mm(cy-17*s)}" stroke="{res}" stroke-width="{sw*1.5:.2f}" '
             f'stroke-linecap="round"/>')

    # the keyhole: a circle over an inverted pucuk rebung. The circle is wider
    # than the shaft's shoulder, which is what separates a keyhole from a cone.
    kx, ky = cx + 22 * s, cy - 8 * s
    o.append(f'<circle cx="{mm(kx)}" cy="{mm(ky)}" r="{mm(7.6*s)}" fill="{res}"/>')
    o.append(f'<path d="M{mm(kx-4.0*s)} {mm(ky+5.4*s)} L{mm(kx+4.0*s)} '
             f'{mm(ky+5.4*s)} L{mm(kx)} {mm(ky+24*s)} Z" fill="{res}"/>')
    return "\n".join(o)


# ------------------------------------------------------------ the full print --
def square(res=RESIST, ground=VOID, fill=None, medal=True):
    """The complete 350 mm print, origin at (0,0) in mm."""
    o = [f'<rect x="0" y="0" width="{mm(SQ)}" height="{mm(SQ)}" fill="{ground}"/>']
    a, bb = HEM, SQ - HEM
    c, d = HEM + TEPI, SQ - HEM - TEPI
    for lo, hi in ((a, bb), (c, d)):
        o.append(f'<rect x="{mm(lo)}" y="{mm(lo)}" width="{mm(hi-lo)}" '
                 f'height="{mm(hi-lo)}" fill="none" stroke="{res}" stroke-width="1.7"/>')
    for k in range(26):                                    # one cecek per punch
        t = c + (d - c) * (k + 0.5) / 26
        for x, y in ((t, a + TEPI / 2), (t, bb - TEPI / 2),
                     (a + TEPI / 2, t), (bb - TEPI / 2, t)):
            o.append(f'<circle cx="{mm(x)}" cy="{mm(y)}" r="{mm(0.85)}" fill="{res}"/>')

    for flip in (False, True):
        o.append(f'<g transform="translate({mm(c)},{mm(c)})">' if not flip
                 else f'<g transform="translate({mm(d)},{mm(d)}) rotate(180)">')
        o.append(cecek_row(0, INNER, PLINTH / 2, 61, res))
        o.append(f'<line x1="0" y1="{mm(PLINTH)}" x2="{mm(INNER)}" y2="{mm(PLINTH)}" '
                 f'stroke="{res}" stroke-width="1.1" opacity=".55"/>')
        for k in range(N):
            o.append(f'<g transform="translate({mm(BASE*k)},{mm(PLINTH)})">'
                     + rebung(BASE, SHOOT, res, fill=fill) + '</g>')
        for k in range(N - 1):
            o.append(f'<g transform="translate({mm(BASE*(k+0.5))},{mm(PLINTH)})">'
                     + counter(BASE, SHOOT, res, up=True) + '</g>')
        o.append('</g>')

    if medal:
        o.append(medallion(SQ / 2, SQ / 2, 1.0, res))
    return "\n".join(o)



def txt(x, y, s, fill="#8A8C8E", size=10.5, ls=1.6, anchor="start", weight=None):
    w = f' font-weight="{weight}"' if weight else ""
    return (f'<text x="{x}" y="{y}" {MONO} font-size="{size}" letter-spacing="{ls}" '
            f'fill="{fill}" text-anchor="{anchor}"{w}>{s}</text>')
