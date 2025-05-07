def use_or_as_fallback():
    name = input("Enter your name: ") or "Anonymous"
    return name

# Enter your name: Alice
# Output: Alice

# Enter your name:
# Output: Anonymous
