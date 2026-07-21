---
title: eComrads MCP
created: 2026-07-21
updated: 2026-07-21
type: entity
tags: [product, mcp, ai-tools, video-generation, ai-ugc]
sources: [raw/articles/14-second-ai-vlog-method.md]
confidence: low
contested: true
---

# eComrads MCP

## Overview

The supplied source describes eComrads MCP as a custom [[mcp]] connector for [[claude]] that turns plain-English instructions into downstream video-generation requests. It gives the endpoint `https://mcp.ecomrads.com/mcp` and presents eComrads as the connector layer in a workflow using [[seedance-2-0]]. ^[raw/articles/14-second-ai-vlog-method.md]

## Source-described role

- Add the endpoint once in Claude's custom connectors settings.
- Describe scenes, character details, and spoken lines in natural language.
- Generate one scene at a time, inspect it, then continue to the next scene.
- Assemble the approved clips into a short vertical or wide export.

## Evidence boundary

**Confirmed:** the raw user-provided source contains the endpoint and the described connector workflow.

**Unverified:** whether the endpoint is currently live, its authentication and pricing, the service's actual model routing, whether it renders Seedance 2.0, and the claimed 4K output. No external validation was performed during this ingest.

## Related

- [[claude]] — agent interface named by the source
- [[seedance-2-0]] — video model named as the rendering layer
- [[14-second-ai-vlog-method]] — workflow that uses the connector
- [[video-generation]] — broader technical context
