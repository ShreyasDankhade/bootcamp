from functools import partial

# Create a partial function for generating nested dictionaries
nested_dict = partial(dict, **{'nested': {}})

new_dict = nested_dict(a=1, b=2)
new_dict['nested']['key'] = 'value'
print(new_dict)  # Output: {'a': 1, 'b': 2, 'nested': {'key': 'value'}}
