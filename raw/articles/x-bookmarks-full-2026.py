#!/Users/mali/venvs/web-tools/bin/python3
"""
X Bookmarks 2026 — Full Week-by-Week Scraper
Scrapes X bookmarks by scrolling down until a date cutoff is reached.
Organizes by week, optionally extracts page titles per tweet.
Outputs weekly MD files to X-Bookmarks-Archive/ + master JSON.

Usage:
    # Scrape only 2026 (stop at Jan 1, no title extraction)
    python x-bookmarks-full-2026.py --until 2026-01-01

    # Scrape down to March 15, 2026
    python x-bookmarks-full-2026.py --until 2026-03-16

    # Scrape everything with title extraction
    python x-bookmarks-full-2026.py --until 2020-01-01 --extract-titles
"""

import os, time, json, argparse
from datetime import datetime, timezone, timedelta

from camoufox.sync_api import Camoufox

VAULT = os.path.expanduser('~/Documents/Obsidian_Vault/AI-Second-Brain')
OUTPUT_DIR = os.path.join(VAULT, 'X-Bookmarks-Archive')
PROFILE_DIR = os.path.expanduser('~/.hermes/x_profile')

os.makedirs(OUTPUT_DIR, exist_ok=True)


def week_range(dt):
    monday = dt - timedelta(days=dt.weekday())
    sunday = monday + timedelta(days=6)
    return monday.strftime('%Y-%m-%d'), sunday.strftime('%Y-%m-%d')


def scrape_bookmarks_until(cutoff_date):
    """
    Scroll bookmarks until we hit tweets older than cutoff_date.
    cutoff_date: string like '2026-03-16' — stops when tweet date < this.
    Returns list of {url, date} dicts or None if session expired.
    """
    with Camoufox(
        persistent_context=True,
        user_data_dir=PROFILE_DIR,
        headless=True,
        humanize=True,
    ) as context:
        page = context.new_page()
        page.goto('https://x.com/i/bookmarks', timeout=30000)
        time.sleep(5)

        if '/login' in page.url:
            print("ERROR: Session expired. Need fresh cookies.")
            return None

        # Try to sort by Latest
        try:
            sort_btn = page.query_selector('div[data-testid="caret"]')
            if sort_btn:
                sort_btn.click()
                time.sleep(1)
                latest = page.query_selector('div[role="menuitem"]:has-text("Latest")')
                if latest:
                    latest.click()
                    time.sleep(3)
                    print("[info] Sorted by Latest")
        except:
            print("[warn] Could not sort by Latest — using default (Top)")

        seen = set()
        all_bookmarks = []
        scroll_attempts = 0
        max_scrolls = 600
        scroll_stall_count = 0
        prev_total = 0

        print(f"[info] Scrolling until tweets older than {cutoff_date}...")

        while scroll_attempts < max_scrolls:
            articles = page.query_selector_all('article[role="article"]')
            new_this_round = 0

            for article in articles:
                try:
                    link = article.query_selector('a[href*="/status/"]')
                    time_el = article.query_selector('time')
                    if link and time_el:
                        href = link.get_attribute('href')
                        dt_str = time_el.get_attribute('datetime') or ''

                        if dt_str:
                            tweet_date = dt_str[:10]
                            if tweet_date < cutoff_date:
                                print(f"[info] Hit tweet dated {tweet_date} "
                                      f"(before cutoff {cutoff_date}) — stopping")
                                return all_bookmarks

                        if href and href not in seen:
                            seen.add(href)
                            all_bookmarks.append({
                                "url": f"https://x.com{href}",
                                "date": dt_str,
                            })
                            new_this_round += 1
                except:
                    continue

            current_total = len(all_bookmarks)
            print(f"[scroll {scroll_attempts}] {current_total} bookmarks "
                  f"(+{new_this_round} new)")

            # Stalled: no new bookmarks this scroll
            if current_total == prev_total:
                scroll_stall_count += 1
            else:
                scroll_stall_count = 0
                prev_total = current_total

            # If stalled for many scrolls, try a bigger push
            if scroll_stall_count >= 3:
                print(f"[info] Stalled at scroll {scroll_attempts}, "
                      f"trying bigger scroll to force lazy load...")
                page.evaluate("window.scrollBy(0, 5000)")
                time.sleep(4)
                # Check if we got new articles
                new_count = len(page.query_selector_all('article[role="article"]'))
                if new_count <= len(articles):
                    scroll_stall_count += 2  # penalize, will hit 8 and exit
                continue

            # If stalled 8+ times with big scrolls too, we're at the end
            if scroll_stall_count >= 8:
                print("[info] End of content — no more bookmarks loading")
                break

            prev_total = current_total

            # Scroll down
            page.evaluate("window.scrollBy(0, 1500)")
            time.sleep(2)

            # Click "See new posts" if visible
            try:
                btn = page.locator('button:has-text("See new posts")')
                if btn.count() > 0:
                    btn.first.click()
                    time.sleep(2)
            except:
                pass

            scroll_attempts += 1

        print(f"\n[done] Total bookmarks collected: {len(all_bookmarks)}")
        return all_bookmarks


def organize_by_week(bookmarks):
    weekly = {}
    for bm in bookmarks:
        dt_str = bm.get('date', '')
        try:
            dt = datetime.fromisoformat(dt_str.replace('Z', '+00:00')) if dt_str else datetime.now(timezone.utc)
        except:
            dt = datetime.now(timezone.utc)

        monday_str, sunday_str = week_range(dt)
        week_key = f"Week of {monday_str}"
        if week_key not in weekly:
            weekly[week_key] = {'monday': monday_str, 'sunday': sunday_str, 'tweets': []}
        weekly[week_key]['tweets'].append({'url': bm['url'], 'date': dt_str})
    return weekly


def extract_titles(weekly):
    with Camoufox(
        persistent_context=True,
        user_data_dir=PROFILE_DIR,
        headless=True,
        humanize=True,
    ) as context:
        total = sum(len(w['tweets']) for w in weekly.values())
        processed = 0
        for week_key in sorted(weekly.keys()):
            week_data = weekly[week_key]
            print(f"\n[week] {week_key}: {len(week_data['tweets'])} bookmarks")
            for tweet in week_data['tweets']:
                processed += 1
                url = tweet['url']
                pg = context.new_page()
                try:
                    pg.goto(url, timeout=10000, wait_until='domcontentloaded')
                    time.sleep(0.8)
                    title = pg.title()
                    tweet['title'] = title
                    if '/login' in pg.url:
                        print(f"  [{processed}/{total}] SESSION EXPIRED — stopping")
                        return
                except Exception as e:
                    tweet['title'] = f"Error: {str(e)[:60]}"
                finally:
                    pg.close()
                    time.sleep(0.3)
                if processed % 20 == 0:
                    print(f"  [{processed}/{total}] processed")
        print(f"\n[done] Titles extracted: {processed}")


def save_outputs(weekly):
    master = []
    for week_key in sorted(weekly.keys()):
        wd = weekly[week_key]
        monday = wd['monday']
        tweets = wd['tweets']

        lines = [
            f"# X Bookmarks — {week_key}", "",
            f"> **Period:** {monday} to {wd['sunday']}",
            f"> **Count:** {len(tweets)}",
            f"> **Extracted:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "", "---", "",
        ]
        for t in tweets:
            title = t.get('title', 'No title extracted')
            url = t.get('url', '')
            date = t.get('date', '')[:10] if t.get('date') else ''
            lines.append(f"- **{date}** — [{title}]({url})")
        lines.append("")

        file_path = os.path.join(OUTPUT_DIR, f'X-Bookmarks-{monday}.md')
        with open(file_path, 'w') as f:
            f.write('\n'.join(lines))
        print(f"[saved] {file_path} ({len(tweets)} tweets)")
        master.extend(tweets)

    master_path = os.path.join(OUTPUT_DIR, 'X-Bookmarks-2026-Master.json')
    with open(master_path, 'w') as f:
        json.dump({
            'exported': datetime.now().isoformat(),
            'total_bookmarks': len(master),
            'weeks': {k: v['tweets'] for k, v in weekly.items()},
        }, f, indent=2)
    print(f"\n[master] {master_path} ({len(master)} total)")


def main():
    parser = argparse.ArgumentParser(
        description='Scrape X bookmarks week-by-week into Obsidian vault.')
    parser.add_argument(
        '--until', required=True,
        help='Stop scrolling when a tweet date is BEFORE this (YYYY-MM-DD). '
             'Use 2026-01-01 for 2026 only, 2020-01-01 for everything.')
    parser.add_argument(
        '--extract-titles', action='store_true',
        help='Visit each bookmark URL to extract page title (slow but thorough).')
    args = parser.parse_args()

    print("=" * 60)
    print("X Bookmarks Scraper")
    print(f"Cutoff: scroll until tweets older than {args.until}")
    print(f"Title extraction: {'ON' if args.extract_titles else 'OFF'}")
    print("=" * 60)

    print(f"\n[step 1] Scraping bookmark URLs (stop before {args.until})...")
    bookmarks = scrape_bookmarks_until(args.until)
    if not bookmarks:
        print("No bookmarks found or session expired. Exiting.")
        return

    print(f"\n[step 2] Organizing {len(bookmarks)} bookmarks by week...")
    weekly = organize_by_week(bookmarks)
    print(f"[info] {len(weekly)} weeks covered")
    for wk in sorted(weekly.keys()):
        print(f"  {wk}: {len(weekly[wk]['tweets'])} bookmarks")

    if args.extract_titles:
        total = sum(len(w['tweets']) for w in weekly.values())
        print(f"\n[step 3] Extracting titles for {total} bookmarks...")
        extract_titles(weekly)
    else:
        print("\n[step 3] Skipping title extraction (use --extract-titles)")

    print("\n[step 4] Saving outputs...")
    save_outputs(weekly)

    print("\n" + "=" * 60)
    print("DONE")
    print("=" * 60)


if __name__ == '__main__':
    main()
