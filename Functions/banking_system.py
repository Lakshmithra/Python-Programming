from datetime import datetime

def create_account():
    import random
    account_no  = str(random.randint(1000,9999))
    while account_no in accounts:
        account_no  = str(random.randint(1000,9999))
    name = input("Enter your name: ")
    balance = 0
    transaction = []
    accounts[account_no] = {'name' : name , 'balance' : balance ,
                            'transactions' : transaction}
    print(f"Account created successfully ! Your account number is {account_no}")

def deposit_amount():
    current_transaction = {}
    no = input("Enter account number : ")
    if no in accounts:
        amount = int(input("Enter the amount : "))
        accounts[no]['balance'] += amount
        date = date_time()
        current_transaction = {'date': date , 'type' : 'Deposit',
                               'amount' : amount , 'balance' :accounts[no]['balance']}
        accounts[no]['transactions'].append(current_transaction)
        print(f"\nAmount deposited successfully !")
    else:
        print(f"Account {no} doesn't exist")

def withdraw_amount():
    no = input("Enter account number : ")
    if no in accounts:
        amount = int(input("Enter the amount : "))
        if accounts[no]['balance'] >= amount:
            accounts[no]['balance'] -= amount
            date = date_time()
            current_transaction = {'date': date , 'type' : 'Withdraw', 'amount' : amount
                                   , 'balance' :accounts[no]['balance']}
            accounts[no]['transactions'].append(current_transaction)
            print(f"\nAmount withdrawed successfully !")
        else:
            print("INSUFFICIENT BALANCE !")
    else:
        print(f"Account {no} doesn't exist")

def display_transactions():
    no = input("Enter account number : ")
    if no in accounts:
       print()
       print(f"{'Date':<15}{'Type':<10}{'Amount':<10}{'Balance':<10}")
       for i in accounts[no]['transactions']:
           print(f"{i['date']:<15}{ i['type']:<10}{i['amount']:<10}{i['balance']:<10}")
    else:
        print(f"Account {no} doesn't exist")

    
def date_time():
    now = datetime.now()
    current_time = now.strftime('%d-%m-%Y')
    return current_time
        
accounts = {}
while(1):
    print("\n1.Create account\n2.Deposit\n3.Withdraw\n4.Display history\n5.Exit\n")
    choice = int(input("Enter your choice (1/2/3/4/5): "))
    if choice == 1:
        create_account()
    elif choice == 2:
        deposit_amount()
    elif choice == 3:
        withdraw_amount()
    elif choice == 4:
        display_transactions()
    elif choice == 5:
        print("\n....Program terminated....")
        break
    else:
        print("Invalid choice")
