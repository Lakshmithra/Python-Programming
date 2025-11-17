# *args allows a function to accept any number of positional arguments.
# These arguments are collected into a tuple, which means you can iterate,
# add, compare, or perform any operation on them.

def args_func(*args):
    return sum(args)
s = args_func(8,18,26)
print(s)

# You can use any name instead of *args (like *eee below),
# but *args is the standard convention. It still collects values into a tuple.

def my_args_func(*eee):
    return max(eee)
m = my_args_func(8,18,26,52)
print(m)

# **kwargs allows a function to accept any number of keyword arguments.
# These arguments are collected into a dictionary, so you can check for keys
# like 'fruit', 'color', etc., or access their values.

def kwargs_func(**kwargs):
    if 'fruit' in kwargs:
        print("I like fruits")
    else:
        print("I don't like fruits")

kwargs_func(fruit = 'watermelon')   # contains 'fruit' → prints "I like fruits"
kwargs_func(vegetable = 'carrot')   # no 'fruit' → prints "I don't like fruits"
