# Program to calculate total bill for purchased items with discount if total > 5000

total = 0
n = int(input("Enter the number of items purchased: "))
for i in range (1 , n+1):
    price = int(input(f"\nEnter the price of the item {i}: "))
    quantity = int(input(f"Enter the quantity of the item {i}: "))
    total = total + (price * quantity)
if (total > 5000):
    total = total * 0.9
    print("\nTotal bill = ", total)
else:
    print("\nTotal bill = ", total)
