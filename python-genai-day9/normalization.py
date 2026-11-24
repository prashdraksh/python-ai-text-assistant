
import math


def normalize_vector(vector):
    magnitude = math.sqrt(sum(x ** 2 for x in vector))

    if magnitude == 0:
        raise ValueError("Cannot normalize a zero vector.")

    return [x / magnitude for x in vector]


vector = [3, 4]

normalized = normalize_vector(vector)

print("Original vector:", vector)
print("Normalized vector:", normalized)

normalized_magnitude = math.sqrt(
    sum(x ** 2 for x in normalized)
)

print("Normalized magnitude:", normalized_magnitude)
