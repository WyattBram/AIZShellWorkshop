# Part 1 — Explain the Workshop Challenge (10 min)

## 1. What to expect (2 min)

- 45 minutes, three parts: explain → break something on purpose and fix it → reveal the polished version.
- You'll leave with an actual hardened CLAUDE.md you built yourself, on your own machine, plus the mental model behind it.
- This isn't a security talk. It's about a skill that applies to literally anything you build at this hackathon.

## 2. Where the industry is actually heading (5 min)

**The claim:** writing code, line by line, is not the bottleneck anymore, and it's not where your leverage as an engineer comes from. The bottleneck is *specifying intent clearly enough that a capable system can execute it correctly* — and then *verifying it actually did*.

- Every senior engineer in industry right now is spending more of their week reviewing, directing, and correcting AI-generated work than typing from scratch. That's not a future trend, that's this year.
- The skill that's actually scarce: writing down what "correct" means for your project *before* you ask for the work, so the answer is checkable instead of vibes-based.
- A CLAUDE.md (or system prompt, or spec, or design doc — the artifact has many names) is that skill made concrete. It's not a nice-to-have wrapper around "real" engineering — writing it well *is* the engineering work now.
- Enterprise-ready, industry-standard software isn't defined by clever code anymore. It's defined by: is the standard stated, is it documented, is it tested, does the assistant know where to look before it starts guessing. Those are exactly the four things this workshop builds, hands-on, in the next 20 minutes.
- One of today's guardrails even has an objective, automatable check behind it — a linter that either passes or doesn't. Another one is measurable directly — fewer turns to the same answer. That's the model industry is actually moving toward: not "does this feel right," but "can we measure that this is actually better."

**The tie-in:** today you're going to watch an AI assistant with no instructions do reasonable-looking work that still fails an objective check, leave real project documents untouched even though they were sitting right there, and burn extra turns rediscovering things a one-page lookup table would've told it instantly. Then you're going to fix all three, the same way you'd fix it on the job.

## 3. Questions before we start (3 min)

- Pause here. Ask the room directly: anyone unclear on what we're building or why?
