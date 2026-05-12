#!/usr/bin/env python3
"""
X Bookmarks Weekly Scraper — Hermes cron job
Extracts tweets from authenticated X bookmarks page (past 7 days only).
Outputs to Obsidian vault.
"""

from datetime import datetime, timedelta, timezone
import sys, json, os, time, re

sys.path.insert(0, '/Users/mali/venvs/web-tools/lib/python3.13/site-packages')
from camoufox.sync_api import Camoufox

# Only run on Mondays from April 13 2026 onwards
MIN_DATE = datetime(2026, 4, 13, tzinfo=timezone.utc)
if datetime.now(timezone.utc) < MIN_DATE:
    print(f"[skip] Not yet enabled. Runs from {MIN_DATE.date()} onwards.")
    sys.exit(0)

VAULT   = os.path.expanduser('~/Documents/Obsidian_Vault/AI-Second-Brain')

# ── Load cookies from JSON (EditThisCookie export with sameSite fix) ──────────
SAMESITE_MAP = {
    "unspecified": "None",
    "lax": "Lax",
    "strict": "Strict",
    "no_restriction": "None",
}

with open("/tmp/x_cookies.json") as f:
    raw_cookies = json.load(f)

cookies = []
for c in raw_cookies:
    cookie = {
        "name": c["name"],
        "value": c["value"],
        "domain": c["domain"],
        "path": c["path"],
        "secure": c.get("secure", False),
        "httpOnly": c.get("httpOnly", False),
        "sameSite": SAMESITE_MAP.get(c.get("sameSite", "").lower(), "None"),
    }
    if not c.get("session", True) and "expirationDate" in c:
        cookie["expires"] = c["expirationDate"]
    cookies.append(cookie)

print(f"[cookies] {len(cookies)} loaded")

# ── Extract tweet data ────────────────────────────────────────────────────────
def extract_tweet(page, url):
    result = {
        "url": url, "author_handle": "", "author_name": "",
        "text": "", "date": "", "title": "",
        "reply_count": "", "retweet_count": "", "like_count": "",
        "quote_count": "", "images": [], "error": None
    }
    try:
        result["title"] = page.title()
    except:
        pass
    try:
        for sel in ['[data-testid="tweetText"]', 'div[data-testid="tweetText"]']:
            try:
                text = page.inner_text(sel, timeout=3000)
                if text and len(text) > 5:
                    result["text"] = text
                    break
            except:
                continue
        if not result["text"]:
            try:
                article = page.query_selector('article[role="article"]')
                if article:
                    ps = article.query_selector_all('p')
                    result["text"] = ' '.join(
                        p.inner_text() for p in ps if p.inner_text().strip()
                    )
            except:
                pass
    except Exception as e:
        result["error"] = str(e)

    for key, sel in {
        'reply_count': '[data-testid="reply"]',
        'retweet_count': '[data-testid="retweet"]',
        'like_count': '[data-testid="like"]',
        'quote_count': '[data-testid="quote"]',
    }.items():
        try:
            el = page.query_selector(sel)
            if el:
                result[key] = el.inner_text().strip()
        except:
            pass

    try:
        time_el = page.query_selector('time')
        if time_el:
            result["date"] = time_el.get_attribute('datetime') or time_el.inner_text()
    except:
        pass

    try:
        result["images"] = [
            img.get_attribute('src')
            for img in page.query_selector_all('img[alt="Image"]')
            if img.get_attribute('src')
        ]
    except:
        pass

    return result

# ── Scrape bookmarks page ───────────────────────────────────────────────────
def scrape_bookmarks():
    cutoff = datetime.now(timezone.utc) - timedelta(days=7)
    bookmark_urls = []

    PROFILE_DIR = os.path.expanduser('~/.hermes/x_profile')
    with Camoufox(persistent_context=True, user_data_dir=PROFILE_DIR, headless=True, humanize=True) as context:
        page = context.new_page()

        page.goto('https://x.com/i/bookmarks', timeout=20000)
        time.sleep(4)

        # Sort by Latest
        try:
            sort_btn = page.query_selector('div[data-testid="caret"]')
            if sort_btn:
                sort_btn.click()
                time.sleep(1)
                latest = page.query_selector('div[role="menuitem"]:has-text("Latest")')
                if latest:
                    latest.click()
                    time.sleep(2)
                    print("[bookmarks] Sorted by Latest")
        except Exception as e:
            print(f"[bookmarks] Sort: {e}")

        seen = set()
        scroll_attempts = 0
        max_scrolls = 60
        last_height = 0

        while scroll_attempts < max_scrolls:
            articles = page.query_selector_all('article[role="article"]')
            for article in articles:
                try:
                    link = article.query_selector('a[href*="/status/"]')
                    time_el = article.query_selector('time')
                    if link and time_el:
                        href = link.get_attribute('href')
                        dt_str = time_el.get_attribute('datetime') or ''
                        if href and href not in seen:
                            seen.add(href)
                            dt = datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
                            if dt >= cutoff:
                                bookmark_urls.append({
                                    "url": "https://x.com" + href,
                                    "bookmarked_at": dt_str
                                })
                except:
                    continue

            if bookmark_urls:
                oldest = bookmark_urls[-1]["bookmarked_at"]
                oldest_dt = datetime.fromisoformat(oldest.replace('Z', '+00:00'))
                if oldest_dt < cutoff:
                    bookmark_urls = [b for b in bookmark_urls
                                     if datetime.fromisoformat(
                                         b["bookmarked_at"].replace('Z','+00:00')
                                     ) >= cutoff]
                    print(f"[bookmarks] Cutoff reached. {len(bookmark_urls)} past-week URLs.")
                    break

            page.evaluate("window.scrollBy(0, 800)")
            time.sleep(1.5)
            scroll_attempts += 1

            new_height = page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                page.evaluate("window.scrollBy(0, 2000)")
                time.sleep(2)
                new_height = page.evaluate("document.body.scrollHeight")
                if new_height == last_height:
                    print(f"[bookmarks] End of content at scroll {scroll_attempts}")
                    break
            last_height = new_height

            if scroll_attempts % 10 == 0:
                print(f"[bookmarks] Scrolled {scroll_attempts}, collected {len(bookmark_urls)} past-week URLs")

        print(f"[bookmarks] Total: {len(bookmark_urls)} past-week bookmarks")
        browser.close()

    return bookmark_urls

# ── Categorize ──────────────────────────────────────────────────────────────
def categorize(text, url):
    text_lower = (text or "").lower()
    if any(k in text_lower for k in [
        "dubai","iran","uae","missile","ballistic","gulf","hormuz",
        "mossad","emirates","israel","war","taiwan","china","us navy"
    ]):
        return "Geopolitics & UAE"
    if any(k in text_lower for k in [
        "llm","model","ai","gpt","claude","hermes","openai","langchain",
        "rag","embed","unsloth","quantiz","mlx","hf ","huggingface",
        "local model","ollama","vllm","qwen","mistral","gemini",
        "whatcani","localai","text-to"
    ]):
        return "AI & Tech"
    if any(k in text_lower for k in [
        "github","open source","open-source","rust","git","release","npm"
    ]):
        return "Open Source"
    if any(k in text_lower for k in [
        "sport","game","football","steam","app","life","health",
        "nutrition","music","movie","netflix","series","vacation"
    ]):
        return "Entertainment & Lifestyle"
    return "General"

# ── Render note ───────────────────────────────────────────────────────────────
def render_note(tweets, week_start, week_end):
    sections = {}
    for t in tweets:
        sections.setdefault(t.get("category","General"), []).append(t)

    lines = [
        f"# X Bookmarks — Week of {week_start.strftime('%Y-%m-%d')}",
        "",
        f"> **Extracted:** {datetime.now().strftime('%Y-%m-%d %H:%M')} via Hermes cron",
        f"> **Week:** {week_start.strftime('%Y-%m-%d')} → {week_end.strftime('%Y-%m-%d')}",
        f"> **Tweet count:** {len(tweets)}",
        "",
        "---",
        "",
        "## Bookmark Table",
        "",
        "| Date | Category | Author | Topic / Headline | URL |",
        "|------|----------|---------|------------------|-----|",
    ]

    # Extract author from title (format: "(2) Handle on X: \"text\"")
    def extract_handle(title):
        import re
        m = re.search(r'\((?:[0-9]+ )?([^/]+) on X', title or "")
        return "@" + m.group(1).strip() if m else ""

    def slug(text):
        t = (text or "").replace('\n', ' ').strip()
        return t[:80] + ('...' if len(t) > 80 else '')

    for t in sorted(tweets, key=lambda x: x.get("date", "")):
        dt = t.get("date", "")[:10]
        cat = t.get("category", "General")
        author = extract_handle(t.get("title", ""))
        topic = slug(t.get("text", "") or t.get("title", ""))
        url = t.get("url", "")
        lines.append(f"| {dt} | {cat} | {author} | {topic} | [link]({url}) |")

    lines.extend(["", "---", ""])

    for cat, items in sections.items():
        lines.append(f"## {cat}")
        lines.append("")
        for t in items:
            dt = t.get("date", "")[:10]
            url = t.get("url", "")
            text = t.get("text", "").replace('\n', ' ').strip()
            title = t.get("title", "")
            rt = t.get("retweet_count", "")
            likes = t.get("like_count", "")
            lines.append(f"### Tweet — {dt}")
            lines.append(f"- **URL:** {url}")
            if title:
                lines.append(f"- **Title:** {title[:120]}")
            if text:
                lines.append(f"- **Text:** {text[:300]}{'...' if len(text) > 300 else ''}")
            if rt or likes:
                lines.append(f"- **Engagement:** RT {rt} · Likes {likes}")
            lines.append("")
        lines.append("")

    lines.extend([
        "---",
        "## Raw Data",
        "Full extraction data: `x-bookmarks-weekly.json`",
        "",
        "## Tags",
        "#x-bookmarks #weekly #cron #x",
    ])

    return '\n'.join(lines)

# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    week_end   = datetime.now(timezone.utc)
    week_start = week_end - timedelta(days=7)

    print(f"[main] Past 7 days: {week_start.date()} → {week_end.date()}")
    bookmark_urls = scrape_bookmarks()

    if not bookmark_urls:
        print("[main] No new bookmarks this week.")
        sys.exit(0)

    tweets = []

    with Camoufox(persistent_context=True, user_data_dir=PROFILE_DIR, headless=True, humanize=True) as context:

        for i, bk in enumerate(bookmark_urls):
            url = bk["url"]
            print(f"[{i+1}/{len(bookmark_urls)}] {url}")
            page = context.new_page()
            try:
                page.goto(url, timeout=15000)
                time.sleep(2)
                tweet = extract_tweet(page, url)
                tweet["bookmarked_at"] = bk["bookmarked_at"]
                tweet["category"] = categorize(tweet["text"], tweet["url"])
                tweets.append(tweet)
                print(f"  [{tweet['category']}] {tweet['text'][:60]}...")
            except Exception as e:
                print(f"  FAILED: {e}")
                tweets.append({"url": url, "error": str(e), "category": "Error"})
            page.close()
            time.sleep(1)

        browser.close()

    # Save raw JSON
    raw_path = os.path.join(VAULT, 'x-bookmarks-weekly.json')
    os.makedirs(os.path.dirname(raw_path), exist_ok=True)
    with open(raw_path, 'w') as f:
        json.dump({
            "week_start": week_start.isoformat(),
            "week_end": week_end.isoformat(),
            "tweets": tweets
        }, f, indent=2)

    # Save note
    note = render_note(tweets, week_start, week_end)
    note_path = os.path.join(VAULT, 'X-Bookmarks-Weekly.md')
    with open(note_path, 'w') as f:
        f.write(note)

    cats = len(set(t['category'] for t in tweets))
    print(f"\n[done] {len(tweets)} tweets, {cats} categories")
    print(f"  JSON  → {raw_path}")
    print(f"  Note  → {note_path}")

if __name__ == '__main__':
    main()
