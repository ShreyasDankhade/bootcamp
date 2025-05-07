import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_dict(cls, book_dict):
        return cls(book_dict["title"], book_dict["author"])

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(data["title"], data["author"])

book_dict = {"title": "1984", "author": "George Orwell"}
book_from_dict = Book.from_dict(book_dict)
print(book_from_dict.title)  # Output: 1984

json_string = '{"title": "Animal Farm", "author": "George Orwell"}'
book_from_json = Book.from_json(json_string)
print(book_from_json.title)  # Output: Animal Farm
