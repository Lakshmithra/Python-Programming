# Program to check whether two numbers are amicable or not

def sumproperdivisor(n):
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total += i
    return total
def amicablenos(m , n):
    if sumproperdivisor(m) == n and sumproperdivisor(n) == m:
        print(f"{m} and {n} are amicable numbers")
    else:
        print(f"{m} and {n} are not amicable numbers")
    
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
amicablenos(n1 , n2)
