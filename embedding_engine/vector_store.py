import faiss
import numpy as np
from config.settings import settings

class VectorStore:

    def __init__(self):
        self.index = faiss.IndexFlatIP(settings.VECTOR_DIM)
        self.metadata = []

    def add(self, embeddings, metadata):
        self.index.add(np.array(embeddings))
        self.metadata.extend(metadata)

    def search(self, query_embedding, top_k=5):
        scores, indices = self.index.search(
            np.array([query_embedding]), top_k
        )

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx < len(self.metadata):
                results.append({
                    "score": float(score),
                    "metadata": self.metadata[idx]
                })
        return results