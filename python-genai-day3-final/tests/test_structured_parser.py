
import pytest
from structured_parser import parse_json_response


def test_valid_json():
    result = parse_json_response('{"answer": "Hello"}')

    assert result["answer"] == "Hello"


def test_invalid_json():
    with pytest.raises(ValueError):
        parse_json_response('{"answer":')


def test_json_array():
    with pytest.raises(ValueError):
        parse_json_response('["Python", "Java"]')
