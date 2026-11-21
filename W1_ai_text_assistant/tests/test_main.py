from main import prepare_prompt
import pytest

def test_valid_text_and_task():
    result = prepare_prompt("Python is useful.", "summarize")
    assert result["input"] == "Python is useful."
    assert result["instructions"] == "Summarize the following text in a concise manner, highlighting the key points and main ideas."

def test_invalid_text():
    with pytest.raises(ValueError):
        prepare_prompt("", "summarize")