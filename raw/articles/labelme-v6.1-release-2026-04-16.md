---
updated: 2026-04-18
type: raw
title: "What's new in LabelMe v6.1"
source: https://labelme.io/blog/labelme-v6.1
date: 2026-04-16
fetch_time: 2026-04-18
---

# What's new in LabelMe v6.1

LabelMe v6.1 is out. (Download or upgrade from [here](https://labelme.io/downloads)).

The big one is SAM3 AI-Box mode. The AI toolbar also got a cleanup, and model downloads finally show a progress bar. If you call labelme from scripts, read the migration notes before upgrading.

---

## SAM3 AI-Box mode

Drag a single box, get multiple shapes back. SAM3 figures out what's inside and segments each object separately. Good for crowds, shelves, piles of anything.

![LabelMe v6.1 SAM3 AI-Box mode producing multiple shapes from a single bounding box](https://cdn.labelme.io/blog/labelme-v6.1/sam3-ai-box.webp)

---

## Unified AI toolbar

Four AI tools (`ai_polygon`, `ai_mask`, `ai_polygon_rectangle`, `ai_mask_rectangle`) became two: AI Points → Shape, and AI Box → Shape, each with a polygon/mask toggle. The toolbar now has a separator between manual and AI tools, which makes the AI tools easier to find when you haven't opened the app in a week.

![LabelMe v6.1 unified AI toolbar with AI-Points and AI-Box buttons and a separator between manual and AI tools](https://cdn.labelme.io/blog/labelme-v6.1/ai-toolbar.webp)

---

## AI model downloads show progress

This was overdue. The app used to freeze with no feedback while the model downloaded. Now there's a progress bar, and you can cancel it.

![LabelMe v6.1 AI model download dialog with progress bar and cancel button](https://cdn.labelme.io/blog/labelme-v6.1/ai-download-progress.webp)

---

## Other improvements

- Opening one image also loads the rest of the folder into the file list
- Hover over the disabled AI widget and it flashes the toolbar buttons at you
- Canvas repaints are async now, so heavy redraws no longer block the UI
- Greek, Ukrainian, and Russian translations, all from [@kancheng](https://github.com/kancheng)

---

## Migration notes

### `labelme.utils.lblsave` deprecated

Use `imgviz.io.lblsave` instead. The old import still works but emits a `DeprecationWarning` and will be removed in a future release.

### "Open Recent" removed

The recent-files submenu in the File menu is gone. Use the file list dock or the OS file dialog.

---

## Fixes

- Deleting a shape used to require two undos to restore it; now one undo is enough
- SAM3 is greyed out in AI-Points mode (it doesn't support point prompts)
- AI mode tooltips now match the renamed menu labels
- Unchecking **File > Save Automatically** had no effect since v6.0.0

---

## Get v6.1

Available for Windows, macOS, and Linux from the [downloads page](https://labelme.io/downloads). See the [installation docs](https://labelme.io/docs/install-labelme-app) if you need help.

If something breaks, [open a GitHub issue](https://github.com/wkentaro/labelme/issues) or ask on [Discord](https://labelme.io/discord).

---

*Source: [LabelMe Blog - What's new in LabelMe v6.1](https://labelme.io/blog/labelme-v6.1)*