import random
guess_no = random.randint(1,100)
attempt = 0
iscontinue = True

print("\nWelcome to our number guessing game !")
print("\nAre you ready ?\n")
while iscontinue:

    n = int(input("Guess the number (1-100) : "))
    
    if n > 0 and n <= 100:
        attempt += 1
        if n == guess_no:
            
            print("\nCongrats ! You have guessed correctly !")
            print(f"\nAttempts : {attempt}")
            while True:
                choice = input("\nDo you want to continue ? (yes/no) : ").strip().upper()
                if choice == "YES":
                    guess_no = random.randint(1,100)
                    attempt = 0
                    iscontinue = True
                    print("\nNew number generated ! Try to guess it !\n")
                    break
                elif choice == "NO":
                    iscontinue = False
                    print("\nThank you for playing ! See you again !")
                    break
                else:
                    print("\nInvalid ! Enter a valid yes or no !")
                       
        elif abs(guess_no - n) < 10:
            print("You're too close !")
        elif abs(guess_no - n) < 30:
            print("You're close !")
        elif abs(guess_no - n) < 50:
            print("You're far !")
        elif abs(guess_no - n) >= 50:
            print("You're too far !")
                   
    else:
        print("\nInvalid ! Enter a number between 1 and 100")

        
        
        
