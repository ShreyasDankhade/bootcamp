numbers = [1, -2, 3, -4, 5]

# Replace negative numbers with 0
result = [0 if x < 0 else x for x in numbers]
print(result)  # [1, 0, 3, 0, 5]
