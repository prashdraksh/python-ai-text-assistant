
import os
from google import genai
from google.genai import types

MODEL_NAME = "gemini-3.1-flash-lite"


def create_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing.")

    http_options = types.HttpOptions(timeout=120000)

    return genai.Client(
        api_key=api_key,
        http_options=http_options
    )


def generate_response(
    client,
    messages,
    max_output_tokens=2048
):
    if not isinstance(messages, dict):
        raise ValueError("Messages must be a dictionary.")

    instructions = messages.get("instructions")
    user_input = messages.get("input")

    if not isinstance(instructions, str) or not instructions.strip():
        raise ValueError("Valid instructions are required.")

    if not isinstance(user_input, str) or not user_input.strip():
        raise ValueError("Valid input is required.")

    if (
        not isinstance(max_output_tokens, int)
        or isinstance(max_output_tokens, bool)
        or max_output_tokens <= 0
    ):
        raise ValueError("max_output_tokens must be a positive integer.")

    interaction = client.interactions.create(
        model=MODEL_NAME,
        system_instruction=instructions,
        input=user_input,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": {
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
        },
        generation_config={
            "max_output_tokens": max_output_tokens,
            "thinking_level": "low"
        }
    )

    if interaction.status != "completed":
        errors = getattr(interaction, "errors", None)
        raise ValueError(
            f"Gemini did not complete successfully. "
            f"Status: {interaction.status}. Errors: {errors}"
        )

    output = interaction.output_text

    if not output:
        raise ValueError("Gemini completed without returning text.")

    return output
