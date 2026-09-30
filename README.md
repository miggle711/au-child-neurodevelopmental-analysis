# Growing Up Different

A data visualisation exploring autism, disability and developmental support
in Australian children, built for Monash University's FIT3179 Data
Visualisation 2 assignment.

**Live site: [miggle711.github.io/au-child-neurodevelopmental-analysis](https://miggle711.github.io/au-child-neurodevelopmental-analysis/)**

## What this is

The assignment brief asked for a visualisation investigating
neurodevelopmental conditions in Australian children, covering diagnosis
rates, service usage and demographic characteristics, and how access to
support has changed over time. This project pulls together data from the
Australian Bureau of Statistics, the Australian Institute of Health and
Welfare, the Australian Early Development Census, NDIS Data Research and
the Productivity Commission into 15 charts and maps, built entirely in
Vega-Lite and Vega, telling that story on a single scrollable page.

## Repository structure

- **[index.html](index.html)** &mdash; the live page itself
- **[specs/](specs/)** &mdash; every chart and map specification as
  human-readable JSON, plus rendered PNG previews in `specs/previews/`
- **[data/](data/)** &mdash; raw source files (`data/raw/`) and the small,
  clean extracts each chart actually reads (`data/processed/`)
- **[SOURCES.md](SOURCES.md)** &mdash; every data source used, what was
  checked and ruled out, and why
- **[NARRATIVE.md](NARRATIVE.md)** &mdash; the story structure, the
  rationale behind every chart and idiom choice, and a running log of
  decisions and fixes made along the way
- **[PALETTE.md](PALETTE.md)** &mdash; the colour system, so the same
  attribute (like sex) always looks the same across every chart
- **[deprecated/](deprecated/)** &mdash; earlier chart specs that were
  replaced during development, kept for reference

## A note on the data

Several of the charts, including all three required map idioms, rely on
the Australian Early Development Census as a proxy for developmental
vulnerability, because no Australian dataset publicly tracks autism or
ADHD diagnosis by region. Where a chart uses a proxy measure, an age range
that doesn't perfectly match, or has a genuine gap in the underlying data,
that limitation is disclosed directly on the page next to the chart it
affects. See [NARRATIVE.md](NARRATIVE.md) for the full reasoning behind
every one of these calls.
