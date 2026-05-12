---
title: HyperFrames
created: 2026-04-18
updated: 2026-04-18
type: entity
tags: [genai, video-generation, ai-tools, agent, open-source]
sources: [raw/articles/x-bookmark-2044827454460871072.md]
related_entity: [[heygen]]
---

# HyperFrames

Open-source agent-native framework by HeyGen for converting HTML to MP4 video. Used by HeyGen to build their own launch video in Claude Code.

## Overview

HyperFrames is an open-source framework that lets AI coding agents (Claude Code, etc.) generate MP4 videos from HTML/CSS specifications. The framework is agent-native — designed to be invoked via a skill/package manager rather than manually configured.

Installation:
```
$ npx skills add heygen-com/hyperframes
```

The launch video was built entirely in Claude Code using this framework, then open-sourced.

## Relationship to HeyGen

[[heygen]] is the company behind HyperFrames. HeyGen is a commercial AI video generation platform; HyperFrames is their open-source contribution to the agent tooling ecosystem.

## References

- [@HeyGen announcement](https://x.com/HeyGen/status/2044827454460871072)
- `npx skills add heygen-com/hyperframes`
