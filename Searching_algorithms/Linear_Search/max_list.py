def linear_search_max(arr):
    maxi = 0
    for i in arr:
        if i > maxi:
            maxi = i
    return maxi
  
lst = [15,8,25,30,10]
m = linear_search_max(lst)
print(f"Max in {lst} is {m}")
