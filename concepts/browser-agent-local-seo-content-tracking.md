---
title: "Browser-Agent Local SEO: Content and Tracking"
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [seo, local-seo, browser-agents, browser-automation, prompt-engineering, workflow]
sources: [raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]
---

# Browser-Agent Local SEO: Content and Tracking

## Scope and provenance

Technical sub-concept of [[claude-cowork-seo-system]], preserving Sarvesh Shrivastava ( [[bloggersarvesh]] )'s August 19, 2026 “Grok Bot” variant. Ingested October 7 from a complete local export. This is a source-described workflow and exact prompt record, not an executed audit or independently verified product capability. ^[raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]

## Transferable mechanism

Connect competitor content gaps, entity-presence checks and posting-history evidence to a monthly first-party outcome report. Source-named interfaces are Chrome, SEMrush Content Gap, Google Search, Wikidata, Google's Rich Results Test, Google Search Console, GBP insights and Google Analytics 4. The requests describe browser operations and output contracts; they do not prove “Grok Bot” model/API tool access, knowledge-panel creation, platform metric availability or SEO effectiveness. ^[raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]

| Prompt | Evidence and output contract |
|---:|---|
| 17 | SEMrush Content Gap with own + three domains; competitor-ranking content absent from own site; 50–500 monthly searches, question words how/why/what/when/is/can/does, service-solved problems; top 20 in problem-awareness / solution-comparison / local-service buckets; SEO page title, slug, 200-word brief with target + secondary keywords, questions, recommended word count, internal links and bottom CTA; source prioritizes problem-awareness content. |
| 18 | Inputs exact name/address/phone/website/GBP/founded year/owner/industry; Google searches `[business name] [city]` and `[owner name] [business name]`; Wikidata business-name search; Rich Results Test on website URL; quoted brand search across Google with NAP consistency; requested complete LocalBusiness JSON-LD ready to paste, eligible Wikipedia / Crunchbase / LinkedIn company / industry association presence list, exact anchors/brand mentions and knowledge-panel instructions. The source contains a prompt requesting code, not actual generated JSON-LD; none is fabricated here. |
| 19 | All competitor posting history as far as visible; one row/post: exact date/time, weekday, offer/update/event/product type, words, image, CTA/button text, topic/service, neighborhood/city, price/offer, hashtags/formatting; analyze day/time/type/season/month frequency and exploitable gaps; market-specific days/times/types/topic mix; first four weeks full post copy. This is history reconstruction, distinct from prompt 5's 90-day summary and eight-week calendar. |
| 20 | GSC + GBP insights + GA4 if available; last 30 days versus previous 30 days. GSC: clicks/impressions/CTR/average position and changes; top ten by clicks/improvement/drop; pages winning/losing clicks. GBP: views, branded-vs-discovery queries, calls, directions, website clicks, photo views, review-count change. Analytics: organic sessions/conversion rate, landing pages by sessions and top-page bounce rate. One-page five-minute shareable report: three wins, three problems, one next-month action and GBP calls up/down. |

Keep the source's own prioritization tension: prompt 16 says Stage-4 ready-to-hire work should lead immediate revenue, while prompt 17 explicitly prioritizes problem-awareness content. The article schedules intent mapping in weeks 7–8 and content gaps in weeks 9–10; it does not resolve every budget allocation between them. The full literal week 1–12 plan is in [[claude-cowork-seo-system]]. ^[raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]

Knowledge-graph trust, higher local rankings, AI Overview inclusion, algorithm resilience, posting-time effects and “already proven” competitor patterns remain author assertions. The reporting prompt requests metrics; it does not establish their accessibility or specify call/revenue attribution, analytics event configuration or a dashboard implementation. ^[raw/articles/xarticle-top-20-grok-bot-prompts-for-seo-the-only-stack-you-2090071557590900974.md]

## Verbatim source section — prompts 17–20

The upstream quotation/Markdown order is tangled in prompts 17, 18, 20. The byte-derived excerpt below deliberately retains that order, broken links, spacing and quotation boundaries; the table above explains the task without replacing or silently repairing its canonical prompt.

~~~text
## PART 4: CONTENT + TRACKING (prompts 17-20)

17. content gap analysis

your competitors are ranking for searches your customers are doing right now. this prompt finds every piece of content you're missing and tells you exactly what to write.

> ].   Filter results to find keywords where competitors have ranking content but I have nothing, then filter further to keywords with 50-500 monthly searches which is the local content sweet spot, keywords that contain question words (how, why, what, when, is, can, does), and keywords that relate to problems my service solves.   For the top 20 content gap keywords, organise them into 3 categories: problem-awareness content where searches indicate someone has a problem but doesn't know the solution yet such as 'why is my AC not cooling', solution-comparison content where searches indicate someone is evaluating options such as 'repair vs replace water heater', and local service content where searches indicate someone is ready to hire such as 'emergency plumber [city] cost'.   For each of the top 20 keywords write a suggested page title that is SEO optimised, a suggested URL slug, and a 200-word content brief that includes the target keyword, secondary keywords to include, main questions to answer, word count recommendation, internal links to add, and the CTA at the bottom of the page. Prioritize problem-awareness content first because it does the most work for local businesses by answering objections before the phone call.""Open Chrome and log into SEMrush at[semrush.com](https://semrush.com/). Use the Content Gap tool and enter my domain [[yourdomain.com](https://yourdomain.com/)] vs competitors [[competitor1.com](https://competitor1.com/)], [[competitor2.com](https://competitor2.com/)], [[competitor3.com](https://competitor3.com/)

why this matters: content that ranks for problem-awareness searches turns your website into a 24/7 sales tool. someone searching 'why is my furnace making noise' is one step away from calling a HVAC company.   if your page answers that question and links to your service page, you get the call. your competitor who doesn't have that page doesn't.

18. entity optimisation

this is the most advanced prompt in this entire article. most local SEOs don't even know this is a lever. Google doesn't just rank websites - it ranks entities. your business needs to exist as a verified entity in Google's knowledge graph to unlock the highest level of local trust signals. this prompt builds that entity.

> and entering my website URL and telling me what schema is currently implemented and what's missing. Then check my brand consistency by searching my business name in quotes across Google and noting every place my business information appears and whether the name, address, and phone are consistent.   Then build me a complete entity optimisation plan that includes: the exact LocalBusiness schema markup code I need to add to my homepage (write the complete JSON-LD code ready to paste), a list of authoritative sites where I need to create or claim a presence to build entity signals (include Wikipedia if eligible, Crunchbase, LinkedIn company page, industry associations), the exact anchor text and brand mentions I need to build across the web to strengthen my entity, and instructions for how to get my knowledge panel to appear if it doesn't already exist. This is the SEO work that compounds for years and almost no local business is doing it.""I want to build and strengthen my business entity in Google's knowledge graph to improve local rankings and potentially trigger a knowledge panel. My business details are: Name: [exact business name], Address: [full address], Phone: [phone number], Website: [URL], GBP: [GBP URL], Founded: [year], Owner name: [your name], Industry: [industry].   Open Chrome and do the following research and build-out. First check if my business has a Google Knowledge Panel by searching '[business name] [city]' and '[owner name] [business name]' and tell me what appears. Then check if my business exists on Wikidata by searching[wikidata.org](https://wikidata.org/)for my business name and report what you find. Then audit my schema markup by going to[search.google.com/test/rich-results](https://search.google.com/test/rich-results)

why this matters: Google's understanding of your business as a real-world entity affects how much it trusts your GBP, your website, and your reviews. businesses with strong entity signals rank higher, get more featured in AI overviews, and are more resilient to algorithm updates. this is where local SEO is going - and building it now while nobody else is doing it is the biggest competitive advantage available.

19. competitor GBP posting pattern analysis

everyone knows posting on GBP matters. nobody knows when to post, what format performs, or which topics actually drive map pack visibility. this prompt reverse-engineers everything your top competitors have figured out about GBP posting - the timing, the format, the seasonal patterns - and builds you a posting strategy that works from day one instead of month six.

> "Open Chrome and go to the GBP listings for these competitors: [URL1], [URL2], [URL3]. For each competitor I want a complete forensic analysis of their GBP posting history going back as far as visible. For each post extract: the exact date and time it was posted, the day of the week, the post type (offer/update/event/product), the word count, whether it includes an image, whether it includes a CTA button and what the CTA says, the topic and service mentioned, whether it mentions a specific neighborhood or city, whether it includes a price or offer, and any hashtags or special formatting used.   Put all of this into a spreadsheet with one row per post. Then analyze the patterns and tell me: which days of the week they post most frequently, whether there is a time-of-day pattern, which post types they use most, which topics appear to be seasonal, which months have the highest posting frequency, and whether there are any gaps in their posting schedule I can exploit by posting consistently when they don't.   Then build me a posting strategy that is specifically designed to beat these competitors based on what the data shows actually works in my market - not generic advice, but a posting cadence and format built entirely from reverse-engineering what my specific competitors are doing. Include the optimal days, times, post types, and topic mix for my market. Write the first 4 weeks of posts in full using this strategy."

why this matters: GBP posting is not just about frequency. it's about pattern.   Google notices when businesses post consistently, at what times, on which days, and with what type of content. reverse-engineering your competitors' posting patterns removes all the guesswork and gives you a strategy that's already proven to work in your specific market.

20. monthly SEO performance report

most business owners track the wrong things. vanity metrics like total traffic or domain rating don't tell you if SEO is making you money. this prompt builds a monthly report that only tracks what matters.

> Pull data for the last 30 days vs the previous 30 days for every metric below.   From Google Search Console I need: total clicks from organic search and the change vs previous month, total impressions and the change, average CTR and the change, average position and the change, top 10 keywords by clicks this month, top 10 keywords that improved in position this month, top 10 keywords that dropped in position this month, pages that gained the most clicks, and pages that lost the most clicks.   From Google Business Profile I need: total profile views, total search queries broken into branded vs discovery, calls from GBP, direction requests, website clicks from GBP, photo views, and review count change. From Google Analytics if available I need: organic traffic sessions, organic traffic conversion rate, top organic landing pages by sessions, and bounce rate on top pages.   Then build me a one-page monthly SEO report with 3 wins from this month, 3 problems that need addressing, the single most important action for next month, and a note on whether calls from GBP went up or down. I want this in a format I can read in 5 minutes and share with anyone on my team."the prompt: "Open Chrome and access these three tools: Google Search Console for [[yourdomain.com](https://yourdomain.com/)], Google Business Profile insights for my listing at [GBP URL], and Google Analytics 4 for [[yourdomain.com](https://yourdomain.com/)

why this matters: if you can't measure it you can't manage it. but measuring the wrong things is worse than measuring nothing. calls and revenue from organic are the only numbers that actually matter. this report keeps you focused on the metrics that connect directly to your bank account and stops you from celebrating traffic increases that never turn into customers.
~~~

## Related

- [[claude-cowork-seo-system]] — business context and exact 12-week execution plan.
- [[claude-cowork-seo-system-prompt-library]] — earlier Claude/Cowork prompt cards; do not overwrite their runtime-specific context.
- [[browser-agent-local-seo-gbp]] — adjacent source-specific audit mechanics.
- [[browser-agents]] — browser-operator interface boundary.
