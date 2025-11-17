# The map() function applies a given function to every item in an iterable (like a list, tuple, etc.) and returns a map object.
# Syntax: map(function, iterable)
# You can loop through the map object or convert it to a list to see the results.

def square(num):
    return num**2
n = [1,2,3,4,5]

# map(square, n) applies the square() function to each value in the list n.

print(map(square,n))     # This prints a map object (location) , not the actual squared values.

# Looping through the map object to print each squared value

for i in map(square,n):
    print(i)

# Converting the map object into a list to see all squared results at once

print(list(map(square,n)))
