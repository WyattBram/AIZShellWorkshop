# Part 2 — Workshop (20 min)

Repo branches (public starter repo): `00-broken`, `01-coding-standards`, `02-documentation`, `03-testing`, `04-index`, `main` (reference).
Each non-`main` branch is **independent** — it branches directly from `00-broken` and adds only its own CLAUDE.md section. Each has a `DEMO.md` with the exact prompt to run and what to expect.
Before the session: `pip install -r requirements-dev.txt` once, so `flake8` is ready for stage 1.

**Mechanic:** for every stage, checkout the branch, **start a fresh Claude Code session** (context must not carry over from the previous stage), run the demo prompt, read the result out loud.

## Live break (4 min)

1. `git checkout 00-broken`
2. Open the repo in Claude Code. No CLAUDE.md exists, but `documents/` (ARCHITECTURE, CHANGELOG, DECISIONS, INDEX) is already there, prefilled. Show it.
3. Ask: *"Add a way to cancel a task. You decide whether it should remove the task entirely or just mark it cancelled. Make the change directly."* (grant edit permission live)
   - Model makes a reasonable code change, but doesn't check `flake8` compliance, doesn't write a test, and leaves all the `documents/` files untouched even though this is exactly the kind of tradeoff `DECISIONS.md` exists for.
4. Land the line: **"Nothing here is wrong — it's a perfectly reasonable choice. But we had real project documents sitting right there, and nothing said when to use them. This is what everyone builds at a hackathon, and it's why it falls apart under judging."**

## Add the guardrails (hands-on, ~14 min, ~3-4 min per stage)

For each stage: `git checkout 0X-stage-name`, start a **fresh** Claude Code session, open `CLAUDE.md`, read it together, then run that stage's `DEMO.md` prompt and compare to what the room just saw on `00-broken`.

1. **`01-coding-standards`** — full PEP8 rule set (naming, spacing, line length, docstrings), enforced by `flake8`.
   Prompt is a fairly substantial, normally-phrased feature request — a manager-facing weekly status report covering overdue/due-soon/completed counts, a natural-language sentence per section, and an urgency label — with no dictated names or wording. More surface area means more chances for a real violation to slip in. On `00-broken`, `flake8 app tests` reliably fails with several `E501` line-length violations across both files. On this branch, the same feature gets built with every long line wrapped to fit, and `flake8` passes clean. *"Nobody told the model to write bad lines — a normal, moderately complex request produced several anyway. This isn't a vibe check anymore, it's a pass/fail signal from a real tool."*

2. **`02-documentation`** — trigger rules for `documents/ARCHITECTURE.md`, `CHANGELOG.md`, `DECISIONS.md`.
   A bigger ask this time — a task archiving feature (new field, several new functions across three files, a real cap-counting tradeoff). On `00-broken`, the model reasons about the tradeoff out loud and makes a good call, but `documents/` sits untouched. On this branch, `ARCHITECTURE.md` gets several file descriptions rewritten, `CHANGELOG.md` gets a real multi-bullet dated entry, and `DECISIONS.md` gets a genuine new entry on the cap tradeoff. *"The documents existed the whole time, and the reasoning was just as good either way. The gap was never 'no docs' — it was 'no one said where that thinking is supposed to end up.'"*

3. **`03-testing`** — coverage requirement, actually run `pytest`, report the result.
   Same "add a function" style prompt. Now it writes a real test and reports "N passed" instead of just asserting the change works. *"'Should pass' becomes an actual, checkable number."*

4. **`04-index`** — CLAUDE.md tells the model to read `documents/INDEX.md` first, before anything else.
   Ask (read-only, use `--output-format json` and read `num_turns`): *"If I wanted to add a due-date reminder feature, which files would I need to touch and in what order?"* On `00-broken` this typically takes **5-6 turns** — the model opens `models.py`, `storage.py`, `api.py`, `config.py` one at a time to rebuild the map itself. On this branch it takes **2-3 turns** — the index is a compact routing table (topic → file), not a full description, so a lookup replaces most of the exploration. *"A good index is a trade: a small, fixed cost paid once, against a bigger cost paid every session it's missing. Turn count makes that trade measurable instead of just asserted."*
   Worth calling out explicitly: `INDEX.md` isn't the same file as `ARCHITECTURE.md` from stage 2. `ARCHITECTURE.md` describes the project — it's documentation. `INDEX.md` only routes — topic in, filename out — which is why it stays small and cheap to read even as the project grows.

**Have students do this on their own repo/idea in parallel** if time allows near the end of stage 4 — even 2 minutes of "write one line for your own project" cements it.
