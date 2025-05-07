def generator_expression():
    evens = (x for x in range(10) if x % 2 == 0)
    for num in evens:
        print(num)

generator_expression()  