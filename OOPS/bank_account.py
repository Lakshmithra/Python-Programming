class Bank_Account:

    def __init__(self , owner , balance):
        self.owner = owner
        self.balance = balance

    def current_balance(self):
        print("Current balance : ",self.balance)

    def __str__(self):
        return f"Account owner : {self.owner}\nAccount balance : {self.balance}"
    
    def deposit(self,amount):
        self.balance += amount
        print("Amount deposited successfully")
        print("Current balance : ",self.balance)

    def withdraw(self,amount):

        if amount > self.balance:
            print("Insufficient bank balance")
        else:
            self.balance -= amount
            print("Amount withdrawed succesfully")
        print("Current balance : ",self.balance)
        


a = Bank_Account("Laksh",500)
print(a)
a.deposit(300)
a.withdraw(1000)

