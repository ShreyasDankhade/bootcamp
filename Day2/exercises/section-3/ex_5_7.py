class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def describe(cls):
        return f"Book: {cls.title} by {cls.author}"

class EBook(Book):
    def __init__(self, title, author, file_format):
        super().__init__(title, author)
        self.file_format = file_format

    @classmethod
    def describe(cls):
        return f"EBook: {cls.title} by {cls.author}, Format: {cls.file_format}"

book = Book("1984", "Orwell")
ebook = EBook("1984", "Orwell", "EPUB")

print(book.describe())  # Output: Book: 1984 by Orwell
print(ebook.describe())  # Output: EBook: 1984 by Orwell, Format: EPUB
