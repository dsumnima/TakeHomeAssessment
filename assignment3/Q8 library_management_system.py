'''
Program: Basic Library Management System using OOP and file handling
'''

import json

class Library:
    def __init__(self, filename="library.txt"):
        self.filename = filename

    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except:
            return {}

    def save_books(self, books):
        with open(self.filename, "w") as file:
            json.dump(books, file)

    def add_book(self, title):
        books = self.load_books()
        books[title] = "available"
        self.save_books(books)
        print("Book added!")

    def borrow_book(self, title):
        books = self.load_books()
        if books.get(title) == "available":
            books[title] = "borrowed"
            print("Book borrowed!")
        else:
            print("Book not available!")
        self.save_books(books)

    def return_book(self, title):
        books = self.load_books()
        if title in books:
            books[title] = "available"
            print("Book returned!")
        self.save_books(books)

    def search_book(self, title):
        books = self.load_books()
        if title in books:
            print(f"{title} is {books[title]}")
        else:
            print("Book not found!")

# Run system
lib = Library()

while True:
    print("\n1.Add 2.Borrow 3.Return 4.Search 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        lib.add_book(input("Enter book title: "))
    elif choice == "2":
        lib.borrow_book(input("Enter book title: "))
    elif choice == "3":
        lib.return_book(input("Enter book title: "))
    elif choice == "4":
        lib.search_book(input("Enter book title: "))
    else:
        break
