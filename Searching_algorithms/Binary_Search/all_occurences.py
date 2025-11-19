def find_all_positions(arr , value):
    def first_occurence(arr ,value):
            low = 0
            high = len(arr) - 1
            first = -1
            while low <= high:
                mid = (high + low) // 2
                if arr[mid] == value:
                    first = mid
                    high = mid - 1
                elif arr[mid] > value:
                    high = mid - 1
                else:
                    low = mid + 1
            return first
    
    def last_occurence(arr ,value):
            low = 0
            high = len(arr) - 1
            last = -1
            while low <= high:
                mid = (high + low) // 2
                if arr[mid] == value:
                    last = mid
                    low = mid + 1
                elif arr[mid] > value:
                    high = mid - 1
                else:
                    low = mid + 1
            return last
    f = first_occurence(arr , value)
    l = last_occurence(arr , value)
    if f == -1:
        return []
    else:
        return list(range(f , l+1))
    

lst = [1,2,2,2,3]
target = 2
indices = find_all_positions(lst , target)
print(f"All positions of {target} : {indices}")
