def inline_swap(a, b):
    a, b = b, a
    return a, b

result = inline_swap(1, 2)
print(result)
