from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    age: int
    tags: List[str] = field(default_factory=list)

user = User(name="Grace", age=40)
print(user.tags)  # Output: []

user_with_tags = User(name="Hank", age=35, tags=["admin", "moderator"])
print(user_with_tags.tags)