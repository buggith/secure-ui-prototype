class user:
    def __init__(self, username, password): #constructor
        self.username = username
        self.__password = password # private attribute __password

    def authenticate(self, password):
        if self.__password == password:
            print(f"Welcome, {self.username}")
        else:
            print("Invalid password. Access denied.")

user = user("BABU", "123") #  create object
print(user.authenticate ("123")) # Correct password
print(user.authenticate ("wrongpassword")) # Incorrect password