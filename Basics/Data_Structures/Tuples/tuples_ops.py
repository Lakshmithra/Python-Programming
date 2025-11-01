# Program to demonstrate tuple operations

my_tuple = (1,2,3,4,5)

print(my_tuple)
print("Length of tuple : ",len(my_tuple))

print(my_tuple[1:])
print(my_tuple[-1])

# Demonstrating tuple methods

t = (1,1,2,3,4)

print("Count : ",t.count(1)) # Counts occurrences of 1
print("Index : ",t.index(1)) # Returns first index of 1

# Tuple unpacking (assigning each element to a variable)

student = ('Lakshmithra' , 26 , 'PSG')
name , age , college = student

print("Name : ",name)
print("Age  : ",age)
print("College : ",college)
