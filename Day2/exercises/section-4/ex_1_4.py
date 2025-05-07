def square_numbers():
    numbers = [1, 2, 3]
    return list(map(lambda x: x ** 2, numbers))

result = square_numbers()
print(result)  # Output: [1, 4, 9]
