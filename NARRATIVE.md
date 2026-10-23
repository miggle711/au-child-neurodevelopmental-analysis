# Narrative Plan — AU Child Neurodevelopmental Data Visualisation

Working plan for the FIT3179 Data Visualisation 2 assignment. Amend as the
story, data, or chart choices evolve.

Domain: neurodevelopmental conditions (ADHD, autism, learning disabilities)
in children in Australia, diagnosis/vulnerability rates, demographic and
geographic variation, and how it plays out in education/support systems.
Audience: the average Australian (general public, no stats background).

See [SOURCES.md](SOURCES.md) for full data source details.

---

## Important terminology / data-scope caveat

**"Developmentally vulnerable" (AEDC) is not the same thing as ADHD, autism,
or any named neurodevelopmental condition.** The AEDC is a general school-entry
screening census across 5 domains (physical, social, emotional, language,
communication); a child is "vulnerable" if they score in the bottom 10%
nationally on one or more domains, for any reason (health, disadvantage,
language background, or an underlying condition — the AEDC doesn't say why).

This matters because **all 3 of our map idioms are built on AEDC data**, since
it's the only source with any geographic breakdown (state, LGA, remoteness).
Our condition-specific sources (ABS Autism in Australia 2022, ABS Children
and Young People with Disability 2022, AIHW Australia's Children 2022) are
**confirmed national-only, with no state/territory/PHN/LGA breakdown
anywhere in any of their ~90 combined data tables**.

We actively searched for sub-national ADHD/autism-specific data as a
follow-up (NDIS's full data explorer, AIHW's MBS/PBS geographic tools, NSW/
Vic/Qld state health portals, and the one dataset that used to have this —
ACSQHC's Atlas of Healthcare Variation SA3-level ADHD medicine dispensing,
2013-14 to 2016-17) and came up empty — the Atlas page/data file is no
longer reachable, and nothing else has sub-national breakdown by named
condition. **This is a real, citable limitation of Australian public data,
not a gap in our research** — worth stating explicitly in the assignment's
"What" (data) description as evidence of critical evaluation.

**Framing rule for chart/map copy:** never caption a map as "autism rates" or
"ADHD by region" — always "developmental vulnerability" (AEDC's term) with a
one-line explainer that this is a broader screening measure, correlated with
but distinct from specific diagnosed conditions. Save "autism"/"ADHD"/
"disability" language for the national-only ABS/AIHW charts, where it's
accurate.

---

## Assignment constraints this plan is designed against

- ≥3 different map idioms (Vega-Lite/Vega)
- ≥10 charts total (small-multiples/series count as one)
- ≥8 total idioms, ideally 5–8+ advanced (not bar/line/pie/scatter/bubble/dot
  plot/stacked or grouped bar/area chart) for a D/HD grade
- Combine data from ≥2 different sources (we have 5)
- Single scrollable page, no horizontal scroll, no section-swapping buttons
- Storytelling: text + charts guide the reader in a logical sequence
- Avoid statistical jargon; explain any specialised terms
- "Appropriate level of interactive exploration" — but explicitly NOT an
  "expert tool for exploring and analysing a dataset." No filters/dropdowns/
  free querying. Buttons may show/hide elements, never swap major sections

---

## Interactivity (2026-09-30)

Every chart now has a hover tooltip surfacing its exact value(s) — this is
the "appropriate level" the brief asks for: it deepens understanding of the
point already being made, without turning the page into an exploration
tool. Deliberately did NOT add filters, dropdowns, or free-form querying,
per the brief's explicit "presentation not exploration" principle.

Fixed 4 charts that had no tooltip at all (an inconsistency, not a design
choice): #7 radar (added a `symbol` mark layer with vertex points + a Vega
`tooltip` signal — raw Vega needs this added explicitly, unlike Vega-Lite),
#10 bullet chart, #14 NDIS access trend, #15 NDIS wait-time chart. All 15
charts are now consistent.

Possible further addition if time allows (optional, not required): a
show/hide toggle revealing chart #15's detail after chart #14's headline
story. Not necessary to meet the brief.

A click-highlight linking the state choropleth (#3) to the LGA
proportional symbol map (#4) and the NDIS choropleth (#13) was built,
but found non-functional on inspection and removed on 2026-10-23 — see
the "Cross-chart click highlight removed" note later in this document
for the full story. Each of those three maps works correctly as a
standalone chart; losing the cross-filter doesn't remove any finding
from the page.

---

## Narrative arc (4 acts)

**Act 1: The scale of the issue (national context)**
Establish that autism diagnosis is rising (chart 1), then show that autistic
children face real, measurably higher schooling difficulty and support needs
than other children with disability (chart 2) — grounding the story in
condition-specific evidence before moving to geography.

**Act 2: Where it varies geographically**
The 3 required map idioms live here: state-level, then LGA-level (revealing
within-state clusters invisible at state level — the "aha" moment), then a
remoteness-category view (urban vs regional/remote gap). Uses AEDC
developmental-vulnerability data (the only source with geography — see
caveat above) as a geographic proxy, clearly labelled as distinct from the
condition-specific charts elsewhere in the story.

**Act 3: Who's affected & how it plays out across children**
Age/sex population pyramid (chart 6), disability-group composition in
children 0-14 (chart 7), and co-occurring characteristics among autistic
people (chart 8) — all genuinely condition-specific ABS data.

**Act 4: What happens at school / in support systems**
Educational adjustment (chart 9) → unmet daily-life support needs (chart 11)
→ schooling restriction outcome (chart 10) — a fuller before/during/after
arc on access to support, directly answering the brief's prompt to "explore
how awareness and access to support have changed" (cross-sectional here,
not longitudinal, but the same underlying question).

---

## Chart-by-chart plan

| # | Act | Chart idiom | Basic/Advanced | Data source | What it shows |
|---|-----|-------------|-----------------|--------------|----------------|
| 1 | 1 | Grouped bar chart | Basic | ABS Autism in Australia 2022 | Autism prevalence in Australian children, 2015/2018/2022 (national only) — ✅ built & rendered, `specs/01_autism_trend_area.vl.json`. **Idiom fix (2026-10-23):** was a stacked area/line chart, correctly flagged on review for implying continuity between the three real survey waves — the ABS SDAC only runs every 3-4 years, so a connected line between 2015/2018/2022 visually asserts a trend shape for years with no actual measurement. An ordinal x-axis fixed the spacing (no false sense of annual granularity) but not the continuity problem, since connected points still draw an implied path between unmeasured years. Switched to a grouped bar chart (year on x, age group on xOffset) — each survey wave is now a genuinely discrete, disconnected set of bars, honestly showing 3 real measurements with no implied trajectory between them, while the rising trend is still immediately clear from bar height alone |
| 2 | 1 | Dumbbell / connected dot plot | Advanced | ABS Autism in Australia 2022 (Table 4, national only) | Schooling difficulties/supports, autistic vs. non-autistic children with disability aged 5-20 (attends special classes, needs day off, has difficulty, uses assistance) — ✅ built & rendered, `specs/02_autism_schooling_dumbbell.vl.json`. **Replaced AEDC national trend** — this is genuinely condition-specific service-usage data instead of a general vulnerability proxy |
| 3 | 2 | Choropleth map | Map idiom #1 (Advanced) | AEDC state trends | Developmental vulnerability % by state/territory (AEDC, general screening measure) — ✅ built & rendered, `specs/03_state_choropleth.vl.json`. NT stands out sharply (40.8% vs next-highest 25.9%) |
| 4 | 2 | Proportional symbol map | Map idiom #2 (Advanced) | PHIDU LGA data + HughParsonage/ABS-data centroids | Developmental vulnerability % by LGA (514 of 544 LGAs matched by name to 2016-vintage centroids) — reveals within-state hotspots. ✅ built & rendered, `specs/04_lga_proportional_symbol.vl.json`. Swapped from choropleth to proportional-symbol: no small ready-made LGA boundary TopoJSON with matching codes exists, and a full 544-polygon choropleth would look noisy/patchy given ~19% suppressed LGAs. **Fixed (2026-10-20):** size and colour originally both mapped to `vulnerable_1plus_pct` — textbook double encoding, flagged by the lecturer as redundant/confusing. Size now maps to `vulnerable_1plus_valid_n` (children surveyed) instead, so the two channels carry genuinely different information and a small, extreme-reading LGA no longer looks visually equivalent to a large, reliable one. **Caption updated (2026-10-21)** to fold in chart #5's remoteness-gradient finding after #5 was removed as a redundant idiom (see note above) |
| ~~5~~ | — | ~~Small-multiples map by remoteness area~~ | **Removed (2026-10-21)** | — | Mechanically the same idiom as chart #4 (LGA points sized/coloured by vulnerability %), just faceted by remoteness band — not a genuinely distinct map idiom on honest review. Its finding (22.5% major cities → 35.8% remote/very remote) was folded into chart #4's caption instead of being lost. Old spec in `deprecated/specs/05_remoteness_small_multiples.vl.json`. A tile-grid cartogram was considered as a replacement and rejected (told the same story as chart #3's choropleth, but worse); a hex-bin was also considered, initially rejected as redundant with chart #4, then revisited and actually built as chart #17 once the map-idiom-count risk became concrete — see that chart's own entry below |
| 6 | 3 | Population pyramid | Advanced | ABS AutismDC01 (national only) | Autistic children by age group (0-4, 5-14, 15-24) × sex — ✅ built & rendered, `specs/06_autism_age_sex_pyramid.vl.json`. Shows males diagnosed at ~2-3x the rate of females across all age bands |
| 7 | 3 | Sorted lollipop chart | Advanced | ABS Children and Young People with Disability 2022 (Table 3, national only) | % of children aged 0-14 with each disability group (Sensory & speech, Learning & understanding, Physical, Psychosocial, Head injury/ABI, Other) — ✅ built & rendered, `specs/07_disability_groups_lollipop.vl.json`. "Learning and understanding" (6.5%) is the largest slice. **Idiom fix (2026-10-16):** was a radar chart — an outside review correctly identified radar as the weakest idiom choice here, since these 6 categories have no natural circular order, so a radar's polygon shape/area implies a pattern that isn't actually in the data (a well-known general critique of radar charts, not specific to this dataset). Replaced with a sorted lollipop showing the same 6 numbers honestly, with no implied relationship between categories. This also removes the only raw-Vega (non-Vega-Lite) spec from the page, simplifying the embed logic. Old radar kept in `deprecated/specs/07_disability_groups_radar.vg.json` |
| 8 | 3 | Beeswarm / jittered dot plot | Advanced | ABS Autism in Australia 2022 (Table 3, national, all ages not child-restricted) | Co-occurring characteristics among autistic Australians (e.g. "slow at learning" 71.4%, social/behavioural difficulties 62.4%, mental illness 52.5%) — ✅ built & rendered, `specs/08_autism_cooccurring_beeswarm.vl.json`. **Replaced AEDC SEIFA gradient** — shows autism rarely occurs in isolation. **Known remaining issue:** source table isn't age-restricted to children — a child-restricted equivalent for autism-specific co-occurring types doesn't exist in any source checked (see relevance fix #2 below); this chart stays framed as national context, not a children-only statistic |
| 9 | 4 | Icon array (two panels) | Advanced | AIHW Education (Table 10–11, national only) | % of students receiving an educational adjustment for disability, by school sector and separately by adjustment level — ✅ built & rendered, `specs/09a_education_adjustment_level_icon_array.vl.json` + `specs/09b_education_adjustment_sector_icon_array.vl.json`. Swapped from mosaic plot: Tables 10 & 11 are two separate 1-variable breakdowns, not a real sector×level cross-tab, so a mosaic would require fabricating joint data (against the brief's "no fabricated data" rule). **Split into two charts (2026-10-23):** originally one spec with an outer row-facet separating "Adjustment level" from "School sector," but the rotated row-facet header could not be reliably top-aligned with its row's content — `labelAnchor`, `labelAlign`, and `labelBaseline` were all tried and either had no effect or made it worse, confirmed via precise pixel measurement in a real browser, not just visual judgement. Rather than keep fighting Vega-Lite's row-facet header layout, split into two independent single-level column-facet specs, each with its own plain chart title instead of a rotated side label. Still counted as **one chart** for idiom-count purposes (same idiom, same source table, split for a layout/rendering fix rather than distinct content — consistent with the rubric's "a small-multiples chart, or a series of similar charts, count as a single chart" rule), so this does not change the project's chart-count or idiom-count totals. Old combined spec kept in `deprecated/specs/09_education_adjustment_icon_array.vl.json` |
| 10 | 4 | Bullet chart | Advanced | AIHW Health (Table 28, national only) | % of children aged 5-14 with disability who have a schooling restriction — overall (7.8%) vs boys (9.9%) vs girls (5.6%), each measured against the "all children" reference line — ✅ built & rendered, `specs/10_schooling_restriction_bullet.vl.json`. Swapped from waffle chart (same idiom family as #9, would've been repetitive) and from a plain bar chart (basic, not advanced) |
| 11 | 4 | Sorted horizontal bar chart | Basic, bonus | ABS Children and Young People with Disability 2022 (Table 4, national only) | Among children aged 0-14 with disability who need assistance, % whose need is NOT fully met, by activity type, sorted highest to lowest — ✅ built & rendered, `specs/11_children_unmet_need_bar.vl.json`. **Idiom fix (2026-10-16):** was a 2-column heatmap with independent blue/red colour scales for "met" and "not met" — an outside review correctly identified this as redundant encoding, since the two percentages are complementary (sum to 100 for every activity), so the second colour scale told readers nothing the first didn't already show. Replaced with a single sorted bar of "% not met" — now honestly basic rather than incorrectly advanced, which is the right tradeoff since this is a bonus chart, not one of the 10 required. Health care (30%) and self-care (28%) are the least-met needs. Old heatmap moved to `deprecated/specs/11_children_unmet_need_heatmap.vl.json` |
| 12 | 3 | Streamgraph | Advanced, bonus | AIHW Health (Table 27, national only, 2018) | % of children with each disability group (Intellectual, Sensory & speech, Psychosocial, Physical restriction, Other), by age band 0-4/5-9/10-14 — ✅ built & rendered, `specs/12_disability_by_age_streamgraph.vl.json`. Checked as a ridge-plot candidate first but rejected — the underlying data is discrete categorical %, not a continuous distribution, so a ridge plot would misrepresent its shape. Streamgraph instead directly visualises diagnosis lag: "Intellectual" disability balloons from 1.1% (age 0-4) to 6.9% (age 10-14), while "Sensory and speech" narrows over the same span. This is a **12th, bonus chart** |
| 13 | 2 | Choropleth map | Map idiom #4 (Advanced, bonus) | NDIS Data Research (state, Dec 2024) + ABS Estimated Resident Population (Dec 2024) | Autism NDIS participants per 1,000 population, by state/territory — ✅ built & rendered, `specs/13_ndis_autism_rate_choropleth.vl.json`. Genuinely autism-specific (unlike the AEDC-based maps) and a real per-capita rate (computed by dividing NDIS's raw participant counts by ABS population — the raw sheet's own "% of all NDIS participants" metric was rejected as it reflects scheme caseload mix, not prevalence). Notable finding: produces an almost inverse pattern to the AEDC choropleth — SA highest (13.6 per 1,000), NT *lowest* (5.9 per 1,000), suggesting NT's high AEDC vulnerability doesn't translate into high NDIS autism access, a possible sign of under-diagnosis/under-service in remote areas rather than lower true prevalence. This is a **4th, bonus map** — genuinely condition-specific, unlike maps 3-5 |
| 14 | 1/4 | Line chart | Basic, bonus | Productivity Commission, Report on Government Services 2026 (Table 15A.20, national only) | % of estimated eligible children aged 0-14 who have an NDIS plan, 2019-2023 — ✅ built & rendered, `specs/14_ndis_children_access_trend.vl.json`. **Closes the "access to support over time" gap** (see relevance fix #2 below) — a genuine 5-year multi-year trend showing NDIS access for children rose from 60.2% to 90.2% of the estimated eligible population, with a visible dip in 2021 (not smoothed over). Disability-general, not neurodevelopmental-specific, but autism/developmental delay dominate the NDIS 0-14 population so it's a defensible proxy, clearly labelled as such. **Truncated-axis bug fixed (2026-10-23):** the y-axis domain was hardcoded to `[50, 100]` instead of starting at zero, exaggerating the visual slope of the rise (a real 30-point increase was stretched to fill 60% of the chart's height instead of the honest ~30%) — a classic truncated-axis distortion, caught on review. Fixed to `[0, 100]`; the rise still reads clearly, just without the artificial steepening. **Verified against the source (2026-10-23):** checked directly against `data/raw/rogs/rogs15.csv` — the series genuinely stops at 2023 because the PC stops publishing this specific "% of potential population" metric for this age band after that year (2024/2025 only report a differently-scaled "rate per 1,000" instead), not because of incomplete data collection on this project's part. Corrected the citation year from 2025 to 2026 to match chart #15, confirmed to be the same source download |
| 15 | 4 | Multi-line chart | Basic, bonus | Productivity Commission, Report on Government Services 2026 (Table 15A.45, national only) | Days to approve a first NDIS plan for young children (median and 90th percentile), 2020-21 to 2024-25 — ✅ built & rendered, `specs/15_ndis_wait_time_multiline.vl.json`. A distinct "access to support" story from chart #14 — this is a genuine wait-time reduction (median 28→46→29→10 days; 90th percentile 65→87→69→22 days), and the gap between the two lines shows how unevenly that wait is experienced. **Two honest data quirks disclosed in the chart caption, not hidden:** 2023-24 is missing from the source itself (rendered as a real visual break in the line, not interpolated — required a `format.parse` fix since Vega-Lite otherwise silently coerced the empty CSV value to 0, which would have been a serious, misleading defect), and the age band changed from "0-6" to "0-8" in the final year, so the last point isn't perfectly comparable to earlier ones. Deliberately built as a plain multi-line chart (basic, not advanced) rather than mislabelling it as a "slope chart" — a genuine slope chart is a 2-point before/after comparison, and forcing that framing onto 4 non-consecutive data points would have been dishonest about what the idiom actually is. **Verified against the real source (2026-10-23):** re-checked directly against the Productivity Commission's actual RoGS 2026 Table 15A.45 (`assets.pc.gov.au`) after being asked "are we sure there's no data for 2023-24" — all 5 reported values match the source exactly, and the PC's own footnote gives the specific reason for the gap ("Data were not available for the 2023-24 period due to the NDIA's transition to a new information system"), now reflected in the page caption instead of the previous vaguer "missing from the official record." Also corrected the citation year from 2025 to 2026 (RoGS editions are published the January after their final reference year, and this edition covers through 2024-25) |
| 16 | 2 | Bivariate choropleth | Map idiom #5 (Advanced, bonus) | AEDC state trends + NDIS Data Research + ABS Estimated Resident Population | Merges charts #3 and #13's two separate measures (developmental vulnerability % and NDIS autism rate per 1,000) into a single map, each state coloured by a precomputed 3×3 tercile-based bivariate class — ✅ built & rendered, `specs/16_bivariate_vulnerability_access_choropleth.vl.json`. **Added 2026-10-16** after an outside review flagged two risks: (1) the idiom count fell into D-band territory once the radar and heatmap were correctly downgraded to basic idioms, and (2) a strict marker could read charts #3 and #13 as the same choropleth idiom, capping the map-idiom score at 4% instead of 8%. This chart addresses both — it's a genuinely distinct idiom from a single-variable choropleth, and it makes the "NT is high-vulnerability but low-access" finding visible in one map instead of requiring a reader to compare two separate charts. Includes a 3×3 legend grid (built as a second small chart, `hconcat`-ed beside the map) since Vega-Lite has no native bivariate colour encoding — colour is precomputed per state in `data/processed/bivariate_vulnerability_access_state.csv` and passed through with `scale: null`. With only 8 states, terciles are coarse (roughly groups of 2-3), disclosed in the chart description, not hidden. **Click-highlight attempt (2026-10-17, now moot):** an earlier attempt to wire this chart into the then-existing chart #3 click-highlight hit a genuine compile-time error ("Undefined data set name: source_1") adding a point-selection param to this chart's multi-source layered structure, plausibly the same class of Vega-Lite layer-compositing fragility behind the earlier projection bug on this same chart — reverted rather than ship something broken. That whole click-highlight mechanism was later found to be non-functional on #3/#4/#13 as well (see note below) and removed from the page entirely on 2026-10-23, so this is no longer a relevant gap; chart #16 was never going to need it. Chart #16 works correctly and tells its story on its own. **Palette fixed (2026-10-21):** the original 3×3 grid used two separate hues (orange for vulnerability, green for access), which crossed into confusing brown/olive blends and put the chart's single most important distinction — "bad on both" vs "good on both" — on a red/green axis that's indistinguishable to colourblind readers (flagged by an outside reviewer). Replaced with a single-hue ramp (one warm clay hue throughout): vulnerability drives how dark/saturated a cell is, access modifies within that range, so low-vulnerability states always stay pale regardless of access and the one genuinely worst cell (high vulnerability, low access — NT) is unambiguously the darkest, most saturated colour on the map. No hue discrimination required anywhere, fixing both the colourblind-safety issue and the original "hard to parse" complaint in one change |

**Relevance fix (2026-09-18):** rows 2, 7, and 8 originally used AEDC
"developmental vulnerability" data (a general school-readiness screen, not
condition-specific — see caveat above). On review this made 6 of 10 charts
plus all 3 maps rest on a proxy measure rather than actual named conditions,
which is a weak fit for an assignment specifically about ADHD/autism/
learning disabilities. All 3 have been replaced with genuinely
condition-specific ABS data (schooling difficulties, disability groups,
co-occurring characteristics). **AEDC's footprint is now limited to the 3
required maps only** (rows 3, 4, 5) — unavoidable since AEDC is the only
source with any sub-national geography (see caveat section above for why).
Every other chart (1, 2, 6, 7, 8, 9, 10) now uses ABS/AIHW data that
measures autism, disability, or specific support needs directly.

**Idiom count — final (updated 2026-10-23, after the teaching team's
basic/advanced list and chart #17's addition):** the unit's teaching team
published an authoritative basic/advanced idiom list on the Ed forum
(2026-10-22 or earlier), which settles a few calls this doc had previously
guessed at. Per that list: **lollipop charts are explicitly advanced**
(chart #7 — an earlier version of this note had it wrong, counted as
basic), population pyramids are explicitly advanced (chart #6), stream
graphs are explicitly advanced (chart #12), and waffle/icon-array charts
are explicitly advanced (chart #9). Dot plots are explicitly basic
*excluding connected dot plots* — meaning chart #8 (a plain, unconnected
scatter/dot plot, confirmed earlier in this doc to be "really" a dot plot
rather than a genuine beeswarm) is basic, while chart #2's dumbbell (a
connected dot plot) is advanced. The list doesn't cover map idioms or
bullet charts at all — those sit in their own separate category, governed
by the brief's "≥3 map idioms" rule, not this basic/advanced list.

Non-map idioms: 5 confirmed basic (grouped bar #1, bar #11, dot plot #8,
single-line #14, multi-line #15), 5 confirmed advanced (connected dot
plot/dumbbell #2, population pyramid #6, lollipop #7, icon array #9,
streamgraph #12), plus bullet chart (#10), which isn't named on the
teaching team's list either way but doesn't resemble anything on the
basic list, so almost certainly counts as advanced too.

**Chart #5 removed (2026-10-21):** the small-multiples remoteness map was
mechanically the same idiom as chart #4 (LGA points sized/coloured by
vulnerability %), just faceted by remoteness band — a repeat, not a
distinct idiom, once reviewed honestly. Considered two replacements first
(a tile-grid cartogram, a hex-binned aggregate of the same 514 LGA points)
and rejected both: the tile-grid told the same story as chart #3's
choropleth but worse (NT's large landmass in the real map is not a
distortion worth correcting — NT genuinely has a small population on a
large landmass, so letting it dominate visually is honest, not misleading),
and the hex-bin would blur the same 514 named LGAs into unnamed regional
averages without revealing anything chart #4 doesn't already show.
Rather than force in a 6th map idiom the data didn't call for, chart #5
was cut outright and its one genuinely distinct finding (vulnerability
climbs from 22.5% in major cities to 35.8% in remote/very remote areas)
was folded into chart #4's caption as prose, so the insight survives
without the redundant idiom. Old spec kept in
`deprecated/specs/05_remoteness_small_multiples.vl.json`.

16 charts built and rendered total (10 required + 6 bonus), 5 of them maps
(10 required + 2 bonus) — see `specs/previews/` for PNG test renders.

**Map idioms — the real risk, now resolved (2026-10-23):** the teaching
team separately clarified on the Ed forum that "two choropleth maps count
as two charts but only one idiom" (same for two stream graphs, etc.) —
i.e. idiom identity is about mechanism, not what data is shown. Applying
that honestly to this project's 4 pre-existing maps: #3 (choropleth), #13
(choropleth), and #16 (bivariate choropleth) are all fundamentally "fill a
polygon by a colour derived from a value," the same underlying mechanism
— a strict marker could reasonably collapse all three into **one** idiom,
leaving only #4 (proportional symbol) as a second, genuinely distinct one.
That's 2 map idioms against the brief's explicit requirement of ≥3, which
caps "Idioms and Complexity" at 5% instead of 10% if true — a real,
quantified risk, not a hypothetical one. **Chart #17 (hex-bin map) was
built specifically to close this gap** — binning/aggregating points into a
regular grid is a mechanically distinct technique from both colour-fill-a-
polygon (choropleth family) and size/colour-a-point-at-its-real-location
(proportional symbol), so it holds up as a 3rd distinct map idiom even
under the strict "mechanism, not data" reading. See chart #17's own entry
below for how it was built (including two confirmed Vega-Lite bugs hit and
worked around along the way).

**Chart #16 (bivariate choropleth) was added earlier (2026-10-16) to
address an idiom-count risk**, before the teaching team's map-idiom
clarification existed — it merges #3 and #13's two measures into one map,
restoring an advanced idiom lost when the radar and heatmap were corrected
to basic ones. It remains a genuinely useful chart on its own merits (the
"NT is high-vulnerability AND low-access" finding it makes visible), but
per the map-idiom note above, it's no longer the project's answer to the
3rd-map-idiom question — chart #17 is. See row 16 below for the full
reasoning behind #16 itself.
**Chords/arc diagrams and ridge plots were considered and rejected** — no
source has genuine pairwise co-occurrence data (needed for a chord diagram)
or a continuous distribution (needed for a ridge plot); forcing either
would misrepresent the underlying discrete
categorical/marginal data.

**Relevance fix (2026-09-30):** three issues identified on review against
the assignment's actual content prompt ("diagnosis rates, service usage or
demographic characteristics across age groups or years" / "awareness and
access to support... over time"):
1. Charts #8 and (formerly) #11 used autism data not restricted to children.
   #11 has been swapped to a genuinely child-restricted table (see row 11
   above). #8 has no child-restricted autism-specific equivalent anywhere in
   our sources — a broader search confirmed ABS's SDAC product does not
   cross-tab autism-specific co-occurring types by child age band. Kept as
   national context, explicitly not framed as a children-only statistic.
2. **Resolved — a genuine multi-year support-access trend does exist.** An
   initial search across AEDC, ABS SDAC ×2, and AIHW Health/Education came
   up empty, but a broader search found it in Productivity Commission's
   Report on Government Services (ROGS) Table 15A.20: NDIS participants
   aged 0-14 as a % of the estimated eligible population, 2019-2023 (chart
   #14). Not neurodevelopmental-specific (it's disability-general), but a
   defensible proxy given autism/developmental delay dominate the NDIS 0-14
   cohort — clearly labelled as such in the chart description.
3. Added chart #13 (NDIS autism rate choropleth, a 4th bonus map) — the
   first genuinely condition-specific (not proxy) map in the set, and it
   surfaces a real, non-obvious contrast with the AEDC-based maps (see row
   13 above).

---

## Annotation copy (drafts, for the final page)

Text that will appear alongside each chart on the page itself — distinct
from the JSON spec's internal `description` field, which nobody visiting
the page ever sees. Add one entry per chart as copy is finalised.

**Chart #8 (co-occurring characteristics beeswarm):**
> These figures are for autistic Australians of all ages, not just
> children — no Australian data currently breaks this down by age for
> autism specifically. We include it because these co-occurring
> conditions typically emerge in childhood and tend to persist, so the
> pattern is still directly relevant to understanding autism in children.

---

## Important: data path convention (2026-09-30)

All 14 Vega-Lite specs' `data.url` fields are **page-relative** (e.g.
`data/processed/abs_autism_trend.csv`, no leading `../`), not
spec-relative. This is because vega-embed's browser loader resolves a
spec's internal relative URLs against the *page's* URL (`document.baseURI`),
not the spec file's own URL, even when the spec itself was loaded from a
subfolder via `vegaEmbed(selector, 'specs/foo.vl.json')`. This is
counter-intuitive and caused a real bug: charts loaded and rendered their
axes/scales but drew no data, because Vega silently swallows failed data
loads rather than throwing a visible error.

**Practical consequence for local testing:** `vl2png` (Node's file-based
loader) resolves relative paths differently, relative to the spec file's
own directory by default. To test locally with the corrected page-relative
paths, run vl2png with an explicit base directory flag from the repo root:
```
npx vega-lite2png -b . specs/06_autism_age_sex_pyramid.vl.json out.png
```
Omitting `-b .` will fail with an ENOENT error looking for
`specs/data/...` instead of `data/...`.

---

## Important: chart widths and `"width": "container"` (2026-10-21)

All 15 Vega-Lite specs were converted from arbitrary hardcoded pixel
widths (previously ranging 160–600px per chart, chosen independently per
spec) to `"width": "container"`, so every chart fills its `.chart-frame`
consistently rather than some charts (notably the maps) looking wider
than others for no real design reason. The 3 geo/map specs (03, 04, 13)
keep a fixed `height` tuned to the container's typical rendered width so
Australia's shape doesn't distort; the 3 facet/concat specs (06 pyramid,
09 icon array, 16 bivariate choropleth) use fixed per-sub-panel pixel
widths instead, since `"width": "container"` does not reliably resolve
inside Vega-Lite's `hconcat`/`facet` nesting.

**A critical bug was caught before this shipped:** `"width": "container"`
only works if the vega-embed target `<div>` has a real, explicit CSS
`width` *before* vega-embed measures it. The page's `.chart-frame` is
`display: flex; justify-content: center`, and its child div only had
`max-width: 100%` (no explicit `width`), which let it collapse to 0 width
in a flex row with no content yet — a circular dependency, since
vega-embed needs a real width to know how wide to draw `"width":
"container"`, but the div had no width until something was drawn into
it. Result: every non-facet/concat chart on the page rendered as a
literal empty 0×H SVG (`viewBox="0 0 0 H"`), i.e. **10 of 15 charts
invisible**, only caught by rendering the actual page in a real browser
(Playwright) — the headless Node `vl2png` CLI used to build the
specs/previews/ PNGs has no real flex layout engine and does not
reproduce this failure mode, so it rendered fine there and looked
"verified" without actually being tested in a browser. Fixed by changing
`.chart-frame > div { max-width: 100%; }` to `{ width: 100%; }`.
**Lesson: `vl2png` renders are not a substitute for testing the live page
in an actual browser when a change touches container-relative sizing or
flex/grid layout — static-file rendering and a real flex layout engine do
not fail the same way.**

A second bug from the same pass: `.prose p { max-width: 65ch; }` was
unintentionally capping `.chart-caption` and `.source-tag` width too
(since both are `<p>` tags nested inside `.prose`), making captions wrap
narrower than their own chart above them — the opposite sightline problem
from the width-unification's own stated goal. Fixed with `.prose
p:not(.chart-caption):not(.source-tag)`.

**A third bug found later (2026-10-23):** charts #6 and #9's fixed
per-sub-panel pixel widths (the two facet/concat specs that can't use
`"width": "container"`, see above) were tuned slightly too wide —
measured in a real browser at 719px and 714px respectively against a
718px `.chart-frame`, just enough to trigger `.chart-frame`'s
`overflow-x: auto` and show a horizontal scrollbar. Small (around
15–20px) and easy to miss at a glance, but inconsistent with every other
chart on the page (none of which scroll) and a real violation of the
brief's "full width visible... without horizontal scrolling"
requirement. Fixed by scaling both charts' sub-panel widths down by
roughly 5% (chart #6: 328→310px per panel; chart #9: outer facet
246→238px, inner icon-grid 153→148px, kept at the same ratio to each
other), verified via the live browser's `scrollWidth` vs `clientWidth`
comparison (not just a visual glance) to confirm zero overflow.

---

## Projection: Mercator → Albers (2026-10-23)

All 4 geo map specs (03, 04, 13, 16) switched from `{"type": "mercator"}`
to a custom-tuned Albers equal-area conic projection (`rotate: [-132, 0,
0]`, `center: [0, -27]`, `parallels: [-18, -36]`, chosen to centre and
frame Australia correctly). Mercator preserves local shape/angle but
distorts area, worse at higher latitudes — not a severe problem for
Australia specifically since the continent sits in a fairly narrow
mid-to-low latitude band, but Albers is the more textbook-correct choice
for any map where colour encodes a **rate** (all 4 of these charts do),
since a reader's eye also judges "how much area is this colour," and an
equal-area projection keeps that judgement honest. Verified all 4 render
undistorted in both the headless renderer and a real browser before
committing.

**Also fixed in the same pass:** chart #4 had `projection` declared
twice (once per layer — the geoshape base layer and the circle-mark
layer), the same duplicate-projection pattern that caused chart #16's
earlier label-rendering bug (a confirmed open Vega-Lite bug,
vega-lite#9321, around non-deterministic projection merging across
layers). Moved to a single shared `projection` at the parent level,
matching how #16 was already fixed.

**Cross-chart click highlight removed (2026-10-23):** a known bug was
found during verification — the chart #3 → #4/#13 cross-chart click
highlight did not actually work. Verified directly via the live Vega
view's `state_select` signal (not just visual inspection) — clicking a
state on chart #3 did not change `mapViews['chart04'].signal(
'state_select')` from `[]`, confirmed on both the pre-Albers (Mercator)
and post-Albers commits, so it was unrelated to the projection switch
and predates it. Root cause not investigated (plausibly the same class
of multi-view signal-propagation fragility as the earlier chart #16
layer-compositing bugs, but not confirmed). Rather than leave broken,
silently-dead interactivity code shipped on the page, the whole
mechanism was removed: the `state_select` selection param on #3 and #13,
the plain `state_select` param and `state_upper` calculate transform on
#4, the conditional `opacity`/`strokeWidth`/`stroke` encodings on all
three, and the `addSignalListener`/`mapViews` wiring in `index.html`.
Also removed the "Click a state to highlight it" line from #3's caption,
since it described a feature that no longer exists. All three maps keep
their static styling (plain white borders, 0.7 opacity on #4's dots) and
work correctly as standalone, non-interactive choropleth/proportional-
symbol maps — losing the cross-filter doesn't remove any chart or any
finding from the page, each map's own caption already states its own
story independently.

**Inconsistent map sizes fixed (2026-10-23):** charts #3, #4, #13, and
#16's map panel all drew Australia at visibly different sizes relative
to their frame — flagged on review by comparing two screenshots side by
side. Root cause: each map's `height` had been independently hand-tuned
against its *original pre-Albers* aspect ratio (03: 500:400 = 1.25, 04:
600:500 = 1.2, 13: 440:350 ≈ 1.257, 16's map sub-panel: 522:457 ≈ 1.142)
and never recalculated after the Mercator→Albers switch earlier in this
same session — so none of the four were using the actual, correct
aspect ratio for Australia under Albers, and naturally none matched each
other either. Measured the true ratio empirically by rendering the
TopoJSON at two different canvas sizes and taking the pixel bounding box
of the drawn shape (not the canvas) under Vega-Lite's default geo `fit`
behaviour: consistently ≈1.0825 (width/height) at both sizes tested.
Applied this one ratio to all 4 specs: `height: 664` for the three
`"width": "container"` maps (03, 04, 13, based on the container's
measured ~719px real rendered width), and `height: 482` for #16's map
sub-panel (width stays 522, since it intentionally shares space with the
legend grid beside it). Also removed a leftover `padding: {top:10,
left:5, right:5, bottom:5}` block on #13 that wasn't present on the
other three and was a secondary (smaller) source of its slightly
different scale. Verified by rendering all 4 in a real browser and
comparing side by side — Australia now reads at a consistent scale
across every map on the page.

**Legend clipping and remaining width inconsistency fixed (2026-10-23):**
even after the height fix above, charts #3 and #13's legend titles were
visibly cut off mid-word ("% developmentally vulnerabl[e]", "...per
1,000 people[]"), and the three `"width": "container"` maps (03, 04, 13)
still rendered at slightly different total widths. Root cause: each
chart's `color` legend had its own ad-hoc, inconsistent configuration —
#3 had no explicit `legend` block at all (pure Vega-Lite default
layout), #4 had `orient`/`direction` set but no `titleLimit`, #13 had a
`titleLimit: 140` that turned out too narrow for its title. Because
`"width": "container"` only governs the map's *plot area*, not the
legend sitting beside it, each chart's differently-sized legend added a
different amount of extra width on top of the same container width,
which is what made the three maps' total rendered widths diverge even
though their plot areas were now identical. Fixed by giving all three
maps the same explicit legend config (`orient: "right"`, `direction:
"vertical"`, `titleLimit: 160`, `gradientLength: 160`) and shortening
the two overlong titles to fit cleanly on 2 lines each (chart #13's
41-character 3-line title shortened to "NDIS autism rate (per 1,000)";
chart #3/#4's "% developmentally vulnerable" wrapped to 2 lines instead
of 1). Verified in a real browser — all three legends now render in
full with no clipping, and the three maps' total widths are
consistent.

**State abbreviation labels added to charts 3 and 13 (2026-10-23):** only
chart #16 (bivariate choropleth) had state abbreviation text labels
(NT, WA, QLD...) — flagged on review as an inconsistency, since #3 and
#13 are the same kind of single-variable choropleth and a reader
shouldn't need to already know Australia's state shapes by heart to read
them. Chart #4 (514 LGA dots) was deliberately left unlabelled — adding
8 state labels on top of an already-dense point map risked clutter
without much benefit, since dots there aren't grouped by state
visually. Added a small shared lookup file,
`data/processed/state_label_positions.csv` (state, abbr, and
approximate label lat/lon per state — the same coordinates already used
by chart #16, pulled out into their own reusable file rather than
duplicated), and replicated chart #16's existing two-layer label
pattern (a white-stroke halo text layer, then a solid dark-ink text
layer on top) on #3 and #13 so the same abbreviation reads legibly
against any background colour, light or dark. Both specs restructured
from a single `mark` into a `layer` array to add the text marks, with
`projection` kept at the shared parent level (not redeclared per layer)
to avoid the known Vega-Lite layer-projection bug documented earlier in
this file. Verified in a real browser — labels are legible against every
colour on both maps, no overlap with state borders or the legend.

---

## Chart #17: hex-bin map (added 2026-10-23)

A genuinely distinct 3rd map idiom was needed after the unit's teaching
team clarified (Ed forum, 2026-10-22) that "two choropleth maps count as
two charts but only one idiom" — applying that rule honestly, charts #3,
#13 and #16 (all colour-fill-a-polygon-by-value, same underlying
mechanism) risk collapsing to a single idiom under a strict marker,
leaving only choropleth + proportional-symbol (#4) as 2 confirmed
distinct map idioms against the brief's required 3 ("if less than three
maps are included, the maximum possible mark for 'Visualisation: Idioms
and Complexity' will be reduced from 10% to 5%" — a real, quantified risk,
not a hypothetical one).

**What it is:** the same 422 geocoded LGAs from chart #4, aggregated into
a regular hexagonal grid instead of shown as individual proportional
symbols or administrative polygons — mechanically a genuinely different
idiom (binning/aggregation, not per-feature display), matching the
unit's own advanced-idiom list's closest real-world equivalent (binned
spatial aggregation, as distinct from choropleth or proportional-symbol).
Each hexagon's colour is the sample-size-weighted average vulnerability %
across whichever LGAs fall in that cell.

**Why this took real engineering effort, not just a config change:**
Vega-Lite has no native hexbin transform (confirmed — the standard
workaround elsewhere is precomputing bin geometry in Python, same
approach already used for chart #16's bivariate colour). Two serious,
confirmed bugs were hit and diagnosed in sequence before landing on a
working approach:

1. **GeoJSON `property` field required.** Inline/URL-loaded GeoJSON
   `FeatureCollection`s need an explicit `"format": {"type": "json",
   "property": "features"}` for Vega-Lite to unpack individual Feature
   rows — without it, the whole collection loads as a single opaque
   datum and every `properties.X` field reference silently resolves to
   nothing (`"Infinite extent"` warning, blank chart, no hard error).
   Confirmed via `view.data('source_0')` inspection showing one row
   instead of many.

2. **Auto-fit breaks with many small separate polygons (the real
   blocker).** Even with the field-access bug fixed, every hexagon
   rendered as one shared, bizarre fan/annulus shape spanning the full
   canvas — confirmed via SVG path inspection to be ~191 separate,
   correctly-shaped `<path>` elements, but every single one sharing an
   identical, canvas-filling bounding box. Isolated down to a single
   hexagon alone (not a multi-feature interaction) and reproduced
   independently of file format (GeoJSON and hand-built TopoJSON both
   failed identically) — this is a genuine Vega-Lite/d3-geo limitation
   with automatic geo-`fit` on datasets of many small, separate polygon
   features, not a data or syntax mistake. No existing fix found via
   targeted search of Vega-Lite/d3-geo issue trackers and community
   threads.

**The actual fix:** bypassed Vega-Lite's geo-projection pipeline for this
layer entirely. Each LGA's lon/lat is pre-projected in Python using a
hand-implemented closed-form Albers equal-area conic projection formula
(matching d3-geo's exact `rotate`/`center`/`parallels` construction
already used by every other map on this page), verified against known
city locations (Sydney/Perth/Darwin/Melbourne/Hobart landing in
geographically correct screen positions) before trusting it. Hex-binning
then happens in on-screen pixel space (not lon/lat), which is also more
correct visually — binning in lon/lat space would produce visibly
stretched/non-regular hexagons once projected, since Albers isn't a
uniform-scale projection. The whole thing is a single script,
`scripts/build_hexbin.py`, run once to regenerate the data (not run at
page-load time). Each hexagon's 6 vertices (7 rows per bin, closing back
to the first point) are written to
`data/processed/aedc_lga_hexbins_px.csv` and drawn with a plain
`mark: "line"` (not `geoshape`) using ordinary `x`/`y` quantitative
encodings, `detail: bin_id` to group vertices into separate shapes, and
`order: order` to keep them in the right sequence — completely avoiding
the broken `geoshape`/auto-fit code path.

**Three more bugs found and fixed after the initial version shipped
(2026-10-23):**

1. **State outline dropped entirely, after a real misalignment was
   spotted on review.** The first version layered the hexagons over the
   usual `au_states.topo.json` outline for context, sharing one top-level
   `projection`. Compared side by side, hexagons visibly spilled into the
   ocean in several places (the Gulf of Carpentaria area, the southern
   coastline) — the state layer's own `geoshape` auto-fit and the
   hexagons' pre-baked pixel coordinates were computed against two
   different assumed canvas sizes (`"width": "container"`'s *actual*
   resolved width turned out to differ from the fixed 760px the hex data
   was built against) and drifted apart. Tried fixing the projection
   signal directly (`autosize: {"type": "none"}`) and confirmed it worked,
   but decided the outline wasn't worth the ongoing fragility it
   creates — it's pure decoration, not data, and the hexagon pattern by
   itself is already recognisably Australia-shaped. Dropped the outline
   layer and the geo-projection dependency entirely; the chart is now a
   single coordinate system with nothing else to drift out of sync with.
2. **Shape was upside-down and squashed after removing the outline.**
   Switching back to `"width": "container"` once there was no second
   layer to keep in sync caused the chart to stretch to whatever width
   the container resolved to, independent of the hex data's actual
   pixel extent — producing a wrong aspect ratio, and the y-axis defaults
   to increasing *upward* in Vega-Lite's quantitative scale convention,
   while the pre-computed pixel data increases *downward* (standard
   screen/SVG convention), so without an explicit `scale: {"reverse":
   true}` the whole map rendered flipped top-to-bottom. Fixed by going
   back to a fixed `width`/`height` matching the data's real measured
   extent (708×694, from the actual min/max of the x/y columns) and
   adding the explicit y-reversal.
3. **Pale pink filled cells visually indistinguishable from "no data"
   cells.** The empty-but-in-the-pattern hexagons (gaps directly
   adjacent to real data, drawn outlined but unfilled rather than left
   as a blank hole) were originally given a warm, near-background fill
   colour, which looked too similar to the palest end of the orange
   sequential scale at a glance. Fixed by using a neutral grey
   (`#dcdcdc`, matching the grey already used for chart #4's base map)
   instead — clearly outside the orange family, unambiguous. Also found
   and fixed a silent bug in the `has_data` flag itself: the Python
   script originally wrote `True`/`False` (Python's capitalisation),
   which Vega-Lite's boolean CSV parser doesn't recognise (it expects
   lowercase `true`/`false`), so every row was silently treated as
   truthy and no cell ever used the grey fallback at all — caught by
   inspecting the actual rendered SVG fill colours, not by a thrown
   error. Finally, added a small manual legend entry (a grey swatch + "No
   data" text, positioned as two extra layers past the plot's right
   edge) since Vega-Lite doesn't automatically generate a legend entry
   for a conditional encoding's static fallback value — without it, a
   reader had no on-chart explanation for what the grey cells meant.

125 occupied hexagons + 187 empty-but-adjacent hexagons from 422 LGA
points (a hex radius of 20px). Added as chart #17, right after chart #4
in the maps section, since it's a direct re-presentation of the same
LGA-level dataset through a different lens.

---

## Open decisions / things to amend

- [x] Radar chart confirmed feasible using raw Vega (not Vega-Lite) —
      adapted from https://vega.github.io/vega/examples/radar-chart/
- [x] LGA map built as a proportional symbol map instead of choropleth —
      used `HughParsonage/ABS-data` LGA centroid CSV (2016-vintage, joined by
      cleaned LGA name, 514/544 matched) rather than sourcing/simplifying LGA
      boundary polygons
- [x] Remoteness map built as a small-multiples proportional symbol map,
      using a Regional Australia Institute LGA-to-remoteness lookup PDF
      (extracted to `data/raw/rai/lga_remoteness.csv`, joined by LGA code,
      514/514 matched perfectly — better match rate than the name-based
      centroid join)
- [x] Population pyramid built and tested (`specs/06_autism_age_sex_pyramid.vl.json`)
- [x] Mosaic plot swapped for a two-panel icon array — no real sector×level
      cross-tab exists in the AIHW source, so a mosaic would need fabricated
      joint data (`specs/09_education_adjustment_icon_array.vl.json`)
- [x] Waffle chart swapped for a bullet chart — waffle would've duplicated
      chart #9's icon-array idiom; bullet chart is genuinely advanced and
      shows boys/girls against the "all children" reference line
      (`specs/10_schooling_restriction_bullet.vl.json`)
- [ ] Pick final annotation/callout text for each chart (storytelling +
      grammar is 5% of the rubric)
- [x] PHIDU LGA suppression handled via a filter transform on the
      proportional symbol map (missing dots, not blank polygons — this was
      the reason for choosing proportional symbols over a choropleth)
- [ ] Decide whether NDIS autism data earns a spot as an 11th chart or stays
      unused supplementary context
- [ ] Sketch (Week 7 studio requirement) needs to match this narrative once
      finalised — don't diverge after sketch approval without reason
