# TIC TAC TOE GAME 

def display(board):
    
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

def player_marker():

    markers = {}
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("\nChoose a marker (X or O) : ").upper()
        
    if marker == 'X':
        markers["Player1"] = 'X'
        markers["Player2"] = 'O'
    else:
        markers["Player1"] = 'O'
        markers["Player2"] = 'X'
        
    print("\n" ,markers)   
    return markers

import random

def choose_player():
    return random.choice(["Player1" , "Player2"])

def place_marker(board , marker , position):
    board[position] = marker

def win_check(board , mark):
    
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))

def space_check(board , position):
    return board[position] == ' '

def full_check(board):
    
    for i in range(1,10):
        if space_check(board , i):
            return False
    return True

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board , position):
        try:
            position = int(input("\nEnter a position (1-9) : "))
        except:
            print("Please enter a number !")
            continue
        if position not in [1,2,3,4,5,6,7,8,9]:
            print("\nInvalid position ! Enter between 1 - 9 ")
        if not space_check(board , position):
            print("\nAlready occupied ! choose another position ! ")
            
    return position

def replay():
    
    w = ''
    wish = ['y' , 'n']
    while w not in wish:
         w = input("\nDo you want to play again ? (y / n) : ").lower()
         if w not in wish:
             print("\nI can't understand ! Please enter 'y' or 'n'")
    if w == 'y':
        return True
    if w == 'n':
        return False

print("\nWelcome to  TIC TAC TOE ")

while True:

    board = [' '] * 10

    print("\nBoard Positions :\n")
    placement = ['0','1','2','3','4','5','6','7','8','9']
    display(placement)

    player = choose_player()

    if player == "Player1":
        print("\nPlayer 1 will choose the marker first !")
    else:
        print("\nPlayer 2 will choose the marker first !")

    markers = player_marker()
    player = choose_player()

    if player == "Player1":
        print("\nPlayer 1 will play first !")
    else:
        print("\nPlayer 2 will play first !")

    play = input("\nAre you ready to play ? (y/n) ").lower()
    if play == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if player == "Player1":
            
            print("\nPlayer 1's turn")
            position = player_choice(board)
            place_marker(board , markers["Player1"] , position)
            print("\nCurrent board !\n")
            display(board)

            if win_check(board , markers["Player1"]):
                print("\nPlayer 1 won !")
                print("\nFinal board !\n")
                display(board)
                game_on = False
            else:
                if full_check(board):
                    print("\nIt's a draw")
                    print("\nFinal board !\n")
                    display(board)
                    game_on = False
                else:
                    player = "Player2"
        else:
            
                print("\nPlayer 2's turn")
                position = player_choice(board)
                place_marker(board , markers["Player2"] , position)
                print("\nCurrent board !\n")
                display(board)

                if win_check(board , markers["Player2"]):
                    print("\nPlayer 2 won !")
                    print("\nFinal board !\n")
                    display(board)
                    game_on = False
                else:
                    if full_check(board):
                        print("\nIt's a draw")
                        print("\nFinal board !\n")
                        display(board)
                        game_on = False
                    else:
                        player = "Player1"
    
    if not replay():
        break

print("\nThank you for playing ! Come again !")


        



