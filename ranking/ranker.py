from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class Ranker:

    def rank(self, query_embedding, blog_embeddings, blogs):

        scores = cosine_similarity(
            [query_embedding],
            blog_embeddings
        )[0]

        ranked = []

        for blog, score in zip(blogs, scores):

            blog["score"] = float(score)

            ranked.append(blog)

        ranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranked