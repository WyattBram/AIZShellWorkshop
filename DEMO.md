# Reference solution — main

This is the "claude brain" for the project: a root `CLAUDE.md` that imports four focused files under `.claude/`, instead of one growing monolith.

```text
CLAUDE.md               <- entry point, just a table of contents via @imports
.claude/
  index.md                <- stage 4: read documents/INDEX.md first, before anything else
  coding-standards.md    <- stage 1: full PEP8 rule set, enforced by flake8
  documentation.md        <- stage 2: trigger rules for documents/ARCHITECTURE, CHANGELOG, DECISIONS, INDEX
  testing.md               <- stage 3: coverage requirement, actually running the suite
.flake8                   <- lint config, scoped to exactly this project's standards
requirements-dev.txt      <- flake8 + pep8-naming + flake8-docstrings
documents/
  ARCHITECTURE.md         <- prefilled: file tree + one-line purpose per file
  CHANGELOG.md             <- prefilled: append-only log of code changes
  DECISIONS.md             <- prefilled: log of non-obvious tradeoffs and why
  INDEX.md                  <- prefilled: compact lookup table, topic -> which file has the answer
```

**Why split it up:** each file stays reviewable on its own, in a PR, by whoever owns that concern. A monolithic CLAUDE.md is exactly the kind of file nobody rereads once it's 200 lines — split by topic, each piece stays legible and someone can update `testing.md` without touching `coding-standards.md`.

**Why `INDEX.md` and `ARCHITECTURE.md` are two different files, not one:** `ARCHITECTURE.md` is documentation — a description a human or a future session reads to understand the project, and it grows as the project grows. `INDEX.md` is a working lookup table — topic in, filename out, nothing else — that stays small forever because it only ever holds pointers. `index.md` tells the model to read the cheap one first; `documentation.md` tells it to keep the cheap one current whenever something new gets added, alongside the other three documents.

**Why `coding-standards.md` gets an actual linter:** naming/spacing/docstring rules are the one guardrail in this workshop with an objective, automatable pass/fail check. `flake8 app tests` either exits 0 or it doesn't — no need to eyeball whether the model "felt" consistent.

**Why `documentation.md` points at specific files instead of "write docs":** the documents already existed and were prefilled from day one — the gap was never "no docs," it was "no trigger telling the assistant when a doc needs updating." Four files, four distinct triggers: structure changed → ARCHITECTURE, anything changed → CHANGELOG, a real tradeoff got made → DECISIONS, something new got added → INDEX.

**The takeaway for the room:** every one of these files answers the same question — "what would a good, careful teammate already know before touching this code?" A CLAUDE.md is just that knowledge, written down once, instead of re-explained every session.
