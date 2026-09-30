# Data Sources Tracker

Working list of data sources for the FIT3179 Data Visualisation 2 assignment
(neurodevelopmental conditions in Australian children). Update this file as
sources are added, dropped, or replaced with cleaned extracts.

Raw downloaded files live in `data/raw/<source>/`. **Note:** the two PHIDU
workbooks are 7–8MB each and must NOT be shipped as-is in the final site —
extract only the relevant sheet(s) into a small `data/processed/` CSV before
using them in any chart, to stay under the assignment's "few MB total" budget.

---

## Status legend
- ✅ Confirmed usable, downloaded, inspected
- 🟡 Downloaded, not yet inspected in detail
- 🔲 Candidate, not yet retrieved
- ❌ Ruled out / blocked

---

## Sources

### 1. AEDC — Australian Early Development Census
- **Status:** ✅
- **Files:** `data/raw/aedc/AEDC_state_trends_2009_2024.xlsx`,
  `AEDC_summary_indicators_domains.xlsx`, `AEDC_demographics_by_state.xlsx`,
  `AEDC_participation_by_state.xlsx`
- **Geography:** State/territory; also remoteness category (Major
  Cities/Regional/Remote) and SEIFA quintile in `summary_indicators_domains`
- **Years:** 2009–2024 (5 census waves)
- **Key indicator:** % of children "developmentally vulnerable" on one or
  more of 5 domains (physical, social, emotional, language/cognitive,
  communication)
- **Source URL:** https://www.aedc.gov.au/data-hub/public-data/2024-aedc-results
- **Use:** state choropleth + remoteness-category map/small-multiples + time
  trend chart

### 2. ABS — Autism in Australia, 2022
- **Status:** ✅
- **File:** `data/raw/abs/AutismDC01.xlsx`
- **Geography:** National only, by age group and sex
- **Years:** 2015, 2018, 2022 (SDAC cycles)
- **Source URL:** https://www.abs.gov.au/articles/autism-australia-2022
- **Use:** national trend chart (Table 1, chart #1), population pyramid
  (Table 2, chart #6), schooling difficulties/supports comparison (Table 4,
  chart #2 — autistic vs non-autistic children with disability), co-occurring
  disability types (Table 3, chart #8 — note: not age-restricted to
  children), unmet support needs by activity type (Table 9, chart #11 —
  genuine 2-variable cross-tab, note: not age-restricted to children)
- **Processed extracts:** `data/processed/abs_autism_trend.csv`,
  `abs_autism_age_sex.csv`, `abs_autism_schooling_support.csv`,
  `abs_autism_cooccurring.csv`, `abs_autism_unmet_need.csv`
- **Other real cross-tabs found in this file, not yet used:** Table 8
  (frequency of need for assistance × activity type), Table 10 (provider of
  assistance — formal/informal × activity type) — potential future chart
  material if more idioms are wanted later

### 3. ABS — Children and young people with disability, 2022
- **Status:** ✅
- **File:** `data/raw/abs/ChildrenDisability2022.xlsx`
- **Geography:** National only, ages 0–24, by disability status/sex
- **Years:** 2015, 2018, 2022
- **Source URL:** https://www.abs.gov.au/articles/children-and-young-people-disability-2022
- **Use:** disability group radar chart (Table 3, chart #7 — % of children
  0-14 with each disability group: Sensory & speech, Learning &
  understanding, Physical, Psychosocial, Head injury/ABI, Other)
- **Processed extract:** `data/processed/abs_disability_groups_0_14.csv`

### 4. PHIDU — Social Health Atlas, Child and Youth (Torrens University)
- **Status:** ✅ downloaded, 🟡 not yet extracted to a clean subset
- **Files:** `data/raw/phidu/phidu_child_youth_lga.xlsx` (7.5MB),
  `phidu_child_youth_phn_lga_parts.xlsx` (8.7MB) — **raw only, too large to
  ship**
- **Relevant sheet:** `Early_childhood_development` — AEDC vulnerability
  indicator at **LGA level**, 2024
- **Also present:** `Disability` sheet (ABS Census 2021, need-for-assistance
  by age 0–24, LGA), `Census_health_condition` (LGA-level mental health
  condition prevalence, 2021) — supporting/context data only
- **Source URL:** https://phidu.torrens.edu.au/social-health-atlases/data (Child and Youth Atlas)
- **Use:** LGA-level map — finer geography than AEDC's state data, same
  underlying indicator.
- **Processed extract:** `data/processed/aedc_lga_2024.csv` (52KB, 544 LGAs
  across 8 states/territories). Columns: `lga_code`, `lga_name`, `state`,
  and count/valid-n/% for vulnerable-on-1+-domains, vulnerable-on-2+-domains,
  and on-track-on-all-5-domains. ~19% of LGAs have suppressed values (blank
  cells) due to small-area counts — handle nulls in the map (grey out or
  exclude, don't treat as zero).

### 5. NDIS Data Research — Autism participant dashboard
- **Status:** ✅ downloaded and used (chart #13)
- **File:** `data/raw/ndis/ndis_autism_data_dec2024.xlsx`, sheet `7_State`
- **Geography:** State/territory only (no SA3/SA4 breakdown by disability
  type despite site's rollout-metric pages mentioning SA3/SA4 — that's
  participation rate, not disability type)
- **Years:** as at 31 December 2024
- **Source URL:** https://dataresearch.ndis.gov.au/reports-and-analyses/participant-dashboards/autism
- **Use:** chart #13, a 4th (bonus) map — genuinely autism-specific state
  choropleth of NDIS autism participants per 1,000 population. Raw sheet
  only gives participant counts and "% share of all NDIS participants"
  (the latter reflects scheme caseload mix, not prevalence, so it was
  rejected as misleading for a map). Computed a real per-capita rate instead
  by dividing by ABS Estimated Resident Population (see #12 below) — this
  produces a genuinely different pattern from the AEDC maps (SA highest at
  13.6 per 1,000, NT lowest at 5.9 per 1,000), worth calling out explicitly:
  NT's high AEDC vulnerability doesn't translate into high NDIS autism
  access, suggesting possible under-diagnosis/under-service in remote areas
  rather than lower actual prevalence
- **Processed extract:** `data/processed/ndis_autism_rate_by_state.csv`
  (includes raw participant counts, population denominator, and derived
  rate, all in one file for transparency/reproducibility)

### 12. ABS — National, state and territory population, December 2024
- **Status:** ✅ used as population denominator for chart #13
- **Years:** 31 December 2024 (exact date match to the NDIS snapshot)
- **Source URL:** https://www.abs.gov.au/statistics/people/population/national-state-and-territory-population/dec-2024
- **Use:** population by state/territory, used to convert NDIS autism
  participant counts into a genuine per-capita rate (per 1,000 population)

### 6. Atlas of Healthcare Variation — ADHD medicines dispensing (≤17 yrs) by PHN
- **Status:** ❌ ruled out — page no longer accessible. The Commission's
  current "Atlas Focus Reports" list only has 5 actively maintained topics
  (Antipsychotic medicines dispensing, COPD, Colonoscopy, Heavy menstrual
  bleeding, Opioid medicines dispensing) — ADHD is not among them and the old
  Third Atlas 2018 §5.6 ADHD page/data file is dead.
- Checked and rejected substitute: "Antipsychotic medicines dispensing,
  65 years and over, 2016–17 to 2020–21" — wrong age group (elderly, not
  children) and wrong drug class (antipsychotics ≠ ADHD stimulant medicines).
  Not usable even as a proxy.
- **Conclusion:** no PHN-level ADHD-specific dataset currently available.
  PHIDU (#4) is now the sole source for a finer-than-state map idiom.

### 7. APSC Neurodiversity in the APS workforce
- **Status:** ❌ ruled out — adult public servants only, not children
- **Source URL:** https://www.apsc.gov.au/initiatives-and-programs/workforce-information/research-analysis-and-publications/state-service/state-service-report-2024-25/aps-workforce/diversity-aps-workforce

### 8. ABC News / Four Corners — ADHD diagnosis rates
- **Status:** ❌ ruled out — covers adults (20–64), not children; underlying
  PBS/PLIDA analysis is custom (UNSW), no public raw download
- **Source URL:** https://www.abc.net.au/news/2026-04-20/adhd-diagnosis-rates-adults-australia-data-four-corners/106557646

### 9. data.gov.au
- **Status:** ❌ checked — no standalone dataset found beyond re-links to
  ABS/AIHW/AEDC already listed above

### 10. AIHW — Australia's Children 2022 update, data tables
- **Status:** ✅ downloaded (Health + Education domains)
- **Files:** `data/raw/aihw/aihw_CWS_69_Health_2022.xlsx` (47 sheets),
  `aihw_CWS_69_Education_2022.xlsx` (17 sheets)
- **Geography:** National only
- **Years:** mostly 2018–2021, some series back to 2003
- **Relevant tables (Health):** Table 25–28 "Children with disability" —
  prevalence by disability status/sex/age (2003–2018), disability groups,
  and whether children aged 5–14 have a schooling restriction. Table 27
  (disability groups by age band 0-4/5-9/10-14, chart #12) is a genuine
  cross-tab used for a streamgraph showing diagnosis lag by disability type
- **Processed extract:** `data/processed/aihw_disability_by_age.csv`
- **Relevant tables (Education):** Table 10–11 "School students who received
  an educational adjustment due to disability" — by school sector and level
  of adjustment, 2020 — good proxy for learning-disability support/service
  usage in schools
- **Source URL:** https://www.aihw.gov.au/reports/children-youth/australias-children/data
- **Use:** supporting national-level charts (disability prevalence trend,
  schooling impact, educational adjustment by sector) — not map-eligible
  (national only)

### 11. HughParsonage/ABS-data — LGA centroid coordinates
- **Status:** ✅ downloaded and joined
- **File:** raw source not kept (downloaded directly into
  `data/processed/aedc_lga_2024_with_centroids.csv`)
- **Content:** lat/lon centroid per LGA, 2016 LGA vintage, 544 rows
- **Join method:** matched by cleaned LGA name (stripped trailing
  "(C)"/"(A)"/state qualifiers) against `aedc_lga_2024.csv` — 514/544
  matched (95%); unmatched are mostly LGAs renamed/amalgamated since 2016 or
  ambiguous same-name LGAs across states (e.g. "Campbelltown (NSW)" vs "(SA)")
- **Source URL:** https://raw.githubusercontent.com/HughParsonage/ABS-data/master/LGA_NAME-LGA_CODE-latlon-gpolatlon.csv
- **Use:** enables the LGA proportional symbol map (map idiom #2)

### 12. Regional Australia Institute — LGA to remoteness classification
- **Status:** ✅ downloaded (as PDF) and extracted to CSV
- **File:** `data/raw/rai/lga_remoteness.csv` (565 rows incl. non-geographic
  pseudo-LGA codes; 514 real LGAs matched by code against AEDC data)
- **Content:** one dominant ABS Remoteness Area classification (Major
  Cities/Inner Regional/Outer Regional/Remote/Very Remote) per LGA code —
  clean single-category lookup, not a proportional/population-weighted split
- **Join method:** matched by LGA code directly — 514/514 matched (100%),
  better than the name-based centroid join
- **Source URL:** https://regionalaustralia.org.au/common/Uploaded%20files/Files/2024/Good%20Life%20Guide/LGAs%20to%20RAI%20and%20ABS%20Classifications.pdf
- **Use:** enables the remoteness small-multiples map (map idiom #3). Note:
  ABS does not publish a direct LGA-to-Remoteness-Area correspondence CSV
  (only LGA-to-LGA and RA-to-RA vintage-update files), so this
  third-party-compiled lookup was the practical path

### 11. Longitudinal Study of Australian Children (LSAC)
- **Status:** 🔲 not evaluated — microdata, likely requires application/
  registration for access, probably too heavy a lift for this assignment
- **Source URL:** https://dataverse.ada.edu.au/dataset.xhtml?persistentId=doi:10.26193/XMLCQP

### 13. Productivity Commission — Report on Government Services (ROGS) 2025
- **Status:** ✅ downloaded and used (chart #14)
- **File:** `data/raw/rogs/rogs15.csv` (2.4MB, Part F Section 15 "Services
  for people with disability," full dataset — only a small slice used)
- **Geography:** State/territory + national totals
- **Years:** 2019–2025 (age-band categories vary by year; "0-14 years old"
  is the consistent category across the full range)
- **Table used:** 15A.20 "Service use by selected equity groups" — NDIS
  participants aged 0-14 as a % of the estimated eligible population,
  2019-2023 (2024-2025 switch to a different metric, "rate per 1,000," not
  directly comparable, so excluded from the trend chart)
- **Source URL:** https://www.pc.gov.au/ongoing/report-on-government-services/2025/community-services/services-for-people-with-disability
- **Use:** this closes the "access to support over time" gap identified on
  2026-09-30 — found via a broader search after AEDC/ABS/AIHW/NDIS's own
  autism dashboard were all confirmed to have no multi-year service-usage
  series. Disability-general, not neurodevelopmental-specific, but a
  defensible proxy for this age group (see NARRATIVE.md relevance fix)
- **Processed extract:** `data/processed/ndis_children_access_trend.csv`
- **Note:** this same file also has Table 15A.6 (NDIS participants by
  primary disability type, incl. autism, 2019-2025, all ages, not
  child-restricted) and Table 15A.44/45 (NDIS waiting times by age band,
  currently only 2024-25 populated) — not currently used but worth
  revisiting if more charts are wanted later

---

## Open questions / next steps
- [x] Atlas of Healthcare Variation PHN-level ADHD file — ruled out, page gone, no viable substitute
- [x] Extract `Early_childhood_development` sheet from PHIDU LGA workbook into a small clean CSV — done, `data/processed/aedc_lga_2024.csv`
- [ ] Decide final map idiom set (3 required) once LGA data quality is confirmed
- [x] Check AIHW Australia's Children data tables — done, Health + Education domains downloaded
- [ ] Once final source list is locked, delete/gitignore oversized raw PHIDU files, keep only processed extracts in the repo
