def build_messages(document, question):

    system_instructions = """
    You are a professional document analyst.

    Rules:
    1. Answer only using the provided document.
    2. Do not invent information.
    3. If the answer is unavailable, say so.
    4. Keep responses concise.
    """

    user_message = f"""
    Document:
    {document}

    Question:
    {question}
    """

    return {
        "instructions": system_instructions.strip(),
        "input": user_message.strip()
    }