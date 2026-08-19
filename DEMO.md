# Demo script — 03-testing

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> Add a cancel_task(task_id) function to storage.py and api.py.

**Before (00-broken, no CLAUDE.md):** makes the edit, no new test added, reports "done" on the strength of the code alone.

**After (this branch):** same edit, but adds two real tests — the happy path and the missing-id case — and actually runs `pytest`, reporting "3 passed" instead of just asserting the change works.

**Point to make:** "add a function" doesn't imply "and prove it works" unless you say so. A testing section turns an assumption into a requirement, and turns "should pass" into an actual, checkable pass count.
