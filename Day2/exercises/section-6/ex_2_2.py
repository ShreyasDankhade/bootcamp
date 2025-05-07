from pydantic import ValidationError

def validate_user_data(user_data):
    try:
        user = User(**user_data)
        return user
    except ValidationError as e:
        return str(e)

user_data = {"name": "Shreyas", "age": "not a number"}
validation_result = validate_user_data(user_data)
print(validation_result)  # Output: ValidationError showing 'age' is not an integer
