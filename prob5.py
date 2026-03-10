
def count(uppercase, lowercase, numbers, spl_char):
    uppercase = 0
    lowercase = 0
    numbers = 0
    spl_char = 0
    S= input("enter a string: ")
    for i in S:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
        elif i.isdigit():
            numbers += 1
        else:
            spl_char += 1
    return count(uppercase, lowercase, numbers, spl_char)

     