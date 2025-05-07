import itertools

def duplicate_iterator():
    return itertools.tee(range(3), 2)

iter1, iter2 = duplicate_iterator()

# Iterate independently on both copies
print(list(iter1))  # Output: [0, 1, 2]
print(list(iter2))  # Output: [0, 1, 2]
