with open("example.txt", "w") as file: # Open a file in write mode
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("Goodbye!\n")
with open("example.txt", "r") as file: # Open the file in read mode
    content = file.read() # Read the entire content of the file
    print(content) # Print the content to the console

#with statement automatically handles closing the file after its suite finishes, even if an exception is raised.
