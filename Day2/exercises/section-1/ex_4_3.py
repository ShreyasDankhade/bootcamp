def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1  # Modifies the 'count' variable in the enclosing scope

    inner()  # Calling the inner function
    print(count)  # Output: 1


outer()
