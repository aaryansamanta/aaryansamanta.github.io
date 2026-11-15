# QIHGA–GNN Research Website

Static GitHub Pages research explorer for **Aaryan Samanta**, built around the latest `ieee-aiam-2025-ga-gnn` repository.

## Source of truth
- Research paper: `source/paper.pdf`, `source/paper.tex`
- Executable code: `source/code/aiam_gnn/`
- Dataset: `source/aiam-data.xlsx`
- Figures: `assets/`
- Browser labs: `app.js` (illustrative concept visualizations, not a Python runtime)

## Published scores
The benchmark uses the exact values in the supplied `paper.tex` Table 1: QIHGA–GNN 0.90, Baseline 1 0.85, Baseline 2 0.88 across accuracy, precision, recall, and F1. The paper reports n=20 and TP=9, FP=1, TN=9, FN=1 for QIHGA–GNN.

## Deploy
Publish the `html-pages/` folder to GitHub Pages (or copy its contents into your repository's `docs/` directory and select `/docs` in Pages settings). No build tools or backend required. Open `index.html` locally for preview.

## Notes
The manuscript's sensitivity-analysis narrative discusses accuracy around 0.50–0.56 under noise, while its main Table 1 reports 0.90. The website does not conflate these distinct passages or invent a new robustness result. The paper's baselines are labeled exactly as in the LaTeX table.
