def multiple_unpack(lst):
    a, b, *rest = lst
    return a, b, rest

result = multiple_unpack([1, 2, 3, 4, 5])
print(result)
