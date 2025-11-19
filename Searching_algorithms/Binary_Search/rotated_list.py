def binary_search_rotated(arr , value):
    low = 0
    high = len(arr) - 1
 
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == value:
            return mid
        elif arr[low] <= arr[mid]:
            if arr[low] <= value < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < value <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
  
lst = [15,20,25,5,10]
target = 5
b = binary_search_rotated(lst , target)
if b != -1:
    print(f"{target} is found at index {b}")
else:
    print("Search element not found")
