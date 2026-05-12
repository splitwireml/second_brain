---
title: "unsloth/Qwen-Image-Layered-GGUF"
created: 2026-04-23
updated: 2026-04-23
type: raw
tags: [raw, model, gguf, quantization]
sources: []
---

# unsloth/Qwen-Image-Layered-GGUF

> [!NOTE]
> This is a GGUF quantized version of [Qwen-Image-Layered](https://huggingface.co/Qwen/Qwen-Image-Layered).
> unsloth/Qwen-Image-Layered-GGUF uses [Unsloth Dynamic 2.0](https://docs.unsloth.ai/basics/unsloth-dynamic-2.0-ggufs) methodology for SOTA performance. Important layers are upcasted to higher precision.

## Metadata

- **Model ID**: unsloth/Qwen-Image-Layered-GGUF
- **Base Model**: Qwen/Qwen-Image-Layered
- **Architecture**: qwen_image
- **Total GGUF Size**: ~20.4 GB
- **Pipeline**: image-text-to-image
- **License**: Apache 2.0
- **Library**: ggml
- **Downloads**: 2,278
- **Likes**: 48
- **Created**: 2025-12-19
- **Last Modified**: 2026-01-09

## Available GGUF Quantizations

| File | Size | SHA256 |
|------|------|--------|
| qwen-image-layered-Q4_0.gguf | 11,852,786,304 | 913050097e04... |
| qwen-image-layered-Q4_1.gguf | 12,843,690,624 | 95e34d46b79c... |
| qwen-image-layered-Q4_K_M.gguf | 13,244,770,944 | e6a107938afd... |
| qwen-image-layered-Q4_K_S.gguf | 12,410,759,808 | 10b3dd85d4c1... |
| qwen-image-layered-Q5_0.gguf | 14,400,825,984 | 88a014556b18... |
| qwen-image-layered-Q5_1.gguf | 15,391,730,304 | 3c41666d8f79... |
| qwen-image-layered-Q5_K_M.gguf | 15,027,513,984 | e2b0bf2a003e... |
| qwen-image-layered-Q5_K_S.gguf | 14,325,623,424 | cb4a7026a1f0... |
| qwen-image-layered-Q6_K.gguf | 16,852,429,440 | 9008bd45e691... |
| qwen-image-layered-Q8_0.gguf | 21,761,829,504 | 0d9f3cc357f8... |

## Unsloth Dynamic 2.0

Unsloth Dynamic 2.0 is Unsloth's quantization methodology for GGUF models. Key claim: important layers are upcasted to higher precision for SOTA performance. See [Unsloth Dynamic 2.0 documentation](https://docs.unsloth.ai/basics/unsloth-dynamic-2.0-ggufs).

## Base Model: Qwen-Image-Layered

Qwen-Image-Layered decomposes an image into multiple RGBA layers, enabling independent editing of each layer.

### Key Capabilities

- **Layered decomposition**: Any image → N RGBA layers (variable N, e.g. 3, 4, 8)
- **Inherent editability**: Edit one layer without affecting others
- **Elementary operations**: Resize, reposition, recolor objects cleanly
- **Recursive decomposition**: Any layer can itself be further decomposed
- **Consistency**: Edits preserve consistency across the full image

### Technical Details

- **Framework**: Diffusers (transformers >= 4.51.3 supporting Qwen2.5-VL)
- **Pipeline**: `QwenImageLayeredPipeline`
- **Recommended resolution**: 640 or 1024
- **Default layers**: 4
- **CFG scale**: 4.0 (with cfg_normalize=True)
- **Inference steps**: 50
- **Language**: Bilingual (English + Chinese)

### Author / Citation

```bibtex
@misc{yin2025qwenimagelayered,
      title={Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition},
      author={Shengming Yin, Zekai Zhang, Zecheng Tang, Kaiyuan Gao, Xiao Xu, Kun Yan, Jiahao Li, Yilei Chen, Yuxiang Chen, Heung-Yeung Shum, Lionel M. Ni, Jingren Zhou, Junyang Lin, Chenfei Wu},
      year={2025},
      eprint={2512.15603},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2512.15603},
}
```

## Links

- [HuggingFace Model Card](https://huggingface.co/unsloth/Qwen-Image-Layered-GGUF)
- [Base Model](https://huggingface.co/Qwen/Qwen-Image-Layered)
- [Research Paper (arXiv:2512.15603)](https://arxiv.org/abs/2512.15603)
- [Official Blog](https://qwenlm.github.io/blog/qwen-image-layered/)
- [ModelScope](https://modelscope.cn/models/Qwen/Qwen-Image-Layered)
- [Demo Space](https://huggingface.co/spaces/Qwen/Qwen-Image-Layered)
- [Unsloth GitHub](https://github.com/unslothai/unsloth/)
- [Unsloth Discord](https://discord.gg/unsloth)
