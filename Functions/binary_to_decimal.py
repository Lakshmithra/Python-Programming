# Take last digit → multiply by 2^power → add to decimal → move left

def binary_to_decimal(n):
    decimal = 0
    power = 0
    while(n>0):
        r = n % 10
        n = n // 10
        decimal += r * pow(2 , power)
        power += 1
    print(decimal)
binary_to_decimal(1011)
