class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def validate_isbn(isbn):
        return len(isbn) == 13 and isbn.isdigit()


book = Book("1984", "Orwell")
isbn = "9780143128540"

# Calling static method from instance
print(book.validate_isbn(isbn))  # Output: True

# Calling static method from class
print(Book.validate_isbn(isbn))  # Output: True
