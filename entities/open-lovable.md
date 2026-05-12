---
title: Open Lovable
created: 2026-04-16
updated: 2026-04-16
type: entity
tags: [ai-tools, product, open-source, vibe-coding]
sources: [raw/articles/firecrawl-open-lovable-github-2026-04-16.md]
related_entity: [[firecrawl]]
---

## Overview

Open Lovable is the open-source reference implementation of an AI-powered website-to-React app converter, built by the [[firecrawl]] team. It clones and recreates any website as a modern React application in seconds via a chat interface. The repository serves as both a working product demo and a reference implementation for the commercial [Lovable.dev](https://lovable.dev/) service.

- **GitHub**: [firecrawl/open-lovable](https://github.com/firecrawl/open-lovable)
- **Stars**: 25,292
- **Created**: 2025-08-08
- **License**: MIT
- **Language**: TypeScript

## What It Does

Users paste a URL or describe a website. The system uses [[firecrawl]] (via `@mendable/firecrawl-js`) to scrape and extract the site's structure, then sends the data to an LLM to generate a modern React equivalent. The generated app uses Next.js 15 App Router with Tailwind CSS, Framer Motion animations, and Radix UI components.

## Tech Stack

- **Next.js 15.4.3** with App Router and Turbopack
- **Vercel AI SDK v5** (`ai` package) — multi-provider abstraction
- **AI Providers**: Anthropic Claude, Google Gemini, OpenAI GPT, Groq (user-selectable)
- **Sandbox**: Vercel Sandbox (default, OIDC auth) or E2B for code execution
- **Web Scraping**: `@mendable/firecrawl-js`
- **UI**: Radix UI primitives, Tailwind CSS, Framer Motion, Jotai state, Sonner toasts

## Architecture

```
app/
├── api/          # API routes
├── builder/      # Builder UI
├── generation/   # Code generation logic
└── landing.tsx   # Landing page

components/       # React components
hooks/            # Custom React hooks
lib/              # Core library code
atoms/            # Jotai state atoms
config/           # Configuration
utils/            # Utilities
```

## Relationship to Vibe Coding

Open Lovable is a canonical example of **vibe coding** — describing what you want in natural language and having an AI agent translate intent into a working React application. The [[gsd-2-ai-vibe-coding-framework]] is a dedicated vibe coding framework with extensibility; Open Lovable is a purpose-built product in the same category.

## Environment Variables

| Variable | Purpose |
|---|---|
| `FIRECRAWL_API_KEY` | Required — Firecrawl API key |
| `GEMINI_API_KEY` / `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` / `GROQ_API_KEY` | Choose one AI provider |
| `MORPH_API_KEY` | Optional — faster edits (Fast Apply) |
| `SANDBOX_PROVIDER` | `vercel` (default) or `e2b` |

## Comparison with Related Tools

| Dimension | Open Lovable | [[gsd-2-ai-vibe-coding-framework]] |
|---|---|---|
| Scope | Website → React app | General-purpose vibe coding framework |
| Licensing | MIT (open source) | AGPL-3.0 |
| AI providers | Multiple (user-selected) | Pi SDK-based |
| Extensibility | Read-reference only | Fully extensible via 23 bundled extensions |

## Sources

- `raw/articles/firecrawl-open-lovable-github-2026-04-16.md`
