
def build_messages(document, question):
    if not isinstance(document, str) or not document.strip():
        raise ValueError("Document cannot be empty.")

    if not isinstance(question, str) or not question.strip():
        raise ValueError("Question cannot be empty.")

    system_instructions = """
    You are a professional document analyst.

    Rules:
    1. Answer using only the provided document.
    2. Do not invent information.
    3. If the answer is unavailable, say so.
    4. Keep responses concise.
    5. Return the result as valid JSON with these fields:
       answer, keywords.
    """

    user_message = f"""
    Document:
    {document.strip()}

    Question:
    {question.strip()}
    """

    return {
        "instructions": system_instructions.strip(),
        "input": user_message.strip()
    }
