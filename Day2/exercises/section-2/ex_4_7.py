class DatabaseConnection:
    def __enter__(self):
        print("Opening database connection")
        # DB connection setup
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")
        #  DB connection teardown
        if exc_type:
            print(f"Error: {exc_val}")
        return True


def use_db_connection():
    with DatabaseConnection() as db:
        print("Using the database connection")
        # Uncomment to simulate an error
        # raise Exception("Database error")


use_db_connection()
