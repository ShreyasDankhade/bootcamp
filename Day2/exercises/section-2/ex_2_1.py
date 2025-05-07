def enumerate_example(lst):
    return [(index, value) for index, value in enumerate(lst)]

result = enumerate_example([10, 20, 30])
print(result)
