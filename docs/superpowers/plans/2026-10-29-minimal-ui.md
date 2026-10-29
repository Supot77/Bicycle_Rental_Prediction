# Minimal UI Implementation Plan

> Implement inline in the existing isolated worktree; review the complete diff before publishing.

**Goal:** Give the prediction app a minimal layout and add the supplied UniMAP logo.

**Architecture:** Native Streamlit widgets and containers provide interaction. Local CSS and semantic HTML provide the logo strip and responsive developer footer; the inference contract stays unchanged.

**Tech Stack:** Python 3.12, pinned Streamlit, HTML/CSS, existing saved model.

**Spec:** ../specs/2026-10-29-minimal-ui-design.md

## Constraints

- Keep all five supplied English names and the original three logo files.
- Preserve seven raw inputs, validation, model hashes and dependencies.
- No training, fabricated results, or replacement hosting.

## Implementation

- [x] Add `logo/unimap.png`, copied without alteration from the supplied file.
- [x] Add `.streamlit/config.toml` for a light theme and `assets/app.css` for restrained responsive styling.
- [x] Update `app.py`: responsive branding, two-column controls/result, persistent scenario-aware forecast, developer footer. Keep inference and validation checks intact.
- [x] Run `python scripts/check_setup.py`, `python -m unittest discover -s tests -v`, Python syntax and diff checks.
- [x] Run the maintainer AppTest smoke check: three logos, five exact names, Wednesday reference 43.84, changed input notification, updated prediction, missing-artifact handling and unchanged release hashes.
- [x] Review the running app on desktop and mobile; resolve any overflow or clipping.
- [x] Update README with verified behavior and limits and review the complete diff.

Publication follows the completed checks: commit to GitHub main and verify the remote SHA. The final response records publication rather than claiming a live Cloud check.

Review notes: retained the user's existing dev-container commit by fast-forwarding before editing. Browser review found clipped branding under Streamlit's toolbar; increasing top padding resolved it. Responsive checks used actual content widths of 1164px and 355px, with no horizontal overflow. The supplied UniMAP file's SHA-256 matches the committed copy. Model artifacts, the feature helper, and requirements have no changes.
