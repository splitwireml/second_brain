---
updated: 2026-04-17
title: Open Lovable — GitHub Repository
source: https://github.com/firecrawl/open-lovable
type: github
---

# Open Lovable — GitHub Repository

**URL**: https://github.com/firecrawl/open-lovable
**Owner**: firecrawl
**Stars**: 25,292
**Created**: 2025-08-08
**License**: MIT
**Language**: TypeScript

## Description

> Clone and recreate any website as a modern React app in seconds. An example app made by the Firecrawl team. For a complete cloud solution, check out Lovable.dev.

## Tech Stack

- **Framework**: Next.js 15.4.3 (App Router, TypeScript)
- **AI SDK**: Vercel AI SDK v5 (`ai` package)
- **AI Providers** (multi-provider, user selects one):
  - `@ai-sdk/anthropic` — Anthropic Claude
  - `@ai-sdk/google` — Google Gemini
  - `@ai-sdk/openai` — OpenAI GPT
  - `@ai-sdk/groq` — Groq
- **Web Scraping**: `@mendable/firecrawl-js` (Firecrawl's SDK)
- **Sandbox Providers**:
  - Vercel Sandbox (default, OIDC or PAT auth)
  - E2B (`@e2b/code-interpreter`)
- **Code Execution**: `@e2b/code-interpreter`
- **UI**: Radix UI primitives, Tailwind CSS, Framer Motion, `sonner` toasts
- **State**: Jotai (atoms)
- **Styling**: Tailwind with `@tailwindcss/typography`, custom gradient utilities

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

## Environment Variables

### Required
- `FIRECRAWL_API_KEY` — Firecrawl API key

### AI Provider (choose one)
- `GEMINI_API_KEY`
- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`
- `GROQ_API_KEY`

### Optional
- `MORPH_API_KEY` — for faster edits (Fast Apply)

### Sandbox
- `SANDBOX_PROVIDER=vercel` (default) or `e2b`
- Vercel: `VERCEL_OIDC_TOKEN` (auto via `vercel env pull`) or `VERCEL_TEAM_ID` + `VERCEL_PROJECT_ID` + `VERCEL_TOKEN`
- E2B: `E2B_API_KEY`

## Related

- [Lovable.dev](https://lovable.dev/) — Commercial cloud version
- [Firecrawl](https://firecrawl.dev) — Web scraping API used by this project

## Scripts

```bash
pnpm dev          # Dev with Turbopack
pnpm build        # Production build
pnpm lint         # ESLint
pnpm test:api     # API endpoint tests
pnpm test:code    # Code execution tests
pnpm test:all     # Full test suite
```