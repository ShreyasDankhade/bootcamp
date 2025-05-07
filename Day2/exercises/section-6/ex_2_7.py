from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Shreyas", age=30)

user_dict = user.dict()
print(user_dict)

user_json = user.json()
print(user_json)