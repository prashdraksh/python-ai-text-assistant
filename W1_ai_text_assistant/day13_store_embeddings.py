import chromadb
from sentence_transformers import SentenceTransformer

# 1. Load embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# 2. Documents
documents = [
    "Python is a popular programming language.",
    "Machine learning enables computers to learn patterns from data.",
    "Deep learning uses neural networks."
]

# 3. Generate embeddings
embeddings = model.encode(documents)

# 4. Create persistent ChromaDB client
client = chromadb.PersistentClient(path="./day13_chroma_db")

# 5. Create collection
collection = client.get_or_create_collection(
    name="documind_custom_embeddings"
)

# 6. Store custom embeddings
collection.add(
    ids=["doc_001", "doc_002", "doc_003"],
    documents=documents,
    embeddings=embeddings.tolist(),
    metadatas=[
        {"category": "programming", "page": 1},
        {"category": "machine_learning", "page": 5},
        {"category": "deep_learning", "page": 6}
    ]
)

print("Custom embeddings stored successfully!")
print("Total records:", collection.count())

# 7. Retrieve stored records and embeddings
results = collection.get(
    include=["documents", "embeddings", "metadatas"]
)

print("\n========== STORED DATA ==========")

print("IDs:", results["ids"])
print("Documents:", results["documents"])
print("Metadata:", results["metadatas"])

print("\nEmbedding shape:")
print(len(results["embeddings"]), "documents")
print(len(results["embeddings"][0]), "dimensions")

query = "How do computers learn patterns?"

query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2,
    where={"category": "machine_learning"}
)

print("\n========== CUSTOM EMBEDDING SEARCH ==========")

print("IDs:", results["ids"])
print("Documents:", results["documents"])
print("Metadata:", results["metadatas"])
print("Distances:", results["distances"])