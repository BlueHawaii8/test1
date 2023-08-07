class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed_by = None

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}"

class Patron:
    def __init__(self, name):
        self.name = name
        self.books_borrowed = []

    def borrow_book(self, book):
        if book.borrowed_by is None:
            book.borrowed_by = self
            self.books_borrowed.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed by {book.borrowed_by.name}")

    def return_book(self, book):
        if book in self.books_borrowed:
            book.borrowed_by = None
            self.books_borrowed.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}'")

# Sample usage
if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
    patron1 = Patron("Alice")
    patron2 = Patron("Bob")

    patron1.borrow_book(book1)
    patron2.borrow_book(book1)
    patron2.borrow_book(book2)

    patron1.return_book(book1)
    patron2.return_book(book2)
