# Submission Write-up

For "Growing Up Different", the FIT3179 neurodevelopmental conditions visualisation. Copy each part into the matching Moodle field.

---

## Part I: Domain, Who, Why

**Domain:** Neurodevelopmental conditions in Australian children (autism, ADHD, developmental/learning disability): how common they are, how they vary by age, sex and geography, and what happens to a child's access to support after diagnosis.

**Who:** A general reader with no statistics background and no assumed familiarity with Australian institutions. Every acronym (AEDC, NDIS, SDAC) is defined in plain language on first use, so the page works for a reader coming to this material from outside Australia as well as within it.

**Why:** Public discussion of rising autism/ADHD diagnosis rates tends to split into two oversimplified claims: an "epidemic," or pure over-diagnosis. Neither holds up against the data. Diagnosis is catching up with children as they age, support looks very different depending on what a child needs, and geography affects whether a child is identified and supported more than how severe their needs are. That last point only becomes visible by combining five government sources nobody has previously put on one page; no single source shows that one state can be both the most vulnerable and the least supported in the country.

---

## Part II: What, The Data

Five public sources, chosen to triangulate a broad screening measure (has geography, not condition-specific) against condition-specific survey data (accurate, national only). Full detail in [SOURCES.md](https://github.com/miggle711/au-child-neurodevelopmental-analysis/blob/main/SOURCES.md).

| Source | Author | Used for |
|---|---|---|
| AEDC, 2024 | Australian Government | All 3 required map idioms (only source with sub-national geography) |
| ABS, Autism in Australia / Children and Young People with Disability, 2022 | ABS | Age/sex, co-occurrence, schooling-support, disability-group charts |
| AIHW, Australia's Children, 2022 | AIHW | Educational adjustment, schooling restriction, disability-by-age |
| NDIS Data Research, Dec 2024 | NDIA | Autism access-rate map (only autism-specific source with geography) |
| Productivity Commission, RoGS 2026 | Australian Government | Multi-year access and wait-time trends |

Each source was downloaded raw, then the relevant tables extracted into small processed CSVs. There were three that needed extra work: LGA centroid coordinates came from a community GitHub repo, joined by name to the LGA-level data (514/544 matched); the NDIS autism rate was computed by dividing participant counts by ABS population, the bivariate map's colours were precomputed in Python, ranking each state into terciles on two measures at once.

**Limitation:** no Australian dataset tracks autism/ADHD by region. All three required maps use AEDC's broader "developmental vulnerability" screening measure as a proxy. This disclosed directly in every map caption.

---

## Part III: How, Idiom Rationale and Special Features

### Act 1: How common is it?

**1. Autism prevalence trend** (grouped bar, basic)
Why: the ABS survey only runs every 3-4 years, so a connected line would falsely imply a trend between unmeasured years.
How: discrete bars per survey wave let the reader compare the two age groups at each real measurement point without being misled about what happened in between.
Marks/channels: area marks (bars). Position encodes year and estimate (length, an ordered channel); colour hue encodes age group (a categorical channel for a nominal attribute).

**2. Schooling difficulties, autistic vs. other disability** (dumbbell, advanced)
Why: a dumbbell is the standard idiom for a paired comparison repeated across several categories.
How: the line length between the two dots lets the reader read the size of the gap directly, across all four measures at once.
Marks/channels: a line mark for the connecting rule, point marks for the two values. Position encodes category and percentage (an ordered channel); colour hue encodes group (a categorical channel).

### Act 2: Where it varies

**3. Vulnerability by state** (choropleth, map idiom 1)
Why: a choropleth is the standard idiom for one measure attached to named regions, and a hand-built Albers projection avoids Mercator's distortion of the tropical north versus the south.
How: the colour fill lets the reader read the Northern Territory's extreme value directly off real geography, and hovering bolds the outline under the cursor for confirmation.
Marks/channels: area marks (geoshape polygons), with text marks for state labels. Colour luminance encodes vulnerability rate (an ordered channel); strokeWidth marks the hovered state.

**4. Vulnerability by local area** (proportional symbol map, map idiom 2)
Why: no boundary file exists for all 544 LGAs, and a full choropleth would show suppressed LGAs as confusing holes, so a point map was used instead.
How: size encodes sample size and colour encodes the rate, so the reader doesn't mistake a small, unreliable high reading for a large, reliable one.
Marks/channels: point marks (circles). Position encodes location (longitude/latitude); size (area) encodes children surveyed and colour luminance encodes vulnerability rate, two separate ordered channels rather than one redundant one.

**17. Vulnerability, hex-bin aggregation** (hex-bin grid, map idiom 3)
Why: binning and averaging nearby points on a regular grid is mechanically distinct from both the choropleth and the point map above it.
How: smoothing out LGA-level noise and removing state boundaries lets the reader see the real north-south clustering pattern at a glance.
Marks/channels: line marks closed into hexagon polygons (area). Position encodes precomputed grid location; colour luminance encodes the average rate, with a separate neutral grey for no-data cells.

**13. NDIS autism rate by state** (choropleth, bonus)
Why: reusing chart 3's exact idiom makes the two maps directly comparable at a glance.
How: lets the reader see the pattern reverse between general vulnerability and actual autism-service access, state by state.
Marks/channels: area marks (geoshape polygons), with text marks for state labels. Colour luminance encodes the NDIS rate per 1,000, the same ordered channel as chart 3 for direct comparison.

**16. Vulnerability x access, combined** (bivariate choropleth, bonus, advanced)
Why: the page's key finding, that the NT is worst on both measures, isn't visible from either single map alone.
How: one hue ramp (not two crossed hues) lets the reader read "bad on both" as the single darkest colour, without needing colour vision to tell two hues apart.
Marks/channels: area marks (geoshape polygons for the map, rect marks for the legend grid). Colour (precomputed, one hue varying in luminance/saturation) encodes the combined bivariate class, avoiding a second colour hue that would need to be told apart.

### Act 3: Who it affects

**6. Autism by age and sex** (population pyramid, advanced)
Why: a pyramid is the standard idiom for comparing two populations across the same ordered age bands.
How: mirrored bars let the reader see the reversal in diagnosis rate by sex as a visible asymmetry, without a cluttered shared legend.
Marks/channels: area marks (bars), one panel per sex. Position encodes age group; length encodes the estimate, an ordered channel, with sex encoded by panel rather than colour.

**7. Disability groups among children** (sorted lollipop, advanced)
Why: replaces an earlier radar chart, whose polygon shape implied a relationship between six categories that don't actually have one.
How: sorting the stems by value lets the reader identify the largest category at a glance, with no implied relationship beyond rank.
Marks/channels: line marks (stems) and point marks (the lollipop heads), with a text mark for the value. Position on a common scale encodes percentage, an ordered channel.

**8. Co-occurring conditions** (dot plot, basic)
Why: a co-occurrence rate only makes sense compared against other rates, not a zero baseline, so dots were used instead of bars.
How: lets the reader compare several rates side by side and see that autism rarely occurs alone.
Marks/channels: point marks, with a text mark for the category label. Position encodes percentage; colour luminance also encodes percentage, reinforcing the same ordered attribute.

### Act 4: What happens next

**12. Disability composition by age** (streamgraph, advanced, bonus)
Why: the data is discrete percentages at 3 age bands, not a continuous distribution, so a ridge plot was rejected in favour of a streamgraph.
How: changing band width lets the reader see diagnosis lag directly, as one category's share grows with age.
Marks/channels: area marks (stacked, stream-ordered). Position encodes age group; area (band thickness) encodes percentage, an ordered channel; colour hue encodes disability group, a categorical channel.

**9. Educational adjustment, by level and sector** (icon array, advanced, two panels)
Why: the two source tables are separate one-variable breakdowns, so a mosaic plot would require fabricating data that doesn't exist.
How: each square equals 1% of students, giving the reader a part-of-whole read a bar chart's axis doesn't provide as directly.
Marks/channels: point marks (squares) in a grid, with a text mark for the value. Colour hue (filled vs unfilled) encodes a binary categorical attribute, with count of filled squares standing in for the percentage.

**10. Schooling restriction by sex** (bullet chart, advanced)
Why: a bullet chart's built-in reference marker does something a bar chart can't.
How: lets the reader compare boys' and girls' rates against each other and against the "all children" baseline in one glance.
Marks/channels: area marks (bars) for the value and background range, a line mark (tick) for the reference marker. Length encodes percentage, an ordered channel; colour hue encodes group, a categorical channel.

**11. Support needs not fully met** (grouped bar, basic, bonus)
Why: an earlier heatmap used two colour scales for complementary percentages that always sum to 100, a redundant encoding.
How: a grouped bar with legend click-to-isolate lets the reader focus on "met" or "not met" alone, sorted by highest unmet need.
Marks/channels: area marks (bars), with a text mark for the value. Length encodes percentage, an ordered channel; colour hue encodes status, a categorical channel.

**14. NDIS access over time** (line chart, basic, bonus)
Why: a plain line chart is the correct idiom for one continuous measure over genuinely continuous years.
How: a zero-based axis and a visible 2021 dip let the reader see the real shape of the improvement, not an exaggerated one.
Marks/channels: a line mark, with a text mark for the value. Position on a common scale encodes year and access rate, both ordered channels.

**15. NDIS plan wait times** (multi-line, basic, bonus)
Why: kept as a plain multi-line chart rather than labelled a slope chart, since four non-consecutive years isn't a genuine two-point slope.
How: legend click-to-isolate lets the reader follow one line at a time, and the real gap in 2023-24 renders as a visible break, not a false dip.
Marks/channels: line marks and point marks, with a text mark for the value. Position encodes year and days, ordered channels; colour hue encodes measure (median vs 90th percentile), a categorical channel.

### Interactivity, overall

Kept to two patterns, deliberately excluding filters, dropdowns or free querying, per the brief's "appropriate level" rather than "exploration tool" instruction: a hover tooltip on every chart, legend click-to-isolate on 5 charts (1, 2, 11, 12, 15), and hover highlight on 3 maps (3, 4, 13) whose gradient scale has no legend to click.

### Design principles applied

- **Data-ink ratio:** gridlines and borders minimised throughout; chart 17 drops its state outline layer once it was found to drift out of alignment and added nothing necessary.
- **Storytelling:** four acts, each opening with a question the next chart answers.
- **Layout:** one scrolling column (max 760px), widening into a full-bleed band for the maps only, no horizontal scroll.
- **Typography:** one serif display face, one sans body face, consistent across every chart's own text config.
- **Marks and channels:** named per chart above; colour is reserved for meaning, never decoration, and two earlier double-encoding mistakes (chart 4, an earlier version of chart 11) were caught and fixed on review.
