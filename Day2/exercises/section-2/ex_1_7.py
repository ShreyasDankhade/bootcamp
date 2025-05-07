def safe_int_conversion(value):
    try:
        return int(value)
    except ValueError:
        return "Invalid input, could not convert to int"

# Example usage:
result = safe_int_conversion("123")
print(result)  # Output: 123

result = safe_int_conversion("abc")
print(result)  # Output: Invalid input, could not convert to int
