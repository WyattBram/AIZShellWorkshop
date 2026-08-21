# TaskTracker — Copilot instructions (stage: testing)

Copy this file into `.github/copilot-instructions.md` at the root of your repo (create the `.github/` directory if it doesn't exist). Copilot reads it automatically for every chat response, inline completion, and PR review in this repo.

Same content as this branch's `CLAUDE.md`, ported to Copilot's format.

# Testing

- Every new function that touches `TaskStore` or `app/api.py` gets a matching test in `tests/`. No exceptions for "small" changes.
- After writing or changing a test, actually run `python -m pytest tests/ -q` and report the result. Don't just say a test "should pass."
- Test behavior, not implementation: assert on what a function returns or raises, not on internal calls it happens to make.
