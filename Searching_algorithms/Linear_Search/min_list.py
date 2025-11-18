def linear_search_min(arr):
    mini = arr[0]
    for i in arr:
        if i < mini:
            mini = i
    return mini

lst = [20,15,30,10,25]
m = linear_search_min(lst)
print(f"Min in {lst} is {m}")
    
