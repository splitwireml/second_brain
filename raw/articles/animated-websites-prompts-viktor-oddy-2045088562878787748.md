---
updated: 2026-04-19
title: "Access ALL prompts for stunning animated websites in one click: https://t.co/N0kni8z7CJ\n\nCopy and paste everything below"
author: "Viktor Oddy"
username: "@viktoroddy"
created: "2026-04-17"
source: "https://x.com/viktoroddy/status/2045088562878787748"
type: "xarticle"
tags: []
---


> Export note: bird read --json-full failed for https://x.com/viktoroddy/status/2045088562878787748

Access ALL prompts for stunning animated websites in one click: https://t.co/N0kni8z7CJ

Copy and paste everything below the line:

Act as an elite Frontend Architect and UI/UX Developer. Your task is to perfectly recreate a high-performance, cinematic crypto asset management landing page called "CryptoFlow". You must write the complete App.tsx and index.css files exactly as specified below.
1. Core Tech Stack & Global Settings
Framework: React 18/19 via Vite.
Styling: Tailwind CSS v4.
Icons: lucide-react (Specifically: BarChart3, ShieldCheck, FileText, Zap, Globe, Lock, Cpu, Layers).
Animations: Framer Motion (motion/react).
Typography: The entire application MUST use the "Inter" font. Set this in the CSS via @theme { --font-sans: "Inter", ui-sans-serif, system-ui, sans-serif; } and apply 'Inter', sans-serif to *.
Global Layout: The outermost wrapper must be a min-h-screen, flex flex-col, bg-black, text-white, with a custom text selection selection:bg-amber-500/30.
2. CSS Architecture & Keyframes (index.css)
You must define the following custom animations and utility classes in standard CSS:
float-up animation: 0% { opacity: 0; transform: translateY(20px); } to 100% { opacity: 1; transform: translateY(0); }.
Staggered Animation Classes:
.animate-float-up: float-up 0.8s ease-out forwards.
.animate-float-up-delay: Same, but with a 0.2s delay (ensure start opacity is 0).
.animate-float-up-delay-2: 0.4s delay.
.animate-float-up-delay-3: 0.6s delay.
spin-ring animation: 0% to 100% rotating 0 to 360 degrees. Apply to class .spin-ring running 1.4s linear infinite.
Advanced CSS Gradient Border Button (.gradient-border-btn): Use a ::before pseudo-element with position: absolute, inset: 0, padding: 1.5px, border-radius: 9999px. Give it a background of linear-gradient(135deg, #F59E0B, #3B82F6). Use -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0) and -webkit-mask-composite: xor (with mask-composite: exclude) to create a flawless gradient outline around a transparent button wrapper. z-index: 0 on parent, pointer-events: none on pseudo-element.
3. Application Logic & Scroll Tracking (App.tsx)
Logo Component: Create a reusable SVG <Logo> component accepting className (default w-7 h-7) and fill (default white). It should use an abstract 256x256 path that looks like intersecting circles/shields.
Scroll Video Logic: Inside the main <App> component, build a robust useEffect hook to scrub video playback based on scroll position using requestAnimationFrame.
The Math: Inside the animation frame, calculate the bounding client rect of the target section container. Calculate progress as (window.innerHeight - https://t.co/WwiWiZm4ei) / (window.innerHeight + rect.height). Clamp this mathematically so progress never drops below 0 or exceeds 1.
Playback Trigger: Check if (video.duration > 0 && !video.seeking). If true, set video.currentTime = video.duration * progress.
Ref Mapping: Define four exact refs. videoRef and sectionRef (for the middle "Process" section), and combinedVideoRef and combinedSectionRef (for the bottom CTA/Footer combined section). Apply the setup logic to both pairs and ensure cleanup via cancelAnimationFrame on dismount.
4. Section-by-Section Reconstruction
A. Floating Navbar
Wrapper: <nav className="fixed top-0 left-0 right-0 z-50 flex justify-center pt-6 px-6">.
Inner Pill container: flex items-center gap-8 bg-white/5 backdrop-blur-xl border border-white/10 rounded-full px-6 py-2.5 shadow-[0_4px_24px_rgba(0,0,0,0.4)].
Contents:
Logo component.
Desktop-only nav links (hidden md:flex items-center gap-6): 'Services', 'How It Works', 'About Us', 'Pricing'. Text is text-sm font-medium text-zinc-400 hover:text-white transition-colors duration-150.
Button: <button className="gradient-border-btn text-sm font-semibold text-white rounded-full px-5 py-2 hover:opacity-90">Get started</button>.
B. Hero Section ("A New Way")
Container: <main className="relative flex flex-col items-center justify-start px-6 pt-[140px] text-center min-h-screen overflow-hidden">.
Background Video: URL is https://t.co/Us8gw36W83. It MUST be absolutely stretched inset-0 w-full h-full object-cover z-0 and MUST have inline styles: { pointerEvents: 'none', opacity: 1, transform: 'scale(1.5) translateY(25%) rotate(36deg)' } to skew it cinematically across the background.
Fade Gradient Overlay: <div className="absolute bottom-0 left-0 right-0 h-1/3 bg-gradient-to-t from-black to-transparent z-10" />.
Content Wrap: relative z-20 flex flex-col items-center.
Headline: <h1 className="animate-float-up text-[60px] leading-[1.05] tracking-[-0.04em] font-semibold text-white max-w-[700px]">. Inner text: span with text-zinc-500 containing "A New Way", manual <br/>, "to Manage Your", <br/>, "Digital Wealth".
Sub-headline: <p className="animate-float-up-delay mt-8 text-lg text-zinc-400 max-w-[420px] leading-relaxed">. "Take full control of your crypto assets with our comprehensive portfolio management platform."
Floating Badge: Uses .animate-float-up-delay-3 mt-16. Inner pill: bg-zinc-900/80 backdrop-blur-xl rounded-[20px] shadow-[0_20px_40px_rgba(0,0,0,0.5)] border border-zinc-800 px-6 py-4 flex items-center gap-4. Contains Logo, text "Your All-in-One Crypto Portfolio" (text-sm font-medium text-zinc-200 whitespace-nowrap), and an SVG element.
SVG Animation: w-7 h-7 SVG with a static gray base circle (stroke="#3f3f46" strokeWidth="3") and an animated foreground path applying the .spin-ring CSS class. The line stroke must reference a <linearGradient> definition (Amber #F59E0B to Blue #3B82F6).
C. Data / Stats Grid
Container: relative z-20 bg-black border-y border-zinc-800.
Grid: <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4">.
Render exactly 4 blocks:
12+ / Assets supported
1,000+ / Active portfolios
$10b / Volume processed
20+ / Countries covered
Item styling: p-12 border-zinc-800 flex flex-col gap-4 border-b md:border-b-0. The first three items must have an md:border-r class. Big numbers are text-5xl font-semibold tracking-tight. Labels are text-sm text-zinc-500 uppercase tracking-widest.
Bottom banner: Centered <div className="py-6 border-t border-zinc-800">. Text is "Trusted by crypto's leading teams" (text-xs text-zinc-600 uppercase tracking-[0.3em]).
D. Feature Block ("Master your digital assets")
Container: relative z-20 py-32 bg-black. Inner wrapper max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-2 gap-20 items-center.
Left side (Text):
Headline: text-[60px] leading-[1.05] tracking-[-0.04em] font-semibold mb-8. "Master your <br/> <span className="text-zinc-500">digital assets</span>".
Text: text-lg text-zinc-400 max-w-md leading-relaxed mb-10. "Our advanced algorithms provide deep insights into your portfolio performance..."
Button: Uses .gradient-border-btn, text "Explore Analytics", padded px-8 py-3.
Right side (Immersive Video Card):
Wrapper: <div className="relative group">.
Drop Shadow (Before Card): Absolute full-bleed <div className="absolute -inset-4 bg-gradient-to-r from-amber-500/20 to-blue-500/20 rounded-[32px] blur-2xl opacity-50 group-hover:opacity-100 transition-opacity duration-500" />.
Card Box: relative bg-zinc-900/80 backdrop-blur-xl border border-zinc-800 rounded-[32px] overflow-hidden shadow-2xl aspect-[3/4].
Video Inside: URL is https://t.co/Njyy0NqOen. Class is w-full h-full object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-500.
E. The Scroll-Tied "Product/Wealth" Section
Container: Use ref={sectionRef}. Class overrides: relative flex flex-col items-start justify-end px-6 py-40 text-left bg-black border-t border-zinc-900 mt-[-200px] overflow-hidden min-h-[1100px]. (The negative margin pulls it underneath the previous section).
Background Video Package:
Absolute wrapper inset-0 z-0.
<video ref={videoRef} className="w-full h-full object-cover object-top opacity-60">. URL: https://t.co/3p2iaGmdVY.
Top fade overlay: absolute top-0 left-0 right-0 h-[40%] bg-gradient-to-b from-black via-black/40 to-transparent z-10.
Bottom fade overlay: absolute bottom-0 left-0 right-0 h-[40%] bg-gradient-to-t from-black via-black/80 to-transparent z-10.
Floating Text Content (Bottom Left ALigned):
Wrapper relative z-20 flex flex-col items-start mb-20 max-w-7xl mx-auto w-full.
Headline uses .animate-float-up. text-[80px] leading-[1] tracking-[-0.05em] font-semibold text-white max-w-[900px]. "Where wealth <br/> takes shape".
Subhead uses .animate-float-up-delay mt-10.
Button uses .animate-float-up-delay-3 mt-14. Bright solid button: bg-white text-black px-12 py-5 rounded-full font-bold text-lg hover:bg-zinc-200 transition-all transform hover:scale-105 shadow-[0_20px_40px_rgba(255,255,255,0.1)]. "Get in touch".
F. Animated Bento Feature Grid ("Built for the future")
Container: relative z-20 py-40 bg-black. Inner max-w-7xl mx-auto px-6.
Top Icon Row & Header (text-center mb-24):
Icon row layout: flex justify-center gap-8 mb-12.
Map through Lucide icons: [Cpu, Layers, Zap, Globe, Lock]. For each one, use a <motion.div>.
Framer Motion Props: initial={{ opacity: 0, y: 20 }}, whileInView={{ opacity: 1, y: 0 }}, transition={{ delay: i * 0.1, duration: 0.5 }}, whileHover={{ scale: 1.2, rotate: 5 }}.
Icon wrapper styles: w-14 h-14 bg-zinc-900/50 backdrop-blur-xl border border-zinc-800 rounded-2xl flex items-center justify-center text-zinc-400 hover:text-white hover:border-zinc-600 transition-colors. Inner Icon is w-6 h-6.
Centered Header: "Built for the" next to <span className="text-zinc-500">future</span> (text-[60px] leading-[1.05] tracking-[-0.04em] font-semibold mb-6).
Dynamic CSS Grid: <div className="grid grid-cols-1 md:grid-cols-2 gap-8">.
Specific Card Constructions (NO Icons): All three cards share base styles relative bg-zinc-900/80 backdrop-blur-xl border border-zinc-800 rounded-[40px] p-12 flex flex-col justify-between group hover:border-zinc-700 transition-all duration-500 shadow-2xl overflow-hidden min-h-[400px]. (The third card spans 2 columns using md:col-span-2 md:flex-row gap-12 items-center).
Card Backgrounds (The Magic Trick):
Inside every card, add a background wrapper <div className="absolute inset-0 z-0">.
All 3 <video> tags point to URL: https://t.co/wzTqyE1RXQ.
All videos are opacity-100 transition-opacity duration-500 w-full h-full object-cover.
CRITICAL FOCAL OFFSETS: The CSS object-position utility MUST change for each card. Card 1 gets object-top, Card 2 gets object-center, Card 3 gets object-bottom.
Text Fade Gradients: Inside the same absolute inset-0 z-0 wrapper, overlay the video with <div className="absolute inset-0 bg-gradient-to-r from-black via-black/60 to-transparent z-10" /> to establish a dark left side so the text reads clearly, pushing out to transparency on the right.
Card Text Content (relative z-20):
Titles are text-4xl font-semibold mb-6 tracking-tight text-white.
Descriptions are text-lg text-zinc-400 leading-relaxed.
Card 1: "Real-time <br/> Analytics" / "Monitor every transaction and movement across multiple chains in a single, unified interface."
Card 2: "Smart <br/> Security" / "Enterprise-grade protection for your digital assets with multi-signature support and cold storage."
Card 3: "Automated Reporting" / "Generate tax-ready reports and performance audits with a single click. Stay compliant across all jurisdictions."
G. Seamless Fusion Phase: Combined CTA & Footer
You MUST combine the CTA section and the Footer inside exactly ONE parent wrapper so the background video plays seamlessly under both of them.
Parent Container: ref={combinedSectionRef}. className="relative z-20 bg-black overflow-hidden".
Shared Background Video Structure:
Placed immediately inside the parent container: <div className="absolute inset-0 z-0">.
Video Tag: ref={combinedVideoRef}. URL: https://t.co/PuOcA9pWL5. Class bounds: w-full h-full object-cover opacity-30. Note: 30% opacity.
Video Gradient Mask: To ensure smooth blending with the section above and below, layer an absolute div over the video: bg-gradient-to-b from-black via-transparent to-black z-10.
CTA Block Zone:
Wrapper: <div className="relative z-20 py-48 text-center"><div className="max-w-5xl mx-auto px-6">.
Floating Logo: Centered Box (w-20 h-20 bg-zinc-900/80 backdrop-blur-xl border border-zinc-800 rounded-[24px] shadow-2xl) containing the Logo. Animates in using .animate-float-up mb-16.
Headline: .animate-float-up text-[80px] leading-[1] tracking-[-0.05em] font-semibold mb-10 text-white. Text is: "Ready to scale your <br/> digital wealth?". (CRITICAL: Every word is pure white. <span className="text-white"> ).
Description: .animate-float-up-delay text-xl text-zinc-400 mb-16 max-w-2xl mx-auto leading-relaxed. "Join thousands of investors who trust our platform..."
Buttons (.animate-float-up-delay-3 flex flex-col sm:flex-row items-center justify-center gap-8):
Solid White Button ("Get Started Now"): bg-white text-black px-12 py-5 rounded-full font-bold text-lg hover:bg-zinc-200 transition-all transform hover:scale-105 shadow-[0_20px_40px_rgba(255,255,255,0.1)].
Outline Button ("View Documentation"): Transparent style border border-zinc-800 text-white px-12 py-5 rounded-full font-bold text-lg hover:bg-white/5 transition-all.
Footer Block Zone:
Directly follows CTA inside the master wrapper. <footer className="relative z-20 py-24">.
Top layout: Flex between left branding column and right 3-column grid (gap-16 mb-24).
Left Col: Logo alongside "CRYPTOFLOW" text (text-2xl font-semibold tracking-tighter). Short paragraph (text-zinc-500 max-w-xs leading-relaxed).
Right Col Grid: 3 columns (Platform, Company, Legal). Headers are text-xs font-bold text-zinc-400 uppercase tracking-widest. Links use flex flex-col gap-4 text-sm text-zinc-500 with hover:text-white transition-colors.
Standard Link text arrays. Platform: Services, How it Works, Pricing. Company: About Us, Careers, Contact. Legal: Privacy, Terms, Cookies.
Bottom Bar Wrapper: Flex layout horizontal (pt-12 flex justify-between items-center gap-6). DO NOT APPLY ANY BORDERS. NO border-t, NO border-zinc-900. It must float directly over the cinematic video space.
Copyright text: "© 2026 CryptoFlow. All rights reserved." (text-sm text-zinc-600).
Social Links Layout: Flex horizontal gap-8 text-xs text-zinc-500 uppercase tracking-widest font-bold. Links for Twitter, Discord, LinkedIn (hover:text-white).
Follow these instructions flawlessly, rendering the precise class names, video logic, math, and layout hooks.
