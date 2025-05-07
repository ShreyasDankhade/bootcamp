def access_key_eafp(my_dict, key):
    try:
        return my_dict[key]
    except KeyError:
        return "Key not found"

# Example usage:
result = access_key_eafp({'a': 1, 'b': 2}, 'c')
print(result)  # Output: Key not found
