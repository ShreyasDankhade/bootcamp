from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    country: Optional[str] = None  # Default value is None

user_data = {"name": "Shreyas", "age": 30}
user = User(**user_data)
print(user)