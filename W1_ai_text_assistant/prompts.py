from validation import validate_text

TASK_INSTRUCTIONS = {
        "summarize": "Summarize the following text in a concise manner, highlighting the key points and main ideas.",
        "explain": "Explain the following text in a clear and understandable way.",
        "extract": "Extract the key information from the following text."
    }

def build_prompt(text: str, task: str) -> dict:
    text = validate_text(text)
    task = validate_text(task)
    task = task.lower()

    if task not in TASK_INSTRUCTIONS:
        raise ValueError("Unsupported task.")
    
    output = {
        "instructions": TASK_INSTRUCTIONS[task],
        "input": text
    }
    return output
