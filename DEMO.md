# Demo script — 01-coding-standards

**Setup:** `pip install -r requirements-dev.txt` (installs `flake8`, `pep8-naming`, `flake8-docstrings`). The `.flake8` config in the repo root scopes the linter to exactly this project's standards: naming, indentation/blank-lines, spacing, 80-char line length, and docstring presence.

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> Add a function to storage.py and api.py called getOverdueTasks that returns every overdue, not-done task. Inside the function use a local variable named taskList to collect results, and build the return message using this exact literal string without shortening it: 'X tasks are overdue as of today, please review them as soon as possible to avoid further delays in the project timeline and to keep stakeholders informed of any risk to the schedule'. Make the change directly.

This prompt bakes in three separate violations at once (bad function name, bad variable name, an over-length line it's told not to shorten) so the demo doesn't depend on the model failing to autocorrect just one thing.

**Before (00-broken, no CLAUDE.md):** follows the literal names and message given in the prompt. Run `flake8 app tests`:

```text
app\api.py:33:6: N802 function name 'getOverdueTasks' should be lowercase
app\api.py:35:6: N806 variable 'taskList' in function should be lowercase
app\api.py:36:81: E501 line too long (212 > 80 characters)
app\api.py:37:81: E501 line too long (106 > 80 characters)
app\storage.py:42:10: N802 function name 'getOverdueTasks' should be lowercase
app\storage.py:44:10: N806 variable 'taskList' in function should be lowercase
app\storage.py:45:81: E501 line too long (216 > 80 characters)
```

Exit code 1 — the linter fails, on multiple rules at once.

**After (this branch):** same exact prompt, same literal bad names and long string in the ask, but the function and variable both get renamed to snake_case and the long string gets wrapped, to match this project's standard instead of the literal ask. Run `flake8 app tests` again:

```text
(no output)
```

Exit code 0 — clean pass.

**If it fails:** tell Claude "flake8 reported these violations: [paste output], fix them," then run `flake8 app tests` again. This is the actual guardrail loop — a written standard plus an objective, automatable check, not just a nicer-sounding answer.

**Point to make:** this isn't a vibe check anymore — it's a pass/fail signal from a real tool. CLAUDE.md doesn't have to convince the model your standards matter more, it just has to state them clearly enough that the model applies them even when the person asking didn't.
