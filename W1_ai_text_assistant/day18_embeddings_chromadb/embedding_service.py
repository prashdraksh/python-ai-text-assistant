
from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, texts):

        if not isinstance(texts, list) or not texts:
            raise ValueError("Texts must be a non-empty list.")

        if not all(isinstance(text, str) and text.strip() for text in texts):
            raise ValueError("All texts must be non-empty strings.")

        embeddings = self.model.encode(texts)

        return embeddings.tolist()

    def generate_query_embedding(self, query):

        if not isinstance(query, str) or not query.strip():
            raise ValueError("Query must be a non-empty string.")

        embedding = self.model.encode(query)

        return embedding.tolist()
