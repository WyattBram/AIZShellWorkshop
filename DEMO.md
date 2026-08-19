# Demo script — 01-coding-standards

**Prompt (same on both sides):**
> Without editing anything, describe exactly how you would add a `cancel_task(task_id)` function to storage.py and api.py, in the same style as the existing code. Show the code you'd write.

**Before (00-broken, no CLAUDE.md):** mirrors the existing code faithfully — including the `KeyError`-on-missing-id gap that `complete()` already has — with partial type hints, matching the codebase's actual (inconsistent) style.

**After (this branch):** same feature, but now guards against a missing id with `.get()` + a `None` check (matching `get_task`'s safer pattern instead of `complete`'s gap), full type hints on the new code, and a clean 404 in the API layer — while staying just as short.

**Point to make:** "match the existing style" is ambiguous when the existing style is inconsistent. A coding-standards section tells the model *which* existing pattern to extend and which one is a known gap not to repeat.
