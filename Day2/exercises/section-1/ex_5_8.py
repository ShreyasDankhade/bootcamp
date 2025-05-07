def nested_try_blocks(a, b, c):
    try:
        result = a / b
        try:
            result = result / c
        except ZeroDivisionError:
            print("Inner: Cannot divide by zero")
    except ZeroDivisionError:
        print("Outer: Cannot divide by zero")

# Test the function
nested_try_blocks(10, 2, 0)  # Output: Inner: Cannot divide by zero
nested_try_blocks(10, 0, 5)  # Output: Outer: Cannot divide by zero
