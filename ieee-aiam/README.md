# IEEE AIAM 2025 — Quantum-Inspired GA–GNN Research Explorer

A static, responsive GitHub Pages companion to the supplied publication materials.

## Deploy
1. Unzip and upload the **contents** of this directory to the root of a GitHub repository (or its `/docs` folder).
2. In repository Settings → Pages, choose Deploy from a branch, `main`, and `/ (root)` (or `/docs` if you put these files there).
3. Open the published GitHub Pages URL. No build step or external libraries are required.

## What runs
- Educational feature-selection probability updates, with an illustrative fixed target mask.
- Educational graph neighborhood averaging on a six-node graph.
- Educational weighted-average late fusion with illustrative fixed scores.
- Metric comparisons calculated from the paper's Table 1.

## What does **not** run
- The full QIHGA–GNN model, trained inference, Python/XGBoost training, SHAP generation, or retraining.
- The supplied Python source implements XGBoost/SHAP/sensitivity, not the complete QIHGA–GNN architecture.
- The supplied datasets are not verified as the exact training data in the manuscript.
- The manuscript prose mentions 90% accuracy while Table 1 lists 0.53; this website faithfully labels Table 1 values rather than resolving the conflict.

## Included original materials
- Original supplied Figures 1–5, manuscript PDF, acceptance certificate, Python source, bibliography, and two Excel files.
- Files are presented for research review, not as proof of a fully reproducible QIHGA–GNN experiment.

## Attribution
This interactive website is an AI-assisted educational companion assembled from the supplied paper and repository. It must not be represented as a student-authored implementation of the proposed QIHGA–GNN model.


## Demo-first update
The compact heading now leads directly into the runnable browser labs. The original repository banner is shown in the evidence section, alongside links to the source GitHub repository and the IEEE Xplore URL listed in its README. All numerical results are reported values, and the browser algorithms are explicitly educational.
