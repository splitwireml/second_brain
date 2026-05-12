---
title: browser-harness
created: 2026-04-19
updated: 2026-04-19
type: entity
tags: [browser-automation, agent, open-source]
sources: [raw/articles/browser-harness-github.md]
related_entity: [[browser-use]]
---

# browser-harness

Self-healing browser harness by [[browser-use]] that gives LLMs complete freedom to complete any browser task via direct CDP (Chrome DevTools Protocol) access.

## What it is

A thin (~592 lines of Python) direct CDP harness. No framework, no recipes, no rails. The agent writes the missing code mid-task — `helpers.py` is its primary extension point.

**Tagline:** "You will never use the browser again."

## Architecture

```
Chrome (local or cloud) → CDP WebSocket → daemon.py → /tmp/bu-<NAME>.sock → helpers.py
```

- `daemon.py` (~200 lines) — CDP websocket client + Unix socket relay. One daemon per `BU_NAME`.
- `admin.py` (~160 lines) — daemon lifecycle management, remote browser startup via Browser Use cloud API.
- `helpers.py` (~195 lines) — starting tool calls. Agent edits these mid-task.
- `run.py` (~36 lines) — entry point; calls `ensure_daemon()` then `exec()` Python REPL.

**Protocol:** one JSON line each way over Unix domain socket.

## Local mode (default)

Connects to the user's **already-running, signed-in Chrome** via Chrome's built-in remote debugging interface. Chrome discovery reads `DevToolsActivePort` from:

- macOS: `~/Library/Application Support/Google/Chrome`
- Linux: `~/.config/google-chrome`
- Windows: `~/AppData/Local/Google/Chrome/User Data`

No API key required. No cloud dependency.

**Profile access:** The harness attaches to whatever Chrome profile is currently running — meaning all signed-in sessions (Google, GitHub, cookies, localStorage) are live. The harness does NOT launch a fresh browser.

**First-connect requirement:** Chrome shows a native "Allow debugging" dialog on first CDP attach. User must click "Allow" once. After that it persists until Chrome restarts.

## Remote mode (optional)

Set via `BROWSER_USE_API_KEY` in `.env`. Used for parallel agents, sub-agents, or deployment. Free tier: 3 concurrent browsers, no card required at cloud.browser-use.com.

Remote daemon is managed via Browser Use REST API (`api.browser-use.com/api/v3`).

## Self-healing mechanism

When the agent encounters a missing capability (e.g., `upload_file()`), it edits `helpers.py` mid-task to add it, then retries. The next `browser-harness` invocation picks up the updated code.

## Security considerations

- Unix socket (`/tmp/bu-<NAME>.sock`) has `0o600` permissions — owner-only access.
- Full CDP access to Chrome means reading all cookies, localStorage, and JavaScript execution in any open tab.
- Since it uses the user's real signed-in profile, any code running through the harness has the same browser privileges as a DevTools user with the profile open.

## Comparison to alternatives

| | browser-harness | [[pinchtab]] | [[camoufox]] |
|---|---|---|---|
| Browser model | Attaches to user's real Chrome | Launches own browser | Anti-detection fork |
| Profile | User's signed-in profile | Isolated | Isolated |
| Transport | CDP WS → Unix socket | Standalone HTTP server | Playwright/CDP |
| Self-healing | Yes (edits helpers.py) | No | No |
| License | MIT | MIT | Apache 2.0 |

## Related

- [[browser-use]] — company behind the harness
- [[http-browser-automation-for-ai-agents]] — concept of HTTP-based browser control
- [[agent-web-stack]] — includes browser-use as final interaction layer
