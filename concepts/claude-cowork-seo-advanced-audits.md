---
title: "Claude Cowork SEO System: Advanced Audits"
created: 2026-08-03
updated: 2026-08-03
type: concept
tags: [seo, local-seo, claude-cowork, browser-automation, workflow, backlink, conversion, website]
sources: [raw/articles/bloggersarvesh-chief-of-seo-claude-cowork-2026-03-25.md, raw/articles/bloggersarvesh-claude-cowork-seo-2037158013921042794.md, raw/articles/bloggersarvesh-claude-seo-100k-month-playbook-2032130279494853118.md, raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]
---

# Claude Cowork SEO System: Advanced Audits

## Scope and version status

The public Alventra page expands the earlier 20-part system to 22 prompts. Prompt 21 is a detailed on-page audit; prompt 22 is a page-level Ahrefs backlink-gap audit. The public page's 12-week execution schedule still ends at prompt 20, so the placement of these two extensions is **confirmed as unspecified**, not silently guessed. See [[claude-cowork-seo-system]] and [[claude-cowork-seo-system-prompt-library]].

## Prompt 21 — detailed on-page SEO audit

### Source prompt contract

```text
You are now my Head of On-Page SEO. You have 14 years of experience optimising local business and service pages and do not tolerate generic advice. When you say something is broken, tell me exactly what to replace it with.

Open Chrome and fetch this page: [URL].
The target keyword is: [TARGET KEYWORD].
Open the top five ranking pages for that keyword in an incognito tab and benchmark every recommendation against what is actually ranking.
Do not skip sections. Do not summarise. Work through every element in order.
```

The public example supplies `https://thedallasroofers.com/` and `roof replacement dallas`; those are examples, not fixed inputs. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

### Section 1 — non-negotiables

For title, meta description, URL, and H1, output:

`Element | Current | Character/Word Count | Score (0–10) | What's Wrong | Exact Rewrite | Why This Wins`

Required checks:

- **Title:** under 60 characters, target keyword first, plus a hook such as a number, year, modifier, or location; flag buried keywords, stuffing, and AI-sounding language.
- **Meta description:** under 155 characters, keyword once naturally, ending in a CTA; rewrite rather than merely rate it.
- **URL:** short, keyword-bearing, no unnecessary stop words or dates; if wrong, recommend leave-as-is or redirect and write the 301 line.
- **H1:** exactly one, containing the target keyword and matching intent; provide the exact replacement text if wrong and explain the Google/reader advantage in two sentences.

### Section 2 — heading structure

Pull every H2/H3/H4 in order and produce:

1. the current nested outline;
2. a corrected nested outline;
3. whether each H2 is a real heading or a styled paragraph;
4. missing subtopics covered by the top five ranking pages;
5. semantic/entity variations used by competitors;
6. exact rewrites for weak H2s;
7. H3 nesting corrections and H3s that should become H2s;
8. new H3s for relevant People Also Ask questions.

End with the complete corrected outline as a clean indented list.

### Section 3 — paragraph and body-copy critique

Provide a verdict and exact rewrite where needed for:

- the first 100 words: keyword in the first sentence and immediate intent satisfaction;
- paragraphs longer than four lines;
- natural keyword density, exact-match count, and semantic-variation count;
- the top ten ranking-page entities missing from the target page, with insertion locations;
- sections under 75 words that need expansion, including the expansion copy;
- fluff and AI-tell sentences, including delete/rewrite decisions;
- CTA count above the fold, mid-page, and bottom, with missing copy supplied.

### Section 4 — supporting on-page elements

Return `Element | Status | Issue | Fix` for:

- image count, every current alt text, and replacement alt text;
- image filenames, including IMG_2453-style flags;
- internal links out and anchor quality;
- internal links in: pages that should link to the target;
- external links, competitor links, and broken links;
- LocalBusiness, Article, FAQ, Breadcrumb, and Review schema;
- ready-to-paste FAQ JSON-LD when the page has Q&A but lacks FAQ schema;
- Open Graph and Twitter cards;
- word count versus the top-five average and the gap;
- table of contents presence/need;
- featured-snippet opportunity, with a definition/list/table block written if absent.

### Section 5 — intent match and section 6 — scorecard

State whether the page matches informational, comparison, or hire/buy intent and whether it delivers that intent. If not, say what page type it should be.

Then score:

`Title | Meta | URL | H1 | Heading Structure | Body Copy | Keyword Usage | Entity Coverage | Internal Linking | Images/Alt | Schema | Intent Match | Overall`

For every row include score/10, priority, and time to fix.

### Section 7 — WordPress fix-it checklist

Write a numbered top-to-bottom checklist for a business owner using WordPress/Gutenberg with Yoast or Rank Math. For every fix include:

- `Fix #X — plain-English name`
- one-sentence action;
- exact click path, such as `WP Admin → Pages → All Pages → [page] → Yoast SEO → SEO tab → Meta description`;
- exact text to paste in a code block;
- estimated minutes;
- impact: High / Medium / Low.

Order by impact, not by audit section. End with the source's sentence: “If you only do the first three, you’ll still see movement within 14–30 days.” Keep that timeline attributed to the source, not as a verified guarantee.

### Prompt 21 rules

Never say “make it more keyword-rich,” “consider adding,” or another generic instruction when exact copy can be written. Use tables for comparisons. Use plain English for the WordPress section. If a page is paywalled, blocked, or JavaScript-rendered, report the limitation rather than guessing. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

## Prompt 22 — page-level backlink-gap audit

### Operating contract

```text
Act as my senior SEO analyst. You have Ahrefs access in Chrome and I am already logged in. Do not re-authenticate, create accounts, or change settings. If login or a paywalled feature blocks the work, stop and report it.

Goal: run a competitive backlink gap analysis for {{KEYWORD}} and estimate how many unique dofollow referring domains, and which DR tiers, are needed to compete for the top five.
```

### Phase 1 — SERP and backlink baseline

1. Open `https://app.ahrefs.com/keywords-explorer` in Chrome.
2. Set country to United States unless the user specifies another country.
3. Search `{{KEYWORD}}`.
4. Record KD, global and US volume, traffic potential for the number-one page, and the SERP Overview.
5. Capture the top 10 organic results, skipping ads, non-organic featured snippets, People Also Ask, video carousels, and the user's own domain.
6. For every row record rank, exact ranking URL, root-domain DR, page UR, page-level referring domains, page backlinks, and estimated organic traffic.
7. Select five normal competitor pages. Flag YouTube, Reddit, Wikipedia, Quora, or similar platform/UGC results; replace them with the next normal organic result where possible and state every swap.

**Important distinction:** page-level referring domains are the working metric; domain-level DR is context, not the target count. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

### Phase 2 — exact-URL competitor drill-down

Process the five pages sequentially and save each competitor as a checkpoint.

1. From SERP Overview, open the backlink report for the exact ranking URL.
2. Verify scope is `Exact URL`, not Prefix or Domain.
3. Apply filters in this order:
   - dofollow only;
   - one link per domain enabled;
   - English unless the user specifies another language;
   - Platform = All;
   - sort by DR descending.
4. Capture the full filtered set, or the top 100 if longer.
5. Record referring page URL, referring domain, DR, anchor text truncated to 60 characters, link type, and first-seen date.
6. Bucket referring domains into DR 70+, 50–69, 30–49, and 0–29.
7. Separately flag niche-relevant versus generic/off-topic links; inspect only a few uncertain domains rather than opening every row.

### Phase 3 — aggregate analysis

Across the five filtered competitor pages, compute and present:

- mean and median referring domains;
- mean DR of referring domains;
- mean UR;
- mean DR of ranking root domains;
- average DR-tier distribution;
- a target based on the median plus a 10–15% buffer;
- explicit current-DR versus competitor-DR caveat when relevant;
- suspicious PBN, paid-link, or expired-domain patterns, naming competitor and links;
- top 15 referring domains that link to at least two of the five competitors, ranked by competitor count then DR.

The target sentence should have the form:

`To realistically compete for the top five, you need roughly X unique dofollow referring domains, approximately A at DR 70+, B at DR 50–69, and C at DR 30–49.`

The source's rationale is that the median resists one outlier and the buffer accounts for crawler undercounting; both are source reasoning, not a universal Ahrefs law.

### Required final report

```text
# Backlink Gap Analysis — {{KEYWORD}}
## SERP snapshot
[top 10 table]
## Competitor deep-dive
### Competitor 1 — [URL]
– RDs (filtered): N
– DR tier split: 70+ = a, 50–69 = b, 30–49 = c, 0–29 = d
– Notable patterns: …
[repeat for 2–5]
## Aggregate metrics
– Mean RDs: …
– Median RDs: …
– Avg DR of ranking domains: …
## My target to rank top 5
– Total RDs needed: …
– DR mix: …
– Key caveat: …
## Link opportunity shortlist (links to 2+ competitors)
[table of 15]
## Red flags observed
[list or “none”]
```

### Execution controls

- Wait 3–5 seconds between competitor drill-downs.
- After a rate-limit message, wait 60 seconds and retry once.
- Do not export CSVs unless explicitly requested; visible-UI data is the source workflow.
- Do not navigate away from Ahrefs except for limited topic checks on uncertain referring domains.
- If a filter is missing or fails to apply, report it before proceeding.
- Take one screenshot per competitor after filters are applied.
- Stop and ask the user if fewer than five usable organic results exist, KD exceeds 80, or brand-dominated results are structurally uncompetitive.
- Begin by confirming keyword and country before searching.
- The source estimates 15–30 minutes; that is a source-described duration, not a measured benchmark.

## Evidence boundary for both extensions

Prompts 21 and 22 specify detailed research mechanics, fields, output formats, and stop conditions. They do not establish that title rewrites, schema, backlinks, DR targets, or the source's stated ranking timelines will produce a particular outcome. Preserve blocked evidence and platform limitations in the final report.

## Related

- [[claude-cowork-seo-system]]
- [[claude-cowork-seo-system-prompt-library]]
- [[claude-cowork]]
- [[topical-authority-seo]]
- [[broken-link-building]]
- [[human-in-the-loop]]
