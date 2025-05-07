def use_and_for_guarded_expression(is_admin, user_id):
    # This will only call delete_user if is_admin is True
    is_admin and delete_user(user_id)

def delete_user(user_id):
    print(f"User {user_id} deleted.")

use_and_for_guarded_expression(True, 101)  # Output: User 101 deleted.
use_and_for_guarded_expression(False, 102)  # No output (does not call delete_user)
