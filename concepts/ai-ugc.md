---
title: AI-UGC
created: 2026-05-31
updated: 2026-08-08
type: concept
tags: [ai-ugc, content, marketing, ugc, video, viral]
sources: [raw/articles/14-second-ai-vlog-method.md, raw/articles/makeugc-ad-remake-viral-ad-workflow.md, raw/articles/xarticle-how-i-do-6mmonth-with-my-ecom-brand-using-ai-podca-2080778980555133219.md, raw/articles/xarticle-no-bs-guide-to-ai-ugc-at-scale-2049286061105483868.md, raw/articles/xarticle-how-to-build-an-ai-ugc-factory-in-claude-code-2085362363214201033.md, raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]
---

# AI-UGC

AI-generated user-generated content. Short-form video content (TikTok, Instagram Reels, YouTube Shorts) created using AI tools rather than human actors. Core strategy for [[viral-marketing]], [[affiliate-ai-ugc]], and [[ai-cartoon-character-ugc-system]].

The supplied 14-second AI vlog source is a concrete synthetic-UGC workflow: one recurring character, three separately generated scenes, a human QC gate, and platform-specific exports. Its claims about quality, cost, and production speed remain source-reported. ^[raw/articles/14-second-ai-vlog-method.md]

## Reference-led ad remake

The MakeUGC paste describes a reference-led synthetic-UGC path: start from a competitor ad instead of a blank brief, provide a similar-type product, state the desired direction, and let the remake model produce a variant. This can reduce ideation friction, but the source does not establish that the resulting creative preserves performance or that the reference may be reused without permission. ^[raw/articles/makeugc-ad-remake-viral-ad-workflow.md]

## Long-form podcast-style UGC

The [[ceo-vlad]] article adds a longer-form advertising pattern to AI-UGC: two synthetic speakers use a podcast frame, conversational objections, and product-in-context dialogue instead of a short direct pitch. [[infinite-ugc]] is the source-described production tool, with [[claude]] used for scripts and hook volume. The article's claims about watch time, cost, and ecommerce revenue remain source-reported. ^[raw/articles/xarticle-how-i-do-6mmonth-with-my-ecom-brand-using-ai-podca-2080778980555133219.md]

See [[ai-podcast-ads]] for the format-specific workflow and [[ai-ugc-ad-scaling-system]] for the testing loop around it.

## Organic persona-portfolio branch

[[type-kshitij]]'s source adds an organic portfolio variant: lock one AI persona identity, choose slideshow or reaction formats from generation economics, study the target audience's language, and distribute through warmed TikTok accounts. The source calculates roughly `$0.06` per persona-led slideshow and `$0.74` per 10-second reaction, then connects saves/comments/DMs/shares to a SaaS funnel. These economics, performance comparisons, and account-behavior claims remain source-reported. ^[raw/articles/xarticle-no-bs-guide-to-ai-ugc-at-scale-2049286061105483868.md]

The reusable framework is filed as [[ai-ugc-persona-factory]]. It complements the paid creative-testing model in [[ai-ugc-ad-scaling-system]] rather than replacing it.

## Key Patterns

- [[ai-cartoon-ugc-monetization]] — monetizing AI character accounts
- [[ai-generated-ugc-ads]] — AI UGC for advertising
- [[ai-3d-scroll-websites]] — 3D scrolling sites with AI content

## Related Concepts

- [[ugc]] — UGC broadly
- [[viral-marketing]] — viral distribution
- [[marketing]] — marketing with AI UGC
- [[14-second-ai-vlog-method]] — scene-by-scene AI vlog production method
- [[beechinour]] — source author of the Seedance 2.5 UGC and painted-animation branch

## Research-first AI UGC ad factory (2026-08-08)

Machina's source adds a paid-creative factory branch that keeps research ahead of rendering. Higgsfield is presented with two doors: Supercomputer handles research, scripting, images, clips, montage, and refinement on one platform; the DIY route makes Higgsfield models addressable from Claude Code. The source describes these capabilities and the human-versus-AI ad comparison as source claims, not independent product or performance evidence.^[raw/articles/xarticle-how-to-build-an-ai-ugc-factory-in-claude-code-2085362363214201033.md]

### Research and vault

The first input is customer language, not visual style. The source also names the not-yet-announced `@eptwts` research agent for creatives, which is described as returning top-performing niche ads, creators, exact hook lines, and script beats; it points readers to `weeklyaiops.com` for prompt scaffolds, a vault template, and ready-to-run briefs. These named services and offers are source-described and not independently validated. The source's manual path searches TikTok Shop, TikTok's Creative Center, and Meta's ad library; those surfaces show what ran, not what converted, so every ad is a candidate. Customer complaints and review/comment language come before competitor research. Each winning-ad Markdown note stores the live link as a receipt, verbatim transcript, hook family, timed hook/pain/mechanism/proof/CTA beat map, proof device, CTA wording, and one line on why it wins. The notes feed `hooks.md`, `ctas.md`, and one map-of-content note per niche in an Obsidian folder. A persuasion record is kept separate from a capture record: the former stores hook family, beat timing, product entry, proof, objection, and CTA; the latter stores device, framing, light, and cuts.^[raw/articles/xarticle-how-to-build-an-ai-ugc-factory-in-claude-code-2085362363214201033.md]

### Script math and voice

The source fixes delivery before rendering: talking-head speech is about 3.5 words/second; a 30-second ad is roughly 105 words with a ±10% range; every clip stays under 9 seconds; and a six-second clip carries about 21 words. One ad carries one message, ends on its CTA, respells a brand when needed for pronunciation, and is read aloud before rendering. A hook may be an offer, confession, or call-out; the example confession is `I own six push-up bras and i hate five of them`. Native Seedance audio can anchor the voice across clips, while ElevenLabs is the optional voice-design path.^[raw/articles/xarticle-how-to-build-an-ai-ugc-factory-in-claude-code-2085362363214201033.md]

### Locked references and prompts

The character process is: generate a headshot, generate a full-body image from that headshot, and attach both exact images to every clip without recropping or regenerating. The source-preserved prompts are:

```text
casual iPhone-quality selfie-style headshot portrait of a woman in her late 20s, warm chestnut brown hair in a loose low bun with face-framing strands, hazel eyes, light olive skin with a few freckles, friendly wry expression, minimal natural makeup. wearing a heather-grey ribbed tank top, small gold stud earrings, no other jewellery. soft indoor daylight, plain bedroom wall behind, slightly imperfect framing, authentic phone-photo look, not studio, not glossy
```

```text
full-body casual photo of the SAME woman as the reference image, identical face, hair and outfit: late 20s, chestnut brown hair in a loose low bun, heather-grey ribbed tank top, relaxed black lounge joggers, barefoot, small gold stud earrings, no other jewellery. standing relaxed in a cozy bedroom, soft daylight, phone-photo realism, full figure visible head to feet, natural posture
```

The source uses Nano Banana with the headshot as the full-body reference and for before/after variants; it says the exact identity and outfit must remain fixed because the video model averages what it sees. The product also gets one still reused in every relevant clip:

```text
product photography of a matte soft-white plastic sunscreen tube standing upright, flip cap down. label design: warm orange wordmark 'NOON' in clean modern sans-serif, below it smaller text 'daily SPF 50' and 'invisible finish · 50 ml'. minimal skincare aesthetic, soft daylight studio lighting, pale warm background, gentle shadow. centered, whole tube visible
```

The source calls out device class (`iPhone-quality selfie-style`), freckles, loose strands, imperfect framing, skin texture, closed wardrobe, exact quoted label text, material description, and a large brand name as identity/realism anchors. These are source-described prompt mechanics, not independently benchmarked rules.^[raw/articles/xarticle-how-to-build-an-ai-ugc-factory-in-claude-code-2085362363214201033.md]

### Generation laws and clip grammar

The source's failed-render rules are: hold objects rather than script a grasp; stage exactly one object scene-wide with no reflection copies; close the wardrobe and jewellery list; put one continuous action and one emotion in each clip; describe framing rather than asking for a visible camera; repeat the product description verbatim; and move every state change across a cut. A cream demo is therefore “swatch on hand” → cut → “half blended” → cut → “clean skin,” never a generated rubbing transition. Each prompt ends with `iPhone front-facing 23mm equivalent, gentle handheld drift, built-in mic, no music`.

Seedance is the source-described video engine. Its fixed prompt skeleton is a register line, scene line, one delivery word, an exact quoted line, and hard rules; the source's bra example specifies a 9:16 handheld front-camera ad, reference-image identity, reference-audio voice, a fed-up delivery, an exact quote, a held bra, grey tank top, and no captions. Useful additions are a glance away and back around second 8, named micro-behaviors, one physics cue, whole-second durations from 4–9 seconds (usually 5–8), lived-in sets, and `holds the final pose to the last frame` on the close.^[raw/articles/xarticle-how-to-build-an-ai-ugc-factory-in-claude-code-2085362363214201033.md]

```text
a realistic, authentic UGC ad, handheld front-camera selfie video, 9:16. keep the character consistent with the reference images. her voice matches the reference audio exactly

standing in front of her open closet with a mirror, holding the blush-pink bra in one hand. delivery: fed up, venting to a friend. she says exactly: "they all do the same trade. great shape for the first hour, and by six pm the wires are digging and you're counting minutes till home"

the bra stays in her hand as an object the whole clip, never worn. she is fully dressed in her grey ribbed tank top. no on-screen text or captions
```

### Factory loop and gate

The factory renders the hook alone, judges face and voice, extracts approved-hook audio as the later reference (or uses an ElevenLabs hook file), then submits remaining clips in parallel with the same character sheet, product still, and voice anchor. Every beat gets a different room or framing; the backend's concurrency cap is treated as a scheduling constraint. Claude Code concatenates clips with `ffmpeg` and normalizes loudness. A frame check samples 16 evenly spaced frames for limbs/fingers, object permanence, label text, background continuity, and filming-device leaks. It is cut-blind and measures broken rather than persuasive, so the source keeps the human eye as the shipping judge. TikTok's AI-ad disclosure is described as a required upload checkbox.^[raw/articles/xarticle-how-to-build-an-ai-ugc-factory-in-claude-code-2085362363214201033.md]

## Seedance 2.5 UGC and painted-animation branch (2026-08-06)

The source adds a synthetic-UGC lane that favors phone-camera honesty—slight shake, casual autofocus hunting, no gimbal smoothing—plus real pauses, filler words, trailing off, and stretches where the speaker performs the action instead of narrating. It says objects should enter frame through a visible hand action, native SFX are strongest for mechanical subjects, native dialogue is mostly skipped, and music is added during editing. These observations are source-described and include credit to a separate Maximalist UGC guide; they are not independent benchmarks. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

The author instead favors painted animation. The source-described pipeline is Midjourney base images → GPT image models for style conversion, upscaling, and style-locking → `4–10` images as references in each Seedance 2.5 prompt. Gemini is used to extract the exact visual details of imagery or cartoons the operator likes into a reusable style paragraph, which is pasted into Midjourney, GPT image, and Seedance at every shot. The source's Into-the-Spider-Verse-like quality target and its embedded examples are aspirations/evidence boundaries, not verified outcomes. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

