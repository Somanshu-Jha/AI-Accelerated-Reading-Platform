import requests

def search_hn(query, limit=20):

    url = f"https://hn.algolia.com/api/v1/search?query={query}"

    response = requests.get(url)

    data = response.json()

    urls = []

    for item in data["hits"][:limit]:

        if item.get("url"):
            urls.append(item["url"])

    return urls