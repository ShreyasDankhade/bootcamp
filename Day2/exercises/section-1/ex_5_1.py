def divide(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Cannot divide")

# Test the function
divide(10, 0)  # Output: Cannot divide
