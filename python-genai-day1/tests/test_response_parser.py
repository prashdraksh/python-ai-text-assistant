import pytest
from response_parser import parse_response


def test_valid_response():
    response = {
        "output_text": "Hello AI"
    }

    assert parse_response(response) == "Hello AI"


def test_missing_output_text():
    response = {"id": "response_123"}

    with pytest.raises(ValueError):
        parse_response(response)


@pytest.mark.parametrize("text", ["", "   ", "\n\t"])

def test_empty_output_text(text):
    response = {"output_text": text}

    with pytest.raises(ValueError):
        parse_response(response)


def test_non_string_output():
    response = {"output_text": 123}

    with pytest.raises(ValueError):
        parse_response(response)


def test_non_dictionary_response():
    with pytest.raises(ValueError):
        parse_response("Hello AI")