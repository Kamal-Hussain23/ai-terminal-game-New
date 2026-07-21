# Danger Dragon

Navigate the Dragon Rider across a 5x5 grid to collect eggs while avoiding volcanic hazards. A terminal-based Python game built iteratively with automated testing.

## Features

- **WASD Movement** – Move the player (🚀) using W (up), A (left), S (down), D (right)
- **Collectible Scoring** – Collect eggs (🦊) to increase your score by 1 each; new eggs spawn randomly after each pickup
- **Hazard Avoidance** – Touching a volcano (🌋) triggers an immediate Game Over
- **Win / Lose Conditions** – Score 10 points to win; hitting a hazard loses
- **Play Again Prompt** – After winning or losing, choose to restart or exit
- **Screen Clearing** – The terminal clears between turns for a clean display
- **Boundary Enforcement** – Movement is clamped to the 5x5 grid

## How to Run

**Launch the game:**
```bash
python game.py
```

**Run tests:**
```bash
pytest test_game.py -v
```

## What I Learned

This project was built through iterative development — starting with a bare grid loop, then layering on WASD input, screen clearing, collectibles, hazards, scoring, win/lose conditions, a restart prompt, and finally a themed reskin. Each feature was scoped to a single commit, and tests were written or updated alongside every change to prevent regression.

Writing explicit, narrow prompts helped maintain focus and avoid scope creep. Automated testing proved essential: catching broken assertions after refactoring (e.g., switching from `exit()` to returning a status string, or updating grid symbols from ASCII to emoji) gave confidence that existing behavior remained intact. The `setup_function` fixture kept tests isolated, and mocking `input` allowed end-to-end loop testing without manual interaction.

The result is a stable, themed terminal game with 29 passing tests and a clear separation between game logic, rendering, and the main loop.
