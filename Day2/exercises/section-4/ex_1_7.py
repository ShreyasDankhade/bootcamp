def compose(f, g):
    return lambda x: f(g(x))

def add_one(x):
    return x + 1

def square(x):
    return x ** 2

composed_function = compose(add_one, square)
print(composed_function(3))  # Output: 10 (add_one(square(3)) -> add_one(9) -> 10)
