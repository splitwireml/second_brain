---
title: Karpathy CLAUDE.md
created: 2026-04-23
updated: 2026-05-12
type: concept
tags: [claude-code, code-generation, skill, agent]
sources: [raw/articles/defileo-agentic-llm-stack-2026-04-20.md, raw/articles/xarticle-karpathy-claude-md-12-rules-2053116311132155938.md]
author: [[defileo]]
---

# Karpathy CLAUDE.md

A four-principle behavioral configuration file for Claude Code derived from Karpathy's documented complaints about LLM coding mistakes. Published by [[defileo]].

## The Four Principles

1. **Think Before Coding** — Don't assume, surface tradeoffs, state assumptions explicitly, push back when warranted
2. **Simplicity First** — Minimum code that solves the problem, nothing speculative, bias toward caution over speed
3. **Surgical Changes** — Touch only what you must, match existing style, don't improve unrelated code
4. **Goal-Driven Execution** — Transform tasks into verifiable goals with explicit success criteria

## Key Design Tradeoffs

- **Biases caution over speed** — intentional friction for complex tasks, simpler tasks use judgment
- **No speculative features** — only what was explicitly asked for
- **Clean diffs** — every changed line traces directly to user request

## Installation

**Option A — Plugin (all projects):**
```
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

**Option B — Per-project:** Copy the file into the repo directly.

## Relationship to Other Patterns

- Extends [[caveman-claude-skill]] token reduction with behavioral guidelines
- Related to [[prompt-engineering-patterns]] for high-level prompting strategy
- Companion to [[rtk-rust-token-killer]] for input token optimization
- Related to [[claude-code-systems-design]] — architectural approach to building consistent, scalable [[claude-code]] outputs

## Related
## Extension: 12-Rule Version by Mnilax

[[mnilax]] tested the 4-principle template on 30 codebases over 6 weeks. Mistakes dropped from ~41% to under 3% on tasks within the rules' scope. However, the May 2026 Claude Code ecosystem introduced new failure modes not covered by the original 4 rules:

- Agent fights between skill-loaders
- Hook cascades across sessions
- Multi-step workflows breaking across context windows
- Skill loading conflicts

Mnilax extended the template to **12 rules** (original 4 + 8 new). The full template is at [[12-rule-claude-md-template]].

## Related
- [[defileo]] — Original author
- [[mnilax]] — Extended to 12 rules
- [[12-rule-claude-md-template]] — The 12-rule template
- [[claude-code]] — Target platform
