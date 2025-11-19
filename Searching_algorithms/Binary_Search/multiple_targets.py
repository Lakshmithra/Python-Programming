def binary_search(arr , target):
    indices = []
    for i in range(len(target)):
          low = 0
          high = len(arr) - 1
          found = -1
          while low <= high:
            mid = (low + high) // 2
        
            if arr[mid] == target[i]:
                found = mid
                break
            elif arr[mid] > target[i]:
                high = mid - 1
            else:
                low = mid + 1
          indices.append(found)
    return indices
            
lst = [5,10,15,20,25]
value = [10,25]
r = binary_search(lst , value)
print(f"{value} is found at indices {r}")
