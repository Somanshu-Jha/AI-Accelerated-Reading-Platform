import requests

def search_devto(query, limit=20):

    url = f"https://dev.to/api/articles?tag={query}"

    response = requests.get(url)

    data = response.json()

    urls = []

    for article in data[:limit]:
        urls.append(article["url"])

    return urls