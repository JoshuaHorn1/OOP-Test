# Imports...
import random

# Lists...
user_list = []
book_list = []


# Classes...
class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title  # string
        self.author = author  # string
        self.dewey = dewey  # string
        self.isbn = isbn  # string
        self.available = True
        self.borrower = None
        book_list.append(self)  # Holds book objects created - main routine

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print("######################")
        print()


class User:
    def __init__(self, name, address):
        self.name = name  # string
        self.address = address  # string
        self.fees = 0.0  # float
        self.code = random.randint(111111, 999999)
        self.borrowed_books = []
        user_list.append(self)

    def user_details(self):
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Fees: $", self.fees)
        print("User Code: ", self.code)
        print("####################")
        print()


# Functions...
def print_info():
    for book in book_list:
        book.book_details()


def print_user():
    for user in user_list:
        user.user_details()


def add_user():
    name = input("Enter the new user's name: ").title()
    address = input("Enter the new user's address: ")
    User(name, address)
    print(name, address, "has been added to the user list.")


def add_book():
    title = input("Enter the new book's title: ").title()
    author = input("Enter the new book's Author: ").title()
    dewey = input("Enter the new book's dewey code: ").upper()
    isbn = input("Enter the new book's ISBN: ")
    Book(title, author, dewey, isbn)
    print(f"{title} has been added to the book list.")


def find_user():
    user_to_find = input("Enter the name of the user: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi {user_to_find}")
            return user
        print(f"Sorry, there is no user with that name.")
        return None


def find_book():
    book_to_find = input("Enter the name of the book: ").title()
    for book in book_list:
        if book.title == book_to_find:
            print(f"The book '{book_to_find}' is in the catalogue.")
            return book
        print("Sorry, there was no book with that name in the catalogue.")
        return None


def lend_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if book.available:
            confirm = input("Type 'Y' if you want to borrow this book: ").upper()
            if confirm == "Y":
                print(f"{book.title} is now on loan to {user.name}.")
                book.available = False
                book.borrower = user.name
                user.borrowed_books.append(book.title)
            else:
                print(f"Sorry, '{book.title}' is already on loan.")


def return_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if book.title in user.borrowed_books:
            confirm = input("Type 'Y' if you want to borrow this book: ").upper()
            if confirm == "Y":
                print(f"{book.title} has been returned to the library.")
                book.available = True
                book.borrower = user.name
                user.borrowed_books.remove(book.title)
            else:
                print(f"Sorry, '{book.title}' is on loan to someone else.")


# Main Routine...
# Create objects - Books
Book("Lord of the Rings", "J.R.R Tolkien", "TOL", 94365748937563)
Book("The Hunger Games", "Suzanne Collins", "COL", 49853457495466)
Book("A Tale Of Two Cities", "Charles Dickens", "DIC", 943854895789454)
Book("Harry Potter", "J.K.Rowling", "ROW", 9774584385687455)

# Create objects - Users
User("John", "12 Example St")
User("Susan", "1011 Binary Rd")
User("Paul", "25 Appletree Dr")
User("Mary", "8 Moon Cres")

# User menu
new_action = True
while new_action:
    print()
    print(f"1. Lend a book")
    print(f"2. Return a book")
    print(f"3. Add a user")
    print(f"4. Add a book")
    print(f"5. Exit")
    print()
    choice = input("What would you like to do? Enter a number (1-5): ")
    if choice == "1":
        lend_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        add_user()
    elif choice == "4":
        add_book()
    elif choice == "5":
        print("\n*** That is not a valid choice ***")

find_book()
# find_user()
# add_book()
# print_info()
# add_user()
# print_user()