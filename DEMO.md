# Demo script — 02-documentation

**Prompt (same on both sides, run with permissions granted so it can actually edit):**
> Add a task archiving feature: users should be able to archive a task instead of just completing or deleting it, archived tasks should be excluded from the normal task list but still queryable separately, and there should be a way to restore an archived task back to active. You decide the details — whether archiving is a flag or a separate store, how restore should work, and whether archived tasks should still count toward the MAX_TASKS cap. Wire it up across models.py, storage.py, and api.py. Make the change directly.

This is a bigger, multi-part feature on purpose — a new field, several new functions across three files, and at least one genuine design tradeoff (does archiving still count toward the task cap?). More surface area means more for the documentation rules to actually catch.

**Before (00-broken, no CLAUDE.md):** the repo already has `documents/ARCHITECTURE.md`, `CHANGELOG.md`, and `DECISIONS.md` sitting there, prefilled. The model makes a real, well-reasoned code change — new `archived` field, `archive()`/`restore()`/`archived()` on `TaskStore`, three new API functions, a real decision about the `MAX_TASKS` cap — and even states its reasoning in the response. But `git status` afterward shows only the `app/` files changed. All three documents sit untouched.

**After (this branch):** same prompt, same feature, but now:
- `documents/ARCHITECTURE.md` gets three of its four file descriptions rewritten to mention the new field and functions.
- `documents/CHANGELOG.md` gets a real dated entry with multiple bullet points, without touching the existing "Initial" entry.
- `documents/DECISIONS.md` gets a genuine new entry explaining why archived tasks don't count toward the `MAX_TASKS` cap, and why the alternative (counting them) would create unnecessary friction.

**Point to make:** these documents existed the whole time, and the model's reasoning was just as good without the rule — it explained its choices out loud either way. The gap was never "the model doesn't think about tradeoffs," it was "nothing told it where that thinking is supposed to end up." A bigger feature makes a bigger gap between what got reasoned about and what got written down — until something points at the files.

**Not on Claude Code?** `other-tools/` has this same documentation content ported to `.github/copilot-instructions.md` (Copilot) and `.cursor/rules/documentation.mdc` (Cursor) — copy whichever matches your stack.
