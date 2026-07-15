---
title: Software Factory with Claude Code
created: 2026-06-11
updated: 2026-06-11
type: concept
tags: [claude-code, workflow, orchestration, agent, testing]
sources: [raw/articles/xarticle-how-to-build-a-software-factory-with-claude-code-t-2058832033628241931.md]
related_entity: [[sairahul1]]
author: [[sairahul1]]
---

# Software Factory with Claude Code

A structured multi-agent coding workflow proposed by [[sairahul1]] as an alternative to ad-hoc [[vibe-coding]] inside one long Claude Code chat. The core claim is that most AI coding failures are workflow failures: one session is being forced to act as analyst, architect, backend engineer, frontend engineer, tester, and reviewer all at once.

## Core idea

Instead of one overloaded conversation, the source splits delivery into a seven-agent chain with narrow scope, explicit handoffs, and three human checkpoints. The goal is not just more automation, but less silent error propagation.

## The seven roles

1. **Codebase Researcher** — maps relevant files, patterns, risks, and test impact before any implementation.
2. **Story Writer** — converts a rough request into a user story, acceptance criteria, edge cases, exclusions, and open questions.
3. **Spec Writer** — turns the approved story into a technical brief covering data model, API, frontend, tests, and risk.
4. **Backend Builder** — implements server-side code and unit tests within a constrained backend scope.
5. **Frontend Builder** — implements UI against the backend's returned contract without inventing new APIs.
6. **Test Verifier** — writes acceptance tests against the story rather than just unit tests around the implementation.
7. **Implementation Validator** — performs an independent gap review against the approved story and spec, reporting severity instead of patching code.

## Why this differs from generic subagents

This pattern is more opinionated than simple [[claude-code-subagents]]. It defines a fixed production chain, forbids scope creep between adjacent roles, and inserts approval gates between problem definition, technical design, and merge. It is closer to a reusable software-delivery harness than to ad-hoc delegation, and overlaps with the broader runtime-harness ideas in [[dynamic-workflows-in-claude-code]].

## Operational principles worth keeping

- **Explore before build** — research runs first, and is read-only.
- **Problem definition before implementation** — story and spec are separate artifacts, each reviewed by a human.
- **Hard role boundaries** — backend and frontend builders cannot edit each other's layer.
- **Acceptance before merge** — feature completion is judged by acceptance tests, not by unit tests alone.
- **Independent validation** — the final reviewer only audits; it does not self-grade by fixing its own findings.

## CLAUDE.md as project memory

The source treats [[karpathy-claude-md]]-style repo memory as foundational infrastructure rather than an optional prompt trick. CLAUDE.md stores stack facts, commands, architectural rules, and anti-patterns so each fresh Claude Code session starts with stable constraints instead of relearning them from chat history.

## Practical effect

The article's framing is that this converts AI from a faster keyboard into a coordinated team. In wiki terms, the concept sits between [[vibe-coding]], [[claude-code-subagents]], and [[dynamic-workflows-in-claude-code]]: same underlying agent primitives, but packaged as a reproducible feature factory with explicit checkpoints and testing discipline.

## Related

- [[sairahul1]]
- [[claude-code]]
- [[vibe-coding]]
- [[claude-code-subagents]]
- [[dynamic-workflows-in-claude-code]]
- [[karpathy-claude-md]]
