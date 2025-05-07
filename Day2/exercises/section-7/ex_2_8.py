def generate_squares(n):
    for i in range(n):
        yield i * i  # Yield squares one by one

for square in generate_squares(10):
    print(square)
