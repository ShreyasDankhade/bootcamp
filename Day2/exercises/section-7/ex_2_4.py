def contains_divisible_by_99(numbers):
    return any(x % 99 == 0 for x in numbers)

big_list = range(1, 1000000)
result = contains_divisible_by_99(big_list)
print(result)