def apply(func, value):
    return func(value)


result = apply(abs, -42)
print(result)  # Output: 42

result = apply(str, 123)
print(result)  # Output: '123'
