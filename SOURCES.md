# Data Sources

A running record of every data source used in this project, what was checked and ruled out, and why. Update this file whenever a source is added, dropped, or replaced with a cleaned extract.

Raw downloaded files live under `data/raw/<source>/`. The two PHIDU workbooks are 7–8MB each and are never shipped as-is in the final site: only the relevant sheets are extracted into small `data/processed/` CSVs, to stay under the assignment's "few MB total" budget.

**Status key:** ✅ confirmed usable and in use · 🟡 downloaded but not yet inspected in detail · 🔲 a candidate, not yet retrieved · ❌ ruled out

---

## 1. Australian Early Development Census (AEDC)

**Status: ✅.** Files: `data/raw/aedc/AEDC_state_trends_2009_2024.xlsx`, `AEDC_summary_indicators_domains.xlsx`, `AEDC_demographics_by_state.xlsx`, `AEDC_participation_by_state.xlsx`.

This is the national school-entry census of "developmental vulnerability" across five domains (physical, social, emotional, language/cognitive, communication), broken down by state/territory, remoteness category, and SEIFA quintile, across five census waves from 2009 to 2024. It's the only source in this project with any sub-national geography at all, which is why it carries all three required map idioms (state choropleth, LGA proportional symbols, remoteness small-multiples) plus the national trend chart.

Source: https://www.aedc.gov.au/data-hub/public-data/2024-aedc-results

## 2. ABS — Autism in Australia, 2022

**Status: ✅.** File: `data/raw/abs/AutismDC01.xlsx`. National only, by age group and sex, covering the 2015/2018/2022 SDAC cycles.

This file supplies the national autism trend chart (Table 1, chart #1), the age-by-sex population pyramid (Table 2, chart #6), the schooling difficulties/supports comparison between autistic and non-autistic children with disability (Table 4, chart #2), and the co-occurring disability types chart (Table 3, chart #8 — not age-restricted to children, which is disclosed on the page). Two more genuine cross-tabs sit in this file unused — Table 8 (frequency of need for assistance by activity type) and Table 10 (formal/informal provider of assistance by activity type) — worth revisiting if more charts are wanted later.

Processed extracts: `data/processed/abs_autism_trend.csv`, `abs_autism_age_sex.csv`, `abs_autism_schooling_support.csv`, `abs_autism_cooccurring.csv`.

Source: https://www.abs.gov.au/articles/autism-australia-2022

## 3. ABS — Children and Young People with Disability, 2022

**Status: ✅.** File: `data/raw/abs/ChildrenDisability2022.xlsx`. National only, ages 0–24, by disability status and sex, 2015/2018/2022.

Table 3 gives the disability-group breakdown used in chart #7 (% of children aged 0-14 with each disability group — Sensory & speech, Learning & understanding, Physical, Psychosocial, Head injury/ABI, Other), and Table 4 gives the assistance-needed-vs-received breakdown used in chart #11 (support needs not fully met, children aged 0-14).

Processed extracts: `data/processed/abs_disability_groups_0_14.csv`, `abs_children_unmet_need_0_14.csv`.

Source: https://www.abs.gov.au/articles/children-and-young-people-disability-2022

## 4. PHIDU — Social Health Atlas, Child and Youth (Torrens University)

**Status: ✅,** though the raw workbooks are kept locally only and never shipped. Files: `data/raw/phidu/phidu_child_youth_lga.xlsx` (7.5MB) and `phidu_child_youth_phn_lga_parts.xlsx` (8.7MB).

The sheet that matters here is `Early_childhood_development`, which republishes the AEDC vulnerability indicator at LGA level for 2024 — the only source found with finer-than-state geography for this measure. About 19% of the 544 LGAs have suppressed values due to small-area counts; these are treated as nulls (greyed out or excluded), never as zero. The workbook also has an ABS Census 2021 `Disability` sheet and a `Census_health_condition` sheet, kept as context but not used directly.

Processed extract: `data/processed/aedc_lga_2024.csv` (52KB, 544 LGAs across 8 states/territories).

Source: https://phidu.torrens.edu.au/social-health-atlases/data (Child and Youth Atlas)

## 5. NDIS Data Research — Autism Participant Dashboard

**Status: ✅.** File: `data/raw/ndis/ndis_autism_data_dec2024.xlsx`, sheet `7_State`. State/territory only, as at 31 December 2024.

This is the only genuinely autism-specific (not a proxy) source with any geography, and it powers chart #13. The raw sheet gives participant counts and a "% share of all NDIS participants" figure, but that share reflects each state's overall NDIS caseload mix rather than autism prevalence, so it was rejected as a mapping variable. Instead, participant counts were divided by ABS population estimates (source 6 below) to get a genuine rate per 1,000 people. That rate produces a strikingly different pattern from the AEDC maps: South Australia is highest at 13.6 per 1,000, and the Northern Territory is lowest at 5.9 per 1,000 — the opposite of the NT's position on AEDC vulnerability, suggesting under-diagnosis or under-service in remote areas rather than genuinely lower prevalence. Chart #16 (the bivariate choropleth) makes this contrast visible directly on one map.

Processed extract: `data/processed/ndis_autism_rate_by_state.csv` (keeps the raw counts, population denominator, and derived rate together for transparency).

Source: https://dataresearch.ndis.gov.au/reports-and-analyses/participant-dashboards/autism

## 6. ABS — National, State and Territory Population, December 2024

**Status: ✅,** used purely as a population denominator for chart #13's per-capita rate (and, by extension, chart #16). The reference date (31 December 2024) is an exact match to the NDIS snapshot above.

Source: https://www.abs.gov.au/statistics/people/population/national-state-and-territory-population/dec-2024

## 7. AIHW — Australia's Children, 2022 Update

**Status: ✅.** Files: `data/raw/aihw/aihw_CWS_69_Health_2022.xlsx` (47 sheets) and `aihw_CWS_69_Education_2022.xlsx` (17 sheets). National only, mostly 2018–2021 with some series back to 2003.

The Health workbook's "Children with disability" tables (25–28) cover prevalence by disability status, sex and age, and whether children aged 5–14 have a schooling restriction (chart #10). Table 27 specifically — disability groups by age band (0-4/5-9/10-14) — is a genuine cross-tab, used for the streamgraph in chart #12 to show diagnosis lag by disability type. The Education workbook's Tables 10–11 (educational adjustment by school sector and by adjustment level) power the icon array in chart #9.

Processed extract: `data/processed/aihw_disability_by_age.csv` (plus `aihw_education_adjustment.csv` and `aihw_schooling_restriction.csv`).

Source: https://www.aihw.gov.au/reports/children-youth/australias-children/data

## 8. HughParsonage/ABS-data — LGA Centroid Coordinates

**Status: ✅.** This isn't a government source but a community-maintained GitHub repository of LGA centroid coordinates, used to place the dots on chart #4's proportional symbol map. The coordinates are 2016-vintage LGA boundaries, joined against the 2024 AEDC data by cleaned LGA name (stripping trailing qualifiers like "(C)" or a state abbreviation). 514 of 544 LGAs matched (95%); the rest are mostly LGAs renamed or amalgamated since 2016, or ambiguous same-name LGAs across different states.

Source: https://raw.githubusercontent.com/HughParsonage/ABS-data/master/LGA_NAME-LGA_CODE-latlon-gpolatlon.csv

## 9. Regional Australia Institute — LGA to Remoteness Classification

**Status: ✅,** extracted from a PDF into `data/raw/rai/lga_remoteness.csv`. ABS doesn't publish a direct LGA-to-Remoteness-Area correspondence file (only LGA-to-LGA and RA-to-RA vintage updates), so this third-party-compiled lookup was the practical path to a clean, single-category remoteness classification (Major Cities / Inner Regional / Outer Regional / Remote / Very Remote) per LGA. It joins by LGA code directly, matching all 514 of the real LGAs in the AEDC data, and powers the remoteness small-multiples map (chart #5).

Source: https://regionalaustralia.org.au/common/Uploaded%20files/Files/2024/Good%20Life%20Guide/LGAs%20to%20RAI%20and%20ABS%20Classifications.pdf

## 10. Productivity Commission — Report on Government Services (ROGS) 2026

**Status: ✅.** File: `data/raw/rogs/rogs15.csv` (2.4MB; only a small slice of the full "Services for people with disability" section is actually used). State/territory and national totals, 2019–2025.

Two tables from this large dataset close the "access to support over time" gap in the narrative, found only after a broad search confirmed none of AEDC, ABS, AIHW or NDIS's own dashboard has any multi-year service-usage series. Table 15A.20 gives NDIS participants aged 0-14 as a share of the estimated eligible population, 2019–2023 (chart #14) — disability-general rather than neurodevelopmental-specific, but a defensible proxy given how much of the NDIS 0-14 population is there for autism or developmental delay. The series genuinely stops at 2023 because the source stops publishing that specific metric for this age band after that year — 2024 and 2025 only report a "rate per 1,000 people" instead, a differently-scaled figure, not the "% of potential population" used in the chart. Table 15A.45 gives first-plan approval wait times (median and 90th percentile) for young children, with two honest quirks disclosed on the page rather than hidden: 2023-24 is genuinely missing from the source itself (the PC's own footnote attributes this to the NDIA's transition to a new information system that year), and the tracked age band shifts from "0-6" to "0-8" in the final year.

One build note worth keeping: the empty 2023-24 cells were initially silently coerced to zero by Vega-Lite's default CSV parsing, which would have drawn a false dip in the line. Fixed with an explicit `format.parse` directive so the gap renders as a real break instead.

**Verified against the live source (2026-10-23):** re-checked both tables directly against the PC's current published data (`assets.pc.gov.au/2026-01/rogs-2026-partf-section15-disability-services-data-tables.xlsx`) and separately against the already-downloaded `rogs15.csv` — every value used on the page matches the source exactly, and the 2023-24 gap in Table 15A.45 is confirmed "na" for every state/territory and both percentile measures, not an artifact of local processing.

The same file also has Table 15A.6 (NDIS participants by primary disability type including autism, 2019–2025, all ages) and Table 15A.44 (a second wait-time measure, only populated for 2024-25) — both checked and set aside for now.

Processed extracts: `data/processed/ndis_children_access_trend.csv`, `ndis_wait_time_trend_long.csv`.

Source: https://www.pc.gov.au/ongoing/report-on-government-services/2025/community-services/services-for-people-with-disability

## 11. Derived — Bivariate Vulnerability/Access Classification

**Status: ✅,** computed rather than sourced externally. Chart #16 combines two already-documented sources — AEDC state vulnerability (source 1) and NDIS autism access rate (source 5) — by ranking each of the 8 states/territories independently into thirds (low/mid/high) on each measure, then assigning one of nine bivariate classes. With only 8 data points the thirds are coarse, landing in groups of roughly two or three; this is disclosed directly in the chart's own description rather than left implicit.

Processed extracts: `data/processed/bivariate_vulnerability_access_state.csv` (per-state class and precomputed colour) and `bivariate_legend_grid.csv` (the nine legend cells). See NARRATIVE.md's entry for chart #16 for the full reasoning behind adding this chart.

---

## Sources checked and ruled out

**Atlas of Healthcare Variation — ADHD medicines dispensing (≤17 years) by PHN.** The page is no longer live; the Commission's current "Atlas Focus Reports" list covers five other topics (antipsychotics, COPD, colonoscopy, heavy menstrual bleeding, opioids) and the old Third Atlas 2018 ADHD page is dead. A nearby substitute — "Antipsychotic medicines dispensing, 65 years and over" — was checked and rejected: wrong age group (elderly, not children) and wrong drug class entirely. No PHN-level ADHD-specific dataset is currently available anywhere; PHIDU remains the only source of finer-than-state geography in this project.

**APSC Neurodiversity in the APS Workforce.** Covers adult public servants, not children. Not relevant.

**ABC News / Four Corners — ADHD diagnosis rates.** Covers adults aged 20–64, and the underlying PBS/PLIDA analysis is a custom UNSW study with no public raw data download.

**data.gov.au.** Checked directly; it only re-links to the ABS/AIHW/AEDC sources already listed above, nothing additional.

**Longitudinal Study of Australian Children (LSAC).** Not evaluated in depth — it's microdata requiring an application/registration process, likely too heavy a lift for this assignment's scope.

---

## Open items

- Delete or gitignore the oversized raw PHIDU workbooks once the final source list is fully locked in, keeping only the processed extracts in the repository.
