def sort_learning_path(blogs):

    order = {
        "beginner": 0,
        "intermediate": 1,
        "advanced": 2
    }

    return sorted(
        blogs,
        key=lambda x: order.get(x.get("difficulty"), 1)
    )