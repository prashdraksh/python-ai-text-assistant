import pytest
from validation import validate_text

def test_valid_text():
    result = validate_text(" Hello Python ")
    assert result == "Hello Python"

def test_empty_string():
    with pytest.raises(ValueError):
        validate_text("")

def test_whitespace_string():
    with pytest.raises(ValueError):
        validate_text("   ")

def test_integer_input():
    with pytest.raises(ValueError):
        validate_text(123)

def test_none_input():
    with pytest.raises(ValueError):
        validate_text(None)