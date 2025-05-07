x = 5  # Global variable

def modify_global():
    global x
    x = 10  # Modifies the global variable

modify_global()
print(x)  # Output: 10
