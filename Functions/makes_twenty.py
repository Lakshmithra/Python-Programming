def makes_twenty(a,b):
    if a == 20 or b == 20 or (a+b==20):
        return True
    else:
        return False
l = makes_twenty(20,15)
m = makes_twenty(11,9)
n = makes_twenty(5,6)
print(l , m , n)
