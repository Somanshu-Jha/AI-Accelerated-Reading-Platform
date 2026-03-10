from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("BAAI/bge-base-en")

BEGINNER_CONCEPT = """
Introduction to the topic, basic explanation,
what is, overview, beginner guide, fundamentals
"""

INTERMEDIATE_CONCEPT = """
Detailed explanation, architecture,
how it works, implementation details,
technical explanation
"""

ADVANCED_CONCEPT = """
deep technical analysis, optimization,
research level concepts,
protocol design, cryptographic mechanisms
"""


concept_embeddings = model.encode([
    BEGINNER_CONCEPT,
    INTERMEDIATE_CONCEPT,
    ADVANCED_CONCEPT
])


def classify_difficulty(text):

    article_embedding = model.encode([text])[0]

    scores = cosine_similarity(
        [article_embedding],
        concept_embeddings
    )[0]

    labels = ["beginner", "intermediate", "advanced"]

    return labels[scores.argmax()]