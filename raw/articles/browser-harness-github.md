---
updated: 2026-04-19
type: raw
url: https://github.com/browser-use/browser-harness
title: browser-harness
description: Self-healing browser harness that enables LLMs to complete any browser task
author: browser-use
created: 2026-04-17
source: github
stars: 121
language: Python
---

# browser-harness

The simplest, thinnest, self-healing browser harness that gives LLMs complete freedom to complete any browser task. Built directly on CDP.

The agent writes what's missing, mid-task. No framework, no recipes, no rails. One websocket to Chrome, nothing between.

## Setup prompt

Paste into Claude Code or Codex:

```
Set up https://github.com/browser-use/browser-harness for me.

Read `install.md` first to install and connect this repo to my real browser. Then read `SKILL.md` for normal usage. Always read `helpers.py` because that is where the functions are. When I open a setup or verification tab, activate it so I can see the active browser tab. After it is installed, if I am already logged in to GitHub, star this repository as a small verification task; if I am not logged in, just go to browser-use.com.
```

## Remote browsers

Useful for sub-agents or deployment. Free tier: 3 concurrent browsers, no card required.

- Grab a key at cloud.browser-use.com/new-api-key
- Or let the agent sign up itself via docs.browser-use.com/llms.txt

## How simple is it? (~592 lines of Python)

- `install.md` — first-time install and browser bootstrap
- `SKILL.md` — day-to-day usage
- `run.py` (~36 lines) — runs plain Python with helpers preloaded
- `helpers.py` (~195 lines) — starting tool calls; the agent edits these
- `admin.py` + `daemon.py` (~361 lines) — daemon bootstrap plus the CDP websocket and socket bridge

## install.md

Use this file only for first-time install, reconnect, or cold-start browser bootstrap. For day-to-day browser work, read `SKILL.md`.

### Best everyday setup

Clone the repo once into a durable location, then install it as an editable tool so `browser-harness` works from any directory:

```bash
git clone https://github.com/browser-use/browser-harness
cd browser-harness
uv tool install -e .
command -v browser-harness
```

### Browser bootstrap

1. Run `uv sync`. If `browser-harness` is still missing after that, run `command -v browser-harness >/dev/null || uv tool install -e .`.
2. First try the harness directly. If this works, skip manual browser setup:
```bash
uv run browser-harness <<'PY'
print(page_info())
PY
```
3. If that fails and Chrome is already running, open `chrome://inspect/#remote-debugging` in the existing Chrome profile instead of launching a fresh Chrome process.
4. If Chrome is not running, start Chrome first and let the user choose their normal profile if Chrome opens the profile picker.
5. Be explicit with the user about the two possible Chrome actions: choose their normal profile if the profile picker is open, and in the remote-debugging tab tick the checkbox and click `Allow` once if Chrome shows it.
6. Verify with:
```bash
uv run browser-harness <<'PY'
goto("https://github.com/browser-use/browser-harness")
wait_for_load()
print(page_info())
PY
```

### Cold-start reminders

- Try attaching before asking for setup changes.
- The first connect may block on Chrome's `Allow` dialog.
- `DevToolsActivePort` can exist before the port is actually listening. Treat connection refused as "still enabling."
- If the port is listening but `/json/version` returns `404`, treat that as expected on newer Chrome builds and retry `browser-harness`.

## daemon.py key logic

CDP WS holder + Unix socket relay. One daemon per BU_NAME.

Chrome profile discovery paths:
```python
PROFILES = [
    Path.home() / "Library/Application Support/Google/Chrome",       # macOS
    Path.home() / ".config/google-chrome",                          # Linux
    Path.home() / "AppData/Local/Google/Chrome/User Data",         # Windows
]
```

Connects via `DevToolsActivePort` file in the Chrome profile directory.

## helpers.py functions

Core functions available to the agent:
- `goto(url)` — navigate
- `page_info()` — `{url, title, w, h, sx, sy, pw, ph}`
- `click(x, y)` / `type_text(text)` / `press_key(key)` / `scroll(x, y)`
- `screenshot(path, full)` — capture screenshot
- `list_tabs()` / `current_tab()` / `switch_tab(target_id)` / `new_tab(url)`
- `ensure_real_tab()` — switch to a real user tab if current is chrome:// / internal / stale
- `wait(seconds)` / `wait_for_load(timeout)`
- `js(expression, target_id)` — run JavaScript
- `upload_file(selector, path)` — file input via CDP
- `http_get(url)` — pure HTTP, no browser