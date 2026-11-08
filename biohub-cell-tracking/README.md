---
title: Biohub Cell Tracking Algorithm Lab
emoji: 🧬
colorFrom: blue
colorTo: green
sdk: static
pinned: false
short_description: Interactive cell tracking and trajectory analysis.
---

# Biohub Cell Tracking Algorithm Lab

This browser demo implements the **centroid matching/linking stage** of the uploaded `Biohub-Silver-cell-tracking-getting-started-w-nearest-neighbor(1).ipynb` notebook. It uses 3D physical distances (Z/Y/X scale `[1.625, 0.40625, 0.40625]` µm/voxel), globally minimum-cost one-to-one Hungarian assignment, and a 15 µm default link cutoff.

## What is and is not implemented

- **Implemented:** Per-frame centroid association, 3D physical-distance calculation, global assignment, distance gating, trajectories, node/edge CSV exports, synthetic detections, and CSV import.
- **Not implemented:** Original notebook's Zarr/Blosc2 image reading, 3D uniform filtering, 90th-percentile threshold, connected-component segmentation, or the separate CUDA-dependent geometric-fusion model.
- **Data:** Synthetic detections unless the user supplies a centroid CSV. This is not a reproduction of Kaggle competition results.

## Deploy

Create a Hugging Face **Static** Space, then upload `index.html` and this `README.md` to the root. No dependencies or build process required.

## Attribution

The underlying algorithmic steps were derived from the user-uploaded nearest-neighbor baseline notebook. Verify original authorship and third-party attribution before representing this demo as independent work in any application.
