# Program to demonstrate basic set operations

x = set()
x.add(1)
x.add(2)
print(x)

# Adding multiple elements using update()
# (duplicates are ignored automatically)

x.update([4,4,5,6])
print(x)

x.remove(4)
print(x)

# Converting a list to a set (to remove duplicates)

lst = [1,1,1,3,3,3,2,2,2]
print(set(lst))
