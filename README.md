# Code: Terraform — Earlygame Automation

Scripts that automate the early-game bootstrap of a fresh [Code: Terraform]([https://store.steampowered.com/](https://store.steampowered.com/app/868160/Code_Terraform/)) save: First Contact onboarding, the 6 intro Earth contracts, and building out/scaling the base all the way to the 150,000 TP mid-game transition.

For the full technical rundown — architecture, the 0 → 150k TP speedrun strategy, and phase-by-phase details — see [`auto_walkthrough.md`](auto_walkthrough.md).

## Quick start

0. This requires python as well as node installed in PATH. I only tested it under Windows - will not work under other OS (hardcoded %appdata% as I'm lazy)
1. Launch a **new game**.
2. Open **Settings** and click **Open Scripts Folder** (this is what initializes the save's script workspace files on disk — required before anything below will work).
3. **Unpause** the game.
4. From that scripts folder, run:
   ```
   python early_game.py --auto
   ```
5. Follow the console output — it prints an actionable recommendation whenever it needs something only you can do in-game (e.g. clicking a newly unlocked contract).

`--auto` runs onboarding, solves the intro contracts, deploys scripts to every idle machine, and then keeps running as a background watcher/dashboard. See the module docstring at the top of [`early_game.py`](early_game.py) (or run it with `--help`) for the individual `--onboarding` / `--contracts` / `--scan` / `--advisor` / `--daemon` flags if you'd rather run steps separately.


Note: the final transition at 150k TP will not work for you - I didn't include my other (ugly) scripts :-D
