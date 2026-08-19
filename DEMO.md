# Demo script — 01-coding-standards

**Prompt (same on both sides):**
> Without editing anything, add a function to storage.py and api.py that pushes a task's due date back by N days. Name the functions yourself.

**Before (00-broken, no CLAUDE.md):** the model has to pick a name for this on its own — "postpone," "reschedule," "delay," "defer," and "snooze" are all reasonable words, and nothing says which one this project uses. It usually guesses something sensible, but a different session, a different phrasing, or a different teammate's prompt could just as easily land on a different word.

**After (this branch):** same ask, but the naming is settled in advance — "postpone," every time, plus snake_case and a one-line docstring, because the rule is written down rather than left to be re-decided per session.

**Point to make:** the model wasn't wrong before, and it may not even be wrong most of the time. That's the trap — "usually right" isn't the same as "consistent," and consistency is what a growing codebase with multiple contributors actually needs. A coding-standards section isn't there to catch failures, it's there to remove a decision the model would otherwise make fresh every time.
