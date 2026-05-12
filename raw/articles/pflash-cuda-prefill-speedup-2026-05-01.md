---
title: "PFlash: 10x prefill speedup over llama.cpp at 128K on a RTX 3090"
source: "x-bookmarks"
tweet_id: "2050213728298185029"
tweet_url: "https://x.com/pupposandro/status/2050213728298185029"
author_name: "Sandro"
author_handle: "@pupposandro"
tweet_date: "Fri May 01 14:00:18 +0000 2026"
bookmark_date: "2026-05-01"
content_type: "x_article"
character_count: 11481
retweet_count: 14
like_count: 133
external_urls:
  - "https://github.com/Luce-Org/lucebox-hub)"
  - "https://github.com/mit-han-lab/Block-Sparse-Attention)"
  - "https://github.com/qhfan/FlashPrefill))"
  - "https://github.com/mit-han-lab/Block-Sparse-Attention)'s"
  - "https://github.com/Luce-Org/lucebox-hub"
  - "https://arxiv.org/abs/2603.02631)"
  - "https://arxiv.org/abs/2502.02789)"
  - "https://arxiv.org/abs/2603.06199)"
  - "https://github.com/ggml-org/llama.cpp)"
  - "https://huggingface.co/Qwen/Qwen3-0.6B)"
  - "https://huggingface.co/Qwen/Qwen3.6-27B)"
---

# PFlash: 10x prefill speedup over llama.cpp at 128K on a RTX 3090

PFlash: 10x prefill speedup over llama.cpp at 128K on a RTX 3090

Co-author: @davideciffa

Speculative prefill for long-context decode on quantized 27B targets, C++/CUDA only. A small drafter loaded in-process scores token importance over the full prompt; the heavy target only prefills the spans that matter.

Source: [github.com/Luce-Org/lucebox-hub](https://github.com/Luce-Org/lucebox-hub) (open source, MIT).

Head-to-head on Qwen3.6-27B Q4_K_M, RTX 3090, single-shot: 24.8 s TTFT vs ~257 s for vanilla llama.cpp = ~10.4× at 128K (and 13.5 s vs 134.95 s = 10.0× at 64K), with NIAH retrieval preserved end-to-end. No Python, no Triton, no PyTorch in the inference loop.

## TL;DR

- Speculative prefill for long-context spec decode. Drafter (Qwen3-0.6B BF16) loaded in the same process as the target scores per-token importance via attention; target prefills only the top-scoring spans.

- Head-to-head single-shot on Qwen3.6-27B Q4_K_M / RTX 3090: 24.8 s TTFT vs ~257 s llama.cpp at 128K = ~10.4×; 13.5 s vs 134.95 s at 64K = 10.0×.

- Quality preserved end-to-end: NIAH single-needle retrieved at every tested context (32K → 128K), keep_ratio=0.05.

- Two algorithms stacked: Cross-Family Speculative Prefill (Liu et al / SambaNova ICLR 2026) for the scoring + selection, FlashPrefill (Fan et al, 2026) for the long-ctx drafter forward.

- C++/CUDA only. Drafter forward is a custom Qwen3-0.6B graph in ggml. FlashPrefill is 4 hand-written CUDA kernels (mean_K → score → select → sparse_fwd) plus BSA ([mit-han-lab/Block-Sparse-Attention](https://github.com/mit-han-lab/Block-Sparse-Attention), FA-2 derived sm_80+) for the sparse attention forward. No Python, Triton, or PyTorch at runtime.

## The problem

Q4_K_M Qwen3.6-27B running on a 24 GB RTX 3090 decodes fast (~74 tok/s with dflash spec decode) but the prefill stage scales O(S²): every doubling of source length quadruples the cost. On a 131,072-token prompt, vanilla llama.cpp takes 248.4 s cold on the same 3090 (measured llama-bench pp131072 --no-warmup -r 1, 527.6 tok/s). That's 4.1 minutes staring at a blank screen before the first token. The decode that follows is fast, but the wait kills the UX.

The shape is the issue, not just the magnitude. Same box, same model, same Q4_K_M GGUF, warmed steady-state across context sizes (each row is the throughput llama.cpp settles into after several calls at the same length):

Throughput (tok/s) drops as context grows because the per-token attention cost rises with sequence length. Cold-start (the first request after process boot, with empty caches) is worse: 248.4 s at 128K vs the 169.3 s warmed-steady-state shown above. Both are real, both matter. PFlash beats both by sidestepping the O(S²) entirely.

## Two algorithms, one pipeline

PFlash stacks two recent long-context techniques. They solve different problems and compose cleanly:

Speculative prefill (the scoring + selection layer)

From Liu et al's Speculative Prefill (arXiv 2502.02789) and SambaNova's Cross-Family Speculative Prefill (arXiv 2603.02631). Insight: a small draft model's attention pattern over a long prompt faithfully predicts which tokens matter for the answer. Run the draft, score per-token importance, keep the top spans, drop the rest. The target then prefills only the spans that matter, never the full 128 K.

Concretely, PFlash's drafter step (all in C++/CUDA, in-process):

1. Forward Qwen3-0.6B BF16 over the prompt via a custom ggml graph (qwen3_0p6b_loader.cpp + qwen3_0p6b_graph.cpp). The drafter sits in the same process and same ggml allocator as the 27B target; no libllama, no PyTorch.

2. Score blocks via the mean_K + score CUDA kernels: per-block mean of K, per-(Q-block, K-block) score, all on device. Alpha-threshold (DFLASH_FP_ALPHA, 0.85 default) selects which K-blocks each Q-block attends to.

3. Compress: select kernel rolls up block selections into per-token survival, the daemon emits the compressed token-id stream over its compress stdout protocol. keep_ratio=0.05 bottoms the survivor count at ~6.5 K at 128 K source.

Quality holds because cross-family draft attention transfers well across model families (verified upstream on RULER, LongBench, NIAH).

FlashPrefill in CUDA (the drafter accelerator)

From Fan et al's FlashPrefill (arXiv 2603.06199). Standard attention is O(S²); at 128 K with a 0.6 B drafter that's tens of seconds of pure attention compute. FlashPrefill is a block-sparse attention algorithm: per-query block, only attend to sink blocks + recent window + dynamic top-K blocks selected via mean-K block-score. Drops the drafter's attention from O(S²) to O(S × selected_blocks).

The reference open-source implementation ([qhfan/FlashPrefill](https://github.com/qhfan/FlashPrefill)) is Triton. For PFlash, we wrote a CUDA port: 4 kernels in flashprefill_kernels.cu (mean_K, score, select, sparse_fwd) and a BSA dispatcher in bsa_launcher.cu + bsa_fwd_inst.cu that targets [mit-han-lab/Block-Sparse-Attention](https://github.com/mit-han-lab/Block-Sparse-Attention)'s FA-2-derived sm_80+ kernel for the actual sparse forward. BSA was originally a PyTorch C++ extension; we wired it without libtorch via a 3-header ATen/c10 stub set under dflash/deps/bsa_stubs/.

The whole drafter forward + scoring at 128 K runs in roughly 12 s of CUDA work, same order as the Triton reference, with no autotune warmup, no Python interpreter, no ~/.triton/cache/ to ship.

Why the stack works

Speculative prefill solves the quality problem: how do you compress without losing the answer-relevant content? FlashPrefill solves a speed problem inside the speculative-prefill drafter step itself: how do you make the drafter fast enough at 128 K that it doesn't become the bottleneck. The two compose cleanly because the target side (dflash spec decode) is unchanged. It just receives a much shorter prompt with full attention enabled.

## Memory dance

The drafter (1.3 GB weights + KV + ~600 MB BSA scratch at 128 K) and the dflash daemon (15 GB target + 3 GB draft + 3 GB KV) don't both fit on 24 GB. The daemon exposes park/unpark/free drafter commands on its stdin protocol so target / draft / drafter weights cycle through VRAM cleanly:

```
# daemon stdin commands per request (all in one process)
park target           # free 15 GB
park draft            # free 3 GB
compress <ids.bin> <keep_x1000> <drafter.gguf>   # ~12 s at 128K, BSA path
free drafter          # release drafter weights + KV + BSA scratch
unpark target         # reload 15 GB (~1.3 s)
unpark draft          # reload 3 GB (~0.3 s)
generate <compressed_ids.bin> 800 <out.bin>       # spec decode, ~10 s
park draft            # back to idle
```

The park/unpark/free dance costs ~3 s per request but unlocks the algorithm on commodity hardware. No Python interpreter ever holds VRAM, so there's no torch caching allocator to flush, no Triton driver scratch to release.

## Head-to-head numbers

Same machine (RTX 3090, 24 GB), same Q4_K_M GGUF target, single-shot. Daemon run with DFLASH_FP_USE_BSA=1 DFLASH_FP_ALPHA=0.85 and keep_ratio=0.05. NIAH single-needle (magic-key + 7-digit answer randomly placed in filler) used as the end-to-end retrieval check.

Speedup grows with context because llama.cpp prefill is O(S²) while dflash compresses to a near-constant-sized survivor set (~3 K at 64 K, ~6.5 K at 128 K with keep_ratio=0.05) before the target ever sees the prompt. Target-side prefill cost is roughly fixed regardless of source length.

Decode after the prefill is the standard dflash spec-decode path with DDTree: ~74 tok/s sustained on Qwen3.6-27B Q4_K_M with the matched z-lab draft.

## Quality

Speculative prefill only matters if the speedup doesn't cost retrieval quality. NIAH single-needle, keep_ratio=0.05, DFLASH_FP_ALPHA=0.85:

DFLASH_FP_ALPHA trades scoring strictness against latency: 0.85 is the bench setting; 0.99 cuts another second at 128 K with a small NIAH-margin loss. Quality holds across this range because cross-family draft attention transfers well across model families (verified upstream on RULER, LongBench, NIAH).

## Architecture sketch

## Bottleneck shifted

At 128 K, drafter scoring is the dominant cost (~12 s of the 24.8 s TTFT). Target prefill on the compressed ~6.5 K survivors is ~10 s; the remaining ~3 s is the park/unpark/free dance. To push the speedup further:

- Smaller drafter. Qwen3-0.6B is the smallest pure-transformer in the family. Distillation or BM25-style scorers could halve drafter time at some quality cost.

- Drafter on a separate GPU. Removes the park/unpark round-trip entirely. Not an option on a single 3090.

- Tighter DFLASH_FP_ALPHA. Bumping from 0.85 → 0.99 cuts ~1 s at 128 K with a small NIAH-margin loss.

- Tighter keep_ratio. 0.05 → 0.02 cuts target prefill from ~10 s to ~3 s, but drops the survivor count under the Q4 target's working window and starts losing the needle. Calibration territory.

## Reproduce

```
# clone with submodules (pulls llama.cpp/ggml + Block-Sparse-Attention)
git clone --recurse-submodules https://github.com/Luce-Org/lucebox-hub
cd lucebox-hub/dflash

# build dflash + BSA kernel (sm_80+, ~10 min cold compile pulls cutlass)
cmake -B build -S . -DCMAKE_BUILD_TYPE=Release \
                    -DCMAKE_CUDA_ARCHITECTURES=86 \
                    -DDFLASH27B_ENABLE_BSA=ON
cmake --build build --target test_dflash test_flashprefill_kernels -j

# fetch weights (target + drafter + spec-decode draft)
huggingface-cli download unsloth/Qwen3.6-27B-GGUF Qwen3.6-27B-Q4_K_M.gguf --local-dir models/
huggingface-cli download Qwen/Qwen3-0.6B model.safetensors tokenizer.json --local-dir models/drafter/
huggingface-cli download z-lab/Qwen3.5-27B-DFlash model.safetensors --local-dir models/draft/

# run the daemon + bench harness
cd ../pflash && pip install -e . && python tests/niah_gen.py --n 1 --ctx 131072 --out /tmp/niah_128k.jsonl
python tests/bench_niah_cpp.py \
  --bin    ../dflash/build/test_dflash \
  --target ../dflash/models/Qwen3.6-27B-Q4_K_M.gguf \
  --draft  ../dflash/models/draft/model.safetensors \
  --drafter-gguf ../dflash/models/drafter/qwen3-0.6b.gguf \
  --cases /tmp/niah_128k.jsonl --keep-ratio 0.05
```

## Tuning

Daemon-side env vars (full list in dflash/src/flashprefill.h):

```
DFLASH_FP_USE_BSA=1       # dispatch sparse FA forward through BSA (sm_80+, required for 10× number)
DFLASH_FP_ALPHA=0.85       # block-selection threshold; higher = stricter = fewer K-blocks per Q-row
DFLASH_FP_PROFILE=1         # log per-stage timings (mean_K / score / select / forward)
```

Implementation lives in lucebox-hub/dflash/; the bench harness in lucebox-hub/pflash/. Numbers from tests/bench_niah_cpp.py, NIAH single-needle, RTX 3090 Ampere sm_86, Qwen3.6-27B Q4_K_M target, Qwen3-0.6B drafter, q4_0 KV, DFLASH_FP_USE_BSA=1 DFLASH_FP_ALPHA=0.85 keep_ratio=0.05.

## Related

- [DFlash on ggml](https://www.lucebox.com/blog/dflash27b): the C++ speculative-decoding daemon PFlash sits in front of. 207 tok/s Qwen3.5-27B on a single RTX 3090.

- Algorithm references: [Cross-Family Speculative Prefill](https://arxiv.org/abs/2603.02631) (SambaNova, ICLR 2026), [Speculative Prefill](https://arxiv.org/abs/2502.02789) (Liu et al, 2025).

- Sparse attention: [FlashPrefill](https://arxiv.org/abs/2603.06199) (Fan et al, 2026).

- Upstream tools: [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp), [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) (drafter), [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) (target).
