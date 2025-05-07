def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

# Create a closure with a multiplier of 3
triple = make_multiplier(3)

# Call the closure
print(triple(10))  # Output: 30
