# Same patterns, other tools

This workshop's live demos are Claude Code-specific (branches, `CLAUDE.md`, `claude -p` for measuring before/after). The four patterns themselves — coding standards, documentation, testing, indexing — aren't. This folder has the same content ported to two other tools' native formats, so you can use them on your own project regardless of what you're using at the hackathon.

## GitHub Copilot

Copy `copilot/.github/copilot-instructions.md` into your repo at `.github/copilot-instructions.md`. Copilot reads it automatically for chat, inline completions, and PR reviews — no other setup needed.

## Cursor

Copy the contents of `cursor/.cursor/rules/` into your repo's `.cursor/rules/` directory. Each `.mdc` file is one pattern, same split as this project's `.claude/` folder. `index.mdc` and `documentation.mdc` are set to `alwaysApply: true` (project-wide); `coding-standards.mdc` and `testing.mdc` are scoped with `globs` so they only kick in on relevant files — adjust the globs for your own project's structure.

## Adapting either one

Everything in both is specific to this sample project (`TaskStore`, `documents/ARCHITECTURE.md`, `flake8`). Swap in your own project's real files, commands, and conventions — the four *kinds* of rule are what to keep, not the exact wording.
