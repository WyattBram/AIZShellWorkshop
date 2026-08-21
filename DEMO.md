# Demo script — 01-coding-standards

**Setup:** `pip install -r requirements-dev.txt` (installs `flake8`, `pep8-naming`, `flake8-docstrings`). The `.flake8` config in the repo root scopes the linter to exactly this project's standards: naming, indentation/blank-lines, spacing, 80-char line length, and docstring presence.

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> We want a weekly status report feature for managers. It should look across all tasks and produce a summary covering three things: how many tasks are overdue and not done, how many are due in the next 3 days, and how many were completed this week. For each of those three groups include a short natural-language sentence describing the situation, written the way you'd actually explain it to a busy manager who just wants the gist, plus the raw counts and task titles for anyone who wants detail. Also include an overall urgency label (something like low, medium, or high) based on how bad the overdue count looks compared to the total number of open tasks. Wire the whole thing up across storage.py and api.py, adding whatever helper functions you need. Make the change directly.

No identifiers or exact wording are dictated here — it's a normal, fairly substantial feature request, phrased the way a real teammate would actually ask for it. It touches three files, adds a new model field (`completed_at`), a couple of new functions, and several natural-language summary sentences. The extra breadth means more chances for a real violation to slip in on its own.

**Before (00-broken, no CLAUDE.md):** builds the whole feature correctly — new field, urgency logic, three-part summary — but several of the natural-language sentences and the urgency-logic lines end up over 80 characters. Run `flake8 app tests`:

```text
app\api.py:64:81: E501 line too long (82 > 80 characters)
app\api.py:69:81: E501 line too long (84 > 80 characters)
app\api.py:71:81: E501 line too long (89 > 80 characters)
app\api.py:78:81: E501 line too long (86 > 80 characters)
app\storage.py:53:81: E501 line too long (86 > 80 characters)
app\storage.py:55:81: E501 line too long (88 > 80 characters)
```

(Exact lines/counts vary run to run — the wording isn't fixed — but a fresh run on `00-broken` reliably produces several `E501` violations across both files, since there are now multiple long sentences instead of just one.) Exit code 1 — the linter fails.

**After (this branch):** same exact prompt, same amount of new code, but every long sentence and logic line gets wrapped to fit, matching this project's standard. Run `flake8 app tests` again:

```text
(no output)
```

Exit code 0 — clean pass.

**If it fails:** tell Claude "flake8 reported these violations: [paste output], fix them," then run `flake8 app tests` again. This is the actual guardrail loop — a written standard plus an objective, automatable check, not just a nicer-sounding answer.

**Point to make:** this isn't a vibe check anymore — it's a pass/fail signal from a real tool. Nobody told the model to write a bad line; a normal, moderately complex feature request, described the way a real teammate would describe it, produced several anyway — more surface area, more chances for something to slip. CLAUDE.md doesn't have to convince the model your standards matter more, it just has to state them clearly enough that the model applies them even at scale, when nobody's watching that closely.

**Not on Claude Code?** `other-tools/` has this same coding-standards content ported to `.github/copilot-instructions.md` (Copilot) and `.cursor/rules/coding-standards.mdc` (Cursor) — copy whichever matches your stack.
