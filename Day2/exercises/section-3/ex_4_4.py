from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

# Example usage:
user1 = User("Shreyas", 30)
user2 = User("Shreyas", 30)
user3 = User("Neel", 25)

print(user1 == user2)  # Output: True (attributes are equal)
print(user1 == user3)  # Output: False (attributes are different)
