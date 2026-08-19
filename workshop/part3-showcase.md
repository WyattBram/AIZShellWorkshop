# Part 3 — Showcase + Ending (5-10 min)

1. `git checkout main`
2. Open the tree:

   ```text
   CLAUDE.md               <- entry point, @imports only
   .claude/
     index.md                <- read documents/INDEX.md first, before anything else
     coding-standards.md    <- backed by an actual flake8 config, not just prose
     documentation.md        <- points at documents/, not a generic "write docs" rule
     testing.md
   .flake8
   requirements-dev.txt
   documents/
     ARCHITECTURE.md         <- describes the project (grows with it)
     CHANGELOG.md
     DECISIONS.md
     INDEX.md                  <- routes to the project (stays small)
   ```

3. Point out: this is the exact same four things everyone just built, live, in the last 20 minutes — just reorganized so each concern lives in its own reviewable file instead of one growing monolith. Nothing here required new skills, only organization.

4. Point out `index.md` is listed first in `CLAUDE.md`'s imports, on purpose — it's not a rule about output, it's a rule about where the model spends its first couple of turns. *"Read the map before wandering the halls."*

5. Point out `INDEX.md` and `ARCHITECTURE.md` are deliberately two different files, not one. `ARCHITECTURE.md` is documentation — it describes the project and grows as the project grows. `INDEX.md` only routes — topic in, filename out — so it stays small and cheap to consult no matter how big everything else gets. `documentation.md` even has its own trigger for keeping `INDEX.md` current, separate from the other three.

6. Point out `coding-standards.md`'s linter link specifically — it's the one guardrail in this workshop with an objective, automatable pass/fail check instead of a judgment call. *"When you can turn a standard into a tool that says yes or no, do that."*

7. **The line to land:** *"This is what a strong, mindful-AI solution looks like — safe, accountable, repeatable, and trustworthy. Not because the model is smarter here than it was on `00-broken` — it's the same model. Because someone wrote down what 'good' means for this project, once, instead of leaving it to be re-guessed every session."*

8. **Direct hackathon tie-in:** *"When judges open your repo in two hours, a CLAUDE.md like this is one of the fastest signals you can give that your team worked like a real engineering team, not just shipped a demo. Copy this pattern into your own repo tonight — five minutes, and every AI-assisted commit after that inherits it."*

9. Close with the takeaway, stated plainly: *"You leave with a hardened AI assistant you built yourself, a mental model for four guardrail patterns — coding standards, documentation, testing, and giving the model a fast way to find things before it starts guessing — and a concrete picture, from this reference solution, of what a polished, trustworthy AI-assisted project looks like. Go build."*
