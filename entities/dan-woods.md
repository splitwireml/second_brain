---
title: Dan Woods
created: 2026-04-16
updated: 2026-04-16
type: entity
tags: [person]
sources: [raw/articles/danveloper-flash-moe-qwen-397b-2026-04-16.md, raw/articles/x-bookmark-2044346237239894229.md]
---

# Dan Woods

X/Twitter creator [@danveloper](https://x.com/danveloper). Built [[flash-moe]] — a system for running 397B parameter MoE models on a MacBook Pro with 48 GB RAM by streaming weights from SSD via Apple's unified memory architecture.

## Key Work

### flash-moe (2026)

Objective-C/Metal implementation of Apple's "LLM in a Flash" paper for running Qwen 3.5 397B on a MacBook Pro M3 Max. No Python in the hot path, no ML framework — pure Metal Shading Language fused GPU pipeline. Claude (Opus 4.6) wrote all the code (~5,000 lines Obj-C + ~1,100 lines Metal shaders) under Dan's direction via Karpathy-style autoresearch methodology.

Repository: [github.com/danveloper/flash-moe](https://github.com/danveloper/flash-moe) (3,641 stars)

### UGC Video Pipeline (2026)

Documented a Claude Code automated UGC video production pipeline using DansUGC:
1. Order real human UGC reactions/demos from [[dansugc]] ($8/video)
2. Research competitors' best converting hooks with social growth engineers
3. Use Gemini to intelligently match demos with UGC reactions and hooks
4. Use Claude Code to orchestrate the full pipeline

## References

- [Dan Woods on X/Twitter](https://x.com/danveloper)
- [flash-moe repository](https://github.com/danveloper/flash-moe)
