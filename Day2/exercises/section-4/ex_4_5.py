import itertools

def slice_range():
    return itertools.islice(range(10), 3, 7)  # Skips first 3, takes next 4

sliced = slice_range()
print(list(sliced))  # Output: [3, 4, 5, 6]
