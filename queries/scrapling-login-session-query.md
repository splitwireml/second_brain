---
title: Scrapling follow-up query — logged-in scraping, session persistence, cookies, and Firefox profile reuse
created: 2026-04-13
updated: 2026-04-14
type: query
tags: [tools, web-scraping, automation, method]
sources: [raw/articles/scrapling-technical-research-2026-04-13.md]
question: "How does Scrapling handle authenticated scraping, including persistent sessions, manual cookies, storage_state-style artifacts, and Firefox profile reuse?"
answer_status: answered
related_pages:
  - [[scrapling]]
  - [[scrapling-api-crawl-js-ssr-query]]
  - [[scrapling-vs-scrapy-vs-firecrawl]]
---

## Question

How does [[scrapling]] handle logged-in scraping?

Specifically:

1. Is the intended flow to log in once and persist the session?
2. Does it support manual cookie injection?
3. Does it save/load a JSON browser session artifact such as Playwright `storage_state`?
4. Can it reuse an existing logged-in Firefox session/profile directly?

## Answer

### Primary mechanism: persistent browser profile directory

Confirmed from current docs and source: Scrapling's browser-session persistence is centered on `user_data_dir`.

- `DynamicSession` and `StealthySession` both launch a persistent Playwright browser context
- the docs define `user_data_dir` as a directory storing browser session data such as cookies and local storage
- if you do not provide it, Scrapling defaults to a temporary profile directory for that run

So the intended pattern is:

1. create a stable profile directory
2. launch a browser session with `headless=False` and that `user_data_dir`
3. log in manually once
4. reuse the same `user_data_dir` on later runs

### Cookies are also supported directly

Confirmed from the browser base code: if `cookies` are provided, Scrapling calls `ctx.add_cookies(config.cookies)` on the browser context.

That means authenticated scraping can also be done by injecting cookies manually rather than relying on the persistent profile directory.

### No confirmed built-in JSON session save/load flow

I did not find a current built-in `storage_state` save/load mechanism in the Scrapling docs or source.

So the answer to "do I save a JSON session file?" is: not as the primary documented/current mechanism. The current first-class mechanism is `user_data_dir`, not a dedicated JSON session artifact.

### Firefox-profile reuse is not confirmed in the current implementation

Important distinction: the current browser implementation uses Playwright Chromium in the main codepath.

- persistent contexts are launched through `playwright.chromium.launch_persistent_context(...)`
- CDP support also connects through `playwright.chromium.connect_over_cdp(...)`

So current Scrapling is not primarily built around direct reuse of an existing Firefox profile/session.

The docs mention a Firefox/Camoufox path only as an older or optional engine pattern from before v0.3.13, not as the main current implementation.

### CDP is not the same as reusing an existing personal browser session

Scrapling supports `cdp_url`, but the implementation connects to Chromium over CDP and then creates a new context. That is not equivalent to a first-class "use my already logged-in Firefox browser session" feature.

## Practical verdict

For authenticated scraping with [[scrapling]], the supported mechanisms are:

- persistent browser profile reuse via `user_data_dir`
- manual cookie injection via `cookies`
- request/session reuse in the HTTP layer via `FetcherSession`

What is not confirmed:

- built-in Playwright `storage_state` JSON save/load
- turnkey reuse of an existing logged-in Firefox profile/session

So the cleanest current workflow is to create a dedicated persistent browser profile for [[scrapling]], log in once, and reuse that same profile directory on later runs.

## Related

- [[scrapling]] — main entity page covering architecture, anti-bot behavior, sessions, and browser layers
- [[scrapling-api-crawl-js-ssr-query]] — adjacent follow-up on API scraping, JS pages, and SSR handling
- [[scrapling-vs-scrapy-vs-firecrawl]] — broader positioning relative to crawler frameworks and hosted services