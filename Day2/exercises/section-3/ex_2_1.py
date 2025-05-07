# novel.py

from ex_1_1 import Book


class Novel(Book):
    def __init__(self, title="Unknown", author="Unknown", genre="Unknown"):
        """
        Initialize the Novel class, inheriting from Book, and add a genre.
        """
        super().__init__(title, author)
        self.genre = genre

    def describe(self):
        """
        Override the describe method to include the word "Novel:" and genre.
        """
        base_description = super().describe()  # Call the parent class describe
        return f"Novel: {base_description}, Genre: {self.genre}"

    def __str__(self):
        """
        String representation for printing, extending Book's __str__ method.
        """
        return f"Novel: {self.title} by {self.author}, Genre: {self.genre}"


# Example of multiple inheritance
class AudioMixin:
    def play_audio(self):
        print(f"Playing audio version of {self.title}")


class AudioBook(Novel, AudioMixin):
    def __init__(self, title, author, genre, audio_format):
        super().__init__(title, author, genre)
        self.audio_format = audio_format

    def __str__(self):
        """
        String representation for the AudioBook, incorporating audio format.
        """
        return f"AudioBook: {self.title} by {self.author}, Genre: {self.genre}, Format: {self.audio_format}"


# Polymorphism demonstration
def demonstrate_polymorphism():
    books = [Book("1984", "Orwell"), Novel("Brave New World", "Huxley", "Dystopian")]
    for book in books:
        print(book.describe())


# Example of checking instance type
def check_isinstance():
    novel = Novel("1984", "Orwell", "Dystopian")
    print(isinstance(novel, Book))  # True
    print(isinstance(novel, Novel))  # True


# Test the functionalities
if __name__ == "__main__":
    # Create and test Novel
    novel = Novel("1984", "Orwell", "Dystopian")
    print(novel.describe())  # Output: Novel: Title: 1984, Author: Orwell, Category: Fiction, Genre: Dystopian

    # Test AudioBook
    audiobook = AudioBook("1984", "Orwell", "Dystopian", "MP3")
    print(audiobook)  # Output: AudioBook: 1984 by Orwell, Genre: Dystopian, Format: MP3
    audiobook.play_audio()  # Output: Playing audio version of 1984

    # Test polymorphism
    demonstrate_polymorphism()

    # Test isinstance
    check_isinstance()
