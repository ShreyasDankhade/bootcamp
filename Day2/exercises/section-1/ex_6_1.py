def manual_iterator():
    lst = [1, 2, 3, 4]
    iterator = iter(lst)

    # Calling next manually
    print(next(iterator))  # Output: 1
    print(next(iterator))  # Output: 2
    print(next(iterator))  # Output: 3
    print(next(iterator))  # Output: 4
    # Uncommenting the next line will raise StopIteration
    # print(next(iterator))

manual_iterator()
