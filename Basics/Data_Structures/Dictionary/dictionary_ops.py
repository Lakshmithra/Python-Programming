# Program to demonstrate dictionary operations

my_dict = {'k1' : 818 , 'k2' : ['G', 'R' , 'L'] , 'k3' : {'G' : 8 , 'R' : 18 , 'L' : 26}}
print(my_dict)

# Accessing a value using .get()
print(my_dict.get('k1'))

# Accessing an element from a list inside the dictionary and converting to lowercase
print(my_dict['k2'][1].lower())

# Accessing a value from a nested dictionary
print(my_dict['k3']['L'])

# Displaying all keys, values, and key-value pairs
print("Keys : ",my_dict.keys())
print("Values : ",my_dict.values())
print("Pairs : ",my_dict.items())

# Creating an empty dictionary and adding key-value pairs
d = {}
d[1] = 100
d[2] = 55
print(d)

# Modifying values using arithmetic operations
d[1] -= 50
d[2] += 50
print(d)

# Creating a nested dictionary and accessing deeply nested keys
nd = {'k' : {'k1' :{'k2' : 0}}}
print(nd['k']['k1']['k2'])



