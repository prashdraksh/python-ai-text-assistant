
def estimate_tokens(text):
    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    return len(text.split())


def check_output_limit(text, max_tokens):
    if not isinstance(max_tokens, int) or isinstance(max_tokens, bool):
        raise ValueError("Token limit must be an integer.")

    if max_tokens <= 0:
        raise ValueError("Token limit must be positive.")

    estimated_tokens = estimate_tokens(text)

    if estimated_tokens > max_tokens:
        raise ValueError("Output exceeds estimated token limit.")

    return estimated_tokens
