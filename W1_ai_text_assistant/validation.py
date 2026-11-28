def validate_text(text: str) -> str:

    # 1. Check input type
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    # 2. Remove unnecessary whitespace
    text = text.strip()
    # 3. Check whether text is empty
    if not text:
        raise ValueError("Input cannot be empty.")
    # 4. Return cleaned text
    return text