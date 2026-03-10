password = "abc123"
masked_password = "+" * len(password)
print(masked_password)

name = "Cyber"
char = name[1]
print(char)

text="newsoftware.exe"
if(text.endswith(".exe")):
    print("Malware file")

filename = "admin.com"
if filename[-4:] == ".com":
    print("Valid user")


user = "google@gmail.com"
if user.find("@") != -1:
    print("IS A USER")

url = "https://www.coursera.org/learn/packt-mastering-cybersecurity-with-python-from-basics-to-advanced-defense-rjc5p/file"
newUrl = url.split("/")[-4:]
print(newUrl)


