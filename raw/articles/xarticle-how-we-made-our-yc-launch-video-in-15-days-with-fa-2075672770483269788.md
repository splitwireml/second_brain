---
source_url: https://x.com/mattchowx/status/2075672770483269788
ingested: 2026-07-12
sha256: 9af80ad948ca1f440cd42f15f2b9e75b95af488a6618b6ca9f67cf3f131e993b
---

---
title: "How we made our YC launch video in 1.5 days with Fable 5"
source: "x-bookmarks"
tweet_id: "2075672770483269788"
tweet_url: "https://x.com/mattchowx/status/2075672770483269788"
author_name: "Matt Chow"
author_handle: "@mattchowx"
tweet_date: "Fri Jul 10 20:05:27 +0000 2026"
bookmark_date: "2026-07-10"
content_type: "x_article"
character_count: 5531
retweet_count: 24
like_count: 488
---

# How we made our YC launch video in 1.5 days with Fable 5

How we made our YC launch video in 1.5 days with Fable 5

Agencies quoted us $4-8k and 2-4 weeks. Fiverr was $500-2k and still over a week. We launched Trope on YC this week with a 75-second video that people keep asking "which agency made this?" about, and the secret: a clubroom, an iPhone, and Fable 5 running Remotion.

Here's the full breakdown.

## Why we didn't just hire someone

Our buyers read production quality as a trust signal, so it couldn't look handheld or homemade. We wanted unlimited revisions without paying anyone per change, and full control over the vision.

The unlock: doing it in code means every asset is reusable. Our website now runs iterations of the motion graphics from the launch video. The second video is basically free.

## The pipeline

Prep (spare time during the week): Drafted the script intermittently and revised it after customer calls. We tried a few structures and landed on talking head + product showcase, which builds the most trust with our audience. Storyboarded key frames with GPT-Image-2 (on the ChatGPT Pro sub we already had) so we knew where wall text, logos, and product shots land, then put everything in one PDF along with a few launch videos we liked as motion reference.

Saturday evening: Shot the talking head in our apartment building's clubroom. Brick wall, plants, decent light. Filming took under an hour. Most of the effort went into lighting and making sure the mic audio was usable.

Saturday night through Sunday: Both of us worked in parallel with Claude Code (Fable 5) on a Remotion project. Remotion is React that renders to video. We had never used it before this weekend. Our literal first prompt was "do you have remotion access?"

My co-founder Victor gave it the 25-page storyboard PDF plus our product code, and it had all 7 product scenes rendered about 2 hours after his first prompt. By 4am that session had transparent title overlays, auto-generated captions, and clips synced to the voiceover word by word. Sunday was motion graphics, transitions from footage into product UI, pacing, the full assembly, and sound. Watchable end to end by Sunday night.

## What actually made it work

Plug your codebase in. We gave Fable 5 our product code so it could pull real design tokens, real fixture data, and real fonts. Every "product" shot in the video is rebuilt React, not a screen recording. That includes the Microsoft Dynamics 365 Business Central scenes (one of our main integrations), recreated and animated directly in Remotion. This is why the product shots look legit instead of like an AI mock.

Transcribe the voiceover first. Whisper with word-level timestamps. Every animation beat lands on the word being said, and you can direct with timecodes: "1:09.34 is where 'If you're tired' should appear." Fable 5 figures out the frame math, pre-renders, and you just check the result.

Screenshots > only descriptions. Paste an annotated frame of what's wrong instead of explaining it. Even better, it checks its own work by rendering single frames and looking at them, so it catches a lot before you do.

Do camera moves in code. All punch-ins and reframes are lossless, in code, instead of in an editor. We could steer with blunt feedback ("this is too tacky") and physical timing language ("0.5s longer", "come in 500ms earlier"), and Fable 5 landed the direction on the first try more often than not. Motion blur, Bezier easing, all of it.

Upscale the footage, not the UI. Topaz (Starlight Precise 2.5) was worth it for the filmed footage (iPhone, dark room, grainy). For the Remotion segments you just re-render at native 4K 60fps for free. Don't AI-upscale generated UI, it only degrades it.

Run parallel sessions. We had up to 6 Fable 5 sessions going at once, roughly one per clip. They notice each other's edits and merge around them. We caught up on each other's work by asking "what changed in this branch" instead of reading diffs. A poor man's collaborative video editor.

Simplify the audio. ElevenLabs sound effects worked, but the mix got better every time we simplified (less is more?). We went from 40 sound effects to 21. Generated music via the API didn't land after 3 rounds, so we prompted the playground directly with strict constraints (instrumental, no risers, section lengths matched to the cut). We also tried AI voice isolation on the VO and reverted it. If we could redo one thing, it'd be the audio recording setup.

Finish in a real editor. One final pass in DaVinci Resolve (free) for audio levels and hitting -14 LUFS for social. The hard visual work was already handled by Fable 5 in Remotion.

## The numbers

1.5 days of build time. Roughly $2.3k all-in at market rates: ~$2,250 of Claude usage at API list prices (measured from our session transcripts afterwards, and fully covered by startup credits for us), plus $78 for Topaz and $19 for ElevenLabs. Versus $4-8k and 2-4 weeks for an agency.

## The takeaway

Video editing with frontier models (Fable 5, and now GPT 5.6) is a great way to ship a launch video fast while keeping full control. Everything is code, so every change is cheap, nothing is locked in an editor project file, and you collaborate over git.

You don't need to know the video framework. We learned what Remotion was mid-project. You need creativity and the willingness to say "redo it" until it matches your vision.

If you want to show off your software, give the model your actual product code. That's the difference between a demo that looks real and one that looks generated.
