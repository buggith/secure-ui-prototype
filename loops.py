names = ["alex", "nancy", "james", "violeta"]
for x in names:
    print(f"good morning, {x}")

# counter = 0
#while counter < 1:
    #print("hello")
   # counter += 1 
    #

num ={1,5,2,55,56,78,100}
for x in num:
    if x<10:
        print(f"small number {x}")
    else: 
        print("large number " + str(x))

while True:
    user = input("enter a letter or type Q to exit: ")
    if user.upper() == "Q":
        break
    print(f"you typed: {user}")