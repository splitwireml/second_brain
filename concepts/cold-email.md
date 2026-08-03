---
title: Cold Email
created: 2026-05-31
updated: 2026-08-03
type: concept
tags: [b2b, cold-email, lead-gen, marketing, outbound]
sources: [raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md, raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md]
---

# Cold Email

Outbound email to prospects who have not opted in. Primary B2B [[lead-gen]] channel. Key for [[ai-implementation-consulting-12k]], agency client acquisition, and [[monetization]] pipelines.

## 2026-08-03 Seven-Step Distribution Playbook

Michel Lieben's source describes cold email as one rail in a broader distribution system, based on a conversation with Charles Tenot (described as the CEO who grew Lemlist from $15M to $53M ARR) and Erwan (his VP of Growth). Their view comes from a platform seeing 20,000 signups/month; Michel's comes from hundreds of B2B clients operated through ColdIQ. These figures are source-described, not independently verified.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

### 1. Run every campaign on two rails

The first rail is real hyper-personalization: enrich every row, build lists only from people who fit the ICP, and use one campaign per segment instead of one campaign for everyone. A first-name merge tag is not treated as personalization. The second rail is multi-channel: email supplies reach, while a LinkedIn touch from a real profile supplies recognition and trust when a prospect checks the sender beside competitors. The source reports that multi-channel clients stay 2.5x longer than email-only clients and recommends attaching a LinkedIn touch to every email sequence; this retention figure is source-described.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

### 2. Treat LinkedIn as an asset and mine engagement

A real LinkedIn audience is treated as an asset that fake accounts cannot safely replace. Weekly, export first-degree connections who engaged with posts, match them against the ICP, and call or reach out using the post they touched as the opener. Erwan's test reportedly reached roughly 95% answers and conversations on the phone, not 95% inbox replies; even wrong-fit conversations produced referrals and market intelligence. Tracking which topics each person engages with supplies a second personalization layer: recurring AI-in-outbound or deliverability engagement suggests different opening language.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

### 3. Split the work between AI and humans

AI handles scraping, enrichment, list building, ICP scoring, intent detection, and campaign analytics—the work that can run unattended. Humans keep the words: the source says strong human writers still outperform AI cold-email copy, framing AI as statistical and creativity as the opposite of statistics. The operating instruction is to automate everything before the message exists, then give the human twice the former writing time for the message itself.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

### 4. Build signals nobody else has

Common signals such as fundraising, new roles, and hiring are described as saturated. The source's examples of reverse-engineered signals are: a target company's email landing in the team's spam folder; a decision maker connecting with competitor reps; a sudden Meta ad-spend increase; a web-traffic spike relevant to a bot-detection product; and missing DMARC on the domain. [[lemlist]] is described as merging the team's spam folders into one list for outreach. The method is to call the last 20 customers, read sales-call transcripts for repeated sentences, and find the public data point that exposes a trigger named by seven of ten prospects. ColdIQ's own example is the spam pattern: AI-post engagement did not explain booked calls, but the repeated spam problem did.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

### 5. Write before you scale

Hand-write 35–50 messages before automating. Manual sends reveal which data points mark a responding lead, which angle earns a response, and which lines feel dead; only after a pattern proves itself across 50 manual sends should it scale to a thousand. The source also gives a free self-test: send the outreach email to yourself first and ask whether you would reply. It describes a response curve where moving from an 8 to a 9 can potentially multiply replies a hundredfold, while a 7 may buy nearly the same silence as a 6; this is an estimate, not a measured law.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

For tier-one accounts, Tom Greenwood reportedly records a personal website-review video for each prospect, spending 15–20 minutes pointing to places where the site loses money. The source reports around a 30% reply rate and meetings that convert because the prospect has a concrete reason to attend; both are source claims.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

### 6. Earn the open with a pattern interrupt

The source compares outbound to street advertising: most messages are unseen, so the current job is to stop the scroll. Examples are a phone-data provider putting the prospect's own number beside “Is this you?” and “Is this your email?” with a screenshot of the prospect's message in a spam folder. Both demonstrate instead of claim. Lowercase subjects, voice notes, and personalized images (the tactic Lemlist became known for) are described as temporary patterns that expire when copied. The recommended research loop is to inspect the first 20 cold emails in your own inbox, record their common pattern, and deliberately break it.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

### 7. Close the loop so the engine improves itself

The source says the wiring already exists through MCPs in [[claude-code]]. A meeting recorder supplies what buyers said; a sequencer supplies who replied, on which channel, and at which step; and a CRM supplies what closed and why. The loop is: record calls and transcripts; find persona, objection, and buying-reason patterns; update the next campaign to target the persona and use buyer language; then feed results back into the next send.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

A source-described example found sales operations responding at three times the rate of a broad sales persona, so the next campaign targeted sales ops only. Another play reactivated deals lost six months earlier by quoting the specific missing feature and returning when it had shipped. At ColdIQ, GTM engineers reportedly prompt a whole campaign build, leave for breakfast, and return about 30 minutes later to review a draft with the list uploaded and every touchpoint placed; around 1,500 companies reportedly run Lemlist through Claude each month. The exact prompt, model/version, API, CRM/sequencer interface, list format, and touchpoint configuration are not specified.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

## Closing Guardrails

The source rejects fake LinkedIn accounts because they are banned quickly and provide no proof when a prospect checks the profile. It also rejects building custom sending infrastructure merely because AI can code: the claimed failure chain is a vibe-coded sender that lands in spam, followed by secondary mailboxes, warmup logic, rotation, and a Frankenstein system that a $100/month tool already outperforms. Lemlist's warmup layer is said to watch 50,000 domains and correct deliverability shifts within 24 hours. The source's recommendation is to keep custom software in internal workflows and rent revenue-critical sending infrastructure; these capabilities, costs, and timings remain source-described.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

Finally, do not scale something that never worked small: automation multiplies a guess. The source provides no model/version, shell command, configuration file/value, parameter schema, verbatim prompt, file format/path, or implementation-level handoff beyond the named MCP/Claude Code, recorder, sequencer, CRM, and campaign artifacts. Those evidence boundaries are preserved rather than filled in.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

## 2026-08-03 Qualification-First List and Offer Gate

Brannon Hogue's local source places list qualification before cold-email execution: start with 5,000 emails, validate them twice while excluding catch-alls, and reduce the list to roughly 2,900 valid emails. Research the prospects with “cheap ai search”; the source says Gemini or any research AI can identify the relevant online signals.^[raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md]

The source then scores leads into tiers 1, 2, and 3, removes tier 3, and reports roughly 1,200 tier-1/tier-2 leads. For a website-builder offer, its example qualification signals are a poor website, a growing staff count, and active growth-minded hiring.^[raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md]

The offer is a second gate: give away a solution to a main business problem completely for free rather than offering a generic “free audit,” stay selective about freeloaders, and use the first solved problem to reveal a second problem that can become paid work. Lead scoring also protects the free-service budget by excluding prospects with no budget.^[raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md]

The local source does not specify the validation service, catch-all method, research interface/API, model version, tier rubric, prompts, offer, send cadence, infrastructure, or conversion measurements; its counts and outcomes remain source-described rather than independently verified.^[raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md]

## Related Concepts

- [[outbound]] — broader multichannel B2B outreach system
- [[linkedin-growth]] — LinkedIn trust, engagement, and conversion layer
- [[lemlist]] — named sequencer and deliverability platform in the source
- [[coldiq]] — source operator and GTM context
- [[michel-lieben]] — source author
- [[brannon-hogue]] — source author of the qualification-first list and free-offer gate
- [[lead-gen]] — cold email as lead generation
- [[b2b]] — B2B cold email context
- [[monetization]] — revenue from cold email campaigns
