from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user_data = {"name": "Shreyas", "age": 30}
user = User(**user_data)
print(user)