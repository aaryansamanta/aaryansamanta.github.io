# Biohub - Cell Tracking During Development — interactive demo

Static GitHub Pages experiment demonstrating the **centroid association** stage of the nearest-neighbor baseline notebook.

## Run

Open `index.html` in a browser, or publish the repository root through GitHub Pages (Settings → Pages → Deploy from branch → main / root). No build step or server is required.

## Inputs and implementation

- Import a centroid CSV with `frame,z,y,x` (or `t,z,y,x`) voxel coordinates, or generate deterministic synthetic centroid detections.
- The physical voxel scales are `Z=1.625`, `Y=0.40625`, `X=0.40625` µm/voxel.
- Consecutive frames are associated with minimum-cost one-to-one Hungarian assignment and a default 15 µm link-distance gate.
- Inspect XY trajectories and assigned links; export node and edge CSV files.

## Scope and scientific limitations

This is a browser implementation of the **association step**, not a full execution of the competition submission. The baseline notebook additionally reads Zarr/Blosc microscopy volumes, downsamples by 4, applies a 3×3×3 uniform filter, thresholds at the 90th percentile, labels connected components, and calculates centroids. Those image-processing steps are not included. Nor does this demo run geometric-fusion/CUDA inference, detect cell division, or reproduce the Kaggle leaderboard evaluation. Synthetic input is demonstration data, not a competition result.

The competition submission schema contains `dataset,row_type,node_id,t,z,y,x,source_id,target_id` plus a consecutive `id` index; the browser exports are inspection tables rather than a validated official competition submission.

Competition: Biohub - Cell Tracking During Development (2026).
