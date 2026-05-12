---
title: LEANN Vector Database
created: 2026-03-31
updated: 2026-03-31
type: concept
tags: [database]
sources: [raw/articles/x-bookmarks-2026.md]
---

     1|# LEANN Vector Database — Technical Research Report
     2|
     3|> **Date:** 2026-03-31
     4|> **Tags:** #vector-database #leann #rag #embeddings #research
     7|---
     8|
     9|## Overview
    10|
    11|LEANN (**L**ow-**E**mbedding **ANN**) is an open-source vector database designed for personal AI and privacy-first RAG workloads. Its core innovation is **graph-based selective recomputation** with high-degree preserving pruning — computing embeddings on-demand instead of storing them all, achieving **97% storage reduction** compared to traditional vector databases like FAISS.
    12|
    13|- **GitHub:** https://github.com/yichuan-w/LEANN
    14|- **Paper:** arXiv:2506.08276 (MLsys 2026 submission)
    15|- **Stars:** ~10.4k
    16|- **License:** MIT
    17|- **PyPI:** `leann`
    18|- **Languages:** Python (API) + C++ (backends)
    19|
    20|---
    21|
    22|## Core Architecture
    23|
    24|### The Storage Savings Trick
    25|
    26|Traditional vector databases store every document's embedding permanently. For 60M documents at 768-dimensional float32, that means:
    27|
    28|```
    29|60,000,000 × 768 × 4 bytes = ~201 GB
    30|```
    31|
    32|LEANN flips this. Instead of storing all embeddings, it:
    33|
    34|1. **Prunes** the HNSW/DiskANN graph to keep only a small fraction of nodes
    35|2. **Recomputes** embeddings on-demand at query time when they're needed
    36|
    37|The result: the same 60M documents fit in **6 GB** — a 97% reduction — with no accuracy loss.
    38|
    39|```
    40|Traditional FAISS:  201 GB
    41|LEANN:              6 GB     (97% savings)
    42|```
    43|
    44|### Index File Structure
    45|
    46|A LEANN index on disk consists of multiple files:
    47|
    48|| File | Purpose |
    49||------|---------|
    50|| `*.leann.meta.json` | Metadata — embedding model, dimensions, backend, config flags, is_compact/is_pruned |
    51|| `*.passages.jsonl` | Raw text passages — one JSON per line: `{"id", "text", "metadata"}` |
    52|| `*.passages.idx` | Pickle map of `passage_id → byte offset` for O(1) seek in JSONL |
    53|| `*.index` | The pruned graph (HNSW or DiskANN) — NOT full embeddings |
    54|| `*.ids.txt` | Ordered list of passage IDs for remapping |
    55|
    56|The `.passages.jsonl` is a simple flat store — no database required. The `.idx` file acts as an offset index so `get_passage(id)` can seek directly to the right byte position.
    57|
    58|### Query Execution Flow
    59|
    60|```
    61|User query string
    62|       ↓
    63|Compute query embedding
    64|  (via embedding server or direct, using stored model)
    65|       ↓
    66|Backend search (HNSW / DiskANN / IVF)
    67|  → Returns passage IDs + similarity scores
    68|       ↓
    69|PassageManager.get_passage(id)
    70|  → Seeks to byte offset in *.passages.jsonl via *.passages.idx
    71|  → Returns: {id, text, metadata}
    72|       ↓
    73|Return enriched SearchResult objects
    74|  SearchResult(id, score, text, metadata)
    75|```
    76|
    77|---
    78|
    79|## Embedding Model Support
    80|
    81|LEANN has a **fully pluggable embedding layer**. You can swap any embedding model without re-indexing the underlying data.
    82|
    83|### Supported Modes
    84|
    85|| Mode | Backend | Notes |
    86||------|---------|-------|
    87|| `sentence-transformers` | HuggingFace `sentence-transformers` library | Default. Any HF model. |
    88|| `openai` | OpenAI API or any OpenAI-compatible endpoint | Ollama, LM Studio, vLLM, etc. |
    89|| `mlx` | Apple Silicon MLX | For macOS with Apple Silicon |
    90|| `ollama` | Ollama local inference | Full privacy, no cloud |
    91|| `gemini` | Google Gemini embedding API | Cloud |
    92|
    93|### How to Configure
    94|
    95|```python
    96|from leann import LeannBuilder
    97|
    98|# Default: sentence-transformers
    99|builder = LeannBuilder(
   100|    backend_name="hnsw",
   101|    embedding_model="facebook/contriever",
   102|    embedding_mode="sentence-transformers",
   103|)
   104|
   105|# Ollama (local)
   106|builder = LeannBuilder(
   107|    backend_name="hnsw",
   108|    embedding_model="nomic-embed-text",
   109|    embedding_mode="openai",
   110|    embedding_options={
   111|        "base_url": "http://localhost:11434/v1",
   112|        "api_key": "***",  # dummy key for Ollama
   113|    }
   114|)
   115|
   116|# OpenAI-compatible endpoint (LM Studio, vLLM, etc.)
   117|builder = LeannBuilder(
   118|    backend_name="hnsw",
   119|    embedding_model="nomic-embed-text",
   120|    embedding_mode="openai",
   121|    embedding_options={
   122|        "base_url": "http://localhost:1234/v1",
   123|        "api_key": "***",
   124|    }
   125|)
   126|```
   127|
   128|### Known Models (from codebase)
   129|
   130|From `embedding_compute.py`:
   131|
   132|```
   133|nomic-embed-text         → 2048 tokens
   134|nomic-embed-text-v1.5   → 2048 tokens
   135|nomic-embed-text-v2     → 512 tokens
   136|mxbai-embed-large       → 512 tokens
   137|all-minilm              → 512 tokens
   138|bge-m3                  → 8192 tokens
   139|snowflake-arctic-embed  → 512 tokens
   140|text-embedding-3-small  → 8192 tokens
   141|text-embedding-3-large  → 8192 tokens
   142|text-embedding-ada-002  → 8192 tokens
   143|```
   144|
   145|Token limits are auto-detected for Ollama and LM Studio via API calls, with a registry fallback for others.
   146|
   147|### Prompt Templates
   148|
   149|You can prepend a prompt template to texts for embedding (useful for search-optimized embeddings):
   150|
   151|```python
   152|builder = LeannBuilder(
   153|    backend_name="hnsw",
   154|    embedding_model="nomic-embed-text",
   155|    embedding_mode="openai",
   156|    embedding_options={
   157|        "prompt_template": "query: {text}",   # for search
   158|        # or "document: {text}" for indexing
   159|    }
   160|)
   161|```
   162|
   163|---
   164|
   165|## Index Building and Updating
   166|
   167|### Build from Scratch
   168|
   169|```python
   170|from leann import LeannBuilder, LeannSearcher
   171|
   172|builder = LeannBuilder(backend_name="hnsw", embedding_model="nomic-embed-text")
   173|builder.add_text("Document 1 about AI and machine learning.", metadata={"source": "doc1"})
   174|builder.add_text("Document 2 about vector databases.", metadata={"source": "doc2"})
   175|builder.add_text("Document 3 about RAG systems.", metadata={"source": "doc3"})
   176|builder.build_index("/path/to/my-index")
   177|```
   178|
   179|### Incremental Updates
   180|
   181|LEANN supports incremental index updates using a **content-hash Merkle tree** (`FileSynchronizer`) to detect new, changed, and removed files:
   182|
   183|```python
   184|builder = LeannBuilder(backend_name="hnsw", embedding_model="nomic-embed-text")
   185|builder.add_text("New document 4 about embeddings.")
   186|builder.update_index("/path/to/existing-index")
   187|```
   188|
   189|**Change detection behavior:**
   190|
   191|| Event | Behavior |
   192||-------|----------|
   193|| New file added | Detected → chunked → embedded → added to index |
   194|| Existing file modified | Detected via content hash → re-indexed |
   195|| File removed | Detected → removed from index |
   196|
   197|### Backend-Specific Update Support
   198|
   199|| Backend | Incremental Adds | Removes | Notes |
   200||---------|-----------------|---------|-------|
   201|| **HNSW (non-compact)** | ✅ Yes | ❌ No | Use `--no-compact` flag |
   202|| **HNSW (compact, default)** | ❌ No | ❌ No | Must rebuild entirely |
   203|| **DiskANN** | ✅ Yes | ❌ No | |
   204|| **IVF** | ✅ Yes | ✅ Yes | Full add+remove support |
   205|
   206|**Important:** Default HNSW is `is_compact=True`, which does not support in-place updates. Use `--no-compact` for incremental builds.
   207|
   208|```bash
   209|# Build without compact mode for incremental support
   210|leann build my-index --docs ./docs --no-compact
   211|```
   212|
   213|### Build from Pre-Computed Embeddings
   214|
   215|If you already have embeddings computed elsewhere:
   216|
   217|```python
   218|builder = LeannBuilder(backend_name="hnsw")
   219|builder.add_text("Doc 1", metadata={"id": "doc1"})
   220|builder.add_text("Doc 2", metadata={"id": "doc2"})
   221|builder.build_index_from_embeddings(
   222|    index_path="/path/to/my-index",
   223|    embeddings_file="/path/to/embeddings.pkl"
   224|)
   225|```
   226|
   227|The embeddings file must be a pickle of `(ids, embeddings_array)`.
   228|
   229|---
   230|
   231|## Search and Query
   232|
   233|### Basic Semantic Search
   234|
   235|```python
   236|from leann import LeannSearcher
   237|
   238|searcher = LeannSearcher("/path/to/my-index")
   239|results = searcher.search("embeddings and vector search", top_k=5)
   240|
   241|for r in results:
   242|    print(f"[{r.score:.4f}] {r.text}")
   243|    print(f"  Metadata: {r.metadata}")
   244|    print(f"  ID: {r.id}")
   245|searcher.cleanup()
   246|```
   247|
   248|### Search Parameters
   249|
   250|| Parameter | Default | Description |
   251||-----------|---------|-------------|
   252|| `query` | (required) | Text query |
   253|| `top_k` | 5 | Number of results to return |
   254|| `complexity` | 64 | Search complexity / candidate list size. Higher = more accurate, slower |
   255|| `beam_width` | 1 | Parallel search paths per iteration |
   256|| `prune_ratio` | 0.0 | Ratio of neighbors to prune |
   257|| `metadata_filters` | None | Post-search metadata filtering |
   258|| `gemma` | 1.0 | Vector/keyword blend. 1.0 = pure vector, 0.0 = pure BM25 keyword |
   259|| `use_grep` | False | Fallback to grep-based keyword search |
   260|
   261|### Hybrid Search (Vector + Keyword)
   262|
   263|```python
   264|# Blend vector and BM25 keyword search
   265|results = searcher.search(
   266|    "machine learning",
   267|    top_k=10,
   268|    gemma=0.7  # 70% vector, 30% BM25 keyword
   269|)
   270|```
   271|
   272|### Grep / Keyword Search Fallback
   273|
   274|```python
   275|# Pure keyword search using grep
   276|results = searcher.search(
   277|    "exact phrase match",
   278|    top_k=5,
   279|    use_grep=True
   280|)
   281|```
   282|
   283|### Search Return Value
   284|
   285|Each `SearchResult` has:
   286|
   287|```python
   288|@dataclass
   289|class SearchResult:
   290|    id: str          # Passage ID
   291|    score: float     # Similarity score (higher = better)
   292|    text: str        # Raw passage text
   293|    metadata: dict   # Arbitrary metadata dict
   294|```
   295|
   296|---
   297|
   298|## Metadata Filtering
   299|
   300|### Overview
   301|
   302|Metadata filtering is implemented via `MetadataFilterEngine`. Filters are applied **post-search** — they filter the vector search candidate set, not the index itself. This means the index always returns candidates, and filters prune them.
   303|
   304|### Supported Operators
   305|
   306|| Category | Operators |
   307||----------|-----------|
   308|| Comparison | `==`, `!=`, `<`, `<=`, `>`, `>=` |
   309|| Membership | `in`, `not_in` |
   310|| String | `contains`, `starts_with`, `ends_with` |
   311|| Boolean | `is_true`, `is_false` |
   312|
   313|### Filter Format
   314|
   315|```python
   316|metadata_filters = {
   317|    "field_name": {"<operator>": value}
   318|}
   319|```
   320|
   321|### Examples
   322|
   323|```python
   324|# Single filter
   325|results = searcher.search(
   326|    "AI research",
   327|    top_k=10,
   328|    metadata_filters={"genre": {"==": "fiction"}}
   329|)
   330|
   331|# Compound AND filters
   332|results = searcher.search(
   333|    "AI research",
   334|    top_k=10,
   335|    metadata_filters={
   336|        "genre": {"==": "fiction"},
   337|        "chapter": {"<=": 10},
   338|        "word_count": {">": 500}
   339|    }
   340|)
   341|
   342|# Membership filters
   343|results = searcher.search(
   344|    "adventure story",
   345|    top_k=10,
   346|    metadata_filters={
   347|        "tags": {"in": ["fantasy", "adventure"]},
   348|        "character": {"not_in": ["Alice", "Bob"]}
   349|    }
   350|)
   351|
   352|# String matching
   353|results = searcher.search(
   354|    "published content",
   355|    metadata_filters={
   356|        "genre": {"contains": "fiction"},
   357|        "title": {"starts_with": "Chapter"},
   358|        "filename": {"ends_with": ".txt"}
   359|    }
   360|)
   361|
   362|# Boolean filters
   363|results = searcher.search(
   364|    "content",
   365|    metadata_filters={
   366|        "is_published": {"is_true": True},
   367|        "is_draft": {"is_false": False}
   368|    }
   369|)
   370|```
   371|
   372|### Setting Metadata at Index Time
   373|
   374|```python
   375|builder.add_text(
   376|    "The chapter about machine learning.",
   377|    metadata={
   378|        "chapter": 5,
   379|        "genre": "fiction",
   380|        "character": "Alice",
   381|        "word_count": 1200,
   382|        "is_published": True,
   383|        "tags": ["ai", "robots", "future"]
   384|    }
   385|)
   386|```
   387|
   388|### Limitations
   389|
   390|- Metadata filtering is **post-search** — if your filter is very restrictive, you may want to increase `top_k` to ensure enough candidates survive filtering
   391|- No OR logic (only AND between fields)
   392|- No native list-field filtering (e.g., "any tag in list") — membership is checked at the field level
   393|
   394|---
   395|
   396|## Architecture: LEANN + Postgres Pattern
   397|
   398|### Can You Use Just the Index + External Metadata Store?
   399|
   400|**Yes.** LEANN's `.passages.jsonl` is just a convenience store. The files that matter for vector search are:
   401|
   402|- `*.index` — the graph index
   403|- `*.ids.txt` — passage ID remapping
   404|- `*.meta.json` — model config
   405|
   406|The `.passages.jsonl` and `.passages.idx` are optional from the perspective of vector search — you could manage your own text/metadata store entirely.
   407|
   408|### Recommended Pattern: LEANN + Postgres
   409|
   410|```
   411|┌─────────────────────────────────────────────────────┐
   412|│                    Postgres                          │
   413|│  passage_id (PK) | text | metadata (JSONB) | ...   │
   414|└──────────────────────┬──────────────────────────────┘
   415|                       │  join on ID
   416|                       ↓
   417|┌─────────────────────────────────────────────────────┐
   418|│              LEANN Vector Index                      │
   419|│  passage_id → graph node → similarity search         │
   420|└─────────────────────────────────────────────────────┘
   421|```
   422|
   423|**Why this works:**
   424|1. Build LEANN index normally (or from pre-computed embeddings)
   425|2. Use LEANN's `SearchResult.id` to look up full text and rich metadata in Postgres
   426|3. Postgres becomes the source of truth for text and structured metadata
   427|4. LEANN handles the vector similarity
   428|
   429|**This is a clean separation** — LEANN doesn't need to know about your schema, and Postgres doesn't need to handle vector operations.
   430|
   431|### Alternative: LEANN as Pure Vector Index
   432|
   433|If you don't need LEANN's built-in text store at all:
   434|
   435|1. Build the index with dummy text or just IDs as text
   436|2. Delete or ignore `*.passages.jsonl`
   437|3. Use LEANN purely as: `passage_id → vector_similarity`
   438|4. Resolve all text/metadata from your own store
   439|
   440|```python
   441|# Index with just IDs as text
   442|builder.add_text("doc-uuid-123", metadata={"id": "doc-uuid-123"})
   443|
   444|# At query time
   445|results = searcher.search("embeddings query", top_k=5)
   446|for r in results:
   447|    doc = postgres.fetch("SELECT * FROM documents WHERE id = %s", r.id)
   448|    # r.id → your Postgres PK
   449|```
   450|
   451|---
   452|
   453|## Backends
   454|
   455|### HNSW (Hierarchical Navigable Small World)
   456|
   457|- **Default backend**
   458|- Fast build and search
   459|- **Incremental updates:** Only with `is_compact=False`
   460|- Parameters: `M` (graph degree), `efConstruction`, `distance_metric`
   461|
   462|```python
   463|builder = LeannBuilder(
   464|    backend_name="hnsw",
   465|    M=16,
   466|    efConstruction=200,
   467|)
   468|```
   469|
   470|### DiskANN
   471|
   472|- Microsoft's disk-based ANN
   473|- Memory-efficient for very large indices
   474|- Requires more dependencies (Intel MKL, boost, etc.)
   475|- Supports incremental updates
   476|
   477|```python
   478|builder = LeannBuilder(
   479|    backend_name="diskann",
   480|    num_neighbors=32,
   481|    search_list_size=50,
   482|)
   483|```
   484|
   485|### IVF (Inverted File Index)
   486|
   487|- Training-based clustering approach
   488|- **Best for add + remove operations**
   489|- Requires minimum corpus size for training (~100+ documents)
   490|
   491|```python
   492|builder = LeannBuilder(backend_name="ivf")
   493|```
   494|
   495|### See Also

- [[llm-server-throughput-optimization]] — LLM inference optimization; LEANN can index LLM outputs for RAG workflows

## Related
- [[llm-server-throughput-optimization]] — inference optimization where LEANN's indexing is relevant
- [[ontology-velocity-investment-framework]] — AI investment context for database infrastructure plays

## Distance Metrics
   496|
   497|```python
   498|# For normalized embeddings (OpenAI Ada, Voyage, Cohere)
   499|builder = LeannBuilder(
   500|    backend_name="hnsw",
   501|