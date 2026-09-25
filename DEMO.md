# Demo 02-documentation

**Prompt :**
> Add a task archiving feature: users should be able to archive a task instead of just completing or deleting it, archived tasks should be excluded from the normal task list but still queryable separately, and there should be a way to restore an archived task back to active. You decide the details — whether archiving is a flag or a separate store, how restore should work, and whether archived tasks should still count toward the MAX_TASKS cap. Wire it up across models.py, storage.py, and api.py. Make the change directly.

This is a bigger, multi-part feature on purpose — a new field, several new functions across three files, and at least one genuine design tradeoff (does archiving still count toward the task cap?). More surface area means more for the documentation rules to actually catch.

**Before (00-broken, no CLAUDE.md):** the repo already has `documents/ARCHITECTURE.md`, `CHANGELOG.md`, and `DECISIONS.md` sitting there, prefilled. The model makes a real, well-reasoned code change — new `archived` field, `archive()`/`restore()`/`archived()` on `TaskStore`, three new API functions, a real decision about the `MAX_TASKS` cap — and even states its reasoning in the response. But you can see that it did not add any documentation. All three documents sit untouched.

**After (this branch):** same prompt, same feature, but now it will add documentation:
- `documents/ARCHITECTURE.md` gets its file descriptions updated to mention the new field and functions.
- `documents/CHANGELOG.md` gets a real dated entry describing what changed, without touching the existing "Initial" entry.
- `documents/DECISIONS.md` gets a genuine new entry explaining why archived tasks don't count toward the `MAX_TASKS` cap, and why the alternative (counting them) would create unnecessary friction.

(Exactly which descriptions get touched and how many bullet points appear can vary run to run, since the model's output isn't fixed, but all three documents reliably get updated.)

**Point to make:** it matters that the model documents what it does as it does it. If documentation only happens later, or not at all, it goes stale and stops matching the real code. Documenting changes in the moment keeps the record accurate, and it means the model itself always has an up-to-date picture of what's going on in your project the next time it reads these files.

**Not on Claude Code?** `other-tools/` has this same documentation content ported to `.github/copilot-instructions.md` (Copilot) and `.cursor/rules/documentation.mdc` (Cursor) — copy whichever matches your stack.
