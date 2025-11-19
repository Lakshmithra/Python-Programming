def binary_search_recursive(arr ,low , high , value):
    if low > high:
        return -1
      
    mid = (low + high) // 2
  
    if arr[mid] == value:
        return mid
    elif arr[mid] > value:
        return binary_search_recursive(arr, low , mid - 1 , value)
    else:
        return binary_search_recursive(arr ,mid + 1 , high, value)
    
lst = [3,8,11,15,18,20]
target = 11
b = binary_search_recursive(lst ,0 , len(lst)-1 , target)

if(b != -1):
    print(f"{target} is found at index {b}")
else:
    print("Search element not found")
