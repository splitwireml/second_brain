---
title: Heynavtoor Pinchtab Browser Automation 2026 03 03
updated: 2026-04-16
source: https://x.com/heynavtoor/status/2028922003365986705
author: "@heynavtoor (Nav Toor)"
date: 2026-03-03
type: tweet
tags: [x, browser-automation, ai-agents, http-api, open-source]
---

# @heynavtoor — PinchTab browser automation for AI agents

**Tweet ID:** 2028922003365986705
**Date:** Tue Mar 03 19:54:35 +0000 2026
**Author:** Nav Toor (@heynavtoor)
**Likes:** 5,159 | **Retweets:** 505 | **Replies:** 182

## Full Tweet

🚨 Someone just solved the biggest bottleneck in AI agents. And it's a 12MB binary.

It's called Pinchtab. It gives any AI agent full browser control through a plain HTTP API.

Not locked to a framework. Not tied to an SDK. Any agent, any language, even curl.

No config. No setup. No dependencies. Just a single Go binary.

Here's why every existing solution is broken:

→ OpenClaw's browser? Only works inside OpenClaw
→ Playwright MCP? Framework-locked
→ Browser Use? Coupled to its own stack

Pinchtab is a standalone HTTP server. Your agent sends HTTP requests. That's it.

Here's what this thing does:

→ Launches and manages its own Chrome instances
→ Exposes an accessibility-first DOM tree with stable element refs
→ Click, type, scroll, navigate. All via simple HTTP calls
→ Built-in stealth mode that bypasses bot detection on major sites
→ Persistent sessions. Log in once, stays logged in across restarts
→ Multi-instance orchestration with a real-time dashboard
→ Works headless or headed (human does 2FA, agent takes over)

Here's the wildest part:

A full page snapshot costs ~800 tokens with Pinchtab's /text endpoint.

The same page via screenshots? ~10,000 tokens.

That's 13x cheaper. On a 50-page monitoring task, you're paying $0.01 instead of $0.30.

It even has smart diff mode. Only returns what changed since the last snapshot. Your agent stops re-reading the entire page every single call.

1.6K GitHub stars. 478 commits. 15 releases. Actively maintained.

100% Open Source. MIT License.

## Repo Link

https://github.com/pinchtab/pinchtab

## Notable Replies

**@adambarlam:** Tried it out. Doesn't work nearly as well as Chrome + OpenClaw Relay plugin.

**@MgkMshrmBrkfst:** Change it to use Brave Browser instead. Chromium-based but lighter and private.

**@iamgalba:** How it's different/better than agent-browser from @vercel?

**@mrscottiem (2 replies):**
1. "Pinchtab ships with an unauthenticated HTTP port open by default, stealth mode to bypass bot detection ToS, and persistent sessions storing your real credentials in a flat file. One compromised agent prompt and it acts as you."
2. "Pinchtab lets hackers steal your money without ever touching your computer. They just put invisible text on any webpage. Your AI reads it, thinks it's an order, and wires your cash."

**@heynavtoor (security response):** "Valid security concerns. The unauthenticated port is definitely something to be aware of — should only be run locally or behind proper auth in production."

## Image Analysis

[Image: pinchtab-headless.png — shows PinchTab dashboard/architecture diagram]