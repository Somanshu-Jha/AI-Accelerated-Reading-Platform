from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from topic_engine.topic_expander import expand_topic
from blog_fetcher.multi_search import multi_source_search
from blog_fetcher.extractor import extract_blog_metadata
from blog_comparator.comparator import BlogComparator
from ranking.ranker import Ranker
from embedding_engine.embedder import Embedder
from ml_models.difficulty_classifier import classify_difficulty

app = FastAPI(
    title="AI Accelerated Reading Platform",
    description="AI powered research engine for discovering and comparing blogs",
    version="0.4"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ranker = Ranker()
embedder = Embedder()
comparator = BlogComparator()


@app.get("/search")
def search(topic: str):

    try:

        print("User topic:", topic)

        queries = expand_topic(topic)

        print("Expanded queries:", queries)

        urls = []

        for q in queries:

            results = multi_source_search(q)

            print("Results for query:", q, len(results))

            urls.extend(results)

        urls = list(set(urls))

        urls = [u for u in urls if u.startswith("http")]

        print("Total URLs:", len(urls))

        if len(urls) == 0:

            return {
                "topic": topic,
                "total_blogs": 0,
                "blogs": []
            }

        extracted = []

        for url in urls:

            blog = extract_blog_metadata(url)

            if blog is None:
                continue

            if blog.get("title") is None:
                continue

            extracted.append(blog)

        print("Extracted blogs:", len(extracted))

        if len(extracted) == 0:

            return {
                "topic": topic,
                "total_blogs": 0,
                "blogs": []
            }

        # classify difficulty
        for blog in extracted:

            text = blog.get("content", "") or blog.get("summary", "")

            blog["difficulty"] = classify_difficulty(text)

        # create query embedding
        query_embedding = embedder.embed(topic)

        blog_embeddings = []
        valid_blogs = []

        for blog in extracted:

            text = blog.get("content", "") or blog.get("summary", "")

            if len(text.strip()) < 100:
                continue

            emb = embedder.embed(text[:2000])

            blog_embeddings.append(emb)

            valid_blogs.append(blog)

        if len(blog_embeddings) == 0:

            return {
                "topic": topic,
                "total_blogs": 0,
                "blogs": extracted
            }

        ranked = ranker.rank(
            query_embedding,
            blog_embeddings,
            valid_blogs
        )

        top_results = ranked[:10]

        result = comparator.compare(top_results)

        return {
            "topic": topic,
            "total_blogs": len(top_results),
            "blogs": result
        }

    except Exception as e:

        print("ERROR:", str(e))

        return {"error": str(e)}