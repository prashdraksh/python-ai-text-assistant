def sentence_chunk(text, max_words=20):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Input text must be a non-empty string.")

    if isinstance(max_words, bool) or not isinstance(max_words, int) or max_words < 1:
        raise ValueError("max_words must be a positive integer.")

    sentences = [
        sentence.strip() + "."
        for sentence in text.split(".")
        if sentence.strip()
    ]

    chunks = []
    current_chunk = []
    current_word_count = 0

    for sentence in sentences:
        words = sentence.split()
        word_count = len(words)

        if current_word_count + word_count <= max_words:
            current_chunk.append(sentence)
            current_word_count += word_count
        else:
            if current_chunk:
                chunks.append(" ".join(current_chunk))

            current_chunk = [sentence]
            current_word_count = word_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

text = (
    "Python is a programming language. "
    "It is easy to learn. "
    "Machine learning uses data to identify patterns. "
    "Deep learning uses neural networks."
)

print(sentence_chunk(text, max_words=10))
print(sentence_chunk("Python is great.", max_words=5))
print(sentence_chunk("Python is great. Machine learning is useful.", max_words=5))
print(sentence_chunk("This sentence contains more than five words.", max_words=5))