# Architecture

```text
app/
  __init__.py     TaskTracker application package (empty besides its docstring).
  config.py       Project-wide configuration values (MAX_TASKS, read from the
                  TASKTRACKER_MAX_TASKS env var).
  models.py       The Task dataclass: id, title, tags, done, due, and the
                  is_overdue() check.
  storage.py      TaskStore: dict-backed, in-memory storage for tasks. All
                  reads and writes to task data go through here.
  api.py          Thin functions (create_task, complete_task, get_task,
                  list_by_tag) that wrap a single module-level TaskStore
                  instance. No HTTP layer — plain Python calls only.

tests/
  test_api.py     Tests against the api.py layer.

documents/
  ARCHITECTURE.md This file.
  CHANGELOG.md    Running log of code changes.
  DECISIONS.md    Log of non-obvious tradeoffs and why they were made.
  INDEX.md        Compact lookup table: topic/question -> which file to check.
```

Not a real service: no persistence (data is lost on restart) and no web
framework wired up despite `api.py`'s naming. It's an in-memory sample
project for practicing how to write project guidance for an AI assistant.
