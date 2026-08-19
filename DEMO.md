# Demo script — 02-documentation

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> Add a way to cancel a task. You decide whether it should remove the task entirely or just mark it cancelled. Make the change directly.

**Before (00-broken, no CLAUDE.md):** the repo already has `documents/ARCHITECTURE.md`, `CHANGELOG.md`, and `DECISIONS.md` sitting there, prefilled. The model makes a real, reasonable code change — but doesn't touch any of them. Nothing told it those files are its job to keep current.

**After (this branch):** same prompt, same reasonable choice (mark cancelled, don't delete), but now:
- `documents/ARCHITECTURE.md` gets the new field/function added to the file descriptions.
- `documents/CHANGELOG.md` gets a new dated entry, without touching the existing "Initial" entry.
- `documents/DECISIONS.md` gets a real entry explaining *why* cancel marks instead of deletes (mirrors the existing `done`-doesn't-delete precedent already written there).

**Point to make:** these documents existed the whole time — the gap wasn't "no docs," it was "no one told the assistant when to use them." Documentation isn't one blanket rule ("write docs"), it's specific triggers pointing at specific files: this happened, so write it here.
