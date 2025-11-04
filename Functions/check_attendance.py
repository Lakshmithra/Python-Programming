# Program to check whether a student is present or absent

def checkattendance(r):
    present = [14,18,28,32]
    for i in present:
        if i == r:
            return True
          
n = int(input("Enter the roll no : "))
a = checkattendance(n)

if a:
    print(f"{n} is present")
else :
    print(f"{n} is absent")
    
