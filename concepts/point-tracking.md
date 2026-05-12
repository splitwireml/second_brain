---
title: Point Tracking
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [point-tracking, computer-vision, video]
sources: []
---

## Overview

Point tracking is the computer vision task of following a specific point (or set of points) across consecutive video frames. Given a point's location in frame 1, the tracker predicts its location in subsequent frames as objects move, deform, or go occluded.

## How it works

1. Initialize with sparse points (clicked by user or detected by detector)
2. For each new frame, predict where each point moved
3. Handle occlusions via re-identification or motion modeling

## Relationship to Other Concepts

- [[segmentation]] — point tracking can be seen as a 1-pixel "segmentation" of a moving point; related human-AI collaborative patterns apply
- [[sam3-ai-box]] — similar human-guidance AI pattern but for boxes vs. points
- [[video-segmentation]] — tracking regions/objects across frames vs. tracking individual points
- [[training-free]] — many modern trackers (e.g., CoTracker, TAPIR) operate zero-shot without task-specific training

## Key Methods

- **TAPIR** (Track Anything, Predict Interactions) — SAM-powered point tracking
- **CoTracker** — collaborative tracking of multiple points with correlation volumes
- **OCSORT** — occlusion-aware multi-object tracking

## Related Concepts

- [[sam3-ai-box]] — box-based variant of human-guided visual AI
- [[segmentation]] — the broader task family
- [[video-segmentation]] — temporal extension of segmentation across frames
