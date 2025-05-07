def greet_user(name, *, age):
    print(f"Hello {name}, Age: {age}")

# Test the function
greet_user("Shreyas", age=25)  # Output: Hello Shreyas, Age: 25
# greet_user("Shreyas", 25)     # This will raise a TypeError
