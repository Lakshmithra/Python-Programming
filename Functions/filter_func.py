# The filter() function filters items out of an iterable based on whether they satisfy a given condition (True/False).
# It returns a filter object containing only the items that passed the test.
# Syntax: filter(function, iterable)
# The function must return True or False.

def check_even(n):
    return n % 2 == 0
nums = [0,1,2,3,4,5,6,7,8,9,10]

# Using filter(check_even, nums) keeps only the numbers where check_even() returns True

print(filter(check_even , nums))     # This prints a filter object, not the actual values

# Loop through the filter object to print even numbers one by one

for i in filter(check_even , nums):
    print(i)

# Convert the filter object into a list to see all even numbers at once

print(list(filter(check_even , nums)))
