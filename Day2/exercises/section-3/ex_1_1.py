# Define the Book class
class Book:
    # Class variable
    category = "Fiction"

    def __init__(self, title="Unknown", author="Unknown"):
        """
        Constructor to initialize title and author. Provides default values.
        """
        self.title = title
        self.author = author

    def describe(self):
        """
        Method to return a formatted string with book details.
        """
        return f"Title: {self.title}, Author: {self.author}, Category: {self.category}"

    def update_title(self, new_title):
        """
        Method to update the title of the book.
        """
        self.title = new_title


# Example of creating an object and printing its attributes
def create_and_print_book():
    book = Book("1984", "Orwell")
    print(f"Title: {book.title}, Author: {book.author}")


# Example of calling the describe method
def describe_book():
    book = Book("1984", "Orwell")
    print(book.describe())


# Example of using a class variable (category)
def print_category():
    book = Book("1984", "Orwell")
    print(f"Category from instance: {book.category}")
    print(f"Category from class: {Book.category}")


# Example of updating the object's state (title)
def update_and_verify_title():
    book = Book("1984", "Orwell")
    print("Before update:", book.describe())
    book.update_title("Animal Farm")
    print("After update:", book.describe())


# Example of using default constructor values
def create_with_default_values():
    book = Book()
    print(f"Book with default values: {book.describe()}")


# Example of adding a dynamic attribute after object creation
def add_dynamic_attribute():
    book = Book("1984", "Orwell")
    book.year_published = 1949  # Adding an attribute dynamically
    print(f"Book year published: {book.year_published}")


# Example of checking object type with isinstance
def check_type_of_object():
    book = Book("1984", "Orwell")
    print(f"Is book an instance of Book? {isinstance(book, Book)}")
    print(f"Is book an instance of str? {isinstance(book, str)}")


# Reusable function calls
if __name__ == "__main__":
    create_and_print_book()
    describe_book()
    print_category()
    update_and_verify_title()
    create_with_default_values()
    add_dynamic_attribute()
    check_type_of_object()
