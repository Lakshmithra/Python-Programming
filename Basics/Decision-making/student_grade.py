marks = int (input("Enter your marks: "))
if (marks >= 90):
    print("Grade: A")
elif ((marks <= 89) and (marks >= 75)):
    print("Grade: B")
elif ((marks <= 74) and (marks >= 60)):
    print("Grade: C")
elif ((marks >= 0) and (marks < 60)):
    print("Grade: D")
else:
    print("Invalid marks!")

