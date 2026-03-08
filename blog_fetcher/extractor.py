from newspaper import Article


def extract_blog_metadata(url):

    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        return {
            "title": article.title,
            "author": article.authors,
            "summary": article.summary,
            "url": url
        }

    except Exception as e:

        return {
            "title": None,
            "author": None,
            "summary": None,
            "url": url
        }