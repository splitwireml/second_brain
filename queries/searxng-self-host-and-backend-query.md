---
title: "SearXNG: self-hostable and backend operation"
created: 2026-04-18
updated: 2026-04-18
type: query
tags: [search, self-hosted, tools]
sources: [raw/articles/searxng-deep-technical-research-2026-04-18.md, raw/articles/theahmadosman-agent-web-stack-2026-04-15.md]
question: "Is SearXNG self-hostable, and can it run as a backend (not just a front-end UI)?"
answer_status: answered
related_pages:
  - [[searxng]]
  - [[agent-web-stack]]
---

## Question

Is SearXNG self-hostable, and can it run as a backend (not just a front-end UI)?

## Answer

**Yes to both.**

### Self-Hostable

SearXNG is explicitly designed to be self-hosted. Evidence from the codebase:

- **No external dependencies for search** — it queries third-party engines directly from your server. No SerpAPI or paid backend required for the core search function.
- **Docker support** — the repo has a `container/` directory with Docker configuration. One command to spin up.
- **Minimal hardware requirements** — it's a Python/Flask app. A $5-20/month VPS is sufficient for personal use.
- **AGPL license** — you can run it, modify it, and self-host it commercially.
- **Privacy-respecting by design** — no tracking, no user profiling, no external calls except to the search engines you configure.

The "Agent Web Stack" by [[theahmadosman]] demonstrates this pattern — [[searxng]] is the candidate discovery layer running on the agent's own infrastructure, not calling out to a hosted API.

### Runs as a Backend

Yes. SearXNG has a full **JSON API** that makes it usable purely as a backend for other applications:

**API endpoints** (from `searx/webapp.py`):
- `GET /search?q=query&format=json` — returns results as JSON, suitable for agent consumption
- `GET /search?q=query&format=csv` — machine-readable output
- `GET /search?q=query&format=rss` — RSS feed
- `GET /?q=query&engines=google,bing` — can restrict which engines are queried

**Key backend-relevant properties:**
- **API-accessible** — outputs JSON, so agents can consume results programmatically
- **Engine selection via URL param** — `?engines=google,braveapi,arxiv` lets callers pick specific backends
- **No UI required** — the JSON API works without ever touching the web UI; `format=json` returns structured results
- **`searxng.data/engine_descriptions.json`** — machine-readable engine metadata (languages, regions, whether API key required)
- **`searxngng.msg`** (binary message catalog) — supports i18n of responses

In the [[agent-web-stack]], [[searxng]] is used purely as a backend tool — the agent calls its JSON API to get candidate URLs, then passes those to [[firecrawl]] for extraction. The UI is never involved.

## Practical Verdict

SearXNG is purpose-built for self-hosted backend operation. The web UI is incidental — its real value for agents and developers is the JSON API (`/search?q=...&format=json`). Deploy it on a VPS, call it from any application, no API key needed for most engines.
