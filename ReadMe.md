## Design Decisions

- Streamlit was chosen instead of a separate backend because the system is
  session-based, stateless, and does not require persistence or authentication.
- The simulation uses causal rules and feedback loops rather than black-box
  prediction models to improve interpretability.
- Time is modeled explicitly (monthly steps) to capture compounding effects.

These decisions prioritize clarity, correctness, and simplicity over unnecessary complexity.

## App Overview

![App Overview](screenshots/app_overview.png)

## Story Mode

![Story Mode](screenshots/story_mode.png)

