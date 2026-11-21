import pytest
from prompts import build_prompt


def test_summarize_task():
    result = build_prompt("Python is useful.", "summarize")

    assert result["input"] == "Python is useful."
    assert result["instructions"] == "Summarize the following text in a concise manner, highlighting the key points and main ideas."

def test_explain_task():
    result = build_prompt("Python is useful.", "explain")

    assert result["input"] == "Python is useful."
    assert result["instructions"] == "Explain the following text in a clear and understandable way."

def test_extract_task():
    result = build_prompt("Python is useful.", "extract")

    assert result["input"] == "Python is useful."
    assert result["instructions"] == "Extract the key information from the following text."

def test_uppercase_task():
    result = build_prompt("Python is useful.", "SUMMARIZE")

    assert result["input"] == "Python is useful."
    assert result["instructions"] == "Summarize the following text in a concise manner, highlighting the key points and main ideas."

def test_unsupported_task():
    with pytest.raises(ValueError):
        build_prompt("Python is useful.", "unsupported_task")

def test_empty_text():
    with pytest.raises(ValueError):
        build_prompt("", "summarize")

def test_empty_task():
    with pytest.raises(ValueError):
        build_prompt("Python is useful.", "")