---
title: "turning codex into a 260 million lead database"
author: "Levi Munneke"
username: "@levikmunneke"
created: "2026-04-30"
source: "https://x.com/levikmunneke/status/2049704890780524901"
type: "x_article"
tags: []
---

turning codex into a 260 million lead database

everyone is still buying $99/mo apollo seats and scraping the same 50,000 fatigued contacts.

meanwhile there's 260+ million business listings sitting completely untouched.

here's how to use codex to build an entire scraping pipeline yourself in one afternoon. for less than the cost of a single apollo seat per month.

THE PROBLEM WITH HOW EVERYONE IS DOING IT

apollo. lusha. zoominfo. seamless.

every agency owner buying outbound data is buying the exact same data as every other agency owner.

the people getting bombarded never reply.

the people who would reply are nowhere on those platforms.

local business owners aren't on apollo. the dentist with no website. the contractor whose google profile hasn't been updated since 2021. the gym owner with 200 reviews and a $40 wordpress site that loads in 9 seconds. those people are wide open. they are getting zero outbound. and they have real, visible, scrapeable problems you can solve.

google maps has all of them.

WHY CODEX CHANGES THE MATH

a year ago you needed a developer for this. you'd post on upwork, get quoted $1,500, get a half-broken script three weeks later, then pay another $400 every time the api changed.

codex eliminates that entire chain.

you open the cli. you describe what you want. it writes the code, runs it, debugs the errors itself, fixes the rate limit issues, handles the retries, and spits out a clean csv.

you don't need to know python. you need to know how to describe what you want in plain english and how to read the output.

that's it.

the cost difference is absurd. apollo at $99/mo gets you data everyone else has. codex plus a $5 rapidapi key gets you data nobody has touched.

THE STACK

three pieces. that's the whole thing.

1. codex (openai's coding agent in the cli)

2. a rapidapi key for a google maps places endpoint - $5-15/mo for 10,000+ requests

3. a python environment on your laptop or a $7/mo vps

total monthly cost: under $25.

output: 10,000s enriched local leads per day, in a format ready to drop into instantly or smartlead.

THE FIRST PROMPT - THE GOOGLE MAPS SCRAPER

open codex in your terminal. paste this:

"build me a python script that uses the rapidapi 'local business data' endpoint to pull every business matching a search query in a given city. accept three command line arguments: query (like 'roofing contractor'), city (like 'dallas tx'), and max_results. for each business return: business name, full address, phone, website url, google rating, review count, business category, latitude, longitude, and the google place id. output a clean csv with proper headers. handle rate limiting with exponential backoff. log progress every 50 businesses. skip duplicates by place id."

codex will write the script. it'll ask which rapidapi endpoint you want - tell it "local business data" or whichever places api you grabbed a key for. it'll write the requests, handle the json parsing, build the csv writer, and run a test pull.

first run, you'll get something like 200-500 businesses for that query in that city. clean. structured. ready to enrich.

run the same script across 5 service categories and 10 cities and you have 25,000 raw leads in an hour or two.

THE SECOND PROMPT - THE WEBSITE ENRICHER

raw maps data isn't enough. you need contact info and personalisation hooks. that means crawling each business website.

paste this into codex next:

"now build a second python script that takes the csv from the maps scraper as input. for each row that has a website url, crawl up to 5 pages of that site (homepage, contact, about, team, services). extract: every email address found, every phone number, the page title and meta description, whether the site has https, page load speed in seconds, whether the site is mobile responsive (check viewport meta tag), the year copyright if visible, and whether they have any of these signals: 'book online', 'free quote', 'request appointment', 'schedule consultation'. flag businesses where the website returned a 404, took longer than 5 seconds to load, or had no ssl. output an enriched csv with all original maps data plus these new fields."

run that script overnight on your raw csv. by morning you have a fully enriched lead list.

every row now tells you:

- the owner's email (or a contact form if no email is exposed)

- whether their site is fast or broken

- whether they have basic conversion infrastructure

- whether their copyright year is current

- a clear, specific pain point you can lead with

THE THIRD PROMPT - THE SIGNAL EXTRACTOR

this is the part nobody is doing. and it's where the replies actually come from.

paste this:

"take the enriched csv and add a 'signal' column. for each business, generate one specific, observable problem based on their data. examples: 'no website attached to google profile', 'site loads in 8.4 seconds, killing mobile conversions', 'only 11 google reviews, ranked 9th in map pack', 'no online booking despite being a service business', 'copyright year is 2019 - site likely abandoned', 'no https - browsers flag the site as not secure', 'no meta description - google fills it in for them with random text'. write the signal in plain language, the way you'd describe it to the owner over coffee."

now your csv isn't a lead list. it's a list of leads with the exact opening line of your cold email already written, based on something the business owner can verify in 10 seconds by looking at their own profile.

THE EMAIL THAT WRITES ITSELF

a generic apollo cold email looks like:

"hey john, hope your week is going well. i help dentists like yourself generate more new patient appointments through paid ads."

an email written off your codex pipeline looks like:

"hey john - noticed your google profile doesn't have a website attached, and the place id matches an old wix site that's been down for months. built you a free landing page mockup for [business name] - want me to send it over?"

one of those gets ignored. the other gets a reply.

THE MATH

let's run it.

5 service categories x 10 cities x 500 businesses = 25,000 raw leads.

after enrichment, roughly 60% will have a usable email or contact form. that's 15,000 contactable leads.

at 800 sends per day across 30-40 warmed inboxes (instantly handles this), you cover the entire list in 19 days.

reply rate on hyper-specific, signal-driven cold email runs 3-7% in our experience versus 0.5-1.5% on generic apollo blasts.

3% of 15,000 = 450 replies.

even if only 15% of those are positive, that's 67 booked discovery calls from one weekend of codex work and three weeks of sending.

infrastructure cost for the whole operation: under $400/mo all-in (codex + rapidapi + sending stack + vps).

one closed retainer at $3-5k pays for the year.

THE SETUP - ONE AFTERNOON

hour 1: install codex cli, log in, test it works. hour 2: grab a rapidapi key for a google maps places endpoint. test 10 free requests in postman to confirm the response shape. hour 3: prompt codex to build the maps scraper. test it on one query. confirm csv output looks clean. hour 4: prompt codex to build the website enricher. run it on your test csv. confirm emails are being extracted. hour 5: prompt codex to build the signal extractor. review the signals it generates - tweak the prompt if they're too generic.

next morning: run the full pipeline on your real target list. start sending by friday.

THE PART NOBODY TALKS ABOUT

the actual edge here isn't the scraper. it's the data nobody else has.

every agency owner using apollo is fishing in the same pond. that pond has been over-fished for three years. the businesses on it have been emailed by 200 different people offering the same services with the same templates.

google maps is a pond that has barely been fished at all. and codex just gave you a fishing rod for $25/mo.

the people who deploy this in the next two weeks will have a 12-month head start on the agencies still complaining about apollo reply rates.

if you want the 5-min breakdown of how we run the full gtm engine generating 100+ opportunities per month for our clients...

→ [hiivearts.com/x](https://hiivearts.com/x)
