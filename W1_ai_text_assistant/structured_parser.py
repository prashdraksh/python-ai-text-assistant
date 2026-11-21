
import json
from jsonschema import validate, ValidationError


RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {
            "type": "string",
            "minLength": 1
        },
        "keywords": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "minItems": 1
        }
    },
    "required": ["answer", "keywords"],
    "additionalProperties": False
}


def parse_json_response(response_text):

    if not isinstance(response_text, str):
        raise ValueError("Response must be a string.")

    try:
        data = json.loads(response_text)
    except json.JSONDecodeError as exc:
        raise ValueError("Invalid JSON response.") from exc

    if not isinstance(data, dict):
        raise ValueError("JSON response must be an object.")

    try:
        validate(instance=data, schema=RESPONSE_SCHEMA)
    except ValidationError as exc:
        raise ValueError(f"Invalid response structure: {exc.message}") from exc

    return data
