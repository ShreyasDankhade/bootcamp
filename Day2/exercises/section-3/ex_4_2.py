from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int = 0  # Default value

# Example usage:
user1 = User("Shreyas")
user2 = User("Neel", 25)

print(user1)
print(user2)