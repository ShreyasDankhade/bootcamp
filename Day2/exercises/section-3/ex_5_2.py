class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, s):
        title, author = s.split("|")
        return cls(title, author)


book_string = "1984|George Orwell"
book = Book.from_string(book_string)
print(book.title)  # Output: 1984
print(book.author)  # Output: George Orwell
