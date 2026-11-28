
def keyword_search(query, documents):
    query_words = set(query.lower().split())

    results = []

    for document in documents:
        document_words = set(document.lower().split())

        score = len(query_words.intersection(document_words))

        results.append({
            "document": document,
            "score": score
        })

    results.sort(key=lambda item: item["score"], reverse=True)

    return results


documents = [
    "Machine learning enables computers to learn patterns from data.",
    "Python is a popular programming language.",
    "Deep learning uses neural networks.",
    "Artificial intelligence helps machines perform intelligent tasks."
]

query = "How do computers learn?"

results = keyword_search(query, documents)

for result in results:
    print(f"Score: {result['score']} | {result['document']}")
