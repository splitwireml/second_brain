---
title: paper.design - research
created: 2026-04-21
type: raw
source: web/paper.design
---

# paper.design Research Sources

## Pages Consulted
- https://paper.design (homepage)
- https://paper.design/docs/mcp (MCP documentation)
- https://paper.design/blog (blog listing)
- https://paper.design/blog/a-real-space-to-design-in-the-age-of-agents (key blog post)
- https://paper.design/blog/seed (seed round announcement)
- https://paper.design/compare/pencil (Paper vs Pencil comparison)
- https://paper.design/pricing (pricing page)
- https://paper.design/roadmap (roadmap page)

## Key Findings

### What is Paper.design
- Canvas-based design tool (Figma-like UI) built on real HTML/CSS internals
- Design file IS the DOM — no translation layer
- Desktop app (macOS/Windows) + web app
- Local MCP server at http://127.0.0.1:29979/mcp
- AI agents connect via MCP to read/write designs
- Supported: Cursor, Claude Code, Codex, Copilot, OpenCode
- $4.2M seed round (Accel + Basecase, Feb 2025)
- Founders: Stephen Haney, Vlad Moroz, Ksenia Kondrashova
- Pricing: Free (100/week MCP calls), Pro $20/mo (1M/week)

### MCP Tools
- get_basic_info, get_selection, get_node_info, get_children, get_tree_summary
- get_screenshot, get_jsx (export to React/Tailwind or inline-styles)
- get_computed_styles, get_fill_image, get_font_family_info
- write_html (inject/replace nodes in canvas)
- set_text_content, rename_nodes, duplicate_nodes
- update_styles, delete_nodes
- create_artboard, find_placement
- start_working_on_nodes, finish_working_on_nodes

### Blog Post Key Quotes (Feb 27, 2026)
"A real space to design in the age of agents"
- "Agents are shipping faster than we can think so we need a space to zoom out more than ever."
- "The canvas must evolve to embrace the new paradigm."
- "The buzz is that execution is becoming purely conversational: you describe a thing, an agent writes the code, and hands you something cool."
- "Agents can probably help a lot, especially with connectivity and repetitive tasks. But if you're a designer who thinks AI will design for you, you're a little fucked."
- "You can't scale design decisions in a chat box."
- "We needed to rethink the foundations and finally build something that exports code, imports React components, fetches APIs and lets you iterate quickly."
- "The canvas needs to be made of the same material as the product."
- "This is the part that changes the whole dynamic: it goes both ways."

### Pricing Details
- Free: 100/week MCP tool calls, limited image generation, 25MB max image size, limited collaboration
- Pro: $20/mo ($16/user/month yearly), 1M/week MCP tool calls, 100x more image gen/day, video export, 100MB max, unlimited collaboration, priority feedback
- Organizations: Everything in Pro + SAML/SSO, admin controls, custom contracts, dedicated support, priority onboarding

### Paper vs Pencil (from Paper's compare page)
Paper: Real HTML/CSS canvas — web-native, no translation step. Agents read and write same language they were trained on. Web and desktop app.
Pencil: WebGL canvas, .pen JSON format — requires translation to HTML/CSS. Desktop app + IDE extension. Local, single-user.

### Roadmap Highlights
- In progress: CSS Grid, Native Tailwind CSS integration (partnered with Tailwind team), Fetch live data (MCP from APIs/Google Sheets), Host assets from Paper as CDN
- Planned: Components with slots (props/slots, aligned with code), Themes and tokens, Full sharing permissions, Pen tool + vector editing, Icon packs + shadcn
- Canvas-aware agent assistant, Right click → Remix, Generate videos, Three.js islands, Particle system

### Community Quotes
- Jeff Buzulencia: "sooo up until a couple of weeks ago i was still designing manually and then building with Claude Code. i might be ocd about the design process. buuuuut I started using @paper with their MCP annd 🤯"
- Yahya: "Paper & claude code is the perfect combo to ship custom web stuff."
- Jordan Singer: "if you're building software meant to be consumed by humans, take the time to actually design it. AI has a design smell because it's 'designing' via code. we can tell!"
- Steve Ruiz: "If you're a designer then you should be racing to get as close to the product as possible so that you can experience your design decisions as you make them"
