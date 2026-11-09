# PTCG AI Battle Challenge — Mega Lucario ex Agent Lab

Static GitHub Pages demo built from the supplied **Simple Baseline + Matchup Tests** notebook. The page is a **partial JavaScript port of explicitly identified rule-scoring branches**, not the full official `cgb`/`cg` SDK or a complete Pokémon TCG simulator.

## Source alignment
- Deck: exact 60 IDs and quantities from the notebook `DECK` constant.
- Policy: selected branches from `LucarioPolicy._score_option`, `_score_active_choice`, `_score_to_hand`, `_score_play_trainer`, and `_base_attack`.
- Crustle wall: card ID 345 and the guard against Mega Lucario ex attacks; Hariyama is preserved as a non-ex route.
- Local results: notebook-reported Crustle win rate 47% to 77% (100 games each); Public21 selected mean 70.92%. Results are historical data, not recalculated by this browser page.

## Limitations
The notebook uses the official `cg` API, full observations, legal options, and its attack planner. This demo uses user-selected illustrative states and **does not** execute the complete Python policy, official battle engine, game episodes, or training. Its simplified option examples must not be treated as exact official game outputs. No game results are fabricated.

## Deploy
Create a GitHub repository, upload `index.html`, `style.css`, `app.js`, and `data.js` to the repository root. Under Settings → Pages select Deploy from branch, `main`, `/ (root)`.

## Notes
No third-party runtime or external assets required. Uses Verdana. All files work from a static web server or GitHub Pages.
