# Program to find the sum of proper divisors of a number

def sumproperdivisor(n):
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total += i
    return total
  
num = int(input("Enter a number : "))
s = sumproperdivisor(num)
print("Sum : ",s)
