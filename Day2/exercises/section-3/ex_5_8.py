class Book:
    category = "Fiction"

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def validate_isbn(isbn):
        return len(isbn) == 13 and isbn.isdigit()

    @classmethod
    def category_info(cls):
        return f"Books in this category are: {cls.category}"

    def describe(self):
        return f"Title: {self.title}, Author: {self.author}, Category: {self.category}"


book = Book("1984", "Orwell")
isbn = "9780143128540"

# Static method for ISBN validation
print(Book.validate_isbn(isbn))  # Output: True

# Class method for category information
print(Book.category_info())  # Output: Books in this category are: Fiction

# Instance method to describe the book
print(book.describe())  # Output: Title: 1984, Author: Orwell, Category: Fiction
