# TaskTracker — Copilot instructions

Copy this file into `.github/copilot-instructions.md` at the root of your repo (create the `.github/` directory if it doesn't exist). Copilot reads it automatically for every chat response, inline completion, and PR review in this repo.

This is the same content as this project's `CLAUDE.md` + `.claude/` files, ported to Copilot's single-file format instead of split by topic.

## Project index

Before doing anything else in this project, read `documents/INDEX.md`. It's a compact lookup table — topic or question, mapped to which file actually has the answer — not a full description of anything. Use it to go straight to the right file instead of opening files one at a time to find it.

Keep `documents/INDEX.md` current: when a new document, module, or major concern gets added, add a row pointing at it.

## Coding standards

This project follows PEP 8. Checked by `flake8` (config in `.flake8`) — run `flake8 app tests` after any change and fix anything it reports before calling a change done.

### Naming

- **Function / method / variable:** lowercase, words separated by underscores (snake_case) — `my_function`, `car_color`. A single lowercase letter is fine for a loop/math variable inside a function (`i`, `j`).
- **Constant:** uppercase, words separated by underscores — `MY_CONSTANT`.
- **Class:** capitalize each word, no underscores (PascalCase) — `CarModel`.
- **Module:** short, lowercase, underscores if needed — `my_module.py`.
- **Package:** short, lowercase, no underscores — `mypackage`.

### Layout

- 4 spaces per indent level, never tabs.
- Two blank lines around top-level functions and classes; one blank line around method definitions inside a class.
- Max line length 80 characters, including comments. Wrap and indent continuation lines so they're visibly not a new statement.
- One statement per line.

### Spacing

- A single space around `=` for assignment and around comparison/math operators, grouped sensibly (`c = (a + b) * (a - b)`, not `c=(a+b)*(a-b)`).
- No space around `=` for a default parameter value (`def f(x=0):`, not `def f(x = 0):`).
- Don't pad assignment/annotation operators to line them up in a column.

### Comments and docstrings

- Every public function, class, and method gets a docstring, starting and ending with `"""`.
- A one-line docstring can be on a single line; a multi-line docstring lists each argument on its own line and has a blank line before the closing `"""`.
- Write comments as whole sentences in plain English. Keep them accurate — an outdated comment is worse than none.
- Block comments: each line starts with `#`; separate paragraphs with a line containing a single `#`. Use inline comments sparingly, never to restate the obvious.

## Documentation

This project keeps its own history in `documents/`. Naming and code-comment style are covered above — this is about project-level records, not code style.

- **When you add, remove, or change the purpose of a file** — update `documents/ARCHITECTURE.md` so the file tree and the one-line description of each file stay accurate.
- **After making any code change** — append an entry to `documents/CHANGELOG.md` describing what changed and why. Don't touch older entries.
- **When you make a non-obvious tradeoff** — pick one approach over another for a real reason, not the only option available — add an entry to `documents/DECISIONS.md` explaining the choice and why the alternative was rejected. Routine changes with an obvious "only way to do it" don't need an entry.
- **When you add a new document, module, or major concern** — add a row to `documents/INDEX.md` pointing at it. `INDEX.md` is a lookup table, not a description — keep entries to one line.

If none of the above applies to a change, don't touch `documents/` just to have touched it.

## Testing

- Every new function that touches `TaskStore` or `app/api.py` gets a matching test in `tests/`. No exceptions for "small" changes.
- After writing or changing a test, actually run `python -m pytest tests/ -q` and report the result. Don't just say a test "should pass."
- Test behavior, not implementation: assert on what a function returns or raises, not on internal calls it happens to make.
