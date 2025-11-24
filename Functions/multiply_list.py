def multiply_list(lst):
    mul = 1
    for i in lst:
        mul *= i
    return mul
  
lst = [1,2,3,-4]
m = multiply_list(lst)
print(m)
