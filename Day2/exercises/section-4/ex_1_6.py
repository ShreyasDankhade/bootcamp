def sort_by_second_element():
    data = [(1, "b"), (2, "a")]
    return sorted(data, key=lambda x: x[1])

result = sort_by_second_element()
print(result)  # Output: [(2, 'a'), (1, 'b')]
