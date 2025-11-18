def linear_search(arr,string):
    for i in range(len(arr)):
        if arr[i] == string:
            return i
    else:
         return 0
        
lst = ['apple', 'banana', 'cherry', 'dates']
v = linear_search(lst,'cherry')

if v!= 0:
    print(f"Cherry is found at index {v}")
else:
    print("Cherry is not found")
