from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "answer": {
            "type": "string",
            "minLength": 1
        },
        "keywords": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1
        }
    },
    "required": ["answer", "keywords"],
    "additionalProperties": False
}

# response = {
#     "answer": "Machine learning learns patterns from data.",
#     "keywords": "machine learning, data",
#     "confidence": 0.95
# }
response = {
    "answer": "",
    "keywords": ["machine learning"]
}

try:
    validate(instance=response, schema=schema)
    print("Response is valid!")
except ValidationError as exc:
    print("Invalid response:", exc.message)