# Program to simulate traffic signal actions based on color input

while (1):
    colour = str (input("Enter the colour of traffic signal: "))
    if (colour == "red"):
        print("STOP!")
    elif (colour == "yellow"):
        print("GET READY!")
    elif (colour == "green"):
        print("GO!")
    elif (colour == "exit"):
        print("Program terminated!")
        break
    else:
        print("INVALID COLOUR!")
