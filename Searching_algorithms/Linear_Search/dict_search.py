def linear_search_dict(arr , value):
    for i in arr:
        if i == value:
            return i
            
lst = [{'id':1},{'id':2}]
target = {'id':2}
n = linear_search_dict(lst , target)
print(n)
