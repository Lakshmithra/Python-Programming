def add_item(inventory):
    
    n = int(input("Enter number of items : "))
    for i in range(n):
        print(f"Enter details of item {i+1}")
        name = input("Name : ")
        quantity = int(input("Quantity : "))
        price = float(input("Price per unit : "))
        inventory[name] = [quantity , price]


def update_stock(inventory):

    n = input("Enter the name of the item to be updated : ")
    for i , j in inventory.items():
        found = False
        if n == i:
            c = input("Purchased / Sale ? : ").lower()
            if c == 'purchased':
                q = int(input("Enter the quantity : "))
                j[0] += q
            elif c == 'sale':
                q = int(input("Enter the quantity : "))
                if q > j[0]:
                    print("Not enough stock! Sale cannot be completed.")
                else:
                    j[0] -= q
            found = True
            break
    if not found:
        print("Item not found !")


def display_report(inventory):
  
    print('-' * 80)
    print(f"{'Name':<12}{'Quantity':<12}{'Price':<12}{'Total Value':<15}")
    print('-' * 80)
    for i , j in inventory.items():
         print(f"{i:<12}{j[0]:<12}{j[1]:<12}{j[0] * j[1]:<15}")
    print('-' * 80)
    print("\nLow-Stock items(quantity < 10)\n")
    low_stock = False
    for i , j in inventory.items():
        if j[0] < 10:
            print(f"- {i} : {j[0]}")
            low_stock = True
    if not low_stock:
        print("----None----\n")

inventory = {}
while(1):
    print("\n1.Add Item\n2.Update Stock\n3.Display Report\n4.Exit\n")
    choice = int(input("Enter your choice(1/2/3/4) : "))
    if choice == 1:
            add_item(inventory)
    elif choice == 2:
            update_stock(inventory)
    elif choice == 3:
            display_report(inventory)
    elif choice == 4:
            print("....\nProgram terminated....")
            break
