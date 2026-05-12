---
title: "Vane (ItzCrazyKns)"
created: 2026-04-16
updated: 2026-04-16
type: entity
tags: [ai-tools, rag, search, open-source, self-hosted]
sources: [raw/articles/itzcrazykns-vane-ai-answering-engine.md]
---

## Overview

Vane is a **privacy-focused AI answering engine** — an open-source, self-hosted alternative to Perplexity. It runs entirely on your own hardware, combines internet search with LLM-powered synthesis, and delivers answers with cited sources. Think of it as an AI search engine you fully own and control.

## Key Facts

- **Repo**: [github.com/ItzCrazyKns/Vane](https://github.com/ItzCrazyKns/Vane)
- **Stars**: 33,762 | **Forks**: 3,658
- **License**: MIT
- **Language**: TypeScript (Next.js)
- **Created**: 2024-04-09
- **Topics**: `ai-agents`, `ai-search-engine`, `answering-engine`, `rag`, `search-engine`, `searxng`, `self-hosted-ai`

## What It Does

Vane takes a user query, classifies it, optionally runs web research (via SearxNG) and widgets in parallel, then synthesizes an LLM-generated answer with citations.

**Supported LLM providers:**
- Local: Ollama
- Cloud: OpenAI, Anthropic Claude, Google Gemini, Groq, and compatible OpenAI-API-compliant servers

**Search modes:**
- Speed Mode (quick answers)
- Balanced Mode (everyday use)
- Quality Mode (deep research)

**Source types:** Web search, discussions, academic papers, image/video search, domain-restricted search, file uploads (PDF, text, images).

## Architecture

Next.js application with:
- `POST /api/chat` — chat UI backend
- `POST /api/search` — programmatic search API
- `GET /api/providers` — list available providers
- Agent orchestration: question classification → parallel research + widgets → answer synthesis with citations — see [[vane-agentic-search-workflow-query]] for detailed agentic workflow breakdown
- SearxNG as the privacy-preserving meta-search backend
- Embedding models for semantic search over uploaded files

## Installation

**Docker (recommended):**
```bash
docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest
```

**One-click deploy:** Sealos, RepoCloud, ClawCloud, Hostinger

## Related

- [[searxng]] — privacy-first meta-search engine powering Vane's web search
- [[perplexica]] — similar AI answering engine (Vane is its upstream fork)
- [[hermes-agent]] — can use Vane as a search tool within agent workflows
- [[agent-web-stack]] — alternative 3-stage agent web access pipeline (SearXNG → Firecrawl → Camofox)
- [[vane-self-hosted-ai-search-query]] — answered query on backend architecture, OpenRouter support, and free search provider requirements
