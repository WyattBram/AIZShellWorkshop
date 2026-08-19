# Demo script — 04-index

**Prompt (same on both sides, read-only — use `--output-format json` so you can read `num_turns`):**
> Without editing anything: if I wanted to add a due-date reminder feature, which files would I need to touch and in what order? Just tell me the plan.

```
claude -p --output-format json "<prompt>"
```

Pull `num_turns` out of the JSON result (or just count the tool calls scrolling by in an interactive session).

**Before (00-broken, no CLAUDE.md):** the model has to open `models.py`, `storage.py`, `api.py`, and `config.py` one at a time to work out what already exists (`due`, `is_overdue()`) before it can answer. Typically **5-6 turns**.

**After (this branch):** CLAUDE.md points straight at `documents/ARCHITECTURE.md` and tells the model to read it first. The same question now gets answered in **2 turns** — one to read the index, one to answer — because the map of what every file does was already handed over instead of rediscovered.

**Point to make:** this isn't magic, it's a trade. `ARCHITECTURE.md` costs a few hundred tokens of context every session — small, fixed, paid once up front. The alternative is the model re-deriving that same map by opening files, every single time, which costs more and doesn't get cheaper the second time someone asks. A good index is worth more than it costs, and turn count is a real, checkable way to show that instead of just asserting it.
