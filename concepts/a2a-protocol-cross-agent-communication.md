---
title: A2A Protocol Cross-Agent Communication
created: 2026-04-02
updated: 2026-04-02
type: concept
tags: [protocol]
sources: [raw/articles/x-bookmarks-2026.md]
---

     1|# A2A Protocol: Cross-Agent Communication Research
     2|
     3|> Research date: 2026-04-02
     4|> Source: Web research (a2a-protocol.org, GitHub, Google Developers Blog, DEV Community)
     5|
     6|## What is A2A?
     7|
     8|**Agent2Agent (A2A) Protocol** is an open standard for inter-agent communication, launched by Google Cloud in April 2025, now governed by the Linux Foundation. 50+ launch partners including Anthropic, Atlassian, Cohere, Salesforce, SAP, ServiceNow, and Workday.
     9|
    10|**The problem it solves:** MCP (Model Context Protocol) handles agent-to-tool access (vertical). A2A handles agent-to-agent collaboration (horizontal). Together they form a complete agent interoperability stack.
    11|
    12|**Technical foundation:**
    13|- JSON-RPC 2.0 over HTTP(S)
    14|- Server-Sent Events (SSE) for streaming
    15|- OAuth 2.0 / API keys for authentication
    16|- Agent Cards (`.\well-known/agent.json`) for capability discovery
    17|- Protocol version: v0.3.0 (v1.0.0 released)
    18|
    19|## A2A vs MCP
    20|
    21|| | MCP | A2A |
    22||---|---|---|
    23|| **Role** | Agent-to-tool | Agent-to-agent |
    24|| **Architecture** | Client-server (agent as client) | Peer-to-peer |
    25|| **Purpose** | Give agents tools | Agents collaborate as peers |
    26|| **Discovery** | Tool registries | Agent Cards |
    27|| **Governance** | Anthropic (MCP) / Linux Foundation | Linux Foundation |
    28|
    29|## Core A2A Concepts
    30|
    31|### Agent Card
    32|JSON manifest at `/.well-known/agent.json` acts as agent resume for capability discovery.
    33|
    34|### Task Lifecycle
    35|submitted working input-required completed / failed / canceled
    36|
    37|- **contextId**: Groups related tasks into a conversational session
    38|- **taskId**: Resumable handle for long-running tasks
    39|- New session = omit both fields. Resume = pass the previous taskId
    40|
    41|### Message Parts
    42|Content types: text, data (JSON), or artifact (files, structured output)
    43|
    44|### Streaming
    45|message/sendSubscribe returns SSE for real-time progress updates
    46|
    47|## Agent Wrappers (Claude Code, Codex, OpenCode)
    48|
    49|### 1. claude-a2a (GitHub: ericabouaf/claude-a2a)
    50|npm install -g claude-a2a
    51|cd /path/to/project && claude-a2a  (starts on localhost:3008)
    52|
    53|Wraps Claude Code SDK as A2A server. NOT production-ready.
    54|
    55|### 2. claude-code-agent (GitHub: dwmkerr/claude-code-agent, v0.1.3)
    56|Most mature Claude Code A2A wrapper. Each A2A request = isolated workspace.
    57|Docker/Kubernetes/Helm deployable. Supports parallel sessions.
    58|Configure MCP servers, plugins per session via .init-session.sh
    59|
    60|### 3. a2a-opencode (GitHub: shashikanth-gs/a2a-opencode)
    61|Exposes OpenCode as A2A agent. Full A2A v0.3.0.
    62|Swap LLM provider in one config line. Works with LangGraph, Google ADK.
    63|
    64|### 4. Codex
    65|No native A2A wrapper as of April 2026. Wrap manually with @a2a-js/sdk.
    66|Intent app (intent.com) orchestrates Claude Code, Codex, OpenCode, Auggie.
    67|
    68|## Architecture
    69|
    70|Orchestrator (LangGraph/Google ADK/Custom)
    71|  A2A Protocol (JSON-RPC + SSE)
    72|    Claude Code A2A (port 2222) -> Project A workspace
    73|    OpenCode A2A (port 3001) -> Project B workspace
    74|    Codex A2A (port 4000) -> Project C workspace
    75|
    76|Run multiple agents on different ports, each with own workspace.
    77|
    78|## SDKs for Orchestrators
    79|- Python: a2aproject/a2a-python (1.8k stars)
    80|- JavaScript: a2aproject/a2a-js (505 stars)
    81|
## Related Concepts

- [[vibe-kanban-agent-spawning]] — Vibe Kanban's agent spawning; uses ACP for agent communication
- [[paperclipai-paperclip]] — adapter architecture for multi-agent orchestration; A2A complements this pattern
- [[autonomous-ios-ui-testing]] — FlowDeck CLI for autonomous iOS UI testing; relevant to agent tool-use and testing workflows
- [[research-code-agent-cli-automation]] — CLI agent comparison; A2A is relevant to multi-agent orchestration

## Key References
- Spec: https://a2a-protocol.org/latest/specification/
- Google ADK codelab: https://codelabs.developers.google.com/intro-a2a-purchasing-concierge
- a2a-opencode: https://github.com/shashikanth-gs/a2a-opencode
- claude-code-agent: https://github.com/dwmkerr/claude-code-agent
- Intent: https://intent.com
    88|