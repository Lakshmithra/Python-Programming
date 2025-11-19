def binary_search(arr , value):
    low = 0
    high = len(arr) - 1    
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == value:
            return True
        elif arr[mid] > value:
            high = mid - 1
        else:
            low = mid + 1         
    return False
  
lst = [5,10,15,20,25,30]
target = 18
b = binary_search(lst , target)
print(b)
