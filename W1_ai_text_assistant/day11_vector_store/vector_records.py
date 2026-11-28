def create_vector_record(chunk_id, text, embedding, document_name, page_number):

    if not isinstance(chunk_id, str) or not chunk_id.strip():
        raise ValueError("chunk_id must be a non-empty string")

    if not isinstance(text, str) or not text.strip():
        raise ValueError("text must be a non-empty string")

    if (
        not isinstance(embedding, list)
        or not embedding
        or not all(
            isinstance(i, (int, float)) and not isinstance(i, bool)
            for i in embedding
        )
    ):
        raise ValueError("embedding must be a non-empty list of numbers")

    if not isinstance(document_name, str) or not document_name.strip():
        raise ValueError("document_name must be a non-empty string")

    if isinstance(page_number, bool) or not isinstance(page_number, int) or page_number <= 0:
        raise ValueError("page_number must be a positive integer")

    return {
        "id": chunk_id,
        "text": text,
        "embedding": embedding,
        "metadata": {
            "document": document_name,
            "page": page_number
        }
    }



record1 = create_vector_record(
    "chunk_001",
    "Python is a programming language.",
    [0.1, 0.2, 0.3],
    "programming.pdf",
    1
)

record2 = create_vector_record(
    "chunk_002",
    "Machine learning learns patterns from data.",
    [0.4, 0.5, 0.6],
    "AI_guide.pdf",
    5
)

record3 = create_vector_record(
    "chunk_003",
    "Deep learning uses neural networks.",
    [0.7, 0.8, 0.9],
    "AI_guide.pdf",
    6
)
vector_records = [record1, record2, record3]
print(len(vector_records))
for record in vector_records:
    print("id:", record['id'])
    print("document:", record['metadata']['document'], "page:", record['metadata']['page'])
