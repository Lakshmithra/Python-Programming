# Program to demonstrate set comparison methods

a = {1,2,3}
b = {4,5,6}
c = {2,4,6}

# Checking if sets have no common elements (disjoint)

print(a.isdisjoint(b))   # True (no common elements)
print(a.isdisjoint(c))   # False (2 is common)

a = {1,2,3}
b = {1,2}

# issubset(): checks if all elements of one set are present in another

print(b.issubset(a)) # True if b ⊆ a
print(a.issubset(b)) # True if a ⊆ b

# issuperset(): checks if a set contains all elements of another

print(a.issuperset(b)) # True if a ⊇ b
print(b.issuperset(a)) # True if b ⊇ a



