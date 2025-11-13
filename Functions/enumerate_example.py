# Program to demonstrate built in function enumerate()
# enumerate() adds a counter (index) to each item in a list or sequence.
# It returns pairs of (index, value).

lst = [x for x in range(0,12,2)]

for i in enumerate(lst):
    print(i)                    # returns tuple pairs with index values
  
for x , y in enumerate(lst):
    print(x , end = ' ')
    print(y)

