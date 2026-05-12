---
title: DansUGC
created: 2026-04-15
updated: 2026-04-15
type: entity
tags: [ugc, video, product, service]
sources: [raw/articles/x-bookmark-2044346237239894229.md]
---

# DansUGC

## Overview

DansUGC is a platform for ordering real human UGC (User Generated Content) reaction and demo videos at $8/video. Marketers and creators use it to source authentic human footage for ad creative testing without hiring actors or filming themselves.

## How It Fits in the Workflow

The documented Claude Code + DansUGC pipeline:
1. Order real human UGC reactions/demos from DansUGC ($8/video)
2. Research competitors' best converting hooks with social growth engineers
3. Use Gemini to intelligently match demos with UGC reactions and hooks
4. Use Claude Code to orchestrate the full pipeline

## Relationship to Other Entities

- [[stijn-feijen]] — uses DansUGC in the [[ai-ugc-ad-scaling-system]] workflow alongside [[seedance-2-0]] for generation and [[makeugc]] for publishing
- [[makeugc]] — UGC ad-production platform; DansUGC provides human footage as input to the pipeline
- [[seedance-2-0]] — video generation layer; DansUGC provides human footage that can be combined with AI-generated content
- [[dan-woods]] — documented a Claude Code + DansUGC + Gemini UGC video pipeline

## Related Concepts

- [[ai-ugc-ad-scaling-system]] — broader workflow for AI UGC ad production at scale
