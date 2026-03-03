from sentence_transformers import SentenceTransformer
from config.settings import settings

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)

    def embed(self, text: str):
        return self.model.encode(text, normalize_embeddings=True)

    def embed_batch(self, texts: list):
        return self.model.encode(texts, normalize_embeddings=True)