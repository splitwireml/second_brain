---
title: CLI vs Agent Tool Calling
created: 2026-05-09
updated: 2026-06-14
type: concept
tags: [tools, ai, architecture, comparison]
sources: [raw/articles/mcp-vs-cli-2053166970166772052.md]
related_entity: [[akshay-pachaar]]
author: [[akshay-pachaar]]
---

# CLI vs Agent Tool Calling

The "MCP vs CLI" debate was the central disagreement in 2025 about how AI agents should call external tools. Both approaches had legitimate merits, but the framing itself was the problem.

## The Two Camps

### MCP Camp
- Protocol Anthropic released for connecting agents to external services
- Provides typed contracts for tool interfaces
- Multi-tenant safe
- **Problem**: loading every tool upfront burns massive context (55K+ tokens for 5 servers)

### CLI Camp
- Give the agent a shell, let it call binaries directly
- Lazy loading — only what the agent needs enters context
- No typed contracts — agent must parse unstructured output
- **Problem**: breaks on multi-tenant apps, no type safety

## Why Both Were Wrong

The framing of "which one wins" missed the point. Both approaches survived — they just stopped being the runtime and became primitives that a new runtime composes.

## The Resolution: Code Mode

[[code-mode]] is the runtime that synthesizes both:

| Property | MCP | CLI | Code Mode |
|----------|-----|-----|-----------|
| Typed contracts | Yes | No | Yes (typed imports) |
| Lazy loading | No | Yes | Yes |
| Multi-tenant safe | Yes | No | Yes |
| Tool definitions in code | No | No | **Yes** |

## Key Takeaway

**Tool definitions belong in code, not in context.** The model writes a few lines that import only what it needs. The runtime handles the rest.

MCP gave typed contracts. CLI gave lazy loading. Code Mode took both and put them inside one runtime.

## Related Concepts

- [[code-mode]] — the synthesis runtime
- [[model-context-protocol]] — MCP, the protocol that survived
- [[anthropic]] — creator of MCP and Code Mode
- [[custom-mcp-servers]] — building MCP integrations

## Related
- [[akshay-pachaar]] — related entity from frontmatter; explicit cross-link
