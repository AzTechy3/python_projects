# TomeRater is an application that allows users to read and rate books.
# The purpose of this capstone project is to practice implementing and testing classes in Python
# Below are specifications for methods for 5 different classes that interact with each other.
# These methods test knowledge of lists, loops, dictionaries, strings, control flow, and basic Python syntax
# Class 1 = User
# Class 2 = Book
# Class 3 = Non-Fiction
# Class 4 = Fiction
# Class 5 = TomeRater

# Create a User
# User class - Pages 1 & 2 from PDF instructions
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_address):
        self.email = new_address
        return "Email changed to {email}".format(email=new_address)

    def __repr__(self):
        return "User Name: {name}, email: {email}, books read: {books}".format(name=self.name,email=self.email,books=len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    # Give Books and Users Methods
    # Pages 5 & 6 from PDF instructions
    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        return sum([rating for rating in self.books.values() if rating is not None]) / len(self.books)

# Create a Book
# Book class - Page 3 from PDF instructions
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "This books ISBN has been updated to: {isbn}".format(isbn=new_isbn)

    def add_rating(self, rating):
        try:
            if 0 <= rating <= 4:
                self.ratings.append(rating)
            else:
                return "Invalid Rating"
        except TypeError:
            "Invalid Type"

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    # Give Books and Users Methods
    # Pages 5 & 6 from PDF instructions
    def get_average_rating(self):
        return sum([rating for rating in self.ratings]) / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

# Make a Fiction Subclass of Book
# Fiction class - Page 4 from PDF instructions
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title,author=self.author)

# Make a Non-Fiction Subclass of Book
# Non-Fiction class - Page 4 & 5 from PDF instructions
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manuel on {subject}".format(title=self.title,level=self.level,subject=self.subject)

# Create TomeRater
# TomeRater class - Pages 7 & 8 from PDF instructions
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, "No user with email {email}!".format(email=email))
        if user:
            user.read_book(book, rating)
            book.add_rating(rating)
            self.books[book] = self.books.get(book,0) + 1

    def add_user(self, name, email, user_books=None):
        if email not in self.users:
            self.users[email] = User(name, email)
            if user_books is not None:
                for book in user_books:
                    self.add_book_to_user(book, email)
        else:
            print("An account with this email already exists!")

    # Create Some Analysis Methods for TomeRater
    # Pages 8 & 9 from PDF instructions
    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        return max(self.books, key=self.books.get)

    def highest_rated_book(self):
        highest_rated = max(rating.get_average_rating() for rating in self.books.keys())
        return str([book for book in self.books.keys() if book.get_average_rating() == highest_rated]).strip('[]')

    def most_positive_user(self):
        most_positive = max(rating.get_average_rating() for rating in self.users.values())
        return str([user for user in self.users.values() if user.get_average_rating() == most_positive]).strip('[]')
