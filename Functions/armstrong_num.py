# Program to find whether a number is armstrong number or not

def cubesum(n):
    c = 0
    while(n!=0):
        r = n % 10
        n = n // 10
        c += pow(r , 3)
    return c
def isarmstrong(n):
    if n == cubesum(n):
        armstrong = True
    else:
        armstrong = False
    return armstrong
def printarmstrong(n):
    if isarmstrong(n):
        print(f"{n} is an armstrong number.")
    else:
        print(f"{n} is not an armstrong number.")
num = int(input("Enter a number : "))
printarmstrong(num)
