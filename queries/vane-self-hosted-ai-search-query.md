---
title: "Vane self-hosted AI search — backend, OpenRouter, search providers"
created: 2026-04-18
updated: 2026-04-18
type: query
tags: [ai-tools, rag, search, self-hosted]
sources: [raw/articles/itzcrazykns-vane-ai-answering-engine.md, sources/vane/src/lib/models/providers/index.ts, sources/vane/src/lib/models/providers/openai/index.ts, sources/vane/src/lib/models/providers/openai/openaiLLM.ts, sources/vane/src/lib/searxng.ts]
question: "Does Vane run a backend? Does it support OpenRouter? Does it need a paid search provider?"
answer_status: answered
related_pages:
  - [[vane]]
  - [[searxng]]
  - [[perplexica]]
---

## Question

1. Does Vane run a backend?
2. Does it work with OpenRouter?
3. Does it require a paid search provider, or will free crawling work?

## Answer

### 1. Yes — full backend

Vane is a Next.js application that runs as a complete backend + frontend stack in Docker. The official image bundles both:
- **Next.js** (port 3000) — frontend + API routes
- **SearxNG** — meta-search engine

Key API routes: `POST /api/chat`, `POST /api/search`, `GET /api/providers`, `POST /api/providers`

---

### 2. No native OpenRouter support — but OpenAI provider accepts custom baseURL

OpenRouter is **not** in the provider list (`src/lib/models/providers/index.ts`):

| Supported providers |
|---|
| OpenAI, Ollama, Gemini, Groq, Lemonade, Anthropic, LMStudio, Transformers |

**However**, the OpenAI provider (`src/lib/models/providers/openai/`) accepts a custom `baseURL` field:

```typescript
// openaiLLM.ts — client init
this.openAIClient = new OpenAI({
  apiKey: this.config.apiKey,
  baseURL: this.config.baseURL || 'https://api.openai.com/v1',
});
```

The UI field (`openai/index.ts`) shows:

```typescript
{
  type: 'string',
  name: 'Base URL',
  key: 'baseURL',
  required: true,
  default: 'https://api.openai.com/v1',
}
```

**Workaround**: Add an "OpenAI" connection with:
- API Key: your OpenRouter key
- Base URL: `https://openrouter.ai/api/v1`
- Model: e.g. `anthropic/claude-sonnet-4`

When baseURL differs from the default, preset model lists are hidden — you manually specify model keys. Works fine since it's just passing the model string through to the custom endpoint.

---

### 3. Free search works fine — no paid provider required

**SearxNG** is the only implemented search backend. It's bundled in the Docker image and makes unauthenticated HTTP calls to search engines at no cost.

```typescript
// searxng.ts
const url = new URL(`${searxngURL}/search?format=json`);
url.searchParams.append('q', query);
```

The README mentions Tavily and Exa as "coming soon" paid options — but neither is implemented yet.

---

## Summary

| | |
|---|---|
| Backend? | Yes — Next.js + SearxNG in Docker |
| OpenRouter native? | No |
| OpenRouter via custom baseURL? | **Yes** — use OpenAI provider with OpenRouter baseURL |
| Paid search required? | No — SearxNG is free/bundled |
