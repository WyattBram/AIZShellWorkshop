# Decisions

## In-memory storage, no database

`TaskStore` holds everything in a plain dict, no persistence. This is a
sample/teaching repo, not a real service — a database would add setup cost
with no benefit here. If this ever needs to survive a restart, that's a
real architectural change, not a tweak.

## MAX_TASKS is a hard cap, not a soft warning

`TaskStore.add` raises `ValueError` once `MAX_TASKS` is hit, rather than
warning and continuing. It exists for load-test throttling and is
intentional — don't remove the check to "fix" a crash; raise the cap via
the `TASKTRACKER_MAX_TASKS` env var instead.
