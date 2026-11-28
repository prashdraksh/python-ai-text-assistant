import chromadb

# Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Create or retrieve a collection
collection = client.get_or_create_collection(
    name="documind_chunks"
)

print("Collection created successfully!")
print("Collection name:", collection.name)
print("Number of records:", collection.count())

collection.add(
    ids=[
        "chunk_001",
        "chunk_002",
        "chunk_003"
    ],
    documents=[
        "Python is a popular programming language.",
        "Machine learning enables computers to learn patterns from data.",
        "Deep learning uses neural networks."
    ],
    metadatas=[
        {"document": "programming.pdf", "page": 1},
        {"document": "AI_guide.pdf", "page": 5},
        {"document": "AI_guide.pdf", "page": 6}
    ]
)

results = collection.get()

print("\n========== STORED RECORDS ==========")

print("IDs:", results["ids"])
print("Documents:", results["documents"])
print("Metadata:", results["metadatas"])

print("\nTotal retrieved:", len(results["ids"]))

print("Records added successfully!")
print("Total records:", collection.count())

results = collection.query(
    query_texts=["How do computers learn from data?"],
    n_results=2
)

print("\n========== SEMANTIC SEARCH ==========")

print("IDs:", results["ids"])
print("Documents:", results["documents"])
print("Distances:", results["distances"])
print("Metadata:", results["metadatas"])

results = collection.query(
    query_texts=["How do computers learn from data?"],
    n_results=2,
    where={"document": "programming.pdf"}
)

print("\n========== FILTERED SEARCH ==========")
print("IDs:", results["ids"])
print("Documents:", results["documents"])
print("Metadata:", results["metadatas"])

collection.upsert(
    ids=["chunk_001"],
    documents=["Python is widely used in AI development."],
    metadatas=[
        {"document": "programming.pdf", "page": 2}
    ]
)
res= collection.get(ids=["chunk_001"])
print(res['documents'])
print("Number of records:", collection.count())
print("page :",res['metadatas'][0]['page'])  # Output: 2