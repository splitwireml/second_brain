---
updated: 2026-04-19
title: "10 GitHub repos to spend 60-90% less tokens in Claude Code:\n\n1. RTK (Rust Token Killer)\n\nCLI proxy that filters terminal"
author: "Ronin"
username: "@DeRonin_"
created: "2026-04-18"
source: "https://x.com/DeRonin_/status/2045420155434320270"
type: "xarticle"
tags: []
---


10 GitHub repos to spend 60-90% less tokens in Claude Code:

1. RTK (Rust Token Killer)

CLI proxy that filters terminal output before it hits your context

- 60-90% reduction on common dev commands
- one binary, zero dependencies
- works with Claude Code, Cursor, Copilot

Repo: https://t.co/WayvpBtyBH

2. Context Mode

Sandboxes raw tool output into SQLite instead of dumping it into context

- 98% context reduction on Playwright, GitHub, logs
- only clean summaries enter your conversation
- works as Claude Code plugin

Repo: https://t.co/YNbFIGQz7X

3. code-review-graph

Local knowledge graph that maps your codebase with Tree-sitter

- Claude reads only what matters, not the entire repo
- 49x token reduction on large monorepos
- 6.8x on average reviews

Repo: https://t.co/9gIzmAWN12

4. Token Savior

MCP server that navigates code by symbols, not full files

- 97% reduction on code navigation
- persistent memory across sessions
- 69 tools, zero external deps

Repo: https://t.co/OtvhrMgGWh

5. Caveman Claude

makes Claude talk like a caveman to cut output tokens

- 65-75% output reduction
- one-line install
- keeps full technical accuracy

Repo: https://t.co/onBeghTyfH

6. claude-token-efficient

one CLAUDE.md file that keeps responses terse

- drop-in, no code changes
- reduces output verbosity on heavy workflows
- best for output-heavy sessions

Repo: https://t.co/j6MKo9klQe

7. token-optimizer-mcp

MCP server with caching, compression, and smart tool intelligence

- 95%+ token reduction through intelligent caching
- compresses repeated tool outputs

Repo: https://t.co/0jIVQ4ANls

8. claude-token-optimizer

reusable setup prompts for optimizing any project

- 90% token savings in 5 minutes
- reduces doc token usage from 11K to 1.3K

Repo: https://t.co/puil9WwFGB

9. token-optimizer

finds ghost tokens that silently eat your context

- survives compaction without losing quality
- fixes context quality decay

Repo: https://t.co/92G8e4yeGq

10. claude-context (by Zilliz)

code search MCP that makes your entire codebase the context

- ~40% reduction with equivalent retrieval quality
- hybrid BM25 + dense vector search

Repo: https://t.co/yjfiQOSy15

[ how to stack them ]:

you don't need all 10. pick 2-3 based on your workflow:

> heavy terminal output? RTK
> big codebase? code-review-graph + Token Savior
> lots of MCP servers? Context Mode
> quick fix? Caveman + claude-token-efficient

most people are burning tokens without knowing it

run /context in a fresh session and see how much is gone before you even type a word

your pocket will thank me later :<)
