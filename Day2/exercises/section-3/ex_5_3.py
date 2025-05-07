class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, s):
        title, author = s.split("|")
        return cls(title, author)

class EBook(Book):
    def __init__(self, title, author, file_format):
        super().__init__(title, author)
        self.file_format = file_format

    @classmethod
    def from_string(cls, s):
        title, author, file_format = s.split("|")
        return cls(title, author, file_format)

ebook_string = "1984|George Orwell|EPUB"
ebook = EBook.from_string(ebook_string)
print(ebook.title)  # Output: 1984
print(ebook.author)  # Output: George Orwell
print(ebook.file_format)  # Output: EPUB
