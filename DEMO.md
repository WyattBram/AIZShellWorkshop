# Demo script — 04-workflow

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> Add a way to cancel a task. You decide whether it should remove the task entirely or just mark it cancelled. Make the change directly.

**Before (00-broken, no CLAUDE.md):** makes a reasonable choice and a working edit, but nothing gets named to lint standards, nothing gets tested, and the prefilled `documents/` files (ARCHITECTURE, CHANGELOG, DECISIONS) sit untouched even though the change is exactly the kind of tradeoff they exist to record.

**After (this branch):** the same open-ended ask now produces all four properties at once — `flake8 app tests` clean, a real test covering the new behavior with `pytest` run and the pass count reported, `documents/ARCHITECTURE.md` and `CHANGELOG.md` updated, and a genuine `DECISIONS.md` entry explaining why this option was chosen over the alternative. No new dependency, one coherent change.

**Point to make:** this is the same four ideas from `01-coding-standards`, `02-documentation`, and `03-testing` — just stated together as one definition of "done," instead of three separate asks. Workflow is where the individual practices stop being separate concerns and become how the project actually gets built, every time, without having to remember to ask for each piece separately.
