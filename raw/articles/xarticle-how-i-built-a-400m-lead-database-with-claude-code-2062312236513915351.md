---
source_url: https://x.com/levikmunneke/status/2062312236513915351
ingested: 2026-06-11
sha256: 04ab6cdffba8856d74c423304ca716509ae593ef2c7e93b0541c648d1473f109
---
---
title: "how i built a 400M lead database with Claude Code"
source: "x-bookmarks"
tweet_id: "2062312236513915351"
tweet_url: "https://x.com/levikmunneke/status/2062312236513915351"
author_name: "Levi Munneke"
author_handle: "@levikmunneke"
tweet_date: "Wed Jun 03 23:15:27 +0000 2026"
bookmark_date: "2026-06-03"
content_type: "x_article"
character_count: 7209
retweet_count: 14
like_count: 218
---

# how i built a 400M lead database with Claude Code

how i built a 400M lead database with Claude Code

The lead-gen industry runs on maybe five sources. Sales Navigator, Apollo, ZoomInfo, Crunchbase, and whichever aggregator is hot this quarter. Everyone is fishing the same lake. There are forty other lakes.

Here's where the 400M untapped leads actually lives:

Regulatory. Every regulated trade (doctors, lawyers, contractors, real estate agents, cosmetologists, financial advisors, accountants) has to register with a state body. That body publishes the list. SAM.gov for federal contractors. State business registries for every LLC formed since the Carter administration. Court filings. FCC and FDA databases. The government has been doing your scraping for you for forty years.

Non-profit and institutional. IRS 990s name the board members and officers of every nonprofit in the US. Chambers of commerce publish member rosters. Trade associations publish directories. Universities publish faculty and staff. Alumni associations publish themselves.

Industry-specific platforms. Houzz for contractors. Avvo for lawyers. Healthgrades and ZocDoc for doctors. Yelp Service for trades. These exist because the listed party wants to be found. The directory is built to get them inbound. You scraping the directory is exactly what it's designed to enable.

Event and public-presence. Conference speakers, trade show exhibitor lists, podcast guests, Substack writers, YouTube channels with public business pages. Anyone who showed up to be visible is, by their own choice, visible.

The pattern: these people are listed because of what they do, not because they signed up to be in a CRM. That's the difference.

Why it works

Intent is baked in. Apollo gives you "Plumbing Manager at Joe's Plumbing." You still have to verify the title, the company, whether they're still there, whether they actually make plumbing decisions. A state contractor license tells you, with the government's stamp on it, that this person is a licensed plumber in this state with this license number that is currently active. The verification step is already done. By the state.

Less competition in the inbox. Your competitors are all renting the same Apollo seats and emailing the same 50M contacts. Reply rate on a list everyone bought is whatever's left after the previous twenty senders that week. A list you built from a licensing board, nobody else has. First-touch reply rates on custom lists routinely run 3-5x what they do on Apollo-sourced ones, because the inbox isn't already on fire.

Cheaper past about 50k leads. ZoomInfo seats run $15k to $50k a year. Apollo is cheaper but the credit limits bite at scale. A custom scraper runs on a $40/month VPS, a few hundred dollars of residential proxies, and your time. The crossover is around 50k leads. Under that, pay for Apollo. Above it, scraping is meaningfully cheaper and you own the data.

Deliverability is better. Aggregator emails get sold to thousands of senders. By the time you buy a list, those addresses have been through everyone: spam traps, aggressive bounce filters, personal blocklists. Addresses scraped from public directories haven't been through that meat grinder. They're often the listed party's "contact me to hire me" email, which by definition exists to receive cold outreach.

The method

Discovery. Search for verticals where membership or licensing is mandatory. "[state] [profession] licensing lookup." "[industry] association members." "[trade] directory." Most directories don't market themselves as lead sources, which is why they're not in everyone's pipeline yet. If a profession requires a license, that license is public somewhere.

Extraction. Easy sites are paginated, predictable URLs, clean HTML. Straight requests + BeautifulSoup. Hard sites are JS-rendered, captcha'd, IP-rate-limited. Playwright, rotating residential proxies, sensible delays. Don't hammer. You're not trying to take the site down; you're trying to read what they already publish.

Normalization. The same person appears across five sources with five spellings of their name. Same business, four different addresses. Match on name + location + business + email domain. Dedupe aggressively. A 400M database with 50% duplicates is a 200M database wasting your sending budget pretending to be twice as big.

Enrichment. A directory listing gets you maybe 60% of a usable lead. Combine listings across sources. Verify emails (NeverBounce, MillionVerifier). Append firmographic data from public sources: domain age, tech stack, hiring signals. The lead gets better with every join.

Compliance. CAN-SPAM covers most US B2B cold email if you include an unsubscribe link, a physical address, and don't lie in the subject. GDPR is stricter. For EU contacts you need a legitimate interest basis and clean opt-out plumbing. Beyond that: scrape public data, don't bypass paywalls or break ToS that creates contractual liability, don't sell PII you don't own. Move on.

The numbers, and how Claude Code does the work

The 400M breaks down roughly like this:

- ~180M from state professional licensing boards across regulated trades

- ~90M from IRS 990s and nonprofit data

- ~70M from industry directories, trade associations, and chambers

- ~40M from specialty platforms (Healthgrades, Houzz, Avvo, ZocDoc, and the rest)

- ~20M from conference, event, and podcast public-presence sources

The case study: private clinics. Apollo will give you names and titles at clinics, fine. But state medical boards give you every licensed practitioner in the state, with specialty, license status, and disciplinary history. Cross-reference with Healthgrades for patient-facing emails. Cross-reference with state business registries for the clinic ownership entity. You end up with a list Apollo literally cannot produce, because the data only exists across three public sources and Apollo only buys from aggregators that didn't scrape any of them.

Now, how Claude Code actually does it.

Open a terminal, cd into a project folder, point Claude Code at the directory page you want, and say "build me a scraper for this site that handles pagination and outputs to CSV." It inspects the page, writes a Playwright or requests+BS4 scraper depending on what the page needs, runs it, sees the output, and fixes the parsing where it broke. The loop is fast because Claude Code can actually run the scraper, see the broken output, and iterate without you in the middle.

Then a second pass for normalization and dedup. Have it build the schema, write the matching logic, run it against your raw data. Then a third pass to wire email verification calls in batches against whichever API you use.

The real unlock isn't writing the first scraper. The real unlock is that directory HTML changes. Constantly. A scraper that worked Tuesday breaks Wednesday because the site shipped a redesign. Claude Code rewrites a broken scraper in about ninety seconds. That's the difference between "I built a scraper once" and "I run scrapers across 80 sources continuously." Maintenance was always the choke point. It isn't anymore.

-

if you want to a system like this built out for you shoot me a message. or just book a call -> cal.com/leviwelch/30min
