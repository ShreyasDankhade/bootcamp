def info(name, age=0):
    print(f"Name: {name}, Age: {age}")

# Call it with keyword arguments in any order
info(name="Shreyas", age=30)   # Output: Name: Shreyas, Age: 30
info(age=25, name="Neel")     # Output: Name: Neel, Age: 25
