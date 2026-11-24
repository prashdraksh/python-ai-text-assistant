
import math


def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimensions.")

    return sum(x * y for x, y in zip(a, b))


def cosine_similarity(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimensions.")

    magnitude_a = math.sqrt(sum(x ** 2 for x in a))
    magnitude_b = math.sqrt(sum(x ** 2 for x in b))

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Zero vectors are not allowed.")

    return dot_product(a, b) / (magnitude_a * magnitude_b)


def euclidean_distance(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimensions.")

    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


# Test vectors
A = [1, 2]
B = [4, 8]

print("\n========== UPDATED VECTOR B ==========")
print("Dot Product:", dot_product(A, B))
print("Cosine Similarity:", cosine_similarity(A, B))
print("Euclidean Distance:", euclidean_distance(A, B))