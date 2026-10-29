# Minimal prediction UI

The user requested a cleaner UI and the supplied UniMAP logo, then specified a minimal style. Keep the Streamlit app, current model, seven-input contract, integrity checks, English developer names, and GitHub/Community Cloud deployment.

Use white, navy (#17355A), pale gray (#F6F8FB), slate text (#1D2939), and a quiet border (#E4E8EF). Keep native sans-serif typography, a restrained title, generous space, and visible field labels. The three original logos retain their proportions and colors; their row wraps on small screens.

Desktop: compact branding row, title, two columns containing inputs and forecast, then a light developer footer. Mobile: stacked inputs and result with a two-column developer grid. Use native Streamlit widgets for focus, labels, and input limits. No decorative animation or charts.

Alternatives considered: a more colorful dashboard and a dark dashboard. The user's minimal preference favors a restrained white layout. Layout details are implementation decisions.

The forecast persists across reruns. After an input changes, visibly label the previous forecast and retain its original scenario until the user predicts again. Before prediction, show a dash rather than a fabricated forecast. Preserve the synthetic-data limitation.

Verification: setup checks, existing unit tests, AppTest for three logos, exact names, prediction parity and changed-input behavior, plus desktop/mobile browser review. Local checks are maintainer checks; hosted training remains on Colab. Do not claim a live deployment check unless actually observed.
