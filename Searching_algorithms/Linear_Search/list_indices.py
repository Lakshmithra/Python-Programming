def linear_search_indices(arr , target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

lst = [1,3,1,4,1]
target = 1
o = linear_search_indices(lst , target)
print(f"{target} is found at indices {o}")
