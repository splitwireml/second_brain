---
title: xurl Hermes Setup
created: 2026-05-20
updated: 2026-05-20
type: concept
tags: [tools, hermes-agent, integration, x-api]
sources: [raw/articles/xurl-hermes-setup-2056871280599847054.md]
---

## Definition

Installing and configuring the xurl skill in Hermes Agent to give it read/write access to X via the full X API surface — posting, bookmarks, search, profile lookup, and more through natural language.

## Setup Steps

1. **Install Hermes** — `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`
2. **Run setup wizard** — select xAI Grok OAuth, complete browser login
3. **Install xurl** — `curl -fsSL https://raw.githubusercontent.com/xdevplatform/xurl/main/install.sh | bash`
4. **Authenticate xurl** — create X developer app, OAuth flow with `--app` flag, `xurl auth default`
5. **Launch Hermes, load /xurl** — natural language X interaction

## Key Points

- xurl needs OAuth 2.0 credentials from an X developer app
- Redirect URI must be `http://localhost:8080/callback`
- Must use `--app my-app` flag in `xurl auth oauth2 --app my-app`
- Tokens auto-refresh in the background, stored in `~/.hermes/auth.json`

## Capabilities via Hermes

Post, search, get bookmarks, get timeline, like/unlike, reply, quote, manage lists — all through conversation.

## Related

- [[anatoli-kopadze-thread-2026-05-01]]

- [[hermes-agent]]
- [[xdevelopers]]