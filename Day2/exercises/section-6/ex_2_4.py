from pydantic import BaseModel, conint, constr

class User(BaseModel):
    name: constr(min_length=3)
    age: conint(gt=0)

# Example usage
user_data = {"name": "Shreyas", "age": 30}
user = User(**user_data)
print(user)
# Validation errors
try:
    user_data = {"name": "Sh", "age": 30}
    user = User(**user_data)
except ValidationError as e:
    print(e)  # Output: ValidationError showing 'name' is too short

try:
    user_data = {"name": "Shreyas", "age": -1}
    user = User(**user_data)
except ValidationError as e:
    print(e)  # Output: ValidationError showing 'age' is less than 0
