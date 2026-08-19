# Coding standards

- Type hints on every parameter and return value for new functions, even where existing code is inconsistent about it. Don't copy the gaps.
- New lookups/mutations on `TaskStore` should guard against a missing id the way `get()` does (`.get()`, return `None`), not let `KeyError` bubble up like `complete()` does. That inconsistency is a known issue, not a pattern to extend.
- Commit messages: one line, imperative mood, no period (`add cancel_task`, not `Added cancel_task.`).
- Be concise. Show the code first with no more than one short line of rationale per file. Don't narrate alternatives you rejected, don't explain your reasoning process, don't restate the request.
