# Deprecated

This folder holds earlier chart specs that were replaced during development. They are kept for reference only and are not part of the final visualisation.

`02_national_trend_slope.vl.json` was the original version of chart 2. It used AEDC's general developmental vulnerability measure instead of data specific to autism or ADHD, so it was replaced by `02_autism_schooling_dumbbell.vl.json`, which draws on genuine condition specific data. See NARRATIVE.md for the full reasoning behind that change.

`07_domains_radar.vg.json` had the same problem and was replaced by `07_disability_groups_radar.vg.json`.

`07_domains_comparison_lollipop.vl.json` was an earlier attempt at the same chart, built as a stand in before we confirmed a proper radar chart was feasible in raw Vega.

`08_seifa_gradient_multiline.vl.json` was replaced by `08_autism_cooccurring_beeswarm.vl.json` for the same reason as chart 2 and chart 7.

`10_schooling_restriction_callout.vl.json` turned out to be a plain bar chart once built, which counts as a basic idiom rather than an advanced one, so it was replaced by `10_schooling_restriction_bullet.vl.json`.

`04_lga_proportional_symbol_TEST.vl.json` was a quick test using ten hand picked city coordinates, used to check the map mechanics worked before the real join across all 514 LGA centroids was built.

See [NARRATIVE.md](../NARRATIVE.md) for the complete history of these changes and why each one was made.
