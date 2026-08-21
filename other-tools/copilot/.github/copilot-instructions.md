# TaskTracker — Copilot instructions (stage: coding-standards)

Copy this file into `.github/copilot-instructions.md` at the root of your repo (create the `.github/` directory if it doesn't exist). Copilot reads it automatically for every chat response, inline completion, and PR review in this repo.

Same content as this branch's `CLAUDE.md`, ported to Copilot's format.

# Coding standards

This project follows PEP 8. Checked by `flake8` (config in `.flake8`) — run `flake8 app tests` after any change and fix anything it reports before calling a change done.

## Naming

- **Function / method / variable:** lowercase, words separated by underscores (snake_case) — `my_function`, `car_color`. A single lowercase letter is fine for a loop/math variable inside a function (`i`, `j`).
- **Constant:** uppercase, words separated by underscores — `MY_CONSTANT`.
- **Class:** capitalize each word, no underscores (PascalCase) — `CarModel`.
- **Module:** short, lowercase, underscores if needed — `my_module.py`.
- **Package:** short, lowercase, no underscores — `mypackage`.

## Layout

- 4 spaces per indent level, never tabs.
- Two blank lines around top-level functions and classes; one blank line around method definitions inside a class.
- Max line length 80 characters, including comments. Wrap and indent continuation lines so they're visibly not a new statement.
- One statement per line.

## Spacing

- A single space around `=` for assignment and around comparison/math operators, grouped sensibly (`c = (a + b) * (a - b)`, not `c=(a+b)*(a-b)`).
- No space around `=` for a default parameter value (`def f(x=0):`, not `def f(x = 0):`).
- Don't pad assignment/annotation operators to line them up in a column.

## Comments and docstrings

- Every public function, class, and method gets a docstring, starting and ending with `"""`.
- A one-line docstring can be on a single line; a multi-line docstring lists each argument on its own line and has a blank line before the closing `"""`.
- Write comments as whole sentences in plain English. Keep them accurate — an outdated comment is worse than none.
- Block comments: each line starts with `#`; separate paragraphs with a line containing a single `#`. Use inline comments sparingly, never to restate the obvious.
