# Program to check whether a number is prime or not

def checkprime(num):
    count = 0
    e = int(pow(num , 0.5))
    for i in range(2 , e+1):
        if num % i == 0:
            print(f"{num} is not prime")
            count = count + 1
            break
    if count == 0:
        print(f"{num} is prime")
        
n = int(input("Enter the number : "))
if n == 1:
    print("1 is not prime")
elif n == 2:
    print("2 is prime")
else:
    checkprime(n)
