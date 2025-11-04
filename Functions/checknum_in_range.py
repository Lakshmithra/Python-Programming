# Program to check whether a number falls in a given range 

def checknum(sr , er , n):
    for i in range(sr , er+1):
        if i == n:
            print(f"{n} falls in the given range")
            break
        if i == er:
            print(f"{n} does not fall in the given range")

num = int(input("Enter the number : "))
s = int(input("Enter the start range : "))
e = int(input("Enter the end range : "))
checknum(s , e , num)
