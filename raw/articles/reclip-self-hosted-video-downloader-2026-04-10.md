---
updated: 2026-04-11
type: raw
title: ReClip — Self-Hosted Video/Audio Downloader with Clean Web UI
source_type: github-repo
url: https://github.com/averygan/reclip
author: Avery Gan (averygan)
date: retrieved 2026-04-10
retrieved: 2026-04-10
license: MIT
---

# ReClip — Self-Hosted Video/Audio Downloader

A self-hosted, open-source video and audio downloader with a clean web UI. Paste links from YouTube, TikTok, Instagram, Twitter/X, and 1000+ other sites — download as MP4 or MP3.

## Features
- Download videos from 1000+ supported sites (via yt-dlp)
- MP4 video or MP3 audio extraction
- Quality/resolution picker
- Bulk downloads — paste multiple URLs at once
- Automatic URL deduplication
- Clean, responsive UI — no frameworks, no build step
- Single Python file backend (~150 lines)

## Stack
- Backend: Python + Flask (~150 lines)
- Frontend: Vanilla HTML/CSS/JS (single file, no build step)
- Download engine: yt-dlp + ffmpeg
- Dependencies: 2 (Flask, yt-dlp)

## Quick Start
```bash
brew install yt-dlp ffmpeg
git clone https://github.com/averygan/reclip.git
cd reclip
./reclip.sh
# Open http://localhost:8899
```

Docker: `docker build -t reclip . && docker run -p 8899:8899 reclip`

## Usage Flow
1. Paste one or more video URLs
2. Choose MP4 or MP3
3. Click Fetch → loads video info + thumbnails
4. Select quality/resolution
5. Download individual or all

## Supported Sites
Anything yt-dlp supports: YouTube, TikTok, Instagram, Twitter/X, Reddit, Facebook, Vimeo, Twitch, Dailymotion, SoundCloud, Loom, Streamable, Pinterest, Tumblr, Threads, LinkedIn, etc.

## License

## See Also

- [[reclip-video-downloader]] — ReClip project page
- [[paperclip-orchestrator]] — Paperclip — video pipeline orchestration

MIT