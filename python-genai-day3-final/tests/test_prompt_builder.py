
import pytest
from prompt_builder import build_messages


def test_build_messages():
    result = build_messages(
        "Python is a programming language.",
        "What is Python?"
    )

    assert "instructions" in result
    assert "input" in result
    assert "What is Python?" in result["input"]


def test_empty_document():
    with pytest.raises(ValueError):
        build_messages("   ", "What is Python?")


def test_empty_question():
    with pytest.raises(ValueError):
        build_messages("Python is useful.", "   ")
