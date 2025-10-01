# Program to calculate total, average, and grade of a student

total = 0
avg = 0
s1 = int(input("Enter mark in first subject: "))
s2 = int(input("Enter mark in second subject: "))
s3 = int(input("Enter mark in third subject: "))
s4 = int(input("Enter mark in fourth subject: "))
s5 = int(input("Enter mark in fifth subject: "))
total = s1 + s2 + s3 + s4 + s5
avg = total / 5
print("Total marks : ", total)
print("Average marks : ",avg)
if (avg >= 90):
    print("Grade: A")
elif((avg >= 75) and (avg <= 89)):
    print("Grade B")
elif((avg >= 60) and (avg <= 74)):
    print("Grade C")
else:
    print("Grade D")

