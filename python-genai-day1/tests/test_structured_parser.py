import pytest
from structured_parser import parse_json_response


def test_valid_json():
    response = '{"title": "Python Basics"}'

    result = parse_json_response(response)

    assert isinstance(result, dict)
    assert result["title"] == "Python Basics"


def test_invalid_json():
    response = '{"title": "Python Basics"'

    with pytest.raises(ValueError):
        parse_json_response(response)


def test_json_array():
    response = '["Python", "Java"]'

    with pytest.raises(ValueError):
        parse_json_response(response)


def test_integer_input():
    with pytest.raises(ValueError):
        parse_json_response(123)


def test_empty_json_object():
    response = '{}'

    result = parse_json_response(response)

    assert result == {}
    assert isinstance(result, dict)