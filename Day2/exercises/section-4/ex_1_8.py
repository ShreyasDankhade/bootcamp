def make_multiplier(factor):
    return lambda x: x * factor

doubler = make_multiplier(2)
tripler = make_multiplier(3)

print(doubler(5))  # Output: 10
print(tripler(5))  # Output: 15
