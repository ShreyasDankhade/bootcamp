user = {"name": "Shreyas"}

# .get() — returns None (or a default you provide) if key is missing
print(user.get("name"))       # Shreyas
print(user.get("age"))        # None
print(user.get("age", 0))     # 0  (default value)

# .setdefault() — returns existing value or sets+returns default if missing
age = user.setdefault("age", 25)
print(age)                    # 25
print(user)                   # {'name': 'Shreyas', 'age': 25}
