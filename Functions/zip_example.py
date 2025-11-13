# zip() combines elements from multiple lists into tuples.
# It stops when the shortest list is exhausted.

lst1 = [x for x in range(0,11,2)]
lst2 = [y for y in range(1,10,2)]

z = zip(lst1,lst2)

for i in z:
    print(i)    # print each pair (index-wise combined values)

a = [1,2,3]
b = [4,5,6,7,8]
c = [9,10,12]

# zip stops at the shortest list (here length 3)

for i in zip(a,b,c):
    print(i)
