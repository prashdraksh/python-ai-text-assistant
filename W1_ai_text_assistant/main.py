
from prompts import build_prompt
from llm_service import generate_response
from structured_parser import parse_json_response


def prepare_prompt(text: str, task: str) -> dict:
    return build_prompt(text, task)


def run_assistant(client, text: str, task: str) -> dict:
    # 1. Build the prompt
    messages = prepare_prompt(text, task)

    # 2. Send request to Gemini
    response = generate_response(client, messages)

    # 3. Parse and validate JSON
    result = parse_json_response(response)

    return result
