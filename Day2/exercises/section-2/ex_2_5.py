def map_and_filter_example(lst):
    doubled = list(map(lambda x: x * 2, lst))
    filtered = list(filter(lambda x: x % 2 != 0, lst))
    return doubled, filtered

result = map_and_filter_example([1, 2, 3, 4, 5])
print(result)
