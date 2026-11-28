
import pytest

from structured_parser import parse_json_response


def test_valid_json_response():
    response = """
    {
        "answer": "Python is a programming language.",
        "keywords": ["Python", "programming"]
    }
    """

    result = parse_json_response(response)

    assert result["answer"] == "Python is a programming language."
    assert result["keywords"] == ["Python", "programming"]


def test_invalid_json():
    with pytest.raises(ValueError, match="Invalid JSON response"):
        parse_json_response('{"answer": "Hello"')


def test_missing_required_field():
    response = '{"answer": "Hello"}'

    with pytest.raises(ValueError, match="Invalid response structure"):
        parse_json_response(response)


def test_wrong_data_type():
    response = """
    {
        "answer": "Hello",
        "keywords": "Python"
    }
    """

    with pytest.raises(ValueError, match="Invalid response structure"):
        parse_json_response(response)


def test_empty_answer():
    response = '{"answer": "", "keywords": ["Python"]}'

    with pytest.raises(ValueError, match="Invalid response structure"):
        parse_json_response(response)


def test_unexpected_field():
    response = """
    {
        "answer": "Hello",
        "keywords": ["Python"],
        "confidence": 0.95
    }
    """

    with pytest.raises(ValueError, match="Invalid response structure"):
        parse_json_response(response)
