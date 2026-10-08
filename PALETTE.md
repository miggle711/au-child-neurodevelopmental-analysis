# Colour Palette

Updated 2026-10-08 to a clinical/developmental palette, replacing the
earlier generic orange/blue scheme. Chosen to read as public-health and
early-childhood-screening reporting (think ABS/AIHW style charts) rather
than a generic tech or data-journalism look. Soft clay is the primary
accent, sage green signals a positive/better outcome where a chart has
one, and both sit on a warm paper ground.

## Design tokens (set in index.html's `:root`)

| Token | Value | Use |
|---|---|---|
| `--bg` | `#f6f3ec` | Page background |
| `--bg-band` | `#ece6d8` | Full-bleed section backgrounds (Act 2) |
| `--fg` | `#2b2a26` | Body text |
| `--fg-muted` | `#6e6a5e` | Captions, source tags |
| `--accent` | `#c4703f` | Clay: primary accent, callouts |
| `--accent-soft` | `#e3c4a8` | Light clay tint |
| `--sage` | `#6b7c5e` | Secondary accent: positive/comparison outcomes |
| `--sage-soft` | `#c9d2bd` | Light sage tint |
| `--line` | `#d9d1bd` | Borders, dividers |
| `--chart-bg` | `#fffdf8` | Chart frame background (not pure white) |

**Deliberately single-theme (2026-10-08):** the page always renders in
this light palette, ignoring the visitor's system dark-mode setting. A
dark-mode version was tried and reverted: the 15 Vega/Vega-Lite chart
specs all have axis labels, gridlines and text coloured for a light
background, and none of that recolours per theme. On an actual
dark-mode device the chart frame went dark but its internal text and
gridlines stayed dark-on-dark and became nearly illegible. Properly
supporting dark mode would mean auditing and patching all 15 specs
individually with theme-aware colours, which couldn't be visually
verified in this environment, so the page commits to one palette
instead.

## Categorical attributes (fixed hex values, chart-level)

| Attribute | Value | Colour | Hex | Used in |
|---|---|---|---|---|
| Sex | Male / Boys | Blue | `#4292c6` | #6 (pyramid), #10 (bullet) |
| Sex | Female / Girls | Clay | `#d94801` | #6 (pyramid), #10 (bullet) |
| Condition scope | Autistic | Clay | `#c4703f` | #2 (dumbbell) |
| Condition scope | Non-autistic / general disability | Sage | `#6b7c5e` | #2 (dumbbell) |
| Outcome | Need met / good outcome | Blue | `#3182bd` | #11 (heatmap, "need met" side) |
| Outcome | Need not met / concerning outcome | Red | sequential `reds` | #11 (heatmap, "need not met" side) |

**Note:** sex (#6, #10) deliberately keeps the blue/orange pairing rather
than switching to clay/sage, since that pairing is already locked in and
consistent across both charts that use it (see commit history) — redoing
it to match the new palette exactly would only be worth it if it read as
inconsistent next to the rest of the page. Revisit if it looks out of
place once viewed on the live site.

## Sequential / magnitude scales (per-chart, not shared)

These are legitimate to differ, since each represents a different metric
and readers interpret them locally within one chart, not across charts:

| Chart | Scheme | Metric |
|---|---|---|
| #3 State choropleth | `oranges` | Developmental vulnerability % |
| #4 LGA proportional symbol | `oranges` | Developmental vulnerability % |
| #5 Remoteness small-multiples | `oranges` | Developmental vulnerability % |
| #8 Beeswarm | `oranges` | % reporting co-occurring characteristic |
| #12 Streamgraph | `oranges` | % by disability group |
| #13 NDIS rate choropleth | custom clay ramp (`#e3c4a8` → `#c4703f` → `#6b3a1f`) | NDIS autism participants per 1,000 |

**Note:** #13 used to use Vega's built-in `purples` scheme, which read as
an arbitrary, unrelated colour next to the rest of the page. Replaced with
a custom clay-family ramp so every map on the page sits in the same colour
family, while #13 staying visually distinguishable from #3/#4/#5 by being
a flat sequential ramp rather than a graduated `oranges` scheme (and by
sitting in Act 2 as the explicit "this one is condition-specific, not a
proxy" map).

## Typography

| Role | Typeface | Notes |
|---|---|---|
| Display (headings) | Lora | Humanist serif, used in public-sector and editorial reporting; pairs with the clinical/developmental direction better than a display serif like Fraunces, which read as more decorative/literary |
| Body | Public Sans | Designed for US federal government digital services, widely used in public-health and civic data reporting; reads as credible and unobtrusive |
| Data labels / captions | JetBrains Mono | Unchanged — monospace numerals for source tags and the "Act N" eyebrow labels |

## Whitespace fixes (2026-10-08)

Several charts had excess empty space relative to their actual content,
most visibly chart #2 (dumbbell, 4 rows in a 220px-tall chart) and chart
#13 (NDIS choropleth, 500×400 canvas for a map that renders much smaller).
Fixed by:
- Chart #2: `"height": 220` → `"height": {"step": 45}`, so the chart
  height scales with the actual number of categorical rows instead of a
  guessed fixed value
- Chart #13: reduced `width`/`height` from 500×400 to 440×350, replaced an
  `autosize: fit` attempt (which clipped the title) with explicit `padding`
  instead
- `.chart-frame` in index.html now uses `display: flex;
  justify-content: center` so a chart narrower than its frame doesn't look
  like it's floating in an oversized box

Other charts' heights were checked against their row counts and left
as-is where the ratio was already reasonable (roughly 45-55px per
categorical row).
