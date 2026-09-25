# Demo script — 04-index

**Prompt (same on both sides, read-only):**
> Without editing anything: if I wanted to add a due-date reminder feature, which files would I need to edit? Just tell me the plan.

**Measure tool calls, not turns** — turn count is noisy, `Read` count is stable. This one run gives you:

- **`Read` count** — how many times Claude opened a file; the core metric, since each `Read` permanently adds that file to context.
- **`total_cost_usd`** — dollar cost of the run; rises with `Read` count but also answer length, so noisier.
- **`duration_ms`** — wall-clock time for the run; reflects tool-call round trips plus generation time.

```
claude -p --output-format stream-json --verbose "<prompt>" 2>&1 | tee result.jsonl | grep -o '"name":"Read"' | wc -l

python -c "
import json
lines = open('result.jsonl').read().splitlines()
d = json.loads(lines[-1])
print('total_cost_usd:', d['total_cost_usd'])
print('duration_ms:', d['duration_ms'])
"
```

**Before (00-broken, no CLAUDE.md):** the model has to open `models.py`, `storage.py`, `api.py`, and `config.py` — sometimes more than once — to work out what already exists (`due`, `is_overdue()`) before it can answer. Typically **3-10 `Read` calls**, run to run.

**After (this branch):** CLAUDE.md points straight at `documents/INDEX.md` and tells the model to read it first. `INDEX.md` is deliberately *not* `ARCHITECTURE.md` — it doesn't describe what each file does, it's a compact routing table: "looking for X? check Y." The same question now consistently takes **fewer `Read` calls** than the no-index baseline, because the model looks up which file owns task-data access instead of opening every file to rediscover it.

**Point to make:** every `Read` call pulls that file's full content into context — permanently, for the rest of the session. Fewer reads doesn't just mean a faster answer once, it means the context window fills up slower for everything that comes after. `ARCHITECTURE.md` and `INDEX.md` do different jobs: `ARCHITECTURE.md` is an artifact Claude *writes to* — documentation, output, something a human or a future session reads to understand the project, and it grows as the project grows. `INDEX.md` is something Claude both *reads and writes* — a working lookup table it consults first and keeps current, not a description but a pointer, so it stays small and cheap no matter how big the project gets. That's the trade a good index makes: pay a small, fixed context cost up front so every session after it spends less context rediscovering the same map.

**Not on Claude Code?** `other-tools/` has this same index content ported to `.github/copilot-instructions.md` (Copilot) and `.cursor/rules/index.mdc` (Cursor) — copy whichever matches your stack. The tool-call measurement itself is Claude Code-specific, but the pattern (point at a compact lookup table before exploring) applies wherever your tool reads a persistent instructions file.
