
from documents import documents
from embedding_service import EmbeddingService
from vector_store import VectorStore


def main():
    # Step 1: Initialize services
    embedding_service = EmbeddingService()
    vector_store = VectorStore()

    # Step 2: Extract document text
    texts = [doc["text"] for doc in documents]

    # Step 3: Generate document embeddings
    embeddings = embedding_service.generate_embeddings(texts)

    # Step 4: Store documents and embeddings
    vector_store.add_documents(documents, embeddings)

    # Step 5: Get user query
    query = "How do computers learn from data?"

    print("\nSearch query:", query)

    # Step 6: Generate query embedding
    query_embedding = embedding_service.generate_query_embedding(query)

    # Step 7: Search ChromaDB
    results = vector_store.search(
        query_embedding=query_embedding,
        top_k=3,
        category="machine_learning"
    )

    # Step 8: Display results
    print("\n========== SEMANTIC SEARCH RESULTS ==========")

    for doc_id, document, metadata, distance in zip(
        results["ids"][0],
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        print("\nDocument ID:", doc_id)
        print("Text:", document)
        print("Category:", metadata["category"])
        print("Page:", metadata["page"])
        print(f"Distance: {distance:.4f}")


if __name__ == "__main__":
    main()
