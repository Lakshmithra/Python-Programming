# Program to calculate ticket price based on age and class type

p_age = int(input("Enter your age: "))
c_type = str(input("Enter your class type (economy/business): "))
eprice = 500
bprice = 800
if(p_age < 12):
    if(c_type == "economy"):
        eprice = eprice * 0.5
        print("Price: ",eprice)
    elif (c_type == "business"):
        bprice = bprice * 0.5
        print("Price: ",bprice)
elif (p_age > 60):
    if (c_type == "economy"):
        eprice = eprice * 0.7
        print("Price: ",eprice)
    elif (c_type == "business"):
        bprice = bprice * 0.7
        print("Price: ",bprice)
else:
    if (c_type == "economy"):
        print("Price: ",eprice)
    elif (c_type == "business"):
        print("Price: ",bprice)
