class Book:
    """Represents a book with a title, author, and check-out status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """Represents a collection of books and operations to manage them."""

    def __init__(self):
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds the book by title and checks it out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out '{title}'")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Finds the book by title and returns it."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned '{title}'")
                return
        print(f"Book '{title}' was not checked out or not found.")

    def list_available_books(self):
        """Prints all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No available books.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")

