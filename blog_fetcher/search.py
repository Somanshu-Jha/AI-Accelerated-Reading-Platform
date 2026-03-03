import requests
from bs4 import BeautifulSoup
from config.settings import settings

def search_links(query: str):

    url = "https://www.bing.com/search"
    params = {
        "q": query,
        "format": "rss"
    }

    try:
        response = requests.get(url, params=params, timeout=settings.REQUEST_TIMEOUT)
        soup = BeautifulSoup(response.content, "xml")

        results = []

        for item in soup.find_all("item"):
            link = item.link.text
            title = item.title.text

            results.append({
                "title": title,
                "url": link
            })

            if len(results) >= settings.MAX_SEARCH_RESULTS:
                break

        return results

    except Exception:
        return []