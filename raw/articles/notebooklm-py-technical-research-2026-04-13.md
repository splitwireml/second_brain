---
updated: 2026-04-17
title: notebooklm-py Technical Research — 2026-04-13
source: https://arxiv.org/pdf/...
type: arxiv
---

# notebooklm-py Technical Research — 2026-04-13

**Source:** github.com/teng-lin/notebooklm-py (v0.3.4)
**Research questions:** Authentication flow, creative tool coverage, notebook requirement

---

## Research Question 1: How does authentication work?

### Login mechanism

Authentication is entirely **cookie-based** — there is no OAuth, API key, or service account flow. The library extracts Google auth cookies from a browser session where the user has manually logged into their Google account.

**Two login paths:**

1. **Playwright browser automation** (`notebooklm login`):
   - Opens a real Chromium/Edge/Firefox browser pointing at notebooklm.google.com
   - User logs in manually in the browser
   - Playwright saves the browser's cookie storage state to `~/.notebooklm/storage_state.json`
   - Requires `pip install "notebooklm-py[browser]"` and `playwright install chromium`

2. **Rookiepy cookie extraction** (`notebooklm login --browser chrome`):
   - Directly reads cookies from an already-open browser session via rookiepy
   - No Playwright automation needed — just needs the browser running and logged in
   - Requires `pip install "notebooklm-py[cookies]"`
   - Supports: Chrome, Firefox, Edge, Brave, Arc, Opera, Safari, etc.

### Required cookies

The library validates that `SID` is present (minimum required). Full coverage typically needs:
- `SID` — primary session token (required)
- `__Secure-1PSID`, `__Secure-3PSID` — secure variants by account type
- `HSID`, `SSID`, `NID` — auxiliary auth cookies

**Regional cookie support:** The library includes an exhaustive list of ~90 Google regional TLDs (`google.com.sg`, `google.co.jp`, `google.co.uk`, etc.) where SID cookies may be set on a regional domain instead of `.google.com`. This is critical for non-US Google accounts.

### Runtime token extraction

On every `NotebookLMClient` init via `AuthTokens.from_storage()`, two additional tokens are fetched from the NotebookLM homepage:

- `SNlM0e` — CSRF token, passed as `at=` URL parameter on every RPC call
- `FdrFJe` — session ID, passed as `f.sid=` URL parameter

These are extracted by doing an unauthenticated GET to `notebooklm.google.com` and parsing the HTML for the token values.

### Auto-refresh on auth failure

`ClientCore` accepts a `refresh_callback`. When an RPC call returns an auth error (detected via pattern matching on error messages like "expired", "unauthorized", "re-authenticate"), the library automatically:
1. Re-fetches tokens from the homepage (`fetch_tokens()`)
2. Updates the HTTP client Cookie header
3. Retries the RPC call once

### Multi-account and CI/CD support

- **Named profiles:** `notebooklm profile create work` creates isolated auth storage at `~/.notebooklm/profiles/work/storage_state.json`. Switch with `notebooklm -p work ...`
- **Environment variable:** `NOTEBOOKLM_AUTH_JSON` accepts inline JSON of the storage_state — for CI/CD pipelines where writing a file is inconvenient
- **Custom home:** `NOTEBOOKLM_HOME=/tmp/my-env` for parallel agent isolation

### Security notes

- Storage state files contain live session cookies — saved with `0600` permissions
- The library explicitly validates cookie domains against a whitelist (`.google.com`, `.googleusercontent.com`, `notebooklm.google.com`, plus regional variants)
- Path traversal protection on all auth file paths

---

## Research Question 2: Does it have creative tools?

**Yes — full coverage of all NotebookLM Studio artifact types.**

### Supported artifact types

| Artifact | CLI command | Generation API | Download formats |
|----------|-----------|---------------|-----------------|
| **Audio Overview** (podcast) | `notebooklm generate audio` | `CREATE_ARTIFACT` → poll | MP3, MP4 |
| **Video Overview** | `notebooklm generate video` | `CREATE_ARTIFACT` → poll | MP4 |
| **Cinematic Video** | `notebooklm generate cinematic-video` | `CREATE_ARTIFACT` → poll | MP4 |
| **Slide Deck** | `notebooklm generate slide-deck` | `CREATE_ARTIFACT` → poll | **PDF, PPTX** (PPTX is API-only) |
| **Infographic** | `notebooklm generate infographic` | `CREATE_ARTIFACT` → poll | PNG |
| **Quiz** | `notebooklm generate quiz` | `CREATE_ARTIFACT` → poll + HTML fetch | **JSON, Markdown, HTML** |
| **Flashcards** | `notebooklm generate flashcards` | `CREATE_ARTIFACT` → poll + HTML fetch | **JSON, Markdown, HTML** |
| **Report** | `notebooklm generate report` | `CREATE_ARTIFACT` → poll | Markdown |
| **Data Table** | `notebooklm generate data-table` | `CREATE_ARTIFACT` → poll | **CSV** |
| **Mind Map** | `notebooklm generate mind-map` | `GENERATE_MIND_MAP` | **JSON** |

### Options per artifact type

- **Audio:** 4 formats (deep-dive, brief, critique, debate), 3 lengths, 50+ languages
- **Video:** 3 formats (explainer, brief, cinematic), 9 visual styles
- **Slides:** detailed or presenter format, adjustable length, individual slide revision via natural-language prompt
- **Infographic:** 3 orientations, 3 detail levels, 9 styles (auto, sketch-note, professional, bento-grid, editorial, instructional, bricks, clay, anime, kawaii, scientific)
- **Quiz:** configurable quantity, 4 difficulty levels (easy, medium, hard, harder)
- **Flashcards:** configurable quantity, 4 difficulty levels
- **Report:** briefing doc, study guide, blog post, or custom prompt

### Beyond-web-UI capabilities

The library exposes features not available in NotebookLM's web UI:
- Batch download all artifacts of a type at once
- Quiz/flashcard export as structured JSON (web UI only shows interactive HTML)
- Mind map as JSON for visualization tools (web UI only renders visual)
- PPTX slide deck download (web UI only offers PDF)
- Individual slide revision with natural-language instructions
- Source fulltext access (indexed text of any source)

### Generation polling pattern

Artifacts are generated asynchronously. The flow:
1. Call `CREATE_ARTIFACT` RPC → returns a `GenerationStatus` with a `task_id`
2. Poll `POLL_RESEARCH` RPC every 3 seconds until status is `completed` or `failed`
3. For media artifacts (audio, video, infographic, slide deck): additionally wait for the CDN URL to become available before reporting completion

Rate limiting: `generate_with_retry()` uses exponential backoff (60s initial, 5min max, 2x multiplier) on HTTP 429.

---

## Research Question 3: Does using this mean a notebook has to be created?

**Yes — essentially all operations require a notebook ID.**

Every significant operation in the library requires an active notebook:

- Adding sources → `client.sources.add_url(notebook_id, ...)`
- Chatting → `client.chat.ask(notebook_id, ...)`
- Generating artifacts → `client.artifacts.generate_audio(notebook_id, ...)`
- Research sessions → `client.research.start(notebook_id, ...)`
- Sharing → `client.sharing.set_public(notebook_id, ...)`
- Downloading artifacts → `notebooklm download audio ./podcast.mp3 --notebook <id>`

### Operations that don't require a notebook

Only two operations are notebook-independent:
- `client.notebooks.list()` — list all your notebooks
- `client.notebooks.create(title)` — create a new notebook

### How notebooks are referenced

Notebooks are identified by UUID (e.g., `abc123-def456...`). The CLI maintains a context file (`~/.notebooklm/context.json`) storing the active notebook ID, set via `notebooklm use <id>`. All CLI commands that need a notebook call `require_notebook()` which:
1. Returns the explicit `--notebook` flag value if provided
2. Falls back to the context file's active notebook ID
3. Errors if neither is set

### The practical workflow

```
notebooklm login
notebooklm create "My Research Project"
notebooklm use <notebook-id-from-above>
notebooklm source add "https://arxiv.org/pdf/..."
notebooklm generate audio "make it engaging" --wait
notebooklm download audio ./podcast.mp3
```

You cannot bypass the notebook. It is the fundamental unit of organization in NotebookLM — sources, chat history, artifacts, and sharing settings are all scoped to a notebook.

---

## Architecture Summary

```
notebooklm/
├── client.py              # NotebookLMClient — async context manager entry point
├── _core.py               # ClientCore — HTTP/RPC engine, conversation cache
├── auth.py                # Cookie extraction, token fetch, AuthTokens dataclass
├── rpc/
│   ├── encoder.py         # batchexecute triple-nested array encoding
│   ├── decoder.py         # chunked response parsing, anti-XSSI stripping
│   └── types.py           # RPCMethod enum (~40 obfuscated method IDs), endpoints
├── _sources.py            # SourcesAPI — URLs, YouTube, PDFs, Drive, etc.
├── _artifacts.py          # ArtifactsAPI — all 9 studio artifact types
├── _chat.py               # ChatAPI — streaming question answering
├── _notebooks.py          # NotebooksAPI — CRUD
├── _research.py           # ResearchAPI — web/drive research sessions
├── _notes.py              # NotesAPI + mind map generation
├── _settings.py           # SettingsAPI — output language
├── _sharing.py            # SharingAPI — public links + permissions
├── cli/                   # Click CLI (~20 command groups)
└── exceptions.py          # Full typed exception hierarchy
```

### Protocol

Google's internal **batchexecute** AJAX protocol — not a public API:
- Endpoint: `https://notebooklm.google.com/_/LabsTailwindUi/data/batchexecute`
- Request: `f.req=<JSON-encoded triple-nested array>&at=<csrf_token>&`
- Response: chunked, anti-XSSI stripped, decoded via nested array traversal
- Method IDs are reverse-engineered obfuscated strings (e.g., `wXbhsf`, `CCqFvf`, `R7cb6c`)

### Key files examined

- `src/notebooklm/auth.py` — full cookie extraction, token fetch, regional domain handling
- `src/notebooklm/_core.py` — RPC engine, auto-refresh, conversation cache
- `src/notebooklm/rpc/encoder.py` — batchexecute request encoding
- `src/notebooklm/rpc/decoder.py` — chunked response parsing, error codes
- `src/notebooklm/rpc/types.py` — all ~40 RPC method IDs and enums
- `src/notebooklm/_artifacts.py` — all 9 artifact generation types
- `src/notebooklm/_notebooks.py` — notebook CRUD
- `src/notebooklm/cli/generate.py` — all generate CLI commands with options
- `src/notebooklm/cli/session.py` — login flow with Playwright and rookiepy
- `src/notebooklm/exceptions.py` — full exception hierarchy