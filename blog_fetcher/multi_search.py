from blog_fetcher.search_sources.medium import search_medium
from blog_fetcher.search_sources.devto import search_devto
from blog_fetcher.search_sources.google_rss import search_google_rss
from blog_fetcher.search_sources.google_web import search_google_web

TRUSTED_DOMAINS = [
    "medium.com",
    "dev.to",
    "towardsdatascience.com",
    "hashnode.com"
    "buzzfeed.com"
    "Mashable.com"
    "HackerNoon.com"
    "Boing Boing.com"
    "The Verge.com"
    "KDnuggets.com"
    "CoinDesk.com"
    "9to5Mac.com"
    "Engadget.com"
    "Wired.com"
    "Ars Technica.com"
    "Nir and Far.com"
    "Big Think.com"

]


def prioritize_sources(urls):

    trusted = []
    others = []

    for url in urls:

        if any(domain in url for domain in TRUSTED_DOMAINS):
            trusted.append(url)

        else:
            others.append(url)

    return trusted + others


def multi_source_search(query):

    urls = []

    # trusted sources first
    try:
        urls += search_medium(query)
    except:
        pass

    try:
        urls += search_devto(query)
    except:
        pass

    # fallback
    try:
        urls += search_google_rss(query)
    except:
        pass

    # if still few results → search full web
    if len(urls) < 10:

        try:
            urls += search_google_web(query)
        except:
            pass

    urls = list(set(urls))

    urls = prioritize_sources(urls)

    return urls