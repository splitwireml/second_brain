---
title: 3D Vision
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [3d-vision]
sources: []
---

## Overview

3D vision encompasses techniques for reconstructing, understanding, and generating 3D representations of the world from 2D images or depth sensors. It is a core computer vision discipline underlying robotics, AR/VR, autonomous driving, and content creation.

## Core Tasks

- **3D reconstruction** — recover 3D geometry from multiple 2D views (COLMAP, PatchMatch)
- **NeRF (Neural Radiance Fields)** — implicit scene representation learned from posed images; enables novel view synthesis
- **3D Gaussian Splatting (3DGS)** — explicit scene representation using 3D Gaussians; faster than NeRF
- **Depth estimation** — monocular or stereo depth from single images or video
- **3D object detection** — localize and classify objects in 3D space (bounding boxes or meshes)
- **Mesh/point cloud generation** — generate 3D shapes from text or images (Point-E, DreamFusion, Zero123++)

## Key Methods

- **NeRF** — differentiable volumetric rendering; stores scene as MLF network
- **3DGS** — replaces neural rendering with explicit Gaussian primitives; real-time
- **Depth Anything v2** — monocular depth estimation foundation model
- **DUSt3R** — zero-shot 3D reconstruction from arbitrary image pairs

## Related Concepts

- [[computer-vision]] — the broader domain; 3D vision is a specialized sub-domain
- [[segmentation]] — 3D semantic segmentation extends segmentation to point clouds
- [[training-free]] — methods like DUSt3R operate zero-shot without task-specific training
