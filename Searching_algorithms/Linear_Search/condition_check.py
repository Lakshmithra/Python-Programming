def linear_search_cond(arr, value):
    l = []
    for i in arr:
        if i > value:
            l.append(i)
    return l
lst = [10,20,5,15,30]
target = 15
n = linear_search_cond(lst , target)
print(n)
