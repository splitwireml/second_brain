---
title: "Vibe-Coded Production Security"
created: 2026-05-12
updated: 2026-05-18
type: concept
tags: [coding, method, security, vibe-coding, webdev]
sources: [raw/articles/hartdrawss-thread-2054162227955982833-2026-05-12.md]
related_entity: [[hartdrawss]]
---

# Vibe-Coded Production Security

A checklist of 20 security and production-readiness failures common in vibe-coded applications, posted by [[hartdrawss]].

## The 20 Anti-Patterns

### Security

1. **No rate limiting on API routes** — spam can run up backend costs overnight
2. **Auth tokens in localStorage** — one XSS = all accounts compromised
3. **No input sanitization** — SQL injection still works in 2026
4. **Hardcoded API keys in frontend** — found within 48 hours of launch
5. **Stripe webhooks without signature verification** — anyone can fake successful payments
6. **Sessions that never expire** — stolen token = permanent account access
7. **Password reset links that don't expire** — old email = account takeover

### Scalability & Performance

8. **No database indexing on queried fields** — works at 100 users, dies at 1,000
9. **No pagination on database queries** — one fetch loads entire DB into memory
10. **No database connection pooling** — first traffic spike = crash
11. **Images uploaded directly to server** — no CDN = slow load + high hosting bill

### Error Handling & Observability

12. **No error boundaries in UI** — one crash = white screen = user never returns
13. **No environment variable validation at startup** — silent production breakage
14. **No health check endpoint** — app goes down silently, discovered by client
15. **No logging in production** — zero visibility when things break

### Integration & Deployment

16. **No CORS policy** — any website can make requests to your API
17. **Emails sent synchronously in request handlers** — slow SMTP hangs the app
18. **Admin routes with no role checks** — any logged-in user can access admin panel
19. **No backup strategy on database** — bad migration = total data loss
20. **No TypeScript on AI-generated code** — confident, wrong, untyped code shipped anyway

## Core Theme

Vibe coding tools (Cursor, Lovable, Claude Code, v0) accelerate initial development but skip production hardening. The gaps between "works on my machine" and "survives 1,000 users and an adversarial internet" are where these failures live.

## Related Concepts

- [[vibe-coding]] — The broader development paradigm
- [[github-repo-trust-verification]] — Security vetting for AI-assisted development
- [[hermes-agent]] — Agent systems that also face production hardening concerns
