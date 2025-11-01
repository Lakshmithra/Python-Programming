#Program to demonstrate list comprehension
#Syntax :- [expression for item in iterable if condition]

squares = [x**2 for x in range(0,5,1)]
print("Squares : " ,squares)

even = [x for x in range(0,11,1) if x % 2 == 0]
print("Even    : " ,even)
