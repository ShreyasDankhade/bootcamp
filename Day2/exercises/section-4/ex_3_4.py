from functools import partial

# Create a partial function to print with a fixed prefix
print_with_prefix = partial(print, "Prefix:")
print_with_prefix("Hello, World!")  # Output: Prefix: Hello, World!

# Apply another partial to add a suffix
print_with_prefix_and_suffix = partial(print_with_prefix, end=" :)")
print_with_prefix_and_suffix("Goodbye!")  # Output: Prefix: Goodbye! :)
