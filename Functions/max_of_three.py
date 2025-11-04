#Program to find the maximum of three numbers

def maxofthree(a , b , c):
    if a > b and a > c:
        m = a
    elif b > a and b > c:
        m = b
    else:
        m = c
    return m
  
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))

maximum = maxofthree(n1 , n2 , n3)
print(f"Maximum of {n1} ,{n2} and {n3} : {maximum}")
