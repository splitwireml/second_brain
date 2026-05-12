---
title: Searxng Deep Technical Research 2026 04 18
created: 2026-04-18
updated: 2026-04-18
type: raw
---
# SearXNG Deep Technical Research

## Research Questions
1. **How does SearXNG implement search engines?** (architecture, engine discovery, data flow)
2. **Does SearXNG depend on API keys** like SERP does? (cost model, authentication, scraping vs. API)

---

## Architecture Overview

SearXNG is a **metasearch engine aggregator** written in Python/Flask. It does NOT have its own index. Instead, it distributes user queries across **third-party search backends** (Google, Bing, Brave, academic APIs, etc.) and aggregates the results.

### Three Engine Categories

SearXNG categorizes its 133 engines into three distinct access patterns:

#### Category 1: Pure HTML Scraping (majority — ~120 engines)
- Makes HTTP requests directly to the search engine's **public HTML endpoint**
- Parses the HTML/JS response using **lxml + XPath** to extract results
- **No API key required**
- **Cost: free** (but rate-limited/blocked by the target)
- Examples: `google.py`, `bing.py`, `duckduckgo.py`, `baidu.py`

**How scraping works** (Google as case study):
```
request() → builds URL: https://www.google.com/search?q=query
           → sets cookies, User-Agent, Accept-Language headers
           → returns params dict with full URL

response() → receives httpx response
           → html.fromstring(resp.text)
           → XPath: //a[@data-ved and not(@class)] to find result links
           → extracts title, URL, snippet, thumbnail via XPath/extract_text()
           → returns EngineResults object
```

Google specifically uses a complex "async" UI request pattern where a random `arc_id` is generated hourly to mimic the JavaScript UI callback format. This is reverse-engineered behavior to extract results that would normally only appear via JS rendering.

#### Category 2: Official API (minority — ~10 engines)
- Uses the engine's **official API endpoint** with structured JSON/XML responses
- **API key often required** (set in settings.yml, passed to `api_key` engine variable)
- **Cost: free tier or pay-per-query** depending on the service
- Examples: `braveapi.py`, `base.py` (BASE-search), `deepl.py`, `freesound.py`

**API key flow** (Brave API as case study):
```python
# settings.yml
- name: braveapi
  engine: braveapi
  api_key: 'YOUR-API-KEY'  # required

# braveapi.py
def init(_):
    if not api_key:
        raise SearxEngineAPIException("No API key provided")

def request(query, params):
    params["headers"]["X-Subscription-Token"] = api_key
    params["url"] = f"https://api.search.brave.com/res/v1/web/search?q={query}"
```

#### Category 3: Hybrid (few engines)
- Have an official API but **choose to scrape HTML instead** (often for better results or to avoid API limits)
- Google is the prime example: has a Custom Search API but `use_official_api: False`
- `google.py` about block: `"use_official_api": False, "require_api_key": False`

---

## Engine Loading Pipeline

**File**: `searx/engines/__init__.py`

```
settings.yml (YAML list)
       ↓
load_engines() → for each engine_data dict:
       ↓
  load_engine(engine_data):
    1. module_name = engine_data['engine']  # e.g. "google"
    2. load_module(f"{module_name}.py", ENGINE_DIR)  # loads searx/engines/google.py
    3. update_engine_attributes(engine, engine_data)  # merge YAML config onto module
    4. update_attributes_for_tor(engine)  # adjust URL for Tor if needed
    5. set_traits(engine)  # load region/language mappings from engine_traits.json
    6. call_engine_setup(engine, engine_data)  # run init() function if present
    7. is_engine_active()  # check inactive flag + onion category + tor requirement
    8. register_engine(engine)  # add to global `engines` dict + `categories` dict
```

**Engine shortnames**: Users can use `!g query` to search Google directly. The `engine_shortcuts` dict maps these shortcuts back to engine names.

---

## Engine Interface Contract

Every engine module must implement two functions:

### `request(query: str, params: OnlineParams) -> None`
- Builds the HTTP request URL/headers/data
- Writes directly into the `params` dict:
  - `params['url']` — the full URL to fetch
  - `params['method']` — GET or POST
  - `params['headers']` — additional headers
  - `params['cookies']` — cookies to send
  - `params['data']` — POST form data
- Does NOT actually send the request — just prepares the params

### `response(resp: SXNG_Response) -> EngineResults`
- Receives the HTTP response object
- Parses it (HTML XPath, JSON, XML depending on engine)
- Returns an `EngineResults` container with result items

### Optional: `init(engine_data) -> bool`
- Called once at startup
- Validates configuration (e.g., `braveapi` checks `api_key` is not empty)
- Returns False to mark engine inactive

---

## How a Search Query Flows

**File**: `searx/search/__init__.py`

```
User query: "AI news"
       ↓
SearchQuery model created with:
  - query: "AI news"
  - engineref_list: [list of EngineRef(name, category)]
  - lang, safesearch, pageno, time_range
       ↓
Search().search():
  1. search_external_bang()  # e.g. !w wiki → Wikipedia
  2. search_answerers()      # built-in Q&A (calculator, etc.)
  3. search_standard():
       ↓
     _get_requests():
       - for each EngineRef in engineref_list:
         - processor = PROCESSORS[engine_name]  # OnlineProcessor by default
         - request_params = processor.get_params(search_query, category)
         - append (engine_name, query, params) to requests list
       ↓
     search_multiple_requests():
       - for each request, spawn a threading.Thread
       - each thread calls: processor.search(query, params, container, ...)
       - threads timeout after actual_timeout
       ↓
     OnlineProcessor.search():
       - init_network_in_thread()  # set timeout, httpx client
       - _search_basic():
         - engine.request(query, params)  ← fills in URL
         - _send_http_request(params)     ← actually HTTP GET/POST
         - engine.response(response)      ← parses results
         - extend_container(result_container, results)
```

**Threading model**: Each engine is searched in its own thread. All engine threads run concurrently. Thread timeout kills slow engines. Results stream in as threads complete.

---

## Rate Limiting / Abuse Protection

**File**: `searx/limiter.toml` + `searx/limiter.py`

SearXNG has a built-in **distributed rate limiter** using Redis (or in-process fallback). Operators configure:
- Per-engine request rate limits
- Per-IP request rate limits
- Whether Tor exit nodes are allowed

Engines can declare `using_tor_proxy: true` to route through Tor for onion-category engines.

---

## API Key / Token System

### Which engines require API keys?
- `braveapi` — Brave Search API key
- `deepl` — DeepL translation API
- `freesound` — Freesound API
- `azure` — Azure AI services
- `cloudflareai` — Cloudflare AI
- `astrophysics_data_system` — NASA ADS API
- `springer` — Springer API
- `flickr` — Flickr API
- `core` — (inactive, requires API key)
- `marginalia` — (requires API key)

These are all **OFF by default** (`inactive: true`) and require users to:
1. Obtain an API key from the service
2. Add it to `settings.yml`
3. Uncomment/activate the engine

### Token-based auth
Engines that need auth use the `tokens: []` setting in settings.yml for per-user quotas, and the global `api_key` variable for service-level authentication. Tokens are passed via HTTP headers (e.g., `X-Subscription-Token` for Brave).

### engines[] tokens vs user[] tokens
- `settings.yml` → `engines[name].tokens`: per-engine API tokens (e.g., paid SERP quota)
- `settings.yml` → `server.tokens`: admin API tokens for SearXNG's own internal API

---

## Answering: Does SearXNG Depend on API Keys Like SERP?

**No, not primarily.** SearXNG is designed to NOT require API keys for the majority of its engines.

| Factor | SearXNG | SERP (Google/SerpAPI) |
|--------|---------|----------------------|
| API key required | No (most engines) | Yes |
| Cost to operate | Near zero (except Brave/deepl/etc.) | Per-query SERP credits |
| Data source | Scrapes public HTML | Official Google API |
| Reliability | Breaks when Google changes HTML | Stable API contract |
| Rate limits | Target blocks you | Quota-based |
| Legal risk | Target's ToS prohibits scraping | Licensed use |

**SearXNG's economic model is radically different from SERP:**
- Running SearXNG costs only server hosting (~$5-20/month)
- No per-query costs
- BUT: Operators risk being IP-blocked by Google/Bing

**When you DO need API keys:**
- Brave Search (free tier: 2000 queries/month)
- DeepL (translation, metasearch engine for language pairs)
- Academic APIs (arXiv, NASA ADS, Springer)

**The hybrid model**: Google Scholar (no API) coexists with arXiv (free API), Brave (paid API), etc. SearXNG lets operators choose which trade-off to make per engine.

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `searx/engines/__init__.py` | Engine loading, registration, `load_engines()` |
| `searx/engines/base.py` | Example API engine (BASE-search) |
| `searx/engines/google.py` | Example scraping engine (Google web) |
| `searx/engines/braveapi.py` | Example API-key engine (Brave) |
| `searx/search/__init__.py` | `Search` class, threading, query dispatch |
| `searx/search/processors/online.py` | `OnlineProcessor` — HTTP request/response |
| `searx/enginelib/traits.py` | Language/region trait mappings |
| `searx/data/engine_traits.json` | JSON blob of all engine language/region codes |
| `searx/limiter.toml` | Rate limit configuration |
| `searxng.data/engine_descriptions.json` | Human-readable engine descriptions |

---

## Engine Count Breakdown

```
Total engines: 221 (grep -c "def request" across all .py files in engines/)

API-key-required (inactive by default): ~10
  - braveapi, deepl, freesound, azure, cloudflareai,
    astrophysics_data_system, springer, flickr, core, marginalia

HTML-scraping (no API key): ~120+
  - google, bing, bing_images, bing_news, baidu, yandex,
    duckduckgo, qwant, ecosia, etc.

Official API without key: ~10
  - base (BASE-search), archlinux (AUR), wikidata, etc.
```

---

## Research Metadata
- Source: github.com/searxng/searxng (cloned 2026-04-18)
- Research conducted: 2026-04-18
- Cloned repo: ~/Documents/Research/searxng/sources/searxng
