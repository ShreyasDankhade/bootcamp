from ex_1_1 import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __getitem__(self, index):
        return self.books[index]

# Example usage
library = Library()
library.add_book(Book("1984", "Orwell"))
library.add_book(Book("Animal Farm", "Orwell"))

print(library[0].title)  # Output: 1984
