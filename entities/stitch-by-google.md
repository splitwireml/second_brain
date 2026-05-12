---
title: Stitch by Google
created: 2026-04-24
updated: 2026-04-24
type: entity
tags: [ai-tool, design-tool, ai-design, google, ai-agents]
sources:
  - raw/transcripts/2026-04-24-Stitch-by-Google.md
  - raw/articles/github-google-labs-code-design.md-2026-04-24.md
url: https://github.com/google-labs-code/stitch
related_entity: [[google-labs-code-design]]
---

# Stitch by Google

An AI coding agent by Google Labs that reads a [[google-labs-code-design]] file to understand a project's visual identity and generate code that respects it.

## Overview

Stitch is a Google Labs agent that consumes [[google-labs-code-design]] files — structured design system specifications — to produce design-consistent code. When Stitch generates a new design for a project, it reads the DESIGN.md to understand color roles, typography rules, and component structures before making design decisions.

## Key Claims from Video

- **DesignMD as agent-context file**: Stitch reads [[google-labs-code-design]] at generation time to obtain color roles (e.g., "primary ink for headlines"), typography rationale, and component rules
- **Token = named decision, not just a variable**: A design token like `primary` is described as a named *role* in the design system, not merely a variable. The hex value is one possible fill of that role
- **Specification open-sourced**: Google Labs published the first draft of the [[google-labs-code-design]] format specification on GitHub, enabling any tool to consume or generate DesignMD files
- **Components section (work in progress)**: A new `components` section allows tokens to reference other tokens (e.g., `button-primary.background` references `tertiary` token), enabling token composition
- **CLI for self-validation**: The new `npx @google/design.md lint` CLI lets agents validate their own changes against the spec and catch WCAG contrast errors
- **Agent → lint → agent loop**: The spec enables a workflow where an agent edits a DesignMD, then validates the output with the CLI, then corrects if needed

## Relationship to design.md

Stitch is the primary consumer and generator of [[google-labs-code-design]] files. The announcement video marks the open-sourcing of the [[google-labs-code-design]] format specification as a standalone standard — no longer tied exclusively to Stitch.

## See Also

- [[google-labs-code-design]] — the format specification that Stitch consumes and that is now open-sourced
- [[html-native-design-skill]] — HTML-native design skill pattern for AI coding agents; [[huashu-design]] as canonical implementation; complementary design-to-agent workflow
