---
title: Printing Press
created: 2026-05-09
updated: 2026-05-09
type: concept
tags: [cli, ai-agents, open-source, tooling, agentic-ai]
sources: [raw/articles/xarticle-mvanhorn-2052422567181611010.md]
---

# Printing Press — CLI-Factory and CLI-Library for AI Agents

A CLI toolchain that generates and manages agent-native command-line interfaces. Built by Matt Van Horn (@mvanhorn) and Trevin Chow (@trevin).

## Overview

Most APIs, MCPs, and official CLIs are designed for human use — they waste tokens and time when used by AI agents. The Printing Press solves this by providing:

1. **A Library** of pre-built agent-native CLIs you can install today:
   - Linear, ESPN, Flight GOAT (Google Flights + Kayak nonstop), Contact Goat (LinkedIn + Happenstance + Deepline), and 30+ more

2. **A Factory** that prints new CLIs for any service — just type `/printing-press <product name>`

## Key Properties

- **Fast**: Local execution, no network latency for tool calls
- **Local**: SQLite-backed storage for state and context
- **Agent-native**: Designed from the ground up for AI agent consumption (not humans)
- **Compatible**: Works in Claude Code, Codex, OpenClaw, and Hermes Agent

## Motivation

The core problem: most developer tools assume a human in the loop. They use REST APIs with paginated responses, require session management, and waste context window space on human-oriented formatting. Agent-native CLIs solve this by being:
- Composable via stdin/stdout
- Stateless or with explicit SQLite state
- Token-efficient with structured output

## Related

- [[hermes-agent]] — compatible agent runtime
- [[claude-code]] — compatible IDE agent
- [[openclaw]] — compatible agent framework
- [[mcp]] — alternative tool protocol (but Printing Press argues CLIs beat MCPs for agents)