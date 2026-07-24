---
title: Model Context Protocol (MCP)
created: 2026-05-09
updated: 2026-07-24
type: concept
tags: [tools, model, ai, architecture]
sources: [raw/articles/mcp-vs-cli-2053166970166772052.md, raw/articles/xarticle-youre-using-claude-wrong-if-you-dont-have-these-6--2080083376976044193.md]
related_entity: [[akshay-pachaar]]
author: [[akshay-pachaar]]
---

# Model Context Protocol (MCP)

The Model Context Protocol (MCP) is Anthropic's open protocol for connecting AI agents to external services and tools. It was the center of a major 2025 debate about how agents should call tools.

## The MCP vs CLI Debate

The debate centered on two approaches:

**MCP approach**:
- Provides typed contracts for tool interfaces
- Enables multi-tenant applications without breaking
- Problem: loads full tool schemas into context upfront (55K+ tokens for a 5-server setup)

**CLI approach**:
- Provides lazy loading — agent only loads what it needs
- Problem: no typed contracts, agents guess at outputs

## What MCP Got Right

MCP's typed contracts are valuable:
- Explicit input/output schemas
- Multi-tenant safe
- Agents get structured data, not parsed text

## What Died: Loading Everything Upfront

The real problem wasn't the protocol — it was the habit of loading every tool's full description into context at session start. This could balloon workflows to 150K+ tokens.

The fix: [[code-mode]] flips the model job — instead of calling tools through context, the model writes code that imports tools through a runtime, only paying for what it actually uses.

## Six-Tool Claude Stack (2026-07-24)

AI with Remy's article explains MCP in practical terms as the translation layer between Claude and external tools. It names six source-described integrations: [[n8n]] for workflow automation, [[nano-banana]] for image generation, [[firecrawl]] for known-URL extraction, [[perplexity]] for in-context research, [[apify]] for broad scraping, and [[playwright]] for real-browser interaction. The examples and performance claims are attributed to the article rather than independently verified. ^[raw/articles/xarticle-youre-using-claude-wrong-if-you-dont-have-these-6--2080083376976044193.md]

## MCP Today

- 300M+ MCP SDK downloads (as of early 2026, up from 100M)
- Fastest growing agent infrastructure
- MCP as a protocol survived; the "load everything upfront" pattern did not

## Related Concepts

- [[code-mode]] — the runtime pattern that fixes MCP's context-loading problem
- [[cli-vs-agent-tool-calling]] — the broader debate
- [[custom-mcp-servers]] — building custom MCP server integrations
- [[anthropic]] — MCP's creator
- [[aiwithremy]] — source author of the six-tool Claude stack

## Related
- [[akshay-pachaar]] — related entity from frontmatter; explicit cross-link
