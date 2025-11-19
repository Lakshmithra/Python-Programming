def binary_search(arr , value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid - 1
        else:
            low = mid + 1         
    return -1
  
lst = [5,10,15,20,25,30]
target = 15

b = binary_search(lst , target)

if(b != -1):
    print(f"{target} is found at index {b}")
else:
    print("Search element not found")
