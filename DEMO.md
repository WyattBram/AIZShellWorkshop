# Demo script — 04-index

**Prompt (same on both sides, read-only — use `--output-format json` so you can read `num_turns`):**
> Without editing anything: if I wanted to add a due-date reminder feature, which files would I need to touch and in what order? Just tell me the plan.

```
claude -p --output-format json "<prompt>"
```

Pull `num_turns` out of the JSON result (or just count the tool calls scrolling by in an interactive session).

**Before (00-broken, no CLAUDE.md):** the model has to open `models.py`, `storage.py`, `api.py`, and `config.py` one at a time to work out what already exists (`due`, `is_overdue()`) before it can answer. Typically **5-6 turns**.

**After (this branch):** CLAUDE.md points straight at `documents/INDEX.md` and tells the model to read it first. `INDEX.md` is deliberately *not* `ARCHITECTURE.md` — it doesn't describe what each file does, it's a compact routing table: "looking for X? check Y." The same question now gets answered in **2-3 turns**, because the model looks up which file owns task-data access and reasons from that instead of opening every file to rediscover it.

**Point to make:** `ARCHITECTURE.md` and `INDEX.md` do different jobs. `ARCHITECTURE.md` is an artifact Claude *writes to* — it's documentation, output, something a human or a future session reads to understand the project. `INDEX.md` is something Claude both *reads and writes* — a working lookup table it consults first and keeps current, not a description but a pointer. As the project grows, `ARCHITECTURE.md` gets longer and more expensive to read in full; `INDEX.md` stays small because it only ever holds pointers, not content. That's the trade a good index makes: pay a small, fixed cost up front so lookup stays cheap even as everything else grows.
