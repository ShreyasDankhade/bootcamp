import timeit

def time_builtin_sort():
    return timeit.timeit("sorted([5, 3, 8, 2, 9])", number=1000)

def time_custom_sort():
    return timeit.timeit("sorted([5, 3, 8, 2, 9], reverse=True)", number=1000)

builtin_sort_time = time_builtin_sort()
custom_sort_time = time_custom_sort()

print(f"Built-in sort time: {builtin_sort_time} seconds")
print(f"Custom sort time: {custom_sort_time} seconds")
