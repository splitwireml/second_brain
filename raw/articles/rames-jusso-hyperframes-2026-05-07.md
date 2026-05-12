---
title: "Building on top of HyperFrames"
author_name: "James Russo"
author_handle: "@Rames_Jusso"
tweet_id: "2052465022367043830"
tweet_url: "https://x.com/Rames_Jusso/status/2052465022367043830"
tweet_date: "Thu May 07 19:06:08 +0000 2026"
bookmark_date: "2026-05-07"
source: "x-bookmarks"
content_type: "x_article"
character_count: 4240
retweet_count: 2
like_count: 46
external_urls:
  - "https://llm-stories-hyperframes.vercel.app/"
  - "https://github.com/heygen-com/hyperframes-vercel-template"
type: x_article
tags: []
---

# Building on top of HyperFrames

Building on top of HyperFrames

AI-generated videos you can edit like code. Built with HyperFrames and a few LLMs.

When most people think "AI video" they think Veo, Sora (RIP), Seedance. Photoreal video generators that conjure scenes from prompts.

For a lot of visual products though (animated explainers, dashboards-as-video, narrated stories), you don't need them. You can just write code.

I built an LLM-driven visual story generator on top of HyperFrames for as low as $0.02 a story. Every tweak of a video is a code edit, not an expensive regeneration.

Here's how I got there.

Last year I built a side project with a friend. Generative TikTok-style carousels with text-to-speech overlays. Simple Next.js fullstack app on Vercel, Blob Storage, the AI SDK. Nothing too complex, not even fully agentic, just a basic LLM workflow.

Putting the orchestration together wasn't the hard part. The visuals quality and price was the hard part.

We had to cobble together three model types:

- LLMs to orchestrate and write the scripts

- Image gen models for the visually engaging cards

- TTS models for narration

Each image was around 4 cents using something like Nano Banana 1.

A multi-card carousel ran 20+ cents in image gen alone, plus LLM tokens, plus TTS. And the images hallucinated. Misspelled words on cards, garbled brand names, the kind of output that's not production ready.

Worse, every fix meant another 4 cent regeneration and a prayer the model would get it right this time.

Fast forward to today. With HyperFrames the same app doesn't need image or video gen models at all.

Just text-based LLMs writing code.

The LLM generates the HyperFrames HTML, HyperFrames can be previewed as HTML avoiding render latency (until you want to export), and TTS handles the narration. And the Vercel AI SDK ties it all together.

On cheap cloud models like Gemini 3 Flash you can get very cheap output, approximately 2 cents a story. With a local model on your own GPU it's near-zero, just electricity. At the frontier (Claude Sonnet 4.6 with GPT-5.4-mini) you're closer to 20 cents per story, similar to what image gen used to cost.

Once the LLM produces valid HTML, most tweaks are cheap though. Misspelled word? Edit the string. Wrong color across 12 chapters? Find-and-replace once. With image gen each fix was 4 cents and a re-roll.

You can checkout the app here [https://llm-stories-hyperframes.vercel.app/](https://llm-stories-hyperframes.vercel.app/)

## The setup

The HyperFrames player is a zero-dependency web component. Drop it into any app (Next.js, vanilla HTML, whatever) and you have live browser preview of generated compositions:

```javascript
"use client";

import { useEffect, useState } from "react";

export default function Preview() {
  const [ready, setReady] = useState(false);

  useEffect(() => {
    import("@hyperframes/player").then(() => setReady(true));
  }, []);

  if (!ready) return null;

  return (
    <hyperframes-player
      src="/api/preview"
      width={1920}
      height={1080}
      controls
    />
  );
}
```

The full pipeline:

- Full-stack Next.js app deployed on Vercel

- Frontend uses <hyperframes-player> for live browser preview, no rendering required

- Backend uses the AI SDK to orchestrate LLMs that outline a story and generate the HyperFrames HTML

- TTS via the AI SDK for narration

If you want to render MP4s in your app, you can use our Vercel template to wire up Vercel Sandbox (a Firecracker microVM that runs Chromium and ffmpeg) plus Vercel Blob for output storage.

## What you can build

[Our Vercel template](https://github.com/heygen-com/hyperframes-vercel-template) is just the starting point. It gives you the basic building blocks.

[Embedded Tweet: https://x.com/i/status/2052431072374510065]

The world of possibilities on top of this shape is endless:

- Animated changelog reels for SaaS releases

- Dashboards-as-video, weekly metrics auto-generated and shared online

- Language-learning shorts with synced narration and word highlighting

- AI-narrated docs walkthroughs (LLM picks the code samples, generates the animated explanation)

Clone [the template](https://github.com/heygen-com/hyperframes-vercel-template).

And go build something!