---
title: withoutbg
created: 2026-05-10
updated: 2026-05-10
type: entity
tags: [ai-tool, background-removal, onnx, computer-vision]
sources: []
---

# withoutbg

Background removal service and ONNX-based pipeline. "Focus" is their flagship model optimized for hair and fur edge quality — the highest quality option for general background removal, at the cost of requiring Docker/PyPI rather than running natively on Apple Silicon.

## Relationship to Apple Silicon

withoutbg Focus uses an ONNX pipeline and runs on Apple Silicon via arm64 Docker + PyPI, not natively via MLX. For native MLX options, see [[u2net-mlx]] (smallest), [[sam3-image]] (most capable), or [[birefnet]] (best open license).

## See Also

- [[apple-silicon-background-removal-models-comparison]] — comparison including withoutbg
- [[birefnet]] — MIT-licensed alternative
- [[u2net-mlx]] — native MLX alternative
