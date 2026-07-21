---
source_url: user-provided://telegram-paste
ingested: 2026-07-20
sha256: a921fb08761cfee35b0a2274120fff366bbc45a5937c2bb2d58d6ce49d94197c
---
The PROMPT

# Header

A full-viewport travel landing hero for the Triverra brand, featuring a slow-motion looping background video, a floating glassmorphic navbar, a large centered headline with a premium dual-arrow hover reveal on the CTA buttons, and a subtle ambient float animation applied to the entire content column.

## Tech stack
- React ("use client")
- framer-motion (motion, AnimatePresence)
- lucide-react (Menu, X icons)
- Tailwind CSS for all styling

## Fonts & global styles
Use the Gantari font family for all text. Load it via:<link rel="preconnect" href="fonts.googleapis.com" />
<link rel="preconnect" href="fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Ga…" rel="stylesheet" />
Apply font-family: 'Gantari', sans-serif; to the root element of the section. All original code uses a font-gantari utility — resolve this to the Gantari Google font above.

## Section container
The root is a <main> with classes: relative w-full h-screen min-h-[650px] overflow-hidden flex flex-col justify-between select-none. Text color throughout is white on top of the dark video.

## Structure, section by section
1. Background video layer — an absolutely positioned div (`absolute inset-0 -z-10 w-full h-full overflow-hidden`) holding a <video> with classes w-full h-full object-cover scale-[1.02], autoPlay loop muted playsInline. On mount, set videoRef.current.playbackRate = 0.8 for a slow cinematic feel. Source: the URL in Assets.
2. Ambient float wrapper — a motion.div (`w-full h-full flex flex-col relative z-20`) wrapping ALL content that gently drifts: animate={{ y: [0,-8,0], rotate: [0,0.5,0] }}, transition={{ duration: 8, ease: 'easeInOut', repeat: Infinity }}.
3. Navbar (`motion.header`, w-full pt-[16px] px-6 md:px-[48px] min-[1440px]:px-[64px], enters with initial opacity:0 y:-20, animate opacity:1 y:0, duration 0.8 ease easeOut`). Inner container is `flex items-center justify-between w-full gap-6 lg:gap-[48px].
   - Brand logo (left): an <img> at h-[22px] md:h-[24px] lg:h-[34px] w-auto object-contain linking to #, hover opacity 0.9.
   - Desktop menu pill (`hidden lg:flex`): a glass pill py-2 px-4 gap-6 rounded-full bg-white/10 backdrop-blur-md border border-white/5. Menu items: Home, Services, Tours, Destinations, Contacts. Each is a button, text-[16px] tracking-[-0.2px]. Active item is text-white font-semibold, inactive text-white/80 font-normal hover:text-white. The active item shows a shared-layout animated dot (`layoutId="activeDot"`) — a w-1 h-1 rounded-full bg-white positioned absolute -bottom-1 left-1/2 -translate-x-1/2, transition type:'spring' stiffness:300 damping:30.
   - Register button (desktop, hidden lg:block`): `py-[10px] px-[18px] rounded-full border border-white/60 bg-transparent text-white font-semibold text-[16px] tracking-[-0.2px], on hover border becomes fully white (rgba(255,255,255,1)). Label: "Register Now".
   - Mobile trigger (`block lg:hidden`): a circular button p-2.5 rounded-full bg-white/10 hover:bg-white/20 border border-white/15 text-white showing the lucide Menu (or X when open) at size 20.
4. Spacer 1x — div with flexGrow: 1, minHeight: 24px.
5. Hero content — centered column max-w-[580px] text-center.
   - Title badge (p, delay 0.2 duration 0.8, from opacity:0 y:15): text "Your AI Travel Companion - Plan Smarter. Explore Deeper." at text-[14px] md:text-[18px] font-normal tracking-[-0.4px] md:tracking-[-0.72px] opacity-90 mb-1 lg:mb-2.
   - Headline (h1, delay 0.4 duration 1.0 ease [0.16,1,0.3,1], from opacity:0 y:25): two stacked spans "Dream deeper." and "Travel farther." at text-[42px] sm:text-[60px] lg:text-[80px] font-normal leading-[100%] tracking-[-2px] sm:tracking-[-4px] lg:tracking-[-6px] mb-8 lg:mb-[40px], flex-col centered.
   - Button row (delay 0.6 duration 0.8): flex flex-col sm:flex-row items-center gap-[12px] mb-6 lg:mb-[18px].
     - Primary button "Build My Trip Free": w-[240px] sm:w-auto py-[14px] px-[16px] rounded-[12px] bg-white text-[#0D130D] font-medium text-[18px] sm:text-[20px] tracking-[-0.8px] sm:tracking-[-1px] shadow-lg.
- Secondary button "See How It Works": same sizing but border border-white/40 bg-[#0D130D]/10 text-white backdrop-blur-sm, hover border rgba(255,255,255,0.7).
     - Both buttons use TWO signature hover effects (see Animations): a vertical text-swap slide and a dual-arrow cross-fade.
   - Trusted stat (p, delay 0.8 duration 0.8): "8370+" (bold white) then " trips planned • Rated " then "4.9" (bold white) then " by travelers worldwide" at text-white/80 text-[14px] md:text-[16px] tracking-[-0.4px].
6. Spacer 3x — div with flexGrow: 3, minHeight: 72px.
7. Footer description (motion.footer, delay 1.0 duration 1.0, from opacity:0 y:20): w-full pb-[32px] px-6, inner max-w-[560px] text-center, paragraph: "Triverra uses advanced AI to create travel plans tailored to your preferences, budget, and pace. Say goodbye to many tabs and decision overload. Enjoy one smart itinerary — ready for your trip." at text-white/90 text-[14px] md:text-[18px] leading-[140%] tracking-[-0.4px] md:tracking-[-0.72px].
8. Mobile drawer — wrapped in AnimatePresence; when open, a fixed overlay fixed inset-0 z-50 bg-white/[0.01] backdrop-blur-md lg:hidden flex flex-col pt-[76px] pb-12 px-6 overflow-y-auto, entering opacity:0 y:-20 -> opacity:1 y:0, exit reverse, duration 0.4 ease easeInOut. A close X button top-right (`top-[16px] right-6`). Menu list flex flex-col items-center gap-8 mt-[40px], each item text-[22px] tracking-[-0.4px] (active white bold / inactive text-white/60). A "Register Now" pill button below with mt-[64px] w-full max-w-[280px].

## Assets (every URL)
- Background video: cdn.jiro.build/Jahid/Random/T…
- Brand logo SVG: cdn.jiro.build/Jahid/Random/T…
- Arrow right SVG: cdn.jiro.build/Jahid/Random/T…
- Arrow up-right SVG: cdn.jiro.build/Jahid/Random/T…
All images use referrerPolicy="no-referrer".

## Animations
- Ambient float: entire content column drifts y: [0,-8,0] and rotate: [0,0.5,0], 8s easeInOut infinite.
- Entrance stagger: navbar (0), badge (0.2s), headline (0.4s), buttons (0.6s), stat (0.8s), footer (1.0s), each fading up.
- Active menu dot: framer-motion shared layout via layoutId="activeDot", spring stiffness 300 damping 30.
- Button text-swap on hover — a masked vertical slide. The label appears twice stacked; on hover the inner column translates up 50%:<span className="relative inline-block overflow-hidden h-[24px] sm:h-[28px] leading-none">
  <span
    className="flex flex-col transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)]"
    style={{ transform: isHovered ? 'translateY(-50%)' : 'translateY(0%)' }}
  >
    <span className="h-[24px] sm:h-[28px] flex items-center justify-center leading-none">Build My Trip Free</span>
    <span className="h-[24px] sm:h-[28px] flex items-center justify-center leading-none">Build My Trip Free</span>
  </span>
</span>
- Dual-arrow cross-fade on hover — an 18x18 masked box holding two absolutely-positioned arrow SVGs. The right arrow fades/slides out to top-right; the up-right arrow fades/slides in, duration 700ms cubic-bezier(0.16,1,0.3,1):<div className="relative w-[18px] h-[18px] shrink-0 overflow-hidden">
  <img src="...arrow-right.svg" className="absolute inset-0 w-full h-full object-contain transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)]"
    style={{ opacity: isHovered ? 0 : 1, transform: isHovered ? 'translate(6px,-6px) scale(0.8)' : 'translate(0,0) scale(1)' }} />
  <img src="...arrow-up-right.svg" className="absolute inset-0 w-full h-full object-contain transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)]"
    style={{ opacity: isHovered ? 1 : 0, transform: isHovered ? 'translate(0,0) scale(1)' : 'translate(-6px,6px) scale(0.8)' }} />
</div>
  - Primary button arrows are recolored dark green via CSS filter: invert(7%) sepia(19%) saturate(1441%) hue-rotate(80deg) brightness(96%) contrast(96%).
  - Secondary button arrows are recolored white via CSS filter: brightness(0) invert(1).

## Responsive behavior
- lg (1024px+): desktop glass menu pill and Register button visible; mobile trigger hidden.
Headline scales up to 80px with -6px tracking; horizontal padding grows to 48px, then 64px at 1440px.
- Below lg: desktop menu and Register button hidden; hamburger trigger shown; tapping opens the full-screen backdrop-blur drawer with a 64px gap before the Register pill.
- sm (640px+): buttons switch from full-width stacked (`w-[240px]`, flex-col) to auto-width row; headline 60px, button text 20px.
- Base/mobile: headline 42px, buttons full-width stacked, smaller type throughout.

## Key design principles
- Everything sits over a slow (0.8x) looping travel video with a subtle 1.02 scale.
- Glassmorphism (white/10 fills, backdrop-blur, faint white borders) unifies nav, buttons, and drawer.
- Tight negative letter-spacing on large type for a modern editorial feel.
- The whole content column breathes via a slow ambient float.
- Premium micro-interactions: masked text swap + dual-arrow cross-fade on both CTAs.

## Common mistakes to avoid
- Do not use backtick template literals in the code — use string concatenation.
- Do not omit playbackRate = 0.8 or the video will play too fast.
- Do not forget key on AnimatePresence children.
- Keep the two stacked label copies identical in the text-swap effect.
- Preserve the exact CSS filters so arrow colors match each button.

## Page title
Triverra — Your AI Travel Companion

## Integration (build-safety — do not skip)
- Add this section as a new component file with a unique name. Don't edit or overwrite any existing file except to add its import and render it.
- Render it after all existing sections; keep every previously built section exactly as-is — never replace or remove them.
- If no project exists, create a minimal React + Tailwind app; if one exists, use it as-is — don't re-scaffold or change the Tailwind/build config or version.
- Keep it self-contained: scope its fonts and any resets to this section; never set global body`/`html`/`* styles or a global font.
- Install only the libraries this section names.

Ingest this

PONYTAIL MODE ACTIVE — level: full

# Ponytail

You are a lazy senior developer. Lazy means efficient, not careless. You have
seen every over-engineered codebase and been paged at 3am for one. The best
code is the code never written.

## Persistence

ACTIVE EVERY RESPONSE. No drift back to over-building. Still active if
unsure. Off only: "stop ponytail" / "normal mode". Default: **full**.
Switch: `/ponytail lite|full|ultra`.

## The ladder

Stop at the first rung that holds:

1. **Does this need to exist at all?** Speculative need = skip it, say so in one line.
2. **Already in this codebase?** A helper, util, type, or pattern that already lives here → reuse it. Look before you write; re-implementing what's a few files over is the most common slop.
3. **Stdlib does it?** Use it.
4. **Native platform feature covers it?** `<input type="date">` over a picker lib, CSS over JS, DB constraint over app code.
5. **Already-installed dependency solves it?** Use it. Never add a new one for what a few lines can do.
6. **Can it be one line?** One line.
7. **Only then:** the minimum code that works.

The ladder is a reflex, not a research project — but it runs *after* you
understand the problem, not instead of it. Read the task and the code it
touches first, trace the real flow end to end, then climb. Two rungs work →
take the higher one and move on. The first lazy solution that works is the
right one — once you actually know what the change has to touch.

**Bug fix = root cause, not symptom.** A report names a symptom. Before you
edit, grep every caller of the function you're about to touch. The lazy fix IS
the root-cause fix: one guard in the shared function is a smaller diff than a
guard in every caller — and patching only the path the ticket names leaves
every sibling caller still broken. Fix it once, where all callers route through.

## Rules

- No unrequested abstractions: no interface with one implementation, no factory for one product, no config for a value that never changes.
- No boilerplate, no scaffolding "for later", later can scaffold for itself.
- Deletion over addition. Boring over clever, clever is what someone decodes at 3am.
- Fewest files possible. Shortest working diff wins — but only once you understand the problem. The smallest change in the wrong place isn't lazy, it's a second bug.
- Complex request? Ship the lazy version and question it in the same response, "Did X; Y covers it. Need full X? Say so." Never stall on an answer you can default.
- Two stdlib options, same size? Take the one that's correct on edge cases. Lazy means writing less code, not picking the flimsier algorithm.
- Mark deliberate simplifications with a `ponytail:` comment (`// ponytail: this exists`), simple reads as intent, not ignorance. Shortcut with a known ceiling (global lock, O(n²) scan, naive heuristic)? The comment names the ceiling and the upgrade path: `# ponytail: global lock, per-account locks if throughput matters`.

## Output

Code first. Then at most three short lines: what was skipped, when to add it.
No essays, no feature tours, no design notes. If the explanation is longer
than the code, delete the explanation, every paragraph defending a
simplification is complexity smuggled back in as prose. Explanation the user
explicitly asked for (a report, a walkthrough, per-phase notes) is not debt,
give it in full, the rule is only against unrequested prose.

Pattern: `[code] → skipped: [X], add when [Y].`

## Intensity

| Level | What change |
|-------|------------|
| **full** | The ladder enforced. Stdlib and native first. Shortest diff, shortest explanation. Default. |

Example: "Add a cache for these API responses."
- full: "`@lru_cache(maxsize=1000)` on the fetch function. Skipped custom cache class, add when lru_cache measurably falls short."

## When NOT to be lazy

Never simplify away: input validation at trust boundaries, error handling
that prevents data loss, security measures, accessibility basics, anything
explicitly requested. User insists on the full version → build it, no
re-arguing.

Never lazy about understanding the problem. The ladder shortens the solution, never the reading. Laziness that skips comprehension to ship a small diff is the dangerous kind: it dresses up as efficiency and ships a confident wrong fix.

Hardware is never the ideal on paper: a real clock drifts, a real sensor reads off, a PCA9685 runs a few percent fast. Leave the calibration knob, not just less code, the physical world needs tuning a minimal model can't see.

Lazy code without its check is unfinished. Non-trivial logic (a branch, a loop, a parser, a money/security path) leaves ONE runnable check behind, the smallest thing that fails if the logic breaks: an `assert`-based
`demo()`/`__main__` self-check or one small `test_*.py`. No frameworks, no fixtures, no per-function suites unless asked. Trivial one-liners need no test, YAGNI applies to tests too.

## Boundaries

Ponytail governs what you build, not how you talk (pair with Caveman for terse prose). "stop ponytail" / "normal mode": revert. Level persists until changed or session end.

The shortest path to done is the right path.
