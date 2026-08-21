# Demo script — 03-testing

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> Add a cancel_task(task_id) function to storage.py and api.py. It should handle a task that doesn't exist, and a task that's already been cancelled, sensibly. Make the change directly.

Naming two edge cases in the ask (not-found, already-cancelled) gives the feature enough real branches that "one test" would obviously be incomplete — a bigger gap for the testing rule to close.

**Before (00-broken, no CLAUDE.md):** makes the edit — a real `KeyError`/404 for the missing task, a real `ValueError`/409 for the already-cancelled one — and reports "done" on the strength of the code alone. `tests/test_api.py` is untouched; still just the original one test.

**After (this branch):** same edit, same two edge cases handled the same way, but now three new tests — happy path, not-found, already-cancelled — get written, `pytest` actually runs, and "4 passed" gets reported instead of just asserting the change works.

**Point to make:** "add a function" doesn't imply "and prove it works" unless you say so — and it definitely doesn't imply "prove every branch works." A testing section turns an assumption into a requirement, and turns "should pass" into an actual, checkable pass count that scales with however many cases the feature actually has.

**Not on Claude Code?** `other-tools/` has this same testing content ported to `.github/copilot-instructions.md` (Copilot) and `.cursor/rules/testing.mdc` (Cursor) — copy whichever matches your stack.
