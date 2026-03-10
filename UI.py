import re #importing regular expression module
import hashlib #importing hashlib module for password hashing



#to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#password checker function
def is_srtong_password(password):
    if (len(password) < 8 or
        not re.search(r"[A-Z]", password) or
        not re.search(r"[a-z]", password) or
        not re.search(r"[0-9]", password) or
        not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return False
    return True,"password is strong"


#function to check post login menu
def post_login_menu():
    while True:
        print("Post Login Menu")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Viewing Profile...")
            log_activity("Viewed Profile")
        elif choice == '2':
            print("Editing Profile...")
            log_activity("Edited Profile")
        elif choice == '3':
            print("Logging out...")
            log_activity("Logged Out")
            break
        else:
            print("Invalid choice. Please try again.")

#define user log activities
def log_activity(activity):
    with open("activity_log.txt", "a") as log_file:
        log_file.write(f"{activity}\n")



#registration function
def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    is_valid, message = is_srtong_password(password)
    if not is_valid:
        print("Password is not strong enough. It must be at least 8 characters long and include uppercase letters, lowercase letters, digits, and special characters.")
        return
    #hash the password before storing
    hashed_password = hash_password(password)

    with open("users.txt", "a") as file:
        file.write(f"{username}: {hashed_password}\n") 
    print("Registration successful!")   

#login function
def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        stored_username, stored_password = user.strip().split(": ")
        if username == stored_username and hash_password == stored_password:
            print("Login successful!")
            return True 

    print("Invalid username or password.")
    return False

def main():
    while True:
        print("Welcome to the Application")
        print("1. Register")
        print("2. Login")           
        print("3. Exit")    
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':     
            login_user()
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")  

main()