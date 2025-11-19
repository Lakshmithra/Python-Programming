def binary_search_2D(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = cols - 1
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return (row,col)
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return -1
lst = [[1,2,3],[4,5,6],[7,8,9]]
target = 5
r = binary_search_2D(lst , target)
if r != -1:
    print(f"{target} is found at index {r}")
else:
    print("Search element not found")
