from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int

    def is_adult(self) -> bool:
        return self.age >= 18


# Example usage:
user1 = User("Shreyas", 30)
user2 = User("Neel", 15)

print(user1.is_adult())  # Output: True
print(user2.is_adult())  # Output: False
