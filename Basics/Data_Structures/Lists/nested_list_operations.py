# Creating individual lists (rows)
lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = [7,8,9]


# Creating a matrix (list of lists)
matrix = [lst1 , lst2 , lst3]
print(matrix)
print(matrix[0])
print(matrix[0][0])


# Printing each row using a loop
for i in matrix:
    print(i)
print()    


# Printing each element using nested loops
for i in matrix:
    for j  in i:
        print(j , end = " ")
    print()
    
print("Length of matrix : " , len(matrix))
print("Length of list1 in matrix : ", len(matrix[0]))

print("Sum of list1 in matrix : ",sum(matrix[0]))

# Note: max(matrix) compares rows lexicographically
print("Max of list1 in matrix : ",max(matrix[0]))
print("Max of  matrix : ",max(matrix))

# Demonstrating shallow copy
copy_lst = matrix.copy()
copy_lst[0][0] = 99  # changes reflect in original matrix too
print(copy_lst)
print(matrix)
