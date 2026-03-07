from blog_fetcher.search_sources.google_rss import search_google_rss
from blog_fetcher.search_sources.devto import search_devto
from blog_fetcher.search_sources.hn import search_hn
from blog_fetcher.search_sources.medium import search_medium


def multi_source_search(query):

    urls = []

    try:
        urls += search_google_rss(query)
    except:
        pass

    try:
        urls += search_devto(query)
    except:
        pass

    try:
        urls += search_hn(query)
    except:
        pass

    try:
        urls += search_medium(query)
    except:
        pass

    urls = list(set(urls))

    return urls