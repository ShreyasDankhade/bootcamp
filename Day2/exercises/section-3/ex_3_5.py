from ex_1_1 import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

library = Library()
library.add_book(Book("1984", "Orwell"))
library.add_book(Book("Animal Farm", "Orwell"))

print(len(library))  # Output: 2
