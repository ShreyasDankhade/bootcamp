import timeit

def time_list_comprehension():
    return timeit.timeit("[x*x for x in range(1000000)]", number=100)

def time_generator_expression():
    return timeit.timeit("(x*x for x in range(1000000))", number=100)


list_time = time_list_comprehension()
generator_time = time_generator_expression()

print(f"List comprehension time: {list_time} seconds")
print(f"Generator expression time: {generator_time} seconds")
