import os
import json

DATA_DIR = "data"

def save_blogs(topic, blogs):
    os.makedirs(DATA_DIR, exist_ok=True)

    filename = topic.replace(" ", "_") + ".json"
    path = os.path.join(DATA_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(blogs, f, indent=2)