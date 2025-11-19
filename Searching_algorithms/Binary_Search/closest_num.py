def binary_search(arr , target):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    candidates = []
    if high >= 0:
        candidates.append(arr[high])
    if low < len(arr):
        candidates.append(arr[low])
    return min(candidates , key=lambda x : abs(x - target))

lst = [10,20,30,40,50]
value = 35
r = binary_search(lst , value)
print(f"Number closest to {value} is {r}")
