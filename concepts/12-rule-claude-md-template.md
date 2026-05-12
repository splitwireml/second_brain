---
title: 12-Rule CLAUDE.md Template
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [claude-code, agent, coding, prompting, prompt-engineering, reliability, agent-tool]
sources: [raw/articles/xarticle-karpathys-4-claudemd-rules-cut-claude-mistakes-fro-2053116311132155938.md]
related_entity: [[mnilax]]
---

# 12-Rule CLAUDE.md Template

> A behavioral contract for Claude Code that reduced mistakes from 41% to 3% across 30 codebases over 6 weeks.

## Origin

In January 2026, [[andrej-karpathy]] complained about Claude writing code with three failure modes. [[forrest-chang]] packaged these into a 4-rule CLAUDE.md template that reached 120K GitHub stars.

In May 2026, [[mnilax]] tested the original 4 rules on 30 codebases over 6 weeks. The rules worked (mistakes dropped from ~40% to ~3% on tasks that played to their strengths), but the template was built for January 2026's problems — agent orchestration issues like multi-step workflows, hook cascades, and skill loading conflicts didn't exist yet.

So Mnimiy added 8 more rules, creating a 12-rule template that covered both the original code-writing problems AND the May 2026 agent-orchestration problems.

## The 12 Rules

### Original 4 (Karpathy, January 2026)

1. **Think Before Coding** — State assumptions explicitly. Surface tradeoffs. Ask before guessing. Push back when simpler approach exists. Stop when confused.

2. **Simplicity First** — Minimum code that solves the problem. No speculative features. No abstractions for single-use code. Test: would a senior engineer call it overcomplicated?

3. **Surgical Changes** — Touch only what you must. Don't "improve" adjacent code, comments, or formatting. Match existing style.

4. **Goal-Driven Execution** — Define success criteria. Loop until verified. Don't follow steps — define success and iterate.

### 8 Added Rules (Mnimiy, May 2026)

5. **Use the model only for judgment calls** — Claude for classification, drafting, summarization, extraction. NOT for routing, retries, deterministic transforms.

6. **Token budgets are not advisory** — Per-task: 4,000 tokens. Per-session: 30,000 tokens. Surface the breach. Do not silently overrun.

7. **Surface conflicts, don't average them** — If two patterns contradict, pick one (more recent / more tested). Explain why. Don't blend.

8. **Read before you write** — Before adding code, read exports, immediate callers, shared utilities. "Looks orthogonal" is dangerous.

9. **Tests verify intent, not just behavior** — A test that can't fail when business logic changes is wrong. Encode WHY behavior matters.

10. **Checkpoint after every significant step** — Summarize what was done, what's verified, what's left. If you lose track, stop and restate.

11. **Match the codebase's conventions, even if you disagree** — Conformance > taste inside the codebase.

12. **Fail loud** — "Completed" is wrong if anything was skipped silently. "Tests pass" is wrong if any were skipped.

## Key Insight: Behavioral Contract

> CLAUDE.md is not a wishlist. It's a behavioral contract that closes specific failure modes you've observed.

Every rule should answer: **what mistake does this prevent?**

## Results

Tested across 30 codebases, 50 representative tasks, 6 weeks:

| Configuration | Mistake Rate | Compliance |
|---|---|---|
| No CLAUDE.md | 41% | — |
| 4 rules (Karpathy) | ~3% (on applicable tasks) | 78% |
| 12 rules (Mnimiy) | ~3% | 76% |

Going from 4 rules to 12 added almost no compliance overhead but cut mistake rate by another 8 points. The new rules cover failure modes the original 4 didn't address.

## Where Original Template Silently Breaks

1. **Long-running agent tasks** — No budget rule, no checkpoint rule, no fail-loud rule
2. **Multi-codebase consistency** — "Match existing style" assumes one style; in monorepos, Claude picks randomly
3. **Test quality** — Goal-Driven Execution treats "tests pass" as success; doesn't require meaningful tests
4. **Production vs prototype** — Simplicity First overfires on early-stage code that legitimately needs scaffolding

## Usage

```bash
# 1. Append Karpathy's 4-rule baseline
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md

# 2. Paste rules 5-12 below
```

Keep total under 200 lines. Past 200, compliance falls off. A 6-rule CLAUDE.md tuned to your actual failure modes beats a 12-rule one with rules you'll never need.

## Related

- [[claude-code]] — Target agent
- [[andrej-karpathy]] — Original rules author
- [[forrest-chang]] — Viral packaging
- [[mnilax]] — Extended to 12 rules
- [[skillify]] — Garry Tan's methodology for converting failures into skills
- [[agent-orchestration-patterns]] — Multi-agent orchestration patterns