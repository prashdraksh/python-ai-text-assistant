from chunking import chunk_text


def chunk_documents(documents, chunk_size=100, overlap=20):
    if not documents:
        raise ValueError("Documents cannot be empty.")
    all_chunks = []

    for document in documents:

        chunks = chunk_text(
            document["text"],
            chunk_size=chunk_size,
            overlap=overlap
        )

        for index, chunk in enumerate(chunks, start=1):

            all_chunks.append({
                "document": document["document"],
                "page": document["page"],
                "chunk_id": (
                    f"{document['document']}_"
                    f"{document['page']}_chunk_{index}"
                ),
                "text": chunk
            })

    return all_chunks