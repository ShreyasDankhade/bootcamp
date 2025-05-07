def unpacking_in_loops(lst):
    return [(x, y) for x, y in lst]

result = unpacking_in_loops([(1, 2), (3, 4)])
print(result)
