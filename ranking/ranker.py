import re
from urllib.parse import urlparse
from collections import Counter
from typing import List, Dict

# Domain authority scoring
DOMAIN_AUTHORITY = {
    "wikipedia.org": 1.0,
    "britannica.com": 0.95,
    "lenovo.com": 0.95,
    "nvidia.com": 0.95,
    "medium.com": 0.85,
    "dev.to": 0.9,
    "github.com": 0.9,
    "edu": 0.9,
    "gov": 0.95
}

SPAM_KEYWORDS = [
    "buy now",
    "free download",
    "click here",
    "canva",
    "facebook"
]


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip() if text else ""


def tokenize(text: str):
    return re.findall(r"\b[a-z0-9]+\b", normalize(text))


def domain_score(url: str) -> float:
    domain = urlparse(url).netloc.lower()

    for key, value in DOMAIN_AUTHORITY.items():
        if key in domain:
            return value

    return 0.55  # lower neutral baseline


def spam_penalty(title: str) -> float:
    title = normalize(title)
    for word in SPAM_KEYWORDS:
        if word in title:
            return 0.2
    return 1.0


def keyword_relevance(query: str, title: str) -> float:
    query_tokens = tokenize(query)
    title_tokens = tokenize(title)

    if not query_tokens or not title_tokens:
        return 0.0

    title_counter = Counter(title_tokens)

    score = 0.0

    for token in query_tokens:
        if token in title_counter:
            # weight exact presence higher
            score += 1.5
        else:
            # partial fuzzy matching
            for t in title_tokens:
                if token in t:
                    score += 0.5

    # normalize
    return min(score / (len(query_tokens) * 2), 1.0)


def semantic_bonus(query: str, title: str) -> float:
    # bonus if entire phrase appears
    if normalize(query) in normalize(title):
        return 0.5
    return 0.0


def rank_results(query: str, blogs: List[Dict]) -> List[Dict]:

    ranked = []
    domain_usage = {}

    for blog in blogs:
        url = blog.get("url")
        title = blog.get("title", "")

        if not url or not title:
            continue

        domain = urlparse(url).netloc

        # allow max 4 per domain
        domain_usage[domain] = domain_usage.get(domain, 0) + 1
        if domain_usage[domain] > 4:
            continue

        trust = domain_score(url)
        relevance = keyword_relevance(query, title)
        bonus = semantic_bonus(query, title)
        penalty = spam_penalty(title)

        final_score = (
            (0.45 * trust) +
            (0.35 * relevance) +
            (0.15 * bonus)
        ) * penalty

        blog["ranking_score"] = round(final_score, 3)
        ranked.append(blog)

    ranked.sort(key=lambda x: x["ranking_score"], reverse=True)

    return ranked