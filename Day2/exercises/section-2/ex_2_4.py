def sort_by_second_item(lst):
    return sorted(lst, key=lambda x: x[1])

result = sort_by_second_item([(1, 'b'), (3, 'a'), (2, 'c')])
print(result)