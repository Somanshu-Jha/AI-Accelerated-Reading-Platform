from fastapi import FastAPI
from topic_engine.topic_expander import expand_topic
from blog_fetcher.multi_search import multi_source_search
from blog_fetcher.extractor import extract_blog_metadata
from blog_comparator.comparator import BlogComparator

app = FastAPI(
    title="AI Accelerated Reading Platform",
    description="AI powered research engine for discovering and comparing blogs",
    version="0.3"
)

comparator = BlogComparator()


@app.get("/search")
def search(topic: str):

    print("User topic:", topic)

    queries = expand_topic(topic)

    print("Expanded queries:", queries)

    blogs = []

    for q in queries:

        results = multi_source_search(q)

        print("Results for query:", q, results)

        blogs.extend(results)

    blogs = list(set(blogs))

    blogs = [b for b in blogs if b.startswith("http")]

    print("Total URLs:", len(blogs))

    extracted = [extract_blog_metadata(url) for url in blogs]

    result = comparator.compare(extracted)

    return result