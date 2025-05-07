import itertools

def flatten_lists():
    return itertools.chain([1, 2], [3, 4], [5])

flattened = flatten_lists()
print(list(flattened))  # Output: [1, 2, 3, 4, 5]
