# Demo script — 04-workflow

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> Add a function to storage.py and api.py called getOverdueTasks that returns every task that is overdue and not done. Make the change directly.

**Before (00-broken, no CLAUDE.md):** makes the edit, follows the camelCase name given in the prompt literally (`flake8 app tests` reports two `N802` violations, exit 1), no docstring, no test added, reports "done" with no verification.

**After (this branch):** the same single ask now produces all four properties at once — renamed to `get_overdue_tasks` to satisfy the project's lint rules instead of the literal name in the ask, a docstring on every new function, real tests with `pytest` actually run and the pass count reported, `flake8 app tests` clean (exit 0), and a change summary naming files and rationale. No new dependency, one coherent change.

**Point to make:** this is the same four ideas from `01-coding-standards`, `02-documentation`, and `03-testing` — just stated together as one definition of "done," instead of three separate asks. Workflow is where the individual practices stop being separate concerns and become how the project actually gets built, every time, without having to remember to ask for each piece separately.
