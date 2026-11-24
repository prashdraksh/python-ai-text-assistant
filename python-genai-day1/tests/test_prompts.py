import pytest
from prompts import prepare_prompt


def test_summarize():
    result = prepare_prompt("Python is useful.", "SUMMARIZE")
    assert "Summarize in 3 bullet points." in result


def test_empty_text():
    with pytest.raises(ValueError):
        prepare_prompt("   ", "summarize")


def test_invalid_task():
    with pytest.raises(ValueError):
        prepare_prompt("Python is useful.", "translate")

@pytest.mark.parametrize(
    "text, task",
    [
        ("Python is useful.", "summarize"),
        ("Machine learning is interesting.", "explain"),
        ("Extract important keywords.", "extract"),
        ("  Python is great.  ", " SUMMARIZE "),
    ]
)

def test_valid_inputs(text, task):
    result = prepare_prompt(text, task)
    assert result