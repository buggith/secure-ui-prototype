username = input("enter your username:      ")
password = input("enter your password:      ")      
with open("credentials.txt", "a") as file: # Open the file in append mode
    file.write(f"{username}, {password}\n")  # Append the username and password to the file
print("Credentials saved successfully.")
with open("credentials.txt", "r") as file: # Open the file in read mode
    content = file.read() # Read the entire content of the file
    print("Current contents of credentials.txt:")
    print(content) # Print the content to the console

with open("credentials.txt", "r") as file: # Open the file in read mode
    lines = file.readlines() # Read all lines into a list
    print("List of credentials:")
    for line in lines:
        print(line.strip()) # Print each line, removing any extra whitespace

with open("credentials.txt", "r") as file: # Open the file in read mode
    lines = file.readlines() # Read all lines into a list
    print("Usernames only:")
    for line in lines:
        username = line.split(",")[0] # Split each line by comma and get the username part
        print(username.strip()) # Print the username, removing any extra whitespace