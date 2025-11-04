# Program to find the maximum element in a list

def maxoflist(s):
    m = s[0]
    for i in s:
        if i > m:
            m = i
    return m
  
n = str(input("Enter the elements of list : ")).split()
n = [int(x) for x in n]
maxi = maxoflist(n)
print(f"Maximum element in the list : {maxi}")
