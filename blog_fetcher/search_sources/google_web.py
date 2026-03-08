import requests
from bs4 import BeautifulSoup


def search_google_web(query, limit=10):

    url = f"https://www.google.com/search?q={query}+blog"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    links = []

    for g in soup.select("a"):

        href = g.get("href")

        if href and "http" in href and "google" not in href:
            links.append(href)

        if len(links) >= limit:
            break

    return links