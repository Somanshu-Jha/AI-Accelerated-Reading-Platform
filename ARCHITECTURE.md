# ARCHITECTURE.md

## System Overview

The AI Reading Platform follows a modular AI research pipeline.

Each stage transforms the data and passes it to the next stage.

---

## Current Pipeline

User Query
↓
Topic Expansion
↓
Multi-source Blog Search
↓
Blog Extraction
↓
Embedding Generation
↓
Difficulty Classification
↓
Semantic Ranking
↓
Blog Comparison
↓
API Response

---

## Module Responsibilities

### topic_engine

Responsible for understanding and expanding user queries.

Example:

Input:
python

Expanded queries:

- what is python
- python tutorial
- python advanced concepts
- python architecture

---

### blog_fetcher

Responsible for discovering blogs from multiple sources.

Sources may include:

- Medium
- Dev.to
- RSS feeds
- Web search

Outputs a list of URLs.

---

### extractor

Extracts metadata and content from blog URLs.

Extracted fields:

- title
- author
- summary
- content
- url

Library used:
newspaper3k

---

### embedding_engine

Converts text into vector embeddings using semantic models.

Current model:

BAAI/bge-base-en

Purpose:

Convert text → vector representation.

---

### ranking

Ranks blogs using semantic similarity.

Process:

Query embedding  
vs  
Blog embedding

Similarity determines ranking.

---

### ml_models

Contains machine learning models used in the project.

Current model:

difficulty_classifier.py

Purpose:

Classify blog difficulty:

Beginner  
Intermediate  
Advanced

---

### blog_comparator

Compares multiple blogs discussing the same topic.

Helps identify differences in perspectives.

---

### main.py

FastAPI backend entry point.

Provides API endpoints such as:

/search?topic=...

Returns ranked blog results.

---

## Planned Modules

### storage

Persistent storage for blogs and embeddings.

Possible implementations:

SQLite  
PostgreSQL  
Redis cache

---

### rag_engine

Retrieval-Augmented Generation system.

Steps:

Retrieve relevant blog chunks  
Generate insights using local LLM

---

### vector database

Use FAISS for efficient semantic search.

---

### knowledge graph

Connect related topics and concepts.

Example:

Python
├ OOP
├ Data Science
├ Web Development

---

### AI Research Agent

Future system that can autonomously research topics.

Agents:

Planner Agent  
Research Agent  
Ranking Agent  
Insight Agent
