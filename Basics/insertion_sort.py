arr = [12, 7, 25, 9, 18, 3]
for i in range(1,len(arr)):
    j = i - 1
    key = arr[i]
    while j >=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print(arr)
