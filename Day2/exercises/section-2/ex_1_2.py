def access_key_lbyl(my_dict, key):
    if key in my_dict:
        return my_dict[key]
    else:
        return "Key not found"

# Example usage:
result = access_key_lbyl({'a': 1, 'b': 2}, 'c')
print(result)  # Output: Key not found
