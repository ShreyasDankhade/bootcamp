def sum_large_range():
    return sum(x for x in range(1000000))  # Lazy evaluation with a generator expression

total = sum_large_range()
print(total)
