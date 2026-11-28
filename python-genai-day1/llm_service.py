class FakeResponse:
    def __init__(self, output_text):
        self.output_text = output_text


class FakeLLMClient:
    def responses_create(self, prompt):
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        return FakeResponse(
            "This is a simulated AI response."
        )


def generate_response(client, prompt):

    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    response = client.responses_create(prompt)

    return response.output_text