---
title: Agent Teams
created: 2026-04-15
updated: 2026-07-28
type: concept
tags: [agent, ai-agent, multi-agent, orchestration, claude-code]
sources: [raw/articles/minimax-m27-huggingface-2026-04-15.md, raw/articles/xarticle-how-to-build-a-claude-agent-team-in-7-steps-from-s-2058475548242784649.md, raw/articles/xarticle-how-to-build-a-team-of-ai-agents-that-actually-wor-2058817146411692358.md, raw/articles/xarticle-how-to-build-a-multi-agent-system-that-actually-fi-2068135133618540931.md, raw/articles/xarticle-practical-multi-agent-orchestration-in-codex-2080707291603407077.md]
related_entity: [[minimax-m27]]
---

# Agent Teams

> A multi-agent collaboration paradigm where multiple instances of an AI model (or different models) assume distinct roles with stable identity, enabling them to collaborate autonomously on complex tasks.

**Also known as:** multi-agent systems, role-based agent collaboration, agent swarms

## Overview

Agent Teams refers to orchestration patterns where:
1. **Multiple agents** are instantiated — each with a defined role (e.g., "researcher", "coder", "reviewer", "tester")
2. **Stable role identity** — each agent maintains consistent behavior and decision-making patterns within its role across the session
3. **Autonomous coordination** — agents decide among themselves how to divide labor, share context, and escalate
4. **Shared or private memory** — agents may share a common context window or maintain private memories that are selectively disclosed

## Team design primitives

[[kanikabk]]'s course adds a very practical operating model for Agent Teams: every good team covers four functions even if one agent handles more than one of them.

- **Orchestrator** — decomposes the top-level objective and routes work.
- **Researcher** — gathers and structures source material.
- **Specialist producer(s)** — writes, codes, analyzes, or executes one narrowly-scoped task.
- **Critic / reviewer** — evaluates the output against explicit criteria and requests revisions when needed.^[raw/articles/xarticle-how-to-build-a-team-of-ai-agents-that-actually-wor-2058817146411692358.md]

This is a useful complement to the Claude Code framing: the point of a team is not just more workers, but a built-in review layer that keeps specialized outputs aligned.

## Claude Code framing

rody's seven-step article turns Agent Teams into the top rung of a three-level Claude Code ladder: [[claude-code-subagents]] for repeatable isolated tasks, Agent View for several independent sessions, and Agent Teams when dependent tasks need a lead agent coordinating specialized workers. In that framing, the team is justified only when coordination itself creates value — not just because parallelism is available.

The practical split is:
- **Subagents** — review, docs, tests, and other cheap repeatable jobs inside one parent session
- **Agent View** — 3 to 10 independent tasks where the operator wants a dashboard, dispatch, and attach/peek controls
- **Agent Teams** — multi-file or multi-role work with real dependencies, shared task lists, and cross-agent communication ^[raw/articles/xarticle-how-to-build-a-claude-agent-team-in-7-steps-from-s-2058475548242784649.md]

## Reliability rules

Kanika's article makes the operational layer more explicit:

- require **structured outputs** for every handoff
- install **quality gates** between agents instead of auto-forwarding every result
- keep **tool access minimal** per worker
- support **retry loops with specific feedback** rather than blind reruns
- **log every call** so the failure point is visible in production ^[raw/articles/xarticle-how-to-build-a-team-of-ai-agents-that-actually-wor-2058817146411692358.md]

[[cyrilXBT]]'s later course makes the same pattern more operationally strict: every team should start from a written Definition of Done, keep the Builder separate from the Judge, and require the Judge to verify each required property against evidence instead of approving on overall impression.^[raw/articles/xarticle-how-to-build-a-multi-agent-system-that-actually-fi-2068135133618540931.md]

That source also argues for a hard cycle cap. Builder ↔ Judge revision loops are productive only while corrections are specific and convergent; after repeated failures, the Manager should escalate rather than letting the team simulate progress forever.^[raw/articles/xarticle-how-to-build-a-multi-agent-system-that-actually-fi-2068135133618540931.md]

## Codex team coordination: peer messaging and context boundaries

Eric Provencher's July 24, 2026 local X Article describes a source-reported Codex Multi-Agent V2 implementation in which the coordinator assigns substantive work, avoids duplicate investigations, and tracks agent activity. The role defaults keep one model family while matching reasoning effort to the work: **Scout — GPT-5.6 Sol Light** for narrow read-only discovery; **Worker — GPT-5.6 Sol Medium** for scoped implementation, checks, and support; and **Smart worker — GPT-5.6 Sol High** for difficult implementation, ambiguity resolution, or useful coordination. The article also says Sol can delegate to Terra and presents Ultra as a high-stakes coordination default; these model/tool claims are not independently verified.^[raw/articles/xarticle-practical-multi-agent-orchestration-in-codex-2080707291603407077.md]

Unlike a coordinator-only relay, agents can message each other through a common messaging system with separate inboxes. A scout can identify a dependency and pass findings directly to the worker that needs them. Concurrency is configurable per thread and defaults to **four agents including the coordinator**: a smart worker may coordinate a scout plus another worker, or the coordinator may dispatch three scouts in parallel. The source does not name the messaging protocol, inbox format, scheduler, or API.^[raw/articles/xarticle-practical-multi-agent-orchestration-in-codex-2080707291603407077.md]

Conversation history is another team-design choice. Forking history provides the broader goal and earlier decisions; `fork_turns: "none"` creates a fresh, focused assignment. Fresh-context agents may still contact teammates when they recognize a dependency, but they do not inherit task-specific tool or safety boundaries, so those restrictions must be repeated in the assignment. If a worker must stay a leaf, the source gives this exact boundary: `Complete this assignment directly. Do not spawn other agents; your parent's delegation instructions apply only to your parent.` The source does not specify the history storage format or enforcement mechanism.^[raw/articles/xarticle-practical-multi-agent-orchestration-in-codex-2080707291603407077.md]

The proposed coordinator skill keeps the user available while delegating, sends focused read-only scouts in parallel with `reasoning_effort: "low"` and `fork_turns: "none"`, uses `reasoning_effort: "medium"` for routine implementation and `reasoning_effort: "high"` for hard problems, gives each agent clear ownership, avoids overlap, tells leaf workers not to delegate, reunifies results, and keeps approvals with the user. The source recommends experimenting with reasoning effort, context inheritance, delegation authority, and collaboration style, but supplies no benchmark or measured evaluation method.^[raw/articles/xarticle-practical-multi-agent-orchestration-in-codex-2080707291603407077.md]

## Cost and guardrails

The Claude Code article adds two operational constraints that the earlier MiniMax-centered version did not emphasize:
- **Model routing** — keep the lead agent on a stronger model and route teammates to a cheaper worker model when tasks are execution-heavy
- **Permission and budget caps** — use explicit allow/deny rules plus `--max-budget-usd` so a parallel team cannot silently run away on cost or destructive actions ^[raw/articles/xarticle-how-to-build-a-claude-agent-team-in-7-steps-from-s-2058475548242784649.md]

## MiniMax M2.7's Agent Teams

[[minimax-m27]] natively supports Agent Teams as a built-in capability. The model can spawn multiple cooperative instances that:
- Maintain distinct behavioral profiles per role
- Communicate and share intermediate results
- Make collective decisions about task decomposition
- Handle cross-team collaboration scenarios (e.g., a research agent coordinating with an infra agent)

MiniMax's internal research agent harness uses Agent Teams to drive the RL experiment cycle — one agent handles literature review, another handles data pipelining, another handles experiment launch/monitoring.

## Relation to Other Multi-Agent Systems

| System | Distinction |
|--------|-------------|
| [[claude-code-subagents]] | Same family of orchestration tools, but subagents report back to a parent session and do not collaborate directly |
| Agent View | Session dashboard and dispatch layer; useful for independent workstreams but not itself a collaborating team |
| MetaGPT | Role-based agents for software development with structured shared memory |
| Agent Teams (MiniMax / Claude Code) | Multi-instance coordination with stronger collaboration and task decomposition than a single-agent harness |

## Benefits

- **Task decomposition:** Complex problems split across specialized agents
- **Stable identity:** Each agent behaves consistently within its role
- **Scalability:** Adding more agents scales the team's capacity without linearly increasing prompt complexity
- **Operational clarity:** the subagents → Agent View → Agent Teams ladder helps choose the lightest-weight orchestration mode that still fits the task
- **Quality control:** critic/reviewer roles can catch evidence gaps, tone drift, or implementation mistakes before the next stage inherits them

## Risks and Challenges

- **Coordination overhead:** Agents may conflict or duplicate work without clear protocols
- **Context fragmentation:** Important information may get lost between agent memory boundaries
- **Eval difficulty:** Harder to evaluate multi-agent systems than single-agent
- **Security and cost:** Parallel workers can multiply permissions mistakes and token burn if you skip routing or budget caps
- **Over-design:** Hierarchical teams are attractive, but many workflows only need a simple pipeline plus review

## Related

- [[claude-code]]
- [[claude-code-subagents]]
- [[minimax-m27]]
- [[model-self-evolution]]
- [[multi-agent-orchestration]]
- [[pvncher]]
