import json


def parse_json_response(response_text):

    if not isinstance(response_text, str):
        raise ValueError("Response must be a string.")

    try:
        data = json.loads(response_text)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON response.")

    if not isinstance(data, dict):
        raise ValueError("JSON response must be an object.")

    return data