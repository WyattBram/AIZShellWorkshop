# Workflow

This project's full definition of "done" for any change:

1. **Code** — snake_case everywhere, no exceptions. Use "postpone" for pushing a due date back, never "reschedule," "delay," "defer," or "snooze."
2. **Docs** — a one-line docstring on every new function/class (no exceptions, this codebase has none today — don't extend that gap). End your response with what changed, in which files, and why.
3. **Tests** — a matching test in `tests/` for anything touching `TaskStore` or `app/api.py`. Actually run `python -m pytest tests/ -q` and report the result — don't just assert it "should pass."
4. **Process** — don't add a new dependency without asking first and naming the stdlib/existing alternative you ruled out. One logical change per commit.

A change isn't done until all four are true, not just the code.
