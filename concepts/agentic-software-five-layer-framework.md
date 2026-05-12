---
title: Agentic Software Five-Layer Framework
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [agent, architecture, framework]
sources: [raw/articles/ashpreet-bedi-systems-engineering-agentic-software-2041568919085854847.md]
related_entity: [[ashpreet-bedi]]
author: [[ashpreet-bedi]]
---

# Agentic Software Five-Layer Framework

Systems engineering framework for building production agentic software. Argues that agentic software should be treated as a five-layer system rather than optimizing individual components in isolation.

## Layers

1. **Agent Engineering** — Agent/multi-agent logic, execution flow, model selection, system instructions, tool configurations, handoffs, context management, observability. Behavior should be deterministic where possible and observable where it isn't.

2. **Data Engineering** — Context is data. Well-designed schemas, structured querying, databases for read/writes, object storage, and pipelines. Six layers of grounded context: table metadata, human annotations, query patterns, institutional knowledge, learnings (error patterns + fixes), and runtime context.

3. **Security Engineering** — Auth, RBAC, governance, data isolation, audit trails. JWT-backed tool permissions. Approval tiers: reads freely, writes need user approval, sensitive ops need admin sign-off. Request isolation is a data breach, not a bug.

4. **Interface Engineering** — REST API, Slack, MCP server, terminal. Multiple surfaces each with their own identity system. Auth and access controls must hold consistently across every surface.

5. **Infrastructure Engineering** — Containers, cloud deployment, horizontal scaling. 95% identical to any service. The 5% that's different: longer load balancer timeouts, SSE/websocket streaming, proactive scheduling.

## Key Claims

- Filesystem-backed memory on shared sandbox is a data breach risk
- Read-only access is a tool configuration, not a prompt instruction
- MCP vs CLI debates dissolve when viewed from a systems perspective
- Well-scoped tools > unfettered bash access
- Store sessions, memory, and knowledge in a database, not files
- Layer isolation prevents constraint cascading

## Canonical Implementation

**Dash** (github.com/agno-agi/dash) — open-source self-learning data agent demonstrating all five layers. Leader routes to Analyst (read-only SQL) + Engineer (writable views/schema) specialists. Six layers of grounded context stored in PostgreSQL. JWT RBAC enforced at the database connection level, not the prompt level.

## Related

- [[autoreason]] — Nous Research's iterative self-refinement method
- [[council-of-high-intelligence]] — Multi-agent deliberation framework
- [[agent-teams]] — Multi-agent collaboration paradigm
- [[hermes-agent]] — Open-source agent with multi-layer extension architecture
- [[dash-open-source]] — Canonical implementation of the five-layer framework; open-source data agent by agno-agi demonstrating all five layers
