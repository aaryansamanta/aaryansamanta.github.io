# Kaggriculture — Market Preemption Experiment

A static GitHub Pages demo for exploring the bounded **V14 shift/repay market controller** described in `84-84-base-public-holdout-v14-clone-preemption.ipynb`.

## Run and deploy

1. Upload `index.html` and the `assets/` folder to the root of a GitHub repository (suggested: `kaggriculture`).
2. Open **Settings → Pages → Build and deployment → Deploy from a branch**, choose `main` and `/ (root)`.
3. Visit `https://YOUR-USERNAME.github.io/kaggriculture/` after publication.
4. Or open `index.html` locally in a browser. No build or backend is required.

## Scope and limitations

The browser runs an **isolated decision experiment**, not the full Kaggle simulation, its Python agent, the 719-turn route, or an official competition replay. The interactive model follows the notebook's documented gates: turn 120–679, near-clone distance ≤6, one available market-order slot, four premium products, projected own shed stock after already-scheduled SELL orders, a 4-unit future sale minimum, a market-price floor, pending-shift exclusion, and a 30-unit preemption cap. It conserves planned two-turn sale quantities by repaying on the next turn. The chart implements the competition document's piecewise nonlinear price function using the resource parameters. It does not execute the full V23 impact-order ranking or reconstruct farm actions. Inputs are hypothetical and results are illustrative, not official episode scores.

The notebook's own provenance section explains that its production route was reconstructed from public Kakuteki replays; market-ranking and weed-recovery techniques reuse/adapt public Kaito V23 work; and the shift/repay controller inherits from V13-R3. The browser demonstration does not imply original authorship of those components. See the original notebook and its linked research for details.

## Reference material

- Kaggriculture competition: https://www.kaggle.com/competitions/kaggriculture
- Kaito V23: https://www.kaggle.com/code/kaitofukami/23-23-strict-future-v23-sparse-closed-loop
- V13-R3: https://www.kaggle.com/code/boatlee/v13-r3-top-meta-order-safe-premium-control

## Technical details

Vanilla HTML, CSS and JavaScript; no external dependencies. All calculation and graph rendering occur in the browser. Keyboard-accessible native controls and responsive layouts.

## Source-code fidelity review

The browser decision is transcribed from `_preempt_shift` and `_repay_shift` in the V14 notebook, including `_PREEMPT_FRACTION=2.34358964641`, `_PREEMPT_MIN_FUTURE_QUANTITY=4`, `_PREEMPT_MIN_PRICE_RATIO=0.02364641`, and all primary activation gates. Market price parameters for the four premium products match `_MARKET_PARAMS` in the notebook. The browser accepts clone distance, future SELL quantity, projected stock, and existing SELL volume as explicit scenario inputs rather than reconstructing `_public_signature`, `_ACTIONS`, or the full Python environment. It models a single premium product per decision, whereas the Python code loops across all four products.
