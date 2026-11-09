# UCSB SRA × IJHSR — Mitochondrial Resilience Research Atlas

A static, interactive GitHub Pages companion for the research project begun at UCSB Summer Research Academies 2025 and subsequently published in IJHSR 2026.

## Deploy
Upload the **contents of this folder** to the repository root (or `docs/`) and configure Settings → Pages → Deploy from branch → `main` → `/ (root)` (or `/docs`). The `index.html`, `style.css`, `app.js`, `assets/` and `source/` must remain together. No installation or backend is required.

## Start with the live demo
The executable VCF lab is the **first section immediately below the hero**. Click **Run sample demo — no file needed** to load an explicitly synthetic five-record VCF and immediately run the filter. Change chromosome, positions, sample, or non-reference filter and click **Run VCF filter** to recalculate. You can also upload your own small VCF.

## Interactions
- Gene field guide: six gene descriptions and reported selection/variant summaries.
- VCF lab: actual local JavaScript parsing/filtering of a small plain-text VCF; chromosome, position, sample genotype and non-reference filtering. The built-in example is synthetic and **not** a research dataset. Browser limit 8 MB; compressed VCF unsupported.
- Evidence notebook: selectable research summaries with page excerpts from the supplied publication.
- Research source links: DOI, original partial Jupyter notebook, SRA capstone seminar PDF and GEO accession.

## Scientific and authorship scope
This website is an AI-assisted presentation and educational coding companion, not the full research analysis pipeline or a student-written reproduction. The supplied notebook covers annotation, SNP extraction and VEP preparation but does not include the paper's full PCA, phylogeny, RNA-seq, neural-network or CRISPR workflows. The browser does not train models or execute Python. Reported results and predictions are labeled accordingly. The paper proposes CRISPR validation; it does not establish a causal mitochondrial-resilience mechanism through completed CRISPR experiments. Preserve original author and mentor credits in the linked materials.

Research authors: Aaryan Samanta, Mansi Mandal, Mohammed Yasar Meeran. DOI: https://doi.org/10.36838/IJHSR816.1

This public-safe package excludes the original ZIP's `private/` certificates and acceptance images, full journal issue, and macOS metadata. Manuscript page excerpts are provided for contextual reference; rights in the article remain with their respective rights holders. The original notebook and SRA presentation are included for review.

## Compact header update
The original large hero illustration has been removed, the introduction shortened, and a prominent **Read the published paper** button links to https://doi.org/10.36838/IJHSR816.1. The executable VCF browser lab appears immediately below the compact introduction.


## Demo-first compact edition

The research introduction is minimized and the VCF filter is the first content section. Click **Run sample demo — no file needed** to load and filter five explicitly synthetic VCF records without any upload. The original research repository, published DOI, graphical abstract and CITATION.cff are linked in the source section. The external repository links reflect paths in the supplied research ZIP; live availability may change.

## Visual theme
Bright coastal-science colors (aqua, sky blue, coral, and sunshine yellow), Verdana text, and an ultra-compact demo-first header. All research content and interactive VCF filtering are preserved.
