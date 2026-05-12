---
title: Video Segmentation
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [video-segmentation, computer-vision, video]
sources: []
---

## Overview

Video segmentation is the task of assigning semantic or instance labels to pixels in video sequences, extending image segmentation across time. It requires temporal consistency — objects tracked across frames should maintain the same segmentation identity.

## Variants

- **Semantic video segmentation** — per-pixel class labels across all frames
- **Video instance segmentation (VIS)** — track and segment distinct object instances across frames
- **Video object segmentation (VOS)** — segment a target object given a mask in the first frame (one-shot)
- **Referring video segmentation** — segment objects described by a language expression

## Temporal Consistency Challenge

Unlike image segmentation, video segmentation must handle:
- Object motion and deformation
- Occlusions and dis-occlusions
- Appearance changes (lighting, viewpoint)
- Drifting of the segmentation mask over time

## Key Methods

- **MaskTrack** — one-shot VOS: given initial mask, track and segment in subsequent frames
- **XMem++** — long-range video object segmentation with memory banks
- **SAM + tracking** — combine SAM with point/object tracking for zero-shot video segmentation
- **Video MAE** — self-supervised pretraining on video for segmentation features

## Relationship to Other Concepts

- [[segmentation]] — the image-level analog; video extends this with temporal dimension
- [[point-tracking]] — follows points; video segmentation follows regions/objects
- [[sam3-ai-box]] — box-based segmentation in images; could be extended to video with tracking

## Related Concepts

- [[segmentation]] — foundational task
- [[point-tracking]] — related temporal correspondence task
