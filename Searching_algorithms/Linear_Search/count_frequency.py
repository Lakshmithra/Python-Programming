def linear_search_count(arr , value):
    count = 0
    for i in arr:
        if i == value:
            count += 1
    return count
  
lst = [2,3,2,5,2,7]
target = 2
n = linear_search_count(lst , target)
print("Count : ",n)
