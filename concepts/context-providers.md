---
title: Context Providers
created: 2026-05-04
updated: 2026-05-04
type: concept
tags: [agent, framework, ai-agent, orchestration]
sources: [raw/articles/scout-ashpreetbedi-2049180168200106150.md]
related_entity: [[scout]]
author: [[ashpreet-bedi]]
---

# Context Providers

An architectural pattern for agentic systems: a thin abstraction layer between the main agent and its information sources. Each source (Slack, Drive, CRM, etc.) becomes a **context provider** that exposes two natural-language interfaces to the main agent:

- `query_<source>` — natural-language reads from that source
- `update_<source>` — natural-language writes to that source

## The Problem Context Providers Solve

Building a "company brain" or unified agent that connects multiple tools runs into three failures:

1. **Context pollution** — too many tools overload the main agent's context window with tool schemas, parameters, and intermediate results
2. **Degrading performance** — overlapping scopes between tools cause the main agent to route incorrectly or produce conflicting results
3. **Context exhaustion** — the main agent stops working because its context is full of tool quirks and internal state

## How It Works

The main agent never sees the native tool surface of any source. Instead, it only sees the context provider's `query_*` / `update_*` interface. Behind each context provider is a **sub-agent** that owns all the quirks of its source:

- Slack: look up user before DMing, paginate by cursor, prefer `conversations.replies` for threads
- Drive: handle share permissions, pagination, mime-type filtering
- CRM: schema for contacts/projects/notes/follow-ups

The sub-agent's job is to translate the main agent's natural-language intent into source-specific API calls, then translate the results back into clean, structured context — without polluting the main agent's context with intermediate steps.

## Contrast: Context Providers vs. Skills

Skills are task-specific instructions ("here's how to use Slack") that the model loads on-demand. They move task knowledge out of the always-on prompt and into something conditional. However:

- When a skill module is loaded, the underlying tools still land on the main agent
- Intermediate tool call results are still in the main context
- Load 2 skills with search capabilities → agent context dies immediately

Context Providers solve this differently: the main agent never sees the underlying tools at all. The interface is always just `query_slack` or `update_crm`, regardless of how many tools or skills are involved.

## Key Benefits

1. **Main agent context stays clean** — tool surface is hidden behind a thin interface
2. **Source complexity is encapsulated** — each context provider sub-agent handles pagination, auth, conventions
3. **Composable** — `query_slack` and `query_gdrive` can be used together without the main agent knowing either source
4. **Scalable** — adding a new source only requires a new context provider, the main agent instructions stay unchanged

## Implemented In

- [[scout]] — open-source context agent by [[ashpreet-bedi]] that uses context providers for Slack, Drive, CRM, knowledge wiki, voice wiki, MCP servers, and workspace integration
