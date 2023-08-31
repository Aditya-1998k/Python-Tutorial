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
    def __init__(self):
        self.book =[]
        self.number = 0

    def addBook(self, book):
        self.book.append(book)
        self.number = len(self.book)

    def showDetails(self):
        print(f"The number of books are {self.number}")
        for index, b in enumerate(self.book):
            print(f"{index+1}. {b}")


book1=Library()
book1.addBook("Harry Potter")
book1.addBook("The Alchemist")
book1.addBook("You can Win")
book1.addBook("Godan")
book1.addBook("Gaban")

book1.showDetails()

"""
The number of books are 5
1. Harry Potter
2. The Alchemist
3. You can Win
4. Godan
5. Gaban
"""