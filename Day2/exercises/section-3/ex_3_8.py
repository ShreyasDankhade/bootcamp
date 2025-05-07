class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __bool__(self):
        return bool(self.title) and bool(self.author)

# Example usage
book1 = Book("1984", "Orwell")
book2 = Book("", "")

print(bool(book1))  # Output: True
print(bool(book2))  # Output: False
