def divide_with_success(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide")
    else:
        print("Success:", result)

# Test the function
divide_with_success(10, 2)  # Output: Success: 5.0
divide_with_success(10, 0)  # Output: Cannot divide
