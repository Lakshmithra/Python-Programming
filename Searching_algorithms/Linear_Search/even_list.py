def linear_search_even(arr):
    even = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
    return even

lst = [5,10,15,20,25,30]
e = linear_search_even(lst)
print("Even list : ",e)
