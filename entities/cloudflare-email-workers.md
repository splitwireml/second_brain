---
title: Cloudflare Email Service
created: 2026-04-18
updated: 2026-04-18
type: entity
tags: [platform, inference, apple-silicon, benchmark, llm]
sources: [raw/articles/x-bookmark-2044813085358117062.md, raw/articles/x-bookmark-2044766954032951792.md]
related_entity: [[llama-cpp]]
---

# Cloudflare Email Service

Cloudflare Workers Email Service — public beta (as of April 16, 2026) enabling developers to send and receive emails directly from Cloudflare Workers via REST API or the Agents SDK, with global delivery on Cloudflare's network.

## Overview

Email infrastructure running as a Cloudflare Worker — no mail server configuration, no SMTP relay setup. Developers call a REST API or use the Cloudflare Agents SDK to send/receive emails with the latency and global coverage of Cloudflare's anycast network.

Announced by [@thomasgauvin](https://x.com/thomasgauvin/status/2044766954032951792) on April 16, 2026. Built on top of Cloudflare's existing email routing infrastructure.

## Key Capabilities

- **Send emails** directly from Workers using REST API
- **Receive emails** — inbound email handling in Workers
- **Global delivery** on Cloudflare's network
- **Agents SDK integration** — designed for building AI agents that send/receive email as part of workflows
- **Public beta** as of April 16, 2026

## Relationship to Other Entities

- [[tinygrad]] — separate infrastructure topic (GPU drivers, local inference)
- [[llama-cpp]] — separate inference engine topic

## References

- [@thomasgauvin announcement](https://x.com/thomasgauvin/status/2044766954032951792)
