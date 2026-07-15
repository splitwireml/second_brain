---
title: Manager-Worker PR Loop
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [agent, ai-agent, multi-agent, orchestration, workflow, coding, testing, github, automation]
sources: [raw/articles/xarticle-codex-built-8-features-overnight-5-step-pr-loop-2073470146115490230.md]
related_entity: [[paul-solt]]
---

# Manager-Worker PR Loop

A manager-worker agent architecture for advancing a software backlog through isolated task threads, pull requests, review feedback, and explicit merge gates. One manager thread owns coordination and completion; worker threads own bounded implementation tasks.

## The five-step loop

1. **Create task threads on worktrees** — isolate feature work so workers do not collide.
2. **Have workers implement and open PRs** — each worker produces a reviewable unit rather than mutating the main branch directly.
3. **Review on GitHub** — Codex or another review tool inspects the PR and returns actionable feedback.
4. **Route feedback back to the right worker** — the manager assigns corrections and requests re-tests.
5. **Gate merges** — require CI and tests, plus manual testing for UI-facing work, before a branch becomes merge-ready.

## Manager and worker responsibilities

The manager is an inbox and control plane, not an implementation agent. It schedules work, watches PRs, reads review feedback, checks CI, routes fixes, reports status, and decides whether the work is merge-ready. Workers implement one task and respond to feedback in their own isolated thread/worktree.

The source describes a heartbeat every 5–10 minutes that checks open PRs, review comments, and CI status. It also places `/goal` on each worker so the worker continues toward merge-ready instead of stopping after the first implementation pass.

## Proof-of-concept-first rollout

The operator did not start with a large unattended batch. The rollout was:

1. Run a proof of concept with four tasks.
2. Verify that the manager/worker pattern works.
3. Expand to another task set.
4. Let the manager continue the loop while the operator is away.

This is a useful safety boundary: validate orchestration with a small batch before increasing concurrency or unattended runtime.

## Merge and human gates

The loop is not fully hands-off. The source reports that UI interactions and brittle SwiftUI/AppKit window logic still caused failures; one worker stalled and had to be replaced; and workers did not always follow `AGENTS.md`. Manual testing remained important for UI changes, while some non-UI changes could be merged automatically after checks passed.

The durable design rule is therefore **automate coordination, not judgment**. A manager can keep PRs moving, but the operator still owns taste, UI acceptance, and the decision to trust the evidence.

## Relationship to broader loop design

This is a concrete implementation of [[loop-engineering]] and a specialized form of [[multi-agent-orchestration]]. Its control surfaces are:

- **Heartbeat** — recurrence and monitoring cadence
- **Worktrees/PRs** — isolation and handoff boundary
- **`/goal`** — worker completion contract
- **CI/tests/manual UI checks** — verification and merge gate
- **Manager thread** — sequencing, feedback routing, and finish-line ownership

It complements [[agent-friendly-xcode-projects]]: the project substrate makes builds and tests legible, while this loop determines how multiple Codex threads use that substrate to ship a backlog.

## Evidence status

- **Independently corroborated:** the linked “Run Codex While You Sleep” landing page exists; the source's exact 8-feature, 12-hour-19-minute run and productivity claims remain source-reported.
- **Source-described:** the 5-step PR loop, 5–10 minute heartbeat, `/goal` worker contract, four-task proof of concept, and reported failure modes.
- **Likely generalization:** the same manager/worker pattern can apply beyond Apple apps when worktree isolation, review surfaces, and deterministic checks are available.

## Related

- [[paul-solt]] — source author and operator
- [[loop-engineering]] — broader control-loop design
- [[multi-agent-orchestration]] — general manager/worker architecture
- [[goal-primitive]] — completion contract used on workers
- [[codex]] — agent environment in the source
- [[agent-friendly-xcode-projects]] — Apple build/test substrate
