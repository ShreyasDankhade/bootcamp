import itertools

def generate_permutations():
    return itertools.permutations([1, 2, 3], 2)

def generate_combinations():
    return itertools.combinations([1, 2, 3], 2)

print("Permutations (2):", list(generate_permutations()))  # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print("Combinations (2):", list(generate_combinations()))  # Output: [(1, 2), (1, 3), (2, 3)]
