---
title: "69 Best Open-Source AI Repositories (April 2026)"
created: "2026-04-28"
updated: "2026-04-28"
type: concept
tags: [oss-ai, inference, rag, ai-agent, fine-tuning, deployment, data-prep, vision, multimodal, tooling]
sources: [raw/articles/seelffff-69-best-open-source-ai-repos-2049214021430325677.md]
---

# 69 Best Open-Source AI Repositories (April 2026)

A curated list of 69 production-ready, actively maintained open-source AI repositories published by [[seelffff]] in April 2026. The list covers the full AI stack: inference, RAG, agents, fine-tuning, deployment, data prep, and vision.

## Overview

The central thesis: "the average AI startup pays $8,000–$50,000/year in tool subscriptions" while "the people actually building AI — researchers, engineers, indie hackers — use open-source." The list was compiled from 300+ repositories.

The curation is organized into 10 categories covering the end-to-end AI development lifecycle.

## Categories

### 01 LLM Inference

| # | Project | Stars | Notes |
|---|---------|-------|-------|
| 01 | [[ollama]] | 98K | Local LLM runner; `ollama run llama3` |
| 02 | [[llama-cpp]] | 72K | C++ inference engine; CPU/GPU/Apple Silicon |
| 03 | [[vllm]] | 44K | High-throughput serving; PagedAttention |
| 04 | lmstudio | 28K | Desktop local LLM app; OpenAI-compatible server |
| 05 | jan | 26K | 100% offline ChatGPT alternative |
| 06 | text-generation-webui | 42K | Most feature-complete local LLM UI |
| 07 | localai | 26K | Self-hosted OpenAI drop-in replacement |

### 02 RAG & Knowledge

| # | Project | Stars | Notes |
|---|---------|-------|-------|
| 08 | langchain | 98K | Most popular LLM framework |
| 09 | llamaindex | 38K | Data framework for LLM apps; better than LangChain for pure RAG |
| 10 | rag-anything | 12K | Multimodal RAG for text, tables, images, charts, graphs |
| 11 | chroma | 16K | Open-source vector database |
| 12 | weaviate | 12K | Vector DB with built-in ML models; hybrid search |
| 13 | haystack | 18K | End-to-end NLP RAG framework |
| 14 | docling | 22K | IBM Research; PDF → structured markdown with tables/figures/formulas |

### 03 AI Agents

| # | Project | Stars | Notes |
|---|---------|-------|-------|
| 15 | [[autogen]] (Microsoft) | 40K | Multi-agent conversation framework |
| 16 | crewai | 28K | Role-playing AI agents; crew collaboration |
| 17 | langgraph | 10K | Stateful multi-agent workflows as graphs |
| 18 | agno | 22K | Multi-modal AI agents; 10× faster than LangChain |
| 19 | smolagents | 14K | Hugging Face minimal code agents |
| 20 | openhands | 48K | Open-source Devin alternative; coding agent |
| 21 | superagi | 16K | Self-hosted autonomous agent infrastructure |

### 04 Prompts & Evals

| # | Project | Stars | Notes |
|---|---------|-------|-------|
| 29 | [[dspy]] | 22K | Stanford; programming not prompting; prompt optimization |
| 30 | guidance | 20K | Control LLM output structure; force JSON schemas |
| 31 | outlines | 11K | Structured text generation; zero prompt engineering |
| 32 | promptfoo | 6K | Prompt testing and eval; like unit tests for AI |
| 33 | braintrust | 3K | Eval framework for LLM apps |
| 34 | instructor | 9K | Structured outputs via Pydantic |

### 05 Fine-tuning

| # | Project | Stars | Notes |
|---|---------|-------|-------|
| 35 | [[unsloth]] | 24K | 2× faster, 80% less memory; single GPU |
| 36 | axolotl | 8K | Streamlined fine-tuning; YAML config |
| 37 | llama-factory | 40K | Fine-tune 100+ LLMs via web UI; LORA/QLORA |
| 38 | trl | 12K | Hugging Face; RLHF/DPO/PPO |
| 39 | torchtune | 5K | PyTorch-native fine-tuning by Meta |
| 40 | mergekit | 4K | Merge fine-tuned models; SLERP, DARE, linear merge |

### 06 Tools & Context

| # | Project | Stars | Notes |
|---|---------|-------|-------|
| 41 | markitdown | 38K | Microsoft; convert any file to markdown |
| 42 | files-to-prompt | 3K | Simon Willison; codebase → prompt |
| 43 | crawl4ai | 30K | Web scraping for AI; clean markdown extraction |
| 44 | [[firecrawl]] | 25K | Full site → LLM-ready data |
| 45 | playwright-mcp | 31K | MCP server giving Claude a real browser |
| 46 | model-context-protocol | 11K | Anthropic's MCP standard |
| 47 | awesome-mcp-servers | 27K | 500+ MCP servers catalog |
| 48 | n8n | 47K | Self-hosted workflow automation; 400+ integrations; replaces Zapier |

### 07 Deployment

| # | Project | Stars | Notes |
|---|---------|-------|-------|
| 49 | litellm | 16K | One API for 100+ LLMs |
| 50 | bentoml | 7K | Build and deploy AI services |
| 51 | ray | 34K | Distributed AI inference at scale |
| 52 | triton | 8K | NVIDIA's production inference server |
| 53 | lorax | 3K | Serve hundreds of LoRA adapters on one GPU |
| 54 | supabase | 73K | Open-source Firebase alternative; Postgres + vector search |

### 08 Claude-Specific

| # | Project | Stars | Notes |
|---|---------|-------|-------|
| 55 | obra/superpowers | 160K | Claude Code enhancement; 160K stars |
| 56 | claude-code-skills | official | Anthropic's official skills framework |
| 57 | free-claude-code | 2K | Run Claude Code free via GitHub Models API |
| 58 | claude-mem | 1K | Persistent memory for Claude across sessions |

### 09 Data Prep

| # | Project | Stars | Notes |
|---|---------|-------|-------|
| 59 | unstructured | 10K | Extract/unstructured data for LLMs |
| 60 | datatrove | 3K | Hugging Face; large-scale data processing |
| 61 | trafilatura | 3K | Web content extraction for AI |
| 62 | semchunk | 1K | Semantic text chunking for RAG |
| 63 | datachain | 2K | Iterative; AI-native dataset management |

### 10 Vision & Multimodal

| # | Project | Stars | Notes |
|---|---------|-------|-------|
| 64 | moondream | 10K | 1.6B vision language model; runs on Raspberry Pi |
| 65 | internvl | 7K | State-of-the-art open-source vision model; matches GPT-4V |
| 66 | whisper | 74K | OpenAI speech recognition; 99 languages |
| 67 | insanely-fast-whisper | 8K | Whisper 10-20× faster |
| 68 | stable-diffusion-webui | 143K | AUTOMATIC1111; browser UI for Stable Diffusion |

### Bonus

| # | Project | Notes |
|---|---------|-------|
| 69 | kreo | Copy top Polymarket traders; Telegram bot |

## Source

- Author: [[seelffff]] (@seelffff)
- Tweet: [x.com/seelffff/status/2049214021430325677](https://x.com/seelffff/status/2049214021430325677)
- Date: April 28, 2026
- Engagement: 574 likes, 58 RTs, 16 replies

## Related Concepts

- [[open-source-ai-stack]] — broader concept of open-source AI infrastructure
- [[inference]] — LLM serving and inference optimization
- [[rag]] — retrieval-augmented generation
- [[ai-agent]] — autonomous AI agent frameworks
- [[fine-tuning]] — model adaptation techniques
- [[deployment]] — serving and scaling AI models
