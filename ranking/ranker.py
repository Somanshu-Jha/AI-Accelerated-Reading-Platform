from sklearn.metrics.pairwise import cosine_similarity



class Ranker:

    def rank(self, query_embedding, blog_embeddings, blogs):
        if len(blog_embeddings)==0:
            return []

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