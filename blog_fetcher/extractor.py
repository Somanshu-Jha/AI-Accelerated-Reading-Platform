import requests
from bs4 import BeautifulSoup
from newspaper import Article
from config.settings import settings

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def extract_blog_metadata(url: str):

    try:
        article = Article(url)
        article.download()
        article.parse()

        if article.text and len(article.text) > 300:
            return {
                "title": article.title,
                "url": url,
                "snippet": article.text[:700]
            }

    except:
        pass

    # Fallback parser
    try:
        response = requests.get(url, headers=HEADERS, timeout=settings.REQUEST_TIMEOUT)
        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")
        text = " ".join(p.get_text() for p in paragraphs)

        if len(text) > 300:
            return {
                "title": soup.title.string if soup.title else "Untitled",
                "url": url,
                "snippet": text[:700]
            }

    except:
        pass

    return None