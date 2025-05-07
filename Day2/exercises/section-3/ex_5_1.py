class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def validate_isbn(isbn):
        # A simple validation for ISBN (just a length check for this example)
        return len(isbn) == 13 and isbn.isdigit()



isbn = "9780143128540"
print(Book.validate_isbn(isbn))  # Output: True

invalid_isbn = "97801431285"
print(Book.validate_isbn(invalid_isbn))  # Output: False
