# PROJECT_CONTEXT.md

## Project Name
AI Reading Platform

## Project Type
AI-powered blog research and learning engine.

## Project Vision
Build a startup-grade AI system that discovers blogs, extracts knowledge, ranks them semantically, and generates insights using local AI models.

The platform should function like:

Perplexity AI + Blog Research Engine + AI Learning Platform.

No paid APIs should be required.

---

## Core Objectives

The system should be able to:

• Discover blogs from multiple sources  
• Extract article metadata and content  
• Understand topic semantics  
• Rank blogs using embeddings  
• Classify article difficulty  
• Compare multiple blogs  
• Generate insights from articles  
• Provide structured learning paths  

---

## Technology Stack

Backend:
FastAPI

AI / ML:
Sentence Transformers  
FAISS (planned)  
Local LLM models (Mistral / Llama / Phi)

Data Processing:
newspaper3k  
BeautifulSoup  
requests

Machine Learning:
scikit-learn

Language:
Python

---

## Architecture Style

Modular AI pipeline architecture.

Each capability is implemented as an independent module.

Modules should be loosely coupled and easily replaceable.

---

## Critical Development Rules

1. Always maintain modular architecture.
2. Never break existing working modules.
3. Prefer incremental upgrades.
4. Always provide full replaceable code when updating files.
5. Prefer local AI models over external APIs.
6. Always ensure the core pipeline remains stable before adding new features.

---

## Current Development Stage

Advanced Prototype Stage

Core AI pipeline is operational but several advanced AI features are still pending.

---

## Future Direction

The project will evolve into an AI Research Engine that can:

• Discover information
• Understand knowledge
• Generate insights
• Build learning paths
• Answer research questions


