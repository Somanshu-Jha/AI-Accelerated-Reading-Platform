from sentence_transformers import SentenceTransformer
from config.settings import settings
import torch


class Embedder:

    def __init__(self):

        device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL,
            device=device
        )

    def embed(self, text: str):

        return self.model.encode(
            text,
            normalize_embeddings=True
        )

    def embed_batch(self, texts: list):

        return self.model.encode(
            texts,
            normalize_embeddings=True
        )