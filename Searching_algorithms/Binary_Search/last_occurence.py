def binary_search(arr , target):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return result

lst = [2,3,3,3,4,5]
value = 3
r = binary_search(lst , value)
if r != -1:
    print(f"Last occurence of {value} is at index {r}")
else:
    print("Search element not found")
