---
title: "Browser-Agent Local SEO: Website Audits"
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [seo, local-seo, browser-agents, browser-automation, prompt-engineering, workflow]
sources: [raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]
---

# Browser-Agent Local SEO: Website Audits

## Scope and provenance

Technical sub-concept of [[claude-cowork-seo-system]], preserving Sarvesh Shrivastava ( [[bloggersarvesh]] )'s August 19, 2026 “Grok Bot” variant. Ingested October 7 from a complete local export. This is a source-described workflow and exact prompt record, not an executed audit or independently verified product capability. ^[raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]

## Transferable mechanism

Use browser-accessible competitor gaps and first-party search data to choose whether to optimize an existing page, build a service-city page, or rewrite messaging from customer language. The source specifies logged-in SEMrush and Google Search Console plus Chrome/website/GBP inspection; it supplies no model version, model API, executable crawler, spreadsheet file name, opportunity-score formula or measured ranking result. Full bootstrap and week 1–12 order remain in [[claude-cowork-seo-system]]. ^[raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]

| Prompt | Evidence and output contract |
|---:|---|
| 9 | SEMrush Keyword Gap, own domain versus three competitors; competitors positions 1–20 while own domain absent; export, then volume 100–2,000/month, city/service/near me/emergency/best/local words and KD under 40; top 20 spreadsheet sorted by opportunity score; volume/KD/competitor positions/existing-vs-new page; exact `Action Required` values `Optimize existing page` / `Create new page`. High-volume + low-KD + competitor overlap is the stated ranking heuristic, not a numeric formula. |
| 10 | GSC property→Search Results, last three months, export all queries/pages; per-page keywords/positions/impressions/clicks and intentional-vs-accidental ranking; positions 4–15, high-impression/low-click, zero-ranking and wrong-page/cannibalization buckets; this-week quick wins, next-month rebuilds, next-90-day new pages; current/target position, estimated improvement time and exact on-page changes. |
| 11 | Inventory service×city combinations for five named cities; target patterns `[service] + [city]`, `[service] near [city]`, `best [service] in [city]`; each missing page: title <60 characters, meta <155, natural H1, 100-word opening, 150-word city-specific why-us, 200-word service/process/benefits, city review placeholder, three local FAQs, phone + same-day-service CTA; exact slug, three existing internal-link opportunities and two local citations/directories. |
| 12 | GSC export of last 90 days: all queries/pages/clicks/impressions/CTR/average position; positions 11–20 with ≥100 impressions/month; ranking page title/H1/first-100-word keyword, word count, inbound internal links, current meta; 30-day sprint: week 1 title/H1 for top ten, week 2 thin pages under 500 words, week 3 exact page-to-page links, week 4 meta/CTR fixes; provide replacement copy, not generic instructions. |
| 13 | Last 100 reviews for each of three competitors, then own GBP; top 20 emotional words, ten outcomes, five pre-service fears, exact recommendation phrases, 5-star versus 3-star language; compare emotional gaps; rewrite GBP description, homepage headline/subheadline, review request and three social-proof statements. |

The source claims service-city pages enable rankings, one title change can move page 2 to page 1, and a position-15→5 move is worth more than ten new pages. Those assertions and “before lunch” delivery remain author claims, not observed effects. Review-language extraction is a requested copy handoff, not verified sentiment software. ^[raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]

## Verbatim source section — prompts 9–13

The upstream quotation/Markdown order is tangled in prompts 10, 12. The byte-derived excerpt below deliberately retains that order, broken links, spacing and quotation boundaries; the table above explains the task without replacing or silently repairing its canonical prompt.

~~~text
## PART 2: WEBSITE (prompts 9-13)

9. keyword gap audit

find every keyword your competitors rank for that you don't. this is where the revenue your website should be generating is hiding.

> "Open Chrome and log into my SEMrush account at semrush. com. Go to the Keyword Gap tool and enter my domain [yourdomain. com] and these 3 competitor domains: [competitor1. com], [competitor2. com], [competitor3. com].   Filter results to show only keywords where competitors rank in positions 1-20 but I don't rank at all and export this list. From that list, filter down further to only keywords that meet all of these criteria: monthly search volume between 100 and 2,000 which is the local intent sweet spot, keyword contains at least one of these words: [city name], [service type], 'near me', 'emergency', 'best', 'local', and keyword difficulty under 40. For the top 20 keywords from that filtered list, tell me the current search volume, keyword difficulty, which competitors rank for it and at what position, whether I have any existing page that could rank for it with optimization, and whether I need a new page to target it.   Output as a spreadsheet sorted by opportunity score where high volume plus low difficulty plus multiple competitors ranking equals highest priority. Add a final column called 'Action Required' that says either 'Optimize existing page' or 'Create new page' for each keyword."

why this matters: most businesses are invisible for searches their competitors are winning every day. this audit shows you exactly where the revenue gap is and what to do about it. the filtered list removes all the noise and gives you only the keywords worth going after - the ones with real buyer intent and real search volume.

10. money page audit

most local business websites have the wrong pages ranking. or no pages ranking at all. this audit fixes that.

> ].   Go to Search Results, set the date range to last 3 months, and export all queries and pages. For each page on my site, tell me what keywords it currently ranks for, the average position for each keyword, impressions and clicks for each keyword, and whether the page is optimized for the keyword it's ranking for or whether it's ranking accidentally.   Then identify: pages ranking in positions 4-15 for high-value keywords because these need one optimization push to hit top 3, pages with high impressions but low clicks because that's a title and meta description problem, pages with zero rankings because those are either dead weight or untapped opportunity, and keywords I'm ranking for on a page that isn't the right page for that keyword because that's a cannibalization issue.   Then build me a priority action list with quick wins being pages to optimize this week for immediate ranking improvement, medium effort being pages to rebuild over the next month, and long term being new pages to create over the next 90 days. For each item include the current position, target position, estimated time to see improvement, and exact on-page changes needed.""Open Chrome and go to my Google Search Console at[search.google.com/search-console](https://search.google.com/search-console), log in, and access the property for [[yourdomain.com](https://yourdomain.com/)

why this matters: most businesses are sitting on page 2 rankings that are one title tag change away from page 1. this audit finds them all and tells you exactly what to fix first - no guesswork, no wasted effort.

11. service + city page builder

the fastest way to rank in multiple cities is a dedicated page per service per city. most businesses have one generic service page and wonder why they don't show up in cities 30 minutes away.

> "I need to build location-specific service pages for my website. My primary service is [your main service], the cities I serve are [city1], [city2], [city3], [city4], [city5], my website is [URL], and my target keyword pattern is [service] + [city], [service] near [city], best [service] in [city].   First open Chrome and check my website at [URL] and tell me which city plus service combination pages already exist and which are missing.   Then for each missing combination write a fully optimized page that includes: an SEO title under 60 characters that naturally includes service and city, a meta description under 155 characters that includes service and city and a compelling reason to click, an H1 heading with service and city written naturally, an opening paragraph of 100 words that addresses the specific pain point of someone in that city needing this service right now, a why choose us section of 150 words specific to that city mentioning local landmarks or neighborhoods or area-specific challenges where relevant, a service details section of 200 words covering what the service includes and what the process looks like and what the customer gets, a social proof section with a placeholder for reviews from that city, a FAQ section with 3 questions specific to customers in that city, and a CTA with phone number and 'Call now for same-day service in [city]'.   For each page also give me the exact URL slug, 3 internal linking opportunities from existing pages on my site, and 2 local citations or directories where I should list this specific city plus service combination."

why this matters: Google ranks pages not websites. if you don't have a page specifically about [service] in [city], you will not rank for that search. this prompt builds the entire location page stack in one session - the work that would take a team of writers weeks gets done before lunch.

12. Google Search Console analysis

most business owners log into GSC, get overwhelmed, and close the tab. this prompt makes sense of all of it and finds the revenue hiding on page 2.

> ]. Export the last 90 days of search performance data including all queries, all pages, clicks, impressions, CTR, and average position.   Find my page 2 goldmine by identifying every keyword where I rank between position 11 and 20 with at least 100 impressions per month - these are my highest priority optimization targets because a jump from position 15 to position 5 is worth more than creating 10 new pages. For each page 2 keyword, open the page that's ranking for it on my site and tell me whether the keyword is in the title tag, whether it's in the H1, whether it's in the first 100 words of the page, how many words the page is, whether the page has internal links pointing to it, and what the current meta description says.   Then build me a 30-day optimization sprint where week 1 covers title tag and H1 fixes for the top 10 page 2 keywords, week 2 covers content additions for pages that are too thin (under 500 words), week 3 covers internal linking fixes with exactly which pages should link to which pages, and week 4 covers meta description rewrites to fix pages with high impressions but low CTR. For every single fix, write me the exact new copy - don't give me instructions, give me the actual title tag and H1 and meta description I should use.""Open Chrome and log into Google Search Console at[search.google.com/search-console](https://search.google.com/search-console)for my property [[yourdomain.com](https://yourdomain.com/)

why this matters: page 2 keywords are the lowest hanging fruit in all of SEO. someone is already searching for exactly what you offer - you're just one optimization push away from being visible. this prompt finds every single one of them and tells you exactly what to write.

13. review sentiment analysis

this is the prompt most agencies don't know exists. it takes your competitor's reviews and reverse-engineers the exact emotional language customers use - then builds that language into your website copy, GBP content, and review request scripts. the result is content that resonates at a gut level because it's written in the words your actual customers use.

> "Open Chrome and go to these competitor GBP listings: [URL1], [URL2], [URL3]. Read through the last 100 reviews for each competitor.   I want you to do a deep sentiment analysis across all reviews. Extract: the top 20 emotional words customers use most frequently (e.g. 'relieved', 'impressed', 'finally', 'trustworthy'), the top 10 specific outcomes customers mention (e.g. 'fixed in one visit', 'no mess left behind', 'arrived on time'), the top 5 fears or frustrations mentioned before the service was done (e.g. 'worried it would cost a fortune', 'other companies kept canceling'), the exact phrases customers use when they recommend to others (these are the money phrases for your website), and any language patterns that appear in 5-star reviews but not in 3-star reviews.   Then do the same analysis for my reviews at [my GBP URL]. Compare the sentiment and language between my reviews and my top competitor's reviews and tell me where the emotional gaps are. Finally use all of this data to rewrite: my GBP description using the emotional language real customers use, my homepage headline and subheadline, my review request script so customers naturally use the right words and phrases, and 3 social proof statements I can put on my website that mirror how my best customers talk about my service."

why this matters: most businesses write their own website copy about themselves. the businesses that dominate write their copy in the language their customers actually use. review sentiment analysis finds that language - the exact words that make a stranger trust you enough to call. this is what conversion rate optimisation actually looks like for local businesses.
~~~

## Related

- [[claude-cowork-seo-system]] — business context and exact 12-week execution plan.
- [[claude-cowork-seo-system-prompt-library]] — earlier Claude/Cowork prompt cards; do not overwrite their runtime-specific context.
- [[browser-agent-local-seo-gbp]] — adjacent source-specific audit mechanics.
- [[browser-agents]] — browser-operator interface boundary.
