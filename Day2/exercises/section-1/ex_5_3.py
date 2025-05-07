def divide_with_cleanup(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Cannot divide")
    finally:
        print("Cleanup done")

# Test the function
divide_with_cleanup(10, 2)  # Output: 5.0 Cleanup done
divide_with_cleanup(10, 0)  # Output: Cannot divide Cleanup done
