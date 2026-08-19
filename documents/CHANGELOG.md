# Changelog

## Initial

- Added `Task` model, `TaskStore` (in-memory, capped at `MAX_TASKS`), and the
  `api.py` wrapper functions: `create_task`, `complete_task`, `get_task`,
  `list_by_tag`.
- Added a test for the create/get round trip.
