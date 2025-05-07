class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def static_method():
        # Static method does not have access to instance (`self`) or class (`cls`)
        # Uncommenting the following lines will raise an error
        # print(self.title)  # AttributeError
        # print(cls.title)   # NameError
        print("This is a static method.")


book = Book("1984", "Orwell")
book.static_method()  # Output: This is a static method.
Book.static_method()  # Output: This is a static method.
