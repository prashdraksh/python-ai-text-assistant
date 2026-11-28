
from embedding_service import EmbeddingService


def main():

    service = EmbeddingService()

    texts = [
        "Python is a programming language.",
        "Machine learning enables computers to learn from data."
    ]

    embeddings = service.generate_embeddings(texts)

    print("Number of embeddings:", len(embeddings))
    print("Dimensions:", len(embeddings[0]))

    query = "How do computers learn?"

    query_embedding = service.generate_query_embedding(query)

    print("Query dimensions:", len(query_embedding))


if __name__ == "__main__":
    main()
