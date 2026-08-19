# Demo script — 02-documentation

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> Add a cancel_task(task_id) function to storage.py and api.py, following the existing style. Make the change directly.

**Before (00-broken, no CLAUDE.md):** makes the edit, no docstrings on the new functions, and closes with a terse "done" — no explanation of what changed or why beyond the code itself.

**After (this branch):** same edit, but both new functions get a one-line docstring, and the response ends with a short summary of what changed, in which files, and why.

**Point to make:** documentation isn't just about the code — it's also about the assistant's own accountability for what it did. "Document what you did" applies to the AI's actions in your session, not only to the functions it writes.
