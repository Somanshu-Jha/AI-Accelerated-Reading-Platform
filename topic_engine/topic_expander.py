def expand_topic(topic: str):
    topic = topic.strip()

    return list(set([
        topic,
        f"{topic} review",
        f"{topic} specifications",
        f"{topic} benchmark",
        f"{topic} performance",
        f"{topic} comparison"
    ]))