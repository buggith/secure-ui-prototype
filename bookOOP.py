class user:
    def __init__(self, username, password): #constructor
        self.username = username
        self.__password = password # private attribute __password

    def login(self):
        print(f"Welcome, {self.username}")
admin = user("BABU", "admin123") #  create object
admin.login()


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")
    def return_book(self):
        self.is_available = True
        print(f"You have returned '{self.title}'.")

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")


# Example usage
book1 = Book("1984", "George Orwell", 1949) 
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book1.display_info()
book1.borrow_book() 
book1.borrow_book()
book1.return_book()
