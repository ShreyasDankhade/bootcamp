def compare_for_loop():
    # Using list comprehension
    evens_list = [x for x in range(10) if x % 2 == 0]
    print("List comprehension:", evens_list)

    # Using generator expression
    evens_gen = (x for x in range(10) if x % 2 == 0)
    print("Generator expression:", list(evens_gen))  # Converting to list for display


compare_for_loop()
