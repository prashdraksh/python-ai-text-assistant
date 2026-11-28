
import chromadb


class VectorStore:

    def __init__(self, db_path="./documind_day18_db"):

        self.client = chromadb.PersistentClient(path=db_path)

        self.collection = self.client.get_or_create_collection(
            name="documind_pdf_chunks"
        )

    def add_chunks(self, chunks, embeddings):

        if len(chunks) != len(embeddings):
            raise ValueError("Chunks and embeddings count must match.")

        self.collection.upsert(
            ids=[chunk["chunk_id"] for chunk in chunks],

            documents=[chunk["text"] for chunk in chunks],

            embeddings=embeddings,

            metadatas=[
                {
                    "document": chunk["document"],
                    "page": chunk["page"]
                }
                for chunk in chunks
            ]
        )

        print("Chunks stored successfully!")
        print("Total records:", self.collection.count())

    
    def search(
        self,
        query_embedding,
        top_k=3,
        page=None,
        document=None
    ):

        if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
            raise ValueError("top_k must be a positive integer.")

        filters = []

        if page is not None:
            filters.append({"page": page})

        if document is not None:
            filters.append({"document": document})

        where = None

        if len(filters) == 1:
            where = filters[0]

        elif len(filters) > 1:
            where = {"$and": filters}

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=min(top_k, self.collection.count()),
            where=where
        )


