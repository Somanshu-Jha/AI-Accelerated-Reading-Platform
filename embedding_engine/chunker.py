def chunk_text(text, size=500, overlap=50):

    words = text.split()

    chunks = []

    for i in range(0, len(words), size - overlap):

        chunk = words[i:i+size]

        chunks.append(" ".join(chunk))

    return chunks