---
title: AI UGC Persona Factory
created: 2026-08-04
updated: 2026-08-04
type: concept
tags: [ai-ugc, ai-persona, content-automation, content-infrastructure, tiktok, marketing, workflow, method, cost-optimization]
sources: [raw/articles/xarticle-no-bs-guide-to-ai-ugc-at-scale-2049286061105483868.md]
related_entity: [[type-kshitij]]
author: [[type-kshitij]]
---

# AI UGC Persona Factory

## Definition

A source-described operating model for turning locked AI personas into a daily organic UGC portfolio for SaaS products. The factory has five coupled layers:

1. **Tokenomics** — choose formats and models from per-asset cost before optimizing visual quality.
2. **Identity** — generate one base avatar and reuse it as the identity anchor.
3. **Audience** — learn the target community's language and extract reusable hook rules.
4. **Distribution** — provision warmed, market-consistent TikTok accounts on physical devices.
5. **Funnel** — optimize for saves, comments, DMs, and shares rather than treating views as the conversion endpoint.

This is distinct from [[ai-ugc-ad-scaling-system]]. That concept centers on paid-ad volume testing and winner promotion; this one centers on organic persona portfolios, identity consistency, and account infrastructure. All economics, view counts, conversion comparisons, and platform-behavior claims below are source-reported unless explicitly marked as corroborated. ^[raw/articles/xarticle-no-bs-guide-to-ai-ugc-at-scale-2049286061105483868.md]

## 1. Tokenomics chooses the format

The source's rule is to make the economics work first: formats are selected from the token budget, not the other way around. It treats 720p as sufficient for UGC-style content and gives these source-described price inputs:

| Component | Source-described use | Claimed unit cost |
|---|---|---:|
| Nano Banana (`gemini-3.1-flash-image-preview`) | Persona and first-frame images | $0.039/image |
| Grok Imagine | Text-to-video from a cold prompt | $0.07/sec |
| Kling 2.6 Standard Motion Control | Image + reference video → motion transfer | $0.07/sec |
| Seedance 2.0 Standard | T2V when many reference assets are needed | $0.3034/sec |
| Veo 3 Standard on fal | Hero shots where cheaper models fail | $0.75/sec |

The source's allocation rule is: use Grok when there is no reference video; use Kling Motion Control when transferring motion onto a locked persona; reserve Seedance for multi-reference or higher-realism cases; use Veo only for shots the cheaper models cannot produce. These are operator recommendations, not an independent benchmark of model quality or current pricing. ^[raw/articles/xarticle-no-bs-guide-to-ai-ugc-at-scale-2049286061105483868.md]

### Slideshow format

Inputs:

- 1–2 Nano Banana persona images: `$0.039–$0.078`
- 4–5 Pinterest images scraped through [[apify]]: approximately `$0.001` in the source's calculation
- Local text compositor using Sharp + Canvas: `$0`

The source calculates `$0.04–$0.08` per slideshow and uses `$0.06` as the average. At one slideshow per day, it estimates approximately `$1.80/month` for one account and `$22/month` for 12 accounts producing 360 slideshows. It recommends putting the AI persona in the first one or two slides so the slideshow reads as a moment from that persona's life rather than as a generic scraped collage. ^[raw/articles/xarticle-no-bs-guide-to-ai-ugc-at-scale-2049286061105483868.md]

### Reaction-video format

Inputs for a 10-second reaction video:

1. Generate the first frame with Nano Banana: `$0.039`.
2. Send the first frame plus a reference video to Kling 2.6 Standard Motion Control: `$0.70` for the source's 10-second calculation.
3. Reuse or scrape the reference video: `$0` in the source's calculation.
4. Add trending TikTok audio: `$0`.

The source calculates approximately `$0.74` per reaction, or `$22/month` for one account posting daily and `$266/month` for 12 accounts posting daily. It says a high-view video is not sufficient by itself: the conversion path should ask viewers to bookmark, comment, enter DMs, or share. One source example contrasts a 12K-view video with 202 bookmarks against a 50K-view video, claiming the former drove more signups because the funnel was better. The example and all performance numbers are source claims. ^[raw/articles/xarticle-no-bs-guide-to-ai-ugc-at-scale-2049286061105483868.md]

## 2. Identity locking

The source's first production artifact is a base avatar image. Its prompt interface exposes these fields:

- `ageDesc`
- `characterName`
- `heritage`
- `faceShape`
- `skinTone` and `skinTexture`
- `hairColor` and `hairStyle`
- `eyeColor`
- `bodyBuild`
- `outfitStyle`
- `makeupStyle`

The fixed prompt also specifies a vertical 9:16 upper-body frame, head-to-belly-button composition, a clean face, a confident/slightly playful expression, warm golden-hour or soft window lighting, and a blurred lifestyle background. Its negative list excludes text, watermarks, logos, extra people, distorted faces, extra fingers, CGI/anime/3D-render styles, masculine features, facial hair, nudity, lower-body framing, blur, phones, mirrors, and reflections. The complete source prompt is preserved verbatim in the raw article. ^[raw/articles/xarticle-no-bs-guide-to-ai-ugc-at-scale-2049286061105483868.md]

The handoff is deliberately fixed:

```text
Base avatar image (never change it)
  → Nano Banana first frame for the reference video
  → first frame + reference video
  → Kling Motion Control output
```

The base image is reused for every new video. The source's reason is identity drift: it says both video models can drift the face when they generate the still themselves. This is a source-described workflow rationale, not an independent consistency evaluation.

## 3. Audience and hook extraction

The source says persona production is not a substitute for knowing the customer. Its research loop is:

1. Doom-scroll TikTok in the target niche until the audience's vocabulary, subjects, formats, and references are familiar.
2. Record the target audience's actual terms; the example uses a high-school audience saying “senioritis,” “ngl,” and “cooked,” and discussing grades, AP exams, prom, and college tuition.
3. Feed successful hooks to [[claude-code]] and ask it to extract the meta-pattern: opening words, sentence rhythm, emotional triggers, curiosity-gap location, and promised-versus-delivered payoff.
4. Save the result as a reusable Claude skill.
5. Generate new hooks, then use a humanizer pass when outputs sound like generic AI copy.

The source's example skill is `gradbro-hooks`:

```markdown
---
name: gradbro-hooks
description: Generate TikTok hooks for college admissions content
  in the voice of @gia_sugars-style AI persona accounts. Use when
  given a topic, video, or screenshot for the first 1-3 seconds of
  a TikTok.
---

# Voice rules

- Open with "ngl", "tbh", "bro" or a direct stat. Never "Are you...?"
- One specific number per hook (GPA, acceptance rate, score)
- Curiosity gap by sentence 2. Promise the payoff, deliver in slide 2
- End with implicit CTA ("save this for later", "DM me your essay")
- Strip every AI tell. No "in today's world", no "let's dive in"

# Negative examples (do NOT write)

- "Want to get into your dream college?" (generic, no specificity)
- "Here are 5 tips that will change your life" (listicle stink)

# Example output for topic "Common App essay opening"

1. "ivy admissions officer told me your essay opens wrong if it
    doesn't do this in line 1"
2. "i wrote my essay 4 times. the version that got me into ucla
    started with a sentence i almost deleted"
3. "your common app essay is mid if you're starting with 'growing
    up i always loved'. save this."
```

For the humanizer pass, the source names [blader/humanizer](https://github.com/blader/humanizer), based on Wikipedia's “Signs of AI writing” guide, and gives this installation handoff:

```bash
git clone https://github.com/blader/humanizer ~/.claude/skills/humanizer
```

## 4. Account infrastructure

The source treats the distribution account as part of the product, not as a final upload destination. Its source-described setup is:

1. Factory-reset the iPhone.
2. Set language and region to the target market.
3. Create a fresh Gmail and one fresh Apple ID per phone.
4. Set the App Store region to the target country.
5. Use a paid dedicated/static residential or mobile IP rather than a shared or rotating pool.
6. Create TikTok accounts with fresh email addresses and warm them before posting.
7. Keep the same regional/device signals across the session and post through the physical device during early account growth.

The article says one phone supported up to three persona accounts in its experience and recommends starting with one, adding a second only after the first is healthy, and adding a third only after that. It proposes a warm-up sequence of no post on day one, natural viewing and a few niche follows; natural comments on day two; and the first post on day three or later. It also says to keep browsing between posts, avoid rapid-fire actions, avoid uploading identical media across accounts, and limit hashtags to roughly four or five.

The source further says to open TikTok only after the VPN is on and close TikTok before disconnecting, to keep the device, region, SIM, and IP signals aligned, and to use the final mobile-app post action rather than treating a scheduled draft as the completed publish step until the account has about 1,000 followers. Its later edits mention spacing out account creation, using new phone numbers, adding recovery email immediately, and creating users aged 18+ because TikTok age cannot later be changed without verification. These fingerprint, shadowban, provider, and warm-up claims are source-reported operating knowledge, not an official TikTok guarantee. ^[raw/articles/xarticle-no-bs-guide-to-ai-ugc-at-scale-2049286061105483868.md]

The related [[tiktok-account-infrastructure]] page records the broader physical-device and trust-signal model; this article adds the persona-account cap, warm-up timing, and final-post handoff.

## 5. Scheduling and publishing

Once the physical device layer exists, the article identifies content transfer and scheduling as the remaining bottlenecks. It names two routes:

- **Self-host:** [[postiz]], described as open source, multi-tenant, and using the official TikTok Content Posting API; the source says approval can take 1–3 weeks and recommends applying early.
- **Managed:** [[ghostfeed]], described as OAuth-connected scheduling with a drag-and-drop calendar, automatic token refresh, exponential-backoff retries, and TikTok API error classification.

The source also names PostBridge and Zernio as alternatives. It recommends sending content to the physical device as draft material but completing the final post action on the device during the early reputation-building phase. The article's product capability, approval-time, and scheduling claims are not independently verified here; the current Ghostfeed site independently confirms the product's AI-TikTok/UGC/slideshow positioning. ^[raw/articles/xarticle-no-bs-guide-to-ai-ugc-at-scale-2049286061105483868.md]

## Evidence status

- **Confirmed from the live source:** the article contains the cost tables, two format calculations, identity prompt, identity handoff, hook-skill prompt and install command, account setup sequence, warm-up schedule, scheduling routes, and later edits preserved above.
- **Corroborated positioning:** Ghostfeed's current site describes AI TikTok video cloning, UGC reactions, slideshows, and an “Operating System for running AI UGC at Scale.” This confirms category positioning only.
- **Source-claimed:** `$22–$266/month`, 2M weekly views, the 12K-view/202-bookmark conversion comparison, model prices, provider recommendations, account limits, shadowban/fingerprint behavior, and TikTok API approval timing.
- **Open:** whether the exact economics, model quality, account durability, funnel lift, or scale claims reproduce outside the author's setup.

## Related

- [[type-kshitij]] — source author
- [[ghostfeed]] — managed generation/scheduling route named in the source
- [[ai-ugc]] — umbrella synthetic-UGC concept
- [[ai-ugc-ad-scaling-system]] — paid-ad testing counterpart
- [[ai-persona-marketing]] — broader virtual-character marketing
- [[tiktok-account-infrastructure]] — physical-device distribution layer
- [[tiktok-slideshow-automation]] — adjacent slideshow production pipeline
- [[tiktok]] — primary distribution surface
- [[claude-code]] — hook-skill extraction interface
- [[apify]] — scraper layer named for Pinterest/TikTok assets
- [[nano-banana]] — identity and first-frame image layer
- [[kling]] — motion-control layer
- [[seedance-2-0]] — alternative higher-cost generation path
