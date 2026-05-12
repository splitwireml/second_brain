---
title: "Access ALL prompts for stunning animated websites in one click: https://t.co/N0kni8yzNb\n\nPROMPT:\n\nBuild a premium space "
source: "x-bookmarks"
tweet_id: "2045573887849619593"
tweet_url: "https://x.com/viktoroddy/status/2045573887849619593"
author_name: "Viktor Oddy"
author_handle: "@viktoroddy"
tweet_date: "Sat Apr 18 18:43:14 +0000 2026"
bookmark_date: "2026-04-18"
content_type: "x_article"
character_count: 12047
retweet_count: 12
like_count: 126
external_urls:
  - "https://t.co/N0kni8yzNb"
  - "https://t.co/MN1QQel6k6"
  - "https://t.co/8XnpjAZz3s"
  - "https://t.co/betlswri6G"
  - "https://t.co/vN3Hk6ew0N"
  - "https://t.co/35I0PrXc2I"
  - "https://t.co/BHPaFrLSSR"
  - "https://t.co/imDm1F1DXU"
---

Access ALL prompts for stunning animated websites in one click: https://t.co/N0kni8yzNb

PROMPT:

Build a premium space tourism landing page called "Astra" using React, TypeScript, Vite, Tailwind CSS, Framer Motion (motion/react), hls.js, and Lucide React icons. The page has a black background throughout with white text, using two Google Fonts: Instrument Serif (italic, for headings) and Barlow (weights 300, 400, 500, 600 for body text). The entire design uses a custom "liquid glass" morphism effect for cards, buttons, and badges.

FONTS & CONFIGURATION

Load fonts via Google Fonts in index.html:

https://t.co/MN1QQel6k6
Tailwind config extends fontFamily:

heading: 'Instrument Serif', serif
body: 'Barlow', sans-serif
Tailwind also extends colors using CSS custom properties (HSL-based) for background, foreground, card, primary, secondary, muted, accent, destructive, border, input, ring. Border radius uses --radius: 9999px.

LIQUID GLASS CSS (defined in index.css under @layer components)

Two variants:

.liquid-glass -- Light glass effect:

background: rgba(255,255,255,0.01), background-blend-mode: luminosity
backdrop-filter: blur(4px), no border
box-shadow: inset 0 1px 1px rgba(255,255,255,0.1)
::before pseudo-element creates a gradient border stroke using mask-composite trick:
padding: 1.4px
background: linear-gradient(180deg, rgba(255,255,255,0.45) 0%, rgba(255,255,255,0.15) 20%, transparent 40%, transparent 60%, rgba(255,255,255,0.15) 80%, rgba(255,255,255,0.45) 100%)
-webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0), -webkit-mask-composite: xor, mask-composite: exclude
.liquid-glass-strong -- Stronger glass effect:

Same as above but backdrop-filter: blur(50px)
box-shadow: 4px 4px 4px rgba(0,0,0,0.05), inset 0 1px 1px rgba(255,255,255,0.15)
::before gradient goes from rgba(255,255,255,0.5) to 0.2 at edges
GLOBAL CSS (index.css)

CSS custom properties defined on :root:

--background: 213 45% 67%;
--foreground: 0 0% 100%;
--card: 213 45% 62%;
--card-foreground: 0 0% 100%;
--primary: 0 0% 100%;
--primary-foreground: 213 45% 67%;
--secondary: 213 45% 72%;
--secondary-foreground: 0 0% 100%;
--muted: 213 35% 60%;
--muted-foreground: 0 0% 100% / 0.7;
--accent: 213 45% 72%;
--accent-foreground: 0 0% 100%;
--destructive: 0 84.2% 60.2%;
--border: 0 0% 100% / 0.2;
--input: 0 0% 100% / 0.2;
--ring: 0 0% 100% / 0.3;
--radius: 9999px;
--glass-bg: rgba(255,255,255,0.12);
--glass-border: rgba(255,255,255,0.25);
--glass-shadow: 0 4px 30px rgba(0,0,0,0.08);
--glass-blur: 16px;
Body: font-family: 'Barlow', sans-serif; background: #000; color: #fff; with antialiased font smoothing. html { scroll-behavior: smooth; }. Universal reset: * { margin:0; padding:0; box-sizing: border-box; }.

APP STRUCTURE (App.tsx)

Renders in order inside <div className="bg-black"><div className="relative z-10">:

Navbar
Hero
Wrapped in <div className="bg-black">:
StartSection
FeaturesChess
Stats
CtaFooter
SECTION 1: NAVBAR

Fixed position navbar: fixed top-4 left-0 right-0 z-50 px-6 lg:px-12 py-3. Max-width 7xl centered.

Left: Rocket icon (lucide-react, h-7 w-7 white) + "Astra" in font-heading italic text-2xl white
Center (hidden on mobile, visible md+): liquid-glass rounded-full px-1.5 py-1 container holding nav links as text buttons: "Overview", "Missions", "Technology", "Crew", "Contact" -- each px-4 py-2 text-sm font-medium text-white/80 font-body hover:text-white. Followed by a white filled "Reserve Seat" button with ArrowUpRight icon: bg-white text-black rounded-full px-4 py-2 text-sm font-semibold font-body
Right (mobile only): hamburger Menu/X toggle button in liquid-glass rounded-full p-2.5
Mobile menu: drops down as liquid-glass rounded-2xl p-4 with same links stacked vertically + full-width Reserve Seat button
SECTION 2: HERO

Full viewport height section (min-h-screen) with id="overview", relative overflow-hidden.

Background: <video autoPlay loop muted playsInline> absolutely positioned, covering full section, z-0.

Video URL: https://t.co/8XnpjAZz3s
No overlay, no gradient, full opacity (just an empty <div className="absolute inset-0 z-[1]" />)
Content (z-10, flex column, min-h-screen):

Top area (flex-1, pt-32 md:pt-40, px-6 md:px-16 lg:px-24, pb-12):

Badge (motion.div, animates opacity 0->1, y 20->0, delay 0.3s, duration 0.5s): liquid-glass rounded-full px-1 py-1 flex items-center gap-2 mb-8. Contains:

White pill: bg-white text-black rounded-full px-3 py-1 text-xs font-semibold font-body showing "2026"
Text: text-white text-xs font-body pr-3 "Civilian orbital missions now boarding."
BlurText component for headline: "Beyond the atmosphere. Beyond imagination."

Classes: text-5xl md:text-6xl lg:text-[5rem] font-heading italic text-white leading-[0.85] max-w-3xl tracking-[-3px]
delay={100}
BlurText splits text into words, each word is a motion.span with inline-block mr-[0.25em]. Uses IntersectionObserver (threshold 0.1). Animates from blur(10px), opacity:0, y:50 through blur(5px), opacity:0.5, y:-5 to blur(0px), opacity:1, y:0. Duration 0.7s per word, staggered by delay/1000 per word index.
Subtitle (motion.p, blur 10px->0, opacity 0->1, y 20->0, delay 0.8s, duration 0.6s): mt-6 text-sm md:text-base text-white/70 font-body font-light leading-relaxed max-w-lg -- "Step aboard the next generation of spacecraft. Witness sunrise from orbit, float weightless above the clouds, and see our planet the way only a few hundred humans ever have."

Buttons row (motion.div, same blur animation, delay 1.1s): mt-8 flex flex-wrap items-center gap-4

"Reserve Your Seat": liquid-glass-strong rounded-full px-6 py-3 text-white font-body text-sm font-medium with ArrowUpRight icon
"Watch the Launch Film": text button with Play icon (fill-white), text-white font-body text-sm font-light
Bottom area (motion.div, opacity 0->1, delay 1.4s, duration 0.8s): px-6 md:px-16 lg:px-24 pb-10 pt-8

Divider: border-t border-white/10 pt-6, flex row between:
Left: text-white/40 text-xs font-body uppercase tracking-widest "Trusted by pioneers in aerospace"
Right: Partner logos as text: "SpaceX", "NASA", "Boeing", "Blue Origin", "ESA" -- each text-xl md:text-2xl font-heading italic text-white/60 hover:text-white transition-colors, gap-8 md:gap-12
SECTION 3: START SECTION ("How It Works")

Section with id="missions", relative overflow-hidden py-32 px-6 md:px-16.

Background: <video autoPlay loop muted playsInline> absolutely positioned, full cover, z-0.

Video URL: https://t.co/betlswri6G
No overlay, no gradient, full opacity (just <div className="absolute inset-0 z-[1]" />)
Content (z-10, max-w-6xl centered): Two-column layout (flex-col md:flex-row, gap-16, items-start)

Left column (md:w-1/2, md:sticky md:top-32):

Badge: liquid-glass rounded-full px-3.5 py-1 inline-block mb-6 with "How It Works" text-xs font-medium white
Heading: text-4xl md:text-5xl lg:text-6xl font-heading italic text-white tracking-tight leading-[0.9] "Three steps to orbit."
Paragraph: mt-5 text-white/60 font-body font-light text-sm md:text-base max-w-md leading-relaxed "We stripped away the complexity of space travel. What remains is a seamless path from ground to weightlessness."
Button: liquid-glass-strong rounded-full px-6 py-3 text-white font-body text-sm font-medium with ArrowUpRight, mt-8
Right column (md:w-1/2, flex-col gap-8): Three step cards, each liquid-glass rounded-2xl p-8:

Step number: text-white/30 font-heading italic text-5xl ("01", "02", "03")
Title: mt-3 text-xl font-body font-semibold text-white
Description: mt-2 text-white/60 font-body font-light text-sm leading-relaxed
Steps 

"01" / "Choose Your Mission" / "Suborbital, orbital, or lunar flyby. Pick the experience that matches your ambition."
"02" / "Train in Days" / "AI-adaptive programs prepare you physically and mentally. No pilot license needed."
"03" / "Launch" / "Board your spacecraft, break through the atmosphere, and witness what words cannot describe."
SECTION 4: FEATURES CHESS (Technology)

Section with id="technology", py-32 px-6 md:px-16. Max-w-6xl centered.

Header area (mb-20):

Badge: liquid-glass rounded-full px-3.5 py-1 mb-6 with "Technology"
Heading: text-4xl md:text-5xl lg:text-6xl font-heading italic text-white tracking-tight leading-[0.9] max-w-lg "Precision engineering. Human-centered design."
Two alternating rows (gap-32 between them), each a flex-col md:flex-row with items-center gap-12:

Row 1 (normal order):

Text side (flex-1): heading text-3xl md:text-4xl font-heading italic text-white leading-[0.95] "Spacecraft built for humans, not just engineers." + body text-white/60 font-body font-light text-sm md:text-base leading-relaxed max-w-md + button liquid-glass-strong rounded-full px-5 py-2.5 "Explore the Fleet" with ArrowUpRight
Video side (flex-1): liquid-glass rounded-2xl overflow-hidden wrapping <video autoPlay loop muted playsInline className="w-full h-72 md:h-96 object-cover">
Video URL: https://t.co/vN3Hk6ew0N
Row 2 (reversed: md:flex-row-reverse):

Text: "AI that learns you before you leave the ground." / "Our adaptive training system monitors biometrics, reaction times, and stress responses in real time. It builds a profile unique to you, adjusting every simulation until you are mission-ready." / "See the Training"
Video URL: https://t.co/35I0PrXc2I
SECTION 5: STATS ("By the Numbers")

Section with id="crew", relative overflow-hidden py-32 px-6 md:px-16.

Background: HLS video (using hls.js player component) absolutely positioned, full cover.

HLS URL: https://t.co/BHPaFrLSSR
Top gradient overlay: 200px height, linear-gradient(to bottom, black, transparent), z-[1]
Bottom gradient overlay: 200px height, linear-gradient(to top, black, transparent), z-[1]
Content (z-10, max-w-6xl centered):

Header centered: badge "By the Numbers" + heading "Results speak louder than rockets." (same heading styles)
Grid: grid-cols-2 lg:grid-cols-4 gap-6. Four stat cards, each liquid-glass rounded-2xl p-8 text-center:
Value: text-4xl md:text-5xl lg:text-6xl font-heading italic text-white
Label: text-white/60 font-body font-light text-sm mt-3
 47/Missions completed, 99.8%/Mission success rate, 312/Civilians launched, 72hrs/Average mission length
SECTION 6: CTA + FOOTER

Section with id="contact", relative overflow-hidden.

Background: HLS video, absolutely positioned, full cover.

HLS URL: https://t.co/imDm1F1DXU
Top gradient: 250px, black to transparent, z-[1]
Bottom gradient: 250px, transparent to black, z-[1] (note: linear-gradient(to top, black, transparent))
Content (z-10, px-6 md:px-16, py-40):

Max-w-6xl centered, flex-col md:flex-row items-start md:items-end justify-between gap-12

Left side (max-w-xl):

Heading: text-5xl md:text-6xl lg:text-7xl font-heading italic text-white leading-[0.85] "Your seat is waiting above the clouds."
Paragraph: mt-6 text-white/60 font-body font-light text-sm md:text-base max-w-md leading-relaxed
Buttons (mt-8, flex flex-wrap gap-4):
"Book a Consultation": liquid-glass-strong rounded-full px-6 py-3 with ArrowUpRight
"View All Missions": bg-white text-black rounded-full px-6 py-3 font-body text-sm font-medium
Footer (mt-32, pt-8, border-t border-white/10): flex between:

Left: copyright text-white/40 text-xs font-body
Right: "Privacy", "Terms", "Contact" links, text-white/40 text-xs font-body hover:text-white/60
HLS VIDEO COMPONENT (HlsVideo.tsx)

Accepts src, className, style props. Uses hls.js library. On mount: if Hls.isSupported(), creates new Hls instance, loads source, attaches to video element, cleans up on unmount. Fallback for native HLS (Safari): sets video.src directly. Video element has autoPlay loop muted playsInline.

DEPENDENCIES (package.json)

react, react-dom ^18.3.1
react-router-dom ^7.14.0
motion ^12.38.0 (Framer Motion)
hls.js ^1.6.15
lucide-react ^0.344.0
@supabase/Bolt Database-js ^2.57.4
Tailwind CSS ^3.4.1, PostCSS, Autoprefixer
Vite ^5.4.2, TypeScript ^5.5.3
This prompt contains every video URL, every CSS class, every animation parameter, every text string, and every structural detail needed to reproduce the landing page identically.
