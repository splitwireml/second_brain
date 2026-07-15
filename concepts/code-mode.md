---
title: Code Mode
created: 2026-05-09
updated: 2026-06-14
type: concept
tags: [tools, workflow, ai, architecture]
sources: [raw/articles/mcp-vs-cli-2053166970166772052.md]
related_entity: [[akshay-pachaar]]
author: [[akshay-pachaar]]
---

# Code Mode

Code Mode is a runtime pattern where an AI agent writes code that imports tools at runtime, combining MCP's typed contracts with CLI's lazy loading. It was introduced by Anthropic in November 2025 as the fix to the MCP vs CLI debate.

## The Core Insight

Instead of loading every tool's full description into context at session start, Code Mode flips the model job: the model writes code that imports only the tools it needs.

```
Old model: agent walks into a room with every tool laid out on the table
Code Mode: agent walks into a room with a directory of tools on the wall and picks up only what it needs
```

## Two Primitives

### Bash Primitives
For anything with a binary already installed (git, curl, grep). The model has seen these in training data and knows how to compose them.

```bash
grep -r "import pandas" --include="*.py" .
```

No tool definition needed — the shell does the work.

### Typed Module Imports
For proprietary APIs (Salesforce, Stripe, internal services). Small TypeScript files that describe one tool, with inputs and outputs spelled out. The agent only loads what it actually uses.

```typescript
import { searchFiles } from "@tools/github";
import { sendMessage } from "@tools/slack";
```

## Token Savings

- Anthropic example: Google Drive → Salesforce workflow dropped from ~150K tokens to 2K tokens (98.7% reduction)
- Cloudflare: collapsed 2,500-endpoint API from 1.17M tokens to 1K tokens by exposing just `search` and `execute`

## Key Rule

**Tool definitions belong in code, not in context.** The model writes a few lines that call them. The runtime does the rest.

## Relationship to MCP and CLI

Code Mode is not a replacement for either approach — it is a runtime that uses both:
- Bash for anything on $PATH (lazy, no contracts needed)
- Typed module imports for proprietary APIs (MCP's contracts, loaded lazily)

## Related Concepts

- [[model-context-protocol]] — MCP's typed contracts that Code Mode leverages
- [[cli-vs-agent-tool-calling]] — the broader debate that Code Mode resolves
- [[anthropic]] — Code Mode's originator
- [[claude-code]] — the execution context where Code Mode runs

## Related
- [[akshay-pachaar]] — related entity from frontmatter; explicit cross-link
