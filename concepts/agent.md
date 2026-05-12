---
title: AI Agent
created: 2026-04-11
updated: 2026-04-26
type: concept
tags: [ai-agent-automation, llm]
sources: []
---

## Overview

An AI agent is a system that uses an LLM (or other model) to autonomously plan and execute multi-step tasks — often with tool use, memory, and iterative refinement. Agents observe their environment (via tools, user input, or both), reason about next actions, and execute them in a loop until the goal is reached.

## Key Properties

- **Autonomy** — acts without continuous human intervention
- **Memory** — maintains state across steps (short-term context + long-term retrieved context)
- **Tool use** — calls external tools (search, code execution, API calls) to interact with the world
- **Planning** — decomposes goals into sub-tasks, revises plans based on feedback
- **Multi-agent orchestration** — multiple agents coordinate, possibly with different roles (see [[agent-teams]])

## Core Architectures

- **ReAct** — interleave reasoning traces with tool actions
- **Plan-and-Execute** — planning phase separate from execution
- **Agentic RAG** — agent-driven retrieval with iterative query refinement
- **Tool-augmented LLM** — LLM with function-calling interface to tools

## Related Concepts

- [[vibe-coding]] — vibe coding tools (Cursor, Lovable, Claude Code) are agent-based systems
- [[agent-teams]] — multi-agent collaboration patterns
- [[llm-server-throughput-optimization]] — throughput matters for agents making many concurrent inference calls
- [[cpa-back-office-offshoring]] — AI agents orchestrating offshore accounting staff for US CPA firms (real-world ops agent use case)
- [[agentic-software-five-layer-framework]] — systems engineering framework for building production agentic software; addresses the five-layer architecture (Agent, Data, Security, Interface, Infrastructure) that general AI agent concepts like this one need to operationalize
