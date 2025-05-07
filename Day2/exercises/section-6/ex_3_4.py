from pydantic import BaseModel

class User(BaseModel):
    """
    This model represents a user with essential information
    such as name and email address. It is used to handle user data
    throughout the application.
    """
    id: int
    name: str
    email: str

user_data = {"id": 1, "name": "Shreyas", "email": "charlie@example.com"}
user = User(**user_data)
print(user)