from fastapi import FastAPI
from topic_engine.topic_expander import expand_topic
from blog_fetcher.multi_search import multi_source_search
from blog_fetcher.extractor import extract_blog_metadata
from blog_comparator.comparator import BlogComparator

app = FastAPI()

comparator = BlogComparator()


@app.get("/search")
def search(topic: str):

    try:

        print("User topic:", topic)

        queries = expand_topic(topic)

        print("Expanded queries:", queries)

        blogs = multi_source_search(topic)

        print("Blogs found:", blogs)

        extracted = [extract_blog_metadata(url) for url in blogs]

        result = comparator.compare(extracted)

        return result

    except Exception as e:

        print("ERROR:", str(e))

        return {"error": str(e)}