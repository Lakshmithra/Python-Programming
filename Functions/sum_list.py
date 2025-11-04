# Program to find the sum of all elements in a list

def sumoflist(lst):
    s = 0
    for i in lst:
        s = s + i
    return s
  
n = input("Enter the elements : ").split()
n = [int(x) for x in n]

sl = sumoflist(n)
print(f"Sum of elements of list : {sl}")
