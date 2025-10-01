# Simple ATM simulation program with check balance, withdraw, and deposit options

balance = 10000
originalpin = 1234
pin = int(input("Enter the pin number: "))
if (pin == originalpin):
    while(1):
        print("\n1.Check balance\n2.Withdraw\n3.Deposit\n4.Exit\n")
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            print("Balance = ",balance)
        if (choice == 2):
            withdraw = int(input("Enter the amount to be withdrawn: "))
            balance = balance - withdraw
        if (choice == 3):
            deposit = int(input("Enter the amount to be deposited: "))
            balance = balance + deposit
        if (choice == 4):
            print("Program terminated....")
            break
else:
    print("Your pin number is incorrect! Try again ")
