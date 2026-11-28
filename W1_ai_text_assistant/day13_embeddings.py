from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Documents to convert into embeddings
documents = [
    "Python is a popular programming language.",
    "Machine learning enables computers to learn patterns from data.",
    "Deep learning uses neural networks."
]

# Generate embeddings
embeddings = model.encode(documents)

# Display results
print("Number of documents:", len(documents))
print("Embedding shape:", embeddings.shape)
print("Embedding dimensions:", model.get_embedding_dimension())
print("Embedding type:", embeddings)
for document, embedding in zip(documents, embeddings):
    print("\nDocument:", document)
    print("Vector dimensions:", len(embedding))
    print("First 5 values:", embedding[:5])