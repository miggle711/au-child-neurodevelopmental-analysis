# Colour Palette

A fixed set of colours for attributes that repeat across multiple charts,
so the same thing always looks the same everywhere it appears on the page.
Sequential/magnitude scales (choropleths, heatmaps) are listed separately
below and are not part of this fixed categorical palette — each already
uses an appropriate, distinct scheme for its own metric.

## Categorical attributes (fixed hex values)

| Attribute | Value | Colour | Hex | Used in |
|---|---|---|---|---|
| Sex | Male / Boys | Blue | `#4292c6` | #6 (pyramid), #10 (bullet) |
| Sex | Female / Girls | Orange | `#d94801` | #6 (pyramid), #10 (bullet) |
| Condition scope | Autistic / autism-specific | Orange | `#d94801` | #2 (dumbbell) |
| Condition scope | Non-autistic / general disability | Grey-blue | `#9ecae1` | #2 (dumbbell) |
| Outcome | Need met / good outcome | Blue | `#3182bd` | #11 (heatmap, "need met" side) |
| Outcome | Need not met / concerning outcome | Red | `#d94801` → see note | #11 (heatmap, "need not met" side) |

**Note on #11:** the heatmap already uses `blues` (met) vs `reds` (not met)
as two independent sequential scales, which is a different and equally
valid pattern (severity gradient within each status) — not a plain
two-colour categorical choice. Left as-is; flagged here only so it's not
mistaken for an inconsistency.

**Note on orange meaning two different things (Female/Girls AND
Autistic):** these never appear together in the same chart, so there's no
direct clash, but it does mean orange isn't a single fixed "meaning" across
the whole page the way blue mostly is. Acceptable given the alternative
(inventing a 3rd hue) adds complexity without a real payoff — flagged here
for visibility, revisit if it reads as confusing once charts are laid out
together on the actual page.

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
| #13 NDIS rate choropleth | `purples` | NDIS autism participants per 1,000 |

**Note:** #3, #4, #5, #8, #12 all use `oranges` and are consistent with
each other already (all developmental-vulnerability-adjacent metrics on
the same hue family is arguably a feature, not a bug — reinforces that
these all come from the same AEDC-proxy source, discussed in NARRATIVE.md).
#13 deliberately uses a different hue (`purples`) specifically because it's
a genuinely different, condition-specific metric — this is an intentional
signal, not an inconsistency.

## Fixes needed (tracked, not yet applied)

- [ ] Chart #6 (pyramid): confirm Male=blue/Female=orange is the final
      assignment (matches the table above)
- [ ] Chart #10 (bullet): currently uses a single flat orange for all 3
      bars (All children/Boys/Girls aren't colour-differentiated from each
      other at all) — needs updating so Boys=blue, Girls=orange, matching
      chart #6. "All children" can stay a neutral grey/black since it's not
      a sex category
- [ ] Chart #2 (dumbbell): confirm Autistic=orange/Non-autistic=grey-blue
      is final (already matches the table above, no change needed)
