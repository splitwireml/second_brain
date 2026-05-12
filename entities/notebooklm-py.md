---
title: notebooklm-py
created: 2026-04-13
updated: 2026-04-13
type: entity
tags: [llm, oss-ai, inference, automation]
sources: [raw/articles/notebooklm-py-technical-research-2026-04-13.md]
---

# notebooklm-py

**github.com/teng-lin/notebooklm-py** — Unofficial Python client and CLI for Google NotebookLM. Provides full programmatic access to all NotebookLM features via reverse-engineered Google internal batchexecute RPC APIs — including capabilities absent from the web UI. MIT license, v0.3.4, Python 3.10–3.14.

## What it is

NotebookLM is Google's AI research notebook. It ingests sources (URLs, PDFs, YouTube, Google Drive), builds a grounded knowledge base, and generates derived content (audio podcasts, videos, quizzes, flashcards, reports, mind maps). The web UI exposes these features interactively.

`notebooklm-py` automates all of it — everything the web UI does, plus things it doesn't.

## Authentication

**Cookie-based only. No OAuth, no API key.**

Two login paths:

| Method | Command | Requirement |
|--------|---------|-----------|
| Browser automation | `notebooklm login` | `pip install "notebooklm-py[browser]"` + Playwright |
| Cookie extraction | `notebooklm login --browser chrome` | `pip install "notebooklm-py[cookies]"` + browser open |

The library extracts Google auth cookies from a browser session where you're logged into your Google account. Minimum required cookie: `SID`. Full coverage typically needs `SID`, `__Secure-1PSID`, `__Secure-3PSID`, `HSID`, `SSID`, `NID`.

On every client init, two runtime tokens are fetched from the NotebookLM homepage:
- `SNlM0e` (CSRF token) — sent as `at=` on every RPC call
- `FdrFJe` (session ID) — sent as `f.sid=` URL parameter

**Auto-refresh:** If an RPC call fails with an auth error (expired, unauthorized), the library automatically re-fetches tokens and retries once.

**Multi-account / CI/CD:**
- Named profiles: `notebooklm profile create work` → `notebooklm -p work ...`
- `NOTEBOOKLM_AUTH_JSON` — inline JSON for CI secrets
- `NOTEBOOKLM_HOME` — custom config directory for parallel agent isolation

**Regional cookie support:** ~90 Google regional TLDs (.google.com.sg, .google.co.jp, etc.) so non-US Google accounts work correctly.

## Creative Tools — Full Artifact Coverage

All 9 NotebookLM Studio artifact types are supported:

| Artifact | CLI | Download formats |
|----------|-----|-----------------|
| Audio Overview (podcast) | `notebooklm generate audio` | MP3, MP4 |
| Video Overview | `notebooklm generate video` | MP4 |
| Cinematic Video | `notebooklm generate cinematic-video` | MP4 |
| Slide Deck | `notebooklm generate slide-deck` | **PDF, PPTX** |
| Infographic | `notebooklm generate infographic` | PNG |
| Quiz | `notebooklm generate quiz` | **JSON, Markdown, HTML** |
| Flashcards | `notebooklm generate flashcards` | **JSON, Markdown, HTML** |
| Report | `notebooklm generate report` | Markdown |
| Data Table | `notebooklm generate data-table` | **CSV** |
| Mind Map | `notebooklm generate mind-map` | **JSON** |

**Slide deck PPTX export** and **quiz/flashcard JSON export** are API-only — not available in the web UI.

### Generation flow

1. `CREATE_ARTIFACT` RPC → returns task ID
2. Poll `POLL_RESEARCH` every 3 seconds until `completed`
3. For media (audio/video/infographic/slides): additionally wait for CDN URL availability

Rate limiting: exponential backoff (60s initial, 5min cap, 2x multiplier) on HTTP 429.

## Notebook Requirement

**Every operation requires a notebook.** There is no notebook-free mode.

Notebook-scoped operations:
- Add sources → `notebooklm source add <url> --notebook <id>`
- Chat → `notebooklm chat ask "?" --notebook <id>`
- Generate any artifact → `notebooklm generate audio ... --notebook <id>`
- Research → `notebooklm research start ... --notebook <id>`
- Share → `notebooklm share set-public --notebook <id>`

Only two operations are notebook-independent:
- `notebooklm list` — list all notebooks
- `notebooklm create "Title"` — create a new notebook

The CLI tracks the active notebook in `~/.notebooklm/context.json` (set via `notebooklm use <id>`). All commands call `require_notebook()` which returns the `--notebook` flag value if provided, else falls back to the context file, else errors.

## Architecture

```
notebooklm/
├── client.py              # NotebookLMClient — async context manager
├── _core.py               # ClientCore — HTTP/RPC, conversation cache, auto-refresh
├── auth.py                # Cookie extraction, token fetch, regional domains
├── rpc/
│   ├── encoder.py         # batchexecute request: triple-nested array + form-encode
│   ├── decoder.py         # chunked response + anti-XSSI stripping + error codes
│   └── types.py           # ~40 RPCMethod enum values (obfuscated strings)
├── _sources.py            # URLs, YouTube, PDF, Drive, text, images, audio
├── _artifacts.py         # All 9 artifact types
├── _chat.py              # Streaming Q&A via GenerateFreeFormStreamed endpoint
├── _notebooks.py          # CRUD
├── _research.py          # Web/drive research sessions
├── _notes.py             # Notes + mind map generation
├── _settings.py          # Output language
├── _sharing.py           # Public links + permissions
├── cli/                  # Click CLI: ~20 command groups
└── exceptions.py         # Typed exception hierarchy
```

### Protocol

Google's internal **batchexecute** AJAX RPC — same mechanism Google uses for its own internal AJAX apps:

```
POST https://notebooklm.google.com/_/LabsTailwindUi/data/batchexecute
  ?rpcids=<method_id>&source-path=<path>&f.sid=<session>&rt=c

Body: f.req=<URL-encoded JSON>&at=<csrf_token>&
```

Method IDs are reverse-engineered obfuscated strings (e.g., `wXbhsf=LIST_NOTEBOOKS`, `R7cb6c=CREATE_ARTIFACT`). The library maintains ~40 of these.

**Chat uses a separate streaming endpoint:**
```
POST https://notebooklm.google.com/_/LabsTailwindUi/data/google.internal.labs.tailwind.orchestration.v1.LabsTailwindOrchestrationService/GenerateFreeFormStreamed
```

## CLI Reference

```
notebooklm login                    Browser-based auth
notebooklm list                     List notebooks
notebooklm create/del/rename        Notebook CRUD
notebooklm use <id>                 Set active notebook
notebooklm source add/get/del/refresh/list
notebooklm chat ask "?"
notebooklm generate audio/video/slide-deck/infographic/quiz/flashcards/report/mind-map/data-table
notebooklm download <type> <path> [--format]
notebooklm research start/poll/import
notebooklm share set-public/set-private
notebooklm agent show codex|claude
notebooklm skill install
notebooklm profile create/use/list/delete
notebooklm doctor                   Diagnose auth issues
notebooklm language list
```

## Risks and Limitations

- **Unofficial API** — uses undocumented Google internal endpoints that can break any time
- **Cookie auth fragility** — session cookies expire; the library auto-refreshes but users must re-login periodically
- **Rate limiting** — Google's NotebookLM has per-user and per-ip rate limits; the library handles 429s with backoff but no queue
- **No service account support** — can't be used in server-side Google Workspace automation without a real browser session
- **Polling, not webhooks** — artifact generation uses polling, not real-time callbacks; 3-second poll interval is not configurable

## Related

- [[claude-code-source-leak]] — Claude Code internals research
- [[vibevoice]] — Microsoft voice AI (related: NotebookLM Audio Overview as competing TTS output)
- [[gsd-2-ai-vibe-coding-framework]] — vibe coding framework
- [[a2a-protocol-cross-agent-communication]] — Google's A2A agent protocol
