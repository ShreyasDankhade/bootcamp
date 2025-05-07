def handle_multiple_exceptions(a, b):
    try:
        result = a / b
        if b == 0:
            raise ValueError("Division by zero")
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError as ve:
        print(f"Value error: {ve}")

# Test the function
handle_multiple_exceptions(10, 0)  # Output: Cannot divide by zero
handle_multiple_exceptions(10, 2)  # Output: 5.0
