---
title: Generative UI
created: 2026-06-11
updated: 2026-06-11
type: concept
tags: [ui-design, agentic-ai, web-development, mcp, tools]
sources: [raw/articles/xarticle-generative-ui-is-the-new-frontend-2062220865643982875.md]
related_entity: [[shubham-saboo]]
---

# Generative UI

Generative UI is the pattern where an agent stops merely describing an interface and starts producing the interface itself at runtime. In this framing, the frontend becomes partly agent-authored rather than fully pre-shipped.

## Protocol stack

The source distinguishes three adjacent protocols:
- **MCP** connects agents to tools
- **A2A** connects agents to other agents
- **AG-UI** connects agents to users via a streaming UI layer

On top of AG-UI, **A2UI** carries agent-emitted UI schemas, while MCP apps expose richer application surfaces the agent can directly drive.

## Three implementation patterns

1. **Controlled** — the frontend pre-builds components and the agent selects among them
2. **Declarative** — the agent emits a schema (A2UI) and the app maps it to components
3. **Open-ended** — the agent emits raw HTML or drives an MCP app sandbox directly

## Strategic tradeoff

The article's practical argument is that teams usually think they are choosing a design style when they are actually choosing an architectural control surface. Controlled systems maximize design consistency, declarative systems maximize extensibility, and open-ended systems maximize flexibility at the cost of stronger sandbox and runtime concerns.

## Related

- [[shubham-saboo]]
- [[model-context-protocol]]
- [[agentic-workflow]]
