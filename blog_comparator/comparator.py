class BlogComparator:

    def __init__(self):
        pass


    def compare(self, blogs):
        '''compare multiple blog content and return insights from that

'''
        results = []

        for blog in blogs:

            if blog is None:
                continue

            results.append({
                "title": blog.get("title"),
                "author": blog.get("authors"),
                "summary": blog.get("summary"),
                "url": blog.get("url")
            })

        return {
            "total_blogs": len(results),
            "blogs": results
        }