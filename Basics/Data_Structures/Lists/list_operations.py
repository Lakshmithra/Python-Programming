# Creating a list with different data types
mylist = [26, 0, 8.18, 18]

# Printing the original list
print("My list:", mylist)

# Printing elements from index 1 to the end
print("Slicing:", mylist[1:])

# Printing the length of the list
print("Length of the list:", len(mylist))

# Changing the third element (index 2)
mylist[2] = 18
print("Modified List:", mylist)

# Removing the last element
mylist.pop()
print("Popped List:", mylist)

# Adding a new element to the end
mylist.append(8)
print("Appended List:", mylist)

# Removing the element at index 1
mylist.pop(1)
print("Popped List (index):", mylist)

# Sorting the list in ascending order
mylist.sort()
print("Sorted List:", mylist)

# Reversing the list
mylist.reverse()
print("Reversed List:", mylist)

