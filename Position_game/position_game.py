# Simple Python Position Game

def display(lst):
    print(f"\nHere is the current list : {lst}")

def position():
    choice = 'wrong'
    val = ['0' , '1' , '2']
    while choice not in val:
        choice = input("\nChoose a number (0/1/2) : ")
        if choice not in val:
            print("\nSorry ! Invalid choice")
    return int(choice)

def replacement(lst , place):
    s = input("\nEnter a new string to replace : ")
    lst[place] = s
    return lst

def gameon():
    o = 'wrong'
    option = ['Y' , 'N']
    while o not in option:     
        o = input("\nDo you want to keep playing ? ")
        if o not in option:
            print("Sorry ! I can't understand . Please enter 'Y' or 'N'")
    if o == 'Y':
        return True
    if o == 'N':
        return False

game_list = [0,1,2]
game_on = True

while game_on:

    display(game_list)

    choice = position()

    game_list = replacement(game_list , choice)

    display(game_list)

    game_on = gameon()
    
print("\nThank you for playing !")
