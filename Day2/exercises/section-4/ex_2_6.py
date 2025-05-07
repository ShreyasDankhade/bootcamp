def role_required(role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role == role:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"Access denied. Role '{role}' required.")
        return wrapper
    return decorator


@role_required("admin")
def delete_user(user_id):
    return f"User {user_id} deleted."

# Test with valid role
print(delete_user("admin", 123))  # Works fine

# Test with invalid role
try:
    print(delete_user("guest", 123))  # Raises PermissionError
except PermissionError as e:
    print(e)
