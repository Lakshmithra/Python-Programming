"""
A lambda function in Python is a small, anonymous function (a function without a name).
It is used when we need a simple function for a short period of time, usually inside
map(), filter(), sorted(), or similar functions.

SYNTAX:
    lambda arguments: expression

Explanation:
- 'lambda' is the keyword used to create the function.
- It can have any number of arguments (0 or more).
- It must contain only ONE expression.
- The value of that expression is automatically returned.
- No need to use 'return' or define a normal function.

Examples:
    lambda x: x + 10          → returns x + 10
    lambda a, b: a * b        → returns the product of a and b
    lambda n: n % 2 == 0      → returns True if n is even
"""

nums = [0,1,2,3,4,5,6,7,8,9,10]

s = list(map(lambda n: n ** 2 , nums))
print(s)
t = list(filter(lambda n:n % 2 == 0 , nums))
print(t)
