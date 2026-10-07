---
title: "Browser-Agent Local SEO: Authority and Citations"
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [seo, local-seo, browser-agents, browser-automation, prompt-engineering, workflow]
sources: [raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]
---

# Browser-Agent Local SEO: Authority and Citations

## Scope and provenance

Technical sub-concept of [[claude-cowork-seo-system]], preserving Sarvesh Shrivastava ( [[bloggersarvesh]] )'s August 19, 2026 “Grok Bot” variant. Ingested October 7 from a complete local export. This is a source-described workflow and exact prompt record, not an executed audit or independently verified product capability. ^[raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]

## Transferable mechanism

Build authority work from competitor link overlap, exact NAP comparisons and buyer-intent routing. Chrome is the requested browser; Ahrefs Site Explorer supplies link profiles and SEMrush supplies intent keywords. Link/citation research becomes contact methods, full email copy, a staged 90-day plan and monthly maintenance, rather than an unspecified autonomous outreach product. The source does not supply executable integrations, actual outreach results or ready-made spreadsheet files. ^[raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]

| Prompt | Evidence and output contract |
|---:|---|
| 14 | Ahrefs Site Explorer for three competitor domains; full exports filtered to dofollow, linking-domain DR ≥20, linking-domain traffic ≥100 monthly visits, non-sitewide (no footer/sidebar); prioritize domains linking to all three but not own business, then two, then one; domain + URL, DR, directory/news/blog/association/sponsor type, guest post/sponsorship/citation/PR acquisition, high/medium/low realistic chance and exact outreach strategy; month 1 five easy directory/citation/association links, month 2 five medium news/sponsor/guest-post links, month 3 five authority publication/government/university links; contact method and full email for every link. |
| 15 | Exact business name/address including suite or unit/phone/website; inspect GBP, Yelp, Bing Places, Apple Maps, Facebook, BBB, Angi, HomeAdvisor, Thumbtack, Houzz, Yellow Pages, Manta, Foursquare, Superpages, Citysearch and industry directories; columns: listing exists, exact name/address/phone, website URL, duplicate listings, rating/review count if applicable; red inconsistency flags; prioritized damage/fix instructions/missing directories/monthly maintenance. |
| 16 | SEMrush niche + service-area keywords at ≥20 searches/month; Stage 1 problem-unaware, Stage 2 problem-aware, Stage 3 solution-aware, Stage 4 ready-to-hire; per stage keyword count/combined volume/average KD/top ten by volume; route 4→service pages + GBP, 3→comparison + FAQ, 2→educational blog→service pages, 1→problem-identification; five Stage-4 targets for 90 days plus exact actions. |

The preserved rationale claims 2–4 contextual links/month beat 20 random directory submissions, inconsistent NAP suppresses rankings and corrections can improve them within 30 days, and ready-to-hire terms convert at 5–10× the rate. Those remain attributed claims. This domain-level prompt 14 must not be conflated with the later public 22-prompt page-level Exact URL / one-link-per-domain / DR-tier audit in [[claude-cowork-seo-advanced-audits]]. ^[raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]

## Verbatim source section — prompts 14–16

The upstream quotation/Markdown order is tangled in prompts 14, 16. The byte-derived excerpt below deliberately retains that order, broken links, spacing and quotation boundaries; the table above explains the task without replacing or silently repairing its canonical prompt.

~~~text
## PART 3: BACKLINKS + AUTHORITY (prompts 14-16)

14. competitor backlink audit

backlinks are trust transfer. you don't need hundreds. you need the right ones. this prompt finds exactly where your competitors are getting their authority from.

> ].   Then find my link opportunities by identifying domains that link to ALL 3 competitors but not to me because those are highest priority, domains that link to 2 competitors but not to me because those are medium priority, and domains that link to 1 competitor but not to me because those are worth reviewing.   For each high-priority link opportunity tell me the domain name and URL, the DR of the domain, what type of site it is (directory/news/blog/association/sponsor), how my competitor earned the link (guest post/sponsorship/citation/PR mention), my realistic chance of getting a similar link (high/medium/low), and the exact outreach strategy I should use.   Then build me a prioritized 90-day link building plan where month 1 covers the 5 easiest links to get such as directories and citations and local associations, month 2 covers 5 medium-effort links such as local news and sponsor opportunities and guest posts, and month 3 covers the 5 authority links worth pursuing such as industry publications and local government and universities. For every single link include the contact method and write me the full outreach email I can send immediately.""Open Chrome and log into my Ahrefs account at[ahrefs.com](https://ahrefs.com/). Go to Site Explorer and enter [[competitor1.com](https://competitor1.com/)] first. Export their full backlink profile filtered to dofollow links only, DR of linking domain 20 or higher, traffic of linking domain 100 or more monthly visits, and link type not sitewide so no footer or sidebar links. Repeat this for [[competitor2.com](https://competitor2.com/)] and [[competitor3.com](https://competitor3.com/)

why this matters: 2-4 real contextual links per month compounds faster than 20 random directory submissions. this audit removes all the guesswork - you know exactly who to target, exactly how they earned the link, and exactly what to say when you reach out.

15. local citation audit

citations are how Google verifies your business is real. inconsistent NAP data across directories is one of the most common local SEO killers and most businesses have no idea how many wrong citations are actively working against them.

> "My business information is: Name: [exact business name], Address: [exact address including suite or unit if applicable], Phone: [phone number], Website: [URL]. Open Chrome and search for my business name across these platforms one by one:   Google Business Profile, Yelp, Bing Places, Apple Maps, Facebook, BBB, Angi, HomeAdvisor, Thumbtack, Houzz, Yellow Pages, Manta, Foursquare, Superpages, Citysearch, and any industry-specific directories for [your industry]. For each platform record whether my listing exists, the business name as listed (exact), the address as listed (exact), the phone number as listed (exact), the website URL as listed, whether there are duplicate listings, and the star rating and review count if applicable.   Create a spreadsheet with all findings and flag every inconsistency in red. Then give me a priority fix list showing which inconsistencies are most damaging to local rankings, step-by-step instructions for correcting each one, a list of high-value directories where I have no listing at all and should create one immediately, and a monthly citation maintenance checklist so this problem never comes back."

why this matters: Google cross-references your business information across hundreds of sources. if your phone number is listed differently on Yelp than on Google, it creates a trust signal conflict that suppresses your rankings. fixing citations is one of the few SEO tasks where you can see real ranking improvements within 30 days of making the changes.

16. local search intent mapping

most businesses optimise for the wrong keywords. they chase high-volume awareness terms and ignore the low-volume, high-intent searches that actually generate calls. this prompt maps your entire keyword universe to the buyer journey stage and tells you exactly which ones to prioritise.

> .   Pull all keywords in my niche for my service area with a search volume of 20 or more per month. Then categorise every keyword into one of four stages: Stage 1 is problem-unaware where someone has a problem but doesn't know what it's called yet (e.g. 'water coming through ceiling' or 'AC making weird noise'), Stage 2 is problem-aware where they know the problem but are researching solutions (e.g. 'how to fix a leaking roof' or 'why is my AC not cooling'), Stage 3 is solution-aware where they're comparing options and providers (e.g. 'plumber vs DIY pipe repair' or 'how to choose an HVAC company'), and Stage 4 is ready to hire where they want to book someone now (e.g. 'emergency plumber [city]' or 'HVAC repair near me').   For each stage tell me: the total number of keywords, the combined monthly search volume, the average keyword difficulty, and the top 10 keywords by search volume. Then build me a content and SEO strategy for each stage: Stage 4 keywords go on service pages and GBP because that's where the money is, Stage 3 keywords go on comparison and FAQ pages, Stage 2 keywords go on educational blog content that funnels to service pages, and Stage 1 keywords go on problem-identification content that builds early trust. Finally tell me which 5 keywords from Stage 4 I should rank for within the next 90 days and exactly what I need to do to rank for each one.""I want to map my target keywords to the buyer journey so I know which ones to prioritise for immediate revenue vs long-term traffic. My business is [business type] in [city] and my core services are [service1], [service2], [service3]. Open Chrome and log into SEMrush at[semrush.com](https://semrush.com/)

why this matters: most businesses spend all their SEO budget on Stage 2 keywords that generate traffic but not calls. Stage 4 keywords have lower volume but they convert at 5-10x the rate. this prompt shows you exactly where your SEO effort should be going and stops you from wasting time on keywords that never turn into revenue.
~~~

## Related

- [[claude-cowork-seo-system]] — business context and exact 12-week execution plan.
- [[claude-cowork-seo-system-prompt-library]] — earlier Claude/Cowork prompt cards; do not overwrite their runtime-specific context.
- [[browser-agent-local-seo-gbp]] — adjacent source-specific audit mechanics.
- [[browser-agents]] — browser-operator interface boundary.
