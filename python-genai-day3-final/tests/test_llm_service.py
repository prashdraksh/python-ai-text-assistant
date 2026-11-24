
import pytest
from llm_service import FakeLLMClient, generate_response


def test_successful_generation():
    client = FakeLLMClient()

    messages = {
        "instructions": "Be helpful.",
        "input": "Explain Python."
    }

    result = generate_response(client, messages)

    assert isinstance(result, str)
    assert result


def test_invalid_temperature():
    client = FakeLLMClient()

    messages = {
        "instructions": "Be helpful.",
        "input": "Explain Python."
    }

    with pytest.raises(ValueError):
        generate_response(client, messages, temperature=3)
