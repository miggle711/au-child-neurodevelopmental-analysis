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
| 1 | 1 | Stacked area chart | Basic | ABS Autism in Australia 2022 | Autism prevalence in Australian children, 2015/2018/2022 (national only) — ✅ built & rendered, `specs/01_autism_trend_area.vl.json` |
| 2 | 1 | Dumbbell / connected dot plot | Advanced | ABS Autism in Australia 2022 (Table 4, national only) | Schooling difficulties/supports, autistic vs. non-autistic children with disability aged 5-20 (attends special classes, needs day off, has difficulty, uses assistance) — ✅ built & rendered, `specs/02_autism_schooling_dumbbell.vl.json`. **Replaced AEDC national trend** — this is genuinely condition-specific service-usage data instead of a general vulnerability proxy |
| 3 | 2 | Choropleth map | Map idiom #1 (Advanced) | AEDC state trends | Developmental vulnerability % by state/territory (AEDC, general screening measure) — ✅ built & rendered, `specs/03_state_choropleth.vl.json`. NT stands out sharply (40.8% vs next-highest 25.9%) |
| 4 | 2 | Proportional symbol map | Map idiom #2 (Advanced) | PHIDU LGA data + HughParsonage/ABS-data centroids | Developmental vulnerability % by LGA (514 of 544 LGAs matched by name to 2016-vintage centroids) — reveals within-state hotspots. ✅ built & rendered, `specs/04_lga_proportional_symbol.vl.json`. Swapped from choropleth to proportional-symbol: no small ready-made LGA boundary TopoJSON with matching codes exists, and a full 544-polygon choropleth would look noisy/patchy given ~19% suppressed LGAs |
| 5 | 2 | Small-multiples map by remoteness area | Map idiom #3 (Advanced) | AEDC LGA data + Regional Australia Institute LGA-to-remoteness lookup | 5-panel map (Major Cities/Inner Regional/Outer Regional/Remote/Very Remote), each showing LGA points colored+sized by developmental vulnerability % — ✅ built & rendered, `specs/05_remoteness_small_multiples.vl.json`. Strong visual gradient: Very Remote panel clusters in central/northern Australia with darkest, largest circles (up to 83% in Central Desert, NT) |
| 6 | 3 | Population pyramid | Advanced | ABS AutismDC01 (national only) | Autistic children by age group (0-4, 5-14, 15-24) × sex — ✅ built & rendered, `specs/06_autism_age_sex_pyramid.vl.json`. Shows males diagnosed at ~2-3x the rate of females across all age bands |
| 7 | 3 | Radar chart (raw Vega) | Advanced | ABS Children and Young People with Disability 2022 (Table 3, national only) | % of children aged 0-14 with each disability group (Sensory & speech, Learning & understanding, Physical, Psychosocial, Head injury/ABI, Other) — ✅ built & rendered, `specs/07_disability_groups_radar.vg.json`. **Replaced AEDC 5-domain version** — this shows genuine condition-adjacent disability groups instead of general developmental screening domains. "Learning and understanding" (6.5%) is the largest slice |
| 8 | 3 | Beeswarm / jittered dot plot | Advanced | ABS Autism in Australia 2022 (Table 3, national, all ages not child-restricted) | Co-occurring characteristics among autistic Australians (e.g. "slow at learning" 71.4%, social/behavioural difficulties 62.4%, mental illness 52.5%) — ✅ built & rendered, `specs/08_autism_cooccurring_beeswarm.vl.json`. **Replaced AEDC SEIFA gradient** — shows autism rarely occurs in isolation. Note: source table isn't age-restricted to children, flag this in chart copy |
| 9 | 4 | Icon array (two panels) | Advanced | AIHW Education (Table 10–11, national only) | % of students receiving an educational adjustment for disability, by school sector and separately by adjustment level — ✅ built & rendered, `specs/09_education_adjustment_icon_array.vl.json`. Swapped from mosaic plot: Tables 10 & 11 are two separate 1-variable breakdowns, not a real sector×level cross-tab, so a mosaic would require fabricating joint data (against the brief's "no fabricated data" rule) |
| 10 | 4 | Bullet chart | Advanced | AIHW Health (Table 28, national only) | % of children aged 5-14 with disability who have a schooling restriction — overall (7.8%) vs boys (9.9%) vs girls (5.6%), each measured against the "all children" reference line — ✅ built & rendered, `specs/10_schooling_restriction_bullet.vl.json`. Swapped from waffle chart (same idiom family as #9, would've been repetitive) and from a plain bar chart (basic, not advanced) |
| 11 | 4 | Heatmap (2-column, independent color scales) | Advanced, bonus | ABS Autism in Australia 2022 (Table 9, national, all ages not child-restricted) | % of autistic people's support needs fully met vs. not fully met, by activity type — ✅ built & rendered, `specs/11_autism_unmet_need_heatmap.vl.json`. Genuine 2-variable cross-tab (the real thing a mosaic plot needed but chart #9's source data didn't have). Strong finding: physical/practical needs (health care 78%, self-care 76%) are well met, but needs tied most directly to autism itself — communication (43% unmet) and cognitive/emotional tasks (47% unmet) — are the least met. This is an **11th, bonus chart** (10 is the minimum); keep it unless it makes the page too long, in which case #9 is the more replaceable/weaker of the two icon-array-family charts |
| 12 | 3 | Streamgraph | Advanced, bonus | AIHW Health (Table 27, national only, 2018) | % of children with each disability group (Intellectual, Sensory & speech, Psychosocial, Physical restriction, Other), by age band 0-4/5-9/10-14 — ✅ built & rendered, `specs/12_disability_by_age_streamgraph.vl.json`. Checked as a ridge-plot candidate first but rejected — the underlying data is discrete categorical %, not a continuous distribution, so a ridge plot would misrepresent its shape. Streamgraph instead directly visualises diagnosis lag: "Intellectual" disability balloons from 1.1% (age 0-4) to 6.9% (age 10-14), while "Sensory and speech" narrows over the same span. This is a **12th, bonus chart** |

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

**Idiom count — final:** 1 basic (stacked area chart), 11 advanced (dumbbell,
choropleth, proportional symbol map, small-multiples map, population
pyramid, radar chart, beeswarm, icon array, bullet chart, heatmap,
streamgraph). 12 charts built and rendered total (10 required + 2 bonus) —
see `specs/previews/` for PNG test renders. Comfortably clears the rubric's
"≥8 idioms incl. 5-8 advanced" for HD range, and now much more directly
answers the assignment's actual prompt. **Chords/arc diagrams and ridge
plots were considered and rejected** — no source has genuine pairwise
co-occurrence data (needed for a chord diagram) or a continuous distribution
(needed for a ridge plot); forcing either would misrepresent the underlying
discrete categorical/marginal data.

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
