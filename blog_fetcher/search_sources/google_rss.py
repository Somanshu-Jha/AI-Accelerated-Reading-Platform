import feedparser

def search_google_rss(query, limit=5):

    url = f"https://news.google.com/rss/search?q={query}"

    feed = feedparser.parse(url)

    urls = []

    for entry in feed.entries[:limit]:
        urls.append(entry.link)

    return urls