# Program to find the twinprimes till 1000

def twinprimes():
    primes = []
    for i in range(2 , 1000+1):
        count = 0
        s = int(pow(i , 0.5))
        for j in range(2 , s+1):
            if i % j == 0:
                count = 1
        if count == 0:
            primes.append(i)
    i = 0
    j = 1
    while(j < len(primes)):
        diff = primes[j] - primes[i]
        if diff == 2:
            print(f"({primes[i]} , {primes[j]})")
        i += 1
        j += 1
twinprimes()
