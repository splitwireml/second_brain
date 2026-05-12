---
title: Open WebUI
created: 2026-04-27
updated: 2026-04-27
type: entity
tags: [self-hosted, local-llm, agent, ui-design, open-source]
sources: [raw/transcripts/2026-04-27-julian-goldie-hermes-open-webui.md]
---

# Open WebUI

Self-hosted chat interface for local LLMs. Most popular open-source WebUI for Ollama. Provides a modern chat UI with file attachments, model switching, code preview, web search, and mobile access — as a front-end to agent backends like Hermes.

## Overview

Open WebUI functions as the front-end chat interface, while agent runtimes (Hermes, OpenClaw, custom APIs) act as the back-end reasoning and execution engine. The two connect via a shared API server + environment file, with the agent gateway routing requests.

## Key Capabilities

- **Chat interface** — ChatGPT-style UI for direct agent interaction (vs. terminal)
- **Model switching** — local (Ollama) + external API models; workspace section for model profiles with tags and system prompts
- **File attachments** — attach files, notes, knowledge bases; upload context for agents (Hermes terminal lacks this)
- **Code preview** — render and preview generated code artifacts inline
- **Web search + browsing** — integrated into chat context
- **Image generation integration** — generate/preview images inside the chat interface
- **Code interpreter** — execute code within chat sessions
- **Mobile support** — manage agents via mobile UI
- **Multi-account** — manage multiple agent profiles
- **Conversation management** — search, reference, and manage chat history
- **Docker deployment** — containerized, isolated setup
- **Open source** — MIT license

## Setup with Hermes Agent

1. Pull Open WebUI GitHub documentation
2. Paste setup instructions into Hermes terminal
3. Configure API server + environment file in Hermes
4. Run Open WebUI via Docker
5. Create account, point at Hermes gateway
6. Chat with Hermes through the web UI

## Why Use It Over Hermes Dashboard

The [[hermes-agent]] official dashboard is a mission-control UI (scheduled tasks, skills, sessions) but lacks direct chat. Open WebUI fills that gap with a ChatGPT-style experience: direct interaction, file uploads, model switching, workspace profiles, code preview, and mobile access.

## Compared to Alternatives

| Feature | Open WebUI | Hermes Dashboard | Paperclip/Multico |
|---|---|---|---|
| Chat interface | ✅ | ❌ | ✅ |
| File uploads | ✅ | ❌ | ✅ |
| Model switching | ✅ | ❌ | ✅ |
| Code preview | ✅ | ❌ | ✅ |
| Mission control | ❌ | ✅ | ✅ |
| Docker-native | ✅ | ❌ | ✅ |
| Open source | ✅ | ✅ | Partial |

## Relationships

- [[hermes-agent]] — backend agent; Open WebUI is the chat front-end
- [[openclaw]] — alternative backend agent Open WebUI can connect to
- Ollama — local model runtime Open WebUI runs on (no wiki page)
- [[paperclipai-paperclip]] — alternative "mission control" layer; Open WebUI is more specifically a chat interface than mission control
