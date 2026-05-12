---
title: ReClip — Self-Hosted Video/Audio Downloader with Clean Web UI
created: 2026-04-10
updated: 2026-04-10
type: concept
tags: [tools, oss-ai, product]
sources: [raw/articles/reclip-self-hosted-video-downloader-2026-04-10.md]
---

# ReClip — Self-Hosted Video/Audio Downloader

> A self-hosted, open-source video and audio downloader with a clean web UI. Paste links from YouTube, TikTok, Instagram, Twitter/X, and 1000+ other sites — download as MP4 or MP3.

**GitHub:** [averygan/reclip](https://github.com/averygan/reclip)
**License:** MIT
**Stack:** Python + Flask (~150 lines backend) + Vanilla HTML/CSS/JS frontend

## Overview

ReClip is a minimalist self-hosted downloader that wraps yt-dlp + ffmpeg behind a clean web interface. It supports 1000+ sites (anything yt-dlp handles) and outputs MP4 or MP3 with quality selection, bulk download, and URL deduplication.

## Architecture

Deliberately minimal — the entire stack is ~150 lines of Python (Flask) + a single vanilla HTML/CSS/JS file for the frontend. Two dependencies: Flask and yt-dlp. No frameworks, no build step, no database.

## Features

| Feature | Details |
|---------|---------|
| Multi-site support | Anything yt-dlp supports (YouTube, TikTok, X/Twitter, Instagram, Reddit, Vimeo, Twitch, etc.) |
| Dual output | MP4 video or MP3 audio extraction |
| Quality picker | Resolution/quality selection per video |
| Bulk download | Paste multiple URLs at once |
| URL deduplication | Automatic — no duplicate downloads |
| Thumbnails | Fetches and displays video thumbnails before download |
| Responsive UI | Works on desktop and mobile |

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
4. Select quality/resolution if available
5. Download individual or all

## Backend API

The Flask backend exposes a REST API at `http://localhost:8899/api/`:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/info` | POST | Fetch video metadata + available quality formats |
| `/api/download` | POST | Start async download, returns `job_id` |
| `/api/status/<job_id>` | GET | Poll download status |
| `/api/file/<job_id>` | GET | Download completed file |

See the `reclip-api` skill for full API reference.

## Video Ingestion Pipeline

ReClip + [[vibevoice]] ASR can be chained to ingest video content into the wiki:

1. Download video/audio via ReClip API (`format: "audio"` for MP3)
2. Transcribe with VibeVoice ASR
3. Save to `raw/transcripts/` (transcription JSON → md via transcription_json_to_md.py)
4. Standard wiki ingestion

See the `video-ingestion` skill for the full pipeline.

## Why It Matters

Most yt-dlp frontends are either CLI-only (yt-dlp itself), bloated with unnecessary features, or commercial. ReClip hits a sweet spot: self-hosted, MIT-licensed, clean UI, minimal code surface (~150 lines backend), and no build complexity. It's the kind of tool you deploy once on a home server and forget about.

## Related

- [[open-higgsfield-ai]] — Generative AI creative suite; ReClip could serve as a companion tool for downloading reference videos for AI workflows
- [[prompt-engineering-patterns]] — Prompt patterns for creative work; downloaded content can serve as input for AI generation pipelines
- [[llm-server-throughput-optimization]] — Multi-instance Llama.cpp + nginx; ReClip downloads audio for transcription workflows that feed into this pipeline
