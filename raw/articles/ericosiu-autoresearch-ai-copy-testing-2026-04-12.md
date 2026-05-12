---
updated: 2026-04-17
title: How I Test My Landing Pages 105 Times Before Anyone Sees Them
source: https://x.com/ericosiu/status/2042637743348457767
type: post
author: ericosiu
username: '@ericosiu'
---

# How I Test My Landing Pages 105 Times Before Anyone Sees Them

**Source:** https://x.com/ericosiu/status/2042637743348457767
**Author:** @ericosiu
**Date:** 2026-04-12
**Type:** Thread / Long-form tweet

---

How I test my landing pages 105 times before anyone sees them.

I tested 105 copy variants for a landing page in 8 minutes. Without a single visitor hitting the page.

The page scored 62/100 before. 87/100 after. Then I deployed it and let real traffic validate which version actually converts.

Here's the full system.

---

Karpathy pushed a 630-line Python script to GitHub in March and went to sleep. By morning, it had run 50 ML experiments autonomously. No human touched it.

The pattern: propose a change, run the experiment, measure the result, decide what to try next. Repeat until we converge on something better.

I stole this pattern for business.

Not for training neural networks. For landing pages, email sequences, ad copy, and form pages. Content that converts or doesn't. And I realized the bottleneck was never the testing. It was the waiting.

---

Traditional A/B testing is broken for most businesses.

You write two headlines. You split traffic. You wait 14 days. One wins by 3%. You repeat. At that pace, you test maybe 20 variants per year.

Karpathy's autoresearch tests 50 variants per night.

The difference: autoresearch doesn't need live traffic. It generates its own feedback loop.

```
Traditional A/B Testing:
Variant A ──► Live traffic ──► 14 days
Variant B ──► Live traffic ──► 14 days
│
▼
Winner (maybe)
Total: 2 variants in 14 days

Autoresearch:
10 variants ──► Expert panel ──► 2 min
Top 3 ──► Cross-breed ──► 15 combos
Top 5 ──► Evolve ──► 25 more
│
▼
Winner (scored)
Total: 50+ variants in 8 minutes
```

---

How I test my landing pages 105 times before anyone sees them.

I tested 105 copy variants for a landing page in 8 minutes. Without a single visitor hitting the page.

The page scored 62/100 before. 87/100 after. Then I deployed it and let real traffic validate which version actually converts.

Here's the full system.

---

Karpathy pushed a 630-line Python script to GitHub in March and went to sleep. By morning, it had run 50 ML experiments autonomously. No human touched it.

The pattern: propose a change, run the experiment, measure the result, decide what to try next. Repeat until you converge on something better.

I stole this pattern for business.

Not for training neural networks. For landing pages, email sequences, ad copy, and form pages. Content that converts or doesn't. And I realized the bottleneck was never the testing. It was the waiting.

---

Traditional A/B testing is broken for most businesses.

You write two headlines. You split traffic. You wait 14 days. One wins by 3%. You repeat. At that pace, you test maybe 20 variants per year.

Karpathy's autoresearch tests 50 variants per night.

The difference: autoresearch doesn't need live traffic. It generates its own feedback loop.

```

```
Traditional A/B Testing:
Variant A ──► Live traffic ──► 14 days
Variant B ──► Live traffic ──► 14 days
│
▼
Winner (maybe)
Total: 2 variants in 14 days
Autoresearch:
10 variants ──► Expert panel ──► 2 min
Top 3 ──► Cross-breed ──► 15 combos
Top 5 ──► Evolve ──► 25 more
│
▼
Winner (scored)
Total: 50+ variants in 8 minutes
```

```

---

## Here's how it works for landing pages.

I took our Single Brain landing page. The headline was "Your AI department. Securely deployed." It felt fine. Professional. Clean.

I generated 10 alternative headlines. Then I scored each one with a 5-person simulated expert panel:

1. A CMO at a $50M B2B company ("Would this make me stop scrolling?")

2. A skeptical founder ("Do I believe this?")

3. A conversion rate optimizer ("Is this clear and action-driving?")

4. A senior copywriter ("Is this compelling and differentiated?")

5. An ROI-obsessed CEO ("Would I put this on my site?")

Each expert scores 0-100. Average across all five. The original headline scored 61.6. Dead last out of 10 variants.

The winning headline scored 89.8.

But I didn't stop at headlines. I ran the same loop on the CTA, the subheadline, and the problem section. Then I cross-bred the top 3 winners from each element into 15 combinations and scored those as complete hero sections.

Six rounds. 51 total variants. The page went from 62 to 87 in 8 minutes.

---

Then I ran the same thing on the form page. 54 variants across 7 rounds. Headlines, subtext, value prop bullets, button text, field order, even the thank you page copy.

One finding that surprised me: moving the phone number field from position 3 to position 8 in the form improved the panel's "completion likelihood" score by 27 points. Phone number early creates friction. Phone number late, after someone has already invested in filling out 7 fields, feels like a small addition.

Another finding: "Get Started" as a submit button scored 14 points lower than "Book My Free Strategy Call." The first is vague. The second tells you exactly what happens next.

```

```
Form optimization results:
Element        Before              After             Delta
─────────────────────────────────────────────────────────
Headline       Question-based      Statement + number  +29
Button         "Get Started"       "Book My Strategy   +14
Call"
Field order    Phone at #3         Phone at #8         +27
Thank you      Generic "1-2 days"  "Not a nurture      +25
sequence"
─────────────────────────────────────────────────────────
Overall        57/100              86/100              +29
```

```

The thank you copy went from "Your request has been received and our team will reach out within 1-2 business days" to "Done. Our team reviews every submission personally. Expect a direct reply within 1 business day, not a nurture sequence."

That last line ("not a nurture sequence") is the kind of thing a human writes after years of filling out forms and getting drip campaigns. The panel scored it 25 points higher than the corporate version.

---

Now here's where most people stop. They'd take the autoresearch winner and ship it.

That's a mistake. Simulated panels are smart but they aren't your customers.

This is where autogrowth comes in.

```

```
The full system:
AUTORESEARCH (pre-launch)
│
│  Generate 50+ variants
│  Score with expert panel
│  Evolve winners
│  Ship at 85+ score
│
▼
DEPLOY (live traffic starts)
│
▼
AUTOGROWTH (post-launch)
│
│  Take the winner as control
│  Generate 3-5 mutations
│  Split real traffic
│  Measure actual conversions
│  Promote real winners
│  Kill real losers
│  Repeat weekly
│
▼
COMPOUNDING (forever)
```

```

Autoresearch gets you from 60 to 85 in minutes. Autogrowth gets you from 85 to 95 over weeks with real data. One without the other leaves money on the table.

Without autoresearch, you're A/B testing bad copy against slightly less bad copy for 14 days. Without autogrowth, you're trusting AI opinions over real human behavior.

---

## The five use cases where this matters most:

**1. Landing pages (what I showed above)**

Run autoresearch before any page goes live. Test 50+ headline and CTA combinations in one sitting. Deploy the winner. Let autogrowth refine with real traffic.

**2. Cold email campaigns**

Before sending 800 emails a day, run autoresearch on 10 subject lines and 10 opening lines. Ship the top scorer. Then let autogrowth A/B test 5 variants with real open and reply data over 10 days. Kill losers on day 3.

**3. Ad creative**

Generate 20 headline and description combinations. Panel-score them. Deploy the top 5 to Meta or LinkedIn. Let the ad platform's algorithm pick the real winner with real clicks. The autoresearch step eliminates the obviously bad variants before you spend a dollar.

**4. Content hooks**

Before publishing an X article, run 10 hook variants through the panel. The difference between a hook that scores 65 and one that scores 90 is the difference between 2,000 impressions and 200,000.

**5. Pricing and positioning pages**

Test how different pricing frames land. "$10K/month" vs "less than one junior hire" vs "starting at $333/day." The panel catches framing mistakes that take weeks to discover in the wild.

---

The cost of all of this: about $2 in API calls per run. 8 minutes of compute time. Zero designer time. Zero developer time. Zero waiting for traffic.

The alternative: 2 weeks of split testing with live traffic, during which half your visitors see the losing variant.

The companies that figure this out first get a compounding advantage. Every page, every email, every ad starts at 85+ before a single human sees it. The ones still manually writing two headlines and waiting 14 days are already behind.

Run autoresearch before launch. Run autogrowth after.   

That's the system.

---

If you're a business interested in having AI systems built, you can go to [https://www.singlebrain.com](https://www.singlebrain.com/) or for marketing help, just go to[https://www.singlegrain.com](https://www.singlegrain.com/)

For more like this, level up your marketing with 14,000+ marketers and founders in my Leveling Up newsletter here for free: [https://levelingup.beehiiv.com/subscribe](https://levelingup.beehiiv.com/subscribe)

If you want to join up with our team, [ 'beat AI' first ;) ](https://www.singlegrain.com/apply)