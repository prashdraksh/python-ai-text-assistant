
import math


def cosine_similarity(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimension.")

    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Zero vectors are not allowed.")

    return dot_product / (magnitude_a * magnitude_b)


vector_a = [1, 0, 1]
vector_b = [0.9, 0.1]
vector_c = [0, 1]

print(cosine_similarity(vector_a, vector_b))
print(cosine_similarity(vector_a, vector_c))
