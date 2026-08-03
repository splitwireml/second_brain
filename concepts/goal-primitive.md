---
title: "/goal Primitive"
created: 2026-05-19
updated: 2026-08-03
type: concept
tags: [tools, agent, workflow, orchestration, delegation]
sources: [raw/articles/xarticle-the-ultimate-guide-to-goal-2054988166541770782.md, raw/articles/xarticle-wtf-is-a-loop-part-2-the-15-loops-people-are-actua-2068426104088748331.md, raw/articles/xarticle-loop-engineering-in-5-minutes-no-code-required-2073391903819608421.md, raw/articles/xarticle-getting-started-with-loops-2074208949205881033.md, raw/articles/xarticle-how-i-get-frontier-results-from-any-model-the-harn-2074195371920666718.md, raw/articles/xarticle-codex-built-8-features-overnight-5-step-pr-loop-2073470146115490230.md, raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]
---

# /goal Primitive

A coding agent instruction format where a user defines "done" state once, and the agent works autonomously until it reaches that target. Described as a *primitive* — alongside HTTP and JSON — for coding agent workflows.

## Overview

`/goal` shifts agent interaction from *prompting* (human driving every turn) to *assigning* (agent driving toward a defined target). The user writes the done criteria, submits it once, and the agent manages the work until completion, blocking, or budget exhaustion.

Key properties:
- stays active until achieved, paused, blocked, cleared, or budget-exhausted
- lives inside interactive worker sessions rather than a one-shot prompt label
- works with verification to become a contract, not just a promise

## Distinction from /loop and /schedule

The June 20 loop roundup clarifies a confusion that shows up constantly in agent discourse: `/goal` is outcome-based, `/loop` is cadence-based while the human is still present, and `/schedule` or app-level automations are unattended routines that continue when the operator is away.^[raw/articles/xarticle-wtf-is-a-loop-part-2-the-15-loops-people-are-actua-2068426104088748331.md] The three shapes are related, but they solve different control problems.

That distinction is important because many people call every repeated agent action a "loop" when the operational risk differs sharply:

- `/goal` is best when completion can be judged against explicit evidence
- `/loop` is best for watch-and-react repetition with a human nearby
- `/schedule` is best for periodic unattended maintenance with bounded scope

ClaudeDevs' getting-started article makes `/goal` the manual, real-time version of outcome-based looping: the operator gives a completion criterion and an explicit cap such as "stop after 5 tries," then Claude Code iterates until the goal is met or the budget is exhausted. The article's Lighthouse-score example reinforces why deterministic evidence is the useful unit of a goal loop.^[raw/articles/xarticle-getting-started-with-loops-2074208949205881033.md]

## Current Implementations

Three tools currently speak the broader completion-contract idea:

| Tool | Role | Strength |
|---|---|---|
| [[codex]] (OpenAI) | Builder | Implementation from spec |
| [[claude-code]] (Anthropic) | Reviewer / worker | Goal-driven task execution with built-in loop semantics |
| [[hermes-agent]] | Orchestrator | Coordination, Kanban, handoffs, and verification discipline |

The convergence on the same primitive across three unrelated teams is what enables composition between them.

## The Three Roles

The roles stay stable even as tools change:

1. **Orchestrator** — control loop, task decomposition, worker selection, Kanban cards, background processes, dependencies, final verification
2. **Builder** — takes a spec and produces working code
3. **Reviewer** — reads builder output and finds what is wrong

## /goal as contract

Without verification, `/goal` is a fancier prompt. With verification — running the actual tests, builds, or state checks — it becomes a contract.

A strong `/goal` now tends to include four elements explicitly:^[raw/articles/xarticle-wtf-is-a-loop-part-2-the-15-loops-people-are-actua-2068426104088748331.md]

- target end state
- evidence that proves completion
- constraints on what must not change
- budget or cap on how long the agent may keep trying

The verifier closes the gap between agent self-report and actual state: agents will confidently claim success on work that was never really checked.

Phosphen's harness guide reinforces the same point with the maker/checker split: `/goal` is only safe when a separate checker or objective command owns the finish line, and the condition includes a hard stop such as an iteration, token, or time budget.^[raw/articles/xarticle-how-i-get-frontier-results-from-any-model-the-harn-2074195371920666718.md]

The AI Guides article adds a beginner-facing version of that contract: a working `/goal` needs a finish line a stranger can verify, explicit file/folder scope, an internal checker, and both success and failure stop rules. Its examples are intentionally mundane — research briefs, content audits, weekly reports — which makes the primitive legible outside software engineering.^[raw/articles/xarticle-loop-engineering-in-5-minutes-no-code-required-2073391903819608421.md]

Hanako's eval-engineering course makes the external-check boundary even sharper: an agent stopping tool calls has only ended its turn, while verified completion is the only acceptable run terminator. Low grounding rejects a handoff, schema failure blocks an edge, and suspected fabrication quarantines a branch. The `/goal` contract therefore needs a verdict that changes the run, not merely a score on a dashboard. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

## `/goal` inside a manager-worker loop

Paul Solt's [[manager-worker-pr-loop]] uses `/goal` as a worker-level completion contract: the manager applies it to each task thread so workers continue toward merge-ready instead of stopping after an implementation pass with failing tests. This is a source-specific implementation of the broader rule that goals need evidence, constraints, and a budget; the manager still owns routing and the final merge decision.^[raw/articles/xarticle-codex-built-8-features-overnight-5-step-pr-loop-2073470146115490230.md]

## Multiple Goals

Parallel `/goal`s work across clean boundaries such as different repos, branches, worktrees, or packages. The bad pattern is multiple workers editing the same file simultaneously.

## Related

- [[loop-engineering]]
- [[model-agnostic-agent-harness]]
- [[claude-code]]
- [[codex]]
- [[hermes-agent]]
- [[matt-van-horn]]
- [[phosphenq]]
- [[manager-worker-pr-loop]]
- [[paul-solt]]
