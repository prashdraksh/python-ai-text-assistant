from validation import validate_text


def build_prompt(text: str, task: str) -> str:

    if task == "summarize":
        instruction = "Summarize in 3 bullet points."

    elif task == "explain":
        instruction = "Explain to a beginner."

    elif task == "extract":
        instruction = "Extract key facts as a numbered list."

    else:
        raise ValueError("Unknown task.")

    return f"{instruction}\n\nText:\n{text}"


def prepare_prompt(text: str, task: str) -> str:

    text = validate_text(text)
    task = task.strip().lower()

    return build_prompt(text, task)