from embedding_engine.embedder import Embedder
from embedding_engine.vector_store import VectorStore

class Retriever:

    def __init__(self):
        self.embedder = Embedder()
        self.vector_store = VectorStore()

    def add_documents(self, documents):
        embeddings = self.embedder.embed_batch(
            [doc["content"] for doc in documents]
        )
        self.vector_store.add(embeddings, documents)

    def retrieve(self, query, top_k=5):
        query_embedding = self.embedder.embed(query)
        return self.vector_store.search(query_embedding, top_k)