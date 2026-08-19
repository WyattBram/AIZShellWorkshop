# Workflow

This project's full definition of "done" for any change:

1. **Code** — follow this project's PEP 8 standard (naming, spacing, line length). Run `flake8 app tests` after any change and fix anything it reports.
2. **Docs** — keep `documents/` current: update `ARCHITECTURE.md` when a file's purpose changes, append to `CHANGELOG.md` after any code change, and add to `DECISIONS.md` when you make a non-obvious tradeoff.
3. **Tests** — a matching test in `tests/` for anything touching `TaskStore` or `app/api.py`. Actually run `python -m pytest tests/ -q` and report the result — don't just assert it "should pass."
4. **Process** — don't add a new dependency without asking first and naming the stdlib/existing alternative you ruled out. One logical change per commit.

A change isn't done until all four are true, not just the code.
