
from document_ingestion import ingest_pdf
from document_chunker import chunk_documents
from embedding_service import EmbeddingService
from vector_store import VectorStore


def main():

    # 1. Extract PDF pages
    pdf_path = "sample_pdfs/documind_sample_3_pages.pdf"

    documents = ingest_pdf(pdf_path)

    print("Total pages ingested:", len(documents))

    # 2. Split pages into chunks
    chunks = chunk_documents(
        documents,
        chunk_size=50,
        overlap=10
    )

    print("Total chunks generated:", len(chunks))

    # 3. Generate embeddings
    embedding_service = EmbeddingService()

    texts = [chunk["text"] for chunk in chunks]

    embeddings = embedding_service.generate_embeddings(texts)

    print("Total embeddings generated:", len(embeddings))
    print("Embedding dimensions:", len(embeddings[0]))

    # 4. Store chunks and embeddings
    vector_store = VectorStore()

    vector_store.add_chunks(chunks, embeddings)

    # 5. Search using a natural-language question
    query = "What is text chunking and why is overlap useful?"

    query_embedding = embedding_service.generate_query_embedding(query)

    results = vector_store.search(
        query_embedding=query_embedding,
        top_k=3,
        page=3
    )

    print("Search results:", results["ids"][0])

    print("\n========== SEARCH RESULTS ==========")
    print("Query:", query)

    for chunk_id, text, metadata, distance in zip(
        results["ids"][0],
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        print("\nChunk ID:", chunk_id)
        print("Document:", metadata["document"])
        print("Page:", metadata["page"])
        print("Text:", text)
        print(f"Distance: {distance:.4f}")



if __name__ == "__main__":
    main()
