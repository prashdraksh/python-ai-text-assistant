
import os
from google import genai


MODEL_NAME = "gemini-4-hydrogen"


def create_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing.")

    return genai.Client(api_key=api_key)



def generate_response(
    client,
    messages,
    max_output_tokens=200
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
                    "answer": {
                        "type": "string"
                    },
                    "keywords": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": ["answer", "keywords"]
            }
        },
        generation_config={
            "max_output_tokens": 2048,
            "thinking_level": "low"
        }
    )

    

    if interaction.status != "completed":
        errors = getattr(interaction, "errors", None)

        raise ValueError(
            f"Gemini did not complete successfully. "
            f"Status: {interaction.status}. "
            f"Errors: {errors}"
        )

    output = interaction.output_text

    if not output:
        raise ValueError("Gemini completed without returning text.")

    return output






# class FakeResponse:
#     def __init__(self, output_text):
#         self.output_text = output_text


# class FakeLLMClient:
#     def responses_create(
#         self,
#         instructions,
#         input,
#         temperature,
#         max_output_tokens
#     ):
#         if not instructions.strip() or not input.strip():
#             raise ValueError("Instructions and input cannot be empty.")

#         # Simulated LLM output
#         simulated_output = """
#         {
#             "answer": "Machine learning enables computers to learn patterns from data.",
#             "keywords": ["Machine Learning", "AI", "Data"]
#         }
#         """

#         return FakeResponse(simulated_output)


# def generate_response(
#     client,
#     messages,
#     temperature=0.2,
#     max_output_tokens=200
# ):
#     if not isinstance(messages, dict):
#         raise ValueError("Messages must be a dictionary.")

#     instructions = messages.get("instructions")
#     user_input = messages.get("input")

#     if not isinstance(instructions, str) or not instructions.strip():
#         raise ValueError("Valid instructions are required.")

#     if not isinstance(user_input, str) or not user_input.strip():
#         raise ValueError("Valid input is required.")

#     if not 0 <= temperature <= 2:
#         raise ValueError("Temperature must be between 0 and 2.")

#     if max_output_tokens <= 0:
#         raise ValueError("max_output_tokens must be positive.")

#     response = client.responses_create(
#         instructions=instructions,
#         input=user_input,
#         temperature=temperature,
#         max_output_tokens=max_output_tokens
#     )

#     return response.output_text
