def binary_search(arr , target):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return result

lst = [1,2,2,2,3,4]
value = 2
r = binary_search(lst , value)
if r != -1:
    print(f"First occurence of {value} is at index {r}")
else:
    print("Search element not found")
