# Demo script — 04-workflow

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> Add a function to storage.py and api.py that pushes a task's due date back by N days. Name the functions yourself. Make the change directly.

**Before (00-broken, no CLAUDE.md):** makes the edit, picks a reasonable name for the new function (often "postpone," sometimes something else), no docstrings, no test added, reports "done" with no verification.

**After (this branch):** the same single ask now produces all four properties at once — the naming is settled ("postpone," snake_case, every time), a docstring on every new function, a real test with `pytest` actually run and the pass count reported, and a change summary naming files and rationale. No new dependency, one coherent change.

**Point to make:** this is the same four ideas from `01-coding-standards`, `02-documentation`, and `03-testing` — just stated together as one definition of "done," instead of three separate asks. Workflow is where the individual practices stop being separate concerns and become how the project actually gets built, every time, without having to remember to ask for each piece separately.
