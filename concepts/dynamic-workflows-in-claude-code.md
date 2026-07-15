---
title: Dynamic Workflows in Claude Code
created: 2026-06-11
updated: 2026-06-11
type: concept
tags: [workflow, claude-code, orchestration, agent, tools]
sources: [raw/articles/xarticle-a-harness-for-every-task-dynamic-workflows-in-clau-2061907337154367865.md, raw/articles/xarticle-how-to-master-dynamic-workflows-in-claude-code-6-p-2062127385923776831.md]
related_entity: [[claude-code]]
author: [[codez]]
---

# Dynamic Workflows in Claude Code

Dynamic workflows let [[claude-code]] generate a task-specific JavaScript harness at runtime instead of forcing planning, execution, verification, and synthesis through one default coding loop. Across the two ingested sources, the core claim is consistent: workflows are the structural answer when one context window is no longer enough.

## Why they exist

The workflow mental model is built around three failure modes in long single-context sessions:

- agentic laziness — the model stops after partial coverage and reports done
- self-preferential bias — the same model instance over-trusts its own prior output
- goal drift — the original objective degrades across many turns and compactions

Dynamic workflows counter those failure modes by separating work into isolated subagents, each with its own context window, explicit job, model choice, and isolation level.

## Core primitives

The underlying harness uses three main execution shapes:

- `agent()` for a focused sub-task with its own instructions and optional schema
- `parallel()` for barrier-style fan-out where all branches must finish before synthesis
- `pipeline()` for streaming stage-by-stage processing where items do not need to wait for the full batch

The practical decision rule is simple: if the next step depends on every result, use parallel; if each item can keep flowing independently, use pipeline.

## Six recurring workflow patterns

[[codez]]'s article names six patterns that show up repeatedly in production workflow design:

1. classify-and-act — route heterogeneous work after a cheap classifier inspects complexity or task type
2. fan-out-and-synthesize — split large enumerated work into parallel subagents, then merge results in one synthesis pass
3. adversarial verification — pair each worker with an independent verifier to break self-preference
4. generate-and-filter — produce many options first, then eliminate weak ones by rubric or verification
5. tournament — use pairwise comparison instead of brittle absolute scoring for ranking large sets or subjective outputs
6. loop-until-done — keep iterating until a hard stop condition is met rather than choosing an arbitrary pass count

In practice these patterns are usually composed rather than used alone: migrations combine fan-out, verification, and looping; research combines parallel evidence gathering with claim-checking and synthesis; triage combines classification, deduplication, and escalation.

## Operational guidance

The article also adds practical controls for keeping workflows useful instead of expensive:

- pair loop-heavy runs with [[goal-primitive]] so the end condition is explicit
- set token budgets up front because dynamic workflows can spend far more than a normal session
- quarantine untrusted external input so reader agents cannot also take privileged actions
- save good workflows as reusable templates or Skills once the pattern proves itself

## Related

- [[claude-code]]
- [[anthropic]]
- [[workflow]]
- [[goal-primitive]]
- [[codez]]
