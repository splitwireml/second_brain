---
title: paperclipai/paperclip
created: 2026-04-10
updated: 2026-04-26
type: concept
tags: [orchestration, agent, AI-company, open-source]
sources: [raw/articles/paperclipai-technical-research-2026-04-10.md, raw/articles/x-av1dlive-paperclip-course-2047977902449611165.md, raw/transcripts/2026-04-25-avid-ai-agent-course.md]
related_entity: [[av1dlive]]
---

# paperclipai/paperclip

Open-source AI company orchestration platform. 51k+ GitHub stars (crossed 50,000 during April 2026). MIT license. Creator: Dota.

## Overview

> "If OpenClaw is an employee, Paperclip is the company."

Node.js server + React dashboard that orchestrates AI agents as employees — org charts, budgets, task assignment, goal alignment, governance.

**Not** a chatbot, agent framework, workflow builder, prompt manager, or single-agent tool.

## Architecture

Two-layer design:
1. **Control plane** (Paperclip) — Express API + React dashboard. Manages registry, org chart, task routing, budget tracking, heartbeat monitoring.
2. **Execution layer** (Adapters) — Agents run externally. Paperclip wakes them via heartbeats, they phone home with results.

### Heartbeat Model

Agents run in short execution windows ("heartbeats"), not continuously. Triggers:
- `timer` — scheduled interval
- `assignment` — work assigned/checked out
- `on_demand` — manual API/button trigger
- `automation` — system-triggered

Duplicate wakeups are **coalesced** (merged) if agent is already running.

## Adapters

### Built-in
- `claude_local` — local Claude CLI
- `codex_local` — OpenAI Codex CLI
- `opencode_local` — OpenCode CLI
- `cursor` — Cursor in background mode
- `pi_local` — embedded Pi agent
- `hermes_local` — Hermes CLI
- `openclaw_gateway` — OpenClaw gateway HTTP
- `process` — generic shell
- `http` — external HTTP endpoint

### External Plugins
- `droid_local` — Factory Droid CLI

**Key point:** Not limited to OpenClaw. Works with Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, any HTTP-capable agent.

## Agent Communication

Indirect via **issue/comment system**. No direct peer-to-peer messaging.

- Agents post updates/handoffs as comments on issues
- `@-mentions` wake mentioned agent (triggers heartbeat, costs budget)
- Rules: don't overuse @-mentions, don't use them for assignment

## Workflows

### QA + Approval Gates

Paperclip enforces quality control through two distinct roles:
- **QA agent** — reviews completed work using tools like the agent browser skill (open website, fill form, click button)
- **Approver** — manager who approves work before it enters the org

This solves the Claude Code/agent reliability problem where agents skip tests or produce unchecked output.

### Routines

Reusable scheduled or manual tasks with template variables. Used for:
- PR workflows: create branch, run code review (via grep loop skill), post Discord changelog
- Bookmarks processing: analyze bookmarks, generate reports, create issues
- Release management: merge to master, write changelog, post update

### Skills

Agent tool/plugin modules. Examples:
- `remotion-best-practices` — video creation in React via Remotion
- `grep-loop` — first-pass code review for community contributions
- `skills.sh` registry — centralized skill discovery and installation

### Organizational Learning

Agents learn from feedback over time. Paperclip tracks conversation history so patterns can be refined. The skill consultant agent diagnoses when agents aren't using skills as expected.

## Token and Cost Tracking

Built-in. Adapters emit `costEvents` after each heartbeat (inputTokens, outputTokens, costCents). Per-agent and per-project budgets with soft alerts at 80%, hard stop at 100%.

Supports OpenRouter for cheaper model access (Qwen 3.6+ free tier available as of April 2026).

## Getting Started

Requirements: Node.js 20+, pnpm 9.15+

```bash
npx paperclipai onboard --yes
# or
git clone https://github.com/paperclipai/paperclip.git && cd paperclip && pnpm install && pnpm dev
```

API: `http://localhost:3100` | Embedded Postgres auto-created | No account needed

## Roadmap (as of April 2026)

- CEO chat interface
- Maximizer mode (unlimited token budget for aggressive execution)
- Multi-user support
- Cloud deployment + sandboxing (E2B, cloud agents)
- Desktop app (free, open-source)
- Artifact and deployment features
- Knowledge base + memory improvements

## Comparison

| | Paperclip | CrewAI | AutoGen | LangGraph |
|--|-----------|--------|---------|-----------|
| Focus | Run AI company | Task automation | Agent convos | Graph workflows |
| Dashboard | Full UI | CLI-first | CLI-first | Optional |
| Cost tracking | Built-in | No | No | No |
| Org chart | Yes | No | No | No |

## Related

- [[paperclip-orchestrator]] — different project; a marketing/orchestration tool from a Hermes event
- [[hermes-agent-market-claims]] — Hermes context
- [[vibe-kanban-agent-spawning]] — agent spawning patterns
- [[paperclip-vs-vibe-kanban]] — detailed architecture comparison
- [[a2a-protocol-cross-agent-communication]] — A2A protocol complements Paperclip's adapter architecture
- [[ai-company-stack]] — broader concept of AI-native company infrastructure
- [[av1dlive]] — X creator who produced the getting-started video course
- [[autoreason]] — Nous Research's self-refinement method; shares the "build learning loops into the system" philosophy with Paperclip's error-pattern learning
- [[agentic-software-five-layer-framework]] — [[ashpreet-bedi]]'s systems engineering framework; overlaps with Paperclip's "treat agentic software as infrastructure" philosophy
