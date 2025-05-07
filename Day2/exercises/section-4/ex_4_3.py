import itertools

def generate_nones():
    return list(itertools.repeat(None, 10))


nones = generate_nones()
print(nones)  # Output: [None, None, None, None, None, None, None, None, None, None]
