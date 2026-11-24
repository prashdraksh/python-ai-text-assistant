import json

schema = {
    "type": "object",
    "properties": {
        "answer": {"type": "string"},
        "keywords": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["answer", "keywords"]
}

response = {
    "answer": "Machine learning learns patterns from data.",
    "keywords": ["machine learning", "data"]
}

print(json.dumps(schema, indent=4))
print("\nResponse:")
print(json.dumps(response, indent=4))