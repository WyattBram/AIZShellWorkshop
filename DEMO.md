# Demo script — 01-coding-standards

**Setup:** `pip install -r requirements-dev.txt` (installs `flake8`, `pep8-naming`, `flake8-docstrings`). The `.flake8` config in the repo root scopes the linter to exactly this project's standards: naming, indentation/blank-lines, spacing, 80-char line length, and docstring presence.

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> We need a daily digest feature: look at all tasks, find the ones that are overdue and not done, and produce a short report a manager could read at a glance — how many are overdue, and a friendly reminder message telling them to review the list soon since delays add up and stakeholders will start asking questions if this drags on. Wire it up in storage.py and api.py. Make the change directly.

No identifiers or exact wording are dictated here — it's a normal feature request, phrased the way someone would actually ask for it. The violation comes from the model writing a natural, longer status message and not wrapping it, not from a rigged instruction.

**Before (00-broken, no CLAUDE.md):** builds the feature, reasonably named, but the manager-facing message ends up on one long line (or split across a couple that still run over). Run `flake8 app tests`:

```text
app\api.py:41:81: E501 line too long (82 > 80 characters)
app\api.py:42:81: E501 line too long (119 > 80 characters)
app\api.py:47:81: E501 line too long (101 > 80 characters)
```

(Exact lines/counts vary run to run — the wording isn't fixed — but a fresh run on `00-broken` reliably produces at least one `E501` violation from the digest message.) Exit code 1 — the linter fails.

**After (this branch):** same exact prompt, but the same kind of message gets wrapped across multiple properly-indented lines, each under 80 characters, to match this project's standard. Run `flake8 app tests` again:

```text
(no output)
```

Exit code 0 — clean pass.

**If it fails:** tell Claude "flake8 reported these violations: [paste output], fix them," then run `flake8 app tests` again. This is the actual guardrail loop — a written standard plus an objective, automatable check, not just a nicer-sounding answer.

**Point to make:** this isn't a vibe check anymore — it's a pass/fail signal from a real tool. Nobody told the model to write a bad line; a normal feature request, described the way a real teammate would describe it, produced one anyway. CLAUDE.md doesn't have to convince the model your standards matter more, it just has to state them clearly enough that the model applies them even when nobody's watching that closely.
