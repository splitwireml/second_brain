---
title: Andrej Karpathy
created: 2026-05-11
updated: 2026-05-11
type: entity
tags: [person, ai-researcher]
sources: [raw/articles/xarticle-karpathys-4-claudemd-rules-cut-claude-mistakes-fro-2053116311132155938.md]
---

# Andrej Karpathy

> AI researcher, educator, and former Tesla Autopilot director. Known for building AI systems and teaching neural networks/CS231n at Stanford.

## Profile

- **Known for**: Neural network education (CS231n), Tesla Autopilot, Eureka AI agent, OpenAI founding member
- **Current**: Runs [karpathy.ai](https://karpathy.ai), micro-company of ~2 people
- **X**: [@karpathy](https://x.com/karpathy)

## CLAUDE.md Rules (January 2026)

In January 2026, Karpathy posted a thread complaining about how Claude (and similar coding agents) writes code — identifying three failure modes:

1. **Silent wrong assumptions** — Claude makes guesses without surfacing them
2. **Over-complication** — Claude adds speculative abstractions and features beyond what's needed
3. **Orthogonal damage** — Claude modifies code it shouldn't have touched

These complaints were packaged by [[forrest-chang]] into a 4-rule CLAUDE.md template that went viral (120K+ stars on GitHub). The 4 rules:

- **Rule 1 — Think Before Coding**: State assumptions explicitly, surface tradeoffs, ask before guessing
- **Rule 2 — Simplicity First**: Minimum code that solves the problem, no speculative features
- **Rule 3 — Surgical Changes**: Touch only what you must, don't refactor what's not broken
- **Rule 4 — Goal-Driven Execution**: Define success criteria, loop until verified, don't prescribe steps

## Impact

Forrest Chang's packaging of Karpathy's complaints into a 4-rule CLAUDE.md file became the fastest-growing single-file repo of 2026:
- 5,828 stars in the first day
- 60,000 bookmarks in two weeks
- 120,000 stars today

## Related

- [[claude-code]] — Target of Karpathy's original complaints
- [[forrest-chang]] — Who packaged the complaints into the viral CLAUDE.md template
- [[mnilax]] — Extended Karpathy's 4 rules to 12 rules after testing on 30 codebases