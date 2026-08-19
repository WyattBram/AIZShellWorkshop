# Demo script — 01-coding-standards

**Setup:** `pip install -r requirements-dev.txt` (installs `flake8`, `pep8-naming`, `flake8-docstrings`). The `.flake8` config in the repo root scopes the linter to exactly this project's standards: naming, indentation/blank-lines, spacing, 80-char line length, and docstring presence.

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> Add a function to storage.py and api.py called getOverdueTasks that returns every task that is overdue and not done, along with a formatted message like 'X tasks are overdue as of today, please review them as soon as possible to avoid further delays in the project timeline'. Make the change directly.

**Before (00-broken, no CLAUDE.md):** follows the camelCase name given in the prompt literally — `getOverdueTasks` in both files. Run `flake8 app tests`:

```text
app\api.py:33:6: N802 function name 'getOverdueTasks' should be lowercase
app\storage.py:42:10: N802 function name 'getOverdueTasks' should be lowercase
```

Exit code 1 — the linter fails.

**After (this branch):** same exact prompt, camelCase name and all, but the function gets renamed to `get_overdue_tasks` to match this project's standard instead of the literal name in the ask. Run `flake8 app tests` again:

```text
(no output)
```

Exit code 0 — clean pass.

**If it fails:** tell Claude "flake8 reported these violations: [paste output], fix them," then run `flake8 app tests` again. This is the actual guardrail loop — a written standard plus an objective, automatable check, not just a nicer-sounding answer.

**Point to make:** this isn't a vibe check anymore — it's a pass/fail signal from a real tool. CLAUDE.md doesn't have to convince the model your standards matter more, it just has to state them clearly enough that the model applies them even when the person asking didn't.
