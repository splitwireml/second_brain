---
title: ai-video-virality-formats
created: 2026-04-20
updated: 2026-07-10
type: concept
tags: [content-marketing, seedance-2-0, tiktok, virality, ai-video, ai-ugc]
sources: [raw/articles/frederikfeldt-ai-video-formats-2026-04-20.md, raw/articles/xarticle-every-viral-ai-video-format-explained-in-1-article-2074886930479620587.md, raw/articles/xarticle-how-i-predict-viral-videos-before-they-explode-2074798903124259223.md]
---

# ai-video-virality-formats

Reusable short-form AI video structures that consistently generate viral reach. Earlier notes captured three familiarity-based formats from @FrederikFeldt; John Virality expands the map into 11 formats organized by neurological interrupt, completion-rate mechanic, product fit, and model recommendation.

## Format 1: Before & After Transition

**Performance:** 4.4M likes (record)

**Structure:**
- First half: Old version of character (struggle era, messy hair, tired eyes, cheap apartment)
- Second half: Present day (put together, happy, kids, nice place)
- Trending transition sound (the sound does 80% of the work)
- Match transition timing exactly to the sound's beat drop

**Why it works:** Everyone romanticizes their own glow-up. Viewers project their own journey onto it. People share because it says something about *them*.

**Execution requirements:**
- Two distinct visual identities (not just different outfit — different everything)
- Clean transition matching sound timing exactly
- Generate each half separately in Seedance, stitch in CapCut

## Format 2: Slideshow Story Arc

**Performance:** 1.7M likes, 27 slides, 80% swipe-through rate

**Structure:**
- Snapchat text banner hook ("omg you guys are so cute" or similar)
- Story with emotional arc (pregnancy journey, building something from nothing)
- 20-30 slides (under 15 doesn't build enough momentum)
- Every slide must contain at least one recognizable brand

**Why it works:** Dwell time is the algorithmic signal. Someone swiping through 27 slides = >1 minute on the post = TikTok pushes it harder.

**Key detail:** AI images without brands feel sterile. Real life has logos everywhere. Content needs to too (Starbucks, Target, Nike, Amazon, etc.).

## Format 3: Viral Copy with Product Twist

**Performance:** Copies of viral videos outperforming originals (one copy got 3M likes vs original's 1M)

**Structure:**
1. Find a video already going viral (millions of views, still climbing)
2. Copy it exactly (same sound, format, clip timing, transitions)
3. Use AI to generate your character in the same structure
4. Weave your product naturally into the character's story

**Why it works:** You're leveraging a format the audience already proved they like. Familiarity = trust = engagement.

**Critical requirement:** Must have a persona bible — a 600+ line backstory for your AI character. Random AI girl holding random product = ad. Fully developed character with backstory = content people care about.

## John Virality's 11 AI Video Formats

The 2026 John Virality map shifts this page from a three-format Seedance playbook into a broader format taxonomy for TikTok, Instagram Reels, and YouTube Shorts. Each format specifies the attention mechanism, best-fit product category, and suggested Higgsfield/model route:

| Format | Mechanism | Best fit | Model note |
|---|---|---|---|
| Surreal physics hook | Physical-impossibility interrupt before conscious evaluation | supplements, wellness, beauty, food, luxury | Kling 3.0 or Cinema Studio |
| Freeze-to-motion | Still image becomes animated, creating completion-rate curiosity | ecommerce, fashion, food, strong product photography | Seedance 2.0 |
| Self-insert viral loop / AI dance | Identity expression: the viewer or sharer is literally inside the content | consumer apps, entertainment, lifestyle challenges | Soul |
| Cakeify, squish, melt, inflate | Tactile/physics violations that trigger “is this real?” ambiguity and ASMR-like satisfaction | food, novelty, DTC product, beauty/fashion transitions | Kling 3.0, Seedance 2.0, Cinema Studio |
| Lore fabrication spectacle | Escalating origin/evolution story where each stage implies a bigger next stage | mobile games, entertainment apps, story-led products | Cinema Studio or Veo 3.1 |
| Cellular spectacle | Documentary-style biological visualization that lowers ad skepticism | supplements, wellness, health, skincare | Cinema Studio |
| Ambiguity clip | Footage sits between real and fake, driving epistemic-uncertainty sharing | launches, pre-launch hype, entertainment marketing | Seedance 2.0 or Veo 3.1 |

The practical selection rule is product-fit first: invisible value propositions need cellular spectacle and physics hooks; visual products can use freeze-to-motion and melt transitions; identity-driven apps use self-insert loops and dance templates; games use lore fabrication and ambiguity; broad-awareness products can use cakeify/squish/inflate; pre-launch campaigns lean on ambiguity. ^[raw/articles/xarticle-every-viral-ai-video-format-explained-in-1-article-2074886930479620587.md]


## Format Discovery Loop

Fokki's July 2026 article adds a research layer before format selection: build a swipe feed of roughly 40 faceless channels in one lane, log breakouts daily, and score each candidate by `video views / channel median views` rather than raw view count. In this framing, an outlier score above 10 is signal and above 30 is a format to adapt during the current two-week window; the topic is disposable, while the repeatable shape is the asset.^[raw/articles/xarticle-how-i-predict-viral-videos-before-they-explode-2074798903124259223.md]

The operational loop is `Research → Claude → CapCut → Make → Views`: Claude groups outlier hooks into reusable formats and generates new concepts, CapCut turns shot lists into 9:16 shorts, and Make publishes to TikTok, Shorts, and Reels before writing 48-hour performance back to the same sheet. This makes the format library self-improving instead of a static prompt pack.^[raw/articles/xarticle-how-i-predict-viral-videos-before-they-explode-2074798903124259223.md]

## Why These Three Work

All three trigger the same psychological response: **familiarity**.

- Before/after: familiar structure, new character, instant trust
- Slideshow: familiar context (something a friend shared), emotional investment
- Viral copy: literally a format already validated by the audience

Familiarity → trust → engagement → algorithmic distribution. The algorithm pushes what people engage with, and engagement comes from trust, which comes from familiarity.

## Related

- [[frederikfeldt]] — documented the three familiarity-based formats and 114M views claim
- [[john-virality]] — expanded this concept into an 11-format AI-video taxonomy
- [[seedance-2-0]] — model route for freeze-to-motion and ambiguity clips
- [[kling]] — model route for surreal physics and cakeify/squish-style effects
- [[higgsfield]] — distribution/production layer referenced for routing models
- [[instagram-ugc-system]] — broader system incorporating these formats
- [[ai-ugc-ad-scaling-system]] — scaling framework
- [[virality-mechanics]] — neurological and algorithmic basis for the formats
- [[0x-fokki]] — added the outlier-score research loop and Claude/CapCut/Make execution stack
