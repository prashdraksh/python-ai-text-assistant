
import os
import json
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from chunking import chunk_text
from prompt_builder import build_messages
from llm_service import create_gemini_client, generate_response


# Load environment variables
load_dotenv()


# 1. Prepare document
document = """
Machine learning enables computers to learn patterns from data.
Deep learning is a subset of machine learning.
Artificial intelligence helps machines perform intelligent tasks.
Python is widely used for artificial intelligence development.
Neural networks are commonly used in deep learning.
Supervised learning uses labeled training data.
"""


# 2. Split document into chunks
chunks = chunk_text(document, chunk_size=15, overlap=3)

print("Total chunks:", len(chunks))


# 3. Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


# 4. Generate document embeddings
chunk_embeddings = model.encode(chunks)


# 5. Ask a question
query = "Who invented the telephone?"


# 6. Generate query embedding
query_embedding = model.encode(query)


# 7. Calculate similarity
similarities = model.similarity(
    query_embedding,
    chunk_embeddings
)[0]


# 8. Rank chunks
results = list(zip(chunks, similarities.tolist()))

results.sort(
    key=lambda item: item[1],
    reverse=True
)


# 9. Retrieve top 2 chunks
top_k = 2
retrieved_chunks = results[:top_k]

print("\nRetrieved chunks:")

for chunk, score in retrieved_chunks:
    print(f"\nScore: {score:.4f}")
    print(chunk)


# 10. Prepare context
context = "\n\n".join(
    chunk for chunk, score in retrieved_chunks
)
print(context)

# 11. Build prompt
messages = build_messages(context, query)


# 12. Connect to Gemini
client = create_gemini_client()

try:
    response = generate_response(
        client,
        messages,
        max_output_tokens=2048
    )

    # 13. Parse Gemini JSON response
    result = json.loads(response)

    print("\n========== GEMINI ANSWER ==========")
    print(result["answer"])

    print("\nKeywords:")
    for keyword in result["keywords"]:
        print("-", keyword)

finally:
    client.close()
