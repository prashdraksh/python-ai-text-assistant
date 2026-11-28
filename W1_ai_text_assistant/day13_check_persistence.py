import chromadb

# Reopen existing database
client = chromadb.PersistentClient(
    path="./day13_chroma_db"
)

# Retrieve existing collection
collection = client.get_collection(
    name="documind_custom_embeddings"
)

print("Database reopened successfully!")
print("Collection:", collection.name)
print("Total records:", collection.count())

# Retrieve stored documents
results = collection.get()

print("Stored IDs:", results["ids"])
print("Stored documents:", results["documents"])