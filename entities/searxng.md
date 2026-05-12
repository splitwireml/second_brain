---
title: SearXNG
created: 2026-04-15
updated: 2026-04-18
type: entity
tags: [tools, ai-tools, open-source, search, self-hosted]
sources: [raw/articles/theahmadosman-agent-web-stack-2026-04-15.md, raw/articles/searxng-deep-technical-research-2026-04-18.md]
---

## Overview

SearXNG is a self-hosted metasearch engine — a privacy-respecting, hackable meta-search aggregator that queries multiple search providers and returns unified results. Written in Python/Flask, AGPL-licensed. It does NOT have its own index — it distributes queries across third-party backends.

## Role in Agent Web Stack

In [[theahmadosman]]'s "Agent Web Stack," SearXNG serves as the **candidate source discovery** layer — the first stage in the pipeline:

```
SearXNG (candidate discovery) → [[firecrawl]] (known-URL scrape) → [[camoufox]] (JS/interaction)
```

Agents use SearXNG to discover candidate URLs before passing them to Firecrawl for deeper extraction.

## Engine Architecture

SearXNG has **221 engine modules** in `searx/engines/` (count of `def request` implementations). They fall into three distinct categories based on how they access search data:

### Category 1: Pure HTML Scraping (~120 engines)

The majority of engines make HTTP requests directly to the search engine's **public HTML endpoint** and parse the response using **lxml + XPath**.

**No API key required. Cost: free (but rate-limited/blocked by the target).**

Google is the canonical example (`searx/engines/google.py`):

```python
about = {
    "use_official_api": False,
    "require_api_key": False,
    "results": "HTML",
}

def request(query, params):
    # Builds URL: https://www.google.com/search?q=query
    # Sets cookies, User-Agent, Accept-Language headers
    params['url'] = query_url

def response(resp):
    dom = html.fromstring(resp.text)
    for result in eval_xpath_list(dom, '//a[@data-ved and not(@class)]'):
        title = extract_text(eval_xpath_getindex(result, './/div[@style]', 0))
        url = unquote(raw_url[7:].split("&sa=U")[0])  # strips Google redirector
        # ... thumbnail, content extraction
```

Google specifically uses a complex "async UI" request pattern — a randomly-generated `arc_id` valid for one hour, passed in a format mimicking the JavaScript UI callback. This is reverse-engineered scraping that extracts results normally only rendered via JS.

### Category 2: Official API (~10 engines)

Uses the engine's **official API endpoint** with structured JSON/XML responses. Often requires an API key configured in `settings.yml`.

**API key often required. Cost: free tier or pay-per-query.**

Brave Search API is the cleanest example (`searx/engines/braveapi.py`):

```python
about = {
    "use_official_api": True,
    "require_api_key": True,
    "results": "JSON",
}

api_key: str = ""  # set in settings.yml

def init(_):
    if not api_key:
        raise SearxEngineAPIException("No API key provided")

def request(query, params):
    params["headers"]["X-Subscription-Token"] = api_key
    params["url"] = f"https://api.search.brave.com/res/v1/web/search?q={query}"

def response(resp):
    data = resp.json()
    for result in data.get("web", {}).get("results", []):
        res.add(res.types.MainResult(
            url=result["url"],
            title=result["title"],
            content=result.get("description", ""),
        ))
```

Engines requiring API keys (all `inactive: true` by default):
- `braveapi` — Brave Search (free tier: 2,000 queries/month)
- `deepl` — DeepL translation
- `freesound` — Freesound audio search
- `azure` — Azure AI services
- `cloudflareai` — Cloudflare AI Workers
- `astrophysics_data_system` — NASA ADS API
- `springer` — Springer API
- `flickr` — Flickr API
- `core` — (inactive)
- `marginalia` — (requires API key)

### Category 3: Hybrid (Google Scholar prime example)

Has an official API but **chooses to scrape HTML instead** — typically because the API is rate-limited, expensive, or yields fewer results than scraping.

```python
about = {
    "official_api_documentation": "https://developers.google.com/custom-search/",
    "use_official_api": False,   # ← intentionally scraping
    "require_api_key": False,
    "results": "HTML",
}
```

## Engine Loading Pipeline

**File**: `searx/engines/__init__.py`

```
settings.yml (YAML list)
       ↓
load_engines() → for each engine_data dict:
       ↓
  load_engine(engine_data):
    1. module_name = engine_data['engine']  # e.g. "google"
    2. load_module(f"{module_name}.py", ENGINE_DIR)
    3. update_engine_attributes(engine, engine_data)  # merge YAML config
    4. update_attributes_for_tor(engine)  # adjust URL for Tor if needed
    5. set_traits(engine)  # load region/language mappings from engine_traits.json
    6. call_engine_setup(engine, engine_data)  # run init() if present
    7. is_engine_active()  # check inactive flag + onion category + tor
    8. register_engine(engine)  # add to global engines[] + categories[] dicts
```

## Engine Interface Contract

Every engine module implements two functions:

### `request(query: str, params: OnlineParams) -> None`
Builds the HTTP request by writing into the `params` dict: `url`, `method`, `headers`, `cookies`, `data`. Does NOT send the request.

### `response(resp: SXNG_Response) -> EngineResults`
Receives the HTTP response, parses it (XPath/JSON/XML), returns an `EngineResults` container.

Optional: `init(engine_data) -> bool` — validates config at startup.

## Search Query Flow

**File**: `searx/search/__init__.py`

```
User query: "AI news"
       ↓
SearchQuery(engineref_list=[EngineRef(name, category), ...])
       ↓
Search().search():
  1. search_external_bang()   # e.g. !w → Wikipedia redirect
  2. search_answerers()     # built-in Q&A (calculator, etc.)
  3. search_standard():
       ↓
     _get_requests() → builds list of (engine_name, query, params)
     search_multiple_requests():
       - for each engine, spawns threading.Thread
       - each calls OnlineProcessor.search()
       - threads timeout after actual_timeout
       ↓
     OnlineProcessor._search_basic():
       1. engine.request(query, params)   ← fills in URL
       2. _send_http_request(params)       ← httpx GET/POST
       3. engine.response(response)        ← parses results
       4. extend_container(result_container, results)
```

**Threading model**: Each engine runs in its own thread, all concurrent. Slow engines are killed by timeout. Results stream in as threads complete.

## Rate Limiting

**File**: `searx/limiter.toml` + `searx/limiter.py`

Built-in distributed rate limiter using Redis (or in-process fallback). Operators configure per-engine and per-IP rate limits. Engines can declare `using_tor_proxy: true` for onion-category engines.

## API Keys vs SERP: Comparison

| Factor | SearXNG (most engines) | SERP APIs (Google SerpAPI, Bing API) |
|--------|------------------------|-------------------------------------|
| API key required | **No** | Yes |
| Cost to operate | ~$5-20/mo hosting | Per-query credits ($5-100+/month) |
| Data source | Scrapes public HTML | Official licensed API |
| Reliability | Breaks when target changes HTML | Stable API contract |
| Rate limits | Target blocks your IP | Quota-based |
| Legal risk | Target's ToS prohibits scraping | Licensed commercial use |

**SearXNG's economic model**: Near-zero marginal cost per query. Operators risk IP blocks from Google/Bing instead of paying per-query fees.

## Key Source Files

| File | Purpose |
|------|---------|
| `searx/engines/__init__.py` | Engine loading, registration, `load_engines()` |
| `searx/engines/base.py` | Example API engine (BASE-search, no key) |
| `searx/engines/google.py` | Example scraping engine (518 lines) |
| `searx/engines/braveapi.py` | Example API-key engine (Brave, requires key) |
| `searx/search/__init__.py` | `Search` class, threading, query dispatch |
| `searx/search/processors/online.py` | `OnlineProcessor` — HTTP request/response |
| `searx/enginelib/traits.py` | Language/region trait mappings |
| `searx/data/engine_traits.json` | JSON blob of all engine language/region codes |

## Relationship to Other Tools

- Used alongside [[firecrawl]] for a two-stage search-and-scrape pipeline
- Used with [[camoufox]] as the browser layer for JavaScript-heavy pages
- Contrast with hosted search APIs (Bing API, SerpAPI) — SearXNG is fully self-hosted with no per-query costs
- Part of [[agent-web-stack]] — the first stage (candidate source discovery)
- `[[searxng-self-host-and-backend-query]]` — confirmed self-hostable (VPS), runs as pure JSON API backend without UI

## Sources

- `raw/articles/theahmadosman-agent-web-stack-2026-04-15.md`
- `raw/articles/searxng-deep-technical-research-2026-04-18.md` — deep technical analysis from source code
- searxng.org
- github.com/searxng/searxng
