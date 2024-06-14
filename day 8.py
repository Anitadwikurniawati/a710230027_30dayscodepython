class Book:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.is_available = True

class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.id] = book

    def register_member(self, member):
        self.members[member.id] = member

    def lend_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)
        if book and member and book.is_available:
            book.is_available = False
            member.borrowed_books.append(book)
            print(f"{member.name} borrowed '{book.title}'")
        else:
            print("Book is not available or Member not found")

    def return_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)
        if book and member and book in member.borrowed_books:
            book.is_available = True
            member.borrowed_books.remove(book)
            print(f"{member.name} returned '{book.title}'")
        else:
            print("Book or Member not found or Book was not borrowed by Member")

library = Library()

library.add_book(Book("B001", "1999"))
library.add_book(Book("B002", "Love her is sick"))

library.register_member(Member("M001", "Tata"))
library.register_member(Member("M002", "Azzam"))

library.lend_book("B001", "M001")

library.return_book("B001", "M001")
