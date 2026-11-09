# Stanford RNA 3D Folding Part 2 — browser experiment

Static GitHub Pages project. Upload `index.html`, `styles.css`, and `script.js` to the repository root, then enable Settings → Pages → Deploy from branch → main / root. Suggested repository name: `stanford-rna-3d-folding-2`.

## Executable scope

The browser executes global sequence alignment (match +2, mismatch -1, gap -2), template C1′ coordinate mapping, interpolation/extrapolation for unmatched target residues, five coordinate sets (one mapped trace plus four **illustrative perturbations**), interactive 3D projection, and CSV export. All processing runs locally in JavaScript without a backend.

This is **not** a port of Protenix model inference. The supplied Kaggle notebook uses PyTorch, Protenix weights, RNA MSA, PDB template data, template-based modeling, and RNA structural constraints. Those dependencies and full model inference are not available in this static browser page. Demo-generated coordinates are illustrative and must not be described as validated competition predictions or reproduce the leaderboard result.

The supplied notebook explicitly links to earlier work by qiweiyin, nihilisticneuralnet, and alexxanderlarko. Preserve original authorship and attribution when publishing or presenting adapted work. The silver medal certificate reports 92nd out of 1,867 teams, but this demonstration is not evidence of the scoring pipeline.

Input coordinate CSV: one `x,y,z` row for each template residue, in Å. Exported CSV uses the competition's `ID,resname,resid,x_1,y_1,z_1,...,x_5,y_5,z_5` coordinate-column convention; the demo `ID` prefix is not a Kaggle submission target identifier.

### 3D controls
The left panel has working Rotate, Zoom, and Color buttons. They modify the canvas rendering in the right panel; drag and scroll also work. The Color button cycles through residue position, single color, and depth coloring.
