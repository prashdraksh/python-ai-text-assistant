def validate_text(text: str) -> str:
    text = text.strip()

    if not text:
        raise ValueError("Text cannot be empty.")

    return text