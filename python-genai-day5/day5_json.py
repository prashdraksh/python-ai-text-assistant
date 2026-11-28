import json

response = """
{
    "answer": "Machine learning helps computers learn from data.",
    "keywords": [
        "machine learning",
        "computers",
        "data"
    ]
}
"""

data = json.loads(response)

print(data)
print(type(data))

print("\nAnswer:", data["answer"])
print("Keywords:", data["keywords"])