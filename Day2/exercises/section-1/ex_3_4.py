def show_settings(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Test the function
show_settings(theme="dark", font="Arial", size=12)
# Output:
# theme: dark
# font: Arial
# size: 12
