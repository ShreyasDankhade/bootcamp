def access_attribute_eafp(obj, attr):
    try:
        return getattr(obj, attr)
    except AttributeError:
        return f"Attribute '{attr}' not found"

# Example usage:
class MyClass:
    name = "Alice"

obj = MyClass()
result = access_attribute_eafp(obj, "name")
print(result)  # Output: Alice

result = access_attribute_eafp(obj, "age")
print(result)  # Output: Attribute 'age' not found
