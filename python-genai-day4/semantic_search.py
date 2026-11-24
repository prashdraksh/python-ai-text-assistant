
from sentence_transformers import SentenceTransformer

# Load pretrained embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Machine learning enables computers to learn patterns from data.",
    "Python is a popular programming language.",
    "Deep learning uses neural networks.",
    "Artificial intelligence helps machines perform intelligent tasks."
]

query = "How do computers improve through experience?"

# Convert documents into embeddings
document_embeddings = model.encode(documents)
print("Number of documents:", len(document_embeddings))
print("Vector dimensions:", len(document_embeddings[0]))
print("First 10 values:", document_embeddings[0][:10])
# Convert query into an embedding
query_embedding = model.encode(query)

# Calculate similarity
similarities = model.similarity(
    query_embedding,
    document_embeddings
)[0]

# Rank documents
results = sorted(
    zip(documents, similarities.tolist()),
    key=lambda item: item[1],
    reverse=True
)

for document, score in results:
    print(f"Score: {score:.4f} | {document}")
