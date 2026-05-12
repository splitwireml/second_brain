---
title: Firecrawl Fire Pdf Rust Parser 2026 04 15
updated: 2026-04-15
source: https://x.com/firecrawl/status/2044085849990553606
author: "@firecrawl"
date: 2026-04-14
platform: X/Twitter
tweet_id: "2044085849990553606"
type: thread
---

## Primary Tweet

**@firecrawl** — Tue Apr 14 16:10:18 +0000 2026

> Introducing Fire-PDF, our new Rust-based parsing engine 🔥
>
> - Convert PDFs into markdown 5x faster
> - Extract full tables and preserve formulas
> - Zero config required https://t.co/0V8Vn5ECW7

Engagement: 748 likes, 48 retweets, 16 replies

---

## Thread (Firecrawl's own posts only)

### Reply 1 — 16:11:15
> [ 5x Faster ]
>
> Our open-source Rust library classifies each page in under 400ms and picks the fastest extraction path.
>
> A 216-page financial report processes in ~83 seconds.

### Reply 2 — 16:11:31
> [ Layout-Aware Accuracy ]
>
> Our neural layout model detects each region individually. Tables get full markdown output and formulas are preserved in LaTeX.

### Reply 3 — 16:11:45
> [ Zero Configuration ]
>
> Every PDF sent through the Firecrawl API now goes through Fire-PDF automatically.

### Reply 4 — 16:11:58
> Turn complex PDFs into clean data in seconds: https://t.co/nN4b4yITnL

*(Link resolves to a video demo — no standalone landing page confirmed at time of ingest)*

---

## Notable Replies

- **@ericsr** — "pricing page (on this reference) 404s" (noted on the t.co link)
- **@WinterArc2125** — "@firecrawl @karpathy try this on the Mythos pdf" (tagging Karpathy as a test target)
- **@newlinedotco** — Raises production RAG concerns: zero-config parsing, coordinate/metadata preservation for chunking, visual anchoring, hierarchy of nested headers and table associations
- **@kaka_ruto** — "link to the open source repo?" — no OSS link confirmed in thread
- **@txhno** — "&gt;opensource &gt;no link" — community noting the open-source claim without a repo link
- **@plutuswealthy** / **@notatomicc** — Asking about scanned/OCR documents
- **@vinpac_io** — Asks about image/barcode cropping

---

## Verification Status

| Claim | Status | Notes |
|-------|--------|-------|
| 5x faster than existing | Unverified | Claimed by Firecrawl; no independent benchmark confirmed |
| 400ms/page classification | Unverified | Claimed; no independent measurement |
| 216-page financial report in ~83s | Unverified | Claimed; no independent measurement |
| Neural layout model | Unverified | Stated; no model name, architecture, or training data disclosed |
| Tables → full markdown | Unverified | Claimed; quality not independently tested |
| Formulas preserved in LaTeX | Unverified | Claimed; scope (MathML, handwriting, etc.) unspecified |
| Zero config | Confirmed | Confirmed in thread — no parameters required |
| Open-source Rust library | **Unverified — no public repo found** | Multiple users asked for repo link; no link provided. GitHub org `firecrawl` has 43 repos (109K star main repo). Searched `fire-pdf`, `FirePDF`, and all repos — zero matches. Claim unconfirmed. |
| Fire-PDF auto-applied to all Firecrawl API PDFs | Confirmed | Explicitly stated by Firecrawl |

---

## GitHub Investigation

- GitHub org: `firecrawl` (43 public repos including firecrawl main with 109K stars)
- Searched: `fire-pdf`, `FirePDF` across all firecrawl repos — **0 results**
- Third-party forks: `salhdl/firecrawl-pdfparsing` (0 stars) — unrelated
- firecrawl main README mentions "Media parsing: Parse and extract content from web-hosted PDFs, DOCX" — this predates Fire-PDF and refers to a different pipeline
- **Conclusion:** Fire-PDF was announced as open-source but no public repository existed at announcement time (2026-04-14)

---

## open_source tag

No public OSS repo confirmed. Revisit if a GitHub repo surfaces.