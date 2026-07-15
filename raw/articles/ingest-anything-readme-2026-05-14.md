---
source_url: https://github.com/AstraBert/ingest-anything
ingested: 2026-05-14
sha256: <raw README>
---

<div align="center">
<h1>ingest-anything</h1>
<h2>From data to vector database effortlessly</h2>
</div>
<br>
<div align="center">
    <a href="https://discord.gg/AXcVf269"><img src="https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Join Discord Server" width=200 height=60></a>
</div>
<br>
<div align="center">
    <img src="https://raw.githubusercontent.com/AstraBert/ingest-anything/main/logo.png" alt="Ingest-Anything Logo">
</div>

**`ingest-anything`** is a python package aimed at providing a smooth solution to ingest non-PDF files into vector databases, given that most ingestion pipelines are focused on PDF/markdown files. Leveraging [chonkie](https://docs.chonkie.ai/getting-started/introduction), [PdfItDown](https://github.com/AstraBert/PdfItDown), and [LlamaIndex](https://www.llamaindex.ai) integrations for vector databases and data loaders, `ingest-anything` gives you a fully-automated pipeline for document ingestion within few lines of code!

Find out more about `ingest-anything` on the [Documentation website](https://pdfitdown.eu/built-with-pdfitdown/ingest-anything)! (still under construction)

## Workflow

<div align="center">
    <img src="https://raw.githubusercontent.com/AstraBert/ingest-anything/main/workflow.png" alt="Ingest-Anything Workflow">
</div>

**For text files**
- The input files are converted into PDF by PdfItDown
- The PDF text is extracted using LlamaIndex-compatible reader
- The text is chunked exploiting Chonkie's functionalities
- The chunks are embedded thanks to an Embedding model from Sentence Transformers, OpenAI, Cohere, Jina AI or Model2Vec
- The embeddings are loaded into a LlamaIndex-compatible vector database

**For code files**
- The text is extracted from code files using LlamaIndex SimpleDirectoryReader
- The text is chunked exploiting Chonkie's CodeChunker
- The chunks are embedded thanks to an Embedding model from Sentence Transformers, OpenAI, Cohere, Jina AI or Model2Vec
- The embeddings are loaded into a LlamaIndex-compatible vector database

*For web data*
- HTML content is scraped from URLs with [crawlee](https://crawlee.dev)
- HTML files are turned into PDFs with PdfItDown
- The text is extracted from PDF files using LlamaIndex PyMuPdfReader
- The text is chunked exploiting Chonkie's chunkers
- The chunks are embedded thanks to an Embedding model from Sentence Transformers, OpenAI, Cohere, Jina AI or Model2Vec
- The embeddings are loaded into a LlamaIndex-compatible vector database

**For Agent Workflow**
- Initialize a vector database (e.g., Qdrant, Weaviate).
- Initialize a language model (LLM) (e.g., OpenAI).
- Create an `IngestAgent` instance.
- Use the `create_agent` method to generate a specific agent type (e.g., `IngestAnythingFunctionAgent`, `IngestCodeReActAgent`).
- Ingest data using the agent's `ingest` method.
- Retrieve the agent using the `get_agent` method for querying and interaction.

## Usage

`ingest-anything` can be installed using `pip`:

```bash
pip install ingest-anything
# or, for a faster installation
uv pip install ingest-anything
```

Key examples showing embedding model parameter (`embedding_model="sentence-transformers/all-MiniLM-L6-v2"`) and vector store backends (Qdrant, Weaviate).
