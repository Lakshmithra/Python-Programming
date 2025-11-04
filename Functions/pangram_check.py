# Program to check whether a string is pangram or not

def pangramstr(string):
    unique = ''
    for i in string:
        if i not in unique and i in alphabets :
            unique += i
    length = len(unique)
    if length == 26:
        print(f"{string} is a pangram")
    else:
        print (f"{string} is not a pangram")
      
s = str(input("Enter the string : "))

alphabets = "abcdefghijklmnopqrstuvwxyz"
s = s.lower()

pangramstr(s)
