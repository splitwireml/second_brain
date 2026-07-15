---
title: Claude Code Subagents
created: 2026-06-11
updated: 2026-06-11
type: concept
tags: [claude-code, subagents, workflow, agent, tools]
sources: [raw/articles/xarticle-how-to-build-claude-subagents-better-than-99-of-pe-2064326627719311775.md, raw/articles/xarticle-how-to-build-a-claude-agent-team-in-7-steps-from-s-2058475548242784649.md]
related_entity: [[claude-code]]
author: [[nate-herk]]
---

# Claude Code Subagents

A practical mental model for using Claude Code subagents as a cheap-worker layer under a more capable orchestrator session.

## Core model

The main session acts as the boss and subagents act as isolated workers. Each worker gets a fresh context, its own instructions, optional tool restrictions, and a cheaper model tier when the task does not require a frontier model.

rody's article makes the boundary explicit: subagents are **Level 1** in Claude Code's orchestration stack. They run inside the current session, report back to the parent, and are best for repeatable jobs like review, docs, and tests rather than collaborative project-wide planning. ^[raw/articles/xarticle-how-to-build-a-claude-agent-team-in-7-steps-from-s-2058475548242784649.md]

## Why it helps

The key operational win is context hygiene. Research, file-reading, and one-off analysis can be delegated without polluting the main conversation. The second win is cost control: pair a smart orchestrator with many cheaper workers instead of running one expensive model for every subtask.

## Where subagents stop being enough

When tasks become interdependent, the parent-agent-only pattern starts to break down. rody's ladder suggests moving up one notch at a time:
- stay with subagents for isolated repeatable work
- move to Agent View for several independent sessions you want to monitor in one dashboard
- move to [[agent-teams]] when workers need to coordinate directly or share a task list

## Caveats from the sources

The same mechanism that makes subagents powerful also makes them expensive if used carelessly at scale. Dynamic multi-agent workflows can burn through limits quickly, so the operator still needs to choose when isolation is worth the spend. The follow-on control surface is explicit permission scoping and budget capping once you promote work from subagents to larger orchestration modes.

## Related

- [[claude-code]]
- [[dynamic-workflows-in-claude-code]]
- [[agent-teams]]
- [[rody]]
