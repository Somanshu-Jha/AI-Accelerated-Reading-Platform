class RAGPipeline:

    def run(self, query):

        topics = expand_topic(query)

        blogs = fetch_blogs(topics)

        chunks = chunk_text(blogs)

        embeddings = embed(chunks)

        store.add(embeddings)

        context = store.search(query)

        response = generate(context)

        return response