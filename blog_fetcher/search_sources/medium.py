import feedparser

def search_medium(query, limit=5):

    url = f"https://medium.com/feed/tag/{query}"

    feed = feedparser.parse(url)

    urls = []

    for entry in feed.entries[:limit]:
        urls.append(entry.link)

    return urls