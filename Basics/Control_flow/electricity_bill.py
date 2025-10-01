# Program to calculate electricity bill based on units consumed

bill = 0
units = int(input("Enter the number of units consumed: "))
if (units <= 100):
    bill = bill + (units * 5)
elif ((units >= 101) and (units <= 300)):
    bill = bill + (units * 7)
elif (units > 300):
    bill = bill + (units * 10)
else:
    print("INVALID !")
print("Bill amount = ", bill)
