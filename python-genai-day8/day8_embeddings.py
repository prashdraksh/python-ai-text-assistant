
from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Load the embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

sentences = [
    "I love programming.",
    "I enjoy writing code.",
    "I like eating pizza."
]

# Generate embeddings
embeddings = model.encode(sentences)

# Inspect the results
print("Number of sentences:", len(sentences))
print("Embedding shape:", embeddings.shape)

for sentence, embedding in zip(sentences, embeddings):
    print("\nSentence:", sentence)
    print("Dimensions:", len(embedding))
    print("First 5 values:", embedding[:5])



similarities = util.cos_sim(embeddings, embeddings)

print("\n========== SIMILARITY MATRIX ==========")
print(similarities)
print("\nEmbedding model:", model)
print("Embedding dimensions:", model.get_embedding_dimension())