from embedding_service import EmbeddingService

service = EmbeddingService()

documents = [
    "Python is a programming language.",
    "Machine learning learns patterns."
]

embeddings = service.generate_embeddings(documents)

print("Number of embeddings:", len(embeddings))
print("Dimensions:", len(embeddings[0]))

query_embedding = service.generate_query_embedding(
    "How do computers learn?"
)

print("Query dimensions:", len(query_embedding))