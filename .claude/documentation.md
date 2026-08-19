# Documentation

This project keeps its own history in `documents/`. Naming and code-comment style are covered by coding-standards.md — this is about project-level records, not code style.

- **When you add, remove, or change the purpose of a file** — update `documents/ARCHITECTURE.md` so the file tree and the one-line description of each file stay accurate.
- **After making any code change** — append an entry to `documents/CHANGELOG.md` describing what changed and why. Don't touch older entries.
- **When you make a non-obvious tradeoff** — pick one approach over another for a real reason, not the only option available — add an entry to `documents/DECISIONS.md` explaining the choice and why the alternative was rejected. Routine changes with an obvious "only way to do it" don't need an entry.
- **When you add a new document, module, or major concern** — add a row to `documents/INDEX.md` pointing at it. `INDEX.md` is a lookup table, not a description — keep entries to one line.

If none of the above applies to a change, don't touch `documents/` just to have touched it.
