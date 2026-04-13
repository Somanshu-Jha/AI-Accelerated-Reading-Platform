<div align="center">
  <h1>🚀 AI Accelerated Reading Platform</h1>
  <p><h3>An advanced, AI-powered blog research and learning engine</h3></p>
  <p><strong>Discover • Extract • Rank • Learn</strong></p>
</div>

<br />

The **AI Accelerated Reading Platform** acts as a powerful combination of an advanced AI Search Engine (like Perplexity), a Blog Research Engine, and an AI Learning Platform. It discovers articles, extracts deep knowledge, ranks them semantically, and generates insights using completely local AI models—without relying on any paid APIs.

---

## 📑 Table of Contents
- [✨ Key Features](#-key-features)
- [🏗 Architecture & System Flow](#-architecture--system-flow)
- [💻 Tech Stack](#-tech-stack)
- [🚀 Getting Started](#-getting-started)
- [📂 Project Structure](#-project-structure)
- [🗺️ Development Roadmap](#️-development-roadmap)
- [🚧 Current Limitations & Known Issues](#-current-limitations--known-issues)

---

## ✨ Key Features

### 🟢 Currently Operational
- **Multi-source Blog Discovery**: Automatically discovers relevant articles across platforms (Medium, Dev.to, RSS feeds, Web search).
- **Deep Topic Expansion**: Intelligently expands basic queries (e.g., `python` → `python tutorial`, `python architecture`).
- **Semantic Ranking**: Utilizes Sentence Transformers (`BAAI/bge-base-en`) to rank blogs based on high-level semantic meaning, going far beyond basic keyword matching.
- **Difficulty Classification**: Employs ML models to classify article complexity into Beginner, Intermediate, or Advanced levels.
- **Blog Comparison Engine**: Analyzes and compares multiple blogs discussing the same topic to surface different perspectives and identify content gaps.
- **Privacy-First Local AI**: Built to run entirely on local execution pipelines for insights, ensuring complete data privacy and $0 API costs.

### 🔮 Planned Upgrades
- **RAG Insight Generation**: Automatically synthesize and generate insights from retrieved blog chunks using local LLMs (Mistral, Llama).
- **Reading Time Prediction**: Establish realistic estimations for consuming individual articles.
- **Bias Detection & Topic Clustering**: Identify opinion biases and group similar narratives and technical approaches.
- **Knowledge Graph Generation**: Map conceptual relations to track learning paths (e.g., `Python` → `OOP` → `Data Science`).

---

## 🏗 Architecture & System Flow

The platform relies on a sophisticated, modular AI pipeline. Here is an example of what happens under the hood when a user searches for a topic:

**Example Request:** `GET /search?topic=python`

1. **Query Expansion** (`topic_engine`): System expands "python" into detailed, highly targeted sub-topics.
2. **Multi-Source Search** (`blog_fetcher`): Crawls sources for highly-rated Python blogs based on the sub-topics.
3. **Blog Extraction** (`extractor`): Uses `newspaper3k` to elegantly scrape raw content, titles, authors, and metadata.
4. **Vector Embedding** (`embedding_engine`): Converts the text into vector space representations.
5. **Contextual Classification** (`ml_models`): Assigns a beginner/intermediate/advanced label based on word difficulty and context.
6. **Semantic Ranking** (`ranking`): Matches query embeddings vs. blog embeddings.
7. **Blog Comparison** (`blog_comparator`): Identifies conceptual differences and overlaps.
8. **Final JSON Response** (`main.py`): Delivers structured, actionable intelligence out via the API.

---

## 💻 Tech Stack

- **Framework**: `FastAPI` (Python 3.8+)
- **AI / Machine Learning**: Sentence Transformers (`BAAI/bge-base-en`), `scikit-learn`, Local LLMs integration.
- **Data Extractor**: `newspaper3k`, `BeautifulSoup`, `requests`
- **Future Integrations**: `FAISS` (Vector DB), `SQLite/PostgreSQL` (Storage)

---

## 🚀 Getting Started

### 1. Requirements
Ensure you have Python 3.8 or higher installed on your machine.

### 2. Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/Somanshu-Jha/AI-Accelerated-Reading-Platform.git
cd AI-Accelerated-Reading-Platform
pip install -r requirement.txt
```

### 3. Running the Engine
Start up the FastAPI backend locally:
```bash
uvicorn main:app --reload
```
Navigate to the interactive Swagger UI to test the endpoints at:  
👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## 📂 Project Structure

```text
├── blog_comparator/   # Analyzes perspective shifts between blogs
├── blog_fetcher/      # Advanced crawling from multiple developer sources
├── embedding_engine/  # Text-to-Vector transformations
├── frontend/          # Next.js/React frontend (planned)
├── ml_models/         # Difficulty Classifiers & ML Core
├── rag_engine/        # (Planned) Insight generation via Local LLMs
├── ranking/           # Semantic similarity & sorting logic
├── storage/           # (Planned) Vector & relational database drivers
├── topic_engine/      # Query comprehension & expansion
└── main.py            # FastAPI Application Entrypoint
```

---

## 🗺️ Development Roadmap

- **v0.3**: Enable multi-query retrieval, URL deduplication, and deeper content chunking.
- **v0.4**: Output RAG insight generation using local inference & introduce Reading Time logic.
- **v0.5**: Build bias detection modules & topic clustering algorithms.
- **v0.6**: Implement active Knowledge Graphs and introduce AI Autonomous Research Agents.

---

## 🚧 Current Limitations & Known Issues

- **Search Coverage**: Search coverage is currently limited for niche topics (e.g., broad queries like "science facts" may yield isolated results) due to constrained primary search sources.
- **RSS Parsing Redirects**: Certain RSS sources occasionally return redirect URLs (e.g., `bing.com/news/apiclick.aspx`), which require intermediate translation before accurate metadata extraction can happen.

---
<div align="center">
  <i>Built to transform how we discover and digest complex knowledge. 🧠</i>
</div>
