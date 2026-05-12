#!/usr/bin/env python3
import json
from pathlib import Path

wiki = Path.home() / "wiki"
transcript_path = wiki / "raw" / "assets" / "transcriptions" / "2026-04-17-Gemini-3.1-Seedance-2.0-build-cinematic-10k-websites.json"

with open(transcript_path) as f:
    data = json.load(f)

segments = json.loads(data["text"])
print("Segments:", len(segments))

# Build formatted full text using get() to avoid any encoding edge cases
lines = []
for s in segments:
    start = s.get("Start")
    end = s.get("End")
    speaker = s.get("Speaker")
    content = s.get("Content")
    lines.append("[{:.2f}s - {:.2f}s | Speaker {}]\n{}".format(start, end, speaker, content))
full_text = "\n\n".join(lines)

print("Full text chars:", len(full_text))

# Raw article
raw_article = """---
title: "Gemini 3.1 + Seedance 2.0: Build Cinematic $10k Websites"
source_type: video_transcription
url: https://x.com/viktoroddy/status/2044752987772576083
author: "Viktor Oddy (@viktoroddy)"
date: 2026-04-17
duration: 16:29
tweet_id: "2044752987772576083"
platform: x
likes: 4692
retweets: 477
replies: 65
audio: raw/assets/2026-04-17-Gemini 3.1 + Seedance 2.0 Build Cinematic $10k Web.mp3
transcription: raw/transcripts/2026-04-17-Gemini-3.1-Seedance-2.0-build-cinematic-10k-websites.md
---

## Tweet

**@Viktor Oddy (@viktoroddy):**

Just Recorded a 16 min Tutorial on How to use Gemini 3.1 + Seedance 2.0 Build Cinematic $10k Websites (step-by-step)

You can now build stunning marketing sites fully with AI

## Summary

A 16-minute step-by-step tutorial showing how to design and build animated, cinematic marketing websites using AI tools -- specifically **Gemini 3.1** and **Seedance 2.0**. Viktor Oddy walks through the complete workflow: sourcing style references from Pinterest, generating AI images with Flux/Hexler, animating with Seedance 2.0, and compiling into a website. He also covers selling this as a high-ticket service ($10k+).

## Tools Covered

- **Pinterest** -- Style reference discovery for 3D avatar/character aesthetics
- **Flux / Hexler** -- AI image generation (Flux 1.1 Pro) for backgrounds and characters
- **Seedance 2.0** -- ByteDance video generation model for looping website animations (supersedes Kling 3.0)
- **Gemini 3.1** -- AI model powering the image generation workflow

## Key Claims

- Seedance 2.0 produces better looping animations than Kling 3.0 (smoother spin, no cutoff at loop point)
- Nana Banana Pro 2 is Viktor's preferred model for 3D avatar/character generation
- The workflow enables selling "cinematic $10k websites" as a service
- No need to build from scratch -- replicate what already works in the AI era

## Raw Transcription

""" + full_text

raw_path = wiki / "raw" / "articles" / "viktoroddy-gemini-seedance-websites-2026-04-17.md"
with open(raw_path, "w", encoding="utf-8") as f:
    f.write(raw_article)
print("Raw article:", raw_path.stat().st_size, "bytes")

# Frontmatter index
index_content = """---
title: "Gemini 3.1 + Seedance 2.0: Build Cinematic $10k Websites"
source_type: video_transcription
url: https://x.com/viktoroddy/status/2044752987772576083
author: "Viktor Oddy (@viktoroddy)"
date: 2026-04-17
duration: 16:29
audio: raw/assets/2026-04-17-Gemini 3.1 + Seedance 2.0 Build Cinematic $10k Web.mp3
transcription: raw/transcripts/2026-04-17-Gemini-3.1-Seedance-2.0-build-cinematic-10k-websites.md
---
"""
index_path = wiki / "raw" / "2026-04-17-gemini-seedance-10k-websites.md"
with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)
print("Frontmatter index:", index_path)
print("DONE")
