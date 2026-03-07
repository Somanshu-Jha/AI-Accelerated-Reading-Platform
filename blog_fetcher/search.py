import requests
import xml.etree.ElementTree as ET


def search_blogs(queries, max_results=5):

    urls = []

    for query in queries:

        url = f"https://www.bing.com/news/search?q={query}&format=rss"

        response = requests.get(url)

        root = ET.fromstring(response.content)

        for item in root.iter("item"):

            link = item.find("link").text

            if link:
                urls.append(link)

            if len(urls) >= max_results:
                break

        if len(urls) >= max_results:
            break

    return urls