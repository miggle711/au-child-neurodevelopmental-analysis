# Growing Up Different

A data visualisation exploring autism, disability and developmental support in Australian children, built for Monash University's FIT3179 Data Visualisation 2 assignment.

**Live site: [miggle711.github.io/au-child-neurodevelopmental-analysis](https://miggle711.github.io/au-child-neurodevelopmental-analysis/)**

## What this is

The assignment brief asked for a visualisation investigating neurodevelopmental conditions in Australian children: diagnosis rates, service usage, demographic characteristics, and how access to support has changed over time. This project pulls together data from the Australian Bureau of Statistics, the Australian Institute of Health and Welfare, the Australian Early Development Census, NDIS Data Research, the Productivity Commission and a couple of smaller supporting sources into 16 charts and maps, built entirely in Vega-Lite and Vega, telling that story on a single scrollable page.

## Repository structure

- **[index.html](index.html)** is the live page itself.
- **[specs/](specs/)** holds every chart and map specification as human-readable JSON, with rendered PNG previews alongside each one in `specs/previews/`.
- **[data/](data/)** holds the raw source files (`data/raw/`) and the small, clean extracts each chart actually reads (`data/processed/`).
- **[SOURCES.md](SOURCES.md)** documents every data source used, what was checked and ruled out, and why.
- **[NARRATIVE.md](NARRATIVE.md)** sets out the story structure and the reasoning behind every chart and idiom choice, including a running log of fixes made along the way.
- **[PALETTE.md](PALETTE.md)** documents the colour system, so the same attribute (like sex) always looks the same wherever it appears.
- **[deprecated/](deprecated/)** keeps earlier chart specs that were replaced during development, for reference.

## A note on the data

Three of the five map idioms rely on the Australian Early Development Census as a proxy for developmental vulnerability, because no Australian dataset publicly tracks autism or ADHD diagnosis by region. Where a chart uses a proxy measure, an age range that doesn't line up exactly, or has a genuine gap in the underlying data, that limitation is disclosed directly on the page next to the chart it affects, rather than left for a reader to discover on their own. See [NARRATIVE.md](NARRATIVE.md) for the full reasoning behind each of these calls.
