"""
Write a Library class with no_of_books and books
as two instance variables.
Write a program to create a library from this library
and show how you can print all books, add a book
and get the number of books using different methods.
Show that your program doesn't persist the books
after the program is stopped!
"""

class Library:
    def __init__(self, book, number):
        self.book =book
        self.number = number