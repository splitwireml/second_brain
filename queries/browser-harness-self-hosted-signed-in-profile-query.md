---
title: "browser-harness: self-hosted + signed-in Chrome profile?"
created: 2026-04-19
updated: 2026-04-19
type: query
tags: [browser-automation, self-hosted, security]
sources: [raw/articles/browser-harness-github.md]
question: "Is browser-harness self-hosted, and does it connect to a signed-in Chrome profile?"
answer_status: answered
related_pages:
  - [[browser-harness]]
  - [[browser-use]]
  - [[pinchtab]]
---

## Question

Is browser-harness self-hosted? And if so, does it connect to a signed-in Chrome profile?

## Answer

**Yes to both.**

### Self-hosted by default

browser-harness connects to Chrome running locally on the same machine via Chrome's built-in CDP remote debugging interface. There is no cloud dependency for local use. The `.env` only needs `BROWSER_USE_API_KEY` if using the optional Browser Use cloud for remote browsers.

### Connects to the user's signed-in Chrome profile

The harness attaches to the user's **already-running Chrome** — not a fresh instance. This means:

- All active signed-in sessions are live (Google, GitHub, etc.)
- Cookies, localStorage, and session state are preserved
- Extensions run normally

Chrome shows a native "Allow debugging" dialog on first connect. The user clicks "Allow" once, and it persists until Chrome restarts.

### Practical implications

Since it uses the real signed-in profile, any agent code running through the harness has the same browser privileges as the user with DevTools open. The Unix socket is `0o600` (owner-only), but the Chrome profile data itself is fully accessible to any CDP client that attaches.

## Practical verdict

For local use: fully self-hosted, zero cloud dependency, uses the user's real signed-in profile. If that's a concern (e.g., shared machines), run a dedicated Chrome profile for the harness.
