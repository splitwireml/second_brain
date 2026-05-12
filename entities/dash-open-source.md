---
title: Dash (agno-agi)
created: 2026-04-26
updated: 2026-04-26
type: entity
tags: [oss-ai, agent, model]
sources: [raw/articles/ashpreet-bedi-systems-engineering-agentic-software-2041568919085854847.md]
---

# Dash (agno-agi)

Open-source self-learning data agent by [agno-agi](https://github.com/agno-agi/dash). Natural language → SQL queries → data analysis. Demonstrates the five-layer agentic software framework.

## Architecture

Leader agent routes requests to two specialists:
- **Analyst** — read-only SQL queries via PostgreSQL connection
- **Engineer** — builds computed assets (views, summary tables) on writable engine scoped to single schema

Same interface, different permissions — determined by database connection config, not prompts.

## Six-Layer Context System

1. Table metadata (schema, columns, relationships)
2. Human annotations (metrics, definitions, business rules)
3. Query patterns (known-working SQL)
4. Institutional knowledge (docs, wikis)
5. Learnings (error patterns and discovered fixes)
6. Runtime context (live schema inspection)

The learning loop: agent hits a type error, diagnoses fix, saves it. Query 100 is better than query 1 not because the model improved, but because the data layer got better.

## Security

RBAC with JWT verification enforced at the database connection level — not the prompt level. Every query is scoped to `user_id`. Eval suite tests boundary conditions: credential leaks, destructive SQL, cross-schema boundary attempts.

## Interfaces

REST API, Slack bot, web UI, CLI — all hitting the same agents, tools, and knowledge base.
