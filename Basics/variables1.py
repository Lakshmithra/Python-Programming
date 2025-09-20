"""
Python will ignore string literals that are not assigned to a variable,
you can add a multiline string (triple quotes) in your code, 
and place your comment inside it
"""

# In Python, variables are created when you assign a value to it . Python has no command for declaring a variable

x = 5

# Variables do not need to be declared with any particular type, and can even change type after they have been set

x = "Light"
print(x)

# Variables are case sensitive

X = "Moon"    
print(X)      

# If you want to specify the data type of a variable, this can be done with casting.

y = int(3)
print(y)      

# You can get the data type of a variable with the type() function.

print(type(x))
print(type(y))
