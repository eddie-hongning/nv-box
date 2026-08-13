# nv-box

Internal enclosure and packaging design documents for the NoughtVault TA2 Genesis Plate.

| Document | Object | Job |
| --- | --- | --- |
| `enclosure-001-the-weight.html` | Reclaimed chengal desk block / paperweight | Conceal the plate in plain sight, permanently |
| `textile-000-batik.html` | 350 mm hand-drawn batik square | Wrap the plate, and be a gift nobody was told about |

Enclosure 000 (the three-move walnut karakuri shipper) and Ledger 000 (price, market
and motion) are documented separately as published artifacts. Both are referenced
throughout the documents here — 001 deliberately reverses several of 000's decisions
and lists each reversal in its section `// 00`, and Textile 000 does the same against
Ledger 000 Rev B `§ 11`, which is where batik was first costed.

## Regenerating the batik artwork

The batik drawings are parametric rather than hand-authored. `tools/batik.py` holds
the geometry — the nested resist outlines and the noughts nested inside them are both
solved from the same triangle-inset routine, so a motif cannot overflow its own edge
when a dimension changes. Two generators consume it:

```sh
cd tools
python3 textile-000-build.py && mv textile-000-batik.html ..   # the document
python3 design-export.py                                       # dist/design-system/**
```

Every drawing is authored at two SVG units per millimetre, so the figures are the
specification: changing `SHOOT`, `N` or `KEPALA` in `batik.py` redraws both the
document and the design system correctly at the new proportions. Edit prose in
`tools/textile-000-batik.template.html`, never in the generated HTML.

## The design system

`dist/design-system/` is the Claude Design bundle — eleven standalone component
previews across Foundations, Brand, Motifs, Patterns, Prints and Packaging, each
carrying a first-line `@dsCard` marker so the Design System pane indexes it without
explicit asset registration. It is generated from the same `batik.py`, so the system
and the specification cannot drift apart.

Pushing it needs design-system authorization, which `/design-login` only grants from
an interactive terminal — not from Claude Code on the web. Either run the sync from a
local terminal, or use Claude Design's **Send to Claude Code Web** to seed the project
first. `dist/noughtvault-batik-design-system.zip` is the same bundle, packaged.

## Handling

These documents describe concealment. Treat them as internal:

- Never publish the specs, the release geometry, or photographs of an open unit.
- Vendor-facing drawings carry no brand marks and use the cover description only
  (`pemberat kertas kayu chengal` — a chengal paperweight with a serviceable base).
- Cost figures are estimates pending quotes, and the timber-compliance notes
  (CITES, MTIB licensing, Lacey, EUDR) need confirming with a broker before the
  first production run.
- The batik square is a surprise, so it is subject to the same rule as the
  enclosure: never in the listing, never in What's Included, never in an alt tag.
  The vendor brief says `napkin batik 14 × 14, corak tempahan` and nothing else.
- Only wax-resist work may be called batik. A screen-printed square is a
  batik-*motif* print and the copy has to say so.
