---
title: "Anthropic Prompt Engineering Best Practices — Car Insurance Form Demo"
created: 2026-05-01
updated: 2026-05-01
type: concept
tags: [prompt-engineering, claude-code, anthropic, system-prompt-design, xml-tags, few-shot-prompting, pre-fill, extended-thinking, production-llm]
sources: [raw/transcripts/2026-05-01-claude-code-hidden-features-sairahul1.md, raw/assets/2026-05-01-claude-code-hidden-features-sairahul1.mp3]
related_entity: [[anthropic]]
---

# Anthropic Prompt Engineering Best Practices — Car Insurance Form Demo

## Overview

A 24-minute Anthropic Applied AI team demo (Hannah + Christian) walking through a real-world prompt engineering scenario: building a Swedish car insurance claim assessment system using Claude 4 Sonnet. The demo iterates from a naive prompt ("skiing accident" hallucination) to a production-grade system prompt with structured XML output.

## The Scenario

- **Domain**: Swedish car insurance claims processing
- **Inputs**: (1) Swedish accident report form (17 checkboxes, 2 vehicles), (2) human-drawn sketch of the incident
- **Output**: Determination of which vehicle is at fault, with confidence level
- **Model**: Claude 4 Sonnet, temperature=0, high max_tokens

## Prompt Engineering Iterations

### V1 — Naive Prompt (Baseline)
- Simple task description: "review accident report form, determine what happened, who's at fault"
- **Result**: Claude hallucinated a "skiing accident on Chapangatan" — completely wrong domain
- **Lesson**: Without context, Claude guesses. The guess was plausible (Swedish street name) but entirely incorrect.

### V2 — Task + Tone Context
- Added: AI system helping a human claims adjuster, reviewing car accident forms in Swedish
- Added: tone instruction — stay factual, stay confident, do not guess
- **Result**: Claude correctly identified car accident domain, read checkboxes (Vehicle A: box 1, Vehicle B: box 12), but was **unconfident** about fault determination
- **Lesson**: Context fixes domain errors, but doesn't provide enough structure for confident reasoning

### V3 — Background Detail in System Prompt
- Added comprehensive form structure to system prompt:
  - Form title, two columns (Vehicle A / Vehicle B), 17 rows with meanings
  - Human marking variations (circles, scribbles, not just X's)
  - Form purpose and interpretation guidelines
- **Result**: Claude spent less time narrating form structure, became **confident** — declared Vehicle B at fault
- **Lesson**: Static background knowledge belongs in the system prompt. Also ideal for prompt caching.

### V4 — Step-by-Step Reasoning Instructions
- Added detailed task list in user prompt:
  1. Examine form carefully (each checkbox)
  2. Make a list of what's checked
  3. Then examine sketch, keeping form understanding in mind
  4. Match sketch to form data
  5. Arrive at final assessment
- **Result**: Claude showed its work — listed every checkbox checked/unchecked. Still correct on Vehicle B at fault.
- **Lesson**: Order of analysis matters. Form first → sketch second, not the reverse. Step-by-step instructions improve reasoning traceability.

### V5 — Output Formatting + Guidelines Reminder
- Added: importance guidelines (clear, concise, accurate)
- Added: output formatting — wrap final verdict in `<final_verdict>` XML tags
- **Result**: Succinct output with structured XML tag containing the verdict
- **Lesson**: XML tags enable reliable downstream parsing (e.g., into SQL database). Separates reasoning from actionable output.

## Key Techniques Demonstrated

### 1. Prompt Structure (Recommended Template)
```
[Task Description]     — role, what to do
[Content]                — dynamic inputs (images, forms, sketches)
[Detailed Instructions]  — step-by-step reasoning
[Examples]               — few-shot examples for edge cases
[Reminder/Guidelines]    — repeat critical constraints at the end
```

### 2. XML Tags for Structure
- Claude is fine-tuned on XML tag structure
- Tags help Claude refer back to information: `<user_preferences>`, `<final_verdict>`
- Enables reliable programmatic parsing of outputs

### 3. Pre-filled Responses ("Putting Words in Claude's Mouth")
- Start Claude's output with a specific format: e.g., `[` for JSON, `<final_verdict>` for XML
- Shapes output structure without preamble
- Useful for structured JSON/XML responses in production pipelines

### 4. Extended Thinking (Claude 3.7 / Claude 4)
- Enable extended thinking for complex reasoning tasks
- Claude generates `<thinking>` tags with scratch-pad reasoning
- **Meta-use**: Analyze the thinking transcript to understand how Claude processes data, then bake those insights back into the system prompt
- More token-efficient than letting Claude narrate every step in the final output

### 5. Few-Shot Examples in System Prompt
- Bake difficult/edge-case examples into the system prompt
- Include: visual input (base64 image) + expected breakdown + correct conclusion
- Iterative empirical science: identify failure modes → add examples → test

### 6. Conversation History (for User-Facing Apps)
- For conversational applications, include relevant conversation history in system prompt
- Enriches context for multi-turn interactions
- Not used in this batch-processing demo but highlighted as a best practice

## Production Takeaways

| Iteration | What Was Added | Problem Solved |
|-----------|---------------|----------------|
| V1 | Basic task description | Baseline — wrong domain entirely |
| V2 | Task + tone context | Fixed domain hallucination |
| V3 | Form structure in system prompt | Enabled confident fault determination |
| V4 | Step-by-step reasoning order | Improved traceability, correct analysis sequence |
| V5 | XML output formatting + guidelines | Structured, parseable, production-ready output |

## Related Concepts

- [[prompt-engineering-patterns]] — 10 high-impact prompt templates
- [[claude-code-systems-design]] — Shift from prompt-based to system-design-based Claude Code usage
- [[karpathy-claude-md]] — Four-principle CLAUDE.md behavioral config
- [[vibe-coding-in-production]] — Eric Mishra's framework for responsible vibe coding

## Related Entities

- [[anthropic]] — AI company behind Claude
- [[claude-code]] — Anthropic's CLI coding agent
- [[eric-mishra]] — Anthropic researcher on vibe coding in production

## Sources

- `raw/transcripts/2026-05-01-claude-code-hidden-features-sairahul1.md` — Full VibeVoice ASR transcript (7,442 tokens, 24 min)
- `raw/assets/2026-05-01-claude-code-hidden-features-sairahul1.mp3` — Audio file (17MB, MP3)
