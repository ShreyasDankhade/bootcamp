def apply_functions():
    functions = [abs, str, hex]
    value = -42
    return [func(value) for func in functions]

results = apply_functions()
print(results)  # Output: [42, '-42', '-0x2a']
