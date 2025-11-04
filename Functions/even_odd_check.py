# Program to check whether a number is even or odd

def checkevenodd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
      
n = int(input("Enter the number : "))
checkevenodd(n)
