# Changelog

## Other-tools ports

- Added `other-tools/` with the same 4 patterns ported to
  `.github/copilot-instructions.md` (Copilot) and `.cursor/rules/*.mdc`
  (Cursor), for students not using Claude Code.

## Initial

- Added `Task` model, `TaskStore` (in-memory, capped at `MAX_TASKS`), and the
  `api.py` wrapper functions: `create_task`, `complete_task`, `get_task`,
  `list_by_tag`.
- Added a test for the create/get round trip.
