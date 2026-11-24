import pytest

from llm_service import (
    FakeLLMClient,
    generate_response
)
class BrokenClient:
    def responses_create(self, prompt):
        raise RuntimeError("Service unavailable")
    
@pytest.fixture
def client():
    return FakeLLMClient()

def test_client_failure():
    client = BrokenClient()

    with pytest.raises(RuntimeError):
        generate_response(client, "Summarize Python.")

def test_successful_response(client):

    result = generate_response(
        client,
        "Summarize Python."
    )

    assert result == "This is a simulated AI response."


def test_empty_prompt(client):

    with pytest.raises(ValueError):
        generate_response(client, "   ")

# def test_successful_response(client):
#     result = generate_response(client, "Summarize Python.")
#     assert result == "This is a simulated AI response."