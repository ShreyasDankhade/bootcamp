class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __hash__(self):
        return hash((self.title, self.author))

book1 = Book("1984", "Orwell")
book2 = Book("1984", "Orwell")
book_set = {book1, book2}

print(len(book_set))  # Output: 1 (since they are considered equal and hashed the same)
