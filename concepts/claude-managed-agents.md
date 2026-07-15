---
title: Claude Managed Agents
created: 2026-05-21
updated: 2026-05-21
type: concept
tags: [product, agent, orchestration, b2b]
sources: [raw/articles/jouhatsu-code-with-claude-london-2026-05-21.md]
---

# Claude Managed Agents

Anthropic's managed agentic harness paired with production-grade infrastructure. Announced at Code with Claude London (2026-05-21). ^[raw/articles/jouhatsu-code-with-claude-london-2026-05-21.md]

## Core Premise

Two problems prevent businesses from snapping to the exponential:
1. **Getting right outcomes is too difficult** — requires prompt optimization, tool construction, harness engineering
2. **Ship fast AND scalably** — prototypes are easy; production scale is hard

## Features

| Feature | Description |
|---|---|
| **Multi-agent orchestration** | Build fleets of collaborating agents |
| **Outcomes** | Specify what success looks like; Claude iterates to achieve it |
| **Dreaming** | Claude introspects on previous transcripts to learn and self-improve |
| **Self-hosted sandboxes** | Execute work on your own servers (Daytona, Cloudflare, Vercel, Modal) |
| **MCP tunnels** | Access internal MCP servers behind firewalls without public exposure |
| **Advisor strategy** | Small model executes; large model (Opus) advises on demand — 5x cost reduction reported by Eve Legal |

## Customer Example: Asana

Built AI teammates that let humans collaborate directly with agents within Asana projects, delegating tasks. Built on Claude Managed Agents for speed + scale. ^[raw/articles/jouhatsu-code-with-claude-london-2026-05-21.md]

## Architecture

- Spawns sandboxes when executing work (file editing, etc.)
- Can use Anthropic-hosted sandboxes OR self-hosted via first-class provider integrations
- MCP tunnels secure private-network tool access

## Related

- [[anthropic]]
- [[claude-code]]
- [[multi-agent-orchestration]]
- [[mcp]]
