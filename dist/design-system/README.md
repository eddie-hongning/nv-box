# NoughtVault — Batik (Textile 000)

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
