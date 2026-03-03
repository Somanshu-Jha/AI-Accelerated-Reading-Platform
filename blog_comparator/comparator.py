import numpy as np
from embedding_engine.embedder import Embedder

class BlogComparator:

    def __init__(self):
        self.embedder = Embedder()

    def select_best_blog(self, topic, blogs):
        topic_embedding = self.embedder.embed(topic)

        scored = []
        for blog in blogs:
            blog_embedding = self.embedder.embed(
                blog["title"] + " " + blog.get("snippet", "")
            )

            similarity = float(np.dot(topic_embedding, blog_embedding))

            scored.append({
                "blog": blog,
                "score": similarity
            })

        scored.sort(key=lambda x: x["score"], reverse=True)

        return scored[0]["blog"] if scored else None