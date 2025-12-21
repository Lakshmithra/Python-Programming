lst = [12, 7, 25, 9, 18, 3]
for i in range(len(lst)):
    for j in range(len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print(lst)
