def filter_even_numbers():
    return list(filter(lambda x: x % 2 == 0, range(10)))

result = filter_even_numbers()
print(result)  # Output: [0, 2, 4, 6, 8]
