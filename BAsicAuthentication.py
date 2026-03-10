user_credentials = {} # Dictionary to store user credentials

def register_user():
   # Loop until a unique username is provided check if already username exists
    username = input("enter username: ")
    if username in user_credentials:
            print("Username already exists. Please choose a different username.")
    else: 
        password = input("enter password: ")
        user_credentials[username] = password #create key value pair dictionary
        print("User registered successfully.")
#funtion to login user
def login_user():
    username = input("enter your username: ")
    password = input("enter password: ")
    if username in user_credentials and user_credentials[username] == password:
        print("Welcome Back! ")
    else:
        print("Invalid username or password.Try again.")

#main menu
def authentication_system():
    while True:
        print("Welcome to the Basic Authentication System")
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choices = input("Enter your choice (1-3): ")
        if choices == '1':
            register_user()
        elif choices == '2':
            login_user()
        elif choices == '3':
            print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

authentication_system()