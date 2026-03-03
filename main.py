from fastapi import FastAPI
from blog_fetcher.search import search_links
from blog_fetcher.extractor import extract_blog_metadata
from blog_comparator.comparator import BlogComparator
from rag_engine.retriever import Retriever
from rag_engine.generator import Generator
from config.settings import settings

app = FastAPI()

comparator = BlogComparator()
retriever = Retriever()
generator = Generator()

@app.get("/search")
def search_topic(topic: str):

    links = search_links(topic)
    blogs = []

    for link in links:
        meta = extract_blog_metadata(link["url"])
        if meta:
            blogs.append(meta)

    best_blog = comparator.select_best_blog(topic, blogs)

    if not best_blog:
        return {"message": "No relevant blog found."}

    retriever.add_documents([
        {"content": best_blog["snippet"]}
    ])

    return {
        "selected_blog": best_blog
    }

@app.get("/ask")
def ask_question(question: str):

    retrieved_docs = retriever.retrieve(question)

    context = "\n".join(
        doc["metadata"]["content"]
        for doc in retrieved_docs
    )

    prompt = f"""
    Answer only from the provided context.
    Context:
    {context}

    Question:
    {question}
    """

    answer = generator.generate(prompt)

    return {
        "answer": answer,
        "confidence": len(retrieved_docs)
    }