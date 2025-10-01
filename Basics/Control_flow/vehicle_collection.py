# Program to calculate toll collection based on vehicle type

collection = 0
for i in range (1 , 11):
    vehicle = str(input("Enter the type of vehicle (car / bike) : "))
    if (vehicle == "car"):
        collection = collection + 50
    elif (vehicle == "bike"):
        collection = collection + 30
    else:
        print("INVALID! Enter a valid vehicle !")
print("The collection : ", collection)
