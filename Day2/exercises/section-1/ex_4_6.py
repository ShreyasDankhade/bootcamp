def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

# Create a closure for multiplication by 3
triple = make_multiplier(3)
print(triple(10))  # Output: 30

# Create a closure for multiplication by 5
quintuple = make_multiplier(5)
print(quintuple(10))  # Output: 50
