nested_lst = [[1, 2], [3, 4]]

# Flatten the list
flattened = [item for sublist in nested_lst for item in sublist]
print(flattened)  # [1, 2, 3, 4]
