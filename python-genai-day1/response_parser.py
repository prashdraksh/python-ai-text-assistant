import json


def parse_response(response):
    if not isinstance(response, dict):
        raise ValueError("Response must be a dictionary.")

    if "output_text" not in response:
        raise ValueError("Missing output_text.")

    output_text = response["output_text"]

    if not isinstance(output_text, str):
        raise ValueError("output_text must be a string.")

    if not output_text.strip():
        raise ValueError("output_text cannot be empty.")

    return response["output_text"].strip()