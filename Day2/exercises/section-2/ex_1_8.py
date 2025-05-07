def apply_method_lbyl(obj):
    if isinstance(obj, str):
        return obj.upper()
    else:
        return "Incompatible type"

# Example usage:
result = apply_method_lbyl("hello")
print(result)  # Output: HELLO

result = apply_method_lbyl(123)
print(result)  # Output: Incompatible type
