from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("BAAI/bge-base-en")

BEGINNER_TEXT = """
what is, introduction, basics, beginner guide,
history, overview, fundamentals
"""

INTERMEDIATE_TEXT = """
architecture, how it works,
implementation, components,
technical explanation
"""

ADVANCED_TEXT = """
optimization, protocol design,
deep technical analysis,
research level explanation,
advanced mechanisms
"""

reference_embeddings = model.encode([
    BEGINNER_TEXT,
    INTERMEDIATE_TEXT,
    ADVANCED_TEXT
])


def classify_difficulty(text):

    emb = model.encode([text])[0]

    scores = cosine_similarity([emb], reference_embeddings)[0]

    labels = ["beginner", "intermediate", "advanced"]

    return labels[scores.argmax()]