def linear_search(arr,value):
    isfound = False
    for i in range(len(arr)):
        if arr[i] == value:
            isfound = True
            break
    if isfound:
        print (f"{value} is found at index {i}")
    else:
        print("Search element not found")
        
lst = [15,8,25,30,10]
linear_search(lst,25)
