# Index

Quick lookup — where to find something, without opening files to check.

| Looking for...                          | Go to                          |
|------------------------------------------|---------------------------------|
| What each file/module does                | `documents/ARCHITECTURE.md`     |
| Why a past tradeoff was made this way      | `documents/DECISIONS.md`        |
| What changed and when                      | `documents/CHANGELOG.md`        |
| Naming, formatting, docstring rules        | `.claude/coding-standards.md`   |
| When to update which document              | `.claude/documentation.md`      |
| Test coverage requirements                  | `.claude/testing.md`            |
| The `MAX_TASKS` cap / env var behavior     | `app/config.py`, `documents/DECISIONS.md` |
| Task fields (`done`, `due`, `tags`, etc.)  | `app/models.py`                 |
| All CRUD operations on tasks                | `app/storage.py`                |
| The public functions other code calls      | `app/api.py`                    |

Keep this table current: when a new document, module, or major concern gets added, add a row here pointing at it.
