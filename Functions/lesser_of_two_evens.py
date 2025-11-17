def lesser_of_two_evens(a , b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    elif a % 2 == 1 or b % 2 == 1:
        return max(a,b)
m = lesser_of_two_evens(2,4)
n = lesser_of_two_evens(3,4)
print(m , n)
