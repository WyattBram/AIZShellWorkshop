# Demo — 03-testing

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> Add a cancel_task(task_id) function to storage.py and api.py. It should handle a task that doesn't exist, and a task that's already been cancelled, sensibly. Make the change directly.

Naming two edge cases in the ask (not-found, already-cancelled) gives the feature enough real branches that "one test" would obviously be incomplete — a bigger gap for the testing rule to close.

**Before (00-broken, no CLAUDE.md):** makes the edit — a real `KeyError`/404 for the missing task, a real `ValueError`/409 for the already-cancelled one — and reports "done" on the strength of the code alone. No test gets made; `tests/test_api.py` is untouched.

**After (this branch):** same prompt, but now tests get made automatically: the test gets written first, `pytest` gets run and actually fails for the expected reason, then the implementation gets written to handle the two edge cases, and `pytest` gets run again to confirm a real pass count instead of just asserting the change works. (Exactly how many tests get written can vary run to run, since the model's output isn't fixed, but the happy path, not-found, and already-cancelled cases all reliably get covered.)

**Point to make:** "add a function" doesn't imply "and prove it works" unless you say so, and it definitely doesn't imply "prove every branch works," let alone "prove it in that order." A testing section turns an assumption into a requirement: write the failing test first, watch it fail for the right reason, then make it pass. That order is what actually proves the test is checking something real, instead of just rubber-stamping code that already exists.

**Not on Claude Code?** `other-tools/` has this same testing content ported to `.github/copilot-instructions.md` (Copilot) and `.cursor/rules/testing.mdc` (Cursor) — copy whichever matches your stack.
