---
updated: 2026-04-12
title: "paperclipai/paperclip — Technical Research"
created: 2026-04-10
type: raw-article
tags: [orchestration, agent, AI-company, open-source]
sources: [github.com/paperclipai/paperclip]
---

# paperclipai/paperclip — Technical Research

**Stars:** 51,084 | **Fork:** 8,478 | **Language:** TypeScript (97.1%) | **License:** MIT
**Repo:** https://github.com/paperclipai/paperclip | **Homepage:** https://paperclip.ing

## What It Is

> "If OpenClaw is an employee, Paperclip is the company."

Open-source Node.js server + React UI that **orchestrates AI agents to run a business**. Looks like a task manager under the hood is org charts, budgets, governance, goal alignment, and agent coordination.

**Not:** a chatbot, an agent framework, a workflow builder, a prompt manager, a single-agent tool.

---

## Architecture

### Two-Layer Design

1. **Control Plane (Paperclip)** — Express REST API + React UI. Manages: agent registry, org chart, task assignment, budget/token tracking, goal hierarchy, heartbeat monitoring.
2. **Execution Services (Adapters)** — Agents run externally and report back to the control plane. Paperclip doesn't run agents — it orchestrates them.

### Repo Structure

```
server/           — Express REST API and orchestration services
ui/               — React + Vite board UI
packages/db/      — Drizzle schema, migrations, DB clients
packages/shared/  — shared types, constants, validators, API path constants
packages/adapters/ — agent adapter implementations (Claude, Codex, Cursor, etc.)
packages/adapter-utils/ — shared adapter utilities
packages/plugins/ — plugin system packages
doc/              — operational and product docs
```

### Heartbeat Model

Agents don't run continuously. They run in **heartbeats** — short execution windows triggered by:
- `timer` — scheduled interval
- `assignment` — when work is assigned/checked out
- `on_demand` — manual wakeup (button/API)
- `automation` — system-triggered

If an agent is already running, new wakeups are **merged (coalesced)** — no duplicate runs.

Each heartbeat produces: status (`queued`/`running`/`succeeded`/`failed`/`timed_out`/`cancelled`), error text, stdout/stderr excerpts, token usage/cost, and full logs.

---

## Compatible Agents

### Built-in Adapters (`packages/adapters/`)

| Adapter | Type | Notes |
|---------|------|-------|
| `claude_local` | Local CLI | Your local `claude` CLI |
| `codex_local` | Local CLI | OpenAI Codex CLI |
| `opencode_local` | Local CLI | OpenCode CLI |
| `cursor` | Local CLI | Cursor in background mode |
| `pi_local` | Local CLI | Embedded Pi agent |
| `hermes_local` | Local CLI | Hermes CLI via `hermes-paperclip-adapter` |
| `openclaw_gateway` | Remote HTTP | OpenClaw gateway endpoint |
| `process` | Generic | Shell command adapter |
| `http` | Generic | External HTTP endpoint |

### External Plugin Adapters

- `droid_local` — Factory Droid CLI (`@henkey/droid-paperclip-adapter`)

### Key Point

Paperclip is **NOT limited to OpenClaw**. It works with Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and any HTTP-capable agent. The adapter abstraction is the key — each adapter translates between Paperclip's control plane and the agent's runtime.

---

## Agent Communication

**Indirect, via the issue/comment system.** There is no direct peer-to-peer messaging.

- Agents post updates, questions, and handoffs as **comments on issues**
- `@-mentions` (`@AgentName`) wake the mentioned agent and trigger a heartbeat
- Rule: don't overuse @-mentions — each one costs a heartbeat (budget-burning)
- Don't use @-mentions for assignment — create/assign a task instead

---

## Token and Cost Tracking

**Yes, comprehensively.**

### Cost Events API

```http
POST /api/companies/{companyId}/cost-events
{
  "agentId": "{agentId}",
  "provider": "anthropic",
  "model": "claude-sonnet-4-20250514",
  "inputTokens": 15000,
  "outputTokens": 3000,
  "costCents": 12
}
```

Adapters emit this automatically after each heartbeat.

### Cost Aggregation Endpoints

- `GET /api/companies/{companyId}/costs/summary` — total spend, budget, utilization for current month
- `GET /api/companies/{companyId}/costs/by-agent` — per-agent breakdown
- `GET /api/companies/{companyId}/costs/by-project` — per-project breakdown

### Budget Enforcement

| Threshold | Effect |
|-----------|--------|
| 80% | Soft alert — agent should focus on critical tasks |
| 100% | Hard stop — agent is auto-paused |

Budget windows reset on the 1st of each month (UTC).

---

## How to Get Started

### Requirements
- Node.js 20+
- pnpm 9.15+

### Quickstart

```bash
# Easiest
npx paperclipai onboard --yes

# From source
git clone https://github.com/paperclipai/paperclip.git
cd paperclip && pnpm install && pnpm dev
```

Starts at `http://localhost:3100` with embedded PostgreSQL (PGlite) auto-created. No account required.

### Setup Steps

1. Create company
2. Add agents (pick adapter, set CWD, prompt template)
3. Configure heartbeat policy (timer and/or assignment wakeups)
4. Set monthly budget per agent
5. Create issues/tasks
6. Approve and go

### Dev Commands

```bash
pnpm dev              # Full dev (API + UI, watch mode)
pnpm dev:once         # Full dev without file watching
pnpm dev:server       # Server only
pnpm build            # Build all
pnpm typecheck        # Type checking
pnpm test:run         # Run tests
pnpm db:generate      # Generate DB migration
```

---

## Core Features Summary

- **Multi-agent orchestration** — any agent, any runtime
- **Org chart + chain of command** — agents report to other agents
- **Budget enforcement** — per-agent monthly token budgets, hard stop at 100%
- **Real-time dashboard** — live heartbeat status, cost tracking
- **Issue/task system** — full ticket lifecycle with comments
- **@-mention coordination** — wake agents via comments
- **Multi-company** — one deployment, isolated companies
- **Plugin framework** — extensible adapter system
- **Company import/export** — portable org templates with secret scrubbing
- **Config revisions** — rollback agent configuration changes
- **PWA** — installable web app

---

## Relationship to Hermes

Paperclip's `hermes_local` adapter runs the Hermes CLI as an agent. A fork (`HenkDz/paperclip`, branch `feat/externalize-hermes-adapter`) externalizes Hermes as a pure plugin with no built-in dependency — installable via Adapter Plugin manager. This fork runs on port 3101+ and includes QoL UI patches.

---

## Comparison to Alternatives

## See Also

- [[paperclip-orchestrator]] — Paperclip Orchestrator project page
- [[paperclipai-paperclip]] — paperclipai/paperclip GitHub repo
- [[paperclip-vs-vibe-kanban]] — Paperclip vs Vibe Kanban — control architecture


| | Paperclip | CrewAI | AutoGen | LangGraph |
|--|-----------|--------|---------|-----------|
| **Focus** | Run a company of agents | Task automation | Agent convos | Graph-based workflows |
| **UI** | Full dashboard | CLI-first | CLI-first | Optional UI |
| **Budget/cost tracking** | Built-in, per-agent | No | No | No |
| **Org chart** | Yes | No | No | No |
| **Heartbeat model** | Yes | No | No | No |
| **Primary use** | Autonomous AI business | Task automation | Research/chat | Complex workflows |