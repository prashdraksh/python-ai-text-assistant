import chromadb


class VectorStore:

    def __init__(self, db_path="./semantic_search_db"):
        self.client = chromadb.PersistentClient(path=db_path)

        self.collection = self.client.get_or_create_collection(
            name="semantic_search"
        )

    def add_documents(self, documents, embeddings):

        if len(documents) != len(embeddings):
            raise ValueError("Documents and embeddings count must match.")

        self.collection.upsert(
            ids=[doc["id"] for doc in documents],
            documents=[doc["text"] for doc in documents],
            embeddings=embeddings,
            metadatas=[doc["metadata"] for doc in documents]
        )

        print("Documents stored successfully!")
        print("Total records:", self.collection.count())

    def search(self, query_embedding, top_k=3, category=None):

        if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
            raise ValueError("top_k must be a positive integer.")

        where = {"category": category} if category else None

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where
        )

        return results