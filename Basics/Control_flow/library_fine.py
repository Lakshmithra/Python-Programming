# Program to calculate library fine based on number of overdue days

fine = 0
days = int(input("Enter the number of days: "))
if ((days <= 5) and (days >= 1)):
    fine = fine + (2 * days)
elif((days <= 10) and (days >= 6)):
    fine = fine + (3 * days)
elif (days > 10):
    fine = fine + (5 * days)
print("Fine amount = ", fine)
