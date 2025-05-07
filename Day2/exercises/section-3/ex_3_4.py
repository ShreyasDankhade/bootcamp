class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.title < other.title
        return False

books = [Book("1984", "Orwell"), Book("Animal Farm", "Orwell"), Book("Brave New World", "Huxley")]
books.sort()

for book in books:
    print(book.title)  # Output: Animal Farm, Brave New World, 1984
