from newspaper import Article


def extract_blog_metadata(url):

    try:

        article = Article(url)

        article.download()
        article.parse()

        text = article.text

        if len(text) < 200:
            return None

        summary = text[:400]

        return {
            "title": article.title,
            "author": article.authors,
            "summary": summary,
            "content": text,
            "url": url
        }

    except Exception:

        return None