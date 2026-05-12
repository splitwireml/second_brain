---
title: "Using Claude Code: The Unreasonable Effectiveness of HTML"
author: "Thariq" (@trq212)
authorId: "352806502"
createdAt: "Fri May 08 17:56:30 +0000 2026"
type: x-article
tags: [claude-code, html, ai, productivity, workflow, artifacts]
platform: X
id: "2052809885763747935"
likes: 10230
retweets: 1191
replies: 670
url: https://x.com/i/status/2052809885763747935
---
# Using Claude Code: The Unreasonable Effectiveness of HTML

Markdown has become the dominant file format used by agents to communicate with us. It's simple, portable, has some rich text capability and is easy for you to edit.

But as agents have become more and more powerful, I have felt that markdown has become a restricting format. I find it difficult to read a markdown file of more than a hundred lines. I want richer visualizations, color and diagrams and I want to be able to share them easily.

I've started preferring HTML as an output format instead of Markdown and increasingly see this being used by others on the Claude Code team.

## Why HTML?

### Information Density

HTML can convey much richer information compared to markdown:
- Tabular data using tables
- Design data with CSS
- Illustrations with SVG
- Code snippets with script tags
- Interactions using HTML elements with javascript + CSS
- Workflows using SVG and HTML
- Spatial data using absolute positions and canvases
- Images using image tags

### Visual Clarity & Ease of Reading

HTML documents are much easier to read. Claude can organize the structure visually to be ideal to navigate with tabs, illustrations, links, etc. It can even be mobile responsive.

### Ease of Sharing

Markdown files are fairly hard to share since most browsers do not render them natively well. With HTML, as long as you upload the file (for example to S3), you can share the link easily.

### Two-way Interaction

HTML can allow you to interact with the document. You might want to ask it to add sliders or knobs to adjust a design or allow you to tweak different options in the algorithm to see what happens. You can also ask it to let you copy these changes into a prompt to paste back into Claude Code.

### Data Ingestion

One of the biggest reasons to use Claude Code to make HTML files instead of ClaudeAI or Claude Design is all the context Claude Code can ingest. When writing this article, I asked Claude Code to read through my code folder and find all the HTML files I've generated, group and categorize them and then make an HTML file with all diagrams representing each type.

## Use Cases

### Specs, Planning & Exploration

HTML is a rich canvas for Claude to dive into a problem. When I start working on a problem instead of a simple markdown plan I expect to make a web of HTML files.

Example prompts:
- "Generate 6 distinctly different approaches — vary layout, tone, and density — and lay them out as a single HTML file in a grid so I can compare them side by side."
- "Create a thorough implementation plan in a HTML file, be sure to make some mockups, show data flow and add important code snippets."

### Code Review & Understanding

Code can be difficult to read in a Markdown file. With HTML we can render diffs, annotations, flowcharts, modules, etc.

Example prompt:
- "Help me review this PR by creating an HTML artifact that describes it. I'm not very familiar with the streaming/backpressure logic so focus on that."

### Design & Prototypes

Claude Design is based on HTML because HTML is incredibly expressive at design, even if your end surface is not HTML. You can also prototype interactions, such as animations, actions, etc.

Example prompt:
- "I want to prototype a new checkout button, when clicked it does a play animation and then turns purple quickly. Create a HTML file with several sliders and options for me to try different options on this animation, give me a copy button to copy the parameters that worked well."

### Reports, Research & Learning

Claude Code is incredibly good at synthesizing information across multiple data sources. You could assemble this in the form of a long HTML document, an interactive explainer or even a slideshow/deck.

Example prompt:
- "I don't understand how our rate limiter actually works. Read the relevant code and produce a single HTML explainer page: a diagram of the token-bucket flow, the 3–4 key code snippets annotated, and a 'gotchas' section."

### Custom Editing Interfaces

Ask Claude to build a throwaway editor for the exact thing I'm working on. Not a product, or a reusable tool, but a single HTML file, purpose-built for this one piece of data.

Example prompts:
- "I need to reprioritize these 30 Linear tickets. Make me an HTML file with each ticket as a draggable card across Now / Next / Later / Cut columns."
- "Here's our feature flag config. Build a form-based editor for it."

## FAQ

**Isn't it less token efficient?** While markdown often uses fewer tokens, the added expressiveness of HTML and the much higher likelihood of me reading it means I get overall better output. With the 1MM context window in Opus 4.7, the increased token usage is not really noticeable.

**When do you use markdown?** I have honestly stopped using markdown altogether for almost everything.

**How do I view the HTML file?** I tend just open it in a browser locally, or upload to S3 if you want a shareable link.

**Doesn't this take longer to generate?** HTML can take 2-4x longer than Markdown, but the results are worth it.

**What about version control?** This is honestly one of the biggest downsides of HTML, HTML diffs are noisy and hard to review compared to Markdown.

**How do I get Claude to match my taste?** The frontend design plugin helps. But to match your own company's style, you can create a single design system HTML file by pointing Claude at your codebase.

The real reason I use HTML is that I feel much more in the loop with Claude. I had begun to fear that because I had stopped reading plans in depth I would simply have to leave Claude to make its choices. But I am happy to say instead that I feel more in the loop than ever before when using HTML.