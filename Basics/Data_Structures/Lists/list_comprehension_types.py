"""
Program to demonstrate different types of list comprehension

List Comprehension Syntax:
--------------------------
Basic:
[expression for item in iterable]


With condition:
[expression for item in iterable if condition]


With if-else (ternary expression):
[expression_if_true if condition else expression_if_false for item in iterable]


Nested loops:
[expression for item1 in iterable1 for item2 in iterable2]

"""

# 1. Basic list comprehension

lst1 = [x for x in range(1,11,1)]
print(lst1)

# 2. List comprehension with condition
lst2 = [x for x in range(1,11,1) if x % 2 == 0]
print(lst2)

# 3. List comprehension with if-else inside
lst3 = ['EVEN' if x % 2 == 0 else 'ODD' for x in range(1,11,1)]
print(lst3)

# 4. Nested list comprehension (multiplying values)
lst4 = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(lst4)

