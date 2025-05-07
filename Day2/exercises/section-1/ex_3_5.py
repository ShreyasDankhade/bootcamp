def display_info(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)

# Test the function
display_info(1, 2, 3, name="Shreyas", age=30)
# Output:
# Arguments: (1, 2, 3)
# Keyword Arguments: {'name': 'Shreyas', 'age': 30}
